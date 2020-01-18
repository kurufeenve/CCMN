#!/bin/bash

path=$(pwd)
activate () {
  . /bin/activate
}

if command -v python3 &>/dev/null; then
    pip3 install virtualenv
    mkdir venv
    python3 -m venv $path/venv
    source "./venv/bin/activate"
    pip3 install requests
    echo
    echo "=========="
    echo
    echo "DONE :)"
    echo
    echo "=========="
    echo

else
    echo "Python 3 is not installed. 
    If you are on mac in school 42 install python3 throught managed software center 
    and run this script one more time"
fi
