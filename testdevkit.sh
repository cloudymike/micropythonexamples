#!/bin/bash
pushd tools
./loadmicropython.sh
popd
pushd DEVKITv1
./test.sh
popd
