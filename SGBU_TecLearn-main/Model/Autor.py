"""
Model: Autor
Módulo 2 - Catálogo de Livros (Autores)

Este arquivo deve ser implementado pelos alunos usando TDD (Test Driven Development).

Requisitos:
- Classe Autor com atributos: id, nome, nacionalidade, biografia
- Validações:
  * Nome não pode ser vazio
  * Nome deve ter pelo menos 3 caracteres

Exemplos de testes a implementar:
- test_criar_autor_valido()
- test_criar_autor_sem_nome()
- test_criar_autor_nome_curto()
- test_atualizar_biografia()
"""

class Autor:
    def __init__(self, id, nome, nacionalidade=None, biografia=None):
        self.id = id
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.biografia = biografia
        self.validar()

    def validar(self):
        if not self.nome or not self.nome.strip():
            raise ValueError("O nome do autor não pode ser vazio.")
        if len(self.nome.strip()) < 3:
            raise ValueError("O nome do autor deve ter pelo menos 3 caracteres.")

    def __repr__(self):
        return f"Autor(id={self.id}, nome='{self.nome}', nacionalidade='{self.nacionalidade}')"

    def to_dict(self):
        """Retorna os dados do autor em formato de dicionário."""
        return {
            "id": self.id,
            "nome": self.nome,
            "nacionalidade": self.nacionalidade,
            "biografia": self.biografia
        }
