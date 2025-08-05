#!/usr/bin/env bash

_ps=(waybar)
for _prs in "${_ps[@]}"; do 
	if [[ `pidof ${_prs}` ]]; then 
		killall -9 ${_prs}
	fi
done

waybar -c ~/.config/newm/waybar/config &
