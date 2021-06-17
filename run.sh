#!/bin/bash
for zipFile in ./*.zip
do
  rollNum=`echo $zipFile | cut -f3 -d'-' | cut -f1 -d'.'`
  mkdir $rollNum
  unzip $zipFile -d $rollNum
  mv $rollNum/main.c $rollNum/$rollNum.c
done

