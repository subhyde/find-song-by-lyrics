from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# sets the options to a headless browser

options = Options()
options.headless = True
browser = webdriver.Chrome('/users/ethan/Desktop/chromedriver', options=options)

# getting user data and parsing the url
print('Please enter the lyrics of a song')
lyrics = input()
url = 'https://findmusicbylyrics.com/search?q=' + lyrics.replace(" ", "+")

# launches headless browser
browser.get(url)

# gets the data based on the class names
first_song = browser.find_element_by_class_name('gs-title')
sample_lyrics = browser.find_element_by_class_name('gs-snippet')

# prints and formats to remove unnecessary characters
print('\n' + first_song.text.split("Lyrics")[0] + '\nSample Lyrics:\n\n' + sample_lyrics.text.split(': ')[-1])
browser.close()
