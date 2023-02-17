import requests
import os
import sys
from bs4 import BeautifulSoup

AchievementsUnhided = input('Informe a URL das suas conquistas: ')
AllAchievements = input('Informe a URL das conquistas globais: ')

AchUn = []
AchA = []

print("Aguarde...")

# Extrair as informações das conquistas do usuário
response = requests.get(AchievementsUnhided)
soup = BeautifulSoup(response.text, 'html.parser')

for div in soup.find_all('div', {'class': 'achieveTxtHolder'}):
    Achievement = div.find('h3').text
    AchUn.append(Achievement)

# Extrair as informações de todas as conquistas
response = requests.get(AllAchievements)
soup = BeautifulSoup(response.text, 'html.parser')

for div in soup.find_all('div', {'class': 'achieveTxtHolder'}):
    Achievement2 = div.find('h3').text
    AchA.append(Achievement2)

# Encontrar as conquistas restantes
AchievementsMissing = []
for conquista in AchA:
    if conquista not in AchUn:
        AchievementsMissing.append(conquista)

print("Conquistas restantes:\n", AchievementsMissing)

# Salvar as conquistas restantes em um arquivo de texto na área de trabalho do usuário
with open(f"{os.environ['UserProfile']}\Desktop\SteamAchievements.txt", 'w') as arquivo:
    arquivo.write("\n".join(AchievementsMissing))
print("\nLista exportada para área de trabalho!")

input('Pressione enter para finalizar.. ')
sys.exit()
