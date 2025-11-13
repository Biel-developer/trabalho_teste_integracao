"""
Model: Emprestimo
Módulo 3 - Empréstimo e Devolução

Este arquivo deve ser implementado pelos alunos usando TDD (Test Driven Development).

Requisitos:
- Classe Emprestimo com atributos: id, usuario_id, livro_id, data_emprestimo, prazo_devolucao, data_devolucao, status
- Validações:
  * usuario_id deve existir
  * livro_id deve existir e estar disponível
  * data_emprestimo não pode ser futura
  * prazo_devolucao deve ser posterior à data_emprestimo
  * status deve ser 'ativo', 'devolvido' ou 'atrasado'
- Métodos:
  * verificar_disponibilidade_livro()
  * calcular_dias_atraso()
  * registrar_devolucao()
  * verificar_atraso()

Exemplos de testes a implementar:
- test_criar_emprestimo_valido()
- test_emprestar_livro_indisponivel()
- test_calcular_dias_atraso()
- test_registrar_devolucao()
- test_verificar_atraso()
- test_prazo_devolucao_invalido()
"""

from datetime import date, timedelta

class Emprestimo:
    STATUS_VALIDOS = ['ativo', 'devolvido', 'atrasado']

    def __init__(self, id, usuario_id, livro_id, data_emprestimo, prazo_devolucao, data_devolucao=None, status='ativo'):
        self.id = id
        self.usuario_id = usuario_id
        self.livro_id = livro_id
        self.data_emprestimo = data_emprestimo
        self.prazo_devolucao = prazo_devolucao
        self.data_devolucao = data_devolucao
        self.status = status

        self.validar_campos()

    def validar_campos(self):
        if not self.usuario_id:
            raise ValueError("O usuário deve existir.")
        if not self.livro_id:
            raise ValueError("O livro deve existir e estar disponível.")
        if self.data_emprestimo > date.today():
            raise ValueError("A data de empréstimo não pode ser futura.")
        if self.prazo_devolucao <= self.data_emprestimo:
            raise ValueError("O prazo de devolução deve ser posterior à data de empréstimo.")
        if self.status not in self.STATUS_VALIDOS:
            raise ValueError(f"Status inválido. Use um dos seguintes: {', '.join(self.STATUS_VALIDOS)}")

    def verificar_disponibilidade_livro(self, livros_disponiveis):
        """Verifica se o livro está disponível na lista informada."""
        return self.livro_id in livros_disponiveis

    def calcular_dias_atraso(self):
        """Calcula quantos dias de atraso o empréstimo possui."""
        if self.data_devolucao and self.data_devolucao > self.prazo_devolucao:
            return (self.data_devolucao - self.prazo_devolucao).days
        elif not self.data_devolucao and date.today() > self.prazo_devolucao:
            return (date.today() - self.prazo_devolucao).days
        return 0

    def verificar_atraso(self):
        """Atualiza o status para 'atrasado' se houver atraso."""
        if self.calcular_dias_atraso() > 0:
            self.status = 'atrasado'
        return self.status

    def registrar_devolucao(self, data_devolucao=None):
        """Registra a devolução e atualiza o status."""
        self.data_devolucao = data_devolucao or date.today()
        self.status = 'devolvido' if self.calcular_dias_atraso() == 0 else 'atrasado'


    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "livro_id": self.livro_id,
            "data_emprestimo": str(self.data_emprestimo),
            "prazo_devolucao": str(self.prazo_devolucao),
            "data_devolucao": str(self.data_devolucao) if self.data_devolucao else None,
            "status": self.status
        }

    def __repr__(self):
        return f"<Emprestimo {self.id} - Usuario {self.usuario_id}, Livro {self.livro_id}, Status: {self.status}>"
