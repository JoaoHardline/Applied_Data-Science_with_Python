# hashtag para comentarios em python
#def para definir uma funcao em python
def add_Numbers(x, y, z = None):
    if z == None:
        return print(x + y)
    
    else:
        return print(x + y + z)
    

print("\nDigite o valor de x: ")
x = int(input())
print("\nDigite o valor de y:")
y = int(input()) 

add_Numbers(x, y)