import re

def tokenize_line(line):


    patterns = [
        (r'(?P<identificador>[a-zA-Z_]\w*)', 'identificador'),
        (r'(?P<flotante>-?\d+\.\d+)', 'flotante'),
        (r'(?P<entero>-?\d+)', 'entero'),
        (r'(?P<real>-?\d+\.\d+E[-+]?\d+)', 'real'),
        (r'(?P<cadena>".*?")', 'cadena'),
        (r'(?P<para>for)', 'para'),
        (r'(?P<si>if)', 'si'),
        (r'(?P<si_no>else)', 'si_no'),
        (r'(?P<mientras>while)', 'mientras'),
        (r'(?P<definir>def)', 'definir'),
        (r'(?P<retornar>return)', 'retornar'),
        (r'(?P<comentario>//.*$)', 'comentario'),
        (r'(?P<Suma>\+)', 'Suma'),
        (r'(?P<Resta>-)', 'Resta'),
        (r'(?P<Multiplicacion>\*)', 'Multiplicacion'),
        (r'(?P<Division>/)', 'Division'),
        (r'(?P<Exponenciacion>\^)', 'Exponenciacion'),
        (r'(?P<Asignacion>=)', 'Asignacion'),
        (r'(?P<MenorQue><)', 'MenorQue'),
        (r'(?P<MayorQue>>)', 'MayorQue'),
        (r'(?P<MenorIgualQue><=)', 'MenorIgualQue'),
        (r'(?P<MayorIgualQue>>=)', 'MayorIgualQue'),
        (r'(?P<DiferenteQue>!=)', 'DiferenteQue'),
        (r'(?P<ParentesisIzquierdo>\()', 'ParentesisIzquierdo'),
        (r'(?P<ParentesisDerecho>\))', 'ParentesisDerecho'),
        (r'(?P<LlaveIzquierda>{)', 'LlaveIzquierda'),
        (r'(?P<LlaveDerecha>})', 'LlaveDerecha'),
        (r'(?P<CorcheteIzquierdo>\[)', 'CorcheteIzquierdo'),
        (r'(?P<CorcheteDerecho>\])', 'CorcheteDerecho'),
    ]

    tokens = []

    # Buscar coincidencias de patrones en la línea especificada y agregar tokens
    for patterns, token_type in patterns:
        matches = re.finditer(patterns, line)
        for match in matches:
            tokens.append((match.group(), token_type))

    return tokens

def main():
    file_path = "file.txt"
    print("Attempting to open file:", file_path)
    try:
        with open(file_path, 'r') as file:
            print("File opened successfully")
            for line in file:
                tokens = tokenize_line(line)
                # Imprimir los lexemas y sus tipos
                for lexeme, token_type in tokens:
                    print(f"{lexeme.strip()} {token_type}")
    except FileNotFoundError:
        print("El archivo especificado no se encontró.")

if __name__ == "__main__":
    main()