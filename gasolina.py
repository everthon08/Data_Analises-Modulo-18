
sns.set(style= "darkgrid")
grafico= sns.lineplot(x= "dia", y= "venda", data= df_preco_gasolina)
plt.title("Preço médio de venda da gasolina em Sp")
plt.xlabel("dia")
plt.ylabel("venda")
plt.savefig("gasolina.png")
plt.show()
