import subprocess
from terminaltables import AsciiTable #depende de terminal tables
def get_projects():
    b = ["task",'projects']
    output = subprocess.run(b,stdout=subprocess.PIPE).stdout.decode('utf-8')
    with open("temp.txt", "w") as text_file:
            text_file.write(output)

    listado = []

    with open('temp.txt', 'r') as lines:
        for line in lines:
            y = line.split()
            listado.append(y)


    del listado[0:3] #limpando cabeçalho
    del listado [-2:] #limpando rodape
    #loop para deletar o numero de tasks em um projeto.
    a = 0
    for i in listado:
        del i[-1]
        for b in range(len(i)):
            i[b] = (i[b] + " ")
        i.append(''.join(i))
        del i[:-1]
        i[0] = i[0].rstrip()
        a += 1
        i.append(a)
        #possivelmente tenho que alterar isso depois usar PATH de alguma forma.
    listado.append(["Adicionar Novo Projeto", a+1 ])
    listado.insert(0,["Projeto","#"])
    listado.append(["Sair",0])
    return listado
    
def loop_simples_de_coleta(argumento,errormsg,classe):
	if classe == "int":
		while True:
			try:
				resposta = int(input(argumento))
				return resposta
			except:
				print(errormsg)
	elif classe == "stg":
		while True:
			try:
				resposta = input(argumento)
				return resposta
			except:
				print(errormsg)
	elif classe == "bool":
		while True:
			try:
				resposta = bool(int(input(argumento)))
				return resposta
			except:
				print(errormsg)
	elif classe == "float":
		while True:
			try:
				resposta = float(input(argumento))
				return resposta
			except:
				print(errormsg)

def receive_input(lista=list,valor=int):
    for i in lista:
        if i[-1] == valor:
            return i[0]
        else:
            continue

def tratar_input(projeto=str):
    if projeto == "Adicionar Novo Projeto":
        return "add"
    else:
        return projeto

def entrar_input(valor=str):
    if valor == "add":
        nome = input("Nome do Projeto:\n""    ")
        c = "project:" + "'" + nome + "'"
        task = input("Nome da Entrada:\n""    ")
        d = "'" + task + "'"
        b = ["task",'project:',c,d, valor]
        subprocess.run("clear")
        subprocess.run(b,stdout=subprocess.PIPE).stdout.decode('utf-8')
    elif valor == "Sair":
        menu_fun()
    else:
        nome = input("Nome da Entrada:\n""    ")
        c = "'" + nome + "'"
        d = "project:" + "'" + valor + "'" 
        b = ["task",d,c,'add']
        subprocess.run("clear")
        subprocess.run(b,stdout=subprocess.PIPE).stdout.decode('utf-8')

def lista_projetos():
    listado = get_projects()
    del listado[-2:]
    listado.append(["Voltar",0])
    listado.insert(1,["All",1000])
    table_listado = AsciiTable(listado)
    print(table_listado.table)
    r = loop_simples_de_coleta(h,t,i)
    if r == 0:
        menu_fun()
    elif r == 1000:
        task_list = ["task", "list"]
        subprocess.run("clear")
        print(subprocess.run(task_list,stdout=subprocess.PIPE).stdout.decode('utf-8'))
    else:
        rr = receive_input(listado,r)
        c = "project:" + "'" + str(rr) + "'"
        task_list = ["task",c,"list"]
        print(subprocess.run(task_list,stdout=subprocess.PIPE).stdout.decode('utf-8'))

def burnout():
    listado = get_projects()
    del listado[-2:]
    listado.append(["Voltar",0])
    print(AsciiTable(listado).table)
    r = loop_simples_de_coleta(h,t,i)
    if r == 0:
        menu_fun()
    else:
        rr = receive_input(listado,r)
        c = "project:" + "'" + str(rr) + "'"
        b = ["task","burndown.daily ",c]
        print(subprocess.run(b,stdout=subprocess.PIPE).stdout.decode('utf-8'))

def adicionar():
    listado = get_projects()
    table_listado = AsciiTable(listado)
    print(table_listado.table)
    r = loop_simples_de_coleta(h,t,i)
    projeto = receive_input(listado,r)
    entrar_input(tratar_input(projeto))

def menu_fun():
    subprocess.run("clear")
    while True:
        menu = AsciiTable([["Opção","#"],["Entrada de Tarefas",1],["Lista de Tarefas",2],["Burnout Chart",3],["Sair",0]])
        print(menu.table)
        menu_response = loop_simples_de_coleta(h,t,i)
        if menu_response == 1:
            adicionar()
        elif menu_response == 2:
            lista_projetos()
        elif menu_response ==3:
            burnout()
        elif menu_response == 0:
            exit()
        else:
            continue
t = "Tente mais uma vez\n\n"
i = "int"
s = "str"
h = "Input:     "
if __name__ == '__main__':
    menu_fun()
