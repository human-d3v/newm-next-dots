# Dotfiles for newm-next Wayland Compositor
newm-next is the most unique scrolling/tiling Wayland Compositor out there. 
Here is my personal config. 

# Dependencies
These are a non-comprehensive list of dependencies for these dots. 
- NetworkManager (+tools on Gentoo)
- Bluez
- [wallust](https://codeberg.org/explosion-mental/wallust)
- [newm-next](https://github.com/newm-next/newm-next)
- [waybar](https://github.com/Alexays/Waybar)

# Installation

To clone this repository:

```bash
git clone https://github.com/human-d3v/newm-next-dots $HOME/.config/newm
```

## Generic installation of newm-next
Because the compositor is built and installed using `pip`, diagnosing build
issues is a little tricky. Most of the dependency issues occur when building 
[wlroots](https://github.com/swaywm/wlroots). The easiest way to make sure 
that you install all of the dependencies necessary is to build wlroots in the 
[pywm-next](https://github.com/newm-next/pywm-next) repository. That can be 
acheived using the following:

1) Clone pywm-next and enter directory:
```bash
cd /tmp &&
git clone https://github.com/newm-next/pywm-next &&
cd pywm-next &&
```

2) Attempt to build pywm-next:
```bash
git submodule update --init --recursive && meson build && ninja -C build
```

3) Check output for failed installation, install that dependency, rinse, repeat.
<!-- The output should look something like this: -->
<!-- todo: show fail build -->
This may take some time, but once the build completes without issues, it's time
to install pywm-next using pip.

4) Install pywm-next:
```bash
# remove pywm-next from tmp
cd $HOME &&
rm -Rf /tmp/pywm-next
# install pywm-next using pip
pip3 install --user git+https://github.com/newm-next/pywm-next
```

5) Install newm-next:
```bash
pip3 install --user git+https://github.com/newm-next/newm-next
```

## Distro specific isntallation of newm-next
<details>
<summary>On Fedora</summary>

```bash
# install dependencies
sudo dnf install cmake gcc glslang libavcodec-free-devel libavformat-free-devel libavutil-free-devel libdrm-devel libinput-devel libpng-devel libseat-devel libxkbcommon-devel mesa-libEGL-devel mesa-libgbm-devel meson ninja-build pixman-devel python3-devel python3-meson-python python3-pip python-wheel systemd-devel vulkan-loader-devel wayland-devel wayland-protocols-devel xcb-util-errors-devel xcb-util-renderutil-devel xcb-util-wm-devel xorg-x11-server-Xwayland-devel
# install pywm-next packages
pip install --user git+https://github.com/newm-next/pywm-next
# install newm-next packages
pip install --user git+https://github.com/newm-next/newm-next
```
</details>

<details>
<summary>On Ubuntu</summary>

```bash
# install dependencies
sudo apt install git meson pkg-config cmake libwayland-dev wayland-protocols libxkbcommon-dev libinput-dev libpixman-1-dev libdrm-dev libgbm-dev libegl-dev libgles2-mesa-dev libvulkan-dev glslang-tools libseat-dev libxcb-dri3-dev libxcb-composite0-dev libxcb-icccm4-dev libxcb-res0-dev libpng-dev libxcb-present-dev libavutil-dev libxcb-render-util0-dev libxcb-shm0-dev libxcb-xinput-dev libxcb-errors-dev libavcodec-dev libavformat-dev python3-dev python3-pip
# install pywm-next packages (bypassing the PEP 668 externally managed error)
pip install --user --break-system-packages git+https://github.com/newm-next/pywm-next 
# install newm-next packages
pip install --user --break-system-packages git+https://github.com/newm-next/newm-next 
# adding .local/bin/ to PATH (optional)a
## for bash
echo 'PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
## for zsh
echo 'PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
```
</details>

<details>
<summary>On Gentoo</summary>
If you're using Gentoo as your daily driver, it really should go without saying
that you should not just copy the following and try to compile it to your system. 
You will need to add the guru overlay, unmask various packages, adjust package
USE flags and build for your architecture with your make flags. I'm only
including this list for reference.

```bash
# this is with the desktop systemd profile selected
#install dependencies
sudo emerge -av app-misc/brightnessctl dev-libs/light dev-libs/mpc dev-util/geany dev-ruby/sync gnome-extra/yad::guru gui-apps/foot gui-apps/fuzzel::guru gui-apps/mako gui-apps/satty gui-apps/satty gui-apps/slurp gui-apps/waybar gui-apps/wf-recorder gui-apps/wl-clipboard gui-apps/wlogout::guru gui-apps/wtype::wayland-desktop gui-libs/xdg-desktop-portal-wlr media-gfx/imagemagick media-gfx/viewnoir media-sound/mpd media-sound/playerctl media-sound/pulsemixer media-video/ffmpeg media-video/libva-utils media-video/mpv sys-auth/polkit sys-auth/polkit sys-auth/seatd www-client/vivaldi x11-base/xwayland x11-libs/xcb-util-errors x11-terms/alacritty x11-terms/ghostty xfce-base/libxfce4ui xfce-base/thunar xfce-base/tumbler
```
</details>

# Setting up Wayland Environment
Follow the [wayland-session README](https://github.com/human-d3v/newm-next-dots/tree/main/wayland-session). It outlines the install guide for the locking behaviour, Wayland Session variables, and start scripts. 
