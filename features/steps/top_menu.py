# pylint: disable=function-redefined
# pylint: disable=no-name-in-module
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


@given('que entrei no site do "Trivago"')
def step_impl(context):
    context.driver.get("http://www.trivago.com.br")   # Abre o site


@when('digitar {Manaus} na barra de busca')
def step_impl(context, Manaus):
    context.driver.find_element(By.XPATH, '//*[@id="querytext"]').send_keys('Manaus')    # pesquisar por Manaus


@when('clicar em "Manaus" na sugestão')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="suggestion-56507/200"]/div/span[2]').click()
    sleep(2)

@when('clicar em "Aceitar" no pop-up de cookies')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click() # aceitar os cookies

@when('clicar em "Pesquisar"')
def step_impl(context):
    context.driver.find_element(
        By.CLASS_NAME, 'search-button__label').click()

@when('selecionar a "Ordenação" da Pesquisa')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="mf-select-sortby"]').click()

@when('e escolher o tipo "Avaliações e Sugestões"')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@value="7"]').click()

@then('é apresentado o resultado das "Pesquisas"')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="js_price_disclaimer"]').click()
    sleep(5)

@given('que clico tenho meu primeiro "resultado"')
def checkexisttheelement(context): 
    try:
        context.driver.find_element(By.XPATH, '//*[@id="2381212"]/div/article/div[1]/div[2]/div/div/h3/span') ##Valida primeiro nome
    except NoSuchElementException:
        return False
    return True

@when('verifico as "Avaliações"') ##verifica avalições
def checkexisttheelement(context):
    try:
        context.driver.find_element(By.XPATH, '//*[@id="2381212"]/div/article/div[1]/div[2]/div/div/button/span[1]/span[1]/span')
    except NoSuchElementException:
        return False
    return True

@then('verifico o primeiro "Valor" do primeiro da lista') ##Verifica valor do primeiro da lista
def checkexisttheelement(context):
    try:
        context.driver.find_element(By.CLASS_NAME, 'accommodation-list__text--f27b2')
    except NoSuchElementException:
        return False
    return True

