# Generated by Django 3.2.13 on 2022-08-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_auto_20220812_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='notes_subject',
            field=models.CharField(max_length=265),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
