import requests
from bs4 import BeautifulSoup
import csv

def get_spotify_hits(country):
    #gonna have to change the us from a permanent variable to one that shifts
    page = requests.get(f'https://spotifycharts.com/regional/{country}/weekly/latest')
    page
    soup = BeautifulSoup(page.content, 'html.parser')
    #test the soup connection
    table = soup.find('table', attrs={'class': 'chart-table'})

    table_body = table.find('tbody')
    table = []
    #for each entry into the table go get all the information
    for tr in table_body.find_all('tr'):
        #create an empty dictionary to put stuff in
        dict_1 = {}
        #get the name of the artist
        entry_name = tr.find('td', attrs={'class': 'chart-table-track'}).find('span').text
        entry_name = entry_name.replace('by ', '').strip()
        #add it to the dictionary associated with the artist key
        dict_1['artist'] = entry_name
        #get all of the song titles
        title = tr.find('td', attrs={'class': 'chart-table-track'}).find('strong').text
        #add it to the dictionary associated with the song_title key
        dict_1['song_title'] = title
        #get the number of streams
        streaming_number = tr.find('td', attrs={'class': 'chart-table-streams'}).text
        streaming_number = streaming_number.replace(',', '')
        streaming_number = int(streaming_number)
        #add it to the dictionary associated with stream count
        dict_1['stream_count'] = streaming_number
        dict_1[f'{country}'] = country
        table.append(dict_1)
    #drop duplicate entries from list

    #save to csv
    w = csv.writer(open('country_spotify_data.csv', 'w'))
    for entry in table:
        for key, val in entry.items():
            w.writerow([key, val])
    return table

#list in countries
countries = ['us', 'gb', 'ad', 'ar', 'at', 'au', 'be', 'bg', 'bo', 'br',
'ca', 'ch', 'cl', 'co', 'cr', 'cy', 'cz', 'de', 'dk', 'do', 'ec', 'ee',
'es', 'fi', 'fr', 'gr', 'gt', 'hk', 'hn', 'hu', 'id', 'ie', 'il', 'in',
'is', 'it', 'jp', 'lt', 'lu', 'lv', 'mt', 'mx', 'my', 'ni', 'nl', 'no',
'nz', 'pa', 'pe', 'ph', 'pl', 'pt', 'py', 'ro', 'se', 'sg', 'sk', 'sv',
'th', 'tr', 'tw', 'uy', 'vn', 'za']

#function to call all
def all_country_grabber(countries_list):
    for country in countries:
        get_spotify_hits(country)
    return

all_country_grabber(countries)
