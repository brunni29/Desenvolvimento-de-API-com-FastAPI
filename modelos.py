from pydantic import BaseModel, Field, field_validator


class Livro(BaseModel):
    """Modelo que representa um livro do acervo da biblioteca."""

    id: int = Field(gt=0, strict=True)
    titulo: str = Field(min_length=1)
    autor: str = Field(min_length=1)
    ano_publicacao: int = Field(gt=0, strict=True)
    disponivel: bool = Field(strict=True)

    @field_validator("titulo", "autor")
    @classmethod
    def texto_nao_pode_ser_vazio(cls, valor: str) -> str:
        """Impede que título e autor sejam vazios ou formados apenas por espaços."""
        if not valor.strip():
            raise ValueError("O texto não pode ser vazio")
        return valor
