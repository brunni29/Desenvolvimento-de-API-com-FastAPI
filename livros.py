from typing import Annotated

from fastapi import FastAPI, HTTPException, Path

from modelos import Livro
from servico_livros import LivroNaoEncontrado, consultar_livro, listar_livros


app = FastAPI(title="API do Acervo da Biblioteca")


@app.get("/livros", response_model=list[Livro])
def obter_livros() -> list[Livro]:
    """Retorna todos os livros cadastrados no acervo."""
    return listar_livros()


@app.get("/livros/{livro_id}", response_model=Livro)
def obter_livro(
    livro_id: Annotated[int, Path(gt=0)],
) -> Livro:
    """Retorna um livro pelo ID ou HTTP 404 quando ele não existir."""
    try:
        return consultar_livro(livro_id)
    except LivroNaoEncontrado as erro:
        # A exceção pertence à regra de negócio; aqui ela é convertida para HTTP 404.
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado",
        ) from erro
