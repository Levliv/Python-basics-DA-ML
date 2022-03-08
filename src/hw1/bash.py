def head(filename = "first.txt", lines = 10):
    if (line < 0):
        raise RuntimeError("Number of lines must be positive")
    with open(filename, 'rt') as file:
        file_head = [file.readline() for i in range(lines)]
    print(''.join(file_head))

def tail(filename = "first.txt", lines = 10):
    if (line < 0):
        raise RuntimeError("Number of lines must be positive")
    with open(filename, 'rt') as file:
        file_backward = [line for line in reversed(file.readlines())]
        file_backward[0]+='\n'
        file_backward[-1] = file_backward[-1][0:-1]
        print(''.join(file_backward[:lines]))

def nl(filename = "first.txt"):
    with open(filename, 'rt') as file:
        lines = [ line[0:-1] for line in file.readlines()]
        rows = [str(i) for i in range(len(lines))]
        numbered_lines = list(zip(rows, lines))
        list(map(lambda x: print(' '.join(x)), numbered_lines))

def wc(filename = "first.txt"):
    with open(filename, 'rt') as file:
        number_lines = len(file.readlines())
        file.seek(0)
        file_text = file.read()
        words = 0
        for symbol in file_text:
            if (symbol == ' ') | (symbol == '\n'):
                words+=1
        
        print(f"lines = {number_lines}")
        print(f"words = {words}")
        print(f"symbols = {len(file_text)}")
        
