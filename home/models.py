from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from django.utils.html import format_html

DONOTDISTURB = "DND"
OPEN = "OPN"
CLOSED = "CLS"
AWAY = "BRB"

ROOM_STATE_CHOICES = [
    (DONOTDISTURB, "Bitte nicht stören!"),
    (OPEN, "Wir haben geöffnet!"),
    (CLOSED, "Wir haben geschlossen!"),
    (AWAY, "Wir haben gleich wieder geöffnet!"),
]


class HomePage(Page):
    """ Home page model. """
    max_count = 1

    template = "home/home_page.html"

    banner_title = models.CharField(
        "Nachricht des Tages",
         max_length=100,
         blank=True,
         null=False,
    )

    banner_subtitle = RichTextField(
        "Details zur Nachricht des Tages",
        features=[
            "bold",
            "italic",
            "h2",
            "h3",
            "hr",
        ],
        max_length = 255,
        blank=True,
        null=False,
    )

    room_state = models.CharField(
        "Raum-Status",
        max_length=3,
        choices=ROOM_STATE_CHOICES,
        default=OPEN,
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("room_state"),
    ]

    class Meta:
        """ Meta informations. """

        verbose_name = "Homepage"
        verbose_name_plural = "Homepages"
