import requests
from bs4 import BeautifulSoup
import re



def tim_url_lien_quan(url, url_goc):
    url_tim_duoc = set()
    link = requests.get(url)
    link_soup = BeautifulSoup(link.text, 'html.parser')
    results = link_soup('a', attrs={'href': True})
    for i in results:
        a = i['href']
        mau = f'^{url_goc}[^?#]*$'
        mau2 = '^/[^?#]*$'
        if re.match(mau, a):
            url_tim_duoc.add(a)
        else:
            if re.match(mau2, a):
                url_lien_quan = f'{url_goc}{a}'
                url_tim_duoc.add(url_lien_quan)
    return url_tim_duoc



def them_va_duyet_hang_cho(hang_cho, url_goc, so_luong_trang):
    history = hang_cho
    while (len(hang_cho) > 0) and (len(history) < so_luong_trang):
        url_tim_duoc = tim_url_lien_quan(hang_cho.pop(), url_goc)
        hang_cho = hang_cho | (url_tim_duoc - history)
        history = history | url_tim_duoc
    return history
