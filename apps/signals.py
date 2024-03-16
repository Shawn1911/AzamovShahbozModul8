from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to our platform!',
            'Thank you for registering.',
            'azamovshahboz06082001@example.com',  # Sender's email address
            [instance.email],  # Recipient's email address
            fail_silently=False,
        )
