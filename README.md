## Chat Server

Realizado por: midoribluepink a modo de práctica

Consiste de 3 *scripts*. El primero, **server.py**, gestiona el Servidor que tiene como *host* el equipo local y abrirá el puerto 1234 esperando una conexión mediante el protocolo TCP. El *script* **client.py**
gestiona el Cliente del servidor y, al ejecutarse, se conectará automáticamente al servidor *localhost:1234*. Una vez conectados, el primero en enviar un mensaje será el Cliente, 
después el Servidor y así sucesivamente. La conexión se cierra para ambos cuando el Cliente manda la cadena *exit()*.

### Funcionamiento

Al ejecutar `python3 server.py`:

![imagen](https://github.com/user-attachments/assets/a12f2596-7220-407a-a95b-2c8d47e28b43)

se espera la conexión del cliente. Después ejecutamos `python3 client.py`.

Salida de **server.py**:

![imagen](https://github.com/user-attachments/assets/353c63b4-adf9-4bae-8beb-3aa10b8f0697)

Salida de **client.py**:

![imagen](https://github.com/user-attachments/assets/2725df12-27c4-492e-9e89-a2e43d9f5c50)

En este momento es el Cliente quien tiene que enviar el primer mensaje. Salida de **server.py**:

![imagen](https://github.com/user-attachments/assets/ef0008a5-cf86-47a4-98a4-beac21bf8d92)

Y el Servidor puede contestar al cliente. Salida de **client.py**:

![imagen](https://github.com/user-attachments/assets/62758f74-1668-43f0-a1d5-9c03ea9b92ef)

De este modo se pueden enviar y recibir mensajes. Para cerrar la conexión el Cliente deberá mandar la cadena *exit()*.

Salida **server.py**:

![imagen](https://github.com/user-attachments/assets/f9084cf7-a221-4dea-9f74-953e694d5d40)

Salida **client.py**:

![imagen](https://github.com/user-attachments/assets/d8005322-8265-4f06-a015-552777cc37b9)

### intercept.sh

El *script* **intercept.sh** utiliza tshark para interceptar los paquetes enviados por el protocolo TCP dentro de la misma máquina y los muestra. Para utilizar **intercept.sh** no hay
que hacer nada más que ejecutarlo `bash intercept.sh`:

![imagen](https://github.com/user-attachments/assets/69365edf-3555-4e4e-a9f1-6b547d5d75bb)

