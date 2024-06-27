# crear una clase CuentaBancaria que tendrá un balance y una tasa de interes
# se podrán usar sus métodos : deposito, retiro, mostrar_info, generar_interes 
# generar interes=> el balance se multiplica por la tasa y se suma al balance 

#Bonus: poder encadenar los métodos 

class CuentaBancaria:

    nombre_banco="BancoEstafo"
    
    def __init__(self , p_balance_inicial=0 , p_tasa = 0.01  ):
        self.balance = p_balance_inicial
        self.tasa_interes = p_tasa


    def deposito(self,monto_deposito):
        if monto_deposito>0:
            self.balance += monto_deposito
            print(f"deposito exitoso:{monto_deposito}, el balance actual es:{self.balance}")
        else:
            print("monto incorrecto")            
        return self

    def retiro(self,retiro):
        if retiro<self.balance:
            self.balance=self.balance-retiro
            print(f"retiro exitoso:{retiro}, el balance actual es:{self.balance}")
        else:
            print("monto incorrecto, el balance no es suficiente")
        return self

    def mostrar_info(self): 
        print(f"Balance: {self.balance:.2f}") 
        print(f"Tasa de interés: {self.tasa_interes:.2%}") 
        return self # Permite el encadenamiento

    def generar_interes(self):
        self.balance+=self.balance*self.tasa_interes
        return self
    
    def get_balance(self):
        return self.balance


#creacion de una cuenta : instanciar la clase! 
#cuenta1=CuentaBancaria( 100000 )

# cuenta1.deposito(50000) #150.000
# cuenta1.mostrar_info()
# cuenta1.retiro(20000) #130.000
# cuenta1.generar_interes() # 130.000+ 1300 = 131300 
# cuenta1.mostrar_info()

# cuenta2=CuentaBancaria(50000,0.1).deposito(50000).generar_interes().mostrar_info().retiro(10000).mostrar_info()






