# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_auto_20170622_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.User'),
        ),
    ]
