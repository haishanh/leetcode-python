#!/bin/bash

rename()
{
  for f in $(ls | grep '-'); do
    new=$(echo ${f} | sed 's/-/_/g')
    git mv ${f} ${new}
  done
}

move()
{
  for f in $(ls *.py); do
    git mv ${f} solutions
  done
}

case ${1} in
  rename)
    rename
    ;;
  move)
    move
    ;;
  *)
    echo "Do nothing"
    ;;
esac
