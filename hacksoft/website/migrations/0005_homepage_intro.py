# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-23 12:10
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_ourteampage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=wagtail.wagtailcore.fields.StreamField((('h1', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('h2', wagtail.wagtailcore.blocks.RichTextBlock()), ('intro_image', wagtail.wagtailimages.blocks.ImageChooserBlock())), default=''),
            preserve_default=False,
        ),
    ]
