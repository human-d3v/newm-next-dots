import os;
entries = {
    "Vivaldi": "vivaldi",
    "Ghostty": "ghostty",
    "Gimp": "gimp",
    "Thunar": "thunar",
    "Alacritty": "alacritty",
    "Tor": f"{os.environ["HOME"]}/.config/newm/scripts/tor.sh",
    "Foot": "foot",
    "Zoom": f"{os.environ["HOME"]}/.config/newm/scripts/zoom.sh",
    "Calibre": f"{os.environ["HOME"]}/.config/newm/scripts/calibre.sh",
    "VLC": f"{os.environ["HOME"]}/.config/newm/scripts/vlc.sh"
}

shortcuts = {
    1: ("Vivaldi", "vivaldi"),
    2: ("Thunar", "thunar"),
    3: ("Gimp", "gimp"),
}
