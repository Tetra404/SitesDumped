import os
from colorama import Fore
import time
import pyfiglet



try:
    os.system("cls")
except:
    os.system("clear") 


while True:
    def logo(name):
        return name
    
    name =pyfiglet.figlet_format("SİTE CEKİCİ")
    print(Fore.RED + name)
    print(Fore.LIGHTBLACK_EX + "\n <> DEV BY TETRA </> \n")
    url = input(Fore.BLUE + "Hedef Url Adresini Girin "  + Fore.MAGENTA + "Çıkış İçin exit "  + Fore.BLUE + " Yazın-->") 

    if url == "exit":
        print(Fore.RED + "TOOLDAN ÇIKIŞ YAPILIYOR..")
        time.sleep(2)
        break
    elif url.startswith("https://"):
        url = url.replace("https://" , " ")
        url.strip()     
    elif url.startswith("http://"):
        url = url.replace("https://" , " ")
        url = url.strip()
    else:
        pass

    os.system("wget -q -wk" + url)

    print(Fore.GREEN + f"\n Klasör Başarılı Bir Şekilde {url} Klasörüne Kaydedildi.")

