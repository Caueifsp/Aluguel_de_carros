#--------------------------------------------------
def menu():
    print("\n-----------------------------------")
    print("Gerenciar Veiculos:")
    print("    Inserir veiculo........1")
    print("    Listar veiculos........2")
    print("    Pesquisar veiculo......3")
    print("    Atualizar veiculo......4")
    print("    Remover veiculo........5")
    print("\nGerenciar Clientes:")
    print("     Inserir cliente...... 6")
    print("     Listar clientes.......7")
    print("     Pesquisar cliente.....8")
    print("     Atualizar cliente.....9")
    print("     Remover cliente.......10")
    print("\nRelatórios.................11")
    print("\nSair do programa...........0")
    opçao_do_usuario = input("-> ")
    return opçao_do_usuario
#--------------------------------------------------   
def busca(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
              return i
    return -1             
#--------------------------------------------------
def inserir_veiculo(veiculos_codigo,veiculos_modelo,veiculos_ano):
    v_codigo = input("Informe o código: ")

    if busca(veiculos_codigo,v_codigo) == -1:
      v_modelo = input("Informe o modelo: ")
      v_ano = int(input("Informe o ano de fabricação: "))
      veiculos_codigo.append(v_codigo)
      veiculos_modelo.append(v_modelo)
      veiculos_ano.append(v_ano)
      print("\nVeiculo código: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano) + " inserido com sucesso")
    else:
        print("Código " + v_codigo + " já está cadastrado!")  
#--------------------------------------------------
def listar_veiculos(veiculos_codigo,veiculos_modelo,veiculos_ano):
    if len(veiculos_codigo) > 0:
      for i in range(len(veiculos_codigo)):
        v_codigo = veiculos_codigo[i]
        v_modelo = veiculos_modelo[i]
        v_ano = veiculos_ano[i]
        print("\nVeiculo código: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))
    else:
        print("Não há veiculos a serem listados!")    
#--------------------------------------------------
def pesquisar_veiculo(veiculos_codigo,veiculos_modelo,veiculos_ano):
    codigo_pesquisar = input("Informe o código do veiculo a ser pesquisado: ")
    indice = busca(veiculos_codigo, codigo_pesquisar)
    if indice != -1:
        v_codigo = veiculos_codigo[indice]
        v_modelo = veiculos_modelo[indice]
        v_ano = veiculos_ano[indice]
        print("\nVeiculo encontrado!")
        print("\nVeiculo código: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))
    else:
        print("\nVeiculo de código " + codigo_pesquisar + " não encontrado!")    
#--------------------------------------------------
def atualizar_veiculo(veiculos_codigo,veiculos_modelo,veiculos_ano):
    codigo_atualizar = input("Informe o código do veiculo a ser atualizado: ")
    indice = busca(veiculos_codigo, codigo_atualizar)
    if indice != -1:
       v_modelo = input("Informe o novo modelo: ")
       v_ano = input("Informe o novo ano de fabricação: ")
       veiculos_modelo[indice] = v_modelo
       veiculos_ano[indice] = v_ano 
       print("Veiculo atualizado com sucesso!")
    else:
        print("\nVeiculo de código " + codigo_atualizar + " não encontrado!")    
#--------------------------------------------------
# remove deslocando os elementos
def remover1(lista, indice):
    i = indice
    while i < len(lista) - 1:
          lista[i] = lista[i + 1]
          i = i + 1
    lista.pop()    
    
# remove colocando o ultimo elemento na posicao que eu quero remover      
def remover2(lista, indice):
    ultimo_indice = len(lista) - 1
    lista[indice] = lista[ultimo_indice]
    lista.pop()
#--------------------------------------------------
def remover_veiculo(veiculos_codigo,veiculos_modelo,veiculos_ano):
    codigo_remover = input("Informe o código do veiculo a ser removido: ")
    indice = busca(veiculos_codigo, codigo_remover)
    if indice != -1:
        remover2(veiculos_codigo, indice)
        remover2(veiculos_modelo, indice)
        remover2(veiculos_ano, indice)
        print("Veiculo removido com sucesso!")
    else:
        print("\nVeiculo de código " + codigo_remover + " não encontrado!")    
#--------------------------------------------------
def inserir_cliente(clientes_cpf,clientes_nome,clientes_ano):
    year = datetime.date.today().year
    c_cpf = input("Informe o CPF: ")
    if busca(clientes_cpf,c_cpf) == -1:
       c_nome = input("Informe o nome: ")
       c_ano = int(input("Informe o ano: "))
       if year - c_ano >= 18:
          clientes_cpf.append(c_cpf)
          clientes_nome.append(c_nome)
          clientes_ano.append(c_ano)
          print("\nCliente de CPF: " + c_cpf + ", Nome: " + c_nome + ", Ano de nascimento: " + str(c_ano) + " inserido com sucesso!")        
       else:
           print("\nNão é possível cadastrar cliente menor de idade!")  
    else:
       print("\nCPF " + c_cpf + " já está cadastrado!")   
#--------------------------------------------------
def listar_clientes(clientes_cpf,clientes_nome,clientes_ano):
    if len(clientes_cpf) > 0:
      for i in range(len(clientes_cpf)):
        c_cpf = clientes_cpf[i]
        c_nome = clientes_nome[i]
        c_ano = clientes_ano[i]
        print("\nCliente de CPF: " + c_cpf + ", Nome: " + c_nome + ", Ano de nascimento: " + str(c_ano))
    else:
        print("Não há clientes a serem listados!")    
#--------------------------------------------------
def pesquisar_cliente(clientes_cpf,clientes_nome,clientes_ano):
    cpf_pesquisar = input("Informe o CPF do cliente a ser pesquisado: ")
    indice = busca(clientes_cpf, cpf_pesquisar)
    if indice != -1:
       c_cpf = clientes_cpf[indice]
       c_nome = clientes_nome[indice]
       c_ano = clientes_ano[indice]
       print("\nCliente encontrado!")
       print("\nCliente de CPF: " + c_cpf + ", Nome: " + c_nome + ", Ano de nascimento: " + str(c_ano))
    else:
       print("\nCliente de CPF " + cpf_pesquisar + " não encontrado!")   
#--------------------------------------------------
def atualizar_cliente(clientes_cpf,clientes_nome,clientes_ano):
    cpf_atualizar = input("Informe o CPF do cliente a ser atualizado: ")
    indice = busca(clientes_cpf, cpf_atualizar)
    if indice != -1:
       c_cpf = input("Informe o novo CPF: ")
       c_nome = input("Informe o novo nome: ")
       c_ano = input("Informe o novo ano de nascimento: ")
       clientes_cpf[indice] = c_cpf
       clientes_nome[indice] = c_nome
       clientes_ano[indice] = c_ano
       print("\nCliente atualizado com sucesso!")
    else:
       print("\nCliente de CPF " + cpf_atualizar + " não encontrado!")   
#--------------------------------------------------
def remover_cliente(clientes_cpf,clientes_nome,clientes_ano):
    cpf_remover = input("Informe o CPF do cliente a ser removido: ")
    indice = busca(clientes_cpf, cpf_remover)
    if indice != -1:
       remover2(clientes_cpf, indice)
       remover2(clientes_nome, indice)
       remover2(clientes_ano, indice)
       print("Cliente removido com sucesso!")
    else:
       print("\nCliente de CPF " + cpf_remover + " não encontrado!")   
        
#--------------------------------------------------
def modelo_maior_qtd(veiculos_modelo):
    if len(veiculos_modelo) > 0:
      contagem_modelos = {}
      qtd_modelo_maior_qtd = 0
      for modelo in veiculos_modelo:
         if modelo not in contagem_modelos:
             contagem_modelos[modelo]=1
         else:
            contagem_modelos[modelo] = contagem_modelos[modelo]+1
         if contagem_modelos[modelo] > qtd_modelo_maior_qtd:
             qtd_modelo_maior_qtd = contagem_modelos[modelo]      
      print("\nModelo(s) presente(s) em maior quantidade: ")
      for modelo in contagem_modelos:
        if contagem_modelos[modelo] == qtd_modelo_maior_qtd:
             print("\n" + modelo)
    else:
        print("Não há veiculos cadastrados!")        
             
#--------------------------------------------------
def total_qtd_mod(veiculos_modelo):
    modelos_contados = []
    qtd_modelo_atual = 0
    if len(veiculos_modelo) > 0:
      for i in range(len(veiculos_modelo)):
          qtd_modelo_atual = 0
          if veiculos_modelo[i] not in modelos_contados:
              for j in range(len(veiculos_modelo)):
                  if veiculos_modelo[j] == veiculos_modelo[i]:
                      qtd_modelo_atual = qtd_modelo_atual + 1
              modelos_contados.append(veiculos_modelo[i])
              print("\nVeiculo modelo: " + veiculos_modelo[i] + ", quantidade: " + str(qtd_modelo_atual))
    else:
        print("Não há veiculos cadastrados!")          

#--------------------------------------------------
def carro_mais_antigo(veiculos_codigo,veiculos_modelo, veiculos_ano):
    if len(veiculos_ano) > 0:
        ano_mais_velho = veiculos_ano[0]  
        for i in range(1, len(veiculos_ano)):
            v_ano = veiculos_ano[i]
            if v_ano <= ano_mais_velho:
                ano_mais_velho = v_ano
        print("\nCarro(s) mais antigo(s):")
        i = 0 
        for i in range(len(veiculos_ano)):
          if veiculos_ano[i] == ano_mais_velho:
             v_codigo = veiculos_codigo[i]
             v_modelo = veiculos_modelo[i]
             v_ano = veiculos_ano[i]
             print("\nCódigo: " + v_codigo + ", Modelo: " + v_modelo + ", Ano de fabricação: " + str(v_ano))
    else:
        print("Não há veiculos cadastrados!")        
#--------------------------------------------------
def carro_mais_atual(veiculos_codigo,veiculos_modelo, veiculos_ano):
    if len(veiculos_ano) > 0: 
        ano_mais_novo = veiculos_ano[0]
        for i in range(1, len(veiculos_ano)):
            v_ano = veiculos_ano[i]
            if v_ano >= ano_mais_novo:
                ano_mais_novo = v_ano
        print("\nCarro(s) mais novo(s):")
        i = 0
        for i in range(len(veiculos_ano)):
           if veiculos_ano[i] == ano_mais_novo:
             v_codigo = veiculos_codigo[i]
             v_modelo = veiculos_modelo[i]
             v_ano = veiculos_ano[i]
             print("\nCódigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))   
    else:
        print("Não há veiculos cadastrados!")
#--------------------------------------------------
def porcent_nao_ipva(veiculos_ano):
    if len(veiculos_ano) > 0:
       year = datetime.date.today().year
       carros_mais_20anos = []
       for i in range(len(veiculos_ano)):
           diferenca_anos = year - veiculos_ano[i]
           if diferenca_anos > 20:   
             carros_mais_20anos.append(veiculos_ano[i])
       porcentagem = len(carros_mais_20anos) / len(veiculos_ano)
       if porcentagem > 0: 
          print("Percentual de veiculos que não pagam IPVA: {:.0%}".format(porcentagem))
       else:
          print("Todos os carros cadastrados precisam pagar IPVA!")   
    else:
        print("Não há veiculos cadastrados!")   

#--------------------------------------------------
def qtd_porcent_por_idade(clientes_ano):
    if len(clientes_ano) > 0:
      year = datetime.date.today().year
      qtd_jovens = qtd_adultos = qtd_idosos = 0

      for i in range(len(clientes_ano)):
         idade = year - clientes_ano[i]
         if idade >= 18 and idade <= 23:
             qtd_jovens = qtd_jovens + 1
         elif idade >= 24 and idade <= 69:
             qtd_adultos = qtd_adultos + 1
         else:
             qtd_idosos = qtd_idosos + 1  

      porcent_jovens = qtd_jovens / len(clientes_ano)
      porcent_adultos = qtd_adultos / len(clientes_ano)
      porcent_idosos = qtd_idosos / len(clientes_ano) 
      
      print("\nQuantidade de clientes jovens: {}".format(qtd_jovens) + ", Percentual: {:.0%}".format(porcent_jovens))
      print("\nQuantidade de clientes adultos: {}".format(qtd_adultos) + ", Percentual: {:.0%}".format(porcent_adultos)) 
      print("\nQuantidade de clientes idosos: {}".format(qtd_idosos) + ", Percentual: {:.0%}".format(porcent_idosos)) 
    else:
        print("Não há clientes cadastrados!")

#--------------------------------------------------
def relatorio(veiculos_codigo,veiculos_modelo,veiculos_ano,clientes_ano):
    print("-----------------------------------")
    print("Escolha um relatório: \n")
    print("Modelo de carro disponivel em maior quantidade...............1")
    print("Modelos e quantidades disponiveis de cada um.................2")
    print("Informações do(s) carro(s) mais antigo(s)....................3")
    print("Informações do(s) carro(s) mais atual(is)....................4")
    print("Porcentagem de carros que não pagam IPVA em SP...............5")
    print("Quantidade/porcentagem de clientes jovens, adultos e idosos..6")
    print("Retornar ao menu principal...................................0")
    opção_usuario = input("-> ")
    if opção_usuario == '1':
        modelo_maior_qtd(veiculos_modelo)
    elif opção_usuario == '2':
        total_qtd_mod(veiculos_modelo)
    elif opção_usuario == '3':
        carro_mais_antigo(veiculos_codigo,veiculos_modelo, veiculos_ano)
    elif opção_usuario == '4':
        carro_mais_atual(veiculos_codigo,veiculos_modelo, veiculos_ano)
    elif opção_usuario == '5':
        porcent_nao_ipva(veiculos_ano)
    elif opção_usuario == '6':
        qtd_porcent_por_idade(clientes_ano)
    elif opção_usuario == '0':
          main()
    else:
        print("Opção inválida!!! Escolha novamente!")      
#--------------------------------------------------
def main():

    veiculos_codigo = []
    veiculos_modelo = []
    veiculos_ano = []

    clientes_cpf = []
    clientes_nome = []
    clientes_ano = []

    opção = 'x'   
    while opção != '0':
          opção = menu()
          if opção == '1':
              inserir_veiculo(veiculos_codigo,veiculos_modelo,veiculos_ano) 
          elif opção == '2': 
              listar_veiculos(veiculos_codigo,veiculos_modelo,veiculos_ano) 
          elif opção == '3':
              pesquisar_veiculo(veiculos_codigo,veiculos_modelo,veiculos_ano)
          elif opção == '4':
              atualizar_veiculo(veiculos_codigo,veiculos_modelo,veiculos_ano) 
          elif opção == '5':
              remover_veiculo(veiculos_codigo,veiculos_modelo,veiculos_ano)
          elif opção == '6':
              inserir_cliente(clientes_cpf,clientes_nome,clientes_ano)  
          elif opção == '7':
              listar_clientes(clientes_cpf,clientes_nome,clientes_ano)
          elif opção == '8':
              pesquisar_cliente(clientes_cpf,clientes_nome,clientes_ano)
          elif opção == '9':
              atualizar_cliente(clientes_cpf,clientes_nome,clientes_ano)
          elif opção == '10':
              remover_cliente(clientes_cpf,clientes_nome,clientes_ano)
          elif opção == '11':
              relatorio(veiculos_codigo,veiculos_modelo,veiculos_ano,clientes_ano)          
          elif opção == '0':
              print("Obrigado por usar nosso programa!!!")  
          else:
              print("Opção inválida!!! Escolha novamente!")             

#--------------------------------------------------

#Programa principal
import datetime
main()