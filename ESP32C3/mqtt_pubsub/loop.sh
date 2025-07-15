#!/bin/bash
old_tty=$(stty --save)

# Minimum required changes to terminal.  Add -echo to avoid output to screen.
stty -icanon min 0;


while true ; do
    if read -t 0; then # Input ready
        read -n 1 char
        echo -e "\nRead: ${char}\n"
        break
    else # No input
        echo -n '.'
        sleep 1
    fi
done

stty $old_tty
