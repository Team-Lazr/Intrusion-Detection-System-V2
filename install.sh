#!/usr/bin/bash
#	python 3
sudo apt update && sudo apt upgrade -y || "Error Updating"
sudo apt install python3 || "Error Installing Python3"
#	pip
sudo apt install python3-pip || "Error Installing Pip"
#	Google API
pip3 install google-auth-oauthlib || "Error installing google-auth-oauthlib"
pip3 install google-api-python-client || "Error Installing google-api-python-client"
pip3 install google-auth || "Error installing google-auth"
#	Fingerprint
pip3 install adafruit-circuitpython-fingerprint || "Error Installing adafruit-circuitpython-fingerprint"
echo "Installion Complete"
