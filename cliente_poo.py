import socket 
class Cliente: 
    def __init__(self, ip='127.0.0.1', puerto=9001): 
       self.ip = ip 
       self.puerto = puerto 
       self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    def enviar_mensaje(self): 
       self.cliente.connect((self.ip, self.puerto)) 
       mensaje = input("Escribe un mensaje para el servidor: ") 
       self.cliente.send(mensaje.encode()) 
       self.cliente.close() 
       print("El mensaje fue enviado con exito") # print para confirmar el envío exitoso
if __name__ == "__main__": 
 cliente = Cliente() 
 cliente.enviar_mensaje() 
