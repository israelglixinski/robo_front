import tkinter

def monitor():
    janela = tkinter.Tk()
    caixa_texto = tkinter.Text(janela)
    caixa_texto.pack()

    def verifica():
        try:
            caixa_texto.delete('1.0',tkinter.END)
            recupera = open('log.txt','r')
            caixa_texto.insert('1.0', recupera.read())
            caixa_texto.see('end')
            recupera.close()
            janela.after(200,verifica)
        except:
            print('ex')

    verifica()
    janela.mainloop()

monitor()
print('fim')
