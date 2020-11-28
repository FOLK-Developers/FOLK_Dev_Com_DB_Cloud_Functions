#! /bin/bash

cfpath=$1

echo $cfpath

cp -r ./../cloud-function-template/ ./../testing/$cfpath

