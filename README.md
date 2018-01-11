# Data Management System

## Requirements

1. Python 3.5
2. virtualenv

### Installation

Go to a directory of your choice to create a virtual environment using virtualenv or pyvenv for Python 3.5

Python 3.5:

```
pyvenv-3.5 data_management
```

Download and run the code:

```
cd data_management
source bin/activate
git clone https://github.com/kureck/data_management
cd data_management
pip install -e .
py.test graph_distance/tests # to run tests
```
---

## Input

Example of dataset master creation

```bash
python run.py data-generation -m tests/data/master-dataset -fs 2 -fns mobile,2,cars,2,sensors,2
```

Where:

| params        | description     |
| ------------- |:---------------:|
| -m            | root path       |
| -fs           | each file size  |
| -fns          | subfolders,size |

Example of dataset update

```bash
python run.py data-update -m tests/data/master-dataset -fns mobile,4
```

Where:

| params        | description     |
| ------------- |:---------------:|
| -m            | root path       |
| -fns          | subfolders,size |


Example of dataset backup

```bash
python run.py data-backup -mp tests/data/master-dataset -bp tests/data/backup-master
```

Where:

| params        | description     |
| ------------- |:---------------:|
| -m            | root path       |
| -bp           | backup path     |
