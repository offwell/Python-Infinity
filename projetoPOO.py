class Livro:
    def __init__(self, titulo, autor, ID):
        self.titulo = titulo
        self.autor = autor
        self.ID = ID
        self.emprestado = False

class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico = []

class Biblioteca:
    def __init__(self):
        self.catalogo = {}
        self.registro_membros = {}

    def adicionar_livro(self, livro):
        self.catalogo[livro.ID] = livro

    def adicionar_membro(self, membro):
        self.registro_membros[membro.numero_membro] = membro

    def emprestar_livro(self, livro_id, numero_membro):
        livro = self.catalogo.get(livro_id)
        membro = self.registro_membros.get(numero_membro)
        if livro and membro:
            if not livro.emprestado:
                livro.emprestado = True
                membro.historico.append(livro)
                return True
        return False

    def registrar_devolucao(self, livro_id, numero_membro):
        livro = self.catalogo.get(livro_id)
        membro = self.registro_membros.get(numero_membro)
        if livro and membro:
            if livro in membro.historico:
                livro.emprestado = False
                membro.historico.remove(livro)
                return True
        return False

    def pesquisar_livro_por_titulo(self, titulo):
        return [livro for livro in self.catalogo.values() if livro.titulo == titulo]

    def pesquisar_livro_por_autor(self, autor):
        return [livro for livro in self.catalogo.values() if livro.autor == autor]

    def pesquisar_livro_por_ID(self, ID):
        livro = self.catalogo.get(ID)
        return livro if livro else None



livro1 = Livro("Python Programming", "John Smith", 101)
livro2 = Livro("Data Science Handbook", "Alice Johnson", 102)

membro1 = Membro("Alice", 1001)
membro2 = Membro("Bob", 1002)


biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_membro(membro1)
biblioteca.adicionar_membro(membro2)

biblioteca.emprestar_livro(101, 1001)

biblioteca.registrar_devolucao(101, 1001)

print(biblioteca.pesquisar_livro_por_titulo("Python Programming"))
print(biblioteca.pesquisar_livro_por_autor("Alice Johnson"))
print(biblioteca.pesquisar_livro_por_ID(102))
