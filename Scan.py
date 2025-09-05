import os
import sys

import requests
from Checker import Helpers

class Scan:
    def __init__(self, ip, path):
        self.ip = ip
        self.host = Helpers.check_location(ip)
        self.path = Helpers.create_folder(path)

    def config(self):
        env_path = os.path.join(os.getcwd(), ".env")  # Cria .env na raiz do projeto

        if not os.path.exists(env_path):
            with open(env_path, "w") as f:
                f.write(f"SCAN_DIR={self.path}\n")
        else:
            with open(env_path, "r") as f:
                lines = f.readlines()

            updated = False
            with open(env_path, "w") as f:
                for line in lines:
                    if line.startswith("SCAN_DIR="):
                        f.write(f"SCAN_DIR={self.path}\n")
                        updated = True
                    else:
                        f.write(line)
                if not updated:
                    f.write(f"SCAN_DIR={self.path}\n")

    def port_scan_nmap(self):
        try:
            os.system(f"nmap {self.ip} -sC -sV --min-rate 500 | tee {self.path}/nmap.txt")
        except Exception as e:
            print(e)

    def port_scan_rust(self):
        try:
            os.system(f"rustscan -a {self.ip} -r 1-65535 -b 65535 --ulimit 50000 | tee  {self.path}/rust.txt")
        except Exception as e:
            print(e)

    def fuzz_directories(self):
        try:
            if self.host is None:
                os.system(
                    f"ffuf -u http://{self.ip}/FUZZ -w  /opt/SecLists/Discovery/Web-Content/raft-medium-words.txt -c -fw 6 -t 150 | tee {self.path}/dirs.txt")
            if self.host is not None:
                os.system(f"ffuf -u {self.host}FUZZ -w  /opt/SecLists/Discovery/Web-Content/raft-medium-words.txt -c -fw 6 -t 150 | tee {self.path}/dirs.txt")
        except Exception as e:
            print(e)

    def fuzz_subdomains(self):
        try:
            if self.host is None:
                print(f"\033[93m[*] Servidor não provavelmente não possui subdomain\033[0m")
                sys.exit(1)
            sub = self.host.replace("http://", "").replace("/", "")
            response = requests.get(f"{self.host}")
            filter = (len(response.content))
            os.system(f"ffuf -u {self.host} -w  /opt/SecLists/Discovery/DNS/bug-bounty-program-subdomains-trickest-inventory.txt -c -H 'Host: FUZZ.{sub}' -t 150 -fw 6 -fs {filter} | tee {self.path}/subdomains.txt")
        except Exception as e:
            print(e)

