# Generated by Django 3.1.5 on 2021-01-13 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_experience_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
