# Generated by Django 4.1.1 on 2023-02-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixadmin', '0007_alter_mixmodel_date_alter_mixmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mixmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]