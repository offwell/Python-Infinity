alunos = {}

def AdicionarAluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    alunos[matricula] = nome
    print("Aluno adicionado com sucesso.")

def RemoverAluno():
    matricula = input("Digite o número de matrícula do aluno que deseja remover: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso.")
    else:
        print("Aluno não encontrado.")

def AtualizarAluno():
    matricula = input("Digite o número de matrícula do aluno que deseja atualizar: ")
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = novo_nome
        print("Nome do aluno atualizado com sucesso.")
    else:
        print("Aluno não encontrado.")

def VerAlunos():
    if alunos:
        print("Lista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
    else:
        print("Não há alunos cadastrados.")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Atualizar aluno")
        print("4. Ver alunos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            AdicionarAluno()
        elif opcao == "2":
            RemoverAluno()
        elif opcao == "3":
            AtualizarAluno()
        elif opcao == "4":
            VerAlunos()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
