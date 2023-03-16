# Projeto Tech News! :newspaper_roll:

Python e MongoDB foram usados na construção da aplicação que extrai dados do [_blog da Trybe_](https://blog.betrybe.com) para armazená-los em um banco de dados. O projeto foi criado com o objetivo de consultar as últimas notícias sobre tecnologia publicadas no blog, as quais são obtidas por meio de raspagem de dados. Além disso, a consulta pode ser realizada por meio de um menu interativo no ambiente virtual da aplicação.

<details>
  <summary><strong>Objetivos de prática</strong></summary><br />
    <ul>
    <li>Utilizar o terminal interativo do Python</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos</li>
    <li>Aplicar técnicas de raspagem de dados</li>
    <li>Extrair dados de conteúdo HTML</li>
    <li>Armazenar os dados obtidos em um banco de dados</li>
    </ul>
</details>
<details>
  <summary><strong>Rodando Localmente a Aplicação</strong></summary><br />
  
  <p>Para executar a aplicação e os testes, siga os passos abaixo:</p>
  <ol>
    <li>Clone o projeto.</li>
    <li>Abra o terminal e navegue até a raiz do projeto.</li>
    <li>Crie o ambiente virtual com o comando <code>python3 -m venv .venv</code>.</li>
    <li>Ative o ambiente virtual com o comando <code>source .venv/bin/activate</code>.</li>
    <li>Instale as dependências com o comando <code>python3 -m pip install -r dev-requirements.txt</code>.</li>
    <li>Para gerar os relatórios via linha de comando, instale a dependência da linha de comando com o comando <code>pip install .</code>.</li>
    <li>Utilize o comando <code>inventory_report</code> seguido dos argumentos necessários:
      <ul>
        <li>O argumento 1 deve receber o caminho de um arquivo a ser importado.</li>
        <li>O argumento 2 deve receber o formato do relatório (simples ou completo).</li>
        <li>Alternativamente, você pode utilizar o comando <code>python3 -m inventory_report.main</code> seguido dos mesmos argumentos.</li>
      </ul>
    </li>
    <li>Para executar a aplicação com Docker, execute os comandos a seguir na raiz do projeto:
      <ul>
        <li><code>docker-compose up -d</code> para subir o container.</li>
        <li><code>docker-compose down</code> para parar o container.</li>
        <li>Alternativamente, você pode rodar os testes utilizando Docker, utilize o comando <code>tech-news-analyzer</code> na raiz do projeto.</li>
      </ul>
    </li>
    <li>Para rodar a linha de comando da aplicação, execute o comando<code>python3 -m pip install -r dev-requirements.txt</code>.</li>
  </ol>
</details>
<details>
  <summary><strong>Estrutura do Projeto</strong></summary><br />

  ```
.
├── tech_news
│   ├── analyzer
│   │   ├── 🔹ratings.py
│   │   └── 🔹search_engine.py
│   ├── 🔸database.py
│   └── 🔹menu.py
│   └── 🔹scraper.py
├── tests
│   └── 🔸__init__.py
├── 🔸dev-requirements.txt
├── 🔸docker-compose.yml
├── 🔸Dockerfile
├── 🔸pyproject.toml
├── 🔹README.md
├── 🔸requirements.txt
├── 🔸setup.cfg
└── 🔸setup.py
  
    Legenda:
  🔸Arquivos de propriedade intelectual da Trybe
  🔹Arquivos desenvolvidos por mim
  ```
</details>
<!-- 
<details>
  <summary><strong>Detalhes sobre Classes Desenvolvidos</strong></summary><br />
  <p>inventory_report/reports/simple_report.py</p>
    <ul>
      <li>Classe para gerar a versão simplificada do relatório</li>
    </ul>	
  <p>inventory_report/reports/complete_report.py</p>
    <ul>
      <li>Classe para gerar a versão completa do relatório	inventory_report/reports/complete_report.py</li>
    </ul>
  <p>inventory_report/inventory/inventory.py</p>
    <ul>
      <li>Classe para gerar os relatório a partir de arquivos</li>
    </ul>
  <p>inventory_report/importer/importer.py</p>
    <ul>
      <li>Classe abstrata para aplicar o padrão de projeto Strategy</li>
    </ul>
  <p>inventory_report/inventory/inventory_iterator.py</p>
    <ul>
      <li>Refatoração da classe Inventory para aplicar o padrão de projeto Iterator</li>
    </ul>
</details>
-->
