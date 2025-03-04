import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pywhatkit as kit
import csv
import os

# Função para enviar mensagem
def enviar_mensagem(contato, mensagem, tipo_mensagem, imagem_path=None):
    try:
        mensagem = mensagem.replace("{nome}", contato['nome'])
        
        if tipo_mensagem == 'texto':
            kit.sendwhatmsg(contato['numero'], mensagem, 15, 0, wait_time=10, tab_close=True)
        elif tipo_mensagem == 'imagem':
            if imagem_path and os.path.exists(imagem_path):
                kit.sendwhats_image(contato['numero'], imagem_path, mensagem, wait_time=15, tab_close=True)
            else:
                print(f"Imagem não encontrada para o contato {contato['nome']}")
                messagebox.showwarning("Aviso", "Imagem não encontrada ou caminho inválido!")
                return
        print(f"Mensagem enviada para {contato['nome']} ({contato['numero']})")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {contato['nome']} ({contato['numero']}): {e}")
        messagebox.showerror("Erro", f"Erro ao enviar mensagem para {contato['nome']}: {e}")

# Função para carregar o arquivo CSV com números e nomes
def carregar_csv():
    try:
        arquivo_csv = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if arquivo_csv:
            with open(arquivo_csv, newline='') as csvfile:
                leitor = csv.DictReader(csvfile)
                contatos = [{"nome": row['nome'], "numero": row['numero']} for row in leitor]
            return contatos
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar CSV: {e}")
    return []

# Função para enviar as mensagens após a configuração
def enviar_mensagens():
    contatos = carregar_csv()
    if not contatos:
        messagebox.showwarning("Aviso", "Nenhum contato carregado!")
        return
    
    mensagem = app.txt_message.get("1.0", tk.END).strip()  # Captura a mensagem do campo Text
    tipo_mensagem = app.tipo_mensagem_var.get()

    imagem_path = None
    if tipo_mensagem == 'imagem':
        imagem_file = app.imagem_entrada.get()
        if imagem_file and os.path.exists(imagem_file):
            imagem_path = imagem_file
        else:
            messagebox.showwarning("Aviso", "Imagem não selecionada ou caminho inválido!")
            return

    # Enviar as mensagens para cada contato
    for contato in contatos:
        enviar_mensagem(contato, mensagem, tipo_mensagem, imagem_path)
    
    messagebox.showinfo("Sucesso", "Mensagens enviadas com sucesso!")

# Interface principal
class WhatsAppApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WhatsApp Messenger Pro")
        self.geometry("600x600")  # Ajuste para um tamanho menor
        self.configure(bg=Style.BACKGROUND)
        self.style = ttk.Style()
        self.setup_styles()
        self.create_widgets()
    
    def setup_styles(self):
        self.style.theme_use('clam')
        self.style.configure('TFrame', background=Style.BACKGROUND)
        self.style.configure('TLabel', background=Style.BACKGROUND, foreground=Style.TEXT)
        self.style.configure('TRadiobutton', background=Style.BACKGROUND, font=Style.FONT)
        self.style.map('TRadiobutton',
            background=[('active', Style.BACKGROUND)],
            foreground=[('selected', Style.PRIMARY)]
        )
    
    def create_widgets(self):
        # Header
        header_frame = ttk.Frame(self)
        header_frame.pack(pady=15, fill='x')
        
        self.header_label = ttk.Label(header_frame, text="🚀 ZipZops", 
                                     font=("Segoe UI", 16, "bold"), foreground=Style.PRIMARY)
        self.header_label.pack()
        
        # Card principal
        main_card = RoundedFrame(self, radius=Style.RADIUS, color="white", shadow=Style.SHADOW)
        main_card.pack(padx=15, pady=10, fill='both', expand=True)
        
        # Campo de mensagem
        msg_frame = ttk.Frame(main_card)
        msg_frame.pack(pady=10, fill='x', padx=15)
        
        self.msg_label = ttk.Label(msg_frame, text="Mensagem personalizada:", 
                                  font=Style.FONT_BOLD)
        self.msg_label.pack(anchor='w')
        
        self.txt_message = tk.Text(msg_frame, height=6, font=Style.FONT,  # Diminuímos a altura aqui
                                 bg="white", relief='flat', highlightthickness=1,
                                 highlightcolor=Style.PRIMARY, wrap=tk.WORD)
        self.txt_message.pack(fill='x')
        self.txt_message.insert('1.0', "Olá {nome}! 👋\n\n[Escreva sua mensagem aqui]")

        # Seção de mídia
        media_frame = ttk.Frame(main_card)
        media_frame.pack(pady=10, fill='x', padx=15)
        
        self.btn_media = IconButton(media_frame, text="📷 Adicionar Imagem", 
                                      command=self.selecionar_imagem)
        self.btn_media.pack(side='left')

        self.imagem_entrada = ttk.Entry(media_frame, font=Style.FONT, width=20)  # Diminui a largura
        self.imagem_entrada.pack(side='left', padx=5)

        # Seletor de tipo
        type_frame = ttk.Frame(main_card)
        type_frame.pack(pady=10, fill='x', padx=15)
        
        self.type_label = ttk.Label(type_frame, text="Tipo de mensagem:", 
                                   font=Style.FONT_BOLD)
        self.type_label.pack(anchor='w')
        
        self.tipo_mensagem_var = tk.StringVar(value="texto")
        self.rb_text = IconRadioButton(type_frame, text="📝 Apenas Texto", 
                                      value="texto", variable=self.tipo_mensagem_var)
        self.rb_text.pack(anchor='w')
        
        self.rb_image = IconRadioButton(type_frame, text="🖼️ Texto com Imagem", 
                                       value="imagem", variable=self.tipo_mensagem_var)
        self.rb_image.pack(anchor='w')
        
        # Controles
        control_frame = ttk.Frame(main_card)
        control_frame.pack(pady=15, fill='x', padx=15)
        
        self.btn_send = IconButton(control_frame, text="📤 Enviar Mensagens", 
                                     command=enviar_mensagens)
        self.btn_send.pack(side='bottom', pady=5, fill='x')  # Ajuste no espaçamento

    # Função para selecionar arquivo de imagem (agora dentro da classe)
    def selecionar_imagem(self):
        imagem = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if imagem:
            self.imagem_entrada.delete(0, tk.END)
            self.imagem_entrada.insert(0, imagem)

# Configurações de estilo
class Style:
    PRIMARY = "#6366f1"  # Azul forte
    SECONDARY = "#4f46e5"
    BACKGROUND = "#f8fafc"  # Fundo claro
    TEXT = "#1e293b"  # Texto escuro
    SUCCESS = "#22c55e"
    ERROR = "#ef4444"
    FONT = ("Segoe UI", 9)  # Fonte menor para economizar espaço
    FONT_BOLD = ("Segoe UI", 9, "bold")  # Fonte em negrito para título
    RADIUS = 8
    SHADOW = "#D0D0D0"
    BUTTON_HOVER = "#4f46e5"  # Cor para o hover dos botões
    BUTTON_TEXT_COLOR = "#4f46e5"  # Cor do texto nos botões - mudado para preto
    BUTTON_BG_COLOR = "#6366f1"  # Cor de fundo do botão
    BUTTON_HOVER_BG = "#4f46e5"  # Cor do fundo no hover

# Componentes customizados
class RoundedFrame(tk.Canvas):
    def __init__(self, master, radius=25, color="white", shadow=None, **kwargs):
        super().__init__(master, highlightthickness=0, **kwargs)
        self.radius = radius
        self.color = color
        self.shadow = shadow
        self.bind("<Configure>", self.draw)
        
    def draw(self, event=None):
        self.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()
        
        if self.shadow:
            self.create_rounded_rectangle(3, 3, width-3, height-3, radius=self.radius, fill=self.shadow)
        
        self.create_rounded_rectangle(0, 0, width-6, height-6, radius=self.radius, fill=self.color)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y2-radius,
                x2-radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y1+radius,
                x1+radius, y1]
        return self.create_polygon(points, **kwargs, smooth=True)

class IconButton(tk.Canvas):
    def __init__(self, master, text, command=None, bg=Style.BACKGROUND, fg=Style.TEXT,
                 hover_bg=None, icon_size=16, **kwargs):
        super().__init__(master, highlightthickness=0, bg=bg, **kwargs)
        self.command = command
        self.text = text
        self.bg = bg
        self.fg = fg
        self.hover_bg = hover_bg if hover_bg else self.lighten_color(bg)
        self.icon_size = icon_size
        
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)

        self.create_text(10, 10, text=self.text, anchor="w", font=Style.FONT_BOLD, fill=self.fg)
        self.create_oval(10, 10, self.icon_size, self.icon_size, fill="red")
        self.place_button()

    def place_button(self):
        self.config(width=self.winfo_reqwidth(), height=self.winfo_reqheight())

    def on_click(self, event):
        if self.command:
            self.command()

    def on_hover(self, event):
        self.config(bg=self.hover_bg)

    def on_leave(self, event):
        self.config(bg=self.bg)

    def lighten_color(self, color):
        return "#".join([hex(int(x, 16) + 50)[2:].zfill(2) for x in [color[i:i+2] for i in range(1, 6, 2)]])

class IconRadioButton(tk.Radiobutton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, indicatoron=False, background=Style.BACKGROUND,
                         font=Style.FONT, foreground=Style.TEXT, activebackground=Style.BACKGROUND,
                         activeforeground=Style.TEXT)

# Executar o aplicativo
if __name__ == "__main__":
    app = WhatsAppApp()
    app.mainloop()
