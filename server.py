#!/usr/bin/env python3

import socket # Importamos la librería socket

def start_chat_server(): #Definimos la función principal del servidor

    host = 'localhost' #El host es el mismo ordenador en el que estamos
    port = 1234 # Elegimos un puerto cualquiera

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Creamos el socket del servidor
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Configurmos para que se pueda reutilizar la dirección si se cierra el programa
        s.bind((host, port)) #Abrimos el servidor
        s.listen(1) #Ponemos el servidor en escucha

        print(f"[+] Servidor abierto en {host}:{port}. Listo para entablar conexión...")

        client_socket, addr = s.accept() #Aceptamos la conexión y guardamos el socket del cliente y su dirección

        print(f"\n[+] Se ha conectado {addr}")

        while True: #Empezamos el bucle del chat

            data = client_socket.recv(1024).strip().decode() # Recibimos la información del cliente

            if data == 'exit()': # Si es la cadena 'exit()' cerramos la conexión
                print(f"\n[+] Conexión cerrada")
                break

            print(f"\n[+] Cliente dice: {data}")

            message = input("\n[+] Respuesta servidor: ") #Solicitamos la respuesta del servidor

            client_socket.send(message.encode()) # Enviamos la respuesta del servidor al cliente



start_chat_server() # Iniciamos el chat server
