from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
# Create your models here.

class Profile(models.Model):
    image = models.ImageField(default='defalte.png', upload_to='profile_pick')
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        return '{} profile'.format(self.user.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path) 

def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)