"""
Model: Usuario
Módulo 1 - Cadastro de Usuários

Este arquivo deve ser implementado pelos alunos usando TDD (Test Driven Development).

Requisitos:
- Classe Usuario com atributos: id, matricula, nome, tipo, email
- Validações:
  * Matrícula não pode ser vazia
  * Nome deve ter pelo menos 3 caracteres
  * Tipo deve ser 'aluno', 'professor' ou 'funcionario'
  * Email deve ser válido (opcional)

Exemplos de testes a implementar:
- test_criar_usuario_valido()
- test_criar_usuario_sem_matricula()
- test_criar_usuario_nome_curto()
- test_criar_usuario_tipo_invalido()
- test_validar_email()
"""

import re

class Usuario:
    TIPOS_VALIDOS = ['aluno', 'professor', 'funcionario']

    def __init__(self, id, matricula, nome, tipo, email=None):
        self.id = id
        self.matricula = matricula
        self.nome = nome
        self.tipo = tipo
        self.email = email

        self.validar_campos()

    def validar_campos(self):
        if not self.matricula or not self.matricula.strip():
            raise ValueError("A matrícula não pode ser vazia.")
        
        if not self.nome or len(self.nome.strip()) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")
        
        if self.tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido. Use um dos seguintes: {', '.join(self.TIPOS_VALIDOS)}")
        
        if self.email and not self.validar_email(self.email):
            raise ValueError("Email inválido.")

    def validar_email(self, email):
        """Valida o formato básico de email (ex: nome@dominio.com)."""
        padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(padrao_email, email) is not None

    def to_dict(self):
        return {
            "id": self.id,
            "matricula": self.matricula,
            "nome": self.nome,
            "tipo": self.tipo,
            "email": self.email
        }

    def __repr__(self):
        return f"<Usuario {self.id} - {self.nome} ({self.tipo})>"
