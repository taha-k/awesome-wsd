# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awesomegames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighestScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highestScore', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='developer',
            name='likes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_developer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='awesomegames.Developer'),
        ),
        migrations.AlterField(
            model_name='game',
            name='thumbnail_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='highestscore',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awesomegames.Game'),
        ),
        migrations.AddField(
            model_name='highestscore',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awesomegames.Player'),
        ),
    ]
