#!/bin/bash

# Get the current working directory
current_dir=$(pwd)

# Create the virtual environment in the current directory with the given name
python3 -m venv "$current_dir/$1"

