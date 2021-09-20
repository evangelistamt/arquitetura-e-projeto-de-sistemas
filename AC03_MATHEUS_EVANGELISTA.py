from unittest import TestCase, main
import abc

class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if operacao == None:
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

class OperacaoFabrica(object):

    def criar(self, operador):
        if operador == 'soma':
            return Soma()

        elif operador == 'subtracao':
            return Subtracao()

        elif operador == 'multiplicacao':
            return Multiplicacao()

        elif operador == 'divisao':
            return Divisao()
        

class Operacao(metaclass=abc.ABCMeta):

    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2




class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado


class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado


class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado



class Testes(TestCase):


    def test_soma(self):
        somando = Calculadora()
        self.assertEqual(somando.calcular(7, 7, 'soma'), 14)

    def test_subtracao(self):
        calcular = Calculadora()
        self.assertEqual(calcular.calcular(8, 4, 'subtracao'), 4)


    def test_multiplicacao(self):
        calcular = Calculadora()
        self.assertEqual(calcular.calcular(6, 6, 'multiplicacao'), 36)
    
        

    def test_divisao(self):
        dividindo = Calculadora()
        self.assertEqual(dividindo.calcular(15, 3, 'divisao'), 5)


        

duvida = Calculadora()
x = duvida.calcular(5, 5, 'soma')


if __name__ == '__main__':
    main()