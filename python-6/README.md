# Desafio de programação orientada a objetos

   
Uma pequena empresa em crescimento precisa de uma modelagem de dados dinâmica! que permita a expansão de seus usuários e departamentos, e que matenha ou melhore a segurança, padrões e boas práticas, refatore o código proposto.
    
- [x]  Proteja a classe `Employee` para não ser instânciada diretamente.
- [x]  Torne obrigatório a implementação dos métodos da classe `Employee`, implemente-os se for necessários.
- [x]  Proteja o atributo `department` da classe `Manager` para que seja acessado somente através do método `get_department`.
- [x]  Faça a correção dos métodos para que a herança funcione corretamente.
- [x]  Proteja o atributo `sales` da classe `Seller` para que não seja acessado diretamente,
- [x]  crie um método chamado `get_sales` para retornar o valor do atributo e `put_sales` para acrescentar valores a esse atributo, lembrando que as vendas são acumulativas
- [x]  Implemente o método `get_department` que retorna o nome do departamento e `set_department` que muda o nome do departamento para as classes `Manager` e `Seller`
- [x]  Padronize uma carga horária de 8 horas para todos os funcionários.
- [x]  O cálculo do metodo `calc_bonus` do Vendedor dever ser calculado pelo total de suas vendas vezes 0.15



## Tópicos

Neste desafio você vai aprender:

- [x]  Funções e Classes
- Herança
- Composição
- Métodos de classe
- Métodos de Instância
- Métodos estáticos

## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`