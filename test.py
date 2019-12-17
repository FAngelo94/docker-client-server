import subprocess
import os
import sys

NAME_CLIENT_IMAGE = "client_image"
NAME_CLIENT_CONTAINER = "client_container"

NAME_SERVER_IMAGE = "server_image"
NAME_SERVER_CONTAINER = "server_container"

def setup_client():
    os.chdir('client/')
    os.system('docker build -t ' + NAME_CLIENT_IMAGE + ' .')
    os.system(
        'docker run --name ' + NAME_CLIENT_CONTAINER + ' -i -d -v ${PWD}:/srv/app ' + NAME_CLIENT_IMAGE + '')
    os.system('docker exec -w /srv/app ' + NAME_CLIENT_CONTAINER + ' npm install')
    os.system('docker exec -w /srv/app ' + NAME_CLIENT_CONTAINER + ' npm start')
    os.chdir('../')

def setup_server():
    os.chdir('server/')
    os.system('docker build -t ' + NAME_SERVER_IMAGE + ' .')
    os.system(
        'docker run --name ' + NAME_SERVER_CONTAINER + ' -p 49160:8080 -i -d -v ${PWD}:/srv/app ' + NAME_SERVER_IMAGE + ' /bin/bash')
    os.system('docker exec -w /srv/app -d ' + NAME_SERVER_CONTAINER + ' npm install')
    os.system('docker exec -w /srv/app -d ' + NAME_SERVER_CONTAINER + ' npm start')
    os.chdir('../')

def setup_environment():
    print('################')
    print('# Start Initialization #')
    print('################')

    setup_server()
    setup_client()


def start_client():
    print('Starting client...')
    os.system('docker start ' + NAME_CLIENT_CONTAINER + '')
    os.system('docker exec -w /srv/app ' + NAME_CLIENT_CONTAINER + ' npm start')


def start_server():
    print('Startng server...')
    os.system('docker start ' + NAME_SERVER_CONTAINER + '')
    os.system('docker exec -w /srv/app -d ' + NAME_SERVER_CONTAINER + ' npm start')


def start_environment():
    print('Starting environment...')
    start_server()
    start_client()


def stop_client():
    print('Stopping client...')
    os.system('docker stop ' + NAME_CLIENT_CONTAINER + '')


def stop_server():
    print('Stopping server...')
    os.system('docker stop ' + NAME_SERVER_CONTAINER + '')


def stop_environment():
    print('Stopping environment...')
    stop_client()
    stop_server()


def restart_environment():
    print('Restarting environment...')
    stop_environment()
    start_environment()


def delete_client():
    print('Deleting client...')
    os.system('docker rm -f ' + NAME_CLIENT_CONTAINER)
    os.system('docker rmi -f ' + NAME_CLIENT_IMAGE)


def delete_server():
    print('Deleting server...')
    os.system('docker rm -f ' + NAME_SERVER_CONTAINER)
    os.system('docker rmi -f ' + NAME_SERVER_IMAGE)


def delete_environment():
    print('Deleting environment...')
    delete_client()
    delete_server()


def print_help(command):
    print('Welcome to the Jungle!')
    print('Thanks to this script you can manage easly docker containers for client and server')
    print('This is the listo of commands you can use:')
    print('-d, --delete [all | client | server] remove client, servr or both (all is the default option if no parameter is passed)')
    print('-h, --help list of available commands')
    print('-i, --init initialize the environmnet creating and running docker container for client and server')
    print('-r, --restart client and server container')
    print('-s, --start [all | client | server] start client, servr or both (all is the default option if no parameter is passed)')
    print('-t, --terminate [all | client | server] stop one or more container (all is the default option if no parameter is passed)')


def identify_command(command, parameter):
    if command == '-d' or command == '--delete':
        if parameter == 'client':
            delete_client()
        elif parameter == 'server':
            delete_server()
        else:
            delete_environment()
    if command == '-h' or command == '--help':
        print_help(None)
    if command == '-i' or command == '--init':
        if parameter == 'client':
            setup_client()
        elif parameter == 'server':
            setup_server()
        else:
            setup_environment()
    if command == '-r' or command == '--restart':
        restart_environment()
    if command == '-s' or command == '--start':
        if parameter == 'client':
            start_client()
        elif parameter == 'server':
            start_server()
        else:
            start_environment()
    if command == '-t' or command == '--terminate':
        if parameter == 'client':
            stop_client()
        elif parameter == 'server':
            stop_server()
        else:
            stop_environment()

def main():
    command = '-h'
    parameter = None
    if (len(sys.argv) >= 2):
        command = sys.argv[1]
    if len(sys.argv) >= 3:
        parameter = sys.argv[2]
    identify_command(command, parameter)

if __name__ == "__main__":
    main()