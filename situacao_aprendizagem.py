import datetime
import os

quantidade = []
contador = 0
valores = [1070.00, 2970.00, 3999.00, 1699.00]

def menu():
    print("""
    Código      Descrição 
    --------- -------------------------------------------------- 
        1       Fogão 4 Bocas Electrolux Automático 
        2       Geladeira Brastemp Frost Free 
        3       Freezer Vertical Frost Free Brastemp 
        4       Smart TV LED 40" Full HD Philco 
    """)

def quantidade_produtos():
    for i in range(4):
        num = int(input(f"Digite a quantidade do produto do código {i + 1} que você deseja comprar: "))
        quantidade.append(num)

def informacoes_cliente():
    global nome, estado, cidade, rua
    nome = input("Informe seu nome: ")
    estado = input("Informe seu estado: ")
    cidade = input("Informe sua cidade: ")
    rua= input("Informe sua rua: ")

def epigrafe():
    data = datetime.datetime.now()
    print(f""" 
    Nota fiscal nr: {contador} Data Emissão: {data.day}/{data.month}/{data.year} Hora: {data.hour}:{data.minute}
    Cliente: {nome}
    Endereço: {rua}
    Cidade: {cidade}
    Estado: {estado}
    """)

def produto():
    global total
    total_1 = valores[0] * quantidade[0]
    total_2 = valores[1] * quantidade[1]
    total_3 = valores[2] * quantidade[2]
    total_4 = valores[3] * quantidade[3]
    total = total_1 + total_2 + total_3 +total_4
    print(f"""
    -------------------------------------------------------- PRODUTOS ----------------------------------------------------
     Código                      Descrição                      Qtde        UM       Vlr.Unitário        Vlr.Total
    --------- ----------------------------------------------   -------  -----------  ----------------  ----------------
        1           Fogão 4 Bocas Electrolux Automático           {quantidade[0]}       Unidade        {valores[0]}            {total_1}
        2           Geladeira Brastemp Frost Free                 {quantidade[1]}       Unidade        {valores[1]}            {total_2}
        3           Freezer Vertical Frost Free Brastemp          {quantidade[2]}       Unidade        {valores[2]}            {total_3}
        4           Smart TV LED 40" Full HD Philco               {quantidade[3]}       Unidade        {valores[3]}            {total_4}
    ---------- ---------------------------------------------   -------  -----------  ----------------  ----------------
                                                                                                  Total:{total}
    """)

def impostos():
    icms = total * .17
    cofins = total * .03
    pis = total * .0065
    frete = total * .05
    print(f"ICMS: {icms:.2f} PIS: {pis:.2f} COFINS: {cofins:.2f} FRETE: {frete:.2f}")

def estoque():
    saldos = [100 - quantidade[0], 280 - quantidade[1], 250 - quantidade[2], 400 - quantidade[3],]
    print(f"""
      Produto                       Descrição                                Saldo
    ------------ ---------------------------------------------------------- ------- 
         1                Fogão 4 Bocas Electrolux Automático                {saldos[0]}
         2                Geladeira Brastemp Frost Free                      {saldos[1]} 
         3                Freezer Vertical Frost Free Brastemp               {saldos[2]}  
         4                Smart TV LED 40" Full HD Philco                    {saldos[3]}   
    ------------ ---------------------------------------------------------- -------
    """)

while True:
    informacoes_cliente()
    menu()
    quantidade_produtos()
    os.system("cls")
    contador += 1
    epigrafe()
    produto()
    impostos()
    estoque()
    continuar = int(input("Deseja realizar outra compra? \n 0-Sim \n 1-Não \n"))
    if continuar == 0:
        continue
    elif continuar == 1:
        break
    else:
        print("Resposta inválida!")