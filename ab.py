import platform
import random

# Lista de 100 nomes comuns brasileiros
names = [
    "Ana", "Pedro", "Maria", "João", "Lucas", "Fernanda", "Gabriel", "Juliana",
    "Carlos", "Patrícia", "Marcos", "Camila", "Roberto", "Juliano", "Larissa",
    "Mateus", "Amanda", "Ricardo", "Isabela", "Diego", "Sofia", "Felipe", "Larissa",
    "Bruna", "Joana", "Renato", "Bolsonaro", "Arthur", "Mariana", "Júlio", "Tatiane",
    "Lucas", "Vanessa", "Paula", "Thiago", "Claudia", "Ramagem", "Marina", "Roberta",
    "Jéssica", "Sérgio", "Eliane", "André", "Aline", "Rodrigo", "Cíntia", "Gustavo",
    "Letícia", "Maurício", "Isabel", "Eduardo", "Patrícia", "Luana", "Miguel",
    "Gabriela", "Samuel", "Nathalia", "Rodrigo", "Beatriz", "João Paulo", "Gabrielle",
    "Raquel", "Felipe", "Emilly", "Júlia", "Ricardo", "Carla", "Natália", "Robson",
    "Aline", "Leonardo", "Bruna", "Tatiane", "Eliane", "Tânia", "Alice", "Marcelo",
    "Cris", "Amanda", "Mateus", "Aline", "Vera", "José", "Luana", "Marcela"
]

# Função para gerar um sufixo numérico de 4 dígitos
def generate_suffix(existing_suffixes):
    while True:
        suffix = f"{random.randint(0, 9999):04}"
        if suffix not in existing_suffixes:
            existing_suffixes.add(suffix)
            return suffix

# Função para gerar uma lista de e-mails com sufixo numérico e nomes aleatórios
def generate_emails(names, domain, num_emails):
    if num_emails > len(names):
        raise ValueError("Número de e-mails não pode ser maior que o número de nomes disponíveis.")
    
    emails = set()
    existing_suffixes = set()
    
    while len(emails) < num_emails:
        name = random.choice(names).lower()
        suffix = generate_suffix(existing_suffixes)
        email = f"{name}.{suffix}@{domain.lower()}"
        emails.add(email)
    
    return list(emails)

# Parâmetros
domain = "abin.gov.br"
num_emails = 20

# Gerar e-mails
emails = generate_emails(names, domain, num_emails)

# Exibir e-mails
for email in emails:
    print(email)
print(platform.python_version())
