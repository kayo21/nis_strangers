# Generated by Django 3.2.9 on 2021-11-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_auto_20211111_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
