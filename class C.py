class C:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other
X = C()
print(X > 'ham')
print(X < 'ham')


