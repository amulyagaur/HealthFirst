# Generated by Django 2.2.10 on 2020-05-28 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcenter', '0025_opdregistration_is_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='sentiment',
            field=models.CharField(default='Positive', max_length=50),
        ),
    ]
