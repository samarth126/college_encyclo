# Generated by Django 3.2.13 on 2022-07-23 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20220723_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='status',
        ),
    ]