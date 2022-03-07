# Generated by Django 3.2.9 on 2022-02-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220226_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.AddField(
            model_name='profile',
            name='gender_f',
            field=models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], default='male', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='mail_agreement',
            field=models.BooleanField(default=False),
        ),
    ]
