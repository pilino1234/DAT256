#!/bin/bash

pip install prospector[with_mypy]

#prospector app/ --profile carrepsa --with-tool mypy
prospector app/ --profile carrepsa
