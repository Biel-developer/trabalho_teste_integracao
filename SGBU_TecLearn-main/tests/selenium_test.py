from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
base_url = "http://localhost:8000"


def teste_redirect_inicial():
    driver.get(base_url + "/")
    time.sleep(1)
    assert "/cadastro" in driver.current_url
    print("✓ Redirect inicial funcionou")


def teste_navegacao_menu():
    driver.get(base_url + "/cadastro")
    driver.find_element(By.XPATH, "//a[@href='/livros']").click()
    time.sleep(1)
    assert "/livros" in driver.current_url

    driver.find_element(By.XPATH, "//a[@href='/emprestimos']").click()
    time.sleep(1)
    assert "/emprestimos" in driver.current_url

    driver.find_element(By.XPATH, "//a[@href='/relatorios']").click()
    time.sleep(1)
    assert "/relatorios" in driver.current_url

    driver.find_element(By.XPATH, "//a[@href='/cadastro']").click()
    time.sleep(1)
    assert "/cadastro" in driver.current_url
    print("✓ Navegacao menu funcionou")


def teste_cadastro_usuario_aluno():
    driver.get(base_url + "/cadastro/novo")
    time.sleep(1)

    driver.find_element(By.NAME, "matricula").send_keys("2024001")
    driver.find_element(By.NAME, "nome").send_keys("Alexandre Silva")
    Select(driver.find_element(By.NAME, "tipo")).select_by_value("aluno")
    driver.find_element(By.NAME, "email").send_keys("alexandre@teste.com")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    assert "Dados recebidos com sucesso" in driver.page_source
    assert "2024001" in driver.page_source
    assert "Alexandre Silva" in driver.page_source
    print("✓ Cadastro usuario aluno funcionou")


def teste_cadastro_usuario_professor():
    driver.get(base_url + "/cadastro/novo")
    time.sleep(1)

    driver.find_element(By.NAME, "matricula").send_keys("PROF001")
    driver.find_element(By.NAME, "nome").send_keys("Prof. Dacio")
    Select(driver.find_element(By.NAME, "tipo")).select_by_value("professor")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    assert "Dados recebidos com sucesso" in driver.page_source
    assert "PROF001" in driver.page_source
    print("✓ Cadastro usuario professor funcionou")


def teste_cadastro_usuario_funcionario():
    driver.get(base_url + "/cadastro/novo")
    time.sleep(1)

    driver.find_element(By.NAME, "matricula").send_keys("FUNC001")
    driver.find_element(By.NAME, "nome").send_keys("Maria Bibliotecaria")
    Select(driver.find_element(By.NAME, "tipo")).select_by_value("funcionario")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    assert "Dados recebidos com sucesso" in driver.page_source
    assert "FUNC001" in driver.page_source
    print("✓ Cadastro usuario funcionario funcionou")


def teste_botao_cancelar_usuario():
    driver.get(base_url + "/cadastro/novo")
    time.sleep(1)

    driver.find_element(By.XPATH, "//a[@href='/cadastro']").click()
    time.sleep(1)

    assert "/cadastro" in driver.current_url
    assert "Lista de Usuarios" in driver.page_source
    print("✓ Botao cancelar usuario funcionou")


def teste_cadastro_livro_ficcao():
    driver.get(base_url + "/livros/novo")
    time.sleep(1)

    driver.find_element(By.NAME, "isbn").send_keys("978-3-16-148410-0")
    driver.find_element(By.NAME, "titulo").send_keys("1984")
    Select(driver.find_element(By.NAME, "categoria")).select_by_value("ficcao")
    driver.find_element(By.NAME, "estoque").send_keys("5")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    assert "Dados recebidos com sucesso" in driver.page_source
    assert "978-3-16-148410-0" in driver.page_source
    assert "1984" in driver.page_source
    print("✓ Cadastro livro ficcao funcionou")


def teste_cadastro_livro_tecnico():
    driver.get(base_url + "/livros/novo")
    time.sleep(1)

    driver.find_element(By.NAME, "isbn").send_keys("978-0-13-468599-1")
    driver.find_element(By.NAME, "titulo").send_keys("Clean Code")
    Select(driver.find_element(By.NAME, "categoria")).select_by_value("tecnico")
    driver.find_element(By.NAME, "estoque").send_keys("10")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    assert "Dados recebidos com sucesso" in driver.page_source
    assert "Clean Code" in driver.page_source
    print("✓ Cadastro livro tecnico funcionou")


def teste_cadastro_livro_didatico():
    driver.get(base_url + "/livros/novo")
    time.sleep(1)

    driver.find_element(By.NAME, "isbn").send_keys("978-8-57-122850-5")
    driver.find_element(By.NAME, "titulo").send_keys("Engenharia de Software")
    Select(driver.find_element(By.NAME, "categoria")).select_by_value("didatico")
    driver.find_element(By.NAME, "estoque").send_keys("15")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    assert "Dados recebidos com sucesso" in driver.page_source
    assert "Engenharia de Software" in driver.page_source
    print("✓ Cadastro livro didatico funcionou")


def teste_navegacao_tabs_livros():
    driver.get(base_url + "/livros")
    time.sleep(1)

    assert "Catalogo de Livros" in driver.page_source

    driver.find_element(By.XPATH, "//a[@href='/autores']").click()
    time.sleep(1)

    assert "/autores" in driver.current_url
    assert "Catalogo de Autores" in driver.page_source
    print("✓ Navegacao tabs livros funcionou")


def teste_botao_cancelar_livro():
    driver.get(base_url + "/livros/novo")
    time.sleep(1)

    driver.find_element(By.XPATH, "//a[@href='/livros']").click()
    time.sleep(1)

    assert "/livros" in driver.current_url
    print("✓ Botao cancelar livro funcionou")


def teste_cadastro_emprestimo():
    driver.get(base_url + "/emprestimos/novo")
    time.sleep(1)

    driver.find_element(By.NAME, "usuario_id").send_keys("1")
    driver.find_element(By.NAME, "livro_id").send_keys("1")
    driver.find_element(By.NAME, "data_emprestimo").send_keys("14/11/2025")
    driver.find_element(By.NAME, "prazo_devolucao").send_keys("21/11/2025")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    assert "Dados recebidos com sucesso" in driver.page_source
    print("✓ Cadastro emprestimo funcionou")


def teste_estatisticas_emprestimos():
    driver.get(base_url + "/emprestimos")
    time.sleep(1)

    assert "Emprestimos Ativos" in driver.page_source
    assert "Emprestimos em Atraso" in driver.page_source
    assert "Devolvidos Hoje" in driver.page_source
    print("✓ Estatisticas emprestimos funcionou")


def teste_botao_cancelar_emprestimo():
    driver.get(base_url + "/emprestimos/novo")
    time.sleep(1)

    driver.find_element(By.XPATH, "//a[@href='/emprestimos']").click()
    time.sleep(1)

    assert "/emprestimos" in driver.current_url
    print("✓ Botao cancelar emprestimo funcionou")


def teste_pagina_relatorios():
    driver.get(base_url + "/relatorios")
    time.sleep(1)

    assert "Visao Geral" in driver.page_source
    assert "Livros Mais Emprestados" in driver.page_source
    assert "Usuarios Mais Ativos" in driver.page_source
    assert "Taxa de Ocupacao" in driver.page_source
    print("✓ Pagina relatorios funcionou")


def teste_usuario_sem_email():
    driver.get(base_url + "/cadastro/novo")
    time.sleep(1)

    driver.find_element(By.NAME, "matricula").send_keys("2024999")
    driver.find_element(By.NAME, "nome").send_keys("Usuario Sem Email")
    Select(driver.find_element(By.NAME, "tipo")).select_by_value("aluno")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    assert "Dados recebidos com sucesso" in driver.page_source
    assert "Nao informado" in driver.page_source
    print("✓ Usuario sem email funcionou")


def teste_livro_estoque_zero():
    driver.get(base_url + "/livros/novo")
    time.sleep(1)

    driver.find_element(By.NAME, "isbn").send_keys("978-0-00-000000-0")
    driver.find_element(By.NAME, "titulo").send_keys("Livro Estoque Zero")
    Select(driver.find_element(By.NAME, "categoria")).select_by_value("cientifico")
    driver.find_element(By.NAME, "estoque").send_keys("0")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    assert "Dados recebidos com sucesso" in driver.page_source
    print("✓ Livro estoque zero funcionou")


def executar_testes():
    print("\n=== INICIANDO TESTES SELENIUM SGBU ===\n")

    try:
        teste_redirect_inicial()
        teste_navegacao_menu()
        teste_cadastro_usuario_aluno()
        teste_cadastro_usuario_professor()
        teste_cadastro_usuario_funcionario()
        teste_botao_cancelar_usuario()
        teste_cadastro_livro_ficcao()
        teste_cadastro_livro_tecnico()
        teste_cadastro_livro_didatico()
        teste_navegacao_tabs_livros()
        teste_botao_cancelar_livro()
        teste_cadastro_emprestimo()
        teste_estatisticas_emprestimos()
        teste_botao_cancelar_emprestimo()
        teste_pagina_relatorios()
        teste_usuario_sem_email()
        teste_livro_estoque_zero()

        print("\n=== TODOS OS TESTES PASSARAM ===\n")

    except AssertionError as e:
        print(f"\n✗ TESTE FALHOU: {e}\n")

    except Exception as e:
        print(f"\n✗ ERRO: {e}\n")

    finally:
        driver.quit()


if __name__ == "__main__":
    executar_testes()
