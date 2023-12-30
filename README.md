# 0x00. AirBnB Clone - The Console

## Table of Contents
- [Description](#description)
- [Background Context](#background-context)
- [Command Interpreter](#command-interpreter)
- [How to Start](#how-to-start)
- [Usage](#usage)
- [Examples](#examples)

## Description

The Airbnb Console Application is a command-line tool that allows you to interact with a collection of data models. These data models include `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, and `Review`. The application provides a set of commands to create, read, update, and delete instances of these models, as well as other features like counting instances, retrieving all instances, and updating instances with dictionary representations.

## Background Context

The goal is to manage the objects of our project:
- Create a new object (ex: a new User or a new place)
- Retrieve an object from a file, a database, etc.
- Do operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object.

## Command Interpreter

The command interpreter, implemented in the `console.py` file, is the core of this application. It provides an interactive shell that accepts user commands to perform various operations on the data models. Here's how to get started and use the command interpreter:

### How to Start

To start the Airbnb Console Application, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ugwujustine/AirBnB_clone.git
   ```

2. Change your current directory to the project folder:
   ```bash
   cd airbnb-console
   ```

3. Run the command interpreter:
   ```bash
   ./console.py
   ```

You should now see a `(hbnb)` prompt, indicating that you are in the Airbnb Console.

### Usage

The command interpreter supports various commands to manage and interact with the data models. Here are some of the available commands:

- `create <class_name>`: Create a new instance of a class and print its unique ID.
- `show <class_name> <instance_id>`: Display the string representation of an instance based on its class name and ID.
- `all [class_name]`: Retrieve all instances of a class, or if a class name is provided, retrieve all instances of that class.
- `count <class_name>`: Get the count of instances of a specific class.
- `update <class_name> <instance_id> <attribute_name> <attribute_value>`: Update an instance's attribute.
- `destroy <class_name> <instance_id>`: Delete an instance based on its class name and ID.
- `update <class_name> <instance_id> <dictionary_representation>`: Update an instance based on a dictionary representation.

### Examples

Here are some examples of how to use the Airbnb Console Application:

- Create a new `User` instance:
  ```bash
  (hbnb) create User
  ```

- Show details of a `User` instance with a specific ID (replace `<instance_id>` with the actual ID):
  ```bash
  (hbnb) show User <instance_id>
  ```

- Retrieve all instances of the `User` class:
  ```bash
  (hbnb) all User
  ```

- Count the number of instances of the `User` class:
  ```bash
  (hbnb) count User
  ```

- Update a `User` instance's email attribute:
  ```bash
  (hbnb) update User <instance_id> email "new_email@example.com"
  ```

- Delete a `User` instance:
  ```bash
  (hbnb) destroy User <instance_id>
  ```

- Update a `User` instance using a dictionary representation:
  ```bash
  (hbnb) update User <instance_id> {"email": "new_email@example.com", "first_name": "Gift"}
  ```

## Author 🖊️:
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17
