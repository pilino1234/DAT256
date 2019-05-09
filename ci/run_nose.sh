
pip --quiet install nose2 codecov

# Kivy deps
sudo apt-get -qq update > /dev/null
sudo apt-get -qq install -y \
    build-essential \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    libgl1-mesa-dev \
    > /dev/null

# Need to install Cython before Kivy
pip --quiet install cython==0.28.6
pip --quiet install -r app/requirements.txt

nose2 --start-dir app/ --with-coverage
codecov --token=$CODECOV_TOKEN

