#!/bin/bash

pushd .

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
# Build it
sudo docker build -f Dockerfile.linux -t jtrlinux .

mkdir -p hashcrack_jtr/static
rm hashcrack_jtr/static/john.tar.xz

# Copy it out
X=`sudo docker create jtrlinux`
sudo docker cp $X:/opt/john.tar.xz hashcrack_jtr/static/.
sudo docker rm $X

popd
