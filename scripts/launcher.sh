#!/usr/bin/env bash

DEV_PATH=$HOME/Projects/
PROD_PATH=$HOME/.config/

# case "$1" in
# 	"-d")
# 		alacritty --config-file=$DEV_PATH/newm-next-dots/alacritty/alacritty.toml -T newm-next-launcher -e newm-panel-basic launcher 
# 	;;
# 	*)
# 		alacritty --config-file=$PROD_PATH/newm-next-dots/alacritty/alacritty.toml -e newm-panel-basic launcher -T newm-next-launcher
# 	;;
# esac

case $1 in 
	"-d")
		foot --config=$DEV_PATH/newm-next-dots/foot/foot.ini --app-id="newm-next-launcher" newm-panel-basic launcher
		;;
	*)
		foot --config=$PROD_PATH/newm-next-dots/foot/foot.ini --app-id="newm-next-launcher" newm-panel-basic launcher
		;;
esac
