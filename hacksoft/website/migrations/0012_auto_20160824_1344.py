# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-24 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('website', '0011_auto_20160824_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='howweworkpage',
            name='header_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='howweworkpage',
            name='how_we_work_intro',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='howweworkpage',
            name='the_process_content',
            field=wagtail.wagtailcore.fields.StreamField((('title', wagtail.wagtailcore.blocks.RichTextBlock()), ('description', wagtail.wagtailcore.blocks.RichTextBlock())), default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='howweworkpage',
            name='the_process_title',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='howweworkpage',
            name='what_we_do_content',
            field=wagtail.wagtailcore.fields.StreamField((('title', wagtail.wagtailcore.blocks.RichTextBlock()), ('description', wagtail.wagtailcore.blocks.RichTextBlock())), default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='howweworkpage',
            name='what_we_do_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='howweworkpage',
            name='what_we_do_title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
