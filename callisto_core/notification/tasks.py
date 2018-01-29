import requests

from django.conf import settings

from callisto_core.celeryconfig import celery_app
from callisto_core.celeryconfig.tasks import CallistoCoreBaseTask


class _SendEmail(CallistoCoreBaseTask):

    def __init__(self):
        self.mailgun_post_route = f'https://api.mailgun.net/v3/{settings.APP_URL}/messages'

    def _send_email(self, email_data, email_attachments):
        request_params = {
            'auth': ('api', settings.MAILGUN_API_KEY),
            'data': {
                'from': f'"Callisto" <noreply@{settings.APP_URL}>',
                **email_data,
            },
            **email_attachments,
        }
        try:
            response = requests.post(self.mailgun_post_route, request_params)
        except Exception as exc:
            raise self.retry(exc=exc)
        return response


@celery_app.task(base=_SendEmail,
                 bind=True,
                 max_retries=5,
                 soft_time_limit=5)
def SendEmail(self, email_data, email_attachments):
    """Sends emails via the mailgun API"""
    response = self._send_email(email_data, email_attachments)
    return response
