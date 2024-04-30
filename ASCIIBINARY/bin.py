def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
def binencode():
    phrase = input("")
def bindecode():
    result = 0
    bin = input("Me fala o codigo em binário: \n")
    bin = reverse(bin)
    o = 1
    for i in bin:
        if i == "1":
            result += o
        o = o * 2
    print(f"Result: {result}")
    input("")