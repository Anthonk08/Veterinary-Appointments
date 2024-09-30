#importar tkinter
import tkinter as tk

#Modulos de tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font

from Invoices import *

from Conexion import *

class PetsForm:
    # Globals Variables
    global base
    base = None

    global textBoxId
    textBoxId = None

    global textBoxClient
    textBoxClient = None

    global textBoxTelephone
    textBoxTelephone = None

    global textBoxEmail
    textBoxEmail = None

    global comboService
    comboService = None

    global textBoxNamePet
    textBoxNamePet = None

    global comboSex
    comboSex = None

    global groupBox
    groupBox = None

    global tree
    tree = None

    def form(self, event=None):
        #Variables
        global textBoxId
        global textBoxClient
        global textBoxTelephone
        global textBoxEmail
        global comboService
        global textBoxNamePet
        global comboSex
        global base
        global groupBox
        global tree

        try:
            base = Tk()
            base.geometry("1500x350")
            base.title("Citas En El Veterinario. Formulario De Servicios")

            #Client informa1tion
            groupBox = LabelFrame(base, text="Datos Del Cliente", padx=5, pady=5)
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
            groupBox = LabelFrame(base, text="Datos De La Mascota", padx=5, pady=5)
            groupBox.grid(row=1, column=0, ipadx=5, pady=5)
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
            Button(groupBox, text="Guardar", font="bold", width=15, command= self.invoicesSaves).grid(row=3, column=0)
            Button(groupBox, text="Actualizar", font="bold", width=15, command= self.invoicesUpdates).grid(row=3, column=1)
            Button(groupBox, text="Borrar", font="bold", width=15, command= self.invoicesEliminate).grid(row=3, column=2)

            #Invoice list
            groupBox = LabelFrame(base, text="Lista de Facturas", padx=5, pady=5,)
            groupBox.grid(row=0, column=1, rowspan=2, padx=5, pady=5)
            #Treeview create
            tree = ttk.Treeview(groupBox, columns=("ID", "Cliente", "Telefono", "Correo Electronico", "Servicio", "Nombre de la Mascota", "Sexo"),show='headings', height=10,)
            tree.column("# 1", anchor=CENTER, width=50)
            tree.heading("# 1", text="ID")

            tree.column("# 2", anchor=CENTER, width=150)
            tree.heading("# 2", text="Cliente")

            tree.column("# 3", anchor=CENTER, width=100)
            tree.heading("# 3", text="Telefono")

            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Correo Electronico")

            tree.column("# 5", anchor=CENTER, width=150)
            tree.heading("# 5", text="Servicio")

            tree.column("# 6", anchor=CENTER, width=130)
            tree.heading("# 6", text="Nombre de la Mascota")

            tree.column("# 7", anchor=CENTER, width=100)
            tree.heading("# 7", text="Sexo")

            #Agregar datos a la tabla
            for row in CInvoices.showInvoice():
                tree.insert("","end",values=row)

            tree.bind("<<TreeviewSelect>>", self.selectDate)

            tree.pack()

            base.mainloop()

        except ValueError as error:
            print("Error al mostrar interfaz, error: {}".format(error))

    #Dates Save
    def invoicesSaves(self):
        global textBoxClient, textBoxTelephone, textBoxEmail, comboService, textBoxNamePet, comboSex, groupBox

        try:
            #Verificar que los widgets esten inicializados
            if textBoxClient is None or textBoxTelephone is None or textBoxEmail is None or comboService is None or textBoxNamePet is None or comboSex is None:
                print("Los Widgets no estan inicializados")
                return

            client = textBoxClient.get()
            telephone = textBoxTelephone.get()
            email = textBoxEmail.get()
            service = comboService.get()
            namePet = textBoxNamePet.get()
            sex = comboSex.get()

            CInvoices.enterInvoice(client, telephone, email, service, namePet, sex)
            messagebox.showinfo("Informacion", "La factura fue guardada")

            #Actualizar tabla
            self.updateTreeView()

            #Limpiar campos
            textBoxClient.delete(0, END)
            textBoxTelephone.delete(0, END)
            textBoxEmail.delete(0, END)
            textBoxNamePet.delete(0, END)

        except ValueError as error:
            print("Error al ingresar factura {}".format(error))

    #Actualizar datos de la tabla
    def updateTreeView(self):
        global tree
        try:
            #Borrar los hijos de la tabla
            tree.delete(*tree.get_children())
            #Insertar los datos de la tabla
            date = CInvoices.showInvoice()
            #Agregar datos a la tabla
            for row in CInvoices.showInvoice():
                tree.insert("","end",values=row)

        except ValueError as error:
            print("Error al actualizar facturas {}".format(error))

    #Seleccionar dato de la tabla
    def selectDate(self, event=None):
        try:
            #obtener el ID de el dato seleccionado
            itemSelection = tree.focus()
            if itemSelection:
                values = tree.item(itemSelection)['values']
                textBoxId.delete(0, END)
                textBoxId.insert(0, values[0])
                textBoxClient.delete(0, END)
                textBoxClient.insert(0, values[1])
                textBoxTelephone.delete(0, END)
                textBoxTelephone.insert(0, values[2])
                textBoxEmail.delete(0, END)
                textBoxEmail.insert(0, values[3])
                comboService.set(values[4])
                textBoxNamePet.delete(0, END)
                textBoxNamePet.insert(0, values[5])
                comboSex.set(values[6])

        except ValueError as error:
            print("Error al seleccionar dato {}".format(error))

    #Actualizar dato de la tabla
    def invoicesUpdates(self):
        global textBoxId, textBoxClient, textBoxTelephone, textBoxEmail, comboService, textBoxNamePet, comboSex, groupBox

        try:
            #Verificar que los widgets esten inicializados
            if textBoxId is None or textBoxClient is None or textBoxTelephone is None or textBoxEmail is None or comboService is None or textBoxNamePet is None or comboSex is None:
                print("Los Widgets no estan inicializados")
                return

            idInvoice = textBoxId.get()
            client = textBoxClient.get()
            telephone = textBoxTelephone.get()
            email = textBoxEmail.get()
            service = comboService.get()
            namePet = textBoxNamePet.get()
            sex = comboSex.get()

            CInvoices.modifyData(idInvoice, client, telephone, email, service, namePet, sex)
            messagebox.showinfo("Informacion", "La factura fue actualizada")

            #Actualizar tabla
            self.updateTreeView()

            #Limpiar campos
            textBoxId.delete(0, END)
            textBoxClient.delete(0, END)
            textBoxTelephone.delete(0, END)
            textBoxEmail.delete(0, END)
            textBoxNamePet.delete(0, END)

        except ValueError as error:
            print("Error al actualizados factura {}".format(error))

    #Eliminar factura de la tabla
    def invoicesEliminate(self):
        global textBoxId, textBoxClient, textBoxTelephone, textBoxEmail, textBoxNamePet

        try:
            #Verificar que los widgets esten inicializados
            if textBoxId is None:
                print("Los Widgets no estan inicializados")
                return

            idInvoice = textBoxId.get()

            CInvoices.eliminateData(idInvoice)
            messagebox.showinfo("Informacion", "La factura fue eliminada")

            #Actualizar tabla
            self.updateTreeView()

            #Limpiar campos
            textBoxId.delete(0, END)
            textBoxClient.delete(0, END)
            textBoxTelephone.delete(0, END)
            textBoxEmail.delete(0, END)
            textBoxNamePet.delete(0, END)

        except ValueError as error:
            print("Error al eliminar datos {}".format(error))


app = PetsForm()
app.form()
