from tkinter import Text, END
class LineNumbers(Text):
    """
    Campo de texto adaptado para exibir o número de linhas de um CustomText
    """
    def __init__(self, master, text_widget, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.text_widget = text_widget

        # eventos de callback, que vão atualizar o numero de linhas
        self.text_widget.bind('<KeyRelease>', self.on_key_release)
        self.text_widget.bind('<FocusIn>', self.on_key_release)
        self.text_widget.bind('<MouseWheel>', self.on_key_release)
 
        self.insert(1.0, '1')
        self.configure(state='disabled')
    def on_key_release(self, event=None):
        p, q = self.text_widget.index("@0,0").split('.')
        p = int(p)
        final_index = str(self.text_widget.index(END))
        num_of_lines = final_index.split('.')[0]
        line_numbers_string = "\n".join(str(p + no) for no in range(int(num_of_lines)))
        width = len(str(num_of_lines))
        self.configure(state='normal', width=width)  # ativa o widget para a inserção dos novos numeros - ajusta a largura
        self.delete(1.0, END)  # deleta todos os numeros de linha (do elemento 1 ao final da string)
        self.insert(1.0, line_numbers_string)  # insere novamente todos os numeros de linha
        self.configure(state='disabled')  # desabilita o widget - para que esse não possa ser editado