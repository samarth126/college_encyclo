# Generated by Django 3.2.13 on 2022-07-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_notice_notice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice_date',
            field=models.DateTimeField(),
        ),
    ]