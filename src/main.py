"""Aplicação CLI TaskTracker — Bootcamp II, Fase 2."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

ARQUIVO_DADOS = Path(__file__).resolve().parent.parent / "tarefas.json"
PRIORIDADES = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}
STATUS_VALIDOS = {"Pendente", "Concluída"}


def carregar_tarefas() -> list[dict[str, str]]:
    """Carrega tarefas salvas. Arquivo ausente ou inválido inicia lista vazia."""
    try:
        with ARQUIVO_DADOS.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        if not isinstance(dados, list):
            raise ValueError("O conteúdo salvo não é uma lista.")
        return [t for t in dados if isinstance(t, dict) and tarefa_valida(t)]
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, OSError, ValueError) as erro:
        print(f"Aviso: não foi possível carregar os dados ({erro}). Iniciando lista vazia.")
        return []


def salvar_tarefas(tarefas: list[dict[str, str]]) -> None:
    """Persiste a lista de tarefas em JSON legível."""
    try:
        with ARQUIVO_DADOS.open("w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)
    except OSError as erro:
        print(f"Erro ao salvar tarefas: {erro}")


def tarefa_valida(tarefa: dict[str, Any]) -> bool:
    """Verifica se um registro carregado contém campos e valores permitidos."""
    try:
        datetime.strptime(tarefa["data_limite"], "%d/%m/%Y")
        return (
            bool(str(tarefa["titulo"]).strip())
            and str(tarefa["prioridade"]) in {"Alta", "Média", "Baixa"}
            and str(tarefa["status"]) in STATUS_VALIDOS
        )
    except (KeyError, TypeError, ValueError):
        return False


def obter_titulo() -> str:
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório. Informe um título válido.")


def obter_prioridade() -> str:
    while True:
        entrada = input("Prioridade (Alta/Média/Baixa): ").strip().casefold()
        if entrada in PRIORIDADES:
            return PRIORIDADES[entrada]
        print("Erro: prioridade inválida. Escolha Alta, Média ou Baixa.")


def obter_data_limite() -> str:
    while True:
        entrada = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(entrada, "%d/%m/%Y")
            if data.strftime("%d/%m/%Y") != entrada:
                raise ValueError
            return entrada
        except ValueError:
            print("Erro: data inválida. Use uma data existente no formato DD/MM/AAAA.")


def tarefa_duplicada(nova: dict[str, str], tarefas: list[dict[str, str]]) -> bool:
    """Detecta duplicata comparando título, descrição, prioridade e data."""
    campos = ("titulo", "descricao", "prioridade", "data_limite")
    return any(
        all(t.get(campo, "").strip().casefold() == nova[campo].strip().casefold() for campo in campos)
        for t in tarefas
    )


def cadastrar_tarefa(tarefas: list[dict[str, str]]) -> None:
    print("\n--- Cadastro de tarefa ---")
    nova = {
        "titulo": obter_titulo(),
        "descricao": input("Descrição (opcional): ").strip(),
        "prioridade": obter_prioridade(),
        "data_limite": obter_data_limite(),
        "status": "Pendente",
    }
    if tarefa_duplicada(nova, tarefas):
        print("Erro: já existe uma tarefa com as mesmas informações principais.")
        return
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    print("Tarefa cadastrada com sucesso! Status inicial: Pendente.")


def visualizar_tarefas(tarefas: list[dict[str, str]]) -> None:
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa foi cadastrada até o momento.")
    else:
        for indice, tarefa in enumerate(tarefas, start=1):
            print(f"\n{indice}. {tarefa['titulo']}")
            print(f"   Descrição: {tarefa['descricao'] or '—'}")
            print(f"   Prioridade: {tarefa['prioridade']}")
            print(f"   Data limite: {tarefa['data_limite']}")
            print(f"   Status: {tarefa['status']}")
    pendentes = sum(t["status"] == "Pendente" for t in tarefas)
    concluidas = sum(t["status"] == "Concluída" for t in tarefas)
    print(f"\nTotal: {len(tarefas)} | Pendentes: {pendentes} | Concluídas: {concluidas}")


def concluir_tarefa(tarefas: list[dict[str, str]]) -> None:
    pendentes = [(i, tarefa) for i, tarefa in enumerate(tarefas) if tarefa["status"] == "Pendente"]
    if not pendentes:
        print("Não há tarefas pendentes para concluir.")
        return
    print("\n--- Tarefas pendentes ---")
    for indice, tarefa in pendentes:
        print(f"{indice + 1}. {tarefa['titulo']} (limite: {tarefa['data_limite']})")
    while True:
        escolha = input("Digite o número da tarefa que deseja concluir (0 para cancelar): ").strip()
        if escolha == "0":
            print("Operação cancelada.")
            return
        try:
            numero = int(escolha)
            indice = numero - 1
            if 0 <= indice < len(tarefas) and tarefas[indice]["status"] == "Pendente":
                tarefas[indice]["status"] = "Concluída"
                salvar_tarefas(tarefas)
                print(f"Tarefa '{tarefas[indice]['titulo']}' concluída com sucesso!")
                return
            print("Erro: número inválido ou tarefa já concluída. Tente novamente.")
        except ValueError:
            print("Erro: informe um número válido.")


def exibir_menu() -> None:
    print("\n=== TaskTracker ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Concluir tarefa")
    print("4. Sair da aplicação")


def main() -> None:
    tarefas = carregar_tarefas()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            print("Até logo! Suas tarefas foram mantidas no arquivo local.")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nAplicação encerrada pelo usuário.")
