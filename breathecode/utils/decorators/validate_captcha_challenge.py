import logging
import os

from rest_framework.views import APIView

from breathecode.services.google_cloud import Recaptcha
from breathecode.utils.exceptions import ProgrammingError

from ..validation_exception import ValidationException

logger = logging.getLogger(__name__)
__all__ = ['validate_captcha_challenge']


def validate_captcha_challenge(function):

    def wrapper(*args, **kwargs):
        try:
            if hasattr(args[0], '__class__') and isinstance(args[0], APIView):
                data = args[1].data.copy()

            elif hasattr(args[0], 'user') and hasattr(args[0].user, 'has_perm'):
                data = args[0].data.copy()

            # websocket support
            elif hasattr(args[0], 'ws_request'):
                data = args[0].data.copy()

            else:
                raise IndexError()

            apply_captcha = os.getenv('APPLY_CAPTCHA', False)
            print('apply_captcha')
            print(apply_captcha)

            logger.info('CAPTCHA DECORATOR')
            print('CAPTCHA DECORATOR')
            logger.info('apply_captcha')
            print(apply_captcha)

            if not apply_captcha:
                return function(*args, **kwargs)

            logger.info('VERIFYING THE CAPTCHA')
            print('VERIFYING THE CAPTCHA')

            project_id = os.getenv('GOOGLE_PROJECT_ID', '')

            site_key = os.getenv('GOOGLE_CAPTCHA_KEY', '')

            token = data['token'] if 'token' in data else None

            recaptcha_action = data['action'] if 'action' in data else None

            recaptcha = Recaptcha()
            response = recaptcha.create_assessment(project_id=project_id,
                                                   recaptcha_site_key=site_key,
                                                   token=token,
                                                   recaptcha_action=recaptcha_action)

            print('response')
            print(response)
            logger.info('response risk_analysis score')
            logger.info(response.risk_analysis.score)
            print('response risk_analysis score')
            print(response.risk_analysis.score)

            if (response.risk_analysis.score < 0.8):
                raise ValidationException('The action was denied because it was considered suspicious', code=429)

        except IndexError:
            raise ProgrammingError('Missing request information, use this decorator with DRF View')

        return function(*args, **kwargs)

    return wrapper
