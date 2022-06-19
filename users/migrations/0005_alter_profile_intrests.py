# Generated by Django 3.2 on 2021-05-01 09:52

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210501_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='intrests',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('c', 'Coding'), ('r', 'Reading'), ('t', 'Trading'), ('g', 'Gaming')], max_length=4),
        ),
    ]
