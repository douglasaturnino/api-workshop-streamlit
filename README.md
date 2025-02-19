## Dashboard

O objetivo dessa aplicação é criar um dashboard para visualização dos produtos do nosso banco.
Queremos fazer uma apliação end to end que vai desde a coleta/cadastro dos dados (API) até a visualização dos mesmos.

# Objetivo

O objetivo desse é mostrar como é possível fazer o deploy de vários tipos de produtos de dados, passando desde a etapa de especificação até a fase de deploy.
Fazem parte dessa solução:

[FastAPI](https://github.com/douglasaturnino/api-workshop-fastapi)
[Streamlit](https://github.com/douglasaturnino/api-workshop-streamlit)

# Projetos

Os projetos se emcontram nas paginas abaixo

[FastAPI](https://api-workshop-yekz.onrender.com/docs)
[Streamlit](https://api-workshop-dso.streamlit.app/)

# Criando nosso ambiente virtual

Ambientes virtuais são uma ferramenta para manter as dependências necessárias para diferentes projetos em locais separados, evitando problemas de compatibilidade. Neste projeto estamos utilizando o como gerenciador de ambiente o [UV da astral](https://docs.astral.sh/uv/getting-started/features/).

```bash
uv sync
```

Com essa comando caso não tenho a versão `3.12.8` instalado o uv irá instalar a versão.

# Ativando nosso ambiente virtual

Para ativar o ambiente virtual utilizando o uv é igual a utilização do pip nesse caso será:

```bash
source .venv/bin/activate
```
# Executando o servidor

Para executar o servidor, precisamos usar o streamlit e passar o nome do arquivo.

```bash
streamlit run src/main.py
```
