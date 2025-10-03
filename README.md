# Assistente Virtual por Voz 🎙️🤖

Este é um projeto de **assistente virtual controlado por voz** que entende comandos falados, responde com voz sintetizada e pode executar algumas ações básicas como abrir sites, contar piadas e pesquisar na Wikipedia.

## 🚀 Funcionalidades

* Reconhecimento de voz usando [SpeechRecognition](https://pypi.org/project/SpeechRecognition/).
* Conversão de texto para fala com [gTTS](https://pypi.org/project/gTTS/).
* Reprodução de áudio com [pygame](https://www.pygame.org/).
* Execução de comandos básicos:

  * Abrir o YouTube.
  * Pesquisar na Wikipedia.
  * Contar piadas.
  * Encerrar a execução.

## 📦 Instalação

Antes de rodar o projeto, é necessário instalar as dependências.
No terminal do **Visual Studio Code**, execute:

```bash
pip install SpeechRecognition gTTS pyjokes wikipedia playsound pygame
```

## ▶️ Como usar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/assistente-voz.git
   cd assistente-voz
   ```

2. Execute o script principal:

   ```bash
   python assistente.py
   ```

3. O assistente iniciará e você poderá interagir usando sua voz.

### Exemplos de comandos:

* **"Abrir YouTube"** → abre o navegador no YouTube.
* **"Pesquisar Python na Wikipedia"** → retorna um resumo da pesquisa.
* **"Me conta uma piada"** → o assistente responde com uma piada.
* **"Encerrar"** → finaliza o programa.

## 🛠️ Requisitos

* Python 3.8+
* Microfone configurado para captura de áudio
* Conexão com a internet (necessária para o reconhecimento de voz e gTTS)

## 📖 Observações

* O código foi ajustado para funcionar corretamente no **Windows**, evitando erros de permissão ao reproduzir arquivos de áudio temporários.
* Arquivos de áudio são apagados automaticamente após a execução, não ocupando espaço na pasta temporária.

---

👨‍💻 Desenvolvido por **Heytor de Queiroz Alves**
