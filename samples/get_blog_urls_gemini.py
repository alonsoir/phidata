import requests
from bs4 import BeautifulSoup

from samples.get_blog_urls_claude import soup


def obtener_enlaces_pagina(url):
  """
  Extrae enlaces de una página web específica.

  Args:
      url (str): URL de la página web.

  Returns:
      list: Lista de enlaces encontrados en la página.
  """
  enlaces = []
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  for a_tag in soup.find_all('a', href=True):
    enlace = a_tag['href']
    if enlace.startswith('/'):
      enlaces.append(f"{url}{enlace}")

  return enlaces

def guardar_enlaces_archivo(enlaces, filename):
  """
  Guarda una lista de enlaces en un archivo de texto.

  Args:
      enlaces (list): Lista de enlaces a guardar.
      filename (str): Nombre del archivo de texto.
  """
  with open(filename, 'w') as f:
    for enlace in enlaces:
      f.write(f"{enlace}\n")

# URL inicial del blog
url_inicial = "https://aironman2k.wordpress.com/"

# Lista de enlaces vacía
lista_enlaces = []

# Bucle principal para recorrer las páginas del blog
while True:
  # Obtener enlaces de la página actual
  enlaces_pagina = obtener_enlaces_pagina(url_inicial)

  # Añadir enlaces a la lista
  lista_enlaces.extend(enlaces_pagina)

  # Obtener URL siguiente (si existe)
  url_siguiente = None
  for a_tag in soup.find_all('a', href=True):
    if a_tag.text.lower() == "siguiente":
      url_siguiente = a_tag['href']
      break

  # Control de fin de recorrido
  if not url_siguiente:
    break

  # Actualizar URL inicial para la siguiente página
  url_inicial = f"{url_inicial}{url_siguiente}"

# Guardar enlaces en archivo
guardar_enlaces_archivo(lista_enlaces, "enlaces_blog.txt")
