# Generated by Django 4.2.7 on 2024-01-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='email',
            field=models.EmailField(default='bharat@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='school',
            name='renteremail',
            field=models.EmailField(default='bharat@gmail.com', max_length=254),
        ),
    ]
