"""
Um módulo é basicamente um arquivo Python (.py) que contém definições de funções, classes e variáveis. Quando você
 grupa vários módulos em um diretório e inclui um arquivo especial chamado __init__.py, você cria um pacote.

Aqui estão alguns pontos importantes sobre pacotes em Python:

Estrutura de Diretórios: Um pacote é geralmente uma estrutura de diretórios com um arquivo __init__.py dentro. E
ste arquivo pode estar vazio, mas sua presença indica que o diretório deve ser tratado como um pacote.

EX.

mypackage/
├── __init__.py
├── module1.py
└── module2.py

Importação de Pacotes: Você pode importar módulos ou subpacotes de um pacote usando a sintaxe import ou from ...
import .... Por exemplo, se você tem um pacote chamado mypackage e um módulo dentro dele chamado module1, você
pode importá-lo assim:

import mypackage.module1

Ou, se você deseja importar uma função específica do módulo:

EX1.
from mypackage.module1 import minha_funcao

EX.2
from mypackage.subpackage import module3

3 - Pacotes de Terceiros: Além dos pacotes que você cria, há muitos pacotes desenvolvidos por terceiros que você pode
instalar e usar. O Python Package Index (PyPI) é o repositório onde esses pacotes estão disponíveis. Para instalar
pacotes de terceiros, você geralmente usa o pip, que é o gerenciador de pacotes do Python.

pip install



"""