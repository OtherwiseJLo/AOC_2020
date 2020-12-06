#!/bin/bash

if [ $1 -le 9 ]
then
  DAY_VAL="0$1"
else
  DAY_VAL=$1
fi

cp -r Day_N/ Day_$DAY_VAL
