import unittest
from Model.Usuario import Usuario

class TestUsuario(unittest.TestCase):

    def test_criar_usuario_valido(self):
        usuario = Usuario(id=1, nome="João Silva", matricula="2023001", tipo="aluno", email="joao@email.com")
        self.assertEqual(usuario.nome, "João Silva")
        self.assertEqual(usuario.tipo, "aluno")

    def test_criar_usuario_sem_matricula(self):
        with self.assertRaises(ValueError) as context:
            Usuario(id=1, nome="Maria", matricula="", tipo="professor", email="maria@email.com")
        self.assertIn("Matrícula não pode ser vazia", str(context.exception))

    def test_criar_usuario_nome_curto(self):
        with self.assertRaises(ValueError) as context:
            Usuario(id=2, nome="Lu", matricula="2023002", tipo="aluno", email="lu@email.com")
        self.assertIn("Nome deve ter pelo menos 3 caracteres", str(context.exception))

    def test_criar_usuario_tipo_invalido(self):
        with self.assertRaises(ValueError) as context:
            Usuario(id=3, nome="Pedro Santos", matricula="2023003", tipo="visitante", email="pedro@email.com")
        self.assertIn("Tipo de usuário inválido", str(context.exception))

    def test_validar_email(self):
        with self.assertRaises(ValueError) as context:
            Usuario(id=4, nome="Ana Costa", matricula="2023004", tipo="aluno", email="anaemail.com")
        self.assertIn("Email inválido", str(context.exception))


if __name__ == "__main__":
    unittest.main()
