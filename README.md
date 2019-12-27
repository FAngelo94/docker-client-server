# Example of application with client and server encapsuleted in indipendent docker containers

In this example I created one server in NodeJS and one client with React.\
I encapsulated each of them in 2 different docker container and they can communicate each other.

## Client
It is made using React and it just call a GET API of server and print the result on the screen

## Server
I create a NodeJS server with one simple GET API that return a word.\
The guide I followed: https://nodejs.org/de/docs/guides/nodejs-docker-webapp/
