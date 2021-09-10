from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import User,Profile
from django.contrib.auth.models import Group



@receiver(post_save,sender=User)
def User_Profile_group_Creation(sender,instance,created,**kwargs):
    if created:
        user_group,created = Group.objects.get_or_create(name='user')
        instance.groups.add(user_group)
        Profile.objects.create(user = instance)
