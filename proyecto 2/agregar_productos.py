def agregar():
    import random
    import re
    from pathlib import Path    
    archivo=Path('codigos.txt')
    if not archivo.exists():
        with open("codigos.txt","w") as f:
            f.write("Codigo Producto")
            f.write("   "+"Nombre")
            f.write("   "+"Precio")
            f.write("   "+"Proveedor")
            f.write("   "+"Existencia")
            f.write("   "+"Estado")
            f.write("   "+"Descuento")
            f.close()
    abecedario=('abcdefghijklmnopqrstuvwxyz')
    abcd=("")
    codigo=("")
    comprovante=0;
    while comprovante<1:
        i=1
        while i<5:
            numero=str(random.randint(0,9))
            letra=random.choice(abecedario)
            abcd=(abcd+numero)
            codigo=codigo+numero+letra
            i=i+1
        with open("codigos.txt","r") as f:
            lineas=f.readlines()
            buscador=re.escape(codigo)
            patas=re.compile(buscador)
            for linea in lineas:
                if patas.search(linea):
                    comprovante=0;
                else:
                    comprovante=5
            f.close()
    f=open('codigos.txt','a')
    nombre=str(input("Ingrese el nombre del producto""\n"))
    existencia=str(input("Ingrese la cantidad del producto""\n"))
    precio=str(input("Ingrese el precio Q.""\n"))
    proveedor=str(input("Nombre del proveedor""\n"))
    estado=str(input("Estado""\n"))
    descuento=str(input("Ingrese el numero de porcentaje de descueto N%""\n"))
    f.write("\n"+codigo)
    f.write(" "+nombre)
    f.write(" "+precio)
    f.write(" "+proveedor)
    f.write(" "+existencia)
    f.write(" "+estado)
    f.write(" "+descuento)
    f.close()