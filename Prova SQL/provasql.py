import mysql.connector

def conectar_banco():
    conexao = mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="seu_banco_de_dados"
    )
    return conexao

def criar_personagem(nome, classe, nivel, pontos_de_vida):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO personagens (nome, classe, nivel, pontos_de_vida) VALUES (%s, %s, %s, %s)"
    val = (nome, classe, nivel, pontos_de_vida)
    cursor.execute(sql, val)
    conexao.commit()
    print(f"Novo personagem '{nome}' criado com sucesso!")
    conexao.close()

def listar_personagens():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM personagens")
    personagens = cursor.fetchall()
    for personagem in personagens:
        print(personagem)
    conexao.close()

def atualizar_personagem(id, nome, classe, nivel, pontos_de_vida):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "UPDATE personagens SET nome = %s, classe = %s, nivel = %s, pontos_de_vida = %s WHERE id = %s"
    val = (nome, classe, nivel, pontos_de_vida, id)
    cursor.execute(sql, val)
    conexao.commit()
    print(f"Dados do personagem com ID {id} atualizados com sucesso!")
    conexao.close()

def excluir_personagem(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "DELETE FROM personagens WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conexao.commit()
    print(f"Personagem com ID {id} excluído com sucesso!")
    conexao.close()

if __name__ == "__main__":
    criar_personagem("Guerreiro", "Guerreiro", 1, 100)

    print("Todos os personagens:")
    listar_personagens()

    atualizar_personagem(1, "Novo Nome", "Guerreiro", 2, 150)

    print("Todos os personagens após a atualização:")
    listar_personagens()

    excluir_personagem(1)

    print("Todos os personagens após a exclusão:")
    listar_personagens()
