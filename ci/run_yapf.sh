#!/bin/bash

pip install yapf

yapf --diff --recursive --parallel -vv app/
