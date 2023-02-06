#importando o tkinter
from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk, messagebox
from view import *


################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

################# criando janela ###############
janela = Tk()

#titulo
janela.title("")

#tamanho da janela
janela.geometry('1043x453')

#configurando o background
janela.configure(background=co9)

#bloqueando altura e largura
janela.resizable(width=FALSE, height=FALSE)

#criando o frame titulo
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

#criando o frameentrada de dados
frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

#criando o frame data grid view
frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

#labelcima
app_nome = Label(frame_cima, text='Formulário de Consultoria', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg= co1, relief='flat')
app_nome.place(x=10, y=20)

#configurando frame baixo
#campos nome
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10)

e_nome = Entry(frame_baixo, width=45, justify='left',  relief='solid')
e_nome.place(x=15, y=40)

#campos e-mail
l_email = Label(frame_baixo, text='E-mail *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=70)

e_email = Entry(frame_baixo, width=45, justify='left',  relief='solid')
e_email.place(x=15, y=100)

#campos telefone
l_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_telefone.place(x=10, y=130)

e_telefone = Entry(frame_baixo, width=45, justify='left',  relief='solid')
e_telefone.place(x=15, y=160)

#data
l_dataConsulta = Label(frame_baixo, text='Data Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dataConsulta.place(x=10, y=190)

e_calendar = DateEntry(frame_baixo, width=15, justify='left', background='darkblue', foreground='white', borderwidth=2,  relief='solid', date_patternstr='dd/mm/yyyy', localestr='pt-BR')
e_calendar.place(x=15, y=220)

#estado
l_estado = Label(frame_baixo, text='Estado da Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_estado.place(x=150, y=190)

e_estado = Entry(frame_baixo, width=21, justify='left',  relief='solid')
e_estado.place(x=155, y=220)

#campos sobre
l_sobre = Label(frame_baixo, text='Informação Extra *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_sobre.place(x=10, y=250)

e_sobre = Entry(frame_baixo, width=45, justify='left',  relief='solid')
e_sobre.place(x=15, y=280)

global tree

def inserir():
    nome = e_nome.get()
    email = e_email.get()
    tel = e_telefone.get()
    dia = e_calendar.get_date()
    estado = e_estado.get()
    sobre = e_sobre.get()

    lista = [nome, email, tel, dia, estado, sobre]
    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        inserindo_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
    
    e_nome.delete(0,'end')
    e_email.delete(0,'end')
    e_telefone.delete(0,'end')
    e_calendar.delete(0,'end')
    e_estado.delete(0,'end')
    e_sobre.delete(0,'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()
    mostrarView()

def atualizar():
    try:
        tree_dados = tree.focus()
        treev_dicio = tree.item(tree_dados)
        treev_lista = treev_dicio['values']
        valor_id = treev_lista[0]

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_calendar.delete(0,'end')
        e_estado.delete(0,'end')
        e_sobre.delete(0,'end')

        e_nome.insert(0, treev_lista[1])
        e_email.insert(0, treev_lista[2])
        e_telefone.insert(0,treev_lista[3])
        e_calendar.insert(0, treev_lista[4])
        e_estado.insert(0, treev_lista[5])
        e_sobre.insert(0, treev_lista[6])

        def atualizando():
            nome = e_nome.get()
            email = e_email.get()
            tel = e_telefone.get()
            dia = e_calendar.get_date()
            estado = e_estado.get()
            sobre = e_sobre.get()

            lista = [nome, email, tel, dia, estado, sobre, valor_id]
            if nome == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
            else:
                atualiza_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')
            
            e_nome.delete(0,'end')
            e_email.delete(0,'end')
            e_telefone.delete(0,'end')
            e_calendar.delete(0,'end')
            e_estado.delete(0,'end')
            e_sobre.delete(0,'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()
            mostrarView()

        b_confirmar = Button(frame_baixo, command=atualizando , text='Confirmar', width=10, font=('Ivy 10 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=107, y=360)
        
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela.')

def deletar():
    try:
        tree_dados = tree.focus()
        treev_dicio = tree.item(tree_dados)
        treev_lista = treev_dicio['values']
        valor_id = [treev_lista[0]]

        deletar_info(valor_id)

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        for widget in frame_direita.winfo_children():
                widget.destroy()
        mostrarView()
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela.')

#botao inserir
b_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, font=('Ivy 10 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=320)
#botao atualizar
b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=10, font=('Ivy 10 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=107, y=320)
#botao deletar
b_deletar = Button(frame_baixo, command=deletar ,text='Deletar', width=10, font=('Ivy 10 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=199, y=320)

def mostrarView():
    ####frame direita
    global tree

    lista = mostrar_info()

    header_list = ['ID', 'Nome', 'E-mail', 'Telefone', 'Data', 'Estado', 'Sobre']

    #criando o treeview
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=header_list, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical",command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","center","center","center","center"]
    h = [30,170,140,100,120,50,100]
    n = 0

    for col in header_list:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)


mostrarView()
#executando a janela
janela.mainloop()
