#Entrada de dados!
operaçao = input("digite a operação desejada: (+, -, *, /)")
num1 = float(input("digite o primeiro numero:"))
num2 = float(input("digite o segundo numero:"))

#Processamento de dados!
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao =  num1 / num2

#Saida de dados!
if operaçao == "+":
  print("o resultado da sua equação é:", soma)
elif operaçao == "-":
  print("o resultado da sua equação é:", subtracao)
elif operaçao == "*":
  print("o resultado da sua equação é:", multiplicacao)
elif operaçao == "/":
  print("o resultado da sua equação é:", divisao)
else: print("operação invalida")