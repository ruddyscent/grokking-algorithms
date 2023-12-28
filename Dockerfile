FROM arm64v8/ubuntu:22.04

RUN apt-get update \
 && export DEBIAN_FRONTEND=noninteractive \
 && apt-get -y install --no-install-recommends \
    python3-pytest-xdist \
    python3-autopep8 \
    python3-typing-extensions \
    python-is-python3 \
    neovim \
    git \
    less \
 && apt-get clean autoclean \
 && apt-get autoremove --yes

RUN echo "alias vi=nvim" >> ~/.bash_aliases \
 && echo "alias vim=nvim" >> ~/.bash_aliases
