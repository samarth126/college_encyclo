# Generated by Django 3.2.13 on 2022-08-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_auto_20220810_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='notes_unit',
            field=models.CharField(default=True, max_length=260),
        ),
    ]