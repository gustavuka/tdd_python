from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        #Ela é convidada a inserir um item de tarefa imediatamente
        input_box = self.browser.find_elements_by_id("id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        #Ela digita "Buy peacock feathers" em uma caixa de texto
        #(Seu hobby é fazer iscas para pescar)
        input_box.send_keys("Buy peacock feathers")

        #Quando ela tecla enter a página é atualizada, agora a página lista
        #"1: Buy peacock feathers" como um item da lista de tarefas
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_elements_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(any(row.text == "1: Buy peacock feathers"  for row in rows))

        #Ainda continua havendo uma caixa de texto para acrescentar outro item.
        #ELa insere "User peacock feathers to make a fly"
        self.fail("Finish the test!!")

        #A página é atualizada novamente e agora mostra dois itens em sua lista

        #Ana se pergunta se o site lembrará de sua lista. Ela nota que o site
        #gerou um URL único para ela - existe um texto explicativo.

        #Ela acessa essa URL - sua lista continua lá.

        #Satisfeita ela volta a dormir.

if __name__ == '__main__':
    unittest.main(warnings="ignore")
