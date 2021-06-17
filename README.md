# z-lang
## Gabriel Zezze
## gabriel@zezze.dev
<br></br>

## Contexto
A z-lang possui este nome graças ao sobrenome de seu criador (Zezze) e assim possui uma predominância de palavras com a letra “z” no início ou final dos símbolos.
<br></br>

## Inspirações e diferenciais  
A linguagem possui como maior inspiração a linguagem C mas traz elementos de Python como “and”, “or”, por fim traz suas peculiaridades nos operadores de relação escritos por extenso como por exemplo o operador de igualdade ("is equal to") e declaração de variáveis.
<br></br>

## EBNF
```
MAIN = FUNC;

STRING = "'", [ALPHACHAR], "'";
ALPHACHAR = (a | b | ... | z | A | B | ... | Z);

NUMBER = NUMERIC, { NUMERIC };
NUMERIC = (1 | 2| 3 | 4 | 5 | 6 | 7 | 8 | 9);

IDENTIFIER = ALPHACHAR, { ALPHACHAR | NUMERIC | "_" };


EOL = ".z";
TYPE = "numz" | "bool" | "charz"

FUNC = TYPE "func", IDENTIFIER, "(", { ARG }, ")", BLOCK, EOL;
ARG = TYPE, IDENTIFIER;

BLOCK = "{", [ACTION], "}";
ACTION = ( PRINT | ASSIGNMENT | WHILE | FUNC_CALL | CONDITION | RETURN )

PRINT = "zPrint", "(", (EXPRESION | COMPARISON), ")", EOL;

ASSIGNMENT = "var", IDENTIFIER, "->", TYPE, "=", (EXPRESSION | COMPARISON | NUMBER | STRING), EOL;

WHILE = "While", "(", COMPARISON, ")", BLOCK, EOL;

CONDITION = "If", ( ("(", COMPARISON, ")") | COMPARISON ), BLOCK, ( ELIF | ELSE | EOL );
ELIF = "Elif", "(", COMPARISSON, ")", BLOCK, ( ELIF | ELSE | EOL );
ELSE = "Else", BLOCK, EOL;

FUNC_CALL = IDENTIFIER, "(", (EXPRESSION), {",", (EXPRESSION)}, ")", EOL;

RETURN = "return", (EXPRESSION | COMPARISON), EOL;


EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER | "true" | "false ;

COMPARISON = EXPRESSION, ("is_equal_to", "is_not_equal_to", "is_greater_than", "is_lesser_than", "or", "and"), EXPRESSION;
```
<br></br>

## Processo de compilação
O compilador da z-lang foi feito em Python usando o pacote [sly](https://sly.readthedocs.io/en/latest/sly.html) e [llvmlite](https://pypi.org/project/llvmlite/).
O pacote sly foi usado por seus módulos de Tokenização e Parser para criar o zTokenizer e zParser, os quais respectivamente fazem a tokenização e parsing com criação da AST.

De posse da AST após o processo de parsing, é feito o processo de avaliação desta AST o qual durante é usado o pacote llvmlite para ir adicionando instruções ao arquivo “output.ll” que ao fim possui um módulo  llvm pronto para ser compilado para um arquivo “.o” usando o comando “ll” o qual finalmente pode ser compilado para um executável usando qualquer compilador de C ([clang](https://clang.llvm.org/) é recomendado).
<br></br>

## Execução de código .z

Para executar um código “.z” é necessário compila lo usando o compilador da z-lang, para executar o compilador será necessário usar o Pipenv disponível neste repositório e executar os seguintes comandos:

### Compilando código .z
```
pipenv install
pipenv run python main.py <caminho_para_arquivo_.z>
```

### Gerando o arquivo a partir do módulo llvm 
```
llc -filetype=obj out/output.ll
gcc out/output.o -o out/output  
```

### Execução do executável 
```
./out/output
```

