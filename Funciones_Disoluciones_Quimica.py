#!/usr/bin/env python

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox

texto_moles ="""
> Función de Moles: Moles = Masa / Masa Molecular
> Selecciona el parámetro que quieras calcular (numero):
1: Moles
2: Masa
3: Masa Molecular
""" 

texto_molaridad="""
> Función de Molaridad: Molaridad = Moles de soluto / Volumen de disolución
> Selecciona el parámetro que quieras calcular (numero):
1: Molaridad
2: Moles de Soluto
3: Volumen de Disolución
""" 

texto_densidad="""
> Función de Densidad: Densidad = Masa / Volumen
> Selecciona el parámetro que quieras calcular (numero):
1: Densidad
2: Masa
3: Volumen
""" 

texto_riqueza="""
> Función de Riqueza, pureza, % masa, % peso: % Masa = Masa de Soluto / Masa de Disolución
> Selecciona el parámetro que quieras calcular (numero):
1: % Masa
2: Masa de Soluto
3: Masa de Disolución
""" 

texto_molalidad="""
> Función de Molalidad: Molalidad = Nº de Moles de Soluto / Kg de Disolvente
> Selecciona el parámetro que quieras calcular (numero):
1: Molalidad
2: Nº de Moles de Soluto
3: Kg de Disolvente
""" 
 
texto_frac_molar_soluto="""
> Función de Fracción Molar de Soluto: Xs = Nº de Moles de Soluto / Nº de Moles de Totales
> Selecciona el parámetro que quieras calcular (numero):
1: Xs
2: Nº de Moles de Soluto
3: Nº de Moles Totales
"""  

texto_frac_molar_disolvente="""
> Función de Fracción Molar de Disolvente: Xd = Nº de Moles de Disolvente / Nº de Moles de Totales
> Selecciona el parámetro que quieras calcular (numero):
1: Xd
2: Nº de Moles de Disolvente
3: Nº de Moles Totales
"""  

texto_gramos_litro="""
> Función de Gramos / Litro: Gramos / Litro = Gramos de Soluto / Litros de Disolución
> Selecciona el parámetro que quieras calcular (numero):
1: Gramos / Litro
2: Gramos de Soluto
3: Litros de Disolución
"""  
 

def funciones_quimicas(texto, texto1, texto2, texto3):
	def imprimir_seleccion():
		seleccion = entry_eleccion.get()
		seleccion
		ventana.destroy()  # Cierra la ventana después de imprimir la selección
	
	ventana = tk.Tk()
	ventana.title("CÁLCULOS DE QUÍMICA")
		
	# Variable para almacenar la selección
	seleccion_var = tk.StringVar()
	
	label_eleccion = tk.Label(ventana, text=texto)
		
	label_eleccion.pack()
	
	entry_eleccion = tk.Entry(ventana, textvariable=seleccion_var)
	entry_eleccion.pack()
	
	boton_eleccion = tk.Button(ventana, text="Seleccionar", command=imprimir_seleccion)
	boton_eleccion.pack(pady=10)
	
	ventana.mainloop()
	
	def f_calculo_quimica_lab():
		try:
			if seleccion_var.get() == "1":
				param2 = float(entry_param2.get())
				param3 = float(entry_param3.get())
				if texto == texto_riqueza:
					operacion = f"{texto1} = {param2 / param3 * 100}"
				else:
					operacion = f"{texto1} = {param2 / param3}"
			elif seleccion_var.get() == "2":
				param1 = float(entry_param1.get())
				param3 = float(entry_param3.get())			
				operacion = f"{texto2} = {param1 * param3}"
			elif seleccion_var.get() == "3":
				param1 = float(entry_param1.get())
				param2 = float(entry_param2.get())
				operacion = f"{texto3} = {param2 / param1}"
			else:
				messagebox.showerror("Error", "No has elegido ninguna de las opciones 1, 2, 3")
				return
		except ValueError:
			messagebox.showerror("ERROR!!!", ">>> Has añadido un valor en una casilla que no se requiere, revísa lo que quieres calcular. <<<")
	
		resultado.set(operacion)
	
	def salir():
		ventana_operacion.destroy()
	
	ventana_operacion = tk.Tk()
	if seleccion_var.get() == "1":	
		ventana_operacion.title(f"Función de {texto1}, parámetro a calcular: {texto1}")
	elif seleccion_var.get() == "2":
		ventana_operacion.title(f"Función de {texto1}, parámetro a calcular: {texto2}")
	elif seleccion_var.get() == "3":
		ventana_operacion.title(f"Función de {texto1}, parámetro a calcular: {texto3}")	

	resultado = tk.StringVar()
	label_mostrar_resultado = tk.Label(ventana_operacion, textvariable=resultado)
	label_mostrar_resultado.pack()
	
	# Entradas para las operaciones
	label_param2 = tk.Label(ventana_operacion, text=f"{texto2} = ")
	label_param2.pack()
	entry_param2 = tk.Entry(ventana_operacion)
	entry_param2.pack()
	
	label_param1 = tk.Label(ventana_operacion, text=f"{texto1} = ")
	label_param1.pack()
	entry_param1 = tk.Entry(ventana_operacion)
	entry_param1.pack()
	
	label_param3 = tk.Label(ventana_operacion, text=f"{texto3} = ")
	label_param3.pack()
	entry_param3 = tk.Entry(ventana_operacion)
	entry_param3.pack()
	
	boton_calculo = tk.Button(ventana_operacion, text="Calcular", command=f_calculo_quimica_lab)
	boton_calculo.pack(pady=10)
	
	# Botón para salir
	boton_salir = tk.Button(ventana_operacion, text="Salir", command=salir)
	boton_salir.pack(pady=10)
	
	ventana.mainloop()


while True: 

    def imprimir_seleccion():
        seleccion = seleccion_var.get()
        if seleccion == "exit":
            ventana.destroy()  # Cierra la ventana si la selección es "exit"
        else:
            print(f"Seleccionaste: {seleccion}")
            ventana.destroy()  # Cierra la ventana después de imprimir la selección
    
    ventana = tk.Tk()
    ventana.title("CÁLCULOS DE QUÍMICA")
    
    # Variable para almacenar la selección
    seleccion_var = tk.StringVar()
    
    label_eleccion = tk.Label(ventana, text=
    """
    Elige la función que necesites:
    """)
    label_eleccion.pack()
    
    # Crear botones de radio para las opciones
    opciones = [
        ("Moles", "1"),
        ("Molaridad", "2"),
        ("Densidad", "3"),
        ("Riqueza, pureza, % masa, % peso", "4"),
        ("Molalidad", "5"),
        ("Fracción molar soluto", "6"),
        ("Fración Molar disolvente", "7"),
        ("Gramos / Litro", "8"),
        ("Salir", "exit")
    ]
    
    for texto, valor in opciones:
        opcion_btn = tk.Radiobutton(ventana, text=texto, variable=seleccion_var, value=valor)
        opcion_btn.pack(anchor=tk.W)
    
    boton_eleccion = tk.Button(ventana, text="Seleccionar", command=imprimir_seleccion)
    boton_eleccion.pack(pady=10)
    
    ventana.mainloop()

    if seleccion_var.get() == "1":
        funciones_quimicas(texto_moles, "Moles", "Masa", "Masa Molecular")
    elif seleccion_var.get() == "2":
        funciones_quimicas(texto_molaridad, "Molaridad", "Moles de Soluto", "Volumen de Disolución")
    elif seleccion_var.get() == "3":
        funciones_quimicas(texto_densidad, "Densidad", "Masa", "Volumen")
    elif seleccion_var.get() == "4":
        funciones_quimicas(texto_riqueza, "Porecntaje_masa", "Masa de Soluto", "Masa de disolución")
    elif seleccion_var.get() == "5":
        funciones_quimicas(texto_molalidad, "Molalidad", "Nº de Moles de Soluto", "Nº de Moles Totales")
    elif seleccion_var.get() == "6":
        funciones_quimicas(texto_frac_molar_soluto, "Xs", "Nº de Moles de Soluto", "Nº de Moles Totales")  
    elif seleccion_var.get() == "7":
        funciones_quimicas(texto_frac_molar_disolvente, "Xd", "Nº de Moles de Disolvente", "Nº de Moles Totales")  
    elif seleccion_var.get() == "8":
        funciones_quimicas(texto_gramos_litro, "Gramos / Litro", "Gramos de Soluto", "Litros de Disolución")
    elif seleccion_var.get() == "exit":
        break