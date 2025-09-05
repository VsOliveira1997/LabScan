import os
import requests


class Helpers:
    @staticmethod
    def create_folder(pathdir):


        try:
            check = os.popen("uname -a").read()

            if "Darwin" in check:
                    path = os.system(f"mkdir {path_mac}/{name}")
                    if path == 256:
                        print("\033[93m[*] Diretorio ja existe\033[0m")
                    else:
                        print(f"\033[92m[*] Diretorio criado com Sucesso! em {path_mac}\033[0m")
                    return f'{path_mac}{name}'# Verde
            else:
                path = os.system(f"mkdir {path_kali}{name}")
                if path == 256:
                    print("\033[93m[*] Diretorio ja existe\033[0m")
                else:
                    print(f"\033[92m[*] Diretorio criado com Sucesso! em {path_kali}\033[0m")  # Verde
                    return f"{path_kali}{name}"
        except Exception as e:
            print(e)


    @staticmethod
    def check_location(ip):
        try:
            host = requests.head(f"http://{ip}/", timeout=10).headers["Location"]
            check = os.system(f"cat /etc/hosts | grep {ip}")
            if check == 256:
                clean_host = host.replace("http://", "").replace("/", "")
                os.system(f"sudo echo '{ip}  {clean_host}' | sudo tee -a /etc/hosts")
                print(f"\033[92m[*] {host}Adicionado com Sucesso! no /etc/hosts\033[0m")
            if not host:
                print(f"\033[92m[*] Não tem redirect pata um dominio\033[0m")
            else:
                print("\033[93m[*] Ja esta no /etc/hosts\033[0m")  # Amarelo
            return host
        except Exception as e:
            print(e)

