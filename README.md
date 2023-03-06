# SteamAchievementsHidden

This Python program extracts information from two web pages on Steam, compares them, and prints the differences. It requires the user to provide two URLs: one for the user's achievements page and one for the global achievements page. The program extracts the user's achievements information and all achievements information, compares the two lists, and saves the user's missing achievements to a text file on the user's desktop. The program then displays the remaining achievements and informs the user that the list has been exported successfully to the desktop.

## Requirements
Python 3.x
Requests
BeautifulSoup4

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies (Requests, BeautifulSoup4).
3. Run the program with Python by typing python SteamAchievementsScraper.py on your command line.
4. Enter the URLs for the user's achievements page and the global achievements page when prompted.
5. Wait for the program to finish.
6. The program will export a list of the user's missing achievements to a text file on the user's desktop.
