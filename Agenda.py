Tarefas_lis = []

def adicionar():
    print("")
    print('Voce escolheu adicionar')
    print("")
    tit_tarefa = input('Qual a tarefa ? ')
    print('')
    descri_t = input('Qual a descrição? ')
    print('')
    Id_tarefa = int(input('Qual seu ID? '))
    print('')

    Tarefa_ad = (tit_tarefa, descri_t, Id_tarefa)

    Tarefas_lis.append(Tarefa_ad)




def listar():
    print('Você escolheu listar/imprimir sua atual lista de tarefas')
    for tit_tarefa, descri_t, Id_tarefa in Tarefas_lis:
        print('')
        print('*' * 50)
        print(f'Tarefa: {tit_tarefa}, com ID #{Id_tarefa}')
        print('')
        print(f'Descrição: {descri_t}')
        print('*' * 50)


def tarefa_esp():
    print('Você escolheu listar uma tarefa especifa')
    taref_esp = int(input('Qual ID da tarefa?'))
    for tarefa in Tarefas_lis:
        tit_tarefa, descri_t, Id_tarefa = tarefa
        if Id_tarefa == taref_esp:
            print(f'Você escolheu a {tit_tarefa}')
            print(f'Descrição: {descri_t}')

def atualizar():
    print("Você escolheu atualizar uma tarefa")
    att_id = int(input("Qual o ID da tarefa que você quer atualizar? "))

    for i, tarefa in enumerate(Tarefas_lis):
        tit_tarefa, descri_t, Id_tarefa = tarefa
        if Id_tarefa == att_id:
            print(f"Tarefa atual: Título: {tit_tarefa}, Descrição: {descri_t}, ID: {Id_tarefa}")
            print("Digite os novos dados (ou pressione ENTER para manter o atual):")

            novo_titulo = input("Novo título: ")
            nova_desc = input("Nova descrição: ")


            if novo_titulo == "":
                novo_titulo = tit_tarefa
            if nova_desc == "":
                nova_desc = descri_t


            Tarefas_lis[i] = (novo_titulo, nova_desc, Id_tarefa)
            print("Tarefa atualizada com sucesso.")
            break
    else:
        print("Tarefa com esse ID não foi encontrada.")

def deletar():
    print('Você escolheu deletar a tarefa')
    del_tarefa = int(input('Qual o Id da tarefa você quer deletar ? '))
    for i, tarefa in enumerate(Tarefas_lis):
        tit_tarefa, descri_t, Id_tarefa = tarefa
        if Id_tarefa == del_tarefa:
            Tarefas_lis.pop(i)
            print(f'Tarefa com o ID:{del_tarefa} foi deletada com sucesso!')

        else:
            print("Tarefa não encontrada")



def main():
    while True:
        print("")
        print("")
        print("Tarefas")
        print('1- Adicionar tarefa')
        print('2- Listar tarefas')
        print('3- Listar tarefa especifica')
        print('4- Atualizar tarefa')
        print('5- Deletar ')
        print('6- Encerrar, mostrar lista')
        print('')
        print("Qual a opção ?")
        opc = int(input(" "))
        if opc == 1:
            adicionar()

        elif opc == 2:
            listar()

        elif opc == 3:
            tarefa_esp()

        elif opc == 4:
            atualizar()

        elif opc == 5:
            deletar()

        elif opc == 6:
            listar()
            break

main()
