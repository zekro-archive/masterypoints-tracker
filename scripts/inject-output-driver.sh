#!/bin/bash

DRIVER=File
FILE=$2

if [ -z $FILE ]; then
    FILE=$PWD/mp-tracker/const/outputdriver.py
fi

case $1 in
    mongo|mongodb)
        DRIVER=MongoDB
        ;;
    file)
        DRIVER=File
        ;;
esac

echo "import output" > $FILE
echo "" >> $FILE
echo "OUTPUT_DRIVER = output.$DRIVER" >> $FILE
