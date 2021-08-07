#!/bin/sh

action=$(echo -e "Shutdown\nRestart\nSuspend\nHibernate" | rofi -dmenu -p "Action")

if [ "$action" == "Shutdown" ]; then
	systemctl poweroff
elif [ "$action" == "Restart" ]; then
	systemctl reboot
elif [ "$action" == "Suspend" ]; then
	systemctl suspend
elif [ "$action" == "Hibernate" ]; then
	systemctl hibernate
else 
	echo "I'm not sure what you meant. Exiting."
fi
