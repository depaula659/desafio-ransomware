import os
import pyaes

def descriptografar_arquivo(file_name: str, key: bytes):
    """Descriptografa um arquivo usando AES em modo CTR e salva o resultado em um novo arquivo."""
    
    # Lê o conteúdo do arquivo criptografado
    with open(file_name, 'rb') as file:
        file_data = file.read()

    # Descriptografa os dados do arquivo
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    # Define o nome do novo arquivo descriptografado
    new_file_name = file_name.replace(".ransomwaretroll", "")

    # Salva o arquivo descriptografado
    with open(new_file_name, 'wb') as new_file:
        new_file.write(decrypt_data)

    # Remove o arquivo criptografado após a descriptografia
    os.remove(file_name)

    print(f"Arquivo descriptografado com sucesso: {new_file_name}")

if __name__ == "__main__":
    # Nome do arquivo criptografado a ser descriptografado
    file_name = "teste.txt.ransomwaretroll"
    
    # Chave para descriptografia (deve ser 16, 24 ou 32 bytes)
    key = b"testeransomwares"  # Chave de 16 bytes

    # Descriptografa o arquivo
    descriptografar_arquivo(file_name, key)
