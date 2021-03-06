# Generated by Django 3.1.2 on 2020-11-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_courseimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='text',
            field=models.TextField(blank=True, help_text='This uses markdown format', null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='timestamp',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='StepContent',
        ),
    ]
