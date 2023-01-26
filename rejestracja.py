from tkinter import * #możliwość wyświetlania i wpisywania elementów w oknie
from tkinter import messagebox #wyświetlanie komunikatów
import pymysql





#FUNKCJE
def username_enter(znika): #funkcja usuwająca napis z pola tekstowego "Nazwa użytkownika"
    username.get()=='Email'
    username.delete(0,END)

def password_enter(znika): #funkcja usuwająca napis z pola tekstowego "Hasło" oraz zamieniająca wszystkie znaki na *
    password.get()=='Password'
    password.delete(0,END)
    password.config(show="*")
        

    
def data_checking(): #funkcja sprawdzająca dane do logowania
    if username.get()=='' or password.get()=='' or username.get()=='Email' or password.get()=='Password': #zostawienie pustych pól lowowania
        messagebox.showerror("Error","Uzupełnij dane logowania")
    else:
        try: #łączenie z bazą danych
            connection_database()
        except: # w przypadku pojawienia się błędu wyśiwetli się komunikat
            messagebox.showerror("Error","Brak połączenia z bazą danych.")
            return

        query = 'select * from dane_logowania where email=%s and haslo=%s' #zapytanie do BD o email i haslo
        cursor.execute(query,(username.get(),password.get()))
        row = cursor.fetchone()
 
        if row == None: # jeśli dane się nie zgadzają wyświetlany jest komunikat
            messagebox.showerror("Error","Niewłaściwy Email lub Hasło")
        else: #kiedy email i haslo są poprawne następuje zalogowanie użytkownika
            if row[3]=="yes":
                messagebox.showinfo("Succesfull","Zalogowano pracownika ")
                login_window.destroy()
                import pracownik
                
            else:
                messagebox.showinfo("Succesfull","Zalogowano użytkownika"+ str(username.get()))
                login_window.destroy()
                import uzytkownik
                
        

def connection_database():
    wypozyczalnia_samochodow = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database='wypozyczalnia_samochodow'
    )
    cursor = wypozyczalnia_samochodow.cursor()    



wypozyczalnia_samochodow = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database='wypozyczalnia_samochodow'
    )
cursor = wypozyczalnia_samochodow.cursor()

try:
    connection_database()
except:
    messagebox.showerror("Error","Brak połączenia z bazą danych.")
    

#GUI
login_window = Tk() #wywołanie okna
login_window.title("Logowanie")
login_window.geometry("400x350") #rozmiar okna 
login_window.resizable(0,0) #zablokowanie zmiany rozmiaru okna


#stworzenie nagłówka login i hasło
title_username = Label( #nagłówek
    login_window,
    text='EMAIL', 
    font=('Microsoft Yahei UI Light',
    13,
    'bold')
    )
title_username.place(x=170,y=50) #umiejscowienie nagłówka

username = Entry( #pole tekstowe "Nazwa użytkowanika"
    login_window,
    width=25,
    font=('Microsoft Yahei UI Light',
    11,
    'bold')
    )  
username.place(x=90,y=100)
username.insert(0,'Email')
username.bind('<FocusIn>',username_enter)

title_password = Label( #nagłówek Hasło
    login_window,
    text='HASŁO', 
    font=('Microsoft Yahei UI Light',
    13,
    'bold')
    )
title_password.place(x=160,y=150) #umiejscowienie nagłówka

password = Entry( #Pole tekstowe "Hasło"
    login_window,
    width=25,
    font=('Microsoft Yahei UI Light',
    11,
    'bold')
    )
password.place(x=90,y=200)
password.insert(0,'Password')
password.bind('<FocusIn>',password_enter)

login_button = Button( #przycisk logowania
    login_window,
    text='ZALOGUJ',
    font=('Open Sans',
    16,
    'bold'),
    fg='white',
    bg='red',
    command=data_checking
    )
login_button.place(x=140,y=250) #umiejscowienie przycisku logowania



login_window.mainloop()