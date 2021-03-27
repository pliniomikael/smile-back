import urllib.request
from bs4 import BeautifulSoup
from django.template.defaultfilters import slugify
import time
import requests
import re
from cost.models import Citie, Category

headers = requests.utils.default_headers()
headers.update({
    'User-Agent':
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

# def CitiesExtractor(url):
#     response = requests.get(url, headers=headers)
#     bsCities = BeautifulSoup(response.content, 'html.parser')
#     divmae = bsCities.find('select', {'id': 'locCity'})
#     # googleClass = bsOBJloja.find('iframe', )
#     # print(divmae)
#     i = 0
#     divfilha = divmae.findAll('option')
#     # print(divfilha)
#     data = []
#     for cite in divfilha:
#         i = i + 1
#         # print(i)
#         name = cite.text
#         # object = {'name': name}
#         # print(name)
#         c = Citie()
#         c.name = name
#         c.save()


def CitiesExtractor(url):
    response = requests.get(url, headers=headers)
    bsCities = BeautifulSoup(response.content, 'html.parser')
    divmae = bsCities.find('table', {'id': 't2'})
    # googleClass = bsOBJloja.find('iframe', )
    # print(divmae)
    i = 0
    divfilha = divmae.findAll('td', {'class': 'cityOrCountryInIndicesTable'})
    # print(divfilha)
    # data = []
    for cite in divfilha:
        i = i + 1
        # print(cite)
        name = cite.a.text
        link = cite.a.get("href")
        # object = {'name': name}
        # print(name)
        c = Citie()
        c.name = name
        c.link = link
        c.save()


def DadosCitiesExtractor():
    cite = Citie.objects.all()
    for c in cite:
        print("numero: ", c.id)
        # response = requests.get(
        #     'http://api.proxiesapi.com/?auth_key=07063e8acb604e51e5978ec40ec20113_sr98766_ooPq87&url='
        #     + url + ll.slug_scraper,
        #     headers=headers)
        response = requests.get(c.link, headers=headers)
        bsOBJloja = BeautifulSoup(response.content, 'html.parser')
        divfilha = bsOBJloja.findAll('th', {'class': 'highlighted_th prices'})
        for des in divfilha:
            cat = Category()
            cat.description = des.text
            cat.cite = c
            cat.save()
        # print(divfilha)

    # Loja.objects.bulk_update(loja, ["link_loja", "descricao"])


# def BaseCupomManiaLojas(url):
#     response = requests.get(url, headers=headers)
#     bsOBJ = BeautifulSoup(response.content, 'html.parser')
#     divmae = bsOBJ.findAll('li', {'class': 'list-letter-item'})
#     for codigo in divmae:
#         all_hrefs = codigo.findAll('a')

#         data = []
#         for links in all_hrefs:
#             ll = links.get("href")
#             nome = links.text
#             # responseloja = opener.open(
#             #     f'https://www.cuponomia.com.br/desconto/{ll}')
#             # bsOBJloja = BeautifulSoup(responseloja.read(), 'html.parser')
#             # divmaeloja = bsOBJloja.findAll(
#             #     'div', {'class': 'storeDescription-secondTier'})
#             # for codigoloja in divmaeloja:
#             #     all_hrefsloja = codigoloja.findAll('p')
#             #     for desc in all_hrefsloja:
#             #         descri = desc.text
#             object = {
#                 'nome': nome,
#                 'slug_scraper': links.get("href"),
#                 # 'descricao': descri,
#             }
#             data.append(object)
#         Loja.objects.bulk_create([Loja(**q) for q in data])

# def LojaNation(url):
#     response = requests.get(url, headers=headers)
#     bsOBJ = BeautifulSoup(response.content, 'html.parser')
#     nome = re.compile(r"\/cupom-.*?")
#     divmae = bsOBJ.findAll('a', {'href': nome})
#     data = []
#     for codigo in divmae:
#         l = codigo.get("href")
#         text = codigo.text
#         print("href %s - Loja: %s" % (l, text))
#         object = {
#             'nome': text,
#             'slug_scraper': l,
#         }
#         if object in data:
#             pass
#         else:
#             data.append(object)
#     Loja.objects.bulk_create([Loja(**q) for q in data])

# def CiaDescontos(url):
#     response = requests.get(url, headers=headers)
#     bsOBJ = BeautifulSoup(response.content, 'html.parser')
#     nome = re.compile(r"https:\/\/www.ciadosdescontos.com\/cupom\/.\w+")
#     divmae = bsOBJ.findAll('a', {'href': nome})
#     # print(divmae)
#     data = []
#     for codigo in divmae:
#         l = codigo.get("href")
#         text = codigo.text
#         print("href %s - Loja: %s" % (l, text))
#         object = {
#             'nome': text,
#             'slug_scraper': l,
#         }
#         if object in data:
#             pass
#         else:
#             data.append(object)
#     Loja.objects.bulk_create([Loja(**q) for q in data])

# def DescricaoCiaDescontos():
#     loja = Loja.objects.filter(categoria=None)
#     for ll in loja:
#         print("numero: ", ll.id)
#         # response = requests.get(
#         #     'http://api.proxiesapi.com/?auth_key=07063e8acb604e51e5978ec40ec20113_sr98766_ooPq87&url='
#         #     + url + ll.slug_scraper,
#         #     headers=headers)
#         response = requests.get(ll.slug_scraper, headers=headers)
#         bsOBJloja = BeautifulSoup(response.content, 'html.parser')
#         ll.link_loja = bsOBJloja.find('a', {
#             'class': 'company-website-link'
#         }).text
#         ll.descricao = bsOBJloja.find('div', {
#             'class': 'term-description'
#         }).findChild("p").text

#     Loja.objects.bulk_update(loja, ["link_loja", "descricao"])

# def CupomCiaDescontos():
#     loja = Loja.objects.all()
#     for ll in loja:
#         print("numero: ", ll.id)
#         # response = requests.get(
#         #     'http://api.proxiesapi.com/?auth_key=07063e8acb604e51e5978ec40ec20113_sr98766_ooPq87&url='
#         #     + url + ll.slug_scraper,
#         #     headers=headers)
#         response = requests.get(ll.slug_scraper, headers=headers)
#         bsOBJloja = BeautifulSoup(response.content, 'html.parser')
#         divavo = bsOBJloja.findAll('div', {'class': 'coupon-wrapper'})
#         divpai = bsOBJloja.findAll('div', {'class': 'coupon-details'})
#         data = []
#         for di in divavo:
#             for desc in divpai:
#                 if desc.find('h3', {'class': 'entry-title'}):
#                     if desc.find('span', {'class': 'badge-secondary'}):
#                         d = desc.text
#                         ti = di.find('time', {'class': 'expired'}).text
#                         print(ti)
#                         amae = desc.findAll('a', {"data-clipboard-text": True})
#                         for cod in amae:
#                             if cod["data-clipboard-text"] == "Pegar Desconto":
#                                 pass
#                             else:
#                                 # object = {
#                                 #     'loja': ll,
#                                 #     'titulo': d,
#                                 #     'cod': cod["data-clipboard-text"],
#                                 #     'validade': l,
#                                 #     'status': l,
#                                 # }
#                                 print(cod["data-clipboard-text"])
#             # print(amae)

#         # for desc in h3mae:
#         #     if desc.find('span'):
#         #         d = desc.text

#         # print(amae)
#         # ll.link_loja = bsOBJloja.find('a', {
#         #     'class': 'company-website-link'
#         # }).text
#         # ll.descricao = bsOBJloja.find('div', {
#         #     'class': 'term-description'
#         # }).findChild("p").text

#     # Loja.objects.bulk_update(loja, ["link_loja", "descricao"])

# def LojaPromobit(url):
#     response = requests.get(url, headers=headers)
#     bsOBJ = BeautifulSoup(response.content, 'html.parser')
#     divmae = bsOBJ.findAll('div', {'class': 'stores-list'})
#     data = []
#     # print(divmae)
#     for codigo in divmae:
#         lo = codigo.findAll("div", {'class': 'act'})
#         for ll in lo:
#             hr = ll.a.get("href")
#             loja = ll.find("a")
#             new = ''.join(loja(text=True, recursive=False))

#             object = {
#                 'nome': new,
#                 'slug_scraper': hr,
#             }
#             if object in data:
#                 pass
#             else:
#                 data.append(object)
#     Loja.objects.bulk_create([Loja(**q) for q in data])

# def CupomPromo():
#     loja = Loja.objects.all()
#     url = 'https://www.promobit.com.br'
#     for ll in loja:
#         print("numero: ", ll.id)
#         # response = requests.get(
#         #     'http://api.proxiesapi.com/?auth_key=07063e8acb604e51e5978ec40ec20113_sr98766_ooPq87&url='
#         #     + url + ll.slug_scraper,
#         #     headers=headers)
#         response = requests.get(url + ll.slug_scraper, headers=headers)
#         bsOBJloja = BeautifulSoup(response.content, 'html.parser')
#         divavo = bsOBJloja.findAll(
#             'div', {'class': 'coupon-card relative my4 js-coupon-card'})
#         # print(divavo)
#         for cu in divavo:
#             # print(cu)
#             h2 = cu.find("h2", {"class": "coupon-title"})
#             divc = cu.find("div", {"class": "js-coupons__content--inner"})
#             cupo = cu.find("div", {"class": "coupon-card__coupon ml3 pt1"})
#             ee = cupo.find("span").text
#             print(ee)
#             dd = cupo.find("a", {"data-coupon-code": True})
#             print(dd["data-coupon-code"])
#             # for kk in cupo:
#             #     # for k in kk:
#             #     # t
#             #     # print("t", t)
#             #     #     print("kk", k)
#             #     dd = kk.find("a", {"data-coupon-code": True})
#             #     print(dd["data-coupon-code"])
#             # print("ee", ee)
#             # print("kk", kk["data-coupon-code"])
#             # print(dd['data-coupon-code'])

#             # print(divc.text)
#         # divpai = bsOBJloja.findAll('div', {'class': 'coupon-details'})
#         # data = []
#         # for di in divavo:
#         #     for desc in divpai:
#         #         if desc.find('h3', {'class': 'entry-title'}):
#         #             if desc.find('span', {'class': 'badge-secondary'}):
#         #                 d = desc.text
#         #                 ti = di.find('time', {'class': 'expired'}).text
#         #                 print(ti)
#         #                 amae = desc.findAll('a', {"data-clipboard-text": True})
#         #                 for cod in amae:
#         #                     if cod["data-clipboard-text"] == "Pegar Desconto":
#         #                         pass
#         #                     else:
#         #                         # object = {
#         #                         #     'loja': ll,
#         #                         #     'titulo': d,
#         #                         #     'cod': cod["data-clipboard-text"],
#         #                         #     'validade': l,
#         #                         #     'status': l,
#         #                         # }
#         #                         print(cod["data-clipboard-text"])
#         # print(amae)

#         # for desc in h3mae:
#         #     if desc.find('span'):
#         #         d = desc.text

#         # print(amae)
#         # ll.link_loja = bsOBJloja.find('a', {
#         #     'class': 'company-website-link'
#         # }).text
#         # ll.descricao = bsOBJloja.find('div', {
#         #     'class': 'term-description'
#         # }).findChild("p").text

#     # Loja.objects.bulk_update(loja, ["link_loja", "descricao"])