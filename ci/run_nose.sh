
pip --quiet install nose2 codecov

# Kivy deps
sudo apt-get update
sudo apt-get install -y \
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
    libgl1-mesa-dev

# Need to install Cython before Kivy
pip install cython==0.28.6
pip install -r app/requirements.txt

nose2 --start-dir app/ --with-coverage
codecov --token=$CODECOV_TOKEN

