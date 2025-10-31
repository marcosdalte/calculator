# 🧮 Calculadora GUI

Uma calculadora gráfica simples e intuitiva desenvolvida em Python usando a biblioteca Tkinter.

## 📋 Descrição

Esta aplicação fornece uma interface gráfica amigável para realizar operações matemáticas básicas. Com um design limpo e responsivo, a calculadora oferece todas as funcionalidades essenciais em uma interface familiar e fácil de usar.

## ✨ Funcionalidades

- ➕ **Operações básicas**: Adição, subtração, multiplicação e divisão
- 🔢 **Suporte a decimais**: Trabalha com números inteiros e decimais
- 🔢 **Números negativos**: Suporte completo a números negativos
- 📐 **Parênteses**: Suporte a expressões com parênteses para ordem de operações
- 🧹 **Botão limpar**: Remove toda a expressão com um clique
- 📱 **Interface responsiva**: Layout que se adapta ao redimensionamento
- ⚡ **Avaliação segura**: Calcula expressões matemáticas sem vulnerabilidades de segurança
- 🎨 **Design intuitivo**: Interface familiar semelhante a calculadoras físicas
- 🛡️ **Segurança**: Implementação segura sem uso de `eval()`, protegida contra execução de código malicioso

## 🚀 Como usar

### Pré-requisitos

- Python 3.6 ou superior
- Tkinter (geralmente incluído na instalação padrão do Python)

### Instalação e Execução

1. **Clone ou baixe o projeto**:
   ```bash
   git clone <url-do-repositorio>
   cd calculadora
   ```

2. **Execute a aplicação**:
   ```bash
   python calculadora.py
   ```

### Interface

```
┌─────────────────────────────┐
│        [Display]            │
├─────────────────────────────┤
│  7  │  8  │  9  │    /     │
├─────┼─────┼─────┼──────────┤
│  4  │  5  │  6  │    *     │
├─────┼─────┼─────┼──────────┤
│  1  │  2  │  3  │    -     │
├─────┼─────┼─────┼──────────┤
│  0  │  .  │  =  │    +     │
├─────┴─────┴─────┴──────────┤
│           C (Limpar)        │
└─────────────────────────────┘
```

## 🔧 Estrutura do Código

### Classe Principal

```python
class Calculadora(tk.Tk):
    def __init__(self):                      # Inicialização da janela
    def _criar_widgets(self):                # Criação da interface
    def adicionar(self, valor):              # Adiciona caracteres ao display
    def limpar(self):                        # Limpa o display
    def calcular(self):                      # Executa o cálculo seguro
    def _avaliar_expressao_segura(self):     # Parser seguro de expressões
    def _calcular_tokens(self):              # Algoritmo Shunting Yard
```

### Arquitetura de Segurança

O código implementa múltiplas camadas de segurança:

1. **Validação de Entrada**: Regex para aceitar apenas caracteres matemáticos
2. **Tokenização**: Divisão da expressão em tokens válidos
3. **Análise Sintática**: Verificação de parênteses balanceados e operadores válidos
4. **Conversão Segura**: Algoritmo Shunting Yard para infix→postfix
5. **Avaliação Controlada**: Cálculo usando stack sem `eval()`

### Componentes

- **Display**: Campo de entrada que mostra números e operações
- **Botões numéricos**: 0-9 para entrada de números
- **Botões de operação**: +, -, *, / para operações matemáticas
- **Botão decimal**: . para números decimais
- **Botão igual**: = para executar o cálculo
- **Botão limpar**: C para resetar a calculadora

### Algoritmo de Segurança

A calculadora utiliza um **parser matemático seguro** que:

- ✅ **Valida entrada**: Aceita apenas caracteres matemáticos válidos (números, operadores, parênteses)
- ✅ **Shunting Yard**: Implementa o algoritmo Shunting Yard para conversão infix→postfix
- ✅ **Avaliação controlada**: Calcula expressões sem executar código arbitrário
- ✅ **Tratamento de erros**: Gerencia divisão por zero e expressões inválidas
- ✅ **Suporte a precedência**: Respeita a ordem matemática de operações
- ✅ **Parênteses balanceados**: Verifica e processa parênteses corretamente

## ✅ Segurança e Confiabilidade

### 🛡️ Correções de Segurança Implementadas

**RESOLVIDO**: A versão atual **NÃO** utiliza mais a função `eval()` que representava um risco crítico de segurança.

### ✅ Implementação Segura:

- **Parser Matemático Próprio**: Implementação customizada para avaliar expressões
- **Validação Rigorosa**: Aceita apenas caracteres matemáticos válidos
- **Proteção contra Injeção**: Impossibilita execução de código malicioso
- **Algoritmo Shunting Yard**: Conversão segura de notação infix para postfix
- **Controle de Precedência**: Respeita ordem matemática de operações

### 🧪 Casos de Teste de Segurança:

```python
# ✅ Expressões válidas que funcionam:
"2+3*4"           # = 14
"(2+3)*4"         # = 20  
"10/2-1"          # = 4
"-5+3"            # = -2

# ❌ Tentativas maliciosas que são bloqueadas:
"__import__('os').system('dir')"    # Erro: caracteres inválidos
"exec('print(1)')"                  # Erro: caracteres inválidos
"eval('2+2')"                       # Erro: caracteres inválidos
```

## 🛠️ Melhorias Futuras

- [x] ✅ **Substituir `eval()` por parser seguro** - CONCLUÍDO
- [x] ✅ **Implementar suporte a parênteses** - CONCLUÍDO  
- [x] ✅ **Adicionar suporte a números negativos** - CONCLUÍDO
- [ ] Adicionar histórico de cálculos
- [ ] Implementar operações avançadas (%, √, potência)
- [ ] Suporte a atalhos de teclado
- [ ] Temas personalizáveis
- [ ] Modo científico
- [ ] Exportar histórico
- [ ] Suporte a constantes matemáticas (π, e)

## 🐛 Problemas Conhecidos

### ✅ Resolvidos:
- [x] **Segurança**: ~~Uso de `eval()` pode executar código malicioso~~ - **CORRIGIDO**
- [x] **Validação**: ~~Entrada não validada pode causar erros inesperados~~ - **CORRIGIDO**
- [x] **Parênteses**: ~~Limitado a operações sem parênteses~~ - **CORRIGIDO**

### 🔄 Em Monitoramento:
- **Precisão**: Limitação de ponto flutuante em cálculos muito complexos
- **Interface**: Redimensionamento em telas muito pequenas
- **Performance**: Expressões extremamente longas podem ser lentas

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE` para detalhes.

## � Changelog

### Versão 2.0 - Segurança e Funcionalidades Aprimoradas

#### 🛡️ Correções de Segurança:
- **CRÍTICO**: Removido uso perigoso de `eval()` 
- **NOVO**: Implementado parser matemático seguro próprio
- **NOVO**: Validação rigorosa de entrada com regex
- **NOVO**: Proteção completa contra injeção de código

#### ✨ Novas Funcionalidades:
- **NOVO**: Suporte completo a parênteses `(2+3)*4`
- **NOVO**: Suporte a números negativos `-5+3`
- **NOVO**: Algoritmo Shunting Yard para precedência de operadores
- **NOVO**: Tratamento de erros mais específico e amigável
- **NOVO**: Formatação automática de resultados (remove casas decimais desnecessárias)

#### 🔧 Melhorias Técnicas:
- **MELHORIA**: Código mais modular e organizado
- **MELHORIA**: Comentários e documentação aprimorados
- **MELHORIA**: Validação de parênteses balanceados
- **MELHORIA**: Controle de precedência matemática

### Versão 1.0 - Versão Inicial
- Interface básica da calculadora
- Operações matemáticas simples
- Layout responsivo

## �📞 Suporte

Se você encontrar problemas ou tiver sugestões:

- Abra uma [issue](../../issues) no GitHub
- Entre em contato através do email: [seu-email@exemplo.com]

## 🏆 Créditos

Desenvolvido com ❤️ usando Python e Tkinter.

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!**