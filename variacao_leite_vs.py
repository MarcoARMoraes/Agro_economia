import matplotlib.pyplot as plt
from tkinter import *
from tkinter import Tk
from tkinter import ttk

janela_principal = Tk()
janela_principal.title('VARIAÇÃO DE VALORES')
janela_principal.geometry('400x400')
janela_principal.resizable(False, False)
janela_principal.configure(background="white")

#CARREGANDO IMAGEM LOGO
logo_agro_economia = PhotoImage(file="logo.png")

def consulta_leite():
    if cb_comodities.get() == "Leite":
        anos = [2017, 2018, 2019, 2020, 2021, 2022]

        valores = [1.53, 1.24, 1.62, 1.47, 2.03, 2.13]

        #CÁLCULO DO PERCENTUAL
        soma_leite = valores[5] - valores[0]
        aumento_leite = soma_leite / valores[0]
        percentual_aumento_leite = aumento_leite * 100
                
        plt.style.use('ggplot')
        plt.figure(figsize=(7,5))

        plt.title('Variação do leite', fontsize=16, fontweight='bold', fontstyle='italic', fontfamily='serif')
        plt.xlabel('Anos estudados', fontsize=10, fontfamily='serif')
        plt.ylabel('Valores obtidos', fontsize=10, fontfamily='serif')
        plt.tight_layout()
        plt.plot(anos, valores, label='Valores em R$/litro')
        plt.legend(fontsize=14, frameon=True, framealpha=0.5, facecolor='white')
        lbl_resultado['text'] = f'No período entre os anos 2017 e 2022,\n o leite sofreu aumento de {percentual_aumento_leite:.2f}%'
        plt.show()

lbl_titulo = Label(janela_principal, image=logo_agro_economia)
lbl_titulo.place(x=80, y=20)

comodities = ["Arroz", "Aveia", "Cacau", "Café", "Feijão", "Leite", "Milho", "Ovos", "Soja"]

#COMBO BOX
cb_comodities = ttk.Combobox(janela_principal, value=comodities, font="Arial 12", width=10)
cb_comodities.place(x=150, y=110)

#BOTÃO
btn_consultar = Button(janela_principal, text="CONSULTAR", font="Arial 10 bold", command=consulta_leite, relief=GROOVE)
btn_consultar.place(x=160, y=150)

#RESULTADO
lbl_resultado = Label(janela_principal, text="", bg='light grey', width=35, height=7, font="Arial 12 bold")
lbl_resultado.place(x=20, y=200)

#ASSINATURA
lbl_assinatura = Label(janela_principal, text="Desenvolvido por Marco Moraes", font="Arial 12 italic bold", bg="white")
lbl_assinatura.place(x=80, y=360)

janela_principal.mainloop()