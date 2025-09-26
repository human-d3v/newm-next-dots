#!/usr/bin/env bash

# Define step size
step=10

# Get current brightness
get_brightness() {
    brightnessctl -m | cut -d, -f4 | sed 's/%//'
}

# notify
notify_user() {
    local brightness=$(get_brightness)
    notify-send -h string:x-canonical-private-synchronous:sys-notify-backlight -u low -i display-brightness-symbolic "Brightness: ${brightness}%"
}

# change brightness
change_brightness() {
    local current_brightness
    current_brightness=$(get_brightness)
    local new_brightness

    # calculate new brightness
    if [[ "$1" == "+${step}%" ]]; then 
        new_brightness=$((current_brightness + step))
    elif [[ "$1" == "${step}%-" ]]; then 
        new_brightness=$((current_brightness - step))
    else
        echo "Error: Invalid brightness adjustment argument '$1'"
        exit 1
    fi

    # ensure new brightness is within valid range
    if (( new_brightness < 5 )); then 
        new_brightness=5
    elif (( new_brightness > 100 )); then 
        new_brightness=100
    fi

    brightnessctl set "${new_brightness}%"
    notify_user
}

# Execute accordingly
case "$1" in 
    "--get")
        get_brightness
        ;;
    "--inc")
        change_brightness "+${step}%"
        ;;
    "--dec")
        change_brightness "${step}%-"
        ;;
    *)
        get_brightness
        ;;
esac
