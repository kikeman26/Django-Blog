# Generated by Django 3.2 on 2021-05-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(choices=[('india', 'India'), ('america', 'America'), ('china', 'China')], default='india', max_length=7),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHER')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='intrests',
            field=models.CharField(default='c', max_length=4),
        ),
    ]
