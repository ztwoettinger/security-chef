# Generated by Django 3.2.16 on 2023-03-27 18:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20230327_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='target_repo_data',
        ),
        migrations.AddField(
            model_name='job',
            name='repo_url',
            field=models.URLField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='run_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 27, 18, 51, 51, 43226, tzinfo=utc)),
        ),
    ]
