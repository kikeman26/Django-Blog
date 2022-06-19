from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_resized import ResizedImageField
from multiselectfield import MultiSelectField


class Profile(models.Model):

    gender_choices = [('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHER')]
    country_choices = [('mexico', 'Mexico'), ('argentina', 'Argentina'), ('colombia', 'Colombia')]
    intrests_choices = [('c', 'Coding'), ('r', 'Reading'), ('t', 'Trading'), ('g', 'Gaming')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ResizedImageField(size=[300, 300], default='default_profile.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=1, choices=gender_choices, default='M')
    country = models.CharField(max_length=15, choices=country_choices, default='Mexico')
    intrests = MultiSelectField(choices=intrests_choices, max_choices=4)

    def __str__(self):
        return f'{self.user.username} Profile'

