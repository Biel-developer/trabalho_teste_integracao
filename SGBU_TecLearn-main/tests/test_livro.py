import unittest
from Model.Livro import Livro


class TestLivro(unittest.TestCase):

    def test_criar_livro_valido(self):
        livro = Livro(
            id=1,
            isbn="978-85-359-0277-5",
            titulo="Dom Casmurro",
            autores=["Machado de Assis"],
            categoria="Romance",
            sinopse="Um clássico da literatura brasileira.",
            ano=1899,
            editora="Editora Nacional",
            estoque=5,
            status="disponivel"
        )
        self.assertEqual(livro.titulo, "Dom Casmurro")
        self.assertEqual(livro.status, "disponivel")
        self.assertEqual(livro.estoque, 5)

    def test_criar_livro_isbn_invalido(self):
        with self.assertRaises(ValueError) as contexto:
            Livro(
                id=1,
                isbn="1234",
                titulo="Dom Casmurro",
                autores=["Machado de Assis"],
                categoria="Romance",
                sinopse="Um clássico.",
                ano=1899,
                editora="Editora Nacional",
                estoque=5,
                status="disponivel"
            )
        self.assertIn("ISBN inválido", str(contexto.exception))

    def test_criar_livro_estoque_negativo(self):
        with self.assertRaises(ValueError) as contexto:
            Livro(
                id=2,
                isbn="978-85-359-0277-5",
                titulo="Memórias Póstumas de Brás Cubas",
                autores=["Machado de Assis"],
                categoria="Romance",
                sinopse="Obra importante.",
                ano=1881,
                editora="Editora Nacional",
                estoque=-3,
                status="disponivel"
            )
        self.assertIn("Estoque não pode ser negativo", str(contexto.exception))

    def test_alterar_status_livro(self):
        livro = Livro(
            id=3,
            isbn="978-85-359-0277-5",
            titulo="Capitu",
            autores=["Machado de Assis"],
            categoria="Romance",
            sinopse="Outra história.",
            ano=1899,
            editora="Editora Nacional",
            estoque=3,
            status="disponivel"
        )
        livro.alterar_status("emprestado")
        self.assertEqual(livro.status, "emprestado")

    def test_validar_disponibilidade(self):
        livro = Livro(
            id=4,
            isbn="978-85-359-0277-5",
            titulo="Quincas Borba",
            autores=["Machado de Assis"],
            categoria="Romance",
            sinopse="Um clássico.",
            ano=1891,
            editora="Editora Nacional",
            estoque=0,
            status="disponivel"
        )
        self.assertFalse(livro.validar_disponibilidade())
        livro.estoque = 2
        self.assertTrue(livro.validar_disponibilidade())


if __name__ == '__main__':
    unittest.main()
