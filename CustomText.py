from tkinter import Text, END, IntVar
class CustomText(Text):
    """
    Implementação customizada do gadget Text multilinha do tkinter
    """
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)
        
        # tags de texto que devem ser adotar definida cor
        self.tag_configure("error", foreground="#ff0000")
        self.tag_configure("warning", foreground="#0000ff")
        self.tag_configure("regular", foreground="#000000")
        self.tag_configure("comment", foreground="limegreen")

        # define funcoes de callback para cada ação realizada sobre a janela
        self.bind('<Enter>', self.check_syntax)
        self.bind('<BackSpace>', self.check_syntax)
        self.bind(';', self.check_syntax)
        self.bind('<Return>', self.check_syntax)
    def check_syntax(self, event):
        """Checa a sintaxe do texto, aplicando tags aos símbolos e os destacando"""
        textBoxContent = self.get('1.0', END)
    def highlight_pattern(self, pattern, tag, start="1.0", end="end", regexp=False):
        '''Aplica definida tag a uma seção especifica do texto, para que essa possa ser destacada
        
        Keyword arguments:
        pattern -- String a qual a tag deve ser aplicada
        tag -- Tag a ser aplicada
        start -- Ponto de inicio da consulta no campo de texto
        end -- Ponto de fim da consulta no campo de texto
        regexp -- Utilizar regular expressions (regex) na consulta
        '''
        
        # delimitadores
        start = self.index(start)
        end = self.index(end)

        # delimitadores de marcação de pesquisa
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        # contador tipo IntVar (tkinter)    
        count = IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit", count=count, regexp=regexp)
            if(index == ""):
                break
            if(count.get() == 0):
                break # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")