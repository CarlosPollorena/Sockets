import socket  

class ClienteChat: 
    def __init__(self, ip='127.0.0.1', puerto=8090): 
        self.ip = ip 
        self.puerto = puerto 
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    def iniciar_chat(self): 
        self.cliente.connect((self.ip, self.puerto)) 
                
        while True: 
            mensaje = input("Cliente dice: ") # Se cambio a "Cliente dice" para mayor claridad
            self.cliente.send(mensaje.encode()) 

            if mensaje.lower() == "bye":  # se cambio la palabra clave "salir" por "bye"
                print("Cliente cerró la conexión.") 
                break 

            respuesta = self.cliente.recv(1024).decode()

            if respuesta.lower() == "bye":  # se cambio la palabra clave "salir" por "bye"
                print("El servidor ha cerrado la conexión.") 
                break 

            print("Servidor:", respuesta) 
        
        self.cliente.close() 

if __name__ == "__main__": 
    cliente = ClienteChat() 
    cliente.iniciar_chat()



