import requests
import sys

while True:
    print('[0] Exit')
    print('[1] Locate ip')

    option = str(input('# '))

    if option == '0':
        print('Bye!')
        sys.exit()

    if option == '1':
        while True:
            ip = str(input("Ip: "))

            if ip:
                resp = requests.get(f'https://ipapi.co/{ip}/json/')

                json_resp = resp.json()

                print('\033[32m')
                print(json_resp)
                print('\033[0m')

                break
    if option != '0' or '1':
        print('Erro digite uma opção válida!')