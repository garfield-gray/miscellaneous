#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 2 ]; do
        sleep 1
        ((n+=1))
        echo "Retry #$n"
done;



