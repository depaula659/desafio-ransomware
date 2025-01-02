RansomwareTroll - Criptografia e Descriptografia de Arquivos com AES-CTR
RansomwareTroll é uma ferramenta simples que permite criptografar e descriptografar arquivos usando o algoritmo AES no modo CTR (Counter). A criptografia é realizada com uma chave de 16 bytes (AES-128), e os arquivos criptografados têm o sufixo .ransomwaretroll. O objetivo desta ferramenta é demonstrar como a criptografia pode ser implementada de forma prática em Python.
Funcionalidades:

    Criptografia de arquivos: Transforma um arquivo em seu formato criptografado, tornando-o inacessível sem a chave correta.
    Descriptografia de arquivos: Permite a restauração do arquivo original a partir do arquivo criptografado, usando a chave correta.
    AES-CTR: O modo CTR oferece segurança e é amplamente utilizado devido à sua eficiência e paralelização.

Uso:

    Criptografar um arquivo: A ferramenta converte o arquivo original para um formato criptografado.
    Descriptografar um arquivo: A ferramenta permite reverter a criptografia, restaurando o arquivo original.

Pré-requisitos:

    Python 3.x
    Biblioteca pyaes ou pycryptodome (para alternativas).

Instalação:

Para instalar a dependência necessária, execute o seguinte comando:

pip install pyaes
# ou, se preferir o PyCryptodome
pip install pycryptodome

Exemplo de uso:

    Criptografar:

python encrypt.py

    Descriptografar:

python decrypt.py

Aviso:
Este código foi criado para fins educacionais e não deve ser utilizado em ambientes de produção sem as devidas considerações de segurança.
