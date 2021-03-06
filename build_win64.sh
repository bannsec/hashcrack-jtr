#!/bin/bash

set -e

pushd .

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
# Build it
sudo docker build -f Dockerfile.win64 -t jtrwin64 .

mkdir -p hashcrack_jtr/static
rm -f hashcrack_jtr/static/john.tar.xz

# Copy it out
X=`sudo docker create jtrwin64`
sudo docker cp $X:/opt/john.tar.xz hashcrack_jtr/static/.
sudo docker rm $X

# Create the version
git checkout hashcrack_jtr/version.py
sed -i "s/VERSION/`date +%y.%m.%d`/g" hashcrack_jtr/version.py

python3 setup.py bdist_wheel --plat-name win_amd64 --python-tag "py3"

# Cleanup change
git checkout hashcrack_jtr/version.py

popd
