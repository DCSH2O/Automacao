from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # Importando a classe Service
from webdriver_manager.chrome import ChromeDriverManager  # Usando o WebDriver Manager para automatizar o download do chromedriver
import time

# Passo: Garantir que o ChromeDriver seja obtido corretamente
@given(u'Entro na Página de contato do Instituto Joga Junto')
def step_impl(context):
    # Usando o ChromeDriverManager para obter o chromedriver mais recente
    service = Service(ChromeDriverManager().install())  # Instala e configura automaticamente o chromedriver
    context.driver = webdriver.Chrome(service=service)  # Inicializa o navegador com o chromedriver
    context.driver.get('https://www.jogajuntoinstituto.org/')
    context.driver.maximize_window()  # Maximiza a janela para uma melhor visualização

    # Aceitar os termos de uso, se o botão estiver presente
    try:
        accept_button = context.driver.find_element(By.ID, "adopt-accept-all-button")
        accept_button.click()  # Aceita os termos
        print("Termos aceitos com sucesso!")
    except Exception as e:
        print("Erro ao tentar aceitar os termos:", e)

    time.sleep(2)  # Aguarda 2 segundos para garantir que a página carregue completamente

@when(u'Insiro meus dados')
def step_impl(context):
    # Rolando até a seção de contato
    contact_section = context.driver.find_element(By.ID, 'Contato')
    context.driver.execute_script("arguments[0].scrollIntoView();", contact_section)  # Rolando até a seção de contato

    time.sleep(2)  # Garantindo tempo para carregar

    # Preenchendo os campos de dados
    context.driver.find_element(By.ID, 'nome').send_keys('Felipe')
    context.driver.find_element(By.ID, 'email').send_keys('felipe.email@example.com')  # Use um e-mail válido

    # Selecionando a opção "Ser facilitador" no campo "assunto" usando a classe Select
    select_assunto = context.driver.find_element(By.ID, 'assunto')
    select_assunto.send_keys(Keys.ARROW_DOWN)  # Movendo para baixo até a opção desejada (Ser facilitador)
    select_assunto.send_keys(Keys.TAB)  # Passando para o próximo campo

    # Preenchendo o campo de mensagem
    context.driver.find_element(By.ID, 'mensagem').send_keys('Tamo junto ai - QA Avançado Ilhabela Novembro 2024')

@when(u'Envio o formulário e aguardo a mensagem de agradecimento')
def step_impl(context):
    # Enviar o formulário clicando no botão de enviar usando o novo localizador
    submit_button = context.driver.find_element(By.XPATH, "//*[@id='Contato']/div[1]/form/button")
    submit_button.click()  # Clicando no botão "Enviar"

    # Aguardando a mensagem de agradecimento (isso pode variar dependendo do comportamento da página)
    time.sleep(5)  # Espera de 5 segundos para aguardar a possível mensagem de agradecimento
    print("Mensagem enviada! Aguardando resposta...")

@then(u'Fecho o navegador')
def step_impl(context):
    # Aguardar mais alguns segundos para visualizar a resposta
    time.sleep(10)  # Espera adicional para garantir que a resposta seja visível
    print("Navegador permanece aberto para visualização. Feche manualmente após conferir.")
    context.driver.quit()  # Fechar o navegador
