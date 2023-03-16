faturamento = {
'SP' : 67836.43,
'RJ' : 36678.66,
'MG' : 29229.88,
'ES' : 27165.48,
'Outros' : 19849.53
}
total = sum(faturamento.values())

print('\n======= O percentual de contrubuição de cada estado é: =======')

for uf in faturamento:
    percentual = round(faturamento[uf]/total*100,3)
    percentual2 = (faturamento[uf]/total)*100

    print(f'[{uf}] => {percentual} %')
