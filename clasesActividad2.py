class clasesActividad2():

    nombre = ""
    tarjeta = 0
    cantidadCompradores = 0
    cantidadBoletas = 0
    total=0.0

    def comprobarCompradores(self):

        cantidadMaximaParaVender = self.cantidadCompradores * 7

        if(self.cantidadBoletas > cantidadMaximaParaVender):
            return "No se puede comprar mas de {}".format(cantidadMaximaParaVender)
        elif(self.cantidadBoletas <= cantidadMaximaParaVender):
            self.operacion()
            return self.total
        

    def operacion(self):
        
        if(self.cantidadBoletas > 5):
            descuento = 0.15
        elif(self.cantidadBoletas <= 5 and self.cantidadBoletas >= 3 ):
            descuento = 0.10
        elif(self.cantidadBoletas <= 2):
            descuento = 0

        totalPrecioBoletas = self.cantidadBoletas * 12
    
        self.total = totalPrecioBoletas - (totalPrecioBoletas * descuento)

        if(self.tarjeta == 1):
            self.total = self.total - (self.total * 0.10)
37.8
252

214.2
21.42
        


