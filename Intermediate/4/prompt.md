# Python Intermediate Project #4

## Chat Room with Sockets

Create a chat room application that allows multiple users to communicate with each other in real time using sockets. Sockets are a low-level networking interface that enable data exchange between processes running on different machines. You will need to create two Python files: one for the server and one for the client.

Server requirements:

* Responsible for creating a socket, binding it to a port, listening for (and accepting) incoming connections.
* Maintain a list of connected clients in order to broadcast any messages received from one client to all the others.
* Handle any errors or exceptions that occur during the communication.

Client requirements:

* Responsible for connecting to the server socket, sending and receiving messages, and displaying them on the console.
* Allow the user to enter a username and a message, and format them appropriately.
* The client should handle any errors or exceptions that may occur during the communication.
