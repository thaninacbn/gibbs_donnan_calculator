from tkinter import *

#partie calculatoire

def inconnue_x1():
    Y1 = float(y1a_value_entry.get())
    X2 = float(x2_value_entry.get())
    Y2 = float(y2a_value_entry.get())
    x1_result = (X2 * Y2) / Y1
    x1_answer.delete(0,END)
    x1_answer.insert(0,x1_result)


def inconnue_x2():
    X1 = float(x1_value_entry.get())
    Y1 = float(y1b_value_entry.get())
    Y2 = float(y2b_value_entry.get())
    x2_result= (X1 * Y1) / Y2
    x2_answer.delete(0, END)
    x2_answer.insert(0, x2_result)

#Interface graphique: création de la fenêtre
window= Tk()
window.title("Gibbs-Donan Calculator")
window.geometry("600x200")
window.config(background='#22223b')

#Création frame générale
frame= Frame(window, bg='#22223b')

#Création frame des entrées de X1
frame_x1= Frame(frame, bg='#22223b')

#Création frame donnant les concentrations à entrer dans chaque entry
frame_defx1=Frame(frame,bg='#22223b' )

#création de frames pour les labels
frame_label_x1= Frame(frame, bg='#22223b')
frame_label_x2= Frame(frame, bg='#22223b')
frame_answer_1 = Frame(frame, bg='#22223b')
frame_answer_2 = Frame(frame, bg='#22223b')

#création de frames pour les boutons
frame_button_x1= Frame(frame, bg='#22223b')
frame_button_x2 = Frame(frame, bg='#22223b')

#création frames réponses
frame_answer_x1=Frame(frame, bg='#22223b')
frame_answer_x2= Frame(frame, bg='#22223b')

#Placement des concentrations
variable_input1 = Label(frame_defx1, text="Entrez X2 ", font=("Arial", 11), bg='#22223b', fg='#f2e9e4')
variable_input1.pack()
variable_input2 = Label(frame_defx1, text="Entrez Y1 ", font=("Arial", 11), bg='#22223b', fg='#f2e9e4')
variable_input2.pack()
variable_input3 = Label(frame_defx1, text="Entrez Y2 ", font=("Arial", 11), bg='#22223b', fg='#f2e9e4')
variable_input3.pack()

#Input concentrations
label_x1= Label(frame_label_x1, text="L'inconnue est X1", font=("Arial", 12), bg='#22223b', fg='#f2e9e4')
label_x1.pack()
x2_value_entry = Entry(frame_x1, font=("Arial", 10), bg='#4a4e69', fg='#f2e9e4')
x2_value_entry.pack()
y1a_value_entry = Entry(frame_x1, font=("Arial", 10), bg='#4a4e69', fg='#f2e9e4')
y1a_value_entry.pack()
y2a_value_entry = Entry(frame_x1, font=("Arial", 10), bg='#4a4e69', fg='#f2e9e4')
y2a_value_entry.pack()

#Bouton calcul
x1_button=Button(frame_button_x1, text = "Calculer X1",font=("Arial", 10), bg='#22223b', fg='#f2e9e4', command=inconnue_x1 )
x1_button.pack()

#Résultat
x1_answer=Entry(frame_answer_1, bg='#22223b', fg='#f2e9e4')
x1_answer.pack()

#Frame indiquant les concentrations pour chaque entry, partie X2
frame_defx2=Frame(frame,bg='#22223b' )
variable_input3 = Label(frame_defx2, text="  Entrez X1 ", font=("Arial", 11), bg='#22223b', fg='#f2e9e4')
variable_input3.pack()
variable_input4 = Label(frame_defx2, text="  Entrez Y1 ", font=("Arial", 11), bg='#22223b', fg='#f2e9e4')
variable_input4.pack()
variable_input5 = Label(frame_defx2, text="  Entrez Y2 ", font=("Arial", 11), bg='#22223b', fg='#f2e9e4')
variable_input5.pack()

#Frame calculatoire partie X2
frame_x2= Frame(frame, bg='#22223b')
label_x2= Label(frame_label_x2, text="L'inconnue est X2", font=("Arial", 12), bg='#22223b', fg='#f2e9e4')
label_x2.pack()
x1_value_entry = Entry(frame_x2, font=("Arial", 10), bg='#4a4e69', fg='#f2e9e4')
x1_value_entry.pack()
y1b_value_entry = Entry(frame_x2, font=("Arial", 10), bg='#4a4e69', fg='#f2e9e4')
y1b_value_entry.pack()
y2b_value_entry = Entry(frame_x2, font=("Arial", 10), bg='#4a4e69', fg='#f2e9e4')
y2b_value_entry.pack()

#Bouton calcul X2
x2_button=Button(frame_button_x2, text = "Calculer X2",font=("Arial", 10), bg='#22223b', fg='#f2e9e4', command=inconnue_x2)
x2_button.pack()

#Résultat du calcul de X2
x2_answer=Entry(frame_answer_2, bg='#22223b', fg='#f2e9e4')
x2_answer.pack()

#Placement des widget dans la grille

frame_label_x1.grid(row=0,column=1,sticky=W)
frame_defx1.grid(row=1, column=0, sticky=W)
frame_x1.grid(row=1, column=1, sticky=W)
frame_button_x1.grid(row=2, column=1,sticky=W)
frame_answer_1.grid(row=3, column=1, sticky=W)

frame_label_x2.grid(row=0, column=3, sticky=W)
frame_defx2.grid(row=1, column=2, sticky=W)
frame_x2.grid(row=1, column=3, sticky=W)
frame_button_x2.grid(row=2, column=3, sticky=W)
frame_answer_2.grid(row=3, column=3, sticky=W)
frame.pack(expand=YES)

#l'erreur qui a rendu fou pendant 45 min: j'avais oublié le .grid qui empacte la frame MDR

#Lancement de la fenêtre
window.mainloop()