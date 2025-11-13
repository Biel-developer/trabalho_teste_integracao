import unittest
from datetime import date, timedelta
from Model.Relatorio import Relatorio


class TestRelatorio(unittest.TestCase):

    def setUp(self):
        self.relatorios = Relatorio()

        # Dados simulados de empréstimos e usuários
        self.relatorios.emprestimos = [
            {"livro": "Dom Casmurro", "usuario": "João", "data": date(2025, 1, 10), "status": "devolvido"},
            {"livro": "O Cortiço", "usuario": "Maria", "data": date(2025, 1, 12), "status": "atrasado"},
            {"livro": "1984", "usuario": "João", "data": date(2025, 1, 13), "status": "ativo"},
            {"livro": "A Revolução dos Bichos", "usuario": "Ana", "data": date(2025, 2, 1), "status": "ativo"},
            {"livro": "Dom Casmurro", "usuario": "Lucas", "data": date(2025, 2, 10), "status": "devolvido"}
        ]

        self.relatorios.total_livros = 10  # total de livros cadastrados
        self.relatorios.total_emprestados = 4

    def test_livros_mais_emprestados(self):
        resultado = self.relatorios.livros_mais_emprestados(limite=2)
        self.assertIsInstance(resultado, list)
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0]["livro"], "Dom Casmurro")

    def test_usuarios_mais_ativos(self):
        resultado = self.relatorios.usuarios_mais_ativos(limite=2)
        self.assertEqual(resultado[0]["usuario"], "João")
        self.assertTrue(resultado[0]["emprestimos"] >= resultado[1]["emprestimos"])

    def test_calcular_taxa_ocupacao(self):
        taxa = self.relatorios.taxa_ocupacao()
        self.assertGreaterEqual(taxa, 0)
        self.assertLessEqual(taxa, 1)
        self.assertAlmostEqual(taxa, 0.4, places=1)  # 4 de 10 livros emprestados

    def test_filtrar_emprestimos_por_periodo(self):
        data_inicio = date(2025, 1, 10)
        data_fim = date(2025, 1, 31)
        resultado = self.relatorios.emprestimos_por_periodo(data_inicio, data_fim)
        self.assertTrue(all(data_inicio <= e["data"] <= data_fim for e in resultado))
        self.assertGreaterEqual(len(resultado), 1)

    def test_contar_emprestimos_ativos(self):
        total_ativos = self.relatorios.total_emprestimos_ativos()
        self.assertEqual(total_ativos, 2)

    def test_listar_emprestimos_atrasados(self):
        atrasados = self.relatorios.emprestimos_em_atraso()
        self.assertTrue(all(e["status"] == "atrasado" for e in atrasados))
        self.assertGreaterEqual(len(atrasados), 1)


if __name__ == '__main__':
    unittest.main()
