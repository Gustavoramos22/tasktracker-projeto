# TaskTracker

Aplicação de linha de comando para organizar tarefas do dia a dia. O projeto implementa a etapa intermediária do Bootcamp II a partir do planejamento lógico da Fase 1.

## Funcionalidades

- Cadastrar tarefas com título, descrição, prioridade e data limite.
- Validar título obrigatório, prioridade (`Alta`, `Média` ou `Baixa`) e data no formato `DD/MM/AAAA`.
- Evitar tarefas duplicadas com as mesmas informações principais.
- Listar tarefas e exibir contagens de tarefas totais, pendentes e concluídas.
- Concluir tarefas pendentes.
- Salvar os dados localmente em `tarefas.json` para manter as alterações entre execuções.

## Tecnologias

- Python 3.10 ou superior
- Biblioteca padrão do Python (`json`, `datetime`, `pathlib`)
- Git e GitHub para versionamento

## Estrutura

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Instalação e execução

Não há dependências externas. Com Python 3 instalado, execute na raiz do repositório:

```bash
python3 src/main.py
```

A data limite deve ser informada como `DD/MM/AAAA`. O arquivo `tarefas.json` será criado automaticamente na raiz após o primeiro cadastro ou alteração.

## Uso

No menu, escolha uma opção para cadastrar ou listar tarefas, concluir uma tarefa ou encerrar o programa. Prioridade aceita: `Alta`, `Média` ou `Baixa`.

## Versionamento

O histórico de desenvolvimento é organizado em commits incrementais. Para publicar em uma conta GitHub, crie um repositório remoto vazio e associe-o, por exemplo:

```bash
git remote add origin https://github.com/SEU-USUARIO/tasktracker-projeto.git
git push -u origin main
```

## Vídeo demonstrativo (Fase 2)

Grave em formato horizontal 16:9, com duração de 5 minutos, mostrando o repositório/histórico, execução do programa, rejeição de dados inválidos, cadastro válido e listagem atualizada. O vídeo deve seguir os requisitos da atividade e ser publicado como Público ou Não Listado no YouTube.

## Planejamento da Fase 1

O documento original está em [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf).
