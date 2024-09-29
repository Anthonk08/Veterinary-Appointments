#importar tkinter
import tkinter as tk

#Modulos de tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class PetsForm:
    def form(self):
        try:
            base = Tk()
            base.geometry("1840x340")
            base.title("Citas En El Veterinario. Formulario De Servicios")

            #Client informa1tion
            groupBox = LabelFrame(base, text="Datos Del Cliente", padx=20, pady=5)
            groupBox.grid(row=0, column=0, padx=10, pady=10)
            labelId = Label(groupBox, text="ID Factura", width=13, font=("arial", 12)).grid(row=0, column=0)
            textBoxId = Entry(groupBox)
            textBoxId.grid(row=0, column=1)

            labelClient = Label(groupBox, text="Cliente", width=13, font=("arial", 12)).grid(row=1, column=0)
            textBoxClient = Entry(groupBox)
            textBoxClient.grid(row=1, column=1)

            labelTelephone = Label(groupBox, text="Telefono", width=13, font=("arial", 12)).grid(row=2, column=0)
            textBoxTelephone = Entry(groupBox)
            textBoxTelephone.grid(row=2, column=1)

            labelEmail = Label(groupBox, text="Correo Electronico", width=15, font=("arial", 12)).grid(row=3, column=0)
            textBoxEmail = Entry(groupBox)
            textBoxEmail.grid(row=3, column=1)

            labelIdService = Label(groupBox, text="Servicio", width=15, font=("arial", 12)).grid(row=4, column=0)
            seleccionService = tk.StringVar()
            comboService = ttk.Combobox(groupBox, values=["Peluquería y baños", "Corte de uñas", "Limpieza de oídos", "Planes de nutrición", "Control de peso", "Reproducción asistida", "Control prenatal", "Limpieza dental", "Tratamientos periodontales", "Dermatología veterinaria", "Oncología", "Cardiología", "Análisis de laboratorio", "Radiografías", "Consultas veterinarias"], width=25, textvariable= seleccionService)
            comboService.grid(row=4, column=1)
            seleccionService.set("Peluquería y baños")

            #Pet information
            groupBox = LabelFrame(base, text="Datos De La Mascota", padx=20, pady=5)
            groupBox.grid(row=1, column=0, padx=10, pady=10)
            labelNamePet = Label(groupBox, text="Nombre de la Mascota", width=20, font=("arial", 12)).grid(row=0, column=0)
            textBoxNamePet = Entry(groupBox)
            textBoxNamePet.grid(row=0, column=1)

            labelIdPetSex = Label(groupBox, text="Sexo de la Mascota", width=15, font=("arial", 12)).grid(row=2, column=0)
            seleccionSex = tk.StringVar()
            comboSex = ttk.Combobox(groupBox, values=["Masculino", "Femenino"], textvariable= seleccionSex)
            comboSex.grid(row=2, column=1)
            seleccionSex.set("Masculino")

            #CRUD Buttons
            groupBox = LabelFrame(base, text="Edicion De Datos", padx=20, pady=5)
            groupBox.grid(row=2, column=0, padx=10, pady=10)
            Button(groupBox, text="Guardar", width=10).grid(row=3, column=0)
            Button(groupBox, text="Editar", width=10).grid(row=3, column=1)
            Button(groupBox, text="Borrar", width=10).grid(row=3, column=2)

            #Invoice list
            groupBox = LabelFrame(base, text="Lista de Facturas", padx=5, pady=5,)
            groupBox.grid(row=0, column=1, padx=5, pady=5)
            #Treeview create
            tree = ttk.Treeview(groupBox, columns=("ID", "Cliente", "Telefono", "Correo Electronico", "Servicio", "Nombre de la Mascota", "Sexo"),show='headings', height=5,)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="ID")

            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Cliente")

            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Telefono")

            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Correo Electronico")

            tree.column("# 5", anchor=CENTER)
            tree.heading("# 5", text="Servicio")

            tree.column("# 6", anchor=CENTER)
            tree.heading("# 6", text="Nombre de la Mascota")

            tree.column("# 7", anchor=CENTER)
            tree.heading("# 7", text="Sexo")

            tree.pack()

            base.mainloop()

        except ValueError as error:
            print("Error al mostrar interfaz, error: {}".format(error))

app = PetsForm()
app.form()
