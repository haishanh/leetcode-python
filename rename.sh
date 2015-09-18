#!/bin/bash

for f in $(ls | grep '-'); do
  new=$(echo ${f} | sed 's/-/_/g')
  git mv ${f} ${new}
done
