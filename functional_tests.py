from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Ana ouviu falar de uma aplicaco online interessante
        #para lista de tarefas, ela decidiu verificar
        self.browser.get('http://localhost:8000')

        #Ela percebe que o título da página menciona "to-do"
        self.assertIn ("To-Do", self.browser.title)
        self.fail("Finish the test!")

        #Ela é convidada a inserir um item de tarefa imediatamente

        #Ela digita "Buy peacock feathers" em uma caixa de texto
        #(Seu hobby é fazer iscas para pescar)

        #Quando ela tecla enter a página é atualizada, agora a página lista
        #"1: Buy peacock feathers" como um item da lista de tarefas

        #Ainda continua havendo uma caixa de texto para acrescentar outro item.
        #ELa insere "User peacock feathers to make a fly"

        #A página é atualizada novamente e agora mostra dois itens em sua lista

        #Ana se pergunta se o site lembrará de sua lista. Ela nota que o site
        #gerou um URL único para ela - existe um texto explicativo.

        #Ela acessa essa URL - sua lista continua lá.

        #Satisfeita ela volta a dormir.

if __name__ == '__main__':
    unittest.main(warnings="ignore")
