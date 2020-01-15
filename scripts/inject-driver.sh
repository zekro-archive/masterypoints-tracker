#!/bin/bash

DRIVER=File
FILE=$2

if [ -z $FILE ]; then
    FILE=$PWD/mp-tracker/const/datadriver.py
fi

case $1 in
    mongo|mongodb)
        DRIVER=MongoDB
        ;;
    file)
        DRIVER=File
        ;;
esac

echo "import driver" > $FILE
echo "" >> $FILE
echo "DATA_DRIVER = driver.$DRIVER" >> $FILE
