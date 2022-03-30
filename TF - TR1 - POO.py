

print("                                                                        ")
print("****************************DATOS DE ENTRADA****************************")
nombre = input("NOMBRE Y APELLIDO DEL TRABAJADOR :    ")
cat = input("CATEGORIA DEL TRABAJADOR         :    ")
hrx = int(input("INGRESAR HORAS EXTRAS            :    "))
tar = int(input("INGRESAR TARDANZA   (MINUTOS)    :    "))

class Trabajador:
    def __init__(self, nombre, ctg, hrx, tard):
        self.nombre = nombre
        self.cat = ctg
        self.hrx = hrx
        self.tar = tard
        self.sueldobasico = 0
        self.valorA = 0
        self.valorB = 0
        self.valorC = 0
        
# SUELDO BASiCO POR CATEGORIA
    def SueldoCat(self, cat):
        if self.cat=="A":
            self.sueldobasico=3000
        if self.cat=="B":
            self.sueldobasico=2500
        elif self.cat=="C":
            self.sueldobasico=2000
        return self.sueldobasico
    
# HORAS EXTRAS
    def HorasE(self,cat):
        if self.cat=="A" or "B" or "C":
            self.valorA = 1
        return self.valorA   
    
# PAGO POR HORA
    def PagoH(self):
        self.valorB=self.sueldobasico/240
        return self.valorB
    
# CONVERSION DE MINUTOS A HORAS
    def CTardanza(self,tar):
        self.valorC = self.tar/60
        return self.valorC


# VALORES
    def get_sueldobasico(self):
        return self.sueldobasico
    def get_ValorA(self):
        return self.valorA
    def get_ValorB(self):
        return self.valorB
    def get_ValorC(self):
        return self.valorC
    
    
BTrabajador = Trabajador(nombre, cat, hrx, tar)
BTrabajador.SueldoCat(cat)
BTrabajador.HorasE(cat)
BTrabajador.PagoH()
BTrabajador.CTardanza(tar)


class Boleta():
    
    Asueldo=BTrabajador.get_sueldobasico()
    ValorA=BTrabajador.get_ValorA()
    ValorB=BTrabajador.get_ValorB()
    ValorC=BTrabajador.get_ValorC()
    
    Adesc=0
    Aphx=0
    Asn=0
    
# TARDANZAS
    def DescuentoT(self):
        self.Adesc=self.ValorB*self.ValorC
        return self.Adesc
   
#PAGO DE HORAS EXTRAS
    def PHExtra(self, Hx):
        self.Aphx=self.ValorA*self.ValorB*Hx
        return self.Aphx
   
#SUELDO NETO
    def SNeto(self):
        self.Asn=(self.Asueldo+self.Aphx)-self.Adesc
        return self.Asn
    

Boleta_Pago=Boleta()

print("                                                                        ")
print("************************************************************************")
print("*****************************BOLETA DE PAGO*****************************")
print("- NOMBRE Y APELLIDO      :  ", nombre)
print("- CATEGORIA              :  ", cat)
print("- SUELDO BÁSICO          :  ", "S/.", BTrabajador.SueldoCat(cat))
print("- DESCUENTO TARDANZAS    :  ", "S/.", "{:.3f}".format(Boleta_Pago.DescuentoT()))
print("- PAGO POR HORAS EXTRAS  :  ", "S/.", "{:.3f}".format(Boleta_Pago.PHExtra(hrx)))
print("- SUELDO NETO            :  ", "S/.", "{:.3f}".format(Boleta_Pago.SNeto()))
print("                                                                        ")


