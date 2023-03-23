class User:
    name = 'Иван'

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


a = User()
a.set_name('Виктория')

print(a.name)
