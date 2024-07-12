#!/usr/bin/env sh

set -eo pipefail



if [ -z "$1" ]; then
    echo "$0 [new HA tag]"
    exit 1
fi

cd $(dirname $0)

TAG=$1
# reuse an already gitignored path
TMPDIR=$(pwd)/build/hatagtmp

rm -fr $TMPDIR
mkdir -p $TMPDIR
curl -L https://github.com/home-assistant/core/archive/refs/tags/${TAG}.zip -o $TMPDIR/tag.zip
pushd $TMPDIR
echo Unzipping
unzip -q tag.zip
popd

for comp in $(find . -name manifest.json -d 2); do
    compname=$(basename $(dirname $comp))
    hapath=$TMPDIR/core-${TAG}/homeassistant/components/$compname

    if [ -e $hapath ]; then
        echo rsyncing $compname
        rsync -r $hapath/ $compname/
    else
        echo $compname NOT from hass
    fi
done

rm -fr $TMPDIR
