# Generated by Django 3.2.9 on 2021-12-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0004_auto_20211202_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='link',
        ),
        migrations.AddField(
            model_name='track',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
