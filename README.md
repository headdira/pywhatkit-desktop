# Pywhatkit-Desktop 

> Aplicativo desktop para envio automatizado de mensagens personalizadas em massa no WhatsApp, desenvolvido com Python e Tkinter.

## 📋 Visão Geral

Pywhatkit-Desktop automatiza o processo de envio de mensagens personalizadas para múltiplos contatos no WhatsApp. Combina uma interface gráfica intuitiva com recursos avançados de mensagens.

### ✨ Principais Recursos

- 📱 Envio de mensagens em massa para contatos do WhatsApp
- 🎯 Personalização de mensagens com nomes dos destinatários usando variáveis como `{nome}`
- 📸 Suporte para envio de mensagens com texto e imagem
- 📊 Importação simplificada de contatos via arquivo CSV
- 🔔 Notificações em tempo real de sucesso/erro

## 🚀 Como Começar

### Pré-requisitos

- Python 3.13.1
- Conta no WhatsApp Web
- Conexão com a Internet

### 📥 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/headdira/pywhatkit-desktop.git
   cd pywhatkit-desktop
   ```

2. Instale os pacotes necessários:
   ```bash
   pip install pywhatkit
   ```

### 📝 Formato do Arquivo CSV

Seu arquivo CSV de contatos deve incluir:

| nome | numero |
|------|--------|
| João | +5511999999999 |
| Maria | +5511988888888 |

> Observação: Os números de telefone devem incluir o código do país (ex: +55 para Brasil)

## 💻 Como Usar

1. Inicie o aplicativo:
   ```bash
   python app.py
   ```

2. Siga estes passos:
   1. Clique em `📤 Carregar CSV` para carregar seu arquivo de contatos
   2. Digite sua mensagem na caixa de texto (use `{nome}` para personalização)
   3. Para mensagens com imagem:
      - Clique em `📷 Adicionar Imagem`
      - Selecione seu arquivo de imagem
   4. Clique em `📤 Enviar Mensagens` para iniciar o envio

## 📁 Estrutura do Projeto

```
whatsapp-messenger-pro/
├── app.py               # Código principal do aplicativo
├── requirements.txt     # Dependências Python
└── PyWhatKit_DB.txt    # Registros de mensagens
```

## ⚠️ Solução de Problemas

- **Formato do Número**: Certifique-se que os números incluam código do país (+5511999999999)
- **Problemas com Imagens**: Verifique o caminho do arquivo e formatos suportados (jpg, png)
- **WhatsApp Web**: Mantenha o WhatsApp Web ativo durante o envio das mensagens

## 📄 Licença

Codigo aberto, contribuições são bem vindas.

## 📞 Suporte

Contato miniibooking@gmail.com

---

### 📌 Dicas de Uso

1. **Preparação dos Contatos**:
   - Verifique se todos os números estão no formato correto
   - Remova espaços extras nos nomes
   - Evite caracteres especiais no arquivo CSV

2. **Mensagens**:
   - Teste primeiro com poucos contatos
   - Verifique a formatação antes do envio em massa
   - Mantenha uma cópia de segurança do texto das mensagens

3. **Melhores Práticas**:
   - Evite enviar mensagens em horários inadequados
   - Respeite os limites de envio do WhatsApp
   - Mantenha o computador conectado durante o processo

### 🔧 Configurações Recomendadas

- **Sistema Operacional**: Windows 10/11, Linux ou macOS
- **Navegador**: Chrome ou Firefox atualizado
- **Resolução Mínima**: 1280x720
- **Memória RAM**: 4GB ou superior

### 📊 Recursos Adicionais

- Monitor de status de envio
- Log detalhado de mensagens
- Backup automático de configurações
- Suporte a múltiplos formatos de imagem

### 🚫 Limitações Conhecidas

1. Necessário manter WhatsApp Web ativo
2. Limite de envios conforme políticas do WhatsApp
3. Necessária conexão estável com a internet

## 📱 Compatibilidade

O sistema é compatível com as seguintes versões do WhatsApp:
- WhatsApp Web
- WhatsApp Desktop
- WhatsApp Business (web)

> **Importante**: Mantenha sempre seu WhatsApp e navegador atualizados para melhor compatibilidade.
