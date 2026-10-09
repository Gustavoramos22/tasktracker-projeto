# TaskTracker

O **TaskTracker** é uma aplicação de linha de comando desenvolvida em Python para apoiar a organização de tarefas do dia a dia. Este projeto corresponde à Fase 2 do Bootcamp II e transforma em código o planejamento lógico elaborado na Fase 1.

## Objetivo

Oferecer uma forma simples de registrar atividades, acompanhar suas informações principais e identificar tarefas pendentes ou concluídas.

## Funcionalidades implementadas

- **Cadastro de tarefas** com título, descrição, prioridade, data limite e status.

- **Validação do título**, que é obrigatório e não pode conter apenas espaços.

- **Validação da prioridade**, aceitando `Alta`, `Média` ou `Baixa`; variações de maiúsculas e minúsculas são normalizadas.

- **Validação da data limite**, exigindo uma data existente no formato `DD/MM/AAAA`.

- **Prevenção de duplicatas**, comparando título, descrição, prioridade e data limite.

- **Listagem de tarefas**, exibindo os campos de cada registro e os totais de tarefas, pendentes e concluídas.

- **Conclusão de tarefas**, alterando o status de uma tarefa pendente para `Concluída`.

- **Persistência local**, mantendo os registros em um arquivo JSON entre execuções.

- **Menu contínuo**, com opções para cadastrar, visualizar, concluir tarefas e encerrar a aplicação.

## Regras de negócio

Toda tarefa cadastrada recebe inicialmente o status `Pendente`. O título não pode ficar vazio, a prioridade deve pertencer às opções permitidas e a data precisa ser válida. O programa também impede a inclusão de uma tarefa quando já existe outra com o mesmo título, descrição, prioridade e data limite.

## Tecnologias e implementação

- **Python 3** e bibliotecas padrão (`json`, `datetime` e `pathlib`).

- **Git** para controle de versão do desenvolvimento.

- Armazenamento local dos dados em JSON, sem dependências externas.

## Organização do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

- `src/main.py`: implementação da aplicação, incluindo menu, validações, operações sobre tarefas e persistência.

- `docs/planejamento_logico.pdf`: planejamento lógico e arquitetural produzido na Fase 1.

- `.gitignore`: regras para excluir arquivos temporários do Python, ambientes virtuais e o arquivo local `tarefas.json` do controle de versão.

## Escopo atual

O TaskTracker é uma aplicação local, baseada em terminal e destinada a um único usuário. A versão atual permite cadastrar, consultar e concluir tarefas. Não inclui edição ou exclusão de registros, sincronização entre dispositivos, interface gráfica nem testes automatizados.
