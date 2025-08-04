import socket

class Servidor:
    def __init__(self, ip='127.0.0.1', puerto=8090):
        self.ip = ip
        self.puerto = puerto
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def iniciar(self):
        self.servidor.bind((self.ip, self.puerto))
        self.servidor.listen(5)
        print(f"Servidor escuchando en {self.ip}:{self.puerto}")

        conexion, direccion = self.servidor.accept()
        print("Conexión establecida con:", direccion)

        mensaje = conexion.recv(1024).decode()
        print("Mensaje recibido del cliente:", mensaje)

        # se agregó lógica para personalizar la respuesta
        if "me llamo" in mensaje.lower():
            partes = mensaje.lower().split("me llamo")
            nombre = partes[1].strip().split()[0]
        elif "soy" in mensaje.lower():
            partes = mensaje.lower().split("soy")
            nombre = partes[1].strip().split()[0]
        else:
            nombre = "amigo"

    
        respuesta = f"Gracias por tu mensaje, {nombre}."   # se agrego mensaje personalizado "gracias"
        conexion.send(respuesta.encode())

        conexion.close()

if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciar()
