import tkinter as tk #możliwość wyświetlania i wpisywania elementów w oknie
from tkinter import ttk 
from tkinter import messagebox #wyświetlanie komunikatów
import tkcalendar as tkc 
import pymysql
from datetime import datetime


#~~~~~~~~~~~~~~~~~~~~~~wywołanie okna~~~~~~~~~~~~~~~~~~~~~~~~~~
###############################################################

uzytkownik_window = tk.Tk() #wywołanie okna
uzytkownik_window.title("OKNO UŻYTKOWNIKA")
uzytkownik_window.geometry("400x300") #rozmiar okna 
uzytkownik_window.resizable(0,0) #zablokowanie zmiany rozmiaru okna

#~~~~~~~~~~~~~~~~~~~~~~łączenie z bazą danych~~~~~~~~~~~~~~~~~~
###############################################################

wypozyczalnia_samochodow = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database='wypozyczalnia_samochodow'
    )
cursor = wypozyczalnia_samochodow.cursor()

#tabele marek i modeli samochodów 
marki = []
modele = []
ceny_suma =[]
id_samochodu =[]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~funkcje ~~~~~~~~~~~~~~~~~~~~~~~~~~
###############################################################

def model(*args): #zapytanie do bazy danych o model samochodu
    query = ("SELECT model FROM samochody WHERE marka = '"+sel1.get()+"'")
    cursor.execute(query)
    modele= [r for r, in cursor]
    kafelek_model['values'] = modele

def cena(*args): #wyświetlanie ceny wypożyczenia za 1 dzień
    query = ("SELECT cena FROM samochody WHERE model = '"+sel2.get()+"'")
    cursor.execute(query)
    ceny = [r for r, in cursor]
    title_cena.config(text= ("Cena wypożyczenia za 1 dzień: " + str(ceny[0]) +" PLN" ))
    

def show_price(*args): #pokazanie ceny oraz ilość dni na wypożyczeniu
    date_format = "%Y-%m-%d"
    diff = datetime.strptime(str(cal_stop.get_date()),date_format) - datetime.strptime(str(cal_start.get_date()),date_format)
    days=diff.days
    if days >0:
        query =("SELECT cena*"+ str(days)+" FROM samochody WHERE model = '"+sel2.get()+"'")
        cursor.execute(query)
        ceny_suma = [r for r, in cursor]
        messagebox.showinfo('Ilość dni oraz cena',"Cena za wypożyczenie "+ kafelek_marka.get() +" "+ kafelek_model.get()+ " na okres " + str(days) + " dni wynosi: \n"+ str(ceny_suma[0])+" PLN") 
    else: 
        messagebox.showerror("Nieprawidłowe dane","Wprowadź poprawne dane wypożyczenia")

def accept():#okno potwierdzenia rezerwacji
    date_format = "%Y-%m-%d"
    diff = datetime.strptime(str(cal_stop.get_date()),date_format) - datetime.strptime(str(cal_start.get_date()),date_format)
    days=diff.days
    #data_start = datetime.strftime(cal_start.get_date(),date_format)
    data_start = cal_start.get_date()
    data_stop = cal_stop.get_date()
    #data_stop = datetime.strftime(cal_stop.get_date(),date_format)
    print(data_start,data_stop)
    if days >0:
        query =("SELECT cena*"+ str(days)+" FROM samochody WHERE model = '"+sel2.get()+"'")
        cursor.execute(query)
        ceny_suma = [r for r, in cursor]
        query2 =("SELECT id_samochodu FROM samochody WHERE model = '"+sel2.get()+"'")
        cursor.execute(query2)
        id_samochodu = [r for r, in cursor]
        answer = messagebox.askquestion("Potwierdź wybór","Wybrany pojazd to: " + kafelek_marka.get() +" "+ kafelek_model.get()+ "\n Data wypożyczenia: \n OD - "+ str(cal_start.get_date()) +" DO "+ str(cal_stop.get_date())+"\nCena całkowita wynosi: "+ str(ceny_suma[0])+" PLN")
        if answer == "yes":
            try:
                query2 ='INSERT INTO dane_wypozyczen (id_klienta,id_samochodu,data_wyp,data_zwr,suma) VALUES (%s,%s,%s,%s,%s)'
                cursor.execute(query2,(2,id_samochodu,data_start,data_stop,ceny_suma[0]))
                wypozyczalnia_samochodow.commit()
                messagebox.showinfo("Rezerwacja","Dokonano rezerwacji pojazdu, zgłoś się do salonu")

            except Exception as e:
                wypozyczalnia_samochodow.rollback()
                print("Błąd",e)
                wypozyczalnia_samochodow.close()
        else:
            pass
    else: 
        messagebox.showerror("Nieprawidłowe dane","Wprowadź poprawne dane wypożyczenia")

#~~~~~~~~~~~~~~~~~~napisy wyświetlane w oknie~~~~~~~~~~~~~~~~~~
###############################################################

main_title = tk.Label(uzytkownik_window,
    text='WYBIERZ MARKĘ SAMOCHODU', 
    font=('Microsoft Yahei UI Light',
    13,
    'bold')
    )
main_title.place(x=65,y=30) #umiejscowienie nagłówka

title_samochod = tk.Label(uzytkownik_window, 
    text="",
    font=('Microsoft Yahei UI Light',
    9,
    'bold')
    )
title_samochod.place(x=85,y=220)

title_data = tk.Label(uzytkownik_window, 
    text="",
    font=('Microsoft Yahei UI Light',
    9,
    'bold')
)
title_data.place(x=85,y=240)

title_cena = tk.Label(uzytkownik_window,
    text="",
    font=('Microsoft Yahei UI Light',
    9,
    'bold')
)
title_cena.place(x=65,y=240)

#~~~~~~~~~~~~~~~~~~zapytanie do BD o markę pojazdu~~~~~~~~~~~~~~~~~~
####################################################################



query1 = "SELECT samochody.marka FROM samochody GROUP BY samochody.marka ORDER BY samochody.marka "
cursor.execute(query1)
marki = [r for r, in cursor]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Listy rozwijalne~~~~~~~~~~~~~~~~~~~~~~~~
#####################################################################



sel1 = tk.StringVar()
sel2 = tk.StringVar()

kafelek_marka = ttk.Combobox(uzytkownik_window,values=marki,textvariable=sel1)
kafelek_marka.insert(0,"Marka")
kafelek_marka.place(x=130,y=60)

sel1.trace('w',model)
sel2.trace('w',cena)
 
kafelek_model = ttk.Combobox(uzytkownik_window,values=[" "],textvariable=sel2)
kafelek_model.insert(0,"Model")
kafelek_model.config(values = modele)
kafelek_model.place(x=130,y=100)    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~kalendarze~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################

cal_start = tkc.DateEntry(uzytkownik_window,selectmode = "day")
cal_start.place(x=150,y=130)

cal_stop = tkc.DateEntry(uzytkownik_window,selectmode = "day")
cal_stop.place(x=150,y=160)
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~przyciski~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#####################################################################

accept_button = tk.Button(uzytkownik_window,text="WYBIERZ",command=accept)
accept_button.place(x=200,y=190)

show_price_button = tk.Button(uzytkownik_window,text="OFERTA",command=show_price)
show_price_button.place(x=140,y=190)

#####################################################################

uzytkownik_window.mainloop()