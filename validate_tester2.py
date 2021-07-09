# Файл validate_tester2.py

from validate_tester import loadclass
CardHolder = loadclass()

bob = CardHolder('12345-5678', 'Bob Smith', 40, '123 main st')
print('bob:', bob.name, bob.acct, sue.age, sue.addr)

print('bob:', bob.name, bob.acct, bob.age, bob.addr)
      
