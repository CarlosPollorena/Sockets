import socket


class ServidorChat:
    def __init__(self, ip='127.0.0.1', puerto=8090):
        self.ip = ip
        self.puerto = puerto
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def manejar_cliente(self, conexion, direccion):  # se agregó un método para manejar la conexión del cliente
        print("Conexión establecida con:", direccion)

        while True:
            datos = conexion.recv(1024).decode()
            if datos.lower() == "bye":       # se cambió la palabra clave "salir" por "bye"
                print("El cliente ha cerrado la conexión.")
                break

            print("Cliente dice:", datos)  # se cambió el prefijo automático de cliente a cliente dice
            mensaje = input("Servidor dice: ")  # se cambió el prefijo automático de servidor a servidor dice
            conexion.send(mensaje.encode())
            if mensaje.lower() == "bye":  # se cambió la palabra clave "salir" por "bye"
                print("Servidor cerró la conexión.")
                break

        conexion.close()

    def iniciar_chat(self):

        self.servidor.bind((self.ip, self.puerto))
        self.servidor.listen(1) 
        print(f"Servidor escuchando en {self.ip}:{self.puerto}")
        conexion, direccion = self.servidor.accept()
        print("Conexión establecida con:", direccion)

        while True:
            datos = conexion.recv(1024).decode()
            if datos.lower() == "bye":       ## se cambió la palabra clave "salir" por "bye"
                print("El cliente ha cerrado la conexión.")
                break

            print("Cliente dice:", datos) # se cambio el prefijo automatico de cliente a cliente dice
            mensaje = input("Servidor dice: ")  # se cambio el prefijo automatico de servidor a servidor dice
            conexion.send(mensaje.encode())
            if mensaje.lower() == "bye":         # se cambió la palabra clave "salir" por "bye"
                print("Servidor cerró la conexión.")
                break

        conexion.close()

if __name__ == "__main__":
    servidor = ServidorChat()
    servidor.iniciar_chat()
