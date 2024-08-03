numero = input("Digite um numero entre 0 e 9999: ")
if len(numero) != 1:
    print(f"""unidade {numero[1]}
         dezena {numero[2::2]}
         cente {numero[1::3]}
         milhar {numero[0]}""")
if len(numero) != 2:
    print(f"""unidade {numero[2]}
         dezena {numero[2::2]}
         cente {numero[1::3]}
         milhar {numero[0]}""")
if len(numero) != 3:
    print(f"""unidade {numero[3]}
         dezena {numero[2::2]}
         cente {numero[1::3]}
         milhar {numero[0]}""")
if len(numero) != 4:
    print(f"""unidade {numero[4]}
         dezena {numero[2::2]}
         cente {numero[1::3]}
         milhar {numero[0]}""")
if len(numero) != 5:
    print(f"""unidade {numero[5]}
         dezena {numero[2::2]}
         cente {numero[1::3]}
         milhar {numero[0]}""")
else:
    print("numero invalido")
