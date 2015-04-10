#!/bin/sh

for FILE in `cat urls`
do
    FILE=`echo $FILE | perl -pe 's/desc/text/'`.txt
    curl -O $FILE
done