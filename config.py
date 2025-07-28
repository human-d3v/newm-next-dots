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
