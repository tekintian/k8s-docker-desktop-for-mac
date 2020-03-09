#!/bin/bash

file="image_list"

if [ -f "$file" ]
then
  echo "file $file found."

  while IFS='=' read -r key value
  do
    #echo "${key}=${value}"
    docker pull ${value}
    docker tag ${value} ${key}
    echo "docker pull ${key} success."
    docker rmi ${value}
  done < "$file"

else
  echo "file $file not found."
fi
