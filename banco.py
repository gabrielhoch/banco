class Conta:
  def_init_(self,titular,saldo,senha):
      self.titular = titular
      self.saldo = saldo
      self.senha = senha
  #metodos

# metodo saque
def Sacar(self,valor):
  if self.saldo >= valor:
    self.saldo = self.saldo - valor
else:
  print("Vocẽ não em saldo , seu POBRE!")

