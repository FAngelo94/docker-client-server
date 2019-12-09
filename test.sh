#!/bin/bash
if [ "$2" == "client" ]; then # If first parameter passed then print Hi
    echo "ciao"
fi

check=0
if [ "$2" == "client" ]; then
    echo "ciao"
fi

while [ -n "$1" ]; do # while loop starts

    case "$1" in

    -a) echo "-a option passed" ;;

    -b)

        echo "-b option passed, with value $param"

        shift
        ;;

    -h)
        echo "Command line to make easy the work in this project"
        echo "-s install software necessary: "
        ;;

    --)
        shift # The double dash makes them parameters

        break
        ;;

    *) echo "Option $1 not recognized, press -h  to know commands" ;;

    esac

    shift

done
