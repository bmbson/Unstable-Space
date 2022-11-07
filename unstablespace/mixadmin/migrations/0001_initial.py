# Generated by Django 4.1.1 on 2022-10-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MixModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='')),
                ('audio', models.FileField(upload_to='')),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
    ]