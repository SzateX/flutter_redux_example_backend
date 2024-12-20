# Generated by Django 5.1.4 on 2024-12-12 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=100)),
                ('room_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('surname', models.CharField(max_length=160)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferenceAPI.place')),
                ('speakers', models.ManyToManyField(related_name='lectures', to='conferenceAPI.speaker')),
            ],
        ),
    ]
