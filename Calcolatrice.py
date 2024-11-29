import tkinter as tk

Finestra = tk.Tk()
Finestra.title("Calcolatrice")
Finestra.geometry("600x800")
Finestra.resizable(False,False)
Finestra.configure(background="gray")

input_num1 = tk.Entry(Finestra)
input_num1.grid(row=0, column=0, sticky="W",padx=20,pady=0)

input_num2 = tk.Entry(Finestra)
input_num2.grid(row=0, column=0, sticky="W",padx=250,pady=20)

def CalcoloSomma():
    risultato=""
    testo1=input_num1.get()
    testo2=input_num2.get()
    num1 = int(testo1)
    num2 = int(testo2)
    risultato =num1+num2
    text__output1 = tk.Label(Finestra, text=risultato, fg="#FF0000", font=("Helvetica",16))
    text__output1.grid(row=2, column=0, sticky="W",padx=100,pady=20)

def CalcoloSottrazione():
    risultato=""
    testo1=input_num1.get()
    testo2=input_num2.get()
    num1 = int(testo1)
    num2 = int(testo2)
    risultato =num1-num2
    text__output2 = tk.Label(Finestra, text=risultato, fg="#FF0000", font=("Helvetica",16))
    text__output2.grid(row=3, column=0, sticky="W", padx=100,pady=20)

def CalcoloMoltiplicazione():
    risultato=""
    testo1=input_num1.get()
    testo2=input_num2.get()
    num1 = int(testo1)
    num2 = int(testo2)
    risultato =num1*num2
    text__output3 = tk.Label(Finestra, text=risultato, fg="#FF0000", font=("Helvetica",16))
    text__output3.grid(row=4, column=0, sticky="W", padx=100,pady=20)

def CalcoloDivisione():
    risultato=""
    testo1=input_num1.get()
    testo2=input_num2.get()
    num1 = int(testo1)
    num2 = int(testo2)
    if(num2==0 and num1==0):
        text__output4 = tk.Label(Finestra, text="Indefinito", fg="#FF0000", font=("Helvetica",16))
        text__output4.grid(row=5, column=0, sticky="W",padx=100,pady=20)
    elif(num2==0):
        text__output4 = tk.Label(Finestra, text="Impossibile", fg="#FF0000", font=("Helvetica",16))
        text__output4.grid(row=5, column=0, sticky="W",padx=100,pady=20)
    else:
        risultato = num1/num2
        text__output4 = tk.Label(Finestra, text=risultato, fg="#FF0000", font=("Helvetica",16))
        text__output4.grid(row=5, column=0, sticky="W",padx=100,pady=20)
    

button = tk.Button(Finestra, text="+", command=CalcoloSomma)
button.grid(row=2, column=0, sticky="W")

button = tk.Button(Finestra, text="-", command=CalcoloSottrazione)
button.grid(row=3, column=0, sticky="W")

button = tk.Button(Finestra, text="*", command=CalcoloMoltiplicazione)
button.grid(row=4, column=0, sticky="W")

button = tk.Button(Finestra, text="/", command=CalcoloDivisione)
button.grid(row=5, column=0, sticky="W")

if __name__ == "__main__":
    Finestra.mainloop()