
quantidade_pixels = int(input("Quantos pixels ira informar? "))
representacao_linha = []


while len(representacao_linha)< quantidade_pixels:
    pixel_adicionado = int(input("informe o numero: "))
    representacao_linha.append(pixel_adicionado)


def encontra_maior_numero(representacao_linha_pixel):
    maior_valor_pixel = 0

    for pixel in representacao_linha_pixel:
        if maior_valor_pixel < pixel:
            maior_valor_pixel = pixel 
    return maior_valor_pixel


def quantidade_valor_pixel(maior_numero, representacao_linha_pixel):
    quantidade_vezes_pixel_repetido = 0
    quantidade_vezes_repetidas = []

    for  referencia in range(0,maior_numero):
        for pixel in representacao_linha_pixel:
            if referencia == pixel:
                quantidade_vezes_pixel_repetido+=1
        quantidade_vezes_repetidas.append(quantidade_vezes_pixel_repetido)
        quantidade_vezes_pixel_repetido = 0
    return quantidade_vezes_repetidas

def calcula_acumulativa(quantidade_vezes_repetidas):
    referencia_acumulativa = 0
    resultado_acumulativa = []
    for valor in quantidade_vezes_repetidas:
        referencia_acumulativa += valor
        resultado_acumulativa.append(referencia_acumulativa)
    
    return resultado_acumulativa

def calcula_porcentagem(acumulativas):
    porcentagens = []
    operando = acumulativas[len(acumulativas) -1]
    for acumulativa in acumulativas:
        porcentagem = acumulativa / operando
        porcentagens.append(porcentagem)
        porcentagem = 0

    return porcentagens

def valores_equalizacao(porcentagens, maior_valor):
    valores_equalizacao = []

    for porcentagem in porcentagens:
        resultado = porcentagem * maior_valor
        valores_equalizacao.append(round(resultado))
        resultado = 0

    return valores_equalizacao

def equalizador(representacao_pixel, equalizados):
    for index in range(0, len(representacao_pixel)):
        representacao_pixel[index] = equalizados[representacao_pixel[index]]

    return representacao_pixel


maior_numero = encontra_maior_numero(representacao_linha)

conta_pixels_repetidos = quantidade_valor_pixel(maior_numero+1,representacao_linha)

acumulativa_numeros_informados =  calcula_acumulativa(conta_pixels_repetidos)

porcentagem = calcula_porcentagem(acumulativa_numeros_informados)

valores_calculados = valores_equalizacao(porcentagem,maior_numero)

linha_equalizada = equalizador(representacao_linha,valores_calculados)

print(" O Resultado da eqaulização é: " , linha_equalizada)


