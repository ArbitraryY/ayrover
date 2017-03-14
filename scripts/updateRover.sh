#!/bin/bash

DATE=`date +%Y-%m-%d-%T`
OPT=$1
LOCAL_REPO_DIR=/home/ayrover
PROJ_NAME=AYRV

if [ $# != 1 ]
then
	echo "usage: $0 (push|pull)"
	echo "    push - ${LOCAL_REPO_DIR} to Github"
	echo "    pull - from Github to ${LOCAL_REPO_DIR}" 
	exit
fi

cd ${LOCAL_REPO_DIR}

if [ $OPT == "push" ]
then 

	echo "-------- Staging Changes -------------------"
	echo " "
	git add *
	git add -u *

	echo "-------- Committing to Git Repository -------------------"
	echo " "
	git commit -m "Updating ${PROJ_NAME} repository on ${DATE}"

	echo "-------- Push changes to Master -------------------"
	echo " "
	git push

	echo "Updated PLTN production repository on ${DATE}"
elif [ $OPT == "pull" ]
then
	echo "------- Updating ${PROJ_NAME} to latest version ----------"
	git pull
	
else
	echo "$OPT is not a valid option"
	exit
fi