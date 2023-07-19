import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# abrindo o arquivo em modo de leitura e passando o binário
pdf_file = open('teste_pdf.pdf', 'rb')

#le o arquivo pdf, recebe um stream (stream é o binário do arquivo)
dados_do_pdf = PyPDF2.PdfFileReader(pdf_file)

#pegando o número de páginas
print('Número de páginas = ' + str(dados_do_pdf.numPages))

#pegando o conteúdo da página indicada e colocando em uma variável
pagina1 = dados_do_pdf.getPage(0)

#pegando o texto extraido da página 1
texto_da_pagina1 = pagina1.extractText()

print(texto_da_pagina1, 0)


# essa lista serve como uma referência para verificação de palavras
nomes = ['ONU', 'drogas', 'crimes', 'celular']


# essa função recebe um valor em milimetros e devolve em pontos
def mm2p(milimetros):
    return milimetros / 0.352777

# criando um arquivo em pdf e escolhendo o tamanho da página
cnv = canvas.Canvas("criando.pdf", pagesize=A4)

# o eixo vai dar a direção de onde cada palavra deve ser escrita dentro da página A4
eixo = 100

# para cada nome na lista nomes, vai verificar se contém esse nome no texto da página 1
# se contiver, o nome vai ser escrito no novo pdf que será gerado
for nome in nomes:
    if nome in texto_da_pagina1:
        cnv.drawString(mm2p(100), mm2p(eixo), nome)
        # nesse caso estamos decrementando o eixo y para que as palavras sejam escritas uma embaixo da outra
        eixo -= 20
    else:
        None
# está salvando o arquivo pdf
cnv.save()

