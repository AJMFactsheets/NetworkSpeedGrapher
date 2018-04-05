#!/bin/bash

name=$1
count=$2

getData() {
     test="$(speedtest-cli --simple)"


     date >> $name
     echo $test | grep -o 'Download: [0-9]*\.[0-9]*' >> $name
     echo $test | grep -o 'Upload: [0-9]*\.[0-9]*' >> $name

}

while [ "$count" -gt 0 ]
do
     getData

     (( count-- ))

     sleep 3570s

done
echo "fin"
