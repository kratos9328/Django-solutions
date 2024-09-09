#Yes, by default, Django signals run in the same database transaction as the caller.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        # Signal handler tries to add a group to the user
        group = Group.objects.create(name="testgroup")
        instance.groups.add(group)
        print("Signal handler: Group added to user")

try:
    with transaction.atomic():
        new_user = User.objects.create_user(username="testuser", password="password123")
        print("User created")
        # Simulate an error to trigger rollback
        raise Exception("Forcing transaction rollback")

except Exception as e:
    print(f"Exception: {e}")

# Check if the user and group were saved in the database
user_exists = User.objects.filter(username="testuser").exists()
group_exists = Group.objects.filter(name="testgroup").exists()

print(f"User exists after rollback? {user_exists}")
print(f"Group exists after rollback? {group_exists}")