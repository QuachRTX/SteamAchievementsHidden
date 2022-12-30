__author__ = "Quach"
__version__ = "1.0"
__status__ = "development"
__email__ = "quach.vrc@gmail.com"
__github__ = "https://github.com/QuachRTX"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import sys
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(options=options,service=servico)

#______________________________________________________________________________________________

AchievementsUnhided = input('Informe a URL das suas conquistas: ')
AllAchievements = input('Informe a URL das conquistas globais: ')

AchUn = []
AchA = []

print("Aguarde...")

navegador.get(AchievementsUnhided)
time.sleep(5)

qtd = navegador.find_elements(By.CLASS_NAME, 'achieveTxtHolder')
#print("Total de conquistas visiveis: ",len(qtd)-1)

for ach in range(1,len(qtd)):
    x = '//*[@id="personalAchieve"]/div[{}]/div[2]/div[1]/h3'.format(ach)
    Achievement = navegador.find_element(By.XPATH, x).text
    AchUn.append(Achievement)
    


navegador.get(AllAchievements)
time.sleep(5)

qtd = navegador.find_elements(By.CLASS_NAME, 'achieveTxtHolder')
# print(len(qtd))

for ach2 in range(4,len(qtd)+4):
    x = '//*[@id="mainContents"]/div[{}]/div[2]/div[3]/h3'.format(ach2)
    Achievement2 = navegador.find_element(By.XPATH, x).text
    AchA.append(Achievement2)




AchievementsMissing=[]
for conquista in AchA:
    if conquista not in AchUn:
        AchievementsMissing.append(conquista)

print("Conquistas restantes:\n", AchievementsMissing)

try:
    with open(f"{os.environ['UserProfile']}\Desktop\SteamAchievements.txt", 'w') as arquivo:
        arquivo.write("\n".join(AchievementsMissing))
    print("\nLista exportada para área de trabalho!")
except:
    print("Falha ao exportar lista em TXT..")


input('Pressione enter para finalizar.. ')
navegador.quit()
sys.exit()




