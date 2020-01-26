from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Ana ouviu falar de uma aplicaco online interessante
        # para lista de tarefas, ela decidiu verificar
        self.browser.get("http://localhost:8000")

        # Ela percebe que o título da página menciona "to-do"
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        # Ela é convidada a inserir um item de tarefa imediatamente
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # Ela digita "Buy peacock feathers" em uma caixa de texto
        # (Seu hobby é fazer iscas para pescar)
        inputbox.send_keys("Buy peacock feathers")

        # Quando ela tecla enter a página é atualizada, agora a página lista
        # "1: Buy peacock feathers" como um item da lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # Ainda continua havendo uma caixa de texto para acrescentar outro item.
        # ELa insere "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # A página é atualizada novamente e agora mostra dois itens em sua lista
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")

        # Ana se pergunta se o site lembrará de sua lista. Ela nota que o site
        # gerou um URL único para ela - existe um texto explicativo.
        self.fail("Finish the test!")

        # Ela acessa essa URL - sua lista continua lá.

        # Satisfeita ela volta a dormir.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
