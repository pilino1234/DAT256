#!/bin/bash

pip --quiet install nose2 codecov

nose2 --start-dir app/
