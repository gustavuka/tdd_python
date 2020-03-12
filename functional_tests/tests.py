from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import unittest


MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id("id_list_table")
                rows = table.find_elements_by_tag_name("tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Ana ouviu falar de uma aplicaco online interessante
        # para lista de tarefas, ela decidiu verificar
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table("1: Buy peacock feathers" )

        # Ainda continua havendo uma caixa de texto para acrescentar outro item.
        # ELa insere "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        # A página é atualizada novamente e agora mostra dois itens em sua lista
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")

        # Satisfeita ela volta a dormir.

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Ana inicia uma nova lista de tarefas
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # Ela percebe que sua lista tem um URL único.
        ana_list_url = self.browser.current_url
        self.assertRegex(ana_list_url, "/lists/.+")

        # Agora um novo usuário, Francis, chega ao site.
        ## Nova sessão de navegador, bc cookies
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis acessa a página inicial, não há nenhum sinal de Ana
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertNotIn("make a fly", page_text)

        # Francis inicia uma lista inserindo um item novo
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # Francis obtém seu prórpio URL exclusivo
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, "/lists/.+")
        self.assertNotEqual(francis_list_url, ana_list_url)

        # Novamente nao há sinal da lista de Ana
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertIn("Buy milk", page_text)

        # Satisfeitos ambos voltam a dormir
