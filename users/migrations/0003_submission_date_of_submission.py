# Generated by Django 3.2.7 on 2021-12-05 04:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211203_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='date_of_submission',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
