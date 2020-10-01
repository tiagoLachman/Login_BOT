import platform
import os
import time

def ler_txt(caminho):
    dados = open(caminho, 'r')
    nome = ''
    senha = ''
    links = []
    linhas = dados.readlines()
    #print(linhas)
    for linha in linhas:
        if linha.find('nome BOT LOGIN') != -1:
            nome = linha.strip('nome BOT LOGIN:').rstrip()
    for linha in linhas:
        if linha.find('senha BOT LOGIN') != -1:
            senha = linha.strip('senha BOT LOGIN')
            senha = senha.strip(':').rstrip()
    for linha in linhas:
        if linha.find('links BOT LOGIN') != -1:
            aux = ''
            for letra in linha.strip('links BOT LOGIN:'):
                if letra == ',':
                    links.append(aux)
                    aux = ''
                aux = aux + letra
            for x in range(len(links)):
                links[x] = links[x].strip(',').strip('[').strip(']').strip(' ')
                if links[x].find('http://') == -1 or links[x].find('https://') == -1:
                    raise ValueError('links do \'nome_senha.txt\' inadequados , sem \'http\', etc...')
        if nome == '' or senha == '' or links == '':
            raise ValueError("valores do nome_senha.txt vazios")
    dados.close()
    return {'email': nome, 'senha': senha, 'links': links}

if __name__ == '__main__':
    from selenium import webdriver
    diretorio = os.path.dirname(os.path.realpath(__file__))
    if platform.system() == 'Linux':
        diretorio_WebDriver = diretorio + '/WebDrivers/chromedriver'
        diretorio_txt = diretorio + '/nome_senha.txt'
    elif platform.system() == 'Windows':
        diretorio_WebDriver = diretorio + '\\WebDrivers\\chromedriver.exe'
        diretorio_txt = diretorio + '\\nome_senha.txt'

    dados = ler_txt(diretorio_txt)
    print('Salve, sou Jubiscreison seu BOT para logar no Gambolao.net O.O')
    print('Peguei alguns dados que estava no arquivo nome_senha.txt:')
    print(f"email:{dados.get('email')}\nlinks:{dados.get('links')}")
    print('E agora to abrindo o Chrome...')

    browser = webdriver.Chrome(diretorio_WebDriver)

    browser.get('http://gambolao.net/main.php')
    username_textbox = browser.find_element_by_name('username')
    username_textbox.send_keys(dados.get('email'))
    password_textbox = browser.find_element_by_name('pw')
    password_textbox.send_keys(dados.get('senha'))

    login_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[2]")
    login_button.submit()
    print(range(len(dados.get('links'))))
    for cont in range(len(dados.get('links'))):
        time.sleep(3)
        browser.get(dados.get('links')[cont])

    browser.quit()
    exit()
