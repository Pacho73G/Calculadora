from ast import Expression
from tkinter import *
from tkinter import font as tkfont

root = Tk()
root.title("Calculadora Moderna")
root.configure(bg="#f0f0f0")

# Colores
COLOR_BG = "#f0f0f0"
COLOR_BTN = "#ffffff"
COLOR_TEXT = "#333333"
COLOR_OPERATOR = "#4a90e2"
COLOR_EQUAL = "#4CAF50"
COLOR_CLEAR = "#FF5722"

# Configurar el grid para que sea expandible
for i in range(6):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# Crear una fuente personalizada para el display
display_font = tkfont.Font(family="Helvetica", size=24, weight="bold")

display = Entry(root, font=display_font, justify="right", bd=0, bg=COLOR_BG, fg=COLOR_TEXT)
display.grid(row=0, column=0, columnspan=6, sticky='nsew', padx=20, pady=20)

i = 0

def obtener(n):
    global i
    display.insert(i, n)
    i += 1

def operador(operacion):
    global i
    tam = len(operacion)
    display.insert(i, operacion)
    i += tam

def limpiar():
    display.delete(0, END)

def undo():
    estado = display.get()
    if len(estado):
        nuevoEstado = estado[:-1]
        limpiar()
        display.insert(0, nuevoEstado)
    else:
        limpiar()
        display.insert(0, 'Error')

def calcular():
    estado = display.get()
    try:
        math_expression = compile(estado, 'app.py', 'eval')
        resultado = eval(math_expression)
        limpiar()
        display.insert(0, resultado)
    except Exception as identifier:
        limpiar()
        display.insert(0, 'Error')

# Crear una fuente personalizada para los botones
button_font = tkfont.Font(family="Helvetica", size=16)

# Función para crear botones
def crear_boton(texto, comando, fila, columna, colspan=1, bg_color=COLOR_BTN, fg_color=COLOR_TEXT):
    btn = Button(root, text=texto, command=comando, font=button_font, bd=0, bg=bg_color, fg=fg_color, activebackground="#e0e0e0", activeforeground=fg_color)
    btn.grid(row=fila, column=columna, columnspan=colspan, sticky='nsew', padx=5, pady=5)

# Botones de números
numeros = [
    (7, 2, 0), (8, 2, 1), (9, 2, 2),
    (4, 3, 0), (5, 3, 1), (6, 3, 2),
    (1, 4, 0), (2, 4, 1), (3, 4, 2),
    (0, 5, 1)
]

for num, fila, columna in numeros:
    crear_boton(str(num), lambda x=num: obtener(x), fila, columna)

# Botones de operaciones
crear_boton("AC", limpiar, 5, 0, bg_color=COLOR_CLEAR, fg_color="white")
crear_boton("%", lambda: operador("%"), 5, 2)
crear_boton("+", lambda: operador("+"), 2, 3, bg_color=COLOR_OPERATOR, fg_color="white")
crear_boton("-", lambda: operador("-"), 3, 3, bg_color=COLOR_OPERATOR, fg_color="white")
crear_boton("*", lambda: operador("*"), 4, 3, bg_color=COLOR_OPERATOR, fg_color="white")
crear_boton("/", lambda: operador("/"), 5, 3, bg_color=COLOR_OPERATOR, fg_color="white")
crear_boton("←", undo, 2, 4, 2, bg_color="#e0e0e0")
crear_boton("exp", lambda: operador("**"), 3, 4)
crear_boton("^2", lambda: operador("**2"), 3, 5)
crear_boton("(", lambda: operador("("), 4, 4)
crear_boton(")", lambda: operador(")"), 4, 5)
crear_boton("=", calcular, 5, 4, 2, bg_color=COLOR_EQUAL, fg_color="white")

# Establecer un tamaño mínimo para la ventana
root.minsize(400, 500)

root.mainloop()