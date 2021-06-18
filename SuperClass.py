class Super:
	def method(self):
		print('in Super.method')
		
class Super:
	def method(self):
		print('in Super.method')
	def delegate(self):
		self.action()
		
class Inheritor(Super):
	pass
    
class Replaser(Super):
	def method(self):
		print('in Replaser.method')
		
class Extender(Super):
	def method(self):
		print('starting Extender.method')
		Super.method(self)
		print('ending Extender.method')

class Provider(Super):
	def action(self):
		print('in Provider.action')
if __name__ == '__main__':
    for klass in (Inheritor, Replaser, Extender):
        print('\n' + klass.__name__+'...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()

X.data1, X.__dict__['data1']







