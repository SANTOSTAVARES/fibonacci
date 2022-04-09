x = 0
y = 1
def fibonacci(primeiro_numero, segundo_numero):
    sequencia = [primeiro_numero, segundo_numero]
    while True:
        sequencia.append(sequencia[-2] + sequencia[-1])
        if sequencia.__len__() > 100:
            break 
    return sequencia
