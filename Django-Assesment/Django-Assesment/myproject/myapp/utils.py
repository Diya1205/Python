from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(recipient_email, subject, message):
    """
    Sends an email using the settings configured in settings.py.
    """
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False