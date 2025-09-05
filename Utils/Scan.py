import os
import sys
from dotenv import load_dotenv
import requests
from Utils.Checker import Check


load_dotenv(verbose=True)
class Scan:
    def __init__(self, ip):
        self.ip = ip
        self.host = Check.check_location(ip)
        self.path = Check.create_folder()



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
            response = requests.get(f"{self.host}")
            len_filter = (len(response.text))
            print(len_filter)
            if self.host is None:
                os.system(
                    f"ffuf -u http://{self.ip}FUZZ -w  /opt/SecLists/Discovery/Web-Content/raft-medium-words.txt -c -fw {len_filter} -t 150 | tee {self.path}/dirs.txt")
            if self.host is not None:
                os.system(f"ffuf -u {self.host}/FUZZ -w  /opt/SecLists/Discovery/Web-Content/raft-medium-words.txt -c -fw {len_filter} -t 150 | tee {self.path}/dirs.txt")
        except Exception as e:
            print(e)

    def fuzz_subdomains(self):
        try:
            if self.host is None:
                print(f"\033[93m[*] Servidor não provavelmente não possui subdomain\033[0m")
                sys.exit(1)
            sub = self.host.replace("http://", "").replace("/", "")
            response = requests.get(f"{self.host}")
            len_filter = (len(response.content))
            os.system(f"ffuf -u {self.host} -w  /opt/SecLists/Discovery/DNS/bug-bounty-program-subdomains-trickest-inventory.txt -c -H 'Host: FUZZ.{sub}' -t 150 -fs {len_filter} | tee {self.path}/subdomains.txt")
        except Exception as e:
            print(e)

