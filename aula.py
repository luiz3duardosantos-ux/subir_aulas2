#-----------Listas------------
tarefas = []  
tarefas_pend = []  
tarefas_conclu = []  
escolha = 0  
#-----------------------------
#----------FUNÇÕES------------
def add_tarefa(): # Função Adicionar Terefas
    taref = input("Digite o nome da Nova Tarefa: ")  
    tarefas.append(taref)  
    print("\nTarefa Adicionada!\n")  

def pend_tarefa(): # Função define tarefas pendentes
    if not tarefas:  
        print("\nNão possui tarefas para marcar como pendentes!\n")  
        return  
    for i, tarefa in enumerate(tarefas):  
        print(f"{i + 1} - {tarefa}")  
    
    esc2 = int(input("Número da tarefa a marcar como pendente: "))  
    
    if 1 <= esc2 <= len(tarefas):  
        tarefas_pend.append(tarefas.pop(esc2 - 1)) # Remove da lista de tarefas  
        print("\nTarefa adicionada como Pendente!\n")  
    else:  
        print("\nNúmero inválido!\n")  

def remov_tarefa(): # Função Remove Tarefas
    if not tarefas:  
        print("\nNão possui tarefas para remover!\n")  
        return  
    for i, tarefa in enumerate(tarefas):  
        print(f"{i + 1} - {tarefa}")  
    
    esc4 = int(input("\nNúmero da tarefa que deseja remover: "))  
    
    if 1 <= esc4 <= len(tarefas):  
        tarefas.pop(esc4 - 1)  
        print("\nTarefa removida com sucesso!\n")  
    else:  
        print("\nNúmero inválido!\n")  

def conclui_tarefa(): # Função Conclui tarefas
    if not tarefas:  
        print("\nNão possui tarefas para marcar como concluídas!\n")  
        return  
    for i, tarefa in enumerate(tarefas):  
        print(f"{i + 1} - {tarefa}")  
    
    esc3 = int(input("\nNúmero da tarefa a marcar como concluída: "))  
    
    if 1 <= esc3 <= len(tarefas):  
        tarefas_conclu.append(tarefas.pop(esc3 - 1)) # Remove da lista de tarefas  
        print("\nTarefa marcada como Concluída!\n")  
    else:  
        print("\nNúmero inválido!\n")  

#-----------------------------

#-------MENU PRINCIPAL--------
while escolha != 5:  
    print("Digite 1 para adicionar tarefas:")  
    print("Digite 2 para listar tarefas como pendentes:")  
    print("Digite 3 para listar tarefas como concluídas:")  
    print("Digite 4 para remover tarefas:")  
    print("Digite 5 para sair:")  
    escolha = int(input("Opção: "))  

    if escolha > 5 or escolha < 1:  
        print("\nPor favor, selecione uma das opções!\n")  
    else:  
        if escolha == 1:  
            add_tarefa()  
        elif escolha == 2:  
            pend_tarefa()  
        elif escolha == 3:  
            conclui_tarefa()  
        elif escolha == 4:    
            remov_tarefa()  

#-----------------------------

print(f"Tarefas gerais: {tarefas}")  
print(f"Tarefas pendentes: {tarefas_pend}")  
print(f"Tarefas concluídas: {tarefas_conclu}")  
print("\nFIM!")