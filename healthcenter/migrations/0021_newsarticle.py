# Generated by Django 2.2.10 on 2020-05-05 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcenter', '0020_patient_emailid'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]
