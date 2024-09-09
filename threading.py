#Yes, by default, Django signals run in the same thread as the caller.

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"Signal handler thread: {threading.current_thread().name} (ID: {threading.get_ident()})")

print(f"Caller thread: {threading.current_thread().name} (ID: {threading.get_ident()})")
new_user = User.objects.create_user(username="testuser", password="password123")