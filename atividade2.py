def printDecimal(c=0):
    print(f'   {(int(c))}', end=" ")

def printOctal(c):
    print(f"     {(oct(c)[2:])}", end=" ")

def printHexadecimal(c):
    print(f"       {(hex(c)[2:]).upper()}", end=" ")


def printBinario(c):
    print(f"        {(bin(c)[2:])}", end=" ")

def imprimirTabela():
  print("Decimal Octal Hexadecimal Binário")
  print("------- ----- ----------- -------")
  for c in range(256):
      printDecimal(c),
      printOctal(c),
      printHexadecimal(c),
      printBinario(c),
      print("\n")

imprimirTabela()