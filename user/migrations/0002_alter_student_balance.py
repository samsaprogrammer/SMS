# Generated by Django 5.0.6 on 2024-07-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='balance',
            field=models.IntegerField(),
        ),
    ]
