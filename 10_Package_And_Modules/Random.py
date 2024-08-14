from random import random
from random import randint

"""

O módulo `random` em Python é utilizado para gerar números aleatórios e realizar várias operações 
relacionadas a aleatoriedade:

### 1. `random()`
- **Descrição**: Gera um número de ponto flutuante aleatório entre 0.0 e 1.0.
- **Uso**: `random.random()`
- **Exemplo**: 
  ```python
  import random
  num = random.random()
  print(num)  # Saída: um número aleatório entre 0.0 e 1.0, como 0.37444887175646646
  ```

### 2. `uniform(a, b)`
- **Descrição**: Gera um número de ponto flutuante aleatório entre `a` e `b` (inclusive).
- **Uso**: `random.uniform(a, b)`
- **Exemplo**:
  ```python
  import random
  num = random.uniform(1, 10)
  print(num)  # Saída: um número aleatório entre 1 e 10, como 7.582348304620376
  ```

### 3. `randint(a, b)`
- **Descrição**: Gera um número inteiro aleatório entre `a` e `b` (inclusive).
- **Uso**: `random.randint(a, b)`
- **Exemplo**:
  ```python
  import random
  num = random.randint(1, 10)
  print(num)  # Saída: um número inteiro aleatório entre 1 e 10, como 4
  ```

Essas funções são úteis para várias aplicações, como simulações, jogos, e amostragens aleatórias. 
É importante lembrar que, por padrão, o módulo `random` utiliza um gerador de números pseudo-aleatórios, 
o que significa que os números são gerados por algoritmos determinísticos, mas ainda assim parecem aleatórios.

Claro! A função `shuffle` do módulo `random` é usada para embaralhar aleatoriamente os elementos de uma lista. Ela modifica a lista original in-place e não retorna uma nova lista. Aqui está um resumo detalhado da função `shuffle`:

### `shuffle(x[, random])`
- **Descrição**: Embaralha aleatoriamente os itens da lista `x` no local, ou seja, altera a ordem dos elementos na própria lista. Não retorna uma nova lista, mas modifica a lista original.
- **Uso**: `random.shuffle(x[, random])`
  - `x`: A lista a ser embaralhada.
  - `random` (opcional): Uma função de gerador de números aleatórios que pode ser passada para controle adicional sobre a aleatoriedade. Se não for fornecida, `random.shuffle` usará o gerador de números aleatórios padrão do módulo `random`.

### Exemplo
```python
import random

# Lista de exemplo
numeros = [1, 2, 3, 4, 5]

# Embaralha a lista
random.shuffle(numeros)

print(numeros)  # Saída: a lista embaralhada, como [3, 1, 4, 5, 2]
```

### Detalhes Importantes
- **Modificação In-Place**: A função modifica a lista original em vez de criar uma nova lista.
- **Não Retorna Nada**: O valor de retorno de `shuffle` é `None`. A função realiza a operação de embaralhamento diretamente na lista fornecida.
- **Uso de `random` Opcional**: Você pode passar uma função personalizada de gerador de números aleatórios se desejar um controle mais específico sobre o processo de embaralhamento. Se não passar um gerador, o padrão será utilizado.

### Exemplo com Gerador Personalizado
```python
import random

# Lista de exemplo
numeros = [1, 2, 3, 4, 5]

# Função de gerador personalizado (por exemplo, sempre retorna o mesmo valor para testes)
def meu_gerador():
    return 0.5

# Embaralha a lista usando um gerador personalizado
random.shuffle(numeros, random=meu_gerador)

print(numeros)  # Saída: a lista embaralhada de acordo com o gerador personalizado

A função `shuffle` é especialmente útil em situações onde você precisa embaralhar os itens de uma lista,
como em jogos, sorteios ou quando deseja uma ordem aleatória para processamento.


"""

def impares(x):
    return x


print(impares([1, 2, 3, 4, 5, 6, 6]))
