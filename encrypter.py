import os
import pyaes

def encrypt_file(file_path, key):
    """
    Criptografa um arquivo usando AES no modo CTR.

    Args:
        file_path (str): Caminho completo do arquivo a ser criptografado.
        key (bytes): Chave de criptografia (16, 24 ou 32 bytes).

    Returns:
        str: Caminho do novo arquivo criptografado.

    Raises:
        FileNotFoundError: Se o arquivo não existir.
        ValueError: Se a chave não for válida.
    """
    # Verificar existência do arquivo
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}") 

    # Validar tamanho da chave
    if len(key) not in (16, 24, 32):
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes (AES-128, AES-192, AES-256).")
    # Ler os dados do arquivo
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Configurar a criptografia AES
    aes = pyaes.AESModeOfOperationCTR(key)

   # Criptografar os dados
    encrypted_data = aes.encrypt(file_data)
   # Criar o nome do novo arquivo criptografado
    encrypted_file_path = f"{file_path}.encrypted"
   # Salvar os dados criptografados
    with open(encrypted_file_path, "wb") as encrypted_file:
       encrypted_file.write(encrypted_data)
      # Remover o arquivo original com segurança
    os.remove(file_path)

    return encrypted_file_path

def validate_key_length(key):
    """
    Valida o comprimento da chave de criptografia.

    Args:
        key (bytes): A chave de criptografia.

    Raises:
        ValueError: Se o comprimento da chave for inválido.
    """
    if len(key) not in (16, 24, 32):
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes para AES.")
def main():
    """
    Função principal para executar o programa de criptografia.
    """
    # Configuração do caminho do arquivo e chave de criptografia
    file_path = input("Digite o caminho completo do arquivo a ser criptografado: ").strip()
    key = input("Digite a chave de criptografia (16, 24 ou 32 caracteres): ").strip().encode()

    try:
        # Validar o comprimento da chave
        validate_key_length(key)

        # Criptografar o arquivo
        encrypted_file_path = encrypt_file(file_path, key)
        print(f"Arquivo criptografado com sucesso: {encrypted_file_path}")

    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
