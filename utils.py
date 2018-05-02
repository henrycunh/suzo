import sys



# Imprime e dá flush no stdout
def printSh(string):
      sys.stdout.write(string)
      sys.stdout.flush()

# Limpa uma string que pode ser uma tupla
def clear_str(string):
    s = string
    try:
        s = eval(string)
        return s
    except:
        return s