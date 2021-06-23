from cargos import Cargo

class Empleado:
    secuencia = 0

    def __init__(self, nam, ica, sal, pos):
        self.codigo = self.generar_codigo()
        self.nombre = nam
        self.cedula = ica
        self.pago = sal
        self.cargo = pos

    def generar_codigo(self):
        Empleado.secuencia += 1
        return Empleado.secuencia

    def mostrar(self):
        print('código:{}, nombre:{}, cargo:{}-{}'.format(self.codigo, self.nombre, self.cargo.codigo, self.cargo.descripcion))


if __name__ == '__main__':
    cargo1 = Cargo('Docente')
    empleado1 = Empleado('Daniel', '0914', 500, cargo1)
    empleado1.mostrar()

    cargo2 = Cargo('Analista')
    empleado2 = Empleado('Ana', '0914', 500, cargo2)
    empleado2.mostrar()
    