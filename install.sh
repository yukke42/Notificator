#!/bin/bash

# create a setting file
if [ ! -e "config.ini" ];then
  cp config.ini.sample config.ini
fi

# set alias
if [[ $SHELL = *zsh ]]; then
  echo "alias notificate='$(pwd)/notificate.py'" >> ~/.zsh_aliases
elif [[ $SHELL = *bash ]]; then
  echo "alias notificate='$(pwd)/notificate.py'" >> ~/.bash_aliases
fi
