# ⚽ SportManager Pro - Sistema de Gerenciamento de Elenco Esportivo

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Bottle-green.svg)
![Database](https://img.shields.io/badge/Database-SQLite-blue.svg)

Projeto final desenvolvido para a disciplina de **Orientação a Objetos** da **Faculdade de Ciências e Tecnologias em Engenharia - Campus UnB Gama**.

O SportManager Pro é uma aplicação web completa, projetada para auxiliar comissões técnicas no gerenciamento de um time de futebol. O sistema permite um controle detalhado sobre o elenco, finanças, desenvolvimento de jovens talentos, gestão de lesões e planejamento tático. A aplicação foi construída em Python com o microframework Bottle, seguindo a arquitetura MVC e aplicando os quatro pilares da Programação Orientada a Objetos.

---

## Funcionalidades Principais

-   **👤 Módulo de Autenticação:**
    -   Sistema seguro de cadastro e login de usuários (membros da comissão técnica).
    -   Senhas protegidas com hashing `bcrypt` através da biblioteca Passlib.
    -   Gerenciamento de sessão com cookies seguros para manter o usuário logado.
    -   Proteção de rotas, garantindo que apenas usuários autenticados possam acessar as páginas de gerenciamento.

-   **🏆 Módulo de Gerenciamento do Time:**
    -   Criação automática de um time com nome e orçamento padrão no momento do registro do usuário.
    -   Ferramentas para renomear o time, fazer upload de um escudo personalizado e gerenciar o orçamento (adicionar/remover verbas).
    -   Cálculo em tempo real da "força média" do time com base no `overall` dos jogadores do elenco.

-   **🏃‍♂️ Módulo de Gerenciamento de Jogadores:**
    -   Cadastro completo de jogadores com foto, nome, nacionalidade, idade, posição, altura, peso, overall e valor de mercado.
    -   Diferenciação entre jogadores da "Base" e "Profissionais".
    -   Funcionalidade para **promover** um jogador da base para o time profissional.
    -   Funcionalidade para **vender** jogadores, com o valor de mercado sendo automaticamente adicionado ao orçamento do time.
    -   Sistema completo para **editar** todas as informações de um jogador existente.
    -   Página de detalhes para cada jogador, exibindo sua ficha técnica completa.

-   **📋 Módulo de Gestão Tática e Médica:**
    -   Página de **Escalação** com um campo de futebol visual, permitindo ao técnico definir os 11 titulares.
    -   Seleção de **formações táticas** pré-definidas (4-4-2, 4-3-3, 4-2-3-1, etc.).
    -   Ferramenta de **auto-escalação** que sugere um time titular com base em um viés tático (ofensivo, defensivo, equilibrado).
    -   Painel de análise que calcula a força de cada setor do time (defesa, meio-campo, ataque).
    -   Sistema para registrar **lesões**, definindo o tipo e o tempo de recuperação, com o status do jogador sendo atualizado em todo o sistema.

---

## Tecnologias Utilizadas

-   **Backend:** Python 3
-   **Framework Web:** Bottle
-   **Banco de Dados:** SQLite 3
-   **Segurança:** Passlib com Bcrypt para hashing de senhas.
-   **Frontend:** HTML5, CSS3, Bootstrap 5 (para estilização e responsividade).

---

## Como Executar o Projeto

Siga os passos abaixo para configurar e rodar a aplicação em seu ambiente local.

**Pré-requisito:** Ter o Python 3.9 ou superior instalado.

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/TiagoDamaso-dev/SportManegerProVF]
    cd SportManagerPro
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    # No Windows
    python -m venv venv
    venv\Scripts\activate

    # No Linux ou macOS
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas que o projeto precisa.
    ```bash
    pip install -r requirements.txt
    ```
    
4.  **Crie o Banco de Dados Inicial:**
    Este comando irá criar o arquivo `sportmanager.db` com todas as tabelas vazias.
    ```bash
    python database.py
    ```

5.  **(Opcional) Para Resetar o Banco de Dados durante testes:**
    Este comando apaga todos os dados e recria o banco de dados limpo.
    ```bash
    python reset_db.py
    ```

6.  **Execute a Aplicação:**
    ```bash
    python main.py
    ```
    
7.  **Acesse o Sistema:**
    Abra seu navegador e acesse a página de registro para criar sua conta e seu time:
    > **http://localhost:8080/register**

---

## Aplicação dos Pilares da POO

O projeto foi construído para aplicar os 4 pilares da Programação Orientada a Objetos:

1.  **Abstração:** As classes `Jogador`, `Time` e `Usuario` são abstrações de entidades do mundo real. Elas capturam os atributos (dados) e comportamentos (métodos) essenciais para o nosso sistema, ignorando detalhes irrelevantes.

2.  **Encapsulamento:** Protegemos os dados internos dos objetos. O exemplo mais claro é o atributo `_orcamento` da classe `Time`. Ele é "protegido" e só pode ser modificado através de uma interface segura (as rotas de gerenciamento de verba ou a venda de um jogador), garantindo que as regras de negócio sejam sempre aplicadas.

3.  **Herança:** Utilizamos uma hierarquia de classes para reutilizar código e criar especializações, seguindo o princípio "é um":
    -   `Pessoa` (classe base)
    -   `Jogador` (herda de `Pessoa`)
    -   `JogadorProfissional` e `JogadorBase` (herdam de `Jogador`, especializando o tipo).

4.  **Polimorfismo:** O método `descrever_status()` existe na classe `Jogador`, mas é sobrescrito nas classes filhas `JogadorProfissional` e `JogadorBase`. Cada uma fornece sua própria implementação. Isso permite que nosso código na view (`time_view.tpl`) simplesmente chame `jogador.descrever_status()` sem precisar saber o tipo exato do objeto, e o comportamento correto é executado.

---

## Diagrama de Classes (UML)

*(**Instrução para vocês:** Usem uma ferramenta como o [draw.io](https://app.diagrams.net/), criem o diagrama seguindo o guia abaixo, salvem como uma imagem `diagrama.png` na raiz do projeto, e substituam esta linha pela imagem: `![Diagrama de Classes](diagrama.png)`)*

**Guia para criar o Diagrama:**
-   **Caixas (Classes):** Crie uma caixa para cada classe: `Pessoa`, `Jogador`, `JogadorProfissional`, `JogadorBase`, `Time`, `Usuario`.
-   **Atributos:** Dentro de cada caixa, liste os principais atributos (ex: `- nome: string`, `- idade: int`, `-_orcamento: float`).
-   **Métodos:** Liste também os principais métodos (ex: `+ get_orcamento()`, `+ descrever_status()`).
-   **Setas de Herança** (linha sólida com triângulo vazio):
    -   De `Jogador` para `Pessoa`.
    -   De `JogadorProfissional` para `Jogador`.
    -   De `JogadorBase` para `Jogador`.
-   **Linhas de Associação** (linha simples):
    -   Entre `Usuario` e `Time` (com a multiplicidade 1 -- 1, "um usuário possui um time").
    -   Entre `Time` e `Jogador` (com a multiplicidade 1 -- 0..*, "um time possui zero ou muitos jogadores").

---

## Autores

-   **Davi Gualberto Rocha**
-   **Tiago Almeida Damaso**

**Universidade de Brasília (UnB) - Faculdade do Gama (FGA)**