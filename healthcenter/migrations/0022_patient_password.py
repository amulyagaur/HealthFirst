# Generated by Django 2.2.10 on 2020-05-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcenter', '0021_newsarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default='mnbvcxz1234', max_length=1000),
        ),
    ]
