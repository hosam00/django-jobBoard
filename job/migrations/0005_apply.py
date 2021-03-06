# Generated by Django 3.0.8 on 2020-09-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20200904_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('cover_letter', models.TextField(max_length=500)),
            ],
        ),
    ]
