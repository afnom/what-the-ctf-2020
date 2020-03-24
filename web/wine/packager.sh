#!/bin/bash

SOURCE=$(realpath $0 | xargs dirname)
echo $SOURCE

cd $(mktemp -d)
cp -r $SOURCE/templates/ $SOURCE/static/ $SOURCE/app.py .
echo "AFNOM{censored}" > secret.flag

zip app.zip templates/* static/* app.py secret.flag
cp app.zip $SOURCE

rm -r $(pwd)
