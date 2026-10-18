def cadastrar_tarefa(tarefas):
    print("\n" + "-"*30)
    print("      CADASTRAR TAREFA")
    print("-"*30)
    
    while True:
        titulo = input("Título: ").strip()
        if titulo != "":
            break
        print("[Erro] O título é obrigatório e não pode ser apenas espaços em branco.")
    
    descricao = input("Descrição: ").strip()
    
    while True:
        prioridade_input = input("Prioridade (Alta, Média, Baixa): ").strip().lower()
        if prioridade_input in ["alta", "média", "media", "baixa"]:
            prioridade = prioridade_input.capitalize() 
            break
        print("[Erro] Opção inválida! Digite apenas Alta, Média ou Baixa.")
    
    data_limite = input("Data Limite (DD/MM/AAAA ou formato livre): ").strip()
    
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    tarefas.append(tarefa)
    print(f"\n[Sucesso] Tarefa '{titulo}' cadastrada com sucesso!")

def visualizar_tarefas(tarefas):
    print("\n" + "-"*30)
    print("      TAREFAS CADASTRADAS")
    print("-"*30)
    
    if len(tarefas) == 0:
        print("\n[Aviso] Não existem registros no momento.")
        return False # Retorna False para sabermos que a lista está vazia
    
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{indice}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {tarefa['descricao']}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data Limite: {tarefa['data_limite']}")
        print(f"  Status:      {tarefa['status']}")
    print("\n" + "-"*30)
    return True # Retorna True se houverem tarefas exibidas

def concluir_tarefa(tarefas):
    if not visualizar_tarefas(tarefas):
        return
    
    try:
        indice = int(input("\nDigite o número da tarefa que deseja concluir: "))
        if 1 <= indice <= len(tarefas):
            tarefas[indice - 1]["status"] = "Concluída"
            print(f"\n[Sucesso] Tarefa #{indice} marcada como concluída!")
        else:
            print("\n[Erro] Número de tarefa não encontrado.")
    except ValueError:
        print("\n[Erro] Por favor, digite um número válido.")

def excluir_tarefa(tarefas):
    if not visualizar_tarefas(tarefas):
        return
    
    try:
        indice = int(input("\nDigite o número da tarefa que deseja EXCLUIR: "))
        if 1 <= indice <= len(tarefas):
            tarefa_removida = tarefas.pop(indice - 1)
            print(f"\n[Sucesso] Tarefa '{tarefa_removida['titulo']}' foi excluída!")
        else:
            print("\n[Erro] Número de tarefa não encontrado.")
    except ValueError:
        print("\n[Erro] Por favor, digite um número válido.")

def editar_tarefa(tarefas):
    if not visualizar_tarefas(tarefas):
        return
    
    try:
        indice = int(input("\nDigite o número da tarefa que deseja editar: "))
        if 1 <= indice <= len(tarefas):
            tarefa = tarefas[indice - 1]
            print("\n[Aviso] Pressione ENTER caso não queira alterar o campo atual.")
            
            # Edição do Título
            novo_titulo = input(f"Título atual ({tarefa['titulo']}): ").strip()
            if novo_titulo != "":
                tarefa['titulo'] = novo_titulo
                
            # Edição da Descrição
            nova_descricao = input(f"Descrição atual ({tarefa['descricao']}): ").strip()
            if nova_descricao != "":
                tarefa['descricao'] = nova_descricao
                
            # Edição da Prioridade
            while True:
                nova_prioridade = input(f"Prioridade atual ({tarefa['prioridade']}): ").strip().lower()
                if nova_prioridade == "":
                    break # Mantém a antiga
                elif nova_prioridade in ["alta", "média", "media", "baixa"]:
                    tarefa['prioridade'] = nova_prioridade.capitalize()
                    break
                else:
                    print("[Erro] Opção inválida! Digite apenas Alta, Média ou Baixa, ou deixe em branco.")
                    
            # Edição da Data
            nova_data = input(f"Data Limite atual ({tarefa['data_limite']}): ").strip()
            if nova_data != "":
                tarefa['data_limite'] = nova_data
                
            print(f"\n[Sucesso] Tarefa #{indice} atualizada!")
        else:
            print("\n[Erro] Número de tarefa não encontrado.")
    except ValueError:
        print("\n[Erro] Por favor, digite um número válido.")

def main():
    tarefas = [] 
    
    while True:
        print("\n" + "="*40)
        print("          GERENCIADOR DE TAREFAS")
        print("="*40)
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Marcar tarefa como concluída")
        print("4. Editar tarefa")
        print("5. Excluir tarefa")
        print("6. Sair da aplicação")
        
        opcao = input("\nEscolha uma opção (1 a 6): ")
        
        if opcao == '1':
            cadastrar_tarefa(tarefas)
        elif opcao == '2':
            visualizar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            editar_tarefa(tarefas)
        elif opcao == '5':
            excluir_tarefa(tarefas)
        elif opcao == '6':
            print("\nEncerrando a aplicação... Até logo!")
            break
        else:
            print("\n[Erro] Opção inválida! Por favor, digite um número de 1 a 6.")

if __name__ == "__main__":
    main()
