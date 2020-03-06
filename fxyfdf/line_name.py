
'''
下划线
双下划线

'''

class TestA:
  def _method(self): #能在类外面直接调用
    print('I am a private function.')
  def method(self):
    return self._method()
ca = TestA()
ca.method()
ca._method()

print("test class tow line ")
class TestA:
  def __method(self):
    print('This is a method from class TestA')
  def method(self):
    return self.__method()
class TestB(TestA):
  def __method(self):
    print('This is a method from calss TestB')
ca = TestA()
cb = TestB()
ca.method()
cb.method()
#ca.__method()
ca._TestA__method()


class TestB(TestA):
  def __method(self):
    print('This is a method from calss TestB')
  def method(self):
    return self.__method()
cb = TestB()
cb.method()