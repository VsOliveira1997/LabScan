# TODO Fazer a validação se é linux ou windows para poder fazer o basico
# TODO Se for Windows, rodar o basico de enumeração no AD
# TODO Testear em host que não tem ip na maquina
# TODO Colocar o path como env para não ter que digitar todas as vezes
from Utils.Config import Config
from Utils.Scan import Scan
from argparse import ArgumentParser, RawTextHelpFormatter


def print_banner():
        banner = r"""
    ██╗      █████╗ ██████   ███████╗ ██████╗  █████╗ ███╗  ██╗
    ██║     ██╔══██╗██╔══██  ██╔════╝ ██╔════╝██╔══██╗████╗ ██║
    ██║     ███████║██████   ███████  ██║     ███████║██╔██╗██║
    ██║     ██╔══██║██╔══██       ██  ██║     ██╔══██║██║╚████║
    ███████╗██║  ██║██████║  ███████╗ ██████╗ ██║  ██║██║ ╚███║
    ╚══════╝╚═╝  ╚═╝╚═════╝  ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝
    """
        print(banner)

def main():
    print_banner()

    parser = ArgumentParser(
        description="Ferramenta para automatizar o baisco de scan em CTFS.\n"
                    "Exemplo de uso:\n"
                    "  python labscan.py -i 192.168.0.1 --rust-scan ",
        usage="python labscan.py -i <IP> [--rust-scan] [--nmap-scan]",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument("-i", "--ip", required=True)
    parser.add_argument("-d", "--dir", action="store_true", help="Change Path for save DIR")
    parser.add_argument("-rs", "--rust-scan", action="store_true", help="Rust scan mode")
    parser.add_argument("-ns", "--nmap-scan", action="store_true", help="Nmap mode")


    args = parser.parse_args()
    if args.dir:
        Config(args.dir)
    recom = Scan(args.ip)


    print(f"\033[92m[*] Iniciando o recon\033[0m")
    if args.rust_scan:
        print(f"\033[92m[*] Iniciando Rustscan\033[0m")
        recom.port_scan_rust()
    if args.nmap_scan:
        print(f"\033[92m[*] Iniciando NMAP\033[0m")
        recom.port_scan_nmap()
    print(f"\033[92m[*] Iniciando ffuf\033[0m")
    recom.fuzz_directories()
    print(f"\033[92m[*] Iniciando ffuf subdomain\033[0m")
    recom.fuzz_subdomains()


if __name__ == '__main__':
    main()
