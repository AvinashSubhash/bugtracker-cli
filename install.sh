clear
echo "Welcome to Bugtracker v1.0!"
echo ""
echo "Adding Shortcut to bashrc . ."
echo ""
curr_path=$PWD;
install_command="alias bugdtracker=\"cd $curr_path ; python3 main.py ; cd ~ \" "
#echo $install_command
echo $install_command >> ~/.bashrc
source ~/.bashrc
clear
echo "Welcome to Bugtracker v1.0!"
echo ""
echo "Installation Successfull ! !"
echo ""
