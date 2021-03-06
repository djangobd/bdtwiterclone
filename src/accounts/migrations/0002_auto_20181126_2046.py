# Generated by Django 2.1.3 on 2018-11-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_cover',
            field=models.ImageField(blank=True, default='images/default_cover.png', null=True, upload_to='photos', verbose_name='profile cover'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/default_profile.png', null=True, upload_to='photos', verbose_name='profile picture'),
        ),
    ]
