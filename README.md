# Example of application with client and server encapsuleted in indipendent docker containers

In this example I created one server in NodeJS and one client with React.\
I encapsulated each of them in 2 different docker container and they can communicate each other.\

To setup the environment use the following command in the terminal inside the project:
```
python utilities.py -i
```

To see the other available commands to manage the docker containers use the following command in the terminal inside the project:
```
python utilities.py -h
```

## Prerequisites
You need to install Python 3 in your computer to run the python script that help you to manage the docker containers.\
There is also a script shell for Ubuntu user that do almost the same thing of the python script.

## Client
It is made using React and it just call a GET API of server and print the result on the screen

## Server
I create a NodeJS server with one simple GET API that return a word.\
The guide I followed: https://nodejs.org/de/docs/guides/nodejs-docker-webapp/
