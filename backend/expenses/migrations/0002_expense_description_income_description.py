# Generated by Django 4.1.7 on 2023-04-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='income',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]