# Generated by Django 3.1.5 on 2021-01-13 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_experience_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
