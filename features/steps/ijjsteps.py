from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

@given(u'Entro na Página de contato do Instituto Joga Junto')
def step_impl(context):
    # Inicializa o navegador e abre a página
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.get('https://www.jogajuntoinstituto.org/')
    
    # Espera pela presença do campo 'nome' na página
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, 'nome')))

@when(u'Insiro meus dados')
def step_impl(context):
    # Preenche os campos de dados
    context.driver.find_element(By.ID, 'nome').send_keys('Diony')
    context.driver.find_element(By.ID, 'email').send_keys('dionycosta@gmail.com')
    
    # Seleciona a opção "Ser facilitador"
    select_assunto = Select(context.driver.find_element(By.XPATH, '//*[@id="assunto"]'))
    select_assunto.select_by_visible_text('Ser facilitador')

@when(u'Envio a mensagem "Olá da turma de QA Avançado, Ilhabela Novembro 2024"')
def step_impl(context):
    # Preenche a mensagem
    context.driver.find_element(By.ID, 'mensagem').send_keys('Teste de Automação')
    
    # Espera o botão de enviar ser visível e clicável
    botao_enviar = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Contato"]/div[1]/form/button'))
    )
    
    # Usar JavaScript para clicar no botão (garante que o clique seja executado mesmo se houver bloqueios visuais)
    context.driver.execute_script("arguments[0].click();", botao_enviar)

@then(u'Fecho o navegador')
def step_impl(context):
    # Aguardar um tempo para visualizar os resultados antes de fechar o navegador
    time.sleep(5)
    context.driver.quit()
