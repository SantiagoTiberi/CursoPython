from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1 
        self._idteclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f"Id: {self._idteclado}, Marca: {self._marca}, tipo de entrada {self._tipo_entrada}"

if __name__ == '__main__':
    teclado1 = Teclado('Noganet', 'USB')
    print(teclado1)
    teclado2 = Teclado('Logitech', 'Bluetooth')
    print(teclado2)