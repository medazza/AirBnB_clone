AirBnB Clone - The Console

Welcome to our AirBnB clone project! In this exciting work, we'll lay the foundation for a web application by building a command interpreter. This interpreter is essential for managing our Airbnb properties including users, states, cities, locations, and more. This is what we do together:

Building the BaseModel Class: We'll kick things off by crafting a parent class named BaseModel. This class will be responsible for handling the initialization, serialization, and deserialization of our instances.

Setting Up Serialization/Deserialization Flow: Let's establish a straightforward flow for serialization and deserialization. We'll be working with instances, dictionaries, JSON strings, and files to make our data management seamless.

Creating AirBnB Object Classes: We'll design classes for the various objects within AirBnB, like User, State, City, and Place. It's important that these classes inherit from our BaseModel class.

Developing the Abstracted Storage Engine: Next up, we'll create the initial abstracted storage engine, focusing specifically on file storage. This engine will be the powerhouse behind storing and retrieving our precious objects.

Crafting the Command Interpreter:

Here comes the heart of our project – the command interpreter. Think of it as a personalized shell for managing AirBnB objects. With this interpreter, we'll be able to: Create new objects (User, Place, etc.). Retrieve objects from various sources (files, databases, etc.). Perform operations on objects (count, compute stats, etc.). Update attributes of objects. Destroy objects.

Ensuring Reliability with Unit Tests: To make sure our code is robust and dependable, we'll create thorough unit tests. These tests will validate the functionality of all classes and the storage engine. Execution Your shell should work like this in interactive mode:

1 Command Interpreter (console.py)

The command interpreter provides a user-friendly interface for interacting with the AirBnB clone. It allows users to create, update, and manage instances of various classes through a command-line interface.

2 Key Features:

Create new instances of BaseModel and other classes
Update attributes of instances
Display information about instances
Delete instances

4 How to Start the Command Interpreter

To start the AirBnB clone command interpreter, run the following command:

#bash $ ./console.py

How to Use the other Commands:
The command interpreter supports various commands, including:

create: Create a new instance of a specified class.
show: Display information about a specific instance.
destroy: Delete an instance.
all: Display information about all instances or instances of a specific class.
update: Update the attributes of an instance.
Example Usage:

some inputs: 
$ create BaseModel 
$ show BaseModel 1234-5678 
$ all 
$ update BaseModel 1234-5678 name "New Name" 
$ destroy BaseModel 1234-5678

some outputs:
$ show BaseModel 49faff9a-6318-451f-87b6-910505c55907 
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
