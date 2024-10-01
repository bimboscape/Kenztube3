#!/bin/bash

echo "Activating virtual environment."
source /home/kenz/Documents/kenztube/bin/activate

echo "Changing directory."
cd /home/kenz/Documents/kenztube || { echo "Directory not found"; exit 1; }

echo "Running kenztube."
echo "Enjoy!"
python3 kenztube2.0.py

