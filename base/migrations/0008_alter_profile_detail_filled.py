# Generated by Django 3.2.13 on 2022-07-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_profile_detail_filled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='detail_filled',
            field=models.BooleanField(default=False),
        ),
    ]
