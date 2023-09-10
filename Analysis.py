import xlsxwriter

# Resultados de similaridade
results = [
    ("Áudio 1-Áudio 2", result1),
    ("Áudio 1-Áudio 3", result2),
    ("Áudio 1-Áudio 4", result3),
    ("Áudio 2-Áudio 3", result4)
]

# Crie um arquivo do Excel
workbook = xlsxwriter.Workbook('resultados_de_similaridade.xlsx')
worksheet = workbook.add_worksheet()

# Escreva os resultados na planilha
row = 0
col = 0
for pair, similarity in results:
    worksheet.write(row, col, pair)
    worksheet.write(row, col + 1, similarity)
    row += 1

# Crie um gráfico de barras
chart = workbook.add_chart({'type': 'column'})
chart.add_series({'name': 'Similaridade', 'categories': '=Sheet1!$A$1:$A$4', 'values': '=Sheet1!$B$1:$B$4'})

# Insira o gráfico na planilha
worksheet.insert_chart('D2', chart)

# Salve o arquivo do Excel
workbook.close()

print("Gráfico gerado com sucesso. Verifique 'resultados_de_similaridade.xlsx'.")
