#Q1By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet 
that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


#Django signals are executed synchronously, eg
# signals.py
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        print("Signal received: Starting delay...")
        time.sleep(5)  # Simulating a delay
        print("Signal processed: Finished delay after 5 seconds.")

new_user = User.objects.create_user(username="testuser", password="password123")
print("User created.")

#The signal handler (user_post_save) will block execution by sleeping for 5 seconds.
