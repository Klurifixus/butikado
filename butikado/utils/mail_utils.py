import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def send_mailgun_email(subject, message, to_email, from_email):

    MAILGUN_API_KEY = settings.MAILGUN_API_KEY
    MAILGUN_DOMAIN = settings.MAILGUN_DOMAIN
    MAILGUN_API_URL = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"

    response = requests.post(
        MAILGUN_API_URL,
        auth=("api", MAILGUN_API_KEY),
        data={"from": from_email, "to": to_email, "subject": subject, "text": message},
    )

    if response.status_code != 200:
        logger.error(
            f"Failed to send email: {response.status_code} {response.reason} {response.text}"
        )
    else:
        logger.error("Failed to send email: " + response.text)

    return response
