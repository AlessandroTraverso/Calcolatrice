import tkinter as tk

#Creazione finestra

window = tk.Tk()
window.title("La mia finestra")
window.geometry("600x600")
window.resizable(True,False)
window.configure(background="brown")

#Crea etichetta

etichetta=tk.Label(window, text="La mia etichetta", fg="#999900", font=("Helvetica", 16))
etichetta.grid(row=0, column=0, sticky="W",padx=10,pady=20)

#Funzione che stampa etichetta

def stampa_etichetta():
    text="Ok"
    text__output = tk.Label(window, text=text, fg="#999900", font=("Helvetica", 16))
    text__output.grid(row=5, column=0, sticky="S",padx=50,pady=50)

#Bottone

first__button = tk.Button(text="Clicca!", command=stampa_etichetta)
first__button.grid(row=1, column=0, sticky="S")

#Input

input__text = tk.Entry(window)
input__text.grid(row=3, column=0, sticky="W",padx=250,pady=20)

#Funzione che stampa etichetta da input

def stampa_etichetta_input():
    testo=input__text.get()
    text__output1 = tk.Label(window, text=testo, fg="#FF0000", font=("Helvetica",16))
    text__output1.grid(row=5, column=0, sticky="W")

#Input

input__text = tk.Entry(window)
input__text.grid(row=2, column=0, sticky="W")

#Bottone

second__button = tk.Button(window, text="Clicca!", command=stampa_etichetta_input)
second__button.grid(row=3, column=0, sticky="W")


if __name__ == "__main__":
    window.mainloop()

                   
