import os
import sys
class next:
    def ls():
        PATH = input("Где:")
        os.system("dir" + PATH)
    def notpad():
        os.system("notepad")
    def calculatlor():
        os.system("calc")
    def dbg():
        print("Works!")
    def cd():
        cdw = input("Куда?:")
        os.system("cd " + cdw )

def check():
    while True:
        answer = input("Что сделать:")
        if answer == "ls":
            next.ls()
            break
        elif answer == "калькулятор" or "calc":
            next.calculatlor()
            break
        elif answer == "блокнот" or "notepad":
            next.notpad()
            break
        elif answer == "debug":
            next.dbg()
            break
        elif answer == "выйти" or "exit":
            sys.exit()
        elif answer == "cd":
            next.cd()
            break
        else:
            print("Такого нет")
#Class: next
#Commands for next: ls; notepad; calculator; debug; cd
#check lang = RU 
#account: https://github.com/ArChIvExGaMexD
#source: https://github.com/ArChIvExGaMexD/PyLCmd/blob/main/PyLinuxCMD.py
#Классы: next
#Команды для класса next: ls; notepad; calculator; debug; cd
#язык check = RU 
#Аккаунт: https://github.com/ArChIvExGaMexD
#Источник: https://github.com/ArChIvExGaMexD/PyLCmd/blob/main/PyLinuxCMD.py