from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from butikado.utils.mail_utils import send_mailgun_email

@receiver(user_signed_up)
def send_welcome_email(request, user, **kwargs):
    subject = "Welcome to Earns Shop!"
    message = f"Hi {user.get_full_name() or user.username}, welcome to Earns Shop! Thank you for signing up with us."
    to_email = user.email
    from_email = "pirrefixus@gmail.com"  # Replace with your actual email
    
    send_mailgun_email(subject, message, [to_email], from_email)