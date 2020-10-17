# Generated by Django 2.2.6 on 2019-11-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcenter', '0009_auto_20191107_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.CharField(max_length=5000)),
                ('cleanliness', models.CharField(choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], max_length=100)),
                ('med_availability', models.CharField(choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], max_length=100)),
                ('staff_behaviour', models.CharField(choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], max_length=100)),
                ('overall_satisfaction', models.CharField(choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], max_length=100)),
                ('rating', models.IntegerField()),
                ('suggestion', models.CharField(max_length=5000)),
            ],
        ),
    ]
