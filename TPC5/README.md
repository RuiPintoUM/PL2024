**Explicação do Código:**

Este código Python simula uma máquina de vending. Aqui está uma visão geral do funcionamento:

1. **Importações e Tokens:**
   - Usa `ply.lex` para análise léxica.
   - Define tokens como `LISTAR`, `MOEDA`, `SELECIONAR`, `ID`, `VALOR` e `SAIR`.

2. **Inicialização:**
   - `produtos`: Dicionário dos produtos disponíveis.
   - `saldo`: Armazena saldo do usuário.

3. **Funcionalidades:**
   - `adicionar_moeda`: Adiciona valor ao saldo.
   - `listar_produtos`: Mostra produtos disponíveis.
   - `selecionar_produto`: Verifica se há saldo e produto disponível para compra.
   
4. **Processamento de Entrada:**
   - `processar_entrada`: Analisa entrada do usuário e executa operações correspondentes.

5. **Loop Principal:**
   - O usuário interage digitando comandos.
   - Cada comando é processado.
   - O loop termina quando o usuário digita 'SAIR'.
