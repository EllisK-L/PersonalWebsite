# Generated by Django 3.1.5 on 2021-01-12 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210112_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='home'),
        ),
    ]
