#!/bin/sh

action=$(echo  "Shutdown\nRestart\nSuspend\nHibernate" | rofi -dmenu -p "Action")

if [ "$Action" == "Shutdown" ]; then
	systemctl poweroff
elif [ "$Action" == "Restart" ]; then
	systemctl reboot
elif [ "$Action" == "Suspend" ]; then
	systemctl suspend
elif [ "$Action" == "Hibernate" ]; then
	systemctl hibernate
else 
	echo "I'm not sure what you meant. Exiting."
fi
