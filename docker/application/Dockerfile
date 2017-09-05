FROM python:latest
# While we are in dev. Change to alpine, slim or even a custom image

# For phantom JS from source
RUN apt-get update \
    && apt-get install -y \
    qpdf # for decrypting pdf
#    build-essential \
#    g++ \
#    flex \
#    bison \
#    gperf \
#    ruby \
#    perl \
#    libsqlite3-dev \
#    libfontconfig1-dev \
#    libicu-dev \
#    libfreetype6 \
#    libssl-dev \
#    libpng-dev \
#    libjpeg-dev \
#    python \
#    libx11-dev \
#    libxext-dev \
#    ttf-mscorefonts-installer

# Phantom JS from package
RUN apt-get update \
    && apt-get install -y \
    fontconfig

# We add Phantom JS to the PATH
ENV PATH /var/www/docker/bin:$PATH

# For python's imports
ENV PATH /var/www:$PATH


ADD . /var/www
WORKDIR /var/www
RUN usermod -u 1000 www-data
# We need to update pip
# The requirement must be in a fixed version
RUN pip install --no-cache-dir -r requirements.txt
