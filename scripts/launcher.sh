#!/usr/bin/env bash

DEV_PATH=$HOME/Projects/
PROD_PATH=$HOME/.config/

case "$1" in
	"-d")
		alacritty --config-file=$DEV_PATH/newm-next-dots/alacritty/alacritty.toml -e newm-panel-basic launcher -T newm-next-launcher
	;;
	*)
		alacritty --config-file=$PROD_PATH/newm-next-dots/alacritty/alacritty.toml -e newm-panel-basic launcher -T newm-next-launcher
	;;
esac
