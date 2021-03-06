# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('website', '0021_project_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='team_image_main',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='team_imate_secodnary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
