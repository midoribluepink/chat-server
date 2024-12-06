#!/usr/bin/env python3

import socket #Importamos la librería socket

def start_chat_client(): #Definimos la función de chat para el cliente

    host = 'localhost' #Definimos el host
    port = 1234 #Asignamos el mismo puerto que el server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #creamos el socket del cliente
        s.connect((host, port)) #Nos conectamos al servidor
        print(f"Bienvenido al Chat Server. Introduzca 'exit()' para terminar la conexión")

        while True: #Bucle principal del chat

            message = input("\n[+] Respuesta cliente: ") #Solicitamos la respuesta que se enviará al servidor

            s.send(message.encode()) #Enviamos el mensaje

            if message == 'exit()': #Si el mensaje es 'exit()' se cierra la conexión
                print(f"\n[+] Conexión cerrada")
                break

            data = s.recv(1024).strip().decode() #Recibimos el mensaje del servidor

            print(f"\n[+] Servidor dice: {data}") #Imprimimos la respuesta del servidor


start_chat_client() #Inciamos la función de chat del cliente
