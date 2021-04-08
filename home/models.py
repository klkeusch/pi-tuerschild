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
        "Nachricht des Tages", max_length=100, blank=False, null=True
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
    )

    """ Not being used """
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,  # False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    """Not being used """
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
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
        # ImageChooserPanel("banner_image"),
        # PageChooserPanel("banner_cta"),
        FieldPanel("room_state"),
    ]

    def room_state_colored(self, obj):
        color = 'white'
        if obj.room_state == 'DND':
            color = 'red'
        return format_html('<b style="background:{} !important;">{}</b>', colors, obj.room_state)

    class Meta:
        """ Meta informations. """

        verbose_name = "Homepage"
        verbose_name_plural = "Homepages"
