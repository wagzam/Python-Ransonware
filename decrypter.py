import os
import pyaes

# Abrir o arquivo criptografado
file_name = "teste.txt.ransomware"
file = open(file_name, "rb")
file_conteudo = file.read()
file.close()

# Chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_conteudo)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
