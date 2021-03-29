from django.db import models
from django.utils import timezone
import datetime

""" New model for Room status as multiple choice """
class RoomState(models.Model):
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

    room_state = models.CharField(
        'Raumzustand',
        max_length = 3,
        choices = ROOM_STATE_CHOICES,
        default = OPEN,
    )

    publication_date = models.DateTimeField('Erstelldatum', default=timezone.now())


    def where_room_state(self):
        return self.room_state
