#!/bin/bash

pip --quiet install yapf

yapf --diff --recursive --parallel -vv app/
