# Generated by Django 3.0.8 on 2020-09-04 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='job.Job'),
            preserve_default=False,
        ),
    ]
