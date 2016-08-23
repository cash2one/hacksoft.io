from __future__ import unicode_literals
from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel


from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailsnippets.models import register_snippet

from modelcluster.fields import ParentalKey


class HomePage(Page):
    intro_h1 = models.CharField(max_length=255)
    intro_h2 = models.CharField(max_length=255)
    intro_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    how_we_work_title = models.CharField(max_length=255)
    how_we_work_center = RichTextField()
    how_we_work_left = RichTextField()
    how_we_work_right = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro_h1'),
        FieldPanel('intro_h2'),
        ImageChooserPanel('intro_image'),

        FieldPanel('how_we_work_title'),
        FieldPanel('how_we_work_center'),
        FieldPanel('how_we_work_left'),
        FieldPanel('how_we_work_right'),


        InlinePanel('teammate_placement', label="TeamMate"),

    ]


class HowWeWorkPage(Page):
    # STREAM FIELD
    pass



class TechnologiesWeUsePage(Page):
    pass


class OurTeamPage(Page):
    pass


@register_snippet
class Teammate(models.Model):
    name = models.CharField(max_length=255)
    initial_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    secondary_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('initial_photo'),
        ImageChooserPanel('secondary_photo'),
    ]

    def __str__(self):
        return self.name


class TeammatePlacement(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='teammate_placement')
    teammate = models.ForeignKey('website.Teammate', related_name='+')

    panels = [
        SnippetChooserPanel('teammate'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.teammate.name)