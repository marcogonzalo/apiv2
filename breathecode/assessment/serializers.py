from breathecode.utils import serpy
from breathecode.utils.i18n import translation
from breathecode.admissions.models import Academy
from .models import Assessment, Question, Option, UserAssessment, Answer
from breathecode.marketing.models import AcademyAlias
from rest_framework import serializers
from django.utils import timezone
from breathecode.utils.datetime_integer import from_now, duration_to_str
from breathecode.utils.validation_exception import ValidationException


class UserSerializer(serpy.Serializer):
    id = serpy.Field()
    first_name = serpy.Field()
    last_name = serpy.Field()


class AcademySmallSerializer(serpy.Serializer):
    id = serpy.Field()
    slug = serpy.Field()
    name = serpy.Field()


class AssessmentSmallSerializer(serpy.Serializer):
    id = serpy.Field()
    slug = serpy.Field()
    title = serpy.Field()


class QuestionSmallSerializer(serpy.Serializer):
    id = serpy.Field()
    title = serpy.Field()
    question_type = serpy.Field()
    is_deleted = serpy.Field()
    position = serpy.Field()


class OptionSmallSerializer(serpy.Serializer):
    id = serpy.Field()
    title = serpy.Field()
    score = serpy.Field()


class AnswerSmallSerializer(serpy.Serializer):
    id = serpy.Field()
    option = OptionSmallSerializer()
    question = QuestionSmallSerializer()
    value = serpy.Field()


class GetAssessmentLayoutSerializer(serpy.Serializer):
    slug = serpy.Field()
    additional_styles = serpy.Field()
    variables = serpy.Field()
    created_at = serpy.Field()
    academy = AcademySmallSerializer()


class GetAssessmentThresholdSerializer(serpy.Serializer):
    success_next = serpy.Field()
    fail_next = serpy.Field()
    success_message = serpy.Field()
    fail_message = serpy.Field()
    score_threshold = serpy.Field()
    assessment = AssessmentSmallSerializer()


class GetOptionSerializer(serpy.Serializer):
    id = serpy.Field()
    title = serpy.Field()
    help_text = serpy.Field()
    score = serpy.Field()
    position = serpy.Field()


class GetQuestionSerializer(serpy.Serializer):
    id = serpy.Field()
    title = serpy.Field()
    position = serpy.Field()
    help_text = serpy.Field()
    question_type = serpy.Field()

    options = serpy.MethodField()

    def get_options(self, obj):
        return GetOptionSerializer(obj.option_set.filter(is_deleted=False), many=True).data


class GetAssessmentSerializer(serpy.Serializer):
    id = serpy.Field()
    slug = serpy.Field()
    title = serpy.Field()
    lang = serpy.Field()
    private = serpy.Field()
    translations = serpy.MethodField()

    def get_translations(self, obj):
        if obj.translations is None:
            return []
        return [t.lang for t in obj.translations.all()]


class SmallUserAssessmentSerializer(serpy.Serializer):
    id = serpy.Field()
    title = serpy.Field()

    assessment = AssessmentSmallSerializer()

    owner = UserSerializer(required=False)
    owner_email = serpy.Field()

    total_score = serpy.Field()

    started_at = serpy.Field()
    finished_at = serpy.Field()

    created_at = serpy.Field()


class GetUserAssessmentSerializer(serpy.Serializer):
    id = serpy.Field()
    token = serpy.Field()
    title = serpy.Field()
    lang = serpy.Field()

    academy = AcademySmallSerializer(required=False)
    assessment = AssessmentSmallSerializer()

    owner = UserSerializer(required=False)
    owner_email = serpy.Field()
    owner_phone = serpy.Field()

    status = serpy.Field()
    status_text = serpy.Field()

    conversion_info = serpy.Field()
    total_score = serpy.Field()
    comment = serpy.Field()

    started_at = serpy.Field()
    finished_at = serpy.Field()

    created_at = serpy.Field()


class GetAssessmentBigSerializer(GetAssessmentSerializer):
    questions = serpy.MethodField()
    is_instant_feedback = serpy.Field()

    def get_questions(self, obj):
        return GetQuestionSerializer(obj.question_set.filter(is_deleted=False).order_by('-position', 'id'),
                                     many=True).data


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        exclude = ('created_at', 'updated_at')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = ('created_at', 'updated_at', 'assessment')


class AnswerSerializer(serializers.ModelSerializer):
    token = serializers.CharField()

    class Meta:
        model = Answer
        exclude = ('created_at', 'updated_at')

    def validate(self, data):

        lang = self.context['lang']
        validated_data = {**data}
        del validated_data['token']

        uass = UserAssessment.objects.filter(token=data['token']).first()
        if not uass:
            raise ValidationException(
                translation(lang,
                            en=f'user assessment not found for this token',
                            es=f'No se han encontrado un user assessment con ese token',
                            slug='not-found'))
        validated_data['user_assessment'] = uass

        now = timezone.now()
        session_duration = uass.created_at
        max_duration = uass.created_at + uass.assessment.max_session_duration
        if now > max_duration:
            raise ValidationException(
                f'User assessment session started {from_now(session_duration)} ago and it expires after {duration_to_str(uass.assessment.max_session_duration)}, no more updates can be made'
            )

        if 'option' in data and data['option']:
            if Answer.objects.filter(option=data['option'], user_assessment=uass).count() > 0:
                raise ValidationException(
                    translation(lang,
                                en=f'This answer has already been answered on this user assessment',
                                es=f'Esta opción ya fue respondida para este assessment',
                                slug='already-answered'))

        return super().validate(validated_data)

    def create(self, validated_data):

        # copy the validated data just to do small last minute corrections
        data = validated_data.copy()

        if 'option' in data and data['option']:
            data['question'] = data['option'].question

            if data['question'].question_type == 'SELECT':
                data['value'] = data['option'].score

        return super().create({**data})


class AssessmentPUTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assessment
        exclude = ('slug', 'academy', 'lang', 'author')


class PostUserAssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAssessment
        exclude = ('total_score', 'created_at', 'updated_at', 'token')
        read_only_fields = ['id']

    def validate(self, data):

        academy = None
        if 'academy' in data:
            academy = data['academy']
        else:
            if 'assessment' not in data:
                raise ValidationException(
                    'No academy or assessment property found to determine academy ownership of this userassessment')

            academy = data['assessment'].academy

        return super().validate({**data, 'academy': academy})

    def create(self, validated_data):

        # copy the validated data just to do small last minute corrections
        data = validated_data.copy()

        if data['academy'] is None:
            data['status'] = 'ERROR'
            data['status_text'] = 'Missing academy. Maybe the assessment.academy is null?'

        # "us" language will become "en" language, its the right lang code
        if 'lang' in data and data['lang'] == 'us':
            data['lang'] = 'en'

        if 'started_at' not in data:
            data['started_at'] = timezone.now()

        result = super().create({**data, 'total_score': 0, 'academy': validated_data['academy']})
        return result


class PUTUserAssessmentSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)

    class Meta:
        model = UserAssessment
        exclude = ('academy', 'assessment', 'lang', 'total_score', 'token')
        read_only_fields = [
            'id',
            'academy',
        ]

    def update(self, instance, validated_data):

        now = timezone.now()
        session_duration = instance.created_at
        max_duration = instance.created_at + instance.assessment.max_session_duration
        if now > max_duration:
            raise ValidationException(
                f'Session started {from_now(session_duration)} ago and it expires after {duration_to_str(instance.assessment.max_session_duration)}, no more updates can be made'
            )

        # copy the validated data just to do small last minute corrections
        data = validated_data.copy()

        # "us" language will become "en" language, its the right lang code
        if 'lang' in data and data['lang'] == 'us':
            data['lang'] = 'en'

        if 'started_at' not in data and instance.started_at is None:
            data['started_at'] = now

        return super().update(instance, data)
