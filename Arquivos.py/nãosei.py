# Abre o arquivo para leitura
arquivo = open('leis.txt', encoding='utf-8')

# Lê o conteúdo do arquivo como string.
# Experimente também readlines().
conteudo = arquivo.read()

# Fecha o arquivo. Não se esqueça disso!             
arquivo.close()

# Exibe o conteúdo.
print(conteudo)
