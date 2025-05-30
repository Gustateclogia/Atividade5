import statistics
import statistics as st
from statistics import mean, median

#1Importe o módulo statistics e crie uma lista com 14 elementos contendo números em ordem crescente.
valores = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41]
print("Lista de valores:", valores)
#2Calcule a média e a mediana dos valores usando o módulo completo (import statistics).
media = statistics.mean(valores)
mediana = statistics.median(valores)
print(f'Média: {media}')
print(f'Mediana: {mediana}')
#3Use um alias (apelido) para o módulo statistics e refaça os cálculos. Dica: import statistics as st
media_alias = st.mean(valores)
mediana_alias = st.median(valores)
print(f'Média (com alias): {media_alias}')
print(f'Mediana (com alias): {mediana_alias}')
#4Agora, importe apenas as funções mean e median do módulo statistics e refaça os cálculos.
media_func = mean(valores)
mediana_func = median(valores)
print(f'Média (importação direta): {media_func}')
print(f'Mediana (importação direta): {mediana_func}')
#5Por fim, importe todas as funções do módulo statistics e calcule novamente a média e a mediana da lista.
media_all = mean(valores)
mediana_all = median(valores)
print(f'Média (importação total): {media_all}')
print(f'Mediana (importação total): {mediana_all}')


