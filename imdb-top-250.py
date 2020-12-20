from bs4 import BeautifulSoup
import requests
import csv

def fetch_imdb():
    url = "https://www.imdb.com/chart/top"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    films = list()
    for elem in soup.find_all("td", class_="titleColumn"):
        a_film = list()
        a_film.append(elem.next_element.replace('-', '').replace('.', '').strip())
        a_film.append(elem.a.string.strip())
        a_film.append(elem.a.get('href').strip())
        a_film.append(elem.span.string.replace('(', '').replace(')', '').strip())
        films.append(a_film)

    return films

def write_to_console():
    films = fetch_imdb()
    for film in films:
        print (film)

def export_to_csv(csvfile):
    films = fetch_imdb()
    fields = ['Rank', 'Title', 'Url', 'Year']
    with open(csvfile, 'w', newline='', encoding='utf-8') as file:  
        csvwriter = csv.writer(file)  
        csvwriter.writerow(fields)
        csvwriter.writerows(films)
    print("%s created with %s lines" % (csvfile, len(films)))

write_to_console()
export_to_csv("imdb_top_250.csv")
