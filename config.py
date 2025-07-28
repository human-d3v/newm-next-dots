from __future__ import annotations
from typing import Callable, Any

import os
import pwd
import time
import logging

from newm.layout import Layout
from newm.helper import BacklightManager, WobRunner, PaCtl

from pywm import (
    PYWM_MOD_LOGO,
    PYWM_MOD_ALT,
    PYWM_TRANSFORM_90,
    PYWM_TRANSFORM_180,
    PYWM_TRANSFORM_270,
    PYWM_TRANSFORM_FLIPPED,
    PYWM_TRANSFORM_FLIPPED_90,
    PYWM_TRANSFORM_FLIPPED_180,
    PYWM_TRANSFORM_FLIPPED_270,
)

logger = logging.getLogger(__name__)


# =========== systemd integration, start & reconfig services ===============
theme = "Orchis Dark Green"
icon_theme = "Tela-Manjaro"
cursor_theme = "Volantes"
font = "Monaspace Argon 11"
set_interface = "gsettings set org.gnome.desktop.interface"
set_peripheral = "gsettings set org.gnome.desktop.peripherals"


def on_startup():
    # list services and loop through them to spawn each one
    # https://github.com/newm-next/newm-next/blob/master/doc/tips_and_tricks.md
    services = [
        "systemctl --user import-environment DISPLAY WAYLAND_DISPLAY \
            XDG_CURRENT_DESKTOP",
        "hash dbus-update-activation-environment 2>/dev/null && \
            dbus-update-activation-environment --systemd \
            DISPLAY WAYLAND_DISPLAY XDG_CURRENT_DESKTOP",
        "/usr/lib/xfce-polkit/xfce-polkit",
        f"{set_interface} gtk-theme {theme}",
        f"{set_interface} icon-theme {icon_theme}",
        f"{set_interface} cursor-theme {cursor_theme}",
        f"{set_interface} font-name {font}",
        "thunar --daemon",
        "nm-applet --indicator"
    ]

    for s in services:
        service = f"{s} &"
        os.system(service)


def on_reconfigure():
    # https://github.com/newm-next/newm-next/blob/master/doc/look_and_feel.md
    services = [
        f"{set_interface} gtk-theme {theme}",
        f"{set_interface} icon-theme {icon_theme}",
        f"{set_interface} cursor-theme {cursor_theme}",
        f"{set_interface} font-name {font}",
        f"{set_peripheral}.keyboard repeat-interval 30",
        f"{set_peripheral}.keyboard delay 500",
        f"{set_peripheral}.mouse natural-scroll true",
        f"{set_peripheral}.mouse speed 0.0",
        f"{set_peripheral}.mouse accel-profile 'default'",
        f"{set_peripheral}.touchpad natural-scroll true",
        f"{set_peripheral}.touchpad speed 0.0",
        "gsettings set org.gnome.desktop.wm.preferences button-layout :",
    ]

    for s in services:
        service = f"{s} &"
        os.system(service)


# ======== screen dimensions ==============================================
outputs = [
    {'name': 'eDP-1', 'scale': 1.0, 'width': 1920, 'height': 1080, 'mHz': 60,
     'pos_x': 0, 'pos_y': 0, 'anim': True},
]


# ============= pywm settings =============================================
# https://github.com/newm-next/newm-next/blob/master/doc/config.md
pywm = {
        'enable_xwayland': True,
        'xkb_model': "",
        'xkb_layout': "",
        'xkb_options': "caps:ctrl_modifier, ctrl:swap_lwin_lctl",  # custom
        'xcursor_theme': cursor_theme,
        'xcursor_size': 14,
        'tap_to_click': True,
        'natural_scroll': True,
        'focus_follows_mouse': True,
        'constrain_popups_to_toplevel': True,
        'encourage_csd': False,  # disable client side decorations
        'debug': False,
        'shaders': 'basic',
        'renderer_mode': 'pywm',  # enable pywm (alternative is wlr)
}

# ============== general appearance settings ==============================
# https://github.com/newm-next/newm-next/blob/master/doc/config.md
# -- set background
background = {
    'path': os.environ["HOME"] +
    "/.config/newm_next_dots/wallpaper/red_rocks.jpg",
    'time_scale': 0.15,  # time scale of background movement
    'anim': True,
}
# -- other settings
blend_time = 1.0  # time in seconds to blend in and out at startup & shutdown
anim_time = 0.10  # time in seconds for all animations (default is .3 == too slow)
corner_radius = 8

# ============= view settings ============================================
# first, define rules:
# https://github.com/newm-next/newm-next/blob/master/doc/tips_and_tricks.md
def rules(view):
    common_rules = {
        "float": True,
        "float_size": (750, 750),
        "float_pos": (0.5, 0.35)
    }
    float_apps = ("rofi-Networks", "Rofi", "nm-connection-editor")

    if view.app_id in float_apps:
        return common_rules
