# 🧮 Calculadora GUI

Uma calculadora gráfica simples e intuitiva desenvolvida em Python usando a biblioteca Tkinter.

## 📋 Descrição

Esta aplicação fornece uma interface gráfica amigável para realizar operações matemáticas básicas. Com um design limpo e responsivo, a calculadora oferece todas as funcionalidades essenciais em uma interface familiar e fácil de usar.

## ✨ Funcionalidades

- ➕ **Operações básicas**: Adição, subtração, multiplicação e divisão
- 🔢 **Suporte a decimais**: Trabalha com números inteiros e decimais
- 🧹 **Botão limpar**: Remove toda a expressão com um clique
- 📱 **Interface responsiva**: Layout que se adapta ao redimensionamento
- ⚡ **Avaliação em tempo real**: Calcula expressões matemáticas instantaneamente
- 🎨 **Design intuitivo**: Interface familiar semelhante a calculadoras físicas

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
    def __init__(self):           # Inicialização da janela
    def _criar_widgets(self):     # Criação da interface
    def adicionar(self, valor):   # Adiciona caracteres ao display
    def limpar(self):            # Limpa o display
    def calcular(self):          # Executa o cálculo
```

### Componentes

- **Display**: Campo de entrada que mostra números e operações
- **Botões numéricos**: 0-9 para entrada de números
- **Botões de operação**: +, -, *, / para operações matemáticas
- **Botão decimal**: . para números decimais
- **Botão igual**: = para executar o cálculo
- **Botão limpar**: C para resetar a calculadora

## ⚠️ Considerações de Segurança

**IMPORTANTE**: A versão atual utiliza a função `eval()` para avaliar expressões matemáticas, o que pode representar um risco de segurança em ambientes de produção. 

### Recomendações:

- Use apenas para fins educacionais ou desenvolvimento local
- Para uso em produção, substitua `eval()` por um parser seguro
- Considere usar bibliotecas como `simpleeval` ou implementar um parser personalizado

## 🛠️ Melhorias Futuras

- [ ] Substituir `eval()` por parser seguro
- [ ] Adicionar histórico de cálculos
- [ ] Implementar suporte a parênteses
- [ ] Adicionar operações avançadas (%, √, potência)
- [ ] Suporte a atalhos de teclado
- [ ] Temas personalizáveis
- [ ] Modo científico
- [ ] Exportar histórico

## 🐛 Problemas Conhecidos

1. **Segurança**: Uso de `eval()` pode executar código malicioso
2. **Validação**: Entrada não validada pode causar erros inesperados
3. **Expressões complexas**: Limitado a operações básicas

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE` para detalhes.

## 📞 Suporte

Se você encontrar problemas ou tiver sugestões:

- Abra uma [issue](../../issues) no GitHub
- Entre em contato através do email: [seu-email@exemplo.com]

## 🏆 Créditos

Desenvolvido com ❤️ usando Python e Tkinter.

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!**