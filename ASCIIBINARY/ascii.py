ascii_table = [
    chr(i) for i in range(32, 127)
]
def asencode():
    code = input("Me diga o codigo em Dec: ")
    code += " "
    codearray = []
    tempo = ""
    final = ""
    for i in code:
        if i.isdigit():
            tempo += i
        else:
            codearray.append(tempo)
            tempo = ""
            codearray.append(i)
    arr = []
    for i in codearray:
        if i.isdigit():
            i = int(i)
            arr.append(i)
        else: 
            arr.append(i)
    for i in arr:
        try:
            final += (ascii_table[int(i)])
        except ValueError:
            final += i
    print(f"Result: {final}")
    input("")
def asdecode():
    phrase = input("Me diga uma frase: ")
    final = ""
    for i in phrase:
        final += str(ascii_table.index(i))
        final += " "
    print(f"Result: {final}")
    input("")
# print(ascii_table)
