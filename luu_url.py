import os
import requests
import codecs



def tao_thu_muc(name):
    os.mkdir(name)
    os.chdir(name)



def luu_file(url, stt):
    file = codecs.open('file' + str(stt) + '.html', 'w', 'utf8')
    file.write(requests.get(url).text)
    file.close()



def luu_tat_ca_file(history, so_luong_trang):
    for (stt, url_con) in enumerate(history):
        if stt >= so_luong_trang:
            break
        luu_file(url_con, stt)
        print(f'{stt} {url_con}')


def main():
    tao_thu_muc('thinhvv')
    luu_file('https://baomoi.com/', 2)


if __name__ == "__main__":
    main()