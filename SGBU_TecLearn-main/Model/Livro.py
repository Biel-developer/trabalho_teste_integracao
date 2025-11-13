"""
Model: Livro
Módulo 2 - Catálogo de Livros

Este arquivo deve ser implementado pelos alunos usando TDD (Test Driven Development).

Requisitos:
- Classe Livro com atributos: id, isbn, titulo, autores, categoria, sinopse, ano, editora, estoque, status
- Validações:
  * ISBN não pode ser vazio e deve seguir formato válido
  * Título deve ter pelo menos 1 caractere
  * Estoque não pode ser negativo
  * Status deve ser 'disponivel', 'emprestado' ou 'manutencao'
  * Categoria deve ser válida

Exemplos de testes a implementar:
- test_criar_livro_valido()
- test_criar_livro_isbn_invalido()
- test_criar_livro_estoque_negativo()
- test_alterar_status_livro()
- test_validar_disponibilidade()
"""

import re

class Livro:
    STATUS_VALIDOS = ['disponivel', 'emprestado', 'manutencao']
    CATEGORIAS_VALIDAS = [
        'Romance', 'Ficção', 'Drama', 'Terror', 'História', 'Biografia',
        'Ciência', 'Tecnologia', 'Educação', 'Filosofia', 'Outro'
    ]

    def __init__(self, id, isbn, titulo, autores, categoria, sinopse, ano, editora, estoque, status='disponivel'):
        self.id = id
        self.isbn = isbn
        self.titulo = titulo
        self.autores = autores if isinstance(autores, list) else [autores]
        self.categoria = categoria
        self.sinopse = sinopse
        self.ano = ano
        self.editora = editora
        self.estoque = estoque
        self.status = status

        self.validar_campos()

    def validar_campos(self):
        if not self.isbn or not self.validar_isbn(self.isbn):
            raise ValueError("ISBN inválido ou vazio.")
        if not self.titulo or len(self.titulo.strip()) < 1:
            raise ValueError("O título deve ter pelo menos 1 caractere.")
        if self.estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")
        if self.status not in self.STATUS_VALIDOS:
            raise ValueError(f"Status inválido. Use um dos seguintes: {', '.join(self.STATUS_VALIDOS)}")
        if self.categoria not in self.CATEGORIAS_VALIDAS:
            raise ValueError(f"Categoria inválida. Categorias aceitas: {', '.join(self.CATEGORIAS_VALIDAS)}")

    def validar_isbn(self, isbn):
        """Valida ISBN-10 ou ISBN-13 (somente formato básico numérico)."""
        isbn_limpo = re.sub(r'[^0-9Xx]', '', isbn)
        return len(isbn_limpo) in (10, 13)

    def verificar_disponibilidade(self):
        """Retorna True se o livro estiver disponível para empréstimo."""
        return self.status == 'disponivel' and self.estoque > 0

    def emprestar(self):
        """Reduz estoque e muda status para 'emprestado'."""
        if not self.verificar_disponibilidade():
            raise ValueError("Livro não disponível para empréstimo.")
        self.estoque -= 1
        if self.estoque == 0:
            self.status = 'emprestado'

    def devolver(self):
        """Aumenta estoque e muda status para 'disponível'."""
        self.estoque += 1
        self.status = 'disponivel'

    def enviar_manutencao(self):
        """Coloca o livro em manutenção."""
        self.status = 'manutencao'

    def to_dict(self):
        return {
            "id": self.id,
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autores": self.autores,
            "categoria": self.categoria,
            "sinopse": self.sinopse,
            "ano": self.ano,
            "editora": self.editora,
            "estoque": self.estoque,
            "status": self.status
        }

    def __repr__(self):
        return f"<Livro {self.id} - '{self.titulo}' ({self.status})>"
