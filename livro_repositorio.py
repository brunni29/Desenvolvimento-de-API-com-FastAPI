from modelos import Livro

# O acervo fica armazenado em memória.
# Somente este módulo acessa diretamente a coleção de livros.
_LIVROS = {
    1: Livro(
        id=1,
        titulo="Dom Casmurro",
        autor="Machado de Assis",
        ano_publicacao=1899,
        disponivel=True,
    ),
    2: Livro(
        id=2,
        titulo="O Cortiço",
        autor="Aluísio Azevedo",
        ano_publicacao=1890,
        disponivel=True,
    ),
    3: Livro(
        id=3,
        titulo="Memórias Póstumas de Brás Cubas",
        autor="Machado de Assis",
        ano_publicacao=1881,
        disponivel=False,
    ),
    4: Livro(
        id=4,
        titulo="Vidas Secas",
        autor="Graciliano Ramos",
        ano_publicacao=1938,
        disponivel=True,
    ),
    5: Livro(
        id=5,
        titulo="Capitães da Areia",
        autor="Jorge Amado",
        ano_publicacao=1937,
        disponivel=False,
    ),
}


def listar_livros() -> list[Livro]:
    """Retorna todos os livros cadastrados no acervo."""
    return [livro.model_copy() for livro in _LIVROS.values()]


def buscar_por_id(livro_id: int) -> Livro | None:
    """Busca um livro pelo identificador e retorna None se não existir."""
    livro = _LIVROS.get(livro_id)

    # A cópia evita que outra camada altere diretamente o objeto do acervo.
    return livro.model_copy() if livro is not None else None
