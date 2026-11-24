# usuario.py — a classe Usuario: quem é a pessoa e o que ela pode fazer
# A senha nunca fica guardada como foi digitada: guardamos só o resumo (hash).

import hashlib
import secrets

from usuarios.papeis import PERMISSOES


class Usuario:
    # Construtor: matrícula, nome, senha e a lista de papéis
    def __init__(self, matricula, nome, senha, papeis, supervisor=None):
        self.matricula = matricula
        self.nome = nome
        self.papeis = papeis
        self.supervisor = supervisor
        self.situacao = "ativo"

        # O _ na frente avisa: atributo interno, ninguém de fora mexe
        self._sal = secrets.token_hex(8)
        self._senha_hash = self._resumir(senha)

    # Transforma a senha em um resumo que não dá para desfazer
    def _resumir(self, senha):
        texto = (self._sal + senha).encode("utf-8")
        return hashlib.sha256(texto).hexdigest()

    # True se a senha digitada bate com a guardada
    def conferir_senha(self, senha):
        return self._resumir(senha) == self._senha_hash

    # True se a pessoa tem esse papel
    def tem_papel(self, papel):
        return papel in self.papeis

    
    # Verifica se a pessoa tem permissão para realizar uma ação
    def pode(self, permissao):
        if self.situacao != "ativo":
            return False

        for papel in self.papeis:
            if permissao in PERMISSOES[papel]:
                return True

        return False

    
    # Devolve todas as permissões dos cargos, sem repetir
    def permissoes(self):
        lista = []

        for papel in self.papeis:
            for permissao in PERMISSOES[papel]:
                if permissao not in lista:
                    lista.append(permissao)

        return lista

    
    # Troca a senha se a senha atual estiver correta
    def trocar_senha(self, atual, nova):
        if self.conferir_senha(atual):
            self._senha_hash = self._resumir(nova)
            return True

        return False

    
    # Devolve os dados do usuário em um dicionário
    def para_dicionario(self):
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "papeis": self.papeis,
            "permissoes": self.permissoes(),
            "supervisor": self.supervisor,
            "situacao": self.situacao
        }