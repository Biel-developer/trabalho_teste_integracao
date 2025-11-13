import unittest
from datetime import date, timedelta
from Model.Emprestimo import Emprestimo
from Model.Livro import Livro
from Model.Usuario import Usuario


class TestEmprestimo(unittest.TestCase):

    def setUp(self):
        self.livro = Livro(id=1, titulo="Dom Casmurro", autor="Machado de Assis", disponivel=True)
        self.usuario = Usuario("2021001", "João Silva", "aluno")

    def test_criar_emprestimo_valido(self):
        emprestimo = Emprestimo(self.livro, self.usuario, date.today(), date.today() + timedelta(days=7))
        self.assertEqual(emprestimo.livro, self.livro)
        self.assertEqual(emprestimo.usuario, self.usuario)
        self.assertIsNone(emprestimo.data_devolucao)

    def test_emprestar_livro_indisponivel(self):
        self.livro.disponivel = False
        with self.assertRaises(ValueError) as contexto:
            Emprestimo(self.livro, self.usuario, date.today(), date.today() + timedelta(days=7))
        self.assertIn("Livro indisponível", str(contexto.exception))

    def test_calcular_dias_atraso(self):
        emprestimo = Emprestimo(
            self.livro,
            self.usuario,
            date.today() - timedelta(days=10),
            date.today() - timedelta(days=5)
        )
        self.assertEqual(emprestimo.calcular_dias_atraso(), 5)

    def test_registrar_devolucao(self):
        emprestimo = Emprestimo(
            self.livro,
            self.usuario,
            date.today(),
            date.today() + timedelta(days=7)
        )
        emprestimo.registrar_devolucao(date.today())
        self.assertEqual(emprestimo.data_devolucao, date.today())
        self.assertTrue(self.livro.disponivel)

    def test_verificar_atraso(self):
        emprestimo = Emprestimo(
            self.livro,
            self.usuario,
            date.today() - timedelta(days=10),
            date.today() - timedelta(days=5)
        )
        self.assertTrue(emprestimo.verificar_atraso())

    def test_prazo_devolucao_invalido(self):
        with self.assertRaises(ValueError) as contexto:
            Emprestimo(self.livro, self.usuario, date.today(), date.today() - timedelta(days=1))
        self.assertIn("Data de devolução inválida", str(contexto.exception))

if __name__ == '__main__':
    unittest.main()
