# Generated by Django 4.2 on 2023-04-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_amountalerts_survivormodel_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survivormodel',
            name='sex',
            field=models.CharField(max_length=1),
        ),
    ]