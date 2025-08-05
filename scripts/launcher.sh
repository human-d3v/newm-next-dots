#!/usr/bin/env bash

DEV_PATH=$HOME/Projects
PROD_PATH=$HOME/.config

case $1 in 
	"-d")
		foot --config=$DEV_PATH/newm-next-dots/foot/foot.ini --app-id="newm-next-launcher" newm-panel-basic launcher
		;;
	*)
		foot --config=$PROD_PATH/newm/foot/foot.ini --app-id="newm-next-launcher" newm-panel-basic launcher
		;;
esac
