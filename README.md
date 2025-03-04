```markdown
# Pywhatkit-desktop

Aplicativo desktop desenvolvido em Python e Tkinter para envio de mensagens em massa no WhatsApp.
Permite enviar mensagens personalizadas para múltiplos contatos,
com a opção de enviar mensagens de texto simples ou texto com imagem.

## Funcionalidades:
- Carregar um arquivo CSV com nomes e números de telefone dos contatos.
- Personalizar mensagens utilizando placeholders, como `{nome}`.
- Enviar mensagens em dois formatos:
  - **Apenas Texto**.
  - **Texto com Imagem**.
- Seleção fácil de imagens para envio com as mensagens.
- Notificações de sucesso ou erro.

## Requisitos:
- Python 3.x
- PyWhatKit (`pip install pywhatkit`)
- Tkinter (geralmente incluso no Python)
- Arquivo CSV contendo os contatos com as colunas "nome" (nome do contato) e "numero" (número de telefone)

## Instalação:
1. Clone ou faça o download deste repositório.
2. Instale as dependências:
   ```bash
   pip install pywhatkit
   ```

## Como Usar:

1. **Execute o Aplicativo:**
   ```bash
   python app.py
   ```

2. **Carregue os Contatos:**
   - Clique no botão **"📤 Carregar CSV"** para selecionar um arquivo CSV.
   - O CSV deve conter duas colunas: `nome` (nome do contato) e `numero` (número de telefone).

3. **Componha Sua Mensagem:**
   - Digite a mensagem na caixa de texto.
   - Utilize `{nome}` como um placeholder para o nome de cada contato.
   - Escolha entre enviar apenas texto ou incluir uma imagem.

4. **Adicione uma Imagem (Opcional):**
   - Se for enviar uma imagem, clique no botão **"📷 Adicionar Imagem"** e selecione o arquivo de imagem.

5. **Envie as Mensagens:**
   - Clique no botão **"📤 Enviar Mensagens"** para enviar as mensagens.
   - O aplicativo enviará as mensagens para cada contato do arquivo CSV.

## Estrutura de Arquivos:
- `app.py`: Arquivo principal do aplicativo, contendo a lógica.
- `PyWhatKit_DB.txt`: Armazena os dados dos contatos e mensagens.

## Problemas Comuns:
- Certifique-se de que o campo `numero` no arquivo CSV esteja formatado corretamente com o código do país (exemplo: `+5511999999999` para o Brasil).
- Verifique se o caminho do arquivo de imagem é válido ao enviar mensagens com mídia.

## Licença:
```
O valor da licença anual da aplicação é R$ 97. Entre em contato +55(31) 99365-8409. Atenciosamente, Gerson Moreira.
