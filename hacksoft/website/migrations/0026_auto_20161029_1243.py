# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-29 12:43
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_footer_footerlinks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FooterLinks',
        ),
        migrations.AddField(
            model_name='footer',
            name='links',
            field=wagtail.wagtailcore.fields.StreamField((('link', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock())))),), default=''),
            preserve_default=False,
        ),
    ]
