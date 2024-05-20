import requests
from bs4 import BeautifulSoup
from datetime import datetime
from collections import defaultdict

# URL inicial del blog
base_url = 'https://aironman2k.wordpress.com'

# Diccionario para almacenar las entradas por fecha
entries_by_date = defaultdict(list)

# Función para obtener las entradas de una página
def get_entries(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    entries = soup.find_all('div', class_='entry-content')
    print(f"There are {entries.count()} entries on this page.")
    for entry in entries:
        # Check if 'a' and 'time' elements exist before accessing their attributes
        link = entry.find('a')
        time_element = entry.find('time')
        if link and time_element:
            entry_link = link.get('href')
            date_str = time_element.get('datetime')
            date = datetime.fromisoformat(date_str).date()
            entries_by_date[date].append(entry_link)

# Iniciar la búsqueda desde la página principal
get_entries(base_url)

# Buscar las páginas de archivos por año y mes
soup = BeautifulSoup(requests.get(base_url).content, 'html.parser')
archive_links = soup.find_all('a', rel='archives')
for link in archive_links:
    archive_url = link.get('href')
    get_entries(archive_url)

# Ordenar las entradas por fecha y guardar en un archivo
sorted_entries = sorted([(date, links) for date, links in entries_by_date.items()])

with open('entradas_blog_claude.txt', 'w', encoding='utf-8') as file:
    for date, links in sorted_entries:
        for link in links:
            file.write(f"{link}\n")

print('Las entradas se han guardado en el archivo entradas_blog_claude.txt')
