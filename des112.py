from afins.ultilidadescev.dados import tratamento,moeda

quantia = tratamento.correcao('Digite o preço')
moeda.resumo(quantia,80,35)