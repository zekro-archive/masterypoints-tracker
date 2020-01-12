#!/bin/bash

DRIVER=File

case $1 in
    mongo|mongodb)
        DRIVER=MongoDB
        ;;
    file)
        DRIVER=File
        ;;
esac

echo "import output" > $2
echo "" >> $2
echo "OUTPUT_DRIVER = output.$DRIVER" >> $2