import urllib.request
from Les_5.HW_5_1 import decor_threder
from threading import Thread


def download_file(file_name, url=None):
    urllib.request.urlretrieve(url, file_name)


url_linc = [
    'https://upload.wikimedia.org/wikipedia/commons/d/d4/Oasis_de_Huacachina%2C_Ica%2C_Per%C3%BA%2C_2015-07-29%2C_DD_18.JPG?uselang=ru',
    'https://upload.wikimedia.org/wikipedia/commons/b/b5/Libyen-oase1.jpg?uselang=ru',
    'https://upload.wikimedia.org/wikipedia/commons/f/fe/AG_006_large.jpg?uselang=ru',
    'https://upload.wikimedia.org/wikipedia/commons/9/9c/Oasis_Timimoun.jpg?uselang=ru',
    'https://commons.wikimedia.org/wiki/File:ArugotRiver.jpg?uselang=ru#/media/File:ArugotRiver.jpg',
    'https://commons.wikimedia.org/wiki/File:Oasis_in_Libya.jpg?uselang=ru#/media/File:Oasis_in_Libya.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/f/fa/Al_Ain_Oasis%2C_Al_Mutawaa_-_Abu_Dhabi_-_United_Arab_Emirates_-_panoramio.jpg?uselang=ru',
    'https://upload.wikimedia.org/wikipedia/commons/f/f4/Egypt-region-map-cities.gif?uselang=ru',
    'https://upload.wikimedia.org/wikipedia/commons/1/19/Nirvana_around_1992.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaUZ8i6kqV2OPUSqwqP7Dpv8mDJaGEDWzJh5pi1JJfDWy-qcN0&s',
    ]

for i in range(len(url_linc)):

    decor_threder(f'name_{i + 1}', True)(download_file(file_name=f'file{i + 1}', url=url_linc[i]))
