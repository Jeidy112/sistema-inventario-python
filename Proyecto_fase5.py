print("\nSISTEMA DE AUDITORÍA Y REABASTECIMIENTO DE INVENTARIO TIENDA BUEN DÍA")
print("------------------------------------------------------------------------")
# Matriz de inventario
# [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    [101, "Chocolate", 15, 30],
    [102, "Azucar", 25, 20],
    [103, "Panela", 11, 16],
    [104, "Mermelada", 20, 15],
    [105, "café", 20, 28],
    [106, "Arroz", 30, 45]
    ]
# Calcular cantidad exacta a Rebastecer
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:

        return stock_minimo - stock_actual

    # Si el stock es suficiente no se solicita nada
    else:
        return 0
print("\n════REPORTE ACTUAL DE REABASTECIMIENTO DE PRODUCTOS EN INVENTARIO════\n")

# Verificación de productos en inventario
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

   # Cálculo de la cantidad a solicitar
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar información del articulo
    print(f"Codigo del articulo: {codigo}")
    print(f"Nombre del articulo: {nombre}")
    print(f"Stock actual: {stock_actual}")
    print(f"Stock minimo requerido: {stock_minimo}")

    # Validar si necesita reabastecimiento
    if cantidad_pedir > 0:
        print(f"Cantidad a solicitar: {cantidad_pedir}")
        print("Estado: REQUIERE REABASTECIMIENTO")

    else:
        print("Cantidad a solicitar: 0")
        print("Estado: STOCK SUFICIENTE")

    print("----------------------------------------------")
