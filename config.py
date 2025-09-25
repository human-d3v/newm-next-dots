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
        "/usr/libexec/xfce-polkit"
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
        # 'debug': False, # this will throw a weird error
        'shaders': 'basic',
        'renderer_mode': 'pywm',  # enable pywm (alternative is wlr)
}

# ============== general appearance settings ==============================
# https://github.com/newm-next/newm-next/blob/master/doc/config.md
# -- set background
background = {
    'path': os.environ["HOME"] +
    "/Pictures/wallpaper/zion.jpg",
    'time_scale': 0.15,  # time scale of background movement
    'anim': True,
}
# -- other settings
blend_time = 1.0  # time in seconds to blend in and out at startup & shutdown
anim_time = 0.10  # time in seconds for all animations (default is .3 == slow)
corner_radius = 8


# ============= view settings ============================================
# first, define rules:
# https://github.com/newm-next/newm-next/blob/master/doc/tips_and_tricks.md
def rules(view):
    blur_rules = {"blur": {"radius": 6, "passes": 4}}
    float_rules = {
        "float": True,
        "float_size": (750, 750),
        "float_pos": (0.5, 0.35)
    }
    float_app_ids = ("foot", "newm-next-launcher")
    blur_app_ids = ("foot", "newm-next-launcher")
    if view.app_id in blur_app_ids:
        return blur_rules
    if view.app_id in float_app_ids:
        return float_rules


# https://github.com/newm-next/newm-next/blob/master/doc/config.md
view = {
    'corner_radius': 8,
    'padding': 4,   # padding around windows
    'fullscreen_padding': 0,
    'ssd': {   # server-side decorations
        'enabled': False,
        'color': '#BEBEBEFF',
        'width': 2,
    },
    'send_fullscreen': True,
    'accept_fullscreen': True,
    'floating_min_size': False,
    'rules': rules,  # rules from above
    'debug-scaling': True,  # helps diagnose scaling issues
    'border_ws_switch': 75,  # px threshold before view changes into new output
}

interpolation = {  # size adjustments during gestures timeframe
    'size_adjustment': .4  # (.1 == start of anim., .9 == end)
}


# ============ focus settings ============================================
focus = {
    'enabled': True,
    'color': "#3ec760FF",
    # 'gradient': {         # for gradient on focused border
    #     'primary': "",
    #     'secondary': "",
    #     'angle': "",
    # },
    'distance': 4,  # distance to the view
    'width': 2,     # width of border
    'animate_on_change': True,  # animation
    'anim_time': 0.10,
}

# ============= behavior, keys, gestures =================================
# -- scripts
term = '~/.config/newm/scripts/ghostty.sh'
backup_term = 'alacritty'
waybar = '~/.config/newm/scripts/waybar.sh'
launcher = '~/.config/newm/scripts/launcher.sh'
network = '~/.config/newm/scripts/network.sh'
powermenu = '~/.config/dotfiles/scripts/rofi/powermenu.sh'
screenshot = '~/.config/newm/scripts/screenshot.sh'
brightness = '~/.config/dotfiles/scripts/brightness.sh'
volume = '~/.config/dotfiles/scripts/volume.sh'


def key_bindings(layout: Layout) -> list[tuple[str, Callable[[], Any]]]:
    return [
        # == terminal and backup
        ("L-Return", lambda: os.system(f"{term} &")),
        ("L-A-Return", lambda: os.system(f"{backup_term} &")),

        # == restart waybar
        ("L-w", lambda: os.system(f"{waybar} &")),

        # == file manager
        ("L-f", lambda: os.system("thunar &")),

        # == browser
        ("L-b", lambda: os.system("vivaldi &")),

        # == launcher
        ("L-e", lambda: os.system(f"{launcher} &")),
        ("L-n", lambda: os.system(f"{network} &")),
        ("L-q", lambda: os.system(f"{powermenu} &")),

        # == navigation -> vim bindings
        # ==== focus
        ("L-h", lambda: layout.move(-1, 0)),
        ("L-j", lambda: layout.move(0, 1)),
        ("L-k", lambda: layout.move(0, -1)),
        ("L-l", lambda: layout.move(1, 0)),

        # ==== float and stack navigation
        ("L-Tab", lambda: layout.move_in_stack(1)),
        ("L-S-space", lambda: layout.toggle_focused_view_floating()),

        # ==== fullscreen
        ("L-space", lambda: layout.toggle_fullscreen()),

        # ==== overview
        ("L-", lambda: layout.toggle_overview(only_active_workspace=True)),

        # ==== move in layout
        ("L-S-h", lambda: layout.move_focused_view(-1, 0)),
        ("L-S-j", lambda: layout.move_focused_view(0, 1)),
        ("L-S-k", lambda: layout.move_focused_view(0, -1)),
        ("L-S-l", lambda: layout.move_focused_view(1, 0)),

        # ==== resizing
        ("L-C-h", lambda: layout.resize_focused_view(-1, 0)),
        ("L-C-j", lambda: layout.resize_focused_view(0, 1)),
        ("L-C-k", lambda: layout.resize_focused_view(0, -1)),
        ("L-C-l", lambda: layout.resize_focused_view(1, 0)),


        # == misc
        ("L-c", lambda: layout.close_focused_view()),
        ("L-u", lambda: layout.update_config()),
        ("L-Q", lambda: layout.terminate()),
        ("C-A-Delete", lambda: layout.terminate()),
        ("L-A-l", lambda: layout.ensure_locked(anim=True, dim=True)),
        ("Print", lambda: os.system(f"{screenshot} &")),

        # == function keys
        # ==== keboard brightness
        ("XF86KbdBrightnessUp", lambda: os.system("light -A 5 &")),
        ("XF86KbdBrightnessDown", lambda: os.system("light -U 5 &")),
        # ==== monitor brightness
        ("XF86MonBrightnessUp", lambda: os.system(f"{brightness} --up &")),
        ("XF86MonBrightnessDown", lambda: os.system(f"{brightness} --down &")),
        # ==== volume
        ("XF86AudioRaiseVolume", lambda: os.system(f"{volume} --up &")),
        ("XF86AudioLowerVolume", lambda: os.system(f"{volume} --down &")),
        ("XF86AudioMute", lambda: os.system(f"{volume} --toggle &")),
        ("XF86AudioMicMute", lambda: os.system(f"{volume} --mic-toggle")),

    ]


# ============ gestures, grid layout =======================================
# https://github.com/newm-next/newm-next/blob/master/doc/config.md
gesture_bindings = {
    'launcher': (None, 'swipe-5'),
    'move-resize': ('L', 'move-1', 'swipe-2'),
    'swipe': (None, "swipe-3"),
    'swipe_to_zoom': (None, "swipe-4"),
}

gestures = {
    'lp_freq': 60.,     # default
    'lp_inertia': 0.8,  # default
    'two_finger_min_dist': 0.1,  # default
    'c': {      # c gestures
        'enabled': True,
        'scale_px': 800
    },
    'dbus': {   # dbus gestures
        'enabled': True
    },
    'pyevdev': {    # pyevdev (very much encouraged)
        'enabled': False,
        'two_finger_min_dist': 0.1,
        'validate_threshold': 0.02,
    },
}

grid = {
    # 'debug': False,
    'min_dist': 0.05,
    'throw_ps': [1, 5, 15],
    'time_scale': 0.3,
}

resize = {
    'grid_m': 3,
    'grid_ovr': 0.1,
    'hyst': 0.2,
}

swipe = {
    'gesture_factor': 3,
    'grid_m': 1,
    'grid_ovr': 0.2,
    'lock_dist': 0.01,
}

swipe_zoom = {
    'gesture_factor': 4,
    'grid_m': 1,
    'grid_ovr': 0.2,
    'hyst': 0.2,
}

move = {
    'grid_m': 3,
    'grid_ovr': 0.2,
}

move_resize = {
    'gesture_factor': 2
}

# ============ panels ============================================
# https://github.com/newm-next/newm-next/blob/master/doc/config.md
panels = {
    'launcher': {
        'cmd': launcher,
        'cwd': None,            # default
        'corner_radius': 0,     # default
        'h': 0.4,       # height
        'w': 0.8,       # width, default
    },
    'bar': {
        'cmd': waybar,
        'visible_fullscreen': False,
        'visible_normal': True,
    },
    'lock': {
        'cmd': 'alacritty -e newm-panel-basic lock',
        'w': 0.5,
        'h': 0.5,
        'corner_radius': 60,
    },
    'top_bar': {
        'native': {
            'enabled': True,
            'height': 38,
            'texts': lambda: []
        }
    }
}
