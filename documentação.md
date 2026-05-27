# Documentação de Requisitos: Sistema de Triagem (Protocolo de Manchester)

Este documento especifica as funcionalidades, restrições e regras de negócio para o módulo de triagem e gerenciamento de filas do hospital, baseado no briefing fornecido.

---

## 1. Briefing do Projeto

> **Cenário Atual:** *"No meu hospital, a ordem de chegada não é tudo. Quero implementar o Protocolo de Manchester. O paciente chega e a enfermeira dá uma cor: Vermelho (Emergência), Amarelo (Urgente) ou Verde (Pouco Urgente). Pacientes com mais de 60 anos sempre passam na frente do Verde, mesmo que tenham chegado depois."*

---

## 2. Requisitos Funcionais (RF)

Os requisitos funcionais determinam as ações que o sistema deve executar para que o fluxo de triagem funcione corretamente.

| ID | Requisito (O que o sistema faz) | Critério de Aceitação (Como testar) | Rastreabilidade |
| :--- | :--- | :--- | :--- |
| **RF-001** | **Atribuição de Cor na Triagem**<br>O sistema deve permitir que a enfermeira selecione uma cor de risco para o paciente: Vermelho, Amarelo ou Verde. | O sistema deve salvar a cor escolhida e impedir que o formulário seja enviado sem uma cor selecionada. | Briefing |
| **RF-002** | **Cálculo de Idade Prioritária**<br>O sistema deve calcular a idade do paciente com base na sua data de nascimento para identificar se ele tem mais de 60 anos. | Ao puxar o cadastro, se o paciente tiver $\ge 60$ anos, o sistema deve marcar internamente a tag `[Idoso: Sim]`. | Briefing |
| **RF-003** | **Ordenação Dinâmica da Fila**<br>O sistema deve organizar a fila de espera priorizando a gravidade das cores sobre a ordem de chegada. | Pacientes **Vermelhos** ficam no topo, seguidos pelos **Amarelos** e depois pelos **Verdes**. | Briefing |
| **RF-004** | **Atualização da Fila em Tempo Real**<br>O sistema deve atualizar a listagem da fila de espera automaticamente a cada nova triagem finalizada. | Ao salvar a triagem de um paciente, a tela da recepção deve atualizar a fila imediatamente sem precisar atualizar a página (`F5`). | Imagem / Briefing |
| **RF-005** | **Gestão de Tempo Limite**<br>O sistema deve monitorar há quanto tempo o paciente está esperando e emitir alertas baseados na cor. | Se um paciente Amarelo estipular o tempo limite (ex: 30 min) sem atendimento, o sistema deve destacar o nome dele em formato de alerta na tela. | Imagem / Briefing |

---

## 3. Requisitos Não Funcionais (RNF)

Os requisitos não funcionais definem as características de qualidade e restrições técnicas do sistema.

| ID | Categoria | Descrição Técnica | Critério de Sucesso |
| :--- | :--- | :--- | :--- |
| **RNF-001** | Desempenho | O sistema deve ser rápido e otimizado para **não travar na recepção**, mesmo em horários de pico. | O reordenamento da fila e a busca por pacientes devem responder em menos de 1 segundo. |
| **RNF-002** | Confiabilidade | O sistema deve possuir **tratamento de erros** de digitação ou informações erradas |

---

## 4. Regras de Negócio (RN)

As regras de negócio são as leis do hospital que o sistema é obrigado a obedecer. Elas ditam como a lógica da fila deve se comportar.

### 📌 RN-001: Sistema de Prioridade por Cores
A ordem de gravidade clínica estrita do hospital é definida por:
1. **Vermelho** (Emergência) — *Prioridade Máxima*
2. **Amarelo** (Urgente) — *Prioridade Média*
3. **Verde** (Pouco Urgente) — *Prioridade Baixa*

### 📌 RN-002: Prioridade por Idade (Fila Verde)
Pacientes com **mais de 60 anos** que receberem a cor **Verde** devem ser posicionados na fila à frente de todos os pacientes da cor **Verde** que possuem menos de 60 anos, independentemente do horário de chegada.

### 📌 RN-003: Limite da Prioridade por Idade (Não passa Emergência)
A prioridade por idade ($\ge 60$ anos) funciona **apenas dentro da sua respectiva cor (ou em categorias inferiores)**. Um idoso classificado como **Verde** nunca poderá passar na frente de nenhum paciente classificado como **Amarelo** ou **Vermelho**, garantindo que o risco clínico de morte tenha soberania sobre a idade.

### 📌 RN-004: Obrigatoriedade de Cadastro Prévio
O sistema está proibido de iniciar ou salvar o protocolo de triagem se o paciente não estiver previamente cadastrado no sistema do hospital. O vínculo pelo CPF ou número de Prontuário é obrigatório.

---
