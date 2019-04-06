#!/usr/bin/env bash

#
# usage:
#   ./build_apk.sh
# or:
#   ./build_apk.sh --verbose
#

set -e

# Generate passwd/group file, e.g.: doesn't exist on travis ;)

TEMP=$(python -c "import tempfile;print(tempfile.gettempdir())")

TEMP_PASSWD=${TEMP}/passwd
TEMP_GROUP=${TEMP}/group

DOCKER_UID=$(id -u)
DOCKER_UGID=$(id -g)
DOCKER_USER=${USER}

echo "${DOCKER_USER}:x:${DOCKER_UID}:${DOCKER_UGID}:${DOCKER_USER},,,:/buildozer/:/bin/bash">${TEMP_PASSWD}
echo "${DOCKER_USER}:x:${DOCKER_UGID}:">${TEMP_GROUP}

CHANGE_USER="-v ${TEMP_GROUP}:/etc/group:ro -v ${TEMP_PASSWD}:/etc/passwd:ro -u=$UID:$(id -g $USER)"

set -x

docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"

docker pull pilino1234/carrepsa-build

(
    cd app

    docker run --tty pilino1234/carrepsa-build python3 --version
    docker run --tty --volume ${PWD}:/buildozer/ pilino1234/carrepsa-build pip3 freeze
    docker run --tty --volume ${PWD}:/buildozer/ pilino1234/carrepsa-build cython --version
    docker run --tty --volume ${PWD}:/buildozer/ pilino1234/carrepsa-build buildozer --version

#    docker run --tty --volume ${PWD}:/buildozer/ ${CHANGE_USER} jedie/buildozer id
#    docker run --tty --volume ${PWD}:/buildozer/ ${CHANGE_USER} jedie/buildozer pwd
#    docker run --tty --volume ${PWD}:/buildozer/ ${CHANGE_USER} jedie/buildozer ls -la

    # Output something every 10 minutes or Travis kills the job
    # https://github.com/travis-ci/travis-ci/issues/4190#issuecomment-353342526
    while sleep 540; do echo "=====[ $SECONDS seconds still running ]====="; done &

    docker run --tty --volume ${PWD}:/buildozer/ ${CHANGE_USER} pilino1234/carrepsa-build buildozer ${1} android debug
    #docker run --tty --volume ${PWD}:/buildozer/ ${CHANGE_USER} pilino1234/carrepsa-build buildozer ${1} android release

    # Killing background sleep loop
    kill %1

    ls -la
    ls -la bin/
)

