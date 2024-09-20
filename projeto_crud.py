import tkinter as tk
from tkinter import messagebox


def calcular_imc():
    try:
        nome = campo_nome.get()
        altura = float(campo_altura.get())
        peso = float(campo_peso.get())

        if altura == 0 or peso == 0 or nome == '':
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
            return None

        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso adequado"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 34.9:
            classificacao = "Obesidade grau 1"
        elif 35 <= imc < 39.9:
            classificacao = "Obesidade grau 2"
        else:
            classificacao = "Obesidade grau 3"

        resultado = f"Nome: {nome}\nIMC: {imc:.2f}\nClassificação: {classificacao}"
        messagebox.showinfo("Resultado do IMC", resultado)

        with open("dados_imc.txt", "a") as file:
            file.write(f"Nome: {nome}, Altura: {altura}, Peso: {peso}, IMC: {imc:.2f}, Classificação: {classificacao}\n")

        return nome, altura, peso, imc, classificacao

    except ValueError:
        messagebox.showerror("Erro", "Por favor, Preencha todos os campos corretamente")
        return


def ler_dados():
    with open("dados_imc.txt", "r") as arquivo:
        dados = arquivo.readlines()
    return dados


def atualizar_dados():
    nome, altura, peso, imc, classificacao = calcular_imc()
    if altura is None or peso is None or nome is None:
        return
    dados = ler_dados()
    for i in range(len(dados)):
        linha = dados[i].strip()
        if linha.startswith(f"Nome: {nome}"):
            dados[i] = f"Nome: {nome}, Altura: {altura}m, Peso: {peso}kg, IMC: {imc:.2f}, Classificação: {classificacao}\n"
    with open("dados_imc.txt", "w") as arquivo:
        arquivo.writelines(dados)


def excluir_dados():
    nome_excluir = campo_nome.get()
    try:
        with open("dados_imc.txt", "r") as arquivo:
            dados = arquivo.readlines()
        with open('dados_imc.txt', 'w') as arquivo:
            for i in dados:
                linha = i.split(', ')
                if len(linha) >= 1:
                    nome = linha[0].split(': ')[1]
                    if nome != nome_excluir:
                        arquivo.write(i)

    except FileNotFoundError:
        print("Sem dados encontrados")


def exibir_dados():
    dados = ler_dados()
    for linha in dados:
        linha = linha.strip()
        if linha:
            print(linha)


def limpar_campos():
    campo_peso.delete(0, tk.END)
    campo_nome.delete(0, tk.END)
    campo_altura.delete(0, tk.END)

janela = tk.Tk()
janela.title('Calculadora de IMC')
janela.geometry('400x600')

titulo = tk.Label(janela, text='Calculadora de IMC')
titulo.pack(pady=30)

texto_nome = tk.Label(janela, text='Nome:')
texto_nome.pack(pady=5)
campo_nome = tk.Entry(janela)
campo_nome.pack(pady=0)

texto_altura = tk.Label(janela, text='Altura: (em metros)')
texto_altura.pack(pady=5)
campo_altura = tk.Entry(janela)
campo_altura.pack(pady=0)

texto_peso = tk.Label(janela, text='Peso: (em kg)')
texto_peso.pack(pady=5)
campo_peso = tk.Entry(janela)
campo_peso.pack(pady=0)

botao_calcular = tk.Button(janela, text='Calcular IMC', command=calcular_imc)
botao_calcular.pack(pady=20)

botao_atualizar = tk.Button(janela, text='Atualizar dados', command=atualizar_dados)
botao_atualizar.pack(pady=0)

botao_excluir = tk.Button(janela, text="Excluir dados", command=excluir_dados)
botao_excluir.pack(pady=20)

botao_ler = tk.Button(janela, text="Ler dados", command=exibir_dados)
botao_ler.pack(pady=0)

clear_button = tk.Button(janela, text="Limpar os campos", command=limpar_campos)
clear_button.pack(pady=40)

janela.mainloop()