
pip --quiet install nose2 codecov

nose2 --start-dir app/ --with-coverage
codecov --token=$CODECOV_TOKEN

