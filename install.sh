#!/bin/bash
# Installs metax dependencies, makes soft link named metax in /usr/local/bin/ (to gui.py script in current working dir)

if [ "$(id -u)" -ne "0" ]; then
    echo ' [#] Run as root'
    exit 1
fi

for dep in 'apt-get update' 'apt-get -y install fdupes libimage-exiftool-perl python3 python3-pip python-qt4' 'pip3 install requests'; do
    $dep
    if [ "$?" -ne "0" ]; then
        echo ' [-] Failed installing metax dependencies, try manually'  
        exit 1
    fi
done

chmod +x gui.py
ln -s -T "$(pwd)/gui.py" /usr/local/bin/metax
if [ "$?" -ne "0" ]; then
    echo ' [-] Failed creating link of metax in /usr/local/bin/, try manually'  
    exit 1
fi

echo ' [+] Dependencies installed and program setup correctly, you can run "metax" in a terminal'
exit 0
