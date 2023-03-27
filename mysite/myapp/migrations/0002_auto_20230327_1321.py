# Generated by Django 3.2.16 on 2023-03-27 17:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_repo_data', models.JSONField()),
                ('status', models.BooleanField(default=False)),
                ('run_date', models.DateTimeField(default=datetime.datetime(2023, 3, 27, 17, 21, 19, 55477, tzinfo=utc))),
            ],
        ),
        migrations.DeleteModel(
            name='Jobs',
        ),
    ]
