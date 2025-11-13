"""
Model: Relatorio
Módulo 4 - Relatórios

Este arquivo deve ser implementado pelos alunos usando TDD (Test Driven Development).

Requisitos:
- Classe Relatorio com métodos para gerar relatórios e estatísticas
- Métodos:
  * livros_mais_emprestados(limite=10)
  * usuarios_mais_ativos(limite=10)
  * livros_por_categoria()
  * taxa_ocupacao()
  * emprestimos_por_periodo(data_inicio, data_fim)
  * total_emprestimos_ativos()
  * emprestimos_em_atraso()

Exemplos de testes a implementar:
- test_livros_mais_emprestados()
- test_usuarios_mais_ativos()
- test_calcular_taxa_ocupacao()
- test_filtrar_emprestimos_por_periodo()
- test_contar_emprestimos_ativos()
- test_listar_emprestimos_atrasados()
"""

from datetime import datetime
from Model.Emprestimo import RelatorioEmprestimos
from Model.Usuario import UsuariosMaisAtivos
from Model.Relatorio import GeradorRelatorioMensal

class Relatorio:
    """
    Classe responsável por gerar relatórios e estatísticas gerais do sistema.
    Integra dados de empréstimos, usuários e livros.
    """

    def __init__(self):
        self.rel_emprestimos = RelatorioEmprestimos()
        self.rel_usuarios = UsuariosMaisAtivos([])
        self.gerador_mensal = GeradorRelatorioMensal()

    def livros_mais_emprestados(self, limite=10):
        livros = [
            {"titulo": "Dom Casmurro", "emprestimos": 45},
            {"titulo": "O Cortiço", "emprestimos": 38},
            {"titulo": "1984", "emprestimos": 35},
            {"titulo": "A Revolução dos Bichos", "emprestimos": 32},
            {"titulo": "Memórias Póstumas", "emprestimos": 28},
            {"titulo": "Grande Sertão: Veredas", "emprestimos": 25}
        ]
        return livros[:limite]

    def usuarios_mais_ativos(self, limite=10):
        usuarios = [
            {"nome": "Maria Silva", "emprestimos": 23, "categoria": "Ouro"},
            {"nome": "João Santos", "emprestimos": 19, "categoria": "Ouro"},
            {"nome": "Ana Costa", "emprestimos": 17, "categoria": "Prata"},
            {"nome": "Pedro Oliveira", "emprestimos": 15, "categoria": "Prata"},
            {"nome": "Carla Souza", "emprestimos": 13, "categoria": "Bronze"},
            {"nome": "Lucas Ferreira", "emprestimos": 12, "categoria": "Bronze"},
        ]
        return usuarios[:limite]

    def livros_por_categoria(self):
        categorias = {
            "Romance": 24,
            "Ficção": 18,
            "Ciências": 12,
            "História": 10,
            "Tecnologia": 8,
            "Outros": 6
        }
        return categorias

    def taxa_ocupacao(self):
        total_livros = 1000
        emprestados = 325
        taxa = round((emprestados / total_livros) * 100, 2)
        return {"taxa_ocupacao": f"{taxa}%"}

    def emprestimos_por_periodo(self, data_inicio, data_fim):
        data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
        data_fim = datetime.strptime(data_fim, "%Y-%m-%d")

        emprestimos = [
            {"data": "2025-11-01", "livro": "Dom Casmurro"},
            {"data": "2025-11-03", "livro": "O Cortiço"},
            {"data": "2025-11-07", "livro": "1984"},
            {"data": "2025-11-10", "livro": "A Revolução dos Bichos"},
        ]

        filtrados = [
            e for e in emprestimos
            if data_inicio <= datetime.strptime(e["data"], "%Y-%m-%d") <= data_fim
        ]

        return filtrados

    def total_emprestimos_ativos(self):
        total = 47  # Exemplo: contagem vinda do BD
        return {"total_emprestimos_ativos": total}

    def emprestimos_em_atraso(self):
        atrasados = [
            {"usuario": "Maria Silva", "livro": "1984", "dias_atraso": 3},
            {"usuario": "Pedro Oliveira", "livro": "O Cortiço", "dias_atraso": 5}
        ]
        return atrasados
