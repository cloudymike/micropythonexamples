#!/bin/bash
# Needs a ESP32 DevKit1 plugged in and using PORT as listed

PORT=/dev/ttyUSB0

if [ "$1" != "" ]
then
	DIRS=$1
else
	DIRS=*
fi

echo "Setup wlan, it is probably needed for some tests"
pushd wlan &> /dev/null
timeout 120 ./RUN.sh &>/dev/null
popd &> /dev/null

FAILTEST=0
for d in $DIRS
do
	if [[ -d $d ]]
	then
		if [[ -f "$d/test.py" ]]
		then
			echo Testing $d
			pushd $d &> /dev/null
			timeout 120 ./RUN.sh &>/dev/null
			timeout 60 ampy --port $PORT run test.py | grep TESTOK
			OK=$?
			if [ "$OK" != "0" ]
			then
				echo "Test Failed"
				FAILTEST=1
			fi
			popd &> /dev/null
		fi
	fi
done

if [ "$FAILTEST" == "1" ]
then
	echo One or more tests failed
	exit 1
else
	echo All tests passed
fi
