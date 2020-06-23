from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,default=1)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    rut = models.CharField(max_length=100, null=True, blank=True, verbose_name='Rut')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Apellido')
    mobile = models.CharField(max_length = 240,null=True, blank=True, verbose_name='Teléfono Celular')   
    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)