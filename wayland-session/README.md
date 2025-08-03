# Installing environment variables and wayland session information
```bash
sudo install -Dm 755 ./00-lock.sh /usr/lib/systemd/system-sleep/00-lock.sh
sudo install -Dm 755 ./newm-run.sh /usr/local/bin/newm-run.sh
sudo install -Dm 755 ./open-wl /usr/local/bin/open-wl
```

# Installing the desktop profile 
```bash
sudo install -Dm 755 ./newm-next.desktop /usr/share/wayland-sessions/newm-next.desktop
```
