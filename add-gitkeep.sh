#!/bin/bash

# find all empty subdirectories and add a .gitkeep file to each one
find . -type d -empty -not -path "./.git/*" -exec touch {}/.gitkeep \;
