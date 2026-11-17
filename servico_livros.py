import livro_repositorio
from modelos import Livro


class LivroNaoEncontrado(Exception):
    """Exceção usada quando o livro solicitado não existe no acervo."""

    pass


def listar_livros() -> list[Livro]:
    """Retorna a lista de livros por meio do repositório."""
    return livro_repositorio.listar_livros()


def consultar_livro(livro_id: int) -> Livro:
    """Consulta um livro e informa à API quando ele não for encontrado."""
    livro = livro_repositorio.buscar_por_id(livro_id)

    if livro is None:
        raise LivroNaoEncontrado(f"Livro {livro_id} não encontrado")

    return livro
