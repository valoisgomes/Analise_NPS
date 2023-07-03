"""
Versão 3: Paradigma Orientado a Objetos (POO).

Este script adota uma abordagem Orientada a Objetos (OO) para calcular o NPS a partir de feedback de usuários.
Duas classes são definidas, onde:
- Feedback representa um único feedback de usuário;
- AnalisadorFeedback é usado para calcular o NPS a partir de uma lista de Feedbacks.
A POO fornece uma abstração mais clara dos dados e comportamentos envolvidos no cálculo do NPS.
Desta forma, nossa solução estará preparada para as evoluções do nosso projeto.
"""

import read_data as rd

class Feedback:
    def __init__(self, Pastor_A,pastor_b,pastor_c,pastor_d,evento_casais,culto_jovens,vigilia,gps,cantina,acolhimento,equipe_pastoral,culto_preferido,sente_cuidado,parte_familia,satisfacao_igreja,comentario):
        self.pastor_a = Pastor_A
        self.pastor_b = pastor_b
        self.pastor_c = pastor_c
        self.pastor_d = pastor_d
        self.evento_casais = evento_casais
        self.culto_jovens = culto_jovens
        self.vigilia = vigilia
        self.gps = gps
        self.cantina = cantina
        self.acolhimento = acolhimento
        self.equipe_pastoral = equipe_pastoral
        self.culto_preferido = culto_preferido
        self.sente_cuidado = sente_cuidado
        self.parte_familia = parte_familia
        self.satisfacao_igreja = satisfacao_igreja
        self.comentario = comentario

class AnalisadorFeedback:
    def __init__(self, feedbacks):
        self.feedbacks = feedbacks

    def calcular_nps_pastor_a(self):
        # Por ser uma list do Python, aplicamos o conceito de "list comprehension" para filtrar nossos Feedbacks.
        detratores = sum(1 for feedback in self.feedbacks if feedback.pastor_a <= 6)
        promotores = sum(1 for feedback in self.feedbacks if feedback.pastor_a >= 9)

        print(f"Os detratores do Pastor A são: {detratores}")
        print(f"Od promotores do Pastor A são: {promotores}")
        return (promotores - detratores) / len(self.feedbacks) * 100
    def calcular_nps_pastor_b(self):
        # Por ser uma list do Python, aplicamos o conceito de "list comprehension" para filtrar nossos Feedbacks.
        detratores = sum(1 for feedback in self.feedbacks if feedback.pastor_b <= 6)
        promotores = sum(1 for feedback in self.feedbacks if feedback.pastor_b >= 9)

        print(f"Os detratores do Pastor B são: {detratores}")
        print(f"Od promotores do Pastor B são: {promotores}")
        return (promotores - detratores) / len(self.feedbacks) * 100
    def calcular_nps_pastor_c(self):
        # Por ser uma list do Python, aplicamos o conceito de "list comprehension" para filtrar nossos Feedbacks.
        detratores = sum(1 for feedback in self.feedbacks if feedback.pastor_c <= 6)
        promotores = sum(1 for feedback in self.feedbacks if feedback.pastor_c >= 9)

        print(f"Os detratores do Pastor C são: {detratores}")
        print(f"Od promotores do Pastor C são: {promotores}")
        return (promotores - detratores) / len(self.feedbacks) * 100
    def calcular_nps_pastor_d(self):
        # Por ser uma list do Python, aplicamos o conceito de "list comprehension" para filtrar nossos Feedbacks.
        detratores = sum(1 for feedback in self.feedbacks if feedback.pastor_d <= 6)
        promotores = sum(1 for feedback in self.feedbacks if feedback.pastor_d >= 9)

        print(f"Os detratores do Pastor D são: {detratores}")
        print(f"Od promotores do Pastor D são: {promotores}")
        return (promotores - detratores) / len(self.feedbacks) * 100

feedbacks = rd.dados.apply(lambda linha: Feedback(linha['Pastor_A'], linha['Pastor_B'], linha['Pastor_C'], linha['Pastor_D'], 
                                                  linha['Evento_Casais'], linha['Culto_Jovens'], linha['Vigilia'], linha['GPS'], 
                                                  linha['Cantina'], linha['Acolhimento'], linha['Equipe_Pastoral'], 
                                                  linha['Culto_Preferido'], linha['Sente_Cuidado'], linha['Parte_Família'], 
                                                  linha['Satisfação_Igreja'], linha['Comentário']), axis=1)
analisador = AnalisadorFeedback(feedbacks)

nps_pastor_a = analisador.calcular_nps_pastor_a()
nps_pastor_b = analisador.calcular_nps_pastor_b()
nps_pastor_c = analisador.calcular_nps_pastor_c()
nps_pastor_d = analisador.calcular_nps_pastor_d()

print(f"O NPS do Pastor A é: {nps_pastor_a}")
print(f"O NPS do Pastor B é: {nps_pastor_b}")
print(f"O NPS do Pastor C é: {nps_pastor_c}")
print(f"O NPS do Pastor D é: {nps_pastor_d}")