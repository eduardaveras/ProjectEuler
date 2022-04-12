from rsa import find_signature_hash


first_term = 1
second_term = 2
resposta = 0

while first_term < 4_000_000:
    first_term, second_term = second_term, first_term + second_term
    if first_term % 2 == 0:
        resposta = resposta + first_term

print(resposta)
