# Sistema de Controle de Estoque - Hospital do Cerrado

![Logo do Hospital do Cerrado](/img/logo.png)

> **Status do Projeto:** Concluído ✔️

## 📝 Descrição

Este é um sistema web completo para gestão de estoque, desenvolvido com o framework Django. A aplicação permite o controle total sobre o cadastro de produtos, o registro de todas as movimentações (entradas e saídas), e a geração de relatórios essenciais para auditoria e inventário físico.

O projeto foi construído do zero, cobrindo desde a modelagem do banco de dados até a criação de uma interface de usuário funcional e estilizada, incluindo a geração de documentos em PDF.

## ✨ Funcionalidades Principais

-   **Gestão de Produtos:**
    -   Cadastro de novos produtos com quantidade inicial.
    -   Listagem completa de todos os produtos com seu estoque atual.
    -   Exclusão de produtos com tela de confirmação.
-   **Controle de Movimentações:**
    -   Registro de entradas e saídas para cada produto.
    -   Atualização automática do estoque após cada movimento.
    -   Validação para impedir saídas de produtos com estoque insuficiente.
-   **Relatórios Profissionais:**
    -   **Relatório de Balanço:** Gera uma lista de todos os produtos em ordem alfabética, com uma coluna em branco para "Contagem Física", ideal para inventários.
    -   **Geração de PDF:** Permite baixar o relatório de balanço em um arquivo PDF, personalizado com a logo da instituição.
    -   **Relatório de Histórico:** Exibe um registro completo de todas as movimentações já realizadas, ordenadas por data, permitindo uma auditoria completa do fluxo de estoque.
-   **Interface:**
    -   Design limpo e consistente em todas as páginas.
    -   Layout estilizado com base na identidade visual da instituição.

## 🛠️ Tecnologias Utilizadas

-   **Backend:**
    -   [Python](https://www.python.org/)
    -   [Django](https://www.djangoproject.com/)
-   **Frontend:**
    -   HTML5
    -   CSS3
-   **Banco de Dados:**
    -   SQLite3 (padrão do Django para desenvolvimento)
-   **Geração de PDF:**
    -   `xhtml2pdf`
-   **Controle de Versão:**
    -   Git & GitHub

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o projeto em sua máquina.

1.  **Clone o repositório:**
    *(Substitua SEU_USUARIO e SEU_REPOSITORIO pelos seus dados)*
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd NOME_DA_PASTA_DO_PROJETO
    ```
3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv
    # Ativar no Windows
    venv\Scripts\activate
    # Ativar no Mac/Linux
    source venv/bin/activate
    ```
4.  **Crie o arquivo `requirements.txt`:**
    *(Este comando lista todas as bibliotecas que usamos no projeto. É essencial para que outras pessoas possam instalar as mesmas dependências.)*
    ```bash
    pip freeze > requirements.txt
    ```
5.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
6.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```
7.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
8.  Abra seu navegador e acesse `http://127.0.0.1:8000/` para ver a aplicação funcionando.

## 🖼️ Screenshots

Página Principal (Lista de Produtos)
![alt text](/img/image.png)

Página de Relatório de Balanço
![alt text](/img/image-1.png)

PDF gerado
![alt text](/img/image-2.png)

Página de Histórico de Movimentações
![alt text](/img/image-3.png)

## 👨‍💻 Autor

Desenvolvido por **[Nuanderson Nunes]**.

---
