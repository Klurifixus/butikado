from django.core.mail.backends.base import BaseEmailBackend

from .mail_utils import send_mailgun_email


class MailgunEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        """
        Send emails, one by one, to Mailgun API.
        """
        if not email_messages:
            return

        num_sent = 0
        for message in email_messages:
            response = send_mailgun_email(
                subject=message.subject,
                message=message.body,
                to_email=message.to[0],
                from_email=message.from_email,
            )
            if response.status_code == 200:
                num_sent += 1

        return num_sent
