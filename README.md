# Python Currency Converter

## 🇺🇸 English

This project is a **desktop currency converter built with Python** that allows users to check real-time exchange rates between multiple currencies.

The application provides a graphical interface where users can select a source currency and a destination currency and retrieve the latest exchange rate using an external API.

### Features

* Desktop graphical interface built with **CustomTkinter**
* Real-time currency exchange rates
* Dynamic currency selection
* Scrollable list of available currencies
* Data loaded from XML files
* External API integration

### Technologies

* Python
* CustomTkinter
* Requests
* xmltodict
* AwesomeAPI (Exchange Rate API)

### How It Works

1. The application loads currency names from an XML file.
2. Available conversion pairs are loaded from another XML file.
3. The user selects a source currency.
4. The destination currency list is updated dynamically.
5. When the user clicks **Convert**, the system retrieves the latest exchange rate from an external API.
6. The result is displayed in the interface.

### Installation

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python main.py
```

### Project Structure

```
python-currency-converter
│
├── main.py
├── pegar_cotacao.py
├── pegar_moedas.py
├── moedas.xml
├── conversoes.xml
├── requirements.txt
└── README.md
```

---

## 🇧🇷 Português

Este projeto é um **conversor de moedas com interface gráfica desenvolvido em Python** que permite consultar cotações em tempo real entre diferentes moedas.

A aplicação fornece uma interface onde o usuário pode selecionar uma moeda de origem e uma moeda de destino e visualizar a cotação atual utilizando uma API externa.

### Funcionalidades

* Interface gráfica desktop construída com **CustomTkinter**
* Consulta de cotações em tempo real
* Seleção dinâmica de moedas
* Lista rolável de moedas disponíveis
* Leitura de dados a partir de arquivos **XML**
* Integração com API externa

### Tecnologias

* Python
* CustomTkinter
* Requests
* xmltodict
* AwesomeAPI (API de cotações)

### Como funciona

1. A aplicação carrega os nomes das moedas a partir de um arquivo XML.
2. Os pares de conversão disponíveis são carregados de outro XML.
3. O usuário seleciona uma moeda de origem.
4. A lista de moedas de destino é atualizada automaticamente.
5. Ao clicar em **Converter**, o sistema consulta a cotação atual em uma API externa.
6. O resultado é exibido na interface.

### Instalação

Instale as dependências:

```
pip install -r requirements.txt
```

Execute o programa:

```
python main.py
```
