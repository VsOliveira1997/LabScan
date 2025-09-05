# LabScan

LabScan é uma ferramenta simples de pentest desenvolvida em Python para realizar varreduras em hosts e identificar serviços ativos. Ideal para testes de laboratório e aprendizado em segurança ofensiva.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas listadas no arquivo `requirements.txt`

## Instalação

Para instalar e executar a ferramenta, siga os passos abaixo:

1. Clone o repositório:

```bash
git clone https://github.com/VsOliveira1997/LabScan.git
cd LabScan
```

2. (Opcional) Crie um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Execute o script principal com o Python:

```bash
python3 labscan.py -i <IP-alvo> [opções]
```

### Parâmetros disponíveis:

- `-i`: Define o IP de destino
- `-np`: Executa sem ping (no-ping)
- *(Outros parâmetros dependem do script; adicione aqui se necessário)*

### Exemplos:

```bash
python3 labscan.py -i 192.168.1.1
```

```bash
python3 labscan.py -i 192.168.1.1 -np
```

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `labscan.py`: Script principal responsável pelas funcionalidades da ferramenta
- `requirements.txt`: Lista de dependências Python necessárias
- `README.md`: Instruções de uso

## Licença

Este projeto é disponibilizado para fins educacionais. Certifique-se de utilizá-lo com responsabilidade e apenas em ambientes autorizados.
