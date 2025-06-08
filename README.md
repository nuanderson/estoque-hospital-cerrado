Sistema de Controle de Estoque - Hospital do Cerrado
Status do Projeto: Concluído ✔️

📝 Descrição
Este é um sistema web completo para gestão de estoque, desenvolvido com o framework Django. A aplicação permite o controle total sobre o cadastro de produtos, o registro de todas as movimentações (entradas e saídas), e a geração de relatórios essenciais para auditoria e inventário físico.

O projeto foi construído do zero, cobrindo desde a modelagem do banco de dados até a criação de uma interface de usuário funcional e estilizada, incluindo a geração de documentos em PDF.

✨ Funcionalidades Principais
Gestão de Produtos:
Cadastro de novos produtos com quantidade inicial.
Listagem completa de todos os produtos com seu estoque atual.
Exclusão de produtos com tela de confirmação.
Controle de Movimentações:
Registro de entradas e saídas para cada produto.
Atualização automática da quantidade em estoque após cada movimento.
Validação para impedir saídas de produtos com estoque insuficiente.
Relatórios Profissionais:
Relatório de Balanço: Gera uma lista de todos os produtos em ordem alfabética, com uma coluna em branco para "Contagem Física", ideal para inventários.
Geração de PDF: Permite baixar o relatório de balanço em um arquivo PDF, personalizado com a logo da instituição.
Relatório de Histórico: Exibe um registro completo de todas as movimentações já realizadas, ordenadas por data, permitindo uma auditoria completa do fluxo de estoque.
Interface:
Design limpo e consistente em todas as páginas.
Layout estilizado com base na identidade visual da instituição.
🛠️ Tecnologias Utilizadas
Backend:
Python
Django
Frontend:
HTML5
CSS3
Banco de Dados:
SQLite3 (padrão do Django para desenvolvimento)
Geração de PDF:
xhtml2pdf
Controle de Versão:
Git & GitHub
🚀 Como Executar o Projeto Localmente
Siga os passos abaixo para rodar o projeto em sua máquina.

Clone o repositório:
Bash

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
Navegue até o diretório do projeto:
Bash

cd sistema-estoque-django
Crie e ative um ambiente virtual:
Bash

# Criar o ambiente
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Mac/Linux
source venv/bin/activate
Crie o arquivo requirements.txt: (Este comando lista todas as bibliotecas que usamos e salva em um arquivo, tornando a instalação mais fácil para outros)
Bash

pip freeze > requirements.txt
Instale as dependências:
Bash

pip install -r requirements.txt
Aplique as migrações do banco de dados:
Bash

python manage.py migrate
Inicie o servidor de desenvolvimento:
Bash

python manage.py runserver
Abra seu navegador e acesse http://127.0.0.1:8000/ para ver a aplicação funcionando.
🖼️ Screenshots
(Aqui você pode adicionar as imagens que me enviou para mostrar como o sistema ficou!)

Página Principal (Lista de Produtos)

Página de Relatório de Balanço

Relatório em PDF Gerado

👨‍💻 Autor
Desenvolvido por Nuanderson Nunes.