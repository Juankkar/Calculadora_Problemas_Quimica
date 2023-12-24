#!/usr/bin/env python

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox


while True: 

	def imprimir_seleccion():
		seleccion = entry_eleccion.get()
		seleccion
		ventana.destroy()  # Cierra la ventana después de imprimir la selección

	ventana = tk.Tk()
	ventana.title("CÁLCULOS DE QUÍMICA")

	# Variable para almacenar la selección
	seleccion_var = tk.StringVar()

	label_eleccion = tk.Label(ventana, text=
"""
Elige la función que necesites (selecciona en número de la función):
1: Moles
2: Molaridad

Para salir escribe "exit"
""")
	label_eleccion.pack()

	entry_eleccion = tk.Entry(ventana, textvariable=seleccion_var)
	entry_eleccion.pack()

	boton_eleccion = tk.Button(ventana, text="Imprimir Selección y Salir", command=imprimir_seleccion)
	boton_eleccion.pack(pady=10)

	ventana.mainloop()

	# Después de salir de la interfaz gráfica, se ejecuta este código
	# y puedes acceder al valor seleccionado a través de seleccion_var.get()
	print("==> Opción seleccionada: ", seleccion_var.get())

	if seleccion_var.get() == "1":

		def imprimir_seleccion_moles():
			seleccion_moles = entry_eleccion.get()
			seleccion_moles
			ventana_moles.destroy()  # Cierra la ventana después de imprimir la selección

		ventana_moles = tk.Tk()
		ventana_moles.title("CÁLCULOS DE QUÍMICA")

		# Variable para almacenar la selección
		seleccion_var_moles = tk.StringVar()

		label_eleccion_moles = tk.Label(ventana_moles, text=
"""
> Función de Moles: Moles = Masa / Masa Molecular
> Selecciona el parámetro que quieras calcular (numero):
1: Moles
2: Masa
3: Masa Molecular
""")
		label_eleccion_moles.pack()

		entry_eleccion = tk.Entry(ventana_moles, textvariable=seleccion_var_moles)
		entry_eleccion.pack()

		boton_eleccion_moles = tk.Button(ventana_moles, text="Imprimir Selección y Salir", command=imprimir_seleccion_moles)
		boton_eleccion_moles.pack(pady=10)

		ventana_moles.mainloop()

		# Después de salir de la interfaz gráfica, se ejecuta este código
		# y puedes acceder al valor seleccionado a través de seleccion_var.get()
		print("==> Opción seleccionada para la función de los Moles: ", seleccion_var_moles.get())

		def f_moles():
			try:
				if seleccion_var_moles.get() == "1":
					masa = float(entry_masa.get())
					mmolecular = float(entry_mmmolecular.get())
					operacion = f"Moles = {masa / mmolecular}"
				elif seleccion_var_moles.get() == "2":
					moles = float(entry_moles.get())
					mmolecular = float(entry_mmmolecular.get())			
					operacion = f"Masa = {moles * mmolecular}"
				elif seleccion_var_moles.get() == "3":
					moles = float(entry_moles.get())
					masa = float(entry_masa.get())
					operacion = f"Masa Molecular = {masa / moles}"
				else:
					messagebox.showerror("Error", "No has elegido ninguna de las opciones 1, 2, 3")
					return
			except ValueError:
				messagebox.showerror("ERROR!!!", ">>> Has añadido un valor en una casilla que no se requiere, revísa lo que quieres calcular. <<<")

			resultado_moles.set(operacion)

		def salir():
			ventana_operacion_moles.destroy()

		ventana_operacion_moles = tk.Tk()
		ventana_operacion_moles.title("""""")

		resultado_moles = tk.StringVar()
		label_mostrar_resultado = tk.Label(ventana_operacion_moles, textvariable=resultado_moles)
		label_mostrar_resultado.pack()

		# Entradas para las operaciones
		label_masa = tk.Label(ventana_operacion_moles, text="Masa = ")
		label_masa.pack()
		entry_masa = tk.Entry(ventana_operacion_moles)
		entry_masa.pack()

		label_moles = tk.Label(ventana_operacion_moles, text="Moles = ")
		label_moles.pack()
		entry_moles = tk.Entry(ventana_operacion_moles)
		entry_moles.pack()

		label_mmolecular = tk.Label(ventana_operacion_moles, text="Masa Molecular = ")
		label_mmolecular.pack()
		entry_mmmolecular = tk.Entry(ventana_operacion_moles)
		entry_mmmolecular.pack()

		boton_calculo_moles = tk.Button(ventana_operacion_moles, text="Calcular", command=f_moles)
		boton_calculo_moles.pack(pady=10)

		# Botón para salir
		boton_salir = tk.Button(ventana_operacion_moles, text="Salir", command=salir)
		boton_salir.pack(pady=10)

		ventana.mainloop()

	if seleccion_var.get() == "2":

		def imprimir_seleccion_molaridad():
			seleccion_molaridad = entry_eleccion.get()
			seleccion_molaridad
			ventana_moles.destroy()  # Cierra la ventana después de imprimir la selección

		ventana_moles = tk.Tk()
		ventana_moles.title("CÁLCULOS DE QUÍMICA")

		# Variable para almacenar la selección
		seleccion_var_molaridad = tk.StringVar()

		label_eleccion_molaridad = tk.Label(ventana_moles, text=
"""
> Función de Molaridad: Molaridad = Moles de soluto / Volumen de disolución
> Selecciona el parámetro que quieras calcular (numero):
1: Molaridad
2: Moles de Soluto
3: Volumen de Disolución
""")
		label_eleccion_molaridad.pack()

		entry_eleccion = tk.Entry(ventana_moles, textvariable=seleccion_var_molaridad)
		entry_eleccion.pack()

		boton_eleccion_molaridad = tk.Button(ventana_moles, text="Imprimir Selección y Salir", command=imprimir_seleccion_molaridad)
		boton_eleccion_molaridad.pack(pady=10)

		ventana_moles.mainloop()

		# Después de salir de la interfaz gráfica, se ejecuta este código
		# y puedes acceder al valor seleccionado a través de seleccion_var.get()
		print("==> Opción seleccionada para la función de la Molaridad: ", seleccion_var_molaridad.get())

		def f_molaridad():
			try:
				if seleccion_var_molaridad.get() == "1":
					moles = float(entry_moles.get())
					volumen = float(entry_volumen.get())
					operacion = f"Molaridad = {moles / volumen}"
				elif seleccion_var_molaridad.get() == "2":
					molaridad = float(entry_molaridad.get())
					volumen = float(entry_volumen.get())			
					operacion = f"Moles de soluto = {molaridad * volumen}"
				elif seleccion_var_molaridad.get() == "3":
					moles = float(entry_moles.get())
					molaridad = float(entry_molaridad.get())
					operacion = f"Volumen de Disolución = {moles / molaridad}"
				else:
					messagebox.showerror("Error", "No has elegido ninguna de las opciones 1, 2, 3")
					return
			except ValueError:
				messagebox.showerror("ERROR!!!", ">>> Has añadido un valor en una casilla que no se requiere, revísa lo que quieres calcular. <<<")

			resultado_molaridad.set(operacion)

		def salir():
			ventana_operacion_molaridad.destroy()

		ventana_operacion_molaridad = tk.Tk()
		ventana_operacion_molaridad.title("""""")

		resultado_molaridad = tk.StringVar()
		label_mostrar_resultado = tk.Label(ventana_operacion_molaridad, textvariable=resultado_molaridad)
		label_mostrar_resultado.pack()

		# Entradas para las operaciones
		label_moles = tk.Label(ventana_operacion_molaridad, text="Moles de soluto = ")
		label_moles.pack()
		entry_moles = tk.Entry(ventana_operacion_molaridad)
		entry_moles.pack()

		label_molaridad = tk.Label(ventana_operacion_molaridad, text="Molaridad = ")
		label_molaridad.pack()
		entry_molaridad = tk.Entry(ventana_operacion_molaridad)
		entry_molaridad.pack()

		label_volumen = tk.Label(ventana_operacion_molaridad, text="Volumen de disolución = ")
		label_volumen.pack()
		entry_volumen = tk.Entry(ventana_operacion_molaridad)
		entry_volumen.pack()

		boton_calculo_molaridad = tk.Button(ventana_operacion_molaridad, text="Calcular", command=f_molaridad)
		boton_calculo_molaridad.pack(pady=10)

		# Botón para salir
		boton_salir = tk.Button(ventana_operacion_molaridad, text="Salir", command=salir)
		boton_salir.pack(pady=10)

		ventana.mainloop()

	elif seleccion_var.get() == "exit":
		break	

