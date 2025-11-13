import unittest
from Model.Autor import Autor

class TestAutor(unittest.TestCase):

    def test_criar_autor_valido(self):
        autor = Autor(id=1, nome="Machado de Assis", nacionalidade="Brasileiro", biografia="Grande escritor brasileiro.")
        self.assertEqual(autor.nome, "Machado de Assis")
        self.assertEqual(autor.nacionalidade, "Brasileiro")
        self.assertEqual(autor.biografia, "Grande escritor brasileiro.")

    def test_criar_autor_sem_nome(self):
        with self.assertRaises(ValueError) as contexto:
            Autor(id=1, nome="", nacionalidade="Brasileiro", biografia="")
        self.assertEqual(str(contexto.exception), "Nome não pode ser vazio")

    def test_criar_autor_nome_curto(self):
        with self.assertRaises(ValueError) as contexto:
            Autor(id=1, nome="Jo", nacionalidade="Brasileiro", biografia="")
        self.assertEqual(str(contexto.exception), "Nome deve ter pelo menos 3 caracteres")

    def test_atualizar_biografia(self):
        autor = Autor(id=1, nome="Clarice Lispector", nacionalidade="Brasileira", biografia="Escritora")
        autor.atualizar_biografia("Autora de obras importantes da literatura brasileira.")
        self.assertEqual(autor.biografia, "Autora de obras importantes da literatura brasileira.")

if __name__ == "__main__":
    unittest.main()
