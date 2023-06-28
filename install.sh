#!/bin/bash
clear
echo -e "Welcome to Bugtracker v0.1.0!\n"

if [ -d "/home/$USER/.bugtracker-files" ]
then
    yes | rm -R /home/$USER/.bugtracker-files
fi
mkdir /home/$USER/.bugtracker-files
cp -R $PWD /home/$USER/.bugtracker-files/
if ! grep -Fxq "PATH=\$PATH:/home/$USER/.bugtracker-files/bugtracker-cli/" /home/$USER/.bashrc
then
    export PATH=$PATH:/home/$USER/.bugtracker-files/bugtracker-cli/
    echo "PATH=\$PATH:/home/$USER/.bugtracker-files/bugtracker-cli/" >> /home/$USER/.bashrc
fi
exit