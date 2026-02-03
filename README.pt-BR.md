<div align="center">

# 🔗 Solscan Transaction Viewer

**Uma aplicação web Flask para visualizar e exportar transações da blockchain Solana**

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)](https://flask.palletsprojects.com/)
[![Solana](https://img.shields.io/badge/Solana-Blockchain-9945FF?logo=solana)](https://solana.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Funcionalidades](#-funcionalidades) • [Início Rápido](#-início-rápido) • [Uso](#-uso) • [API](#-api) • [Stack Tecnológica](#%EF%B8%8F-stack-tecnológica) • [Licença](#-licença)

**Idiomas:** [🇺🇸 English](README.md) • [🇪🇸 Español](README.es.md)

</div>

---

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Início Rápido](#-início-rápido)
- [Uso](#-uso)
- [API](#-api)
- [Stack Tecnológica](#%EF%B8%8F-stack-tecnológica)
- [Configuração](#%EF%B8%8F-configuração)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 🎯 Visão Geral

**Solscan Transaction Viewer** é uma aplicação web Flask leve que busca e exibe o histórico de transações de qualquer endereço de carteira Solana usando a API do Solscan. Fornece uma visualização de tabela interativa e pesquisável com recursos de ordenação e exportação para CSV.

Perfeito para:
- 📊 Analisar histórico de transações de carteiras
- 🔍 Pesquisar e filtrar transações
- 📥 Exportar dados de transações para CSV
- 📈 Rastrear atividade na blockchain

---

## 👨‍💻 Sobre o Desenvolvedor

<div align="center">

**Desenvolvido por Rafael Vieira (TechBeme)**

[![GitHub](https://img.shields.io/badge/GitHub-TechBeme-181717?logo=github)](https://github.com/TechBeme)
[![Fiverr](https://img.shields.io/badge/Fiverr-Tech__Be-1DBF73?logo=fiverr)](https://www.fiverr.com/tech_be)
[![Upwork](https://img.shields.io/badge/Upwork-Profile-14a800?logo=upwork)](https://www.upwork.com/freelancers/~01f0abcf70bbd95376)
[![Email](https://img.shields.io/badge/Email-contact@techbe.me-EA4335?logo=gmail)](mailto:contact@techbe.me)

**Desenvolvedor Full-Stack & Especialista em Automação**

Especializado em **web scraping**, **sistemas de automação**, **aplicações web modernas** e **integrações de API**.

### 💼 Principais Competências

- 🔍 Web Scraping & Extração de Dados
- ⚡ Automação de Processos & Workflows
- 💻 Desenvolvimento Full-Stack (Flask, React, Python, TypeScript)
- 🔌 Desenvolvimento de APIs & Integrações
- 🗄️ Design e Otimização de Bancos de Dados
- 🎨 Desenvolvimento de UI/UX Moderno

### 🌍 Idiomas

🇺🇸 **English** • 🇧🇷 **Português** • 🇪🇸 **Español**

### 📬 Contato

**Email**: [contact@techbe.me](mailto:contact@techbe.me)

</div>

---

## ✨ Funcionalidades

### Visualização de Dados
- **DataTable Interativa**: Pesquise, ordene e filtre transações com facilidade
- **Detalhes da Transação**: Visualize assinatura, número do bloco, timestamp, instruções, signatários e taxas
- **Dados em Tempo Real**: Busca dados de transações atualizados da API do Solscan
- **Design Responsivo**: Funciona em desktop e dispositivos móveis

### Capacidades de Exportação
- **Exportação CSV**: Baixe dados de transações em formato CSV delimitado por tabulação
- **Dados Formatados**: Taxas SOL devidamente formatadas (9 casas decimais)
- **Histórico Completo**: Exporte todas as transações de uma vez

### Recursos Técnicos
- **Consultas de Alto Limite**: Busca até 99.999.999 transações por endereço
- **Análise de Instruções**: Agrupa e exibe tipos de instruções analisadas
- **Conversão de Taxas**: Conversão automática de lamports para SOL
- **Armazenamento em Memória**: Geração e downloads rápidos de CSV

---

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/TechBeme/Solscan.git
cd Solscan

# Instale as dependências
pip install -r requirements.txt
```

### Executando a Aplicação

```bash
# Modo de desenvolvimento
python flask-solscan.py

# Modo de produção com Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 flask-solscan:app
```

A aplicação iniciará em `http://localhost:5000` (desenvolvimento) ou `http://localhost:8000` (produção).

---

## 📖 Uso

### Visualizando Transações

1. Abra seu navegador e navegue para:
   ```
   http://localhost:5000/<ENDEREÇO_CARTEIRA>
   ```
   Substitua `<ENDEREÇO_CARTEIRA>` por qualquer endereço de carteira Solana válido.

2. A página exibirá uma tabela interativa com todas as transações daquele endereço.

### Usando a DataTable

- **Pesquisar**: Use a caixa de pesquisa para filtrar transações por qualquer campo
- **Ordenar**: Clique nos cabeçalhos das colunas para ordenar ascendente/descendente
- **Paginação**: Navegue pelas páginas de transações
- **Itens por página**: Ajuste quantas transações exibir de uma vez

### Exportando Dados

Clique no botão **"Download CSV"** na parte inferior da página para baixar todos os dados de transações em formato CSV com delimitadores de tabulação.

---

## 🔌 API

### Endpoints

#### `GET /<address>`

Busca e exibe transações para o endereço de carteira Solana especificado.

**Parâmetros:**
- `address` (parâmetro de caminho): Endereço da carteira Solana

**Resposta:**
- Página HTML com DataTable interativa

**Exemplo:**
```
http://localhost:5000/DYw8jCTfwHNRJhhmFcbXvVDTqWMEVFBX6ZKUmG5CNSKK
```

#### `GET /download/<address>`

Baixa dados de transações como um arquivo CSV.

**Parâmetros:**
- `address` (parâmetro de caminho): Endereço da carteira Solana (deve ter sido consultado previamente)

**Resposta:**
- Arquivo CSV com dados de transações delimitados por tabulação

**Exemplo:**
```
http://localhost:5000/download/DYw8jCTfwHNRJhhmFcbXvVDTqWMEVFBX6ZKUmG5CNSKK
```

---

## 🛠️ Stack Tecnológica

| Tecnologia | Versão | Propósito |
|------------|---------|----------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | 3.8+ | Linguagem de programação principal |
| ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white) | 3.0+ | Framework web |
| **Requests** | 2.31+ | Cliente HTTP para chamadas de API |
| **Pandas** | 2.0+ | Processamento de dados e geração de CSV |
| **Gunicorn** | 21.0+ | Servidor WSGI de produção |
| **jQuery** | 3.6.0 | Biblioteca JavaScript |
| **DataTables** | 1.11.5 | Plugin de tabela interativa |
| **Solscan API** | v2 | Dados de transações blockchain |

---

## ⚙️ Configuração

### Variáveis de Ambiente

Nenhuma variável de ambiente necessária para uso básico. A aplicação usa a API pública do Solscan.

### Porta Personalizada

Para executar em uma porta diferente:

```bash
# Desenvolvimento
flask --app flask-solscan run --port 8080

# Produção
gunicorn -w 4 -b 0.0.0.0:8080 flask-solscan:app
```

### Configuração de Workers

Para implantações em produção, ajuste os workers do Gunicorn com base no seu servidor:

```bash
# Fórmula: (2 x CPU_CORES) + 1
gunicorn -w 9 -b 0.0.0.0:8000 flask-solscan:app  # Para CPU de 4 núcleos
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja como você pode ajudar:

1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/funcionalidade-incrivel`)
3. Commit suas mudanças (`git commit -m 'Adiciona funcionalidade incrível'`)
4. Push para a branch (`git push origin feature/funcionalidade-incrivel`)
5. Abra um Pull Request

### Reportando Problemas

Por favor, reporte bugs e solicite funcionalidades através das [GitHub Issues](https://github.com/TechBeme/Solscan/issues).

---

## 📝 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
Licença MIT

Copyright (c) 2026 Rafael Vieira (TechBeme)

A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e dos arquivos de documentação associados (o "Software"), para lidar
no Software sem restrição, incluindo, sem limitação, os direitos
de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender
cópias do Software, e permitir que as pessoas a quem o Software é
fornecido o façam, sujeito às seguintes condições:

O aviso de copyright acima e este aviso de permissão devem ser incluídos em todas
as cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU
IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO,
ADEQUAÇÃO A UM DETERMINADO FIM E NÃO VIOLAÇÃO. EM NENHUMA HIPÓTESE OS
AUTORES OU TITULARES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA
RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, DELITO OU DE OUTRA FORMA, DECORRENTE DE,
FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO
SOFTWARE.
```

---

## ⚠️ Isenção de Responsabilidade

Este projeto é **independente** e **não é afiliado ao Solscan ou Solana**. É uma ferramenta de terceiros que usa dados publicamente disponíveis da API do Solscan para fins educacionais e analíticos.

- Usa endpoints de API publicamente disponíveis
- Respeita limites de taxa e termos da API
- Nenhuma garantia ou garantia de precisão dos dados
- Os usuários são responsáveis pela conformidade com as leis aplicáveis

---

## 🙏 Agradecimentos

- [Solscan](https://solscan.io/) por fornecer a API
- Ecossistema blockchain [Solana](https://solana.com/)
- Framework web [Flask](https://flask.palletsprojects.com/)
- [DataTables](https://datatables.net/) para tabelas interativas
- Todos os contribuidores de código aberto

---

<div align="center">

**Desenvolvido por [Rafael Vieira (TechBeme)](https://github.com/TechBeme)**

[![GitHub](https://img.shields.io/badge/GitHub-TechBeme-181717?logo=github)](https://github.com/TechBeme)
[![Fiverr](https://img.shields.io/badge/Fiverr-Tech__Be-1DBF73?logo=fiverr)](https://www.fiverr.com/tech_be)
[![Upwork](https://img.shields.io/badge/Upwork-Profile-14a800?logo=upwork)](https://www.upwork.com/freelancers/~01f0abcf70bbd95376)
[![Email](https://img.shields.io/badge/Email-contact@techbe.me-EA4335?logo=gmail)](mailto:contact@techbe.me)

⭐ Dê uma estrela neste repo se você achar útil!

</div>
