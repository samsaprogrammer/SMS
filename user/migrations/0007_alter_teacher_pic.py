# Generated by Django 5.0.6 on 2024-07-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_student_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='pic',
            field=models.FileField(upload_to='media'),
        ),
    ]