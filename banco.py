import random
print ('-- BANCO --')
finalizado = False
dinheiro = random.randint(100, 1000)

def verstatus():
    print('Você atualmente tem R$' + str(dinheiro) + '.00 em sua conta.')
verstatus()

def saque(a):
  global dinheiro
  dinheiro -= a
  verstatus()

def deposito(a):
  global dinheiro
  dinheiro += a
  verstatus()

escolha = None
def opcoes():
 print(f'''
 -- Opções --
 [1] Saque
 [2] Depósito
 [3] Ver status
 [4] Sair do banco
 ''')
 escolha = int(input('Digite o número da ação que você deseja realizar: '))
 if escolha == 1:
  saque(int(input('Digite o valor que você deseja sacar: ')))
 elif escolha == 2:
      deposito(int(input('Digite o valor que você deseja depositar: ')))
 elif escolha == 3:
      verstatus()
 elif escolha == 4:
      print('Você saiu do banco.')
      global finalizado
      finalizado = True

while finalizado == False:
    opcoes()
