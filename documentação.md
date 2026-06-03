# Documentação de Requisitos: Sistema HealthManager (Triagem Hospitalar)

Este documento especifica as funcionalidades, restrições e regras de negócio para o módulo de triagem e gerenciamento de filas do hospital, baseado no briefing fornecido.

---

### 1. Propósito
Otimizar o tempo de espera e o fluxo de atendimento de pacientes hospitalares através de um gerenciamento inteligente e automatizado de filas de prioridade.

### 1.2 Briefing do Projeto

> **Cenário Atual:** *"No meu hospital, a ordem de chegada não é tudo. Quero implementar o Protocolo de Manchester. O paciente chega e a enfermeira dá uma cor: Vermelho (Emergência), Amarelo (Urgente) ou Verde (Pouco Urgente). Pacientes com mais de 60 anos sempre passam na frente do Verde, mesmo que tenham chegado depois."*

### 1.3 Definições e Acrônimos
- **RF**: Requisito Funcional (O que o sistema deve fazer)
- **RNF**: Requisito Não-Funcional (Características de qualidade e restrições técnicas)
- **RN**: Regra de Negócio (As leis do hospital que determinam o comportamento do sistema)
- **CLI**: *Command Line Interface* (Interface de Linha de Comando / Terminal)

---

## 2. Requisitos Funcionais (RF)

Os requisitos funcionais determinam as ações diretas que o sistema executa para que o fluxo de triagem funcione corretamente via CLI.

| ID | Requisito (O que o sistema faz) | Critério de Aceitação (Como testar) | Rastreabilidade |
| :--- | :--- | :--- | :--- |
| **RF-001** | **Atribuição de Cor na Triagem**<br>O sistema deve permitir que a enfermeira selecione a classificação de risco através de um menu numérico: [1] Vermelho, [2] Amarelo ou [3] Verde. | Ao digitar a opção da cor, o sistema deve associar o nome correto da classificação ao cadastro do paciente. | Briefing |
| **RF-002** | **Coleta e Verificação de Idade**<br>O sistema deve coletar a idade atual do paciente para identificar se ele pertence ao grupo prioritário de idosos ($\ge 60$ anos). | Ao inserir a idade, se o value for igual ou maior que 60, o sistema deve acionar a lógica de peso prioritário para a fila Verde. | Briefing |
| **RF-003** | **Ordenação Automática da Fila**<br>O sistema deve organizar a fila de espera priorizando a gravidade das cores e usando a ordem de chegada como critério de desempate definitivo. | Pacientes **Vermelhos** devem ficar no topo, seguidos por **Amarelos**, **Verdes Idosos** e, por fim, **Verdes Comuns**. | Briefing / RN-001 / RN-002 |
| **RF-004** | **Exibição Estruturada da Fila**<br>O sistema deve listar os pacientes aguardando de forma legível, quebrando as linhas para cada registro individual. | A listagem não pode exibir blocos de texto brutos (como listas de tuplas/listas nativas). Deve exibir: Posição, Nome, Cor, Idade e Sintomas linha por linha. | Análise Técnica |
| **RF-005** | **Chamada de Paciente (Consumo da Fila)**<br>O sistema deve permitir chamar o próximo paciente do topo, exibindo seus dados na tela e removendo-o da fila de espera. | Ao acionar a chamada, o paciente da posição `0` deve ser exibido com destaque e o comando `.pop(0)` deve retirá-lo da memória. | Análise Técnica |

---

## 3. Requisitos Não Funcionais (RNF)

Os requisitos não funcionais definem os critérios de qualidade, estabilidade e restrições técnicas do software.

| ID | Categoria | Descrição Técnica | Critério de Sucesso |
| :--- | :--- | :--- | :--- |
| **RNF-001** | Desempenho | O sistema deve ser rápido e otimizado para **não travar na recepção**, mesmo em horários de alta rotatividade. | A inserção e a reordenação da lista através do método `.sort()` em memória devem responder em menos de 0.5 segundos. |
| **RNF-002** | Confiabilidade | O sistema deve possuir **tratamento de erros** de digitação para impedir que dados inválidos quebrem a execução do terminal. | Caso a enfermeira digite letras no campo de idade ou opções inexistentes no menu de cores, o sistema deve exibir um alerta e impedir o fechamento inesperado do programa. |
| **RNF-003** | Persistência Temporal | A lista de pacientes deve ser mantida viva enquanto o programa estiver em execução. | O retorno ao menu principal através do laço `while True` não pode resetar ou apagar a lista `fila_hospitalar`. |

---

## 4. Regras de Negócio (RN)

As regras de negócio são as diretrizes de triagem médica que a lógica do código é obrigada a obedecer.

### 📌 RN-001: Sistema de Prioridade por Cores (Manchester)
A ordem de gravidade clínica estrita do hospital para fins de ordenação numérica do sistema é definida por pesos:
1. **Vermelho** (Emergência) — *Peso 1*
2. **Amarelo** (Urgente) — *Peso 2*
3. **Verde** (Pouco Urgente) — *Peso 3*

### 📌 RN-002: Prioridade por Idade na Fila Verde
Pacientes com **60 anos ou mais** que receberem a classificação **Verde** devem receber um peso intermediário (*Peso 2.5*). Isso faz com que eles sejam posicionados automaticamente à frente de todos os pacientes **Verdes Comuns** (Peso 3), independentemente de quem chegou primeiro.

### 📌 RN-003: Soberania Clínica (Limite da Prioridade por Idade)
A prioridade por idade funciona apenas como critério de desempate interno na cor Verde. Um idoso classificado como **Verde** (Peso 2.5) **nunca** poderá passar na frente de nenhum paciente classificado como **Amarelo** (Peso 2) ou **Vermelho** (Peso 1), garantindo que o risco clínico de morte tenha soberania sobre a idade.

### 📌 RN-004: Ordem de Chegada para Pacientes do Mesmo Nível
Caso dois pacientes possuam exatamente o mesmo peso de prioridade (ex: dois pacientes Amarelos), o sistema manterá o posicionamento baseado na ordem cronológica de inserção na lista.