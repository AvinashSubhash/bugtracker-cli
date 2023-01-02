clear
echo -e "Welcome to Bugtracker v1.0!\n"

if [ -d "/home/$USER/.bugtracker-files" ]
then
    yes | rm -R /home/$USER/.bugtracker-files
fi
mkdir /home/$USER/.bugtracker-files
cp -R $PWD /home/$USER/.bugtracker-files/
export PATH=$PATH:/home/$USER/.bugtracker-files/bugtracker-cli/
echo "PATH=\$PATH:/home/$USER/.bugtracker-files/bugtracker-cli/" >> /home/$USER/.bashrc
#echo "Welcome to Bugtracker v1.0!"
#echo ""
#echo "Installation Successfull ! !"
#echo ""
exit