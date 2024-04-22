from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://inmuebles.mercadolibre.com.ar/alquiler/3-ambientes/bsas-gba-norte/san-fernando/alquiler_NoIndex_True#applied_filter_id%3DROOMS%26applied_filter_name%3DAmbientes%26applied_filter_order%3D9%26applied_value_id%3D%5B3-3%5D%26applied_value_name%3D3+ambientes%26applied_value_order%3D3%26applied_value_results%3D16%26is_custom%3Dfalse"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

data = []

for casa in soup.find_all('li', class_="ui-search-layout__item"):
    title = casa.find('h2', class_="ui-search-item__title").text.strip()
    location = casa.find('span', class_="ui-search-item__location").text.strip()
    price = casa.find('span', class_="price-tag-amount").text.strip()
    area = casa.find('li', class_="ui-search-card-attributes__attribute").text.strip()

    data.append({'Título': title, 'Ubicación': location, 'Precio': price, 'Área': area})

datacasas = pd.DataFrame(data)
datacasas.to_csv('datacasas.csv', index=False, encoding='utf-8')
print(datacasas)
