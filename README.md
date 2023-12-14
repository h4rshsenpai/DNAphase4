## Instructions to generate the Database from the dump file

The dump file is stored as `dump.sql` inside the submission folder.

Log in into a MySQL client on your machine and run the following commands:

```SQL
CREATE DATABASE FOOTBALL;
USE FOOTBALL;
source /path/to/submission/folder/dump.sql;
```

## Instructions to create the virtual environment and Install Requirements

It is preferable to create a virtual environment to run the CLI.

Python version >= 3.7 is required to run this project.

Inside the submission folder run the following commands to create and activate the virtual environment  and install the requirements:

```bash
$ python3.8 -m venv venv
OR
$ python3 -m venv venv

$ source ./bin/activate
$ pip install -r requirements.txt
```

## To run the CLI

To Run the Command Line Interface execute the following command:

```bash
$ python MiniWorld.py
```
