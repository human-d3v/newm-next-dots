#!/usr/bin/env bash

# Get brightness
get_backlight() {
	LIGHT=$(printf "%.0f\n" `light -G`)
	echo "${LIGHT}%"
}

# Notify
notify_user() {
	notify-send -h string:x-canonical-private-synchronous:sys-notify-backlight -u low -i "Brightness : $(get_backlight)"
}

# Increase brightness
inc_backlight() {
	light -A 5 && notify_user
}

# Decrease brightness
dec_backlight() {
	light -U 5 && notify_user
}

# Execute accordingly
if [[ "$1" == "--get" ]]; then
	get_backlight
elif [[ "$1" == "--inc" ]]; then
	inc_backlight
elif [[ "$1" == "--dec" ]]; then
	dec_backlight
else
	get_backlight
fi
