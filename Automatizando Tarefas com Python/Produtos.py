                                        # ------------------------------- Passo a Passo Para cadastrar os Produtos ----------------------------
                                        # Passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
                                        # Passo 2: fazer o login 
                                        # Passo 3: Importar a base de dados
                                        # Passo 4: Cadastrar 1 produto
                                        # Passo 5: Repetir o processo de cadastro até acabar os produtos
                                        #------------------------------------------------------------------------------------------------------


#------------------------------------------- Iniciando Programa----------------------------------------
# Passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time


                                        #------------------------------ comandos basicos da biblioteca pyautogui ----------------------------------------
                                        #pyautogui.write -> escrever um texto
                                        #pyautogui.click -> clicar com o mouse
                                        #pyautogui.press -> apertar uma tecla
                                        #pyautogui.hotkey -> apertar um atalho de teclado (Ctrl, c)
                                        #pyautogui.PAUSE = 0.5 -> Delay
                                        #pyautogui.drag -> arrastar 
                                        #pyautogui.scroll -> ir para cima ou para baixo 
                                        #------------------------------------------------------------------------------------------------------


                #---------------------- Passo 1 ----------------------------------------------------------
pyautogui.PAUSE = 0.4
                # abrir o navegado 
pyautogui.press("win")
                #escrevendo o que é para pesquisar 
pyautogui.write("opera")
                # apertando o ENTER
pyautogui.press("enter")
                #----------------------- Fim do Passo 1 ---------------------------------------------------



                    #-------------------------------- Passo 2 -------------------------------------------------
                    #entrando no link da empresa 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

                    #quero dar uma pausa de 3 segundos
time.sleep(2)
                    #fazer o login
pyautogui.click(x=755, y=362)
pyautogui.write("exemplo@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("enter")
                    #-------------------------------- Fim do Passo 2----------------------------------------------


                    #---------------------------------- Passo 3 --------------------------------------------------
                    #Biblioteca de leitura de documentos
import pandas

tabelap = pandas.read_csv("produtos.csv") 
print(tabelap)

                    #-----------------------------Fim do Passo 3-------------------------------------------------


                    #------------------------------------------passo 4 junto com o 5--------------------------------------------



                    #para cada linha da minha tabela 
for linha in tabelap.index:
        
                    #selecionar o primeiro campo
        pyautogui.click(x=777, y=251)

                    #codigo
        codigo = tabelap.loc[linha, "codigo"]
        pyautogui.write(str(codigo))
        pyautogui.press("tab")

                    #marca
        marca = tabelap.loc[linha, "marca"]
        pyautogui.write(str(marca))
        pyautogui.press("tab")

                    #tipo
        tipo = tabelap.loc[linha, "tipo"]
        pyautogui.write(str(tipo))
        pyautogui.press("tab")

                    #categoria
        categoria = tabelap.loc[linha, "categoria"]
        pyautogui.write(str(categoria))
        pyautogui.press("tab")

                    # preço unitario
        preco_unitario = tabelap.loc[linha, "preco_unitario"]
        pyautogui.write(str(preco_unitario))
        pyautogui.press("tab")

                    #custo
        custo = tabelap.loc[linha, "custo"]
        pyautogui.write(str(custo))
        pyautogui.press("tab")

                    #obs
        obs = tabelap.loc[linha, "obs"]
        if not pandas.isna(obs):
            pyautogui.write(str(obs))
        pyautogui.press("tab")

                    #Enviar
        pyautogui.press("enter")
        pyautogui.scroll(5000)

#---------------------------------------------- fim do Passo 4 junto com o 5--------------------------------------
#-----------------------------------------------Fim do programa --------------------------------------------------