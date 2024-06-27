# crear la clase usuario que tendra: nombre, una cuenta (SPOILER: despues podría tener varias)
# crear métodos : crear_nueva_cuenta , recibir_deposito, hacer_retiro, hacer_transferencia,mostrar_balance_usuario
# utilizar la clase CuentaBancaria
from cuenta_bancaria import CuentaBancaria

class Usuario:
    def __init__(self,nombre):
        self.nombre=nombre
        #self.cuenta=None
        self.cuentas=[] #lista de objetos
        
    def crear_nueva_cuenta(self, balance_inicial=0.0, tasa_interes=0.01):
        #self.cuenta = CuentaBancaria(balance_inicial, tasa_interes)
        cuenta_nueva=CuentaBancaria(balance_inicial, tasa_interes)
        self.cuentas.append(cuenta_nueva)
        return self

    def recibir_deposito(self,monto , indice ):
        # if nombre_cuenta in self.cuenta:
        #     self.cuenta[nombre_cuenta]+=monto
        #     print(f"Desposito de {monto} realizado en la cuenta {nombre_cuenta}")
        # else:
        #     print(f"La cuenta {nombre_cuenta} no existe")
        if indice < len(self.cuentas):
            self.cuentas[indice].deposito(monto)
        # if self.cuenta is not None:
        #     self.cuenta.deposito(monto)
            print(f"Desposito de {monto} realizado en la cuenta {indice} de {self.nombre}")
        else:
            self.crear_nueva_cuenta(monto)
            print(f"La cuenta de {self.nombre} no existe, se creo una nueva cuenta")
        return self
        

    def hacer_retiro(self,monto_retiro,indice):
        if indice < len(self.cuentas):
            self.cuentas[indice].retiro(monto_retiro)

        # if self.cuenta:
        #     self.cuenta.retiro(monto_retiro)
            print(f"Retiro de {monto_retiro} realizado en la cuenta {indice} de {self.nombre}")
        else:
            print(f"La cuenta de {self.nombre} no existe")
        # if self.balance>retiro:
        #     self.balance=self.balance-retiro
        #     print(f"Monto a retirar: {retiro}.")
        #     print(f"Nuevo Balance: {self.balance}.")
        # else:
            # print("Error, el monto a retirar excede el acutal balance.")
        return self
    
    def hacer_transferencia(self, cantidad,indice_cuenta_origen, otro_usuario,indice_cuenta_destino):

        if ( indice_cuenta_origen < len(self.cuentas)) and (indice_cuenta_origen < len(otro_usuario.cuentas)) :
            # if self.cuenta.balance >= cantidad:
            self.cuentas[indice_cuenta_origen].retiro(cantidad)
            otro_usuario.cuentas[indice_cuenta_destino].deposito(cantidad)
            print(f"Transferencia de {cantidad:.2f} realizada de {self.nombre} a {otro_usuario.nombre}.")
            # else:
            #     print("Fondos insuficientes para la transferencia.")
        else:
            print("Una de las cuentas no existe.")
        return self
    
    def mostrar_balance_usuario(self):
        for indice, cuenta in enumerate(self.cuentas):
            print(f"El balance de la cuenta {indice} de {self.nombre} es: {cuenta.get_balance()}")
        return self
    
    #a la vuelta probamos el código y modificamos para obtener multiples cuentas

pedro=Usuario("Pedro")
pedro.crear_nueva_cuenta(20000,0.02) 
pedro.crear_nueva_cuenta(10000,0.02) 
pedro.recibir_deposito(10000,0) 
pedro.hacer_retiro(5000,0)

jose=Usuario("Jose").crear_nueva_cuenta(100000,0.02) 
#enviamos una tef desde Jose a Pedro

jose.hacer_transferencia(10000,0,pedro,0).mostrar_balance_usuario()

pedro.mostrar_balance_usuario()


