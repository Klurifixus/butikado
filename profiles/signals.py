from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from butikado.utils.mail_utils import send_mailgun_email
from django.conf import settings  # Import settings

@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    subject = "Welcome to Earns Shop!"
    message = (
        f"Hi {user.get_full_name() or user.username}, "
        "welcome to Earns Shop! Thank you for signing up with us."
    )
    to_email = user.email
    from_email = settings.DEFAULT_FROM_EMAIL  # Use the email from settings
    
    send_mailgun_email(subject, message, [to_email], from_email)
