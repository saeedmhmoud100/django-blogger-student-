from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    image = models.ImageField(default='defalte.png', upload_to='profile_pick')
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        return '{} profile'.format(self.user.username)