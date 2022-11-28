FROM golang:1.19.3
RUN go install github.com/heistp/irtt/cmd/irtt@latest

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ="Europe/Stockholm"
RUN apt-get update -y #  && apt-get upgrade -y 

# Set the python version
ENV PYTHON_VERSION 3.9.0

#Set of all dependencies needed for pyenv to work on Ubuntu
RUN apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget ca-certificates curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev mecab-ipadic-utf8 git

# Set-up necessary Env vars for PyEnv
ENV PYENV_ROOT /root/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Install pyenv
RUN set -ex \
    && curl https://pyenv.run | bash \
    && pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pyenv rehash

# copy python script
COPY ntw-meas/ntw-meas.py /tmp/ntw-meas.py

RUN mkdir -p /tmp/results
COPY combined/combined-entrypoint.sh /tmp/combined-entrypoint.sh
RUN chmod +x /tmp/combined-entrypoint.sh
ENTRYPOINT ["/tmp/combined-entrypoint.sh"]
