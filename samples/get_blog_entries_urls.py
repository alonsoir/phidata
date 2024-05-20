import re

import requests
from bs4 import BeautifulSoup


def get_blog_entries(filename, url):
    """Fetches and processes blog entry data from a given URL.

    Args:
        filename (str): The name of the file to write the entry information to.
        url (str): The URL of the blog entry to extract data from.

    Returns:
        dict (or None): A dictionary containing the parsed blog entry data if successful,
                         or None if an exception occurs.
    """

    entries = []
    try:
        # Abrir la URL de la entrada (Open the entry URL)
        # el dia del mes del año que sea pudo haber más de una entrada, es decir, más de un título
        entry_response = requests.get(url)
        entry_response.raise_for_status()
        if entry_response.status_code == 200:
            print(f"{url} parece que tiene contenido...")
            entry_soup = BeautifulSoup(entry_response.content, 'html.parser')

            # Extraer el título de la entrada (Extract the entry title)
            title = entry_soup.find('h2').text.strip()

            # Extraer el contenido de la entrada (Extract the entry content)
            content = entry_soup.find('div', class_='entry-content').text.strip()

            # Extraer la fecha de publicación de la entrada (Extract the entry publication date)
            date_str = entry_soup.find('time', class_='published')['datetime']
            date = re.findall(r'\d{4}-\d{2}-\d{2}', date_str)[0]

            # Crear una entrada de blog y escribirla en el archivo (Create a blog entry and write to file)
            entry = {
                'title': title,
                'link': url,
                'content': content,
                'date': date
            }
            final_entry=f"{entry['link']}{entry['date']}/{entry['title']}\n"
            print(final_entry)
            with open(filename, 'a') as f:
                f.write(final_entry)

            entries.append(entry)
        return entries  # Return the extracted entry dictionary

    except Exception as e:
        # Si no se encuentra contenido, escribe una advertencia en la consola (If no content found, print a warning)
        print(f"{url}. {e}")
        return None  # Return None on exception

pattern = r"https://aironman2k\.wordpress\.com/(\d{4})/(0[1-9]|1[0-2])/([0-2][0-9]|3[01])/?$"
FILENAME = "entradas_blog.txt"

# Generar URLs para cada año, mes y día
for year in range(2012, 2025):
    for month in range(1, 13):
        # Formatear el mes con dos dígitos
        month_str = f"{month:02d}"
        # Determinar el número máximo de días para el mes actual
        max_days = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month != 2 else 28
        for day in range(1, max_days + 1):
            # Formatear el día con dos dígitos
            day_str = f"{day:02d}"
            # Crear la URL completa
            url = f"https://aironman2k.wordpress.com/{year}/{month_str}/{day_str}/"
            # print(f"Testing {url} with pattern {pattern}? : {re.search(pattern, url)}")
            # Optional: Print only matching URLs (if desired)
            match = re.search(pattern, url)
            if match:
                # print(f"{url} is a match")

                entries = get_blog_entries(FILENAME,url)

                if entries is not None:
                    for entry in entries :
                        print(f"Título: {entry['title']}")
                        print(f"Enlace: {entry['link']}")
                        print(f"Contenido: {entry['content'][:50]}...")
                        print(f"Fecha: {entry['date']}")
                        print("------------------")

print("Done!, fichero creado en : ", FILENAME)
