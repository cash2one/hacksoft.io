# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 12:13
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_project_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()),), template='streams/project_description_paragraph.html')),)),
        ),
    ]
