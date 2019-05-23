

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

# Install unit testing stuff
pip --quiet install pytest pytest-cov codecov

# Decrypt keyfile
openssl aes-256-cbc -K $encrypted_931cb05f54dd_key -iv $encrypted_931cb05f54dd_iv -in keyfile.json.enc -out keyfile.json -d

# Run tests
(
    export KIVY_UNITTEST=1
    py.test --rootdir=app/ -v --cov=./
)

# Upload coverage data
codecov --token=$CODECOV_TOKEN
