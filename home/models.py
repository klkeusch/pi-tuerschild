from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


# """ New model for Room status as multiple choice """
# class RoomStatus(models.Model):
#     DONOTDISTURB = 'DND'
#     OPEN = 'OPN'
#     CLOSED = 'CLS'

#     ROOM_STATUS_CHOICES = [
#         (DONOTDISTURB, 'Do not disturb!'),
#         (OPEN, 'We are open!'),
#         (CLOSED, 'We are closed!'),
#     ]

#     room_status = models.CharField(
#         max_length = 3,
#         choices = ROOM_STATUS_CHOICES,
#         default = OPEN,
#     )

#     def where_room_status(self):
#         return self.room_status

DONOTDISTURB = 'DND'
OPEN = 'OPN'
CLOSED = 'CLS'
AWAY = 'BRB'

ROOM_STATE_CHOICES = [
    (DONOTDISTURB, 'Bitte nicht stören!'),
    (OPEN, 'Wir haben geöffnet!'),
    (CLOSED, 'Wir haben geschlossen!'),
    (AWAY, 'Wir haben gleich wieder geöffnet!')
]

class HomePage(Page):
    """ Home page model. """
    max_count = 1



    template = "home/home_page.html"

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,#False, 
        on_delete=models.SET_NULL, 
        related_name="+",
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name="+",
    )

    room_state = models.CharField(
        'Raumzustand',
        max_length = 3,
        choices = ROOM_STATE_CHOICES,
        default = OPEN,
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        #ImageChooserPanel("banner_image"),
        #PageChooserPanel("banner_cta"),
        FieldPanel("room_state"),
    ]

    class RoomStateChoice(models.Model):


        room_state = models.CharField(
            'Raumzustand',
            max_length = 3,
            choices = ROOM_STATE_CHOICES,
            default = OPEN,
        )

        def __str__(self):
            return self.room_state
        
        def where_room_state(self):
            return self.room_state

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
