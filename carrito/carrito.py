class Carrito:
    def __init__(self, request):
        self.request=request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        #else:
        self.carrito = carrito

    def Agregar (self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carrito.keys():
            self.carrito[producto.id]={
                "producto_id":producto_id,
                "nombre":producto.nombre,
                "descripcion":producto.descripcion,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen_url": producto.imagen.url if producto.imagen else None

            }
        else:
            for key, value in self.carrito.items():
                if key==producto_id:
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.guardar_carrito()  

    def guardar_carrito(self):      
        self.session["carrito"]  = self.carrito  
        self.session.modified = True

    def eliminar_producto(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar_carrito()

    def restar_producto(self, producto):
        producto_id = str(producto.id)
        for key, value in self.carrito.items():
            if key == producto_id:
                value["cantidad"] = value["cantidad"] -1
                if value["cantidad"]<1:
                    self.eliminar_producto(producto)
                break
        self.guardar_carrito()

    def limpiar_carrito(self):
        self.session["carrito"]={}
        self.session.modified = True