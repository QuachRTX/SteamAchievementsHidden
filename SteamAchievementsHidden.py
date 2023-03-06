import requests
import os
import sys
from bs4 import BeautifulSoup

AchievementsUnhided = input('Enter the URL of your achievements: ')
AllAchievements = input('Enter the URL of the global achievements: ')

AchUn = []
AchA = []

print("Please wait...")

# Extracting user's achievements information
response = requests.get(AchievementsUnhided)
soup = BeautifulSoup(response.text, 'html.parser')

for div in soup.find_all('div', {'class': 'achieveTxtHolder'}):
    Achievement = div.find('h3').text
    AchUn.append(Achievement)

# Extracting all achievements information
response = requests.get(AllAchievements)
soup = BeautifulSoup(response.text, 'html.parser')

for div in soup.find_all('div', {'class': 'achieveTxtHolder'}):
    Achievement2 = div.find('h3').text
    AchA.append(Achievement2)

# Finding missing achievements
AchievementsMissing = []
for conquista in AchA:
    if conquista not in AchUn:
        AchievementsMissing.append(conquista)

print("Remaining achievements:\n", AchievementsMissing)

# Saving missing achievements to a text file on user's desktop
with open(f"{os.environ['UserProfile']}\Desktop\SteamAchievements.txt", 'w') as arquivo:
    arquivo.write("\n".join(AchievementsMissing))
print("\nList exported to desktop!")

input('Press enter to exit... ')
sys.exit()
