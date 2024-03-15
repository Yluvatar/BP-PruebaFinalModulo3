import requests
import templates

url = 'https://aves.ninjas.cl/api/birds'


def template_ave_nombre(data):
    contenido = ''
    for ave in data:
        contenido += templates.aves_template.substitute(ave=ave['name']['spanish'], bird=ave['name']['english'],
                                                        img=ave['images']['main'])
    return contenido


aves = requests.get(url)

contenido_html = template_ave_nombre(aves.json())

html_completo = templates.html_template.substitute(contenido=contenido_html)

with open('aves.html', 'w') as file:
    file.write(html_completo)
