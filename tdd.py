################################################################################
# Capitulo 1                                                                   # 
################################################################################
#
#
#
#import unittest
#
#class Dollar:
#    def __init__(self, amount: int):
#        self.amount = amount
#
#    def times(self, multiplier: int) -> None:
#        self.amount *= multiplier
#
#class TestDolar(unittest.TestCase):
#
#    def testMultiplication(self):
#        five = Dollar(5)
#        five.times(2) 
#        self.assertEqual(10, five.amount)
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 2                                                                   # 
################################################################################
#
#
#
#
#import unittest
#
#class Dollar:
#    def __init__(self, amount: int):
#        self.amount: int = amount
#
#    def times(self, multiplier: int) -> None:
#        self.amount *= multiplier
#
#    def get_amount(self) -> float:
#        return self.amount
#
#    def set_amount(self, new_amount: int) -> None:
#        self.amount = new_amount
#
#class TestDolar(unittest.TestCase):
#
#    def testMultiplication(self):
#        five = Dollar(5)
#        five.times(2) 
#        self.assertEqual(10, five.amount)
#        five.set_amount(5)
#        five.times(3) 
#        self.assertEqual(15, five.amount)
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 3                                                                   # 
################################################################################
#
#
#
#import unittest
#
#class Dollar:
#    def __init__(self, amount: int):
#        self.amount: int = amount
#
#    def times(self, multiplier: int) -> None:
#        self.amount *= multiplier
#
#    def equals(self, obj1: Dollar):
#        dollar = obj1
#        return self.amount == dollar.get_amount()
#
#    def get_amount(self) -> float:
#        return self.amount
#
#    def set_amount(self, new_amount: int) -> None:
#        self.amount = new_amount
#
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self):
#        five = Dollar(5)
#        five.times(2) 
#        self.assertEqual(10, five.amount)
#        five.set_amount(5)
#        five.times(3) 
#        self.assertEqual(15, five.amount)
#
#    def test_equality(self):
#        self.assertTrue(Dollar(5).equals(Dollar(5)))
#        self.assertFalse(Dollar(5).equals(Dollar(6)))
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 4                                                                   # 
################################################################################
#
#
#
#import unittest
#
#class Dollar:
#    def __init__(self, amount: int):
#        self.amount: int = amount
#
#    def times(self, multiplier: int) -> None:
#        self.amount *= multiplier
#
#    def equals(self, obj1: Dollar):
#        dollar = obj1
#        return self.amount == dollar.get_amount()
#
#    def get_amount(self) -> float:
#        return self.amount
#
#    def set_amount(self, new_amount: int) -> None:
#        self.amount = new_amount
#
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self):
#        five = Dollar(5)
#        five.times(2) 
#        self.assertEqual(10, five.amount)
#        five.set_amount(5)
#        five.times(3) 
#        self.assertEqual(15, five.amount)
#
#    def test_equality(self):
#        self.assertTrue(Dollar(5).equals(Dollar(5)))
#        self.assertFalse(Dollar(5).equals(Dollar(6)))
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 5                                                                   # 
################################################################################
#
#
#
#import unittest
#
#class Dollar(object):
#    def __init__(self, amount: int):
#        self.amount: int = amount
#
#    def times(self, multiplier: int) -> None:
#        self.amount *= multiplier
#
#    def equals(self, obj1: Dollar):
#        dollar = obj1
#        return self.amount == dollar.get_amount()
#
#    def get_amount(self) -> float:
#        return self.amount
#
#    def set_amount(self, new_amount: int) -> None:
#        self.amount = new_amount
#
#class Franc(object):
#
#    __amount: int
#
#    def __init__(self, amount: int) -> None:
#        self.amount: int = amount
#
#    def times(self, multiplier: int) -> Franc:
#        return Franc(self.amount * multiplier)
#
#    def equals(self, obj1: object) -> Franc:
#        franc: Franc = obj1 
#        return self.amount == franc.amount
#
#
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self):
#        five = Dollar(5)
#        five.times(2) 
#        self.assertEqual(10, five.amount)
#        five.set_amount(5)
#        five.times(3) 
#        self.assertEqual(15, five.amount)
#
#    def test_franc_multiplication(self):
#        five = Franc(5)
#        self.assertEqual(10, five.times(2))
#        self.assertEqual(15, five.times(3))
#
#
#    def test_equality(self):
#        self.assertTrue(Dollar(5).equals(Dollar(5)))
#        self.assertFalse(Dollar(5).equals(Dollar(6)))
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 6                                                                   # 
################################################################################
#
#
#
#import unittest
#class Money:
#    __amount: int
#
#class Dollar(Money):
#    def __init__(self, amount: int):
#        self.amount: int = amount
#
#    def times(self, multiplier: int) -> None:
#        self.amount *= multiplier
#
#    def equals(self, obj1: Dollar):
#        dollar = obj1
#        return self.amount == dollar.get_amount()
#
#    def get_amount(self) -> float:
#        return self.amount
#
#    def set_amount(self, new_amount: int) -> None:
#        self.amount = new_amount
#
#class Franc(Money):
#    def __init__(self, amount: int) -> None:
#        self.amount: int = amount
#
#    def times(self, multiplier: int) -> Franc:
#        return self.amount * multiplier
#
#    def equals(self, obj1: object) -> Franc:
#        franc: Franc = obj1 
#        return self.amount == franc.amount
#
#
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self):
#        five = Dollar(5)
#        five.times(2) 
#        self.assertEqual(10, five.amount)
#        five.set_amount(5)
#        five.times(3) 
#        self.assertEqual(15, five.amount)
#
#    def test_franc_multiplication(self):
#        five = Franc(5)
#        self.assertEqual(10, five.times(2))
#        self.assertEqual(15, five.times(3))
#
#    def test_equality(self):
#        self.assertTrue(Dollar(5).equals(Dollar(5)))
#        self.assertFalse(Dollar(5).equals(Dollar(6)))
#        self.assertTrue(Franc(5).equals(Franc(5)))
#        self.assertFalse(Franc(5).equals(Franc(6)))
#
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 7                                                                   # 
################################################################################
#
#
#
#import unittest
#class Money:
#    __amount: int
#
#    def equals(self, obj1: Dollar):
#        dollar = obj1
#        return self.amount == dollar.amount
#
#
#class Dollar(Money):
#    def __init__(self, amount: int):
#        self.amount: int = amount
#
#    def times(self, multiplier: int) -> None:
#        self.amount *= multiplier
#
#    def get_amount(self) -> float:
#        return self.amount
#
#    def set_amount(self, new_amount: int) -> None:
#        self.amount = new_amount
#
#class Franc(Money):
#    def __init__(self, amount: int) -> None:
#        self.amount: int = amount
#
#    def times(self, multiplier: int) -> Franc:
#        return self.amount * multiplier
#
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self):
#        five = Dollar(5)
#        five.times(2) 
#        self.assertEqual(10, five.amount)
#        five.set_amount(5)
#        five.times(3) 
#        self.assertEqual(15, five.amount)
#
#    def test_franc_multiplication(self):
#        five = Franc(5)
#        self.assertEqual(10, five.times(2))
#        self.assertEqual(15, five.times(3))
#
#    def test_equality(self):
#        self.assertTrue(Dollar(5).equals(Dollar(5)))
#        self.assertFalse(Dollar(5).equals(Dollar(6)))
#        self.assertTrue(Franc(5).equals(Franc(5)))
#        self.assertFalse(Franc(5).equals(Franc(6)))
#        self.assertFalse(Franc(5).equals(Dollar(6)))
#
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 8                                                                   # 
################################################################################
#
#
#
#import unittest
#class Money:
#    __amount: int
#
#    def equals(self, obj1: Dollar):
#        dollar = obj1
#        return self.amount == dollar.amount
#
#    def times(self, multiplier: int) -> object:
#        self.amount *= multiplier
#        return self.amount
#
#    def set_amount(self, new_amount: int) -> None:
#        self.amount = new_amount
#
#
#class Dollar(Money):
#    def __init__(self, amount: int):
#        self.amount: int = amount
#
#    def get_amount(self) -> float:
#        return self.amount
#
#class Franc(Money):
#    def __init__(self, amount: int) -> None:
#        self.amount: int = amount
#
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self):
#        five = Dollar(5)
#        five.times(2) 
#        self.assertEqual(10, five.amount)
#        five.set_amount(5)
#        five.times(3) 
#        self.assertEqual(15, five.amount)
#
#    def test_franc_multiplication(self):
#        five = Franc(5)
#        self.assertEqual(10, five.times(2))
#        five.set_amount(5)
#        self.assertEqual(15, five.times(3))
#
#    def test_equality(self):
#        self.assertTrue(Dollar(5).equals(Dollar(5)))
#        self.assertFalse(Dollar(5).equals(Dollar(6)))
#        self.assertTrue(Franc(5).equals(Franc(5)))
#        self.assertFalse(Franc(5).equals(Franc(6)))
#        self.assertFalse(Franc(5).equals(Dollar(6)))
#
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 9                                                                   # 
################################################################################
#
#
#
#import unittest
#from abc import ABC, abstractmethod
#
#
#class Money(ABC):
#    __amount: int
#
#    def equals(self, obj1: Dollar):
#        dollar = obj1
#        return self.amount == dollar.amount
#
#    def times(self, multiplier: int) -> object:
#        self.amount *= multiplier
#        return self.amount
#
#    @abstractmethod
#    def currency(self) -> str:...
#
#    def set_amount(self, new_amount: int) -> None:
#        self.amount = new_amount
#
#    def get_amount(self) -> float:
#        return self.amount
#
#
#class Dollar(Money):
#    def __init__(self, amount: int):
#        self.amount: int = amount
#
#    def currency(self) -> str:
#        return 'USD'
#
#class Franc(Money):
#    def __init__(self, amount: int) -> None:
#        self.amount: int = amount
#
#    def currency(self) -> str:
#        return 'CHF'
#
#
## TESTS
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self) -> None:
#        five = Dollar(5)
#        five.times(2) 
#        self.assertEqual(10, five.amount)
#        five.set_amount(5)
#        five.times(3) 
#        self.assertEqual(15, five.amount)
#
#    def test_franc_multiplication(self) -> None:
#        five = Franc(5)
#        self.assertEqual(10, five.times(2))
#        five.set_amount(5)
#        self.assertEqual(15, five.times(3))
#
#    def test_equality(self) -> None:
#        self.assertTrue(Dollar(5).equals(Dollar(5)))
#        self.assertFalse(Dollar(5).equals(Dollar(6)))
#        self.assertTrue(Franc(5).equals(Franc(5)))
#        self.assertFalse(Franc(5).equals(Franc(6)))
#        self.assertFalse(Franc(5).equals(Dollar(6)))
#
#    def test_currency(self) -> None:
#        self.assertEqual("USD", Dollar(1).currency())
#        self.assertEqual("CHF", Franc(1).currency())
#
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
################################################################################
# Capitulo 10                                                                  # 
################################################################################
#
#
#
#import unittest
#from abc import ABC, abstractmethod
#
#
#class Money(ABC):
#    __amount: int
#
#    def equals(self, obj1: Dollar):
#        dollar = obj1
#        return self.amount == dollar.amount
#
#    def times(self, multiplier: int) -> object:
#        self.amount *= multiplier
#        return self.amount
#
#    @abstractmethod
#    def currency(self) -> str:...
#
#    def set_amount(self, new_amount: int) -> None:
#        self.amount = new_amount
#
#    def get_amount(self) -> float:
#        return self.amount
#
#
#class Dollar(Money):
#    def __init__(self, amount: int, currencyy: str = "USD"):
#        self.amount:    int = amount
#        self.currencyy: str = currencyy 
#
#
#    def currency(self) -> str:
#        return self.currencyy
#
#class Franc(Money):
#    def __init__(self, amount: int, currencyy: str = "CHF"):
#        self.amount:    int = amount
#        self.currencyy: str = currencyy 
#
#    def currency(self) -> str:
#        return self.currencyy
#
#
## TESTS
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self) -> None:
#        five = Dollar(5)
#        five.times(2) 
#        self.assertEqual(10, five.amount)
#        five.set_amount(5)
#        five.times(3) 
#        self.assertEqual(15, five.amount)
#
#    def test_franc_multiplication(self) -> None:
#        five = Franc(5)
#        self.assertEqual(10, five.times(2))
#        five.set_amount(5)
#        self.assertEqual(15, five.times(3))
#
#    def test_equality(self) -> None:
#        self.assertTrue(Dollar(5).equals(Dollar(5)))
#        self.assertFalse(Dollar(5).equals(Dollar(6)))
#        self.assertTrue(Franc(5).equals(Franc(5)))
#        self.assertFalse(Franc(5).equals(Franc(6)))
#        self.assertFalse(Franc(5).equals(Dollar(6)))
#
#    def test_currency(self) -> None:
#        self.assertEqual("USD", Dollar(1).currency())
#        self.assertEqual("CHF", Franc(1).currency())
#
#    def test_different_class_equality() -> None:
#        self.assertTrue(Money)
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 11                                                                  # 
################################################################################
#
#
#
#import unittest
#from abc import ABC, abstractmethod
#
#
#class Money(ABC):
#    _amount: int
#
#    def __init__(self, amount: int, currencyy: str):
#        self._amount:    int = amount
#        self.currencyy: str = currencyy 
#
#
#    def equals(self, valor: int):
#        return self._amount == valor 
#
#    def times(self, multiplier: int) -> object:
#        self._amount *= multiplier
#        return self._amount
#
#    def currency(self) -> str:
#        return self.currencyy
#
#    def set_amount(self, new_amount: int) -> None:
#        self._amount = new_amount
#
#    def get_amount(self) -> float:
#        return self._amount
#
## TESTS
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self) -> None:
#        m1 = Money(5, "USD")
#        m1.times(2) 
#        self.assertEqual(10, m1._amount)
#        m1.set_amount(5)
#        m1.times(3) 
#        self.assertEqual(15, m1._amount)
#
#    def test_equality(self) -> None:
#        self.assertTrue(Money(5, "USD").equals(5))
#
#    def test_currency(self) -> None:
#        self.assertEqual("USD", Money(1, "USD").currency())
#        self.assertEqual("CHF", Money(1, "CHF").currency())
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
#
################################################################################
# Capitulo 12                                                                  # 
################################################################################
#
#
#
#import unittest
#from abc import ABC, abstractmethod
#
#
#class Money(ABC):
#    _amount: int
#
#    def __init__(self, amount: int, currencyy: str):
#        self._amount:    int = amount
#        self.currencyy: str = currencyy 
#
#
#    def equals(self, valor: int):
#        return self._amount == valor 
#
#    def times(self, multiplier: int) -> object:
#        self._amount *= multiplier
#        return self._amount
#
#    def currency(self) -> str:
#        return self.currencyy
#
#    def plus(self, number: int) -> int:
#        return self._amount + number 
#
#    def set_amount(self, new_amount: int) -> None:
#        self._amount = new_amount
#
#    def get_amount(self) -> int:
#        return self._amount
#
## TESTS
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self) -> None:
#        m1 = Money(5, "USD")
#        m1.times(2) 
#        self.assertEqual(10, m1._amount)
#        m1.set_amount(5)
#        m1.times(3) 
#        self.assertEqual(15, m1._amount)
#
#    def test_equality(self) -> None:
#        self.assertTrue(Money(5, "USD").equals(5))
#
#    def test_currency(self) -> None:
#        self.assertEqual("USD", Money(1, "USD").currency())
#        self.assertEqual("CHF", Money(1, "CHF").currency())
#
#    def test_simple_addition(self) -> None:
#        summ = Money(5,"USD").plus(Money(5,"USD").get_amount())
#        self.assertEqual(Money(10,"USD").get_amount(), summ)
#
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 13                                                                  # 
################################################################################
#
#
#
#import unittest
#from abc import ABC, abstractmethod
#
#class Money(ABC):
#    _amount: int
#
#    def __init__(self, amount: int, currencyy: str):
#        self._amount:    int = amount
#        self.currencyy: str = currencyy 
#
#    def equals(self, valor: int):
#        return self._amount == valor 
#
#    def times(self, multiplier: int) -> object:
#        self._amount *= multiplier
#        return self._amount
#
#    def add(self, number: int) -> None :
#        self._amount += number 
#
#    def currency(self) -> str:
#        return self.currencyy
#
#    def plus(self, number: int) -> int:
#        return self._amount + number 
#
#    def set_amount(self, new_amount: int) -> None:
#        self._amount: int = new_amount
#
#    def get_amount(self) -> int:
#        return self._amount
#
#
## TESTS
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self) -> None:
#        m1 = Money(5, "USD")
#        m1.times(2) 
#        self.assertEqual(10, m1._amount)
#        m1.set_amount(5)
#        m1.times(3) 
#        self.assertEqual(15, m1._amount)
#
#    def test_equality(self) -> None:
#        self.assertTrue(Money(5, "USD").equals(5))
#
#    def test_currency(self) -> None:
#        self.assertEqual("USD", Money(1, "USD").currency())
#        self.assertEqual("CHF", Money(1, "CHF").currency())
#
#    def test_simple_addition(self) -> None:
#        summ = Money(5,"USD").plus(Money(5,"USD").get_amount())
#        self.assertEqual(Money(10,"USD").get_amount(), summ)
#
#    def test_simple_add_value(self) -> None:
#        m1 = Money(10,"USD")
#        x = 10
#        for i in range(0,10):
#            m1.add(i)
#            x += i
#            self.assertEqual(x, m1.get_amount())
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 14                                                                  # 
################################################################################
#
#
#
#import unittest
#from abc import ABC, abstractmethod
#
#
#class Money(ABC):
#    _amount: int
#
#    def __init__(self, amount: int, currencyy: str):
#        self._amount:    int = amount
#        self.currencyy: str = currencyy 
#
#    def equals(self, valor: int):
#        return self._amount == valor 
#
#    def times(self, multiplier: int) -> object:
#        self._amount *= multiplier
#        return self._amount
#
#    def add(self, number: int) -> None :
#        self._amount += number 
#
#    def currency(self) -> str:
#        return self.currencyy
#
#    def plus(self, number: int) -> int:
#        return self._amount + number 
#
#    def set_amount(self, new_amount: int) -> None:
#        self._amount: int = new_amount
#
#    def get_amount(self) -> int:
#        return self._amount
#
## TESTS
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self) -> None:
#        m1 = Money(5, "USD")
#        m1.times(2) 
#        self.assertEqual(10, m1._amount)
#        m1.set_amount(5)
#        m1.times(3) 
#        self.assertEqual(15, m1._amount)
#
#    def test_equality(self) -> None:
#        self.assertTrue(Money(5, "USD").equals(5))
#
#    def test_currency(self) -> None:
#        self.assertEqual("USD", Money(1, "USD").currency())
#        self.assertEqual("CHF", Money(1, "CHF").currency())
#
#    def test_simple_addition(self) -> None:
#        summ = Money(5,"USD").plus(Money(5,"USD").get_amount())
#        self.assertEqual(Money(10,"USD").get_amount(), summ)
#
#    def test_simple_add_value(self) -> None:
#        m1 = Money(10,"USD")
#        x = 10
#        for i in range(0,10):
#            m1.add(i)
#            x += i
#            self.assertEqual(x, m1.get_amount())
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 15                                                                  # 
################################################################################
#
#
#
#import unittest
#from abc import ABC, abstractmethod
#
#
#class Money(ABC):
#    _amount: int
#
#    def __init__(self, amount: int, currencyy: str):
#        self._amount:    int = amount
#        self.currencyy: str = currencyy 
#
#    def equals(self, valor: int):
#        return self._amount == valor 
#
#    def times(self, multiplier: int) -> object:
#        self._amount *= multiplier
#        return self._amount
#
#    def add(self, number: int) -> None :
#        self._amount += number 
#
#    def sub(self, number: int) -> None :
#        self._amount -= number 
#
#    def currency(self) -> str:
#        return self.currencyy
#
#    def plus(self, number: int) -> int:
#        return self._amount + number 
#
#    def set_amount(self, new_amount: int) -> None:
#        self._amount: int = new_amount
#
#    def get_amount(self) -> int:
#        return self._amount
#
## TESTS
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self) -> None:
#        m1 = Money(5, "USD")
#        m1.times(2) 
#        self.assertEqual(10, m1._amount)
#        m1.set_amount(5)
#        m1.times(3) 
#        self.assertEqual(15, m1._amount)
#
#    def test_equality(self) -> None:
#        self.assertTrue(Money(5, "USD").equals(5))
#
#    def test_currency(self) -> None:
#        self.assertEqual("USD", Money(1, "USD").currency())
#        self.assertEqual("CHF", Money(1, "CHF").currency())
#
#    def test_simple_addition(self) -> None:
#        summ = Money(5,"USD").plus(Money(5,"USD").get_amount())
#        self.assertEqual(Money(10,"USD").get_amount(), summ)
#
#    def test_simple_add_value(self) -> None:
#        m1 = Money(10,"USD")
#        x = 10
#        for i in range(0,10):
#            m1.add(i)
#            x += i
#            self.assertEqual(x, m1.get_amount())
#
#    def test_simple_sub_value(self) -> None:
#        m1 = Money(10,"USD")
#        x = 10
#        for i in range(0,10):
#            m1.sub(i)
#            x -= i
#            self.assertEqual(x, m1.get_amount())
#
#
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 16                                                                  # 
################################################################################
#
#
#
#import unittest
#from abc import ABC, abstractmethod
#
#
#class Money(ABC):
#    _amount: int
#
#    def __init__(self, amount: int, currencyy: str):
#        self._amount:    int = amount
#        self.currencyy: str = currencyy 
#
#    def equals(self, valor: int):
#        return self._amount == valor 
#
#    def times(self, multiplier: int) -> object:
#        self._amount *= multiplier
#        return self._amount
#
#    def add(self, number: int) -> None :
#        self._amount += number 
#
#    def sub(self, number: int) -> None :
#        self._amount -= number 
#
#    def currency(self) -> str:
#        return self.currencyy
#
#    def plus(self, number: int) -> int:
#        return self._amount + number 
#
#    def set_amount(self, new_amount: int) -> None:
#        self._amount: int = new_amount
#
#    def get_amount(self) -> int:
#        return self._amount
#
## TESTS
#class TestDolar(unittest.TestCase):
#
#    def test_multiplication(self) -> None:
#        m1 = Money(5, "USD")
#        m1.times(2) 
#        self.assertEqual(10, m1._amount)
#        m1.set_amount(5)
#        m1.times(3) 
#        self.assertEqual(15, m1._amount)
#
#    def test_equality(self) -> None:
#        self.assertTrue(Money(5, "USD").equals(5))
#
#    def test_currency(self) -> None:
#        self.assertEqual("USD", Money(1, "USD").currency())
#        self.assertEqual("CHF", Money(1, "CHF").currency())
#
#    def test_simple_addition(self) -> None:
#        summ = Money(5,"USD").plus(Money(5,"USD").get_amount())
#        self.assertEqual(Money(10,"USD").get_amount(), summ)
#
#    def test_simple_add_value(self) -> None:
#        m1 = Money(10,"USD")
#        x = 10
#        for i in range(0,10):
#            m1.add(i)
#            x += i
#            self.assertEqual(x, m1.get_amount())
#
#    def test_simple_sub_value(self) -> None:
#        m1 = Money(10,"USD")
#        x = 10
#        for i in range(0,10):
#            m1.sub(i)
#            x -= i
#            self.assertEqual(x, m1.get_amount())
#
#if __name__ == '__main__':
#    unittest.main()
#
#
#
################################################################################
# Capitulo 18                                                                  # 
################################################################################
#
#
#
#class TestCase:
#    def __init__(self, name) -> None:
#        pass
#
#    def run(self) -> int:
#        method = getattr(self, self.name)
#        method()
#
#class WasRun(TestCase):
#
#    def __init__(self, name) -> None:
#        self.wasRun = None 
#        TestCase.__init__(self, name)
#
#    def testMethod(self) -> int:
#        self.wasRun = 1
#
#    def run(self) -> int:
#        self.testMethod
#
#
#test = WasRun('testMethod')
#print(test.wasRun)
#test.run()
#print(test.wasRun)
#
#
#
################################################################################
# Capitulo 19                                                                  # 
################################################################################
#
#
#
#class TestCase:
#    def __init__(self, name) -> None:
#        pass
#
#    def run(self) -> int:
#        method = getattr(self, self.name)
#        method()
#
#    def setUP() -> None:
#        pass
#
#    def testSetUp(self) -> None:
#        tes = WasRun('testMethod')
#        test.run()
#        assert(test.wasSetUp)
#
#    def testRunning(self) -> None:
#        tes = WasRun('testMethod')
#        test.run()
#        assert(test.wasRun)
#
#class WasRun(TestCase):
#
#    def __init__(self, name) -> None:
#        self.wasRun = None 
#        TestCase.__init__(self, name)
#
#    def testMethod(self) -> int:
#        self.wasRun = 1
#
#    def run(self) -> int:
#        self.testMethod
#
#    def setUp(self) -> None:
#        self.wasRun = None
#        self.wasSetUp = 1
#
#test = WasRun('testMethod')
#print(test.wasRun)
#test.run()
#print(test.wasRun)
#
#
#
################################################################################
# Capitulo 20                                                                  # 
################################################################################
#
#
#
#class TestCase:
#    def __init__(self, name) -> None:
#        pass
#
#    def run(self, result) -> int:
#        result.testStarted()
#        self.setUp()
#        method = getattr(self, self.name)
#        method()
#        self.tearDown()
#
#    def setUP(self) -> None:
#        self.test = WasRun('testMethod')
#
#    def testTemplateMethod(self) -> None:
#        tes = WasRun('testMethod')
#        test.run()
#        assert('setUp testMethod' == stest.log)
#
#    def tearDown(self) -> None:
#        pass
#
#class WasRun(TestCase):
#
#    def __init__(self, name) -> None:
#        self.wasRun = None 
#        TestCase.__init__(self, name)
#
#    def testMethod(self) -> int:
#        self.wasRun = 1
#        self.log = self.log + 'testMethod'
#
#    def run(self) -> int:
#        self.testMethod
#
#    def setUp(self) -> None:
#        self.log = 'setUp' 
#
#    def testMethod(self) -> None:
#        self.log = self.log + 'testMethod' 
#
#    def tearDown(self) -> None:
#        self.log = self.log + 'tearDown' 
#
#test = WasRun('testMethod')
#print(test.wasRun)
#test.run()
#print(test.wasRun)
#
#
#
################################################################################
# Capitulo 21                                                                  # 
################################################################################
#
#
#
#class TestResult:
#
#    def __init__(self) -> None:
#        self.runCount = 0
#
#    def summary(self) -> None:
#        return f'{self.runCount} run, 0 failed'
#
#    def testStarted(self) -> None:
#        self.runCount = self.runCount + 1
#
#class TestCase:
#    def __init__(self, name) -> None:
#        pass
#
#    def run(self, result: int) -> int:
#        result.TestResult()
#        result.testStarted()
#        self.setUp()
#        method = getattr(self, self.name)
#        method()
#        self.tearDown()
#        return result 
#
#    def setUP(self) -> None:
#        self.test = WasRun('testMethod')
#
#    def testTemplateMethod(self) -> None:
#        tes = WasRun('testMethod')
#        test.run()
#        assert('setUp testMethod' == stest.log)
#
#    def tearDown(self) -> None:
#        pass
#
#    def testResult(self) -> None:
#        test = WasRun('testMethod')
#        result = test.runn()
#        assert('1 run, 0 failed'  == result.summary())
#
#    def testFailedResult(self) -> None:
#        test = WasRun('testBrokenMethod')
#        result = test.runn()
#        assert('1 run, 1 failed',result.summary)
#
#class WasRun(TestCase):
#
#    def __init__(self, name) -> None:
#        self.wasRun = None 
#        TestCase.__init__(self, name)
#
#    def testMethod(self) -> int:
#        self.wasRun = 1
#        self.log = self.log + 'testMethod'
#
#    def run(self) -> int:
#        self.testMethod
#
#    def setUp(self) -> None:
#        self.log = 'setUp' 
#
#    def testMethod(self) -> None:
#        self.log = self.log + 'testMethod' 
#
#    def tearDown(self) -> None:
#        self.log = self.log + 'tearDown' 
#
#    def testBrokenMethod(self) -> None:
#        raise Exception
#
#test = WasRun('testMethod')
#print(test.wasRun)
#test.run()
#print(test.wasRun)
#
#
#
################################################################################
# Capitulo 22                                                                  # 
################################################################################
#
#
#
#class TestResult:
#
#    def __init__(self) -> None:
#        self.runCount = 0
#
#    def summary(self) -> None:
#        return f'{self.runCount} run, 0 failed'
#
#    def testStarted(self) -> None:
#        self.runCount = self.runCount + 1
#
#class TestCase:
#    def __init__(self, name) -> None:
#        pass
#
#    def run(self, result: int) -> int:
#        result.TestResult()
#        result.testStarted()
#        self.setUp()
#        method = getattr(self, self.name)
#        method()
#        self.tearDown()
#        return result 
#
#    def setUP(self) -> None:
#        self.test = WasRun('testMethod')
#
#    def testTemplateMethod(self) -> None:
#        tes = WasRun('testMethod')
#        test.run()
#        assert('setUp testMethod' == stest.log)
#
#    def tearDown(self) -> None:
#        pass
#
#    def testResult(self) -> None:
#        test = WasRun('testMethod')
#        result = test.runn()
#        assert('1 run, 0 failed'  == result.summary())
#
#    def testFailedResult(self) -> None:
#        test = WasRun('testBrokenMethod')
#        result = test.runn()
#        assert('1 run, 1 failed',result.summary)
#
#    def testFailedResultFormatting(self) -> None:
#        result = TestResult()
#        result.testStarted()
#        result.testFailed()
#        assert('1 run, 1 failed',result.summary)
#
#class WasRun(TestCase):
#
#    def __init__(self, name) -> None:
#        self.wasRun = None 
#        TestCase.__init__(self, name)
#
#    def testMethod(self) -> int:
#        self.wasRun = 1
#        self.log = self.log + 'testMethod'
#
#    def run(self) -> int:
#        self.testMethod
#
#    def setUp(self) -> None:
#        self.log = 'setUp' 
#
#    def testMethod(self) -> None:
#        self.log = self.log + 'testMethod' 
#
#    def tearDown(self) -> None:
#        self.log = self.log + 'tearDown' 
#
#    def testBrokenMethod(self) -> None:
#        raise Exception
#
#test = WasRun('testMethod')
#print(test.wasRun)
#test.run()
#print(test.wasRun)
#
#
#
################################################################################
# Capitulo 23                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 24                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 25                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 26                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 27                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 26                                                                  # 
################################################################################
#
#
#
#
##Exercicio 1
#import unittest
#
#def add(x: int, y: int) -> int:
#    if isinstance(x, int) and isinstance(y, int):
#        return x + y
#    raise Exception ('Esta funcao so aceita valores inteiros..')
#
#class TestADD(unittest.TestCase):
#
#    def test_add_passed(self) -> None:
#        self.assertEqual(add(1,1), 2)
#
#    def test_add_error(self) -> None:
#        with self.assertRaises(Exception) as cm:
#            add(1.0, 0.0)
#        self.assertEqual(str(cm.exception), "Esta funcao so aceita valores inteiros..")
#
#if __name__ == '__main__':
#    unittest.main(verbosity=2)
#
##Exercicio 2
#import pytest 
#
#def add(x: int, y: int) -> int:
#    if isinstance(x, int) and isinstance(y, int):
#        return x - y
#    raise Exception ('Esta funcao so aceita valores inteiros..')
#
#class TestAdd:
#
#    def test_true_sub(self) -> None:
#        assert sub(10,10) == 20
#
#    def test_sub_error_msg(self) -> None:
#        with pytest.raises(Exception) as error:
#            sub(1.0,1.0)
#        assert str(error.value) == 'Esta funcao so aceita valores inteiros..'
#
##Exercicio 3
#import pytest 
#
#def mult(x: int, y: int) -> int:
#    if isinstance(x, int) and isinstance(y, int):
#        return x - y
#    raise Exception ('mult..')
#
#class TestMult:
#
#    def test_true_mult(self) -> None:
#        assert mult(10,10) == 20
#
#    def test_mult_error_msg(self) -> None:
#        with pytest.raises(Exception) as error:
#            mult(1.0,1.0)
#        assert str(error.value) == 'mult..'
#
##Exercicio 4
#import pytest 
#
#def div(x: int, y: int) -> int:
#    if isinstance(x, int) and isinstance(y, int):
#        return x - y
#    raise Exception ('div..')
#
#class TestDiv:
#
#    def test_true_div(self) -> None:
#        assert div(10,10) == 20
#
#    def test_div_error_msg(self) -> None:
#        with pytest.raises(Exception) as error:
#            div(1.0,1.0)
#        assert str(error.value) == 'div..'
#
##Exercicio 5
#import pytest 
#
#def sum_equal(x: int, y: int) -> int:
#    if x == y:
#        return x + y
#
#class TestSumEqual:
#
#    def test_true_sum(self) -> None:
#        assert sum_equal(10,10) == 20
#
##Exercicio 6
#import pytest 
#
#def equal(x: int, y: int) -> bool:
#    return x == y
#
#class TestSumEqual:
#
#    def test_true_sum(self) -> None:
#        assert equal(10,10)
#
##Exercicio 7
#import pytest 
#
#def equal_null(x: None, y: None) -> bool:
#    return x == y
#
#class TestSumEqual:
#
#    def test_true_sum(self) -> None:
#        assert equal(None, None)
#
##Exercicio 8
#import pytest 
#
#def equal_null(x: None, y: None) -> bool:
#    return x == y
#
#class TestSumEqual:
#
#    def test_true_sum(self) -> None:
#        assert equal(None, None)
#
#
#
################################################################################
# Capitulo 27                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 28                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 29                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 29                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 30                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 31                                                                  # 
################################################################################
#
#
#
# LEITURA....
#
#
#
################################################################################
# Capitulo 32                                                                  # 
################################################################################
#
#
#
#def tipo_triangulo(a, b, c):
#    if a + b <= c or a + c <= b or b + c <= a:
#        return 0  
#
#    if a == b == c:
#        return 1
#    elif a == b or a == c or b == c:
#        return 2
#    else:
#        return 3
#
#def test_equilatero():
#    assert tipo_triangulo(3, 3, 3) == 1
#
#def test_isosceles():
#    assert tipo_triangulo(3, 3, 4) == 2
#
#def test_escaleno():
#    assert tipo_triangulo(3, 4, 5) == 3
#
#def test_nao_triangulo():
#    assert tipo_triangulo(1, 2, 3) == 0
#
#
#
################################################################################
# FIM...                                                                       # 
################################################################################
#
#
#
