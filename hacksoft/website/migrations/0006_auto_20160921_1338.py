# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-21 13:38
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20160920_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='howweworkpage',
            name='the_process_content',
            field=wagtail.wagtailcore.fields.StreamField((('process_content', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('icon_classes', wagtail.wagtailcore.blocks.CharBlock()), ('description', wagtail.wagtailcore.blocks.RichTextBlock())), template='streams/process_content.html')),)),
        ),
    ]
