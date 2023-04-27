import glob

# Nome do arquivo de saída
output_file = 'arquivo_saida.txt'
output_file_b = 'arquivo_saida_b.txt'

# Abre o arquivo de saída para escrita
with open(output_file, 'w') as out:
    # Loop pelos arquivos no diretório
    for filepath in glob.iglob("ADFA-LD\ADFA-LD\Training_Data_Attack\*.txt", recursive=True):
        # Abre o arquivo atual para leitura
        with open(filepath, 'r') as f:
            # Copia o conteúdo do arquivo para o arquivo de saída
            out.write(f.read())


with open(output_file_b, 'w') as out:
    # Loop pelos arquivos no diretório
    for filepath in glob.iglob("ADFA-LD\ADFA-LD\Training_Data_Master\*.txt", recursive=True):
        # Abre o arquivo atual para leitura
        with open(filepath, 'r') as f:
            # Copia o conteúdo do arquivo para o arquivo de saída
            out.write(f.read())
