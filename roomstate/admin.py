from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import RoomState

class RoomStateAdmin(ModelAdmin):
    """ Roomstate admin """

    model = RoomState
    menu_label = "Raumzustand"
    menu_icon = "home"
    menu_order = 20
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("room_state",)

modeladmin_register(RoomStateAdmin)