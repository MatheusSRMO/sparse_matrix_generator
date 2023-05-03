import hashlib
import secrets
import random

qnt = int(input("Quantas matrizes deseja gerar: "))


for k in range(qnt):
    # Gerar uma string aleatória
    random_string = secrets.token_hex(4)

    # Criar um objeto de hash SHA-256
    hash_object = hashlib.sha256()

    # Atualizar o objeto de hash com a string aleatória
    hash_object.update(random_string.encode('utf-8'))

    # Obter o valor hash como uma string hexadecimal
    file_name = hash_object.hexdigest()[:20]

    m = int(input(f"{k} - Quantas linhas: "))
    n = int(input(f"{k} - Quantas colunas: "))
    with open(f'./{file_name}.txt', 'w') as f:
        f.write(f"{m} {n}\n")
        for i in range(m):
            for j in range(n):
                num_aleatorio = random.randint(1, 10)
                is_null = num_aleatorio >= 4
                if is_null:
                    f.write("0 ")
                    continue
                num_aleatorio = random.randint(1, 9)
                f.write(f"{num_aleatorio} ")
            f.write("\n")

