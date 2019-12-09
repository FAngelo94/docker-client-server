NAME_CLIENT_IMAGE=client_image
NAME_CLIENT_CONTAINER=client_container

NAME_SERVER_IMAGE=server_image
NAME_SERVER_CONTAINER=server_container

setup_client() {
    cd client

    docker build -t $NAME_CLIENT_IMAGE .
    docker run --name $NAME_CLIENT_CONTAINER -v  $NAME_CLIENT_IMAGE

    cd ..
}

setup_server() {
    cd server

    docker build -t $NAME_SERVER_IMAGE .
    docker run --name $NAME_SERVER_CONTAINER -p 49160:8080 -d $NAME_SERVER_IMAGE

    cd ..
}

init() {
    echo "###################"
    echo "# Start the Setup #"
    echo "###################"

    setup_server

    setup_client

    echo "################"
    echo "# Finish Setup #"
    echo "################"
}

stop_client() {
    echo "Stopping client container"
    docker stop $NAME_CLIENT_CONTAINER
}
start_client() {
    echo "Running client container"
    docker start -i $NAME_CLIENT_CONTAINER
}
stop_server() {
    echo "Stopping server container"
    docker stop $NAME_SERVER_CONTAINER
}
start_server() {
    echo "Running server container"
    docker start $NAME_SERVER_CONTAINER
}

restart() {
    stop_client
    stop_server
    start_server
    start_client
}

remove_client() {
    docker rm -f $NAME_CLIENT_CONTAINER
    docker rmi -f $NAME_CLIENT_IMAGE
}
remove_server() {
    docker rm -f $NAME_SERVER_CONTAINER
    docker rmi -f $NAME_SERVER_IMAGE
}
remove_all() {
    remove_server
    remove_client
}

print_help() {
    echo "Command line to make easy the work in this project"
    echo "-d remove server and client container and image of docker"
    echo "-h list of available commands"
    echo "-i initialize the environmnet creating and running docker container for client and server"
    echo "-r restart client and server container"
    echo "-s [all | client | server] start one or more container (all is the default option if no parameter is passed)"
    echo "-t [all | client | server] stop one or more container (all is the default option if no parameter is passed)"
}

if [ "$#" -eq 0 ]; then # If first parameter passed then print Hi
    print_help
fi

while [ -n "$1" ]; do # while loop starts

    case "$1" in

    -d)
        remove_all
        ;;

    -h)
        print_help
        ;;

    -i)
        init
        ;;

    -r)
        restart
        ;;

    -t)
        check=0
        if [ "$2" == "client" ]; then
            stop_client
            check=1
            shift
        fi
        if [ "$2" == "server" ]; then
            stop_server
            check=1
            shift
        fi
        if [ $check -eq 0 ]; then
            stop_server
            stop_client
        fi
        ;;

    -s)
        if [ "$2" == "client" ]; then
            start_client
            shift
        else
            if [ "$2" == "server" ]; then
                start_server
                shift
            else
                start_server
                start_client
            fi
        fi
        ;;

    --)
        shift # The double dash makes them parameters

        break
        ;;

    *) echo "Option $1 not recognized, press -h  to know commands" ;;

    esac

    shift

done
