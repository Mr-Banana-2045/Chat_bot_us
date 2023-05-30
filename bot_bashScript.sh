#!/bin/bash

while sleep 0

do

read -p $'\e[1;33m msg >\e[0m ' text

if echo "$text" | grep -q "hello"; then

    echo -e "\033[94mBot:\033[92m hello my friend"

elif echo "$text" | grep -q "bye"; then

      echo -e "\033[94mBot: \033[92m bye my friend"

else

    echo -e "\033[91merror"

fi

done
