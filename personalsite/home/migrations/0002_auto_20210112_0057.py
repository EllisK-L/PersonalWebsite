# Generated by Django 3.1.5 on 2021-01-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='heading',
            field=models.CharField(max_length=300),
        ),
    ]
