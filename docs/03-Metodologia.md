
# Metodologia

<span style="color:red">Pré-requisitos: <a href="02-Especificacao.md"> Especificação do projeto</a></span>

O desenvolvimento do projeto seguirá uma abordagem ágil, garantindo flexibilidade para adaptação às mudanças de requisitos e otimização do processo de desenvolvimento. A equipe utilizará práticas de Scrum para organização das tarefas, garantindo entregas incrementais e contínuas.
## Relação de ambientes de trabalho

| Ambiente   | Plataforma | Link de Acesso
| :----         |    :----         |    :----   |
| Desenvolvimento        | VS Code + GitHub | 
| Backend        | Python   | 
| Frontend        | HTML, CSS, JS |           |
| Banco de Dados        | Tembo  |  https://cloud.tembo.io/  |
| Gerenciamento         | Trello   |  https://trello.com/b/jXlkngHO/controle-de-energia  |

Além disso, o ambiente de desenvolvimento será configurado localmente antes da implantação em servidores de teste ou produção.

## Controle de versão

A ferramenta de controle de versão adotada no projeto foi o [Git](https://git-scm.com/), sendo que o [GitHub](https://github.com) foi utilizado para hospedagem do repositório.

O projeto segue a seguinte convenção para o nome de branches:

- `main`: versão estável já testada do software
- `unstable`: versão já testada do software, porém instável
- `testing`: versão em testes do software
- `dev`: versão de desenvolvimento do software

Quanto à gerência de issues, o projeto adota a seguinte convenção para etiquetas:

- `documentation`: melhorias ou acréscimos à documentação
- `bug`: uma funcionalidade encontra-se com problemas
- `enhancement`: uma funcionalidade precisa ser melhorada
- `feature`: uma nova funcionalidade precisa ser introduzida

Discuta como a configuração do projeto foi feita na ferramenta de versionamento escolhida. Exponha como a gestão de tags, merges, commits e branches é realizada. Discuta também como a gestão de issues foi feita.


## Planejamento do projeto

###  Divisão de papéis

#### Sprint 1
- _Scrum master_: Matheus
- Diagramas: Maciel
- Protótipos: Felipe
- Documentação: Luis

#### Sprint 2
- _Scrum master_: Matheus
- Desenvolvedor _front-end_: Luis/Portela
- Desenvolvedor _back-end_: Matheus/Luis
- Banco de dados: Maciel
- Prototipos: Portela
- Diagramas: Luis/Maciel 

###  Quadro de tarefas

#### Sprint 1

Atualizado em: 21/04/2024

| Responsável   | Tarefa/Requisito | Iniciado em    | Prazo      | Status | Terminado em    |
| :----         |    :----         |      :----:    | :----:     | :----: | :----:          |
| Matheus        | Contexto | 01/02/2025     | 17/03/2025 | ✔️    | 19/03/2025      |
| Maciel        | Especificação    | 03/02/2025     | 17/03/2025 | ✔️    |  20/03/2025               |
| Luis        | Metodologia  | 01/01/2025     | 17/03/2025 | ✔️     |  20/03/2025                |


#### Sprint 2

Atualizado em: 21/03/2024

| Responsável   | Tarefa/Requisito | Iniciado em    | Prazo      | Status | Terminado em    |
| :----         |    :----         |      :----:    | :----:     | :----: | :----:          |
| Felipe Portela        | Desing do Site   | 19/03/2025     | 28/04/2025 | 📝    |       |
| Gabriel Maciel        | Tabelas dos Bancos de Dados    | 21/04/2025     | 28/04/2025 | 📝   |                 |
| Matheus Felipe      | Coleta de Bibliotecas e APIs  | 21/03/2025     | 28/04/2025 | 📝     |                 |
| Matheus Felipe        | Script de login  |  01/04/2025    | 28/04/2025 | 📝    |       |


Legenda:
- ✔️: terminado
- 📝: em execução
- ⌛: atrasado
- ❌: não iniciado


### Processo

O grupo adotará o framework Scrum para gerenciar o desenvolvimento do projeto. A implementação seguirá as seguintes diretrizes:

- Sprints: O projeto será desenvolvido em ciclos de trabalho curtos, com entregas incrementais.

- Backlog do Produto: As tarefas serão organizadas em um backlog priorizado, garantindo que as atividades mais importantes sejam executadas primeiro.

- Weekly Meetings: Reuniões Semanais para atualização do andamento das tarefas e identificação de bloqueios.

- Review e Retrospectiva: Ao final de cada sprint, será realizada uma revisão para validar entregas e uma retrospectiva para melhorias contínuas.

- Quadros do Trello: O grupo estara se organizando atreves do Trello.
 

### Ferramentas

Liste todas as ferramentas que foram empregadas no projeto, justificando a escolha delas, sempre que possível.

Exemplo: os artefatos do projeto são desenvolvidos a partir de diversas plataformas e a relação dos ambientes com seu respectivo propósito é apresentada na tabela que se segue.

| Ambiente                            | Plataforma                         | Link de acesso                         |
|-------------------------------------|------------------------------------|----------------------------------------|
| Repositório de código fonte         | GitHub                             | http://....                            |
| Documentos do projeto               | GitHub                             | http://....                            |
| Projeto de interface                | Figma                              | http://....                            |
| Gerenciamento do projeto            | GitHub Projects                    | http://....                            |
| Hospedagem                          | Vercel                             | http://....                            |
 
