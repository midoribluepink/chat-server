#!/bin/bash

# Códigos de colores para la salida de la terminal.
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

#Función CTRL+C
function ctrl_c(){
  echo -e "${redColour}[!] Saliendo...${endColour}"
  tput cnorm; exit 1
}

#Capturar el ctrl_c
trap ctrl_c INT

tput civis #Ocultar el cursor de la terminal

echo -e "${yellowColour}[+]${endColour} ${grayColour}¡Bienvenido al interceptor de chats!${endColour}\n" 

echo -e "${yellowColour}[+]${endColour} ${grayColour}A continuación se muestran los${endColour} ${purpleColour}mensajes${endColour} ${redColour}incerceptados${endColour}${grayColour}:${endColour}\n"

stdbuf -oL tshark -i lo -Y "tcp" -e data.data -Tfields 2>/dev/null | while read -r linea; do #Interceptar los datos con tshark
  
  mensaje=$(echo "$linea" | xxd -ps -r) #Decodificar cada línea

  if [ $linea ]; then #Comprobar que no sea una línea vacía
    
    echo -e "${blueColour}Incerceptado:${endColour} ${grayColour}$(echo "$linea" | xxd -ps -r)${endColour}\n"

  fi

done
