#!/bin/bash

pip --quiet install pytest


(
    export KIVY_UNITTEST=1
    py.test --rootdir=app/ -v
)
