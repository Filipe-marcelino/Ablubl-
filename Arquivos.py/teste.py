frase = input('Digite uma frase para gravar no arquivo:')
# O parâmetro 'w' (de write) passado para a função open
# cria um novo arquivo e o habilita para escrita.
arquivo = open('frase.txt', 'w', encoding='utf-8')
arquivo.write(frase)  # Escreve a frase no arquivo.
# Fecha o arquivo logo ao terminar a escrita para evitar 
# corrupção de dados.
arquivo.close()
print('Feito! Verifique o conteúdo do arquivo.')
