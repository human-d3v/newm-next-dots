#!/bin/bash
# https://github.com/newm-next/newm-next/blob/master/doc/env_wayland.md
# this is a combo of the suggested wayland_enablement.sh and newm-run.sh


# --- Set session variables newm-run
export XDG_SESSION_TYPE=wayland
export XDG_SESSION_DESKTOP=wlroots
export XDG_CURRENT_DESKTOP=wlroots
export XDG_CURRENT_SESSION=wlroots

# --- Set gtk variables
export TDESKTOP_DISABLE_GTK_INTEGRATION=1
export CLUTTER_BACKEND=wayland
export BEMENU_BACKEND=wayland

# --- Firefox variables
export MOZ_ENABLE_WAYLAND=1

# --- Qt environment
export QT_QPA_PLATFORM=wayland-egl
export QT_WAYLAND_FORCE_DPI=physical
export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
export QT_QPA_PLATFORMTHEME=qt5ct
export QT_AUTO_SCREEN_SCALE_FACTOR=1

# --- Elementary environment
export ELM_DISPLAY=wl
export ECORE_EVAS_ENGINE=wayland_egl
export ELM_ENGINE=wayland_egl
export ELM_ACCEL=opengl
# export ELM_SCALE=1

# --- SDL environment
export SDL_VIDEODRIVER=wayland

# --- Java environment
export _JAVA_AWT_WM_NONREPARENTING=1

# --- GDK backend
export GDK_BACKEND="wayland,x11"

export NO_AT_BRIDGE=1
export WINIT_UNIX_BACKEND=wayland
export DBUS_SESSION_BUS_ADDRESS
export DBUS_SESSION_PID

# start newm in debug mode
sleep 0.5;
start-newm -d
