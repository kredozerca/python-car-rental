from tkinter import * #możliwość wyświetlania i wpisywania elementów w oknie
from tkinter import messagebox #wyświetlanie komunikatów
import pymysql

main_window = Tk() #wywołanie okna
main_window.title("OKNO PRACOWNIKA")
main_window.geometry("800x600") #rozmiar okna 
main_window.resizable(0,0) #zablokowanie zmiany rozmiaru okna


label1 = Label(main_window,
    text='PRACOWNIK', 
    font=('Microsoft Yahei UI Light',
    13,
    'bold')
    )
label1.place(x=300,y=50) #umiejscowienie nagłówka



main_window.mainloop()

