# Generated by Django 3.2.13 on 2022-08-12 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_auto_20220812_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=110)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.department')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.program')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.year')),
            ],
        ),
    ]
