ism = ["Ali", "Vali", "Jasur"]
yosh = [20, 25, 30]

birlashtir = list(zip(ism, yosh))

natija = [f"{i[0]} ({i[1]} yoshda)" for i in birlashtir]

print(natija)
