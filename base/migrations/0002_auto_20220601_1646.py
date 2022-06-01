# Generated by Django 3.2.13 on 2022-06-01 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.CharField(max_length=110)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=250)),
                ('university', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=110)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=110)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('FIRST', 'First Year'), ('SECOND', 'Second Year'), ('THIRD', 'Third Year'), ('FOURTH', 'Fourth Year')], max_length=110)),
            ],
        ),
        migrations.CreateModel(
            name='Staffadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.club')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.college')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.department')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.program')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.year')),
            ],
        ),
        migrations.CreateModel(
            name='Qpaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qpaper_subject', models.CharField(max_length=265)),
                ('qpaper_college', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.college')),
                ('qpaper_dept', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.department')),
                ('qpaper_year', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.year')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.college')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.department')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.program')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.year')),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=265)),
                ('qpaper_dept', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.department')),
                ('qpaper_year', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.year')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=225)),
                ('notice_date', models.DateTimeField()),
                ('notice_desc', models.CharField(max_length=225)),
                ('notice_college', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.college')),
                ('notice_dept', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.department')),
                ('notice_year', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.year')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes_subject', models.CharField(max_length=265)),
                ('notes_college', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.college')),
                ('notes_dept', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.department')),
                ('notes_year', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.year')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=110)),
                ('date_time', models.DateTimeField()),
                ('tg_audience', models.CharField(max_length=225)),
                ('event_desc', models.CharField(max_length=700)),
                ('venue', models.CharField(max_length=200)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.college')),
            ],
        ),
        migrations.CreateModel(
            name='Event_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.events')),
                ('eventuser', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.profile')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='base.program'),
        ),
    ]
