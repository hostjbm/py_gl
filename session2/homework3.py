# 1. Описати атрибут ip за допомогою дескрипторів.
#     атрибут може бути встановленим лише якщо значення - str,
#     відповідає шаблону "x.x.x.x" та кожен блок може бути конвертований в int
# 2. Створити ssh объект та викликати метод connect (імітація підключення)
# 3. Змінити доступ до методу execute. Якщо  self.connected == False має викликатися метод wait_for_connection (імітіція перепідключення),
#   якщо підключення встановлено має спрацювати метод execute.
import unittest


class IP_Descriptor:

    def __init__(self, ip):
        self.ip = ip

    def __get__(self, instance, owner):
        return self.ip

    def __set__(self, instance, value):
        ip_octets = [x for x in value.split('.') if x.isdigit()]
        if len(value.split('.')) != 4 or len(ip_octets) != 4:
            raise ValueError('Not IP')
        self.ip = value


class SSH():
    ip = IP_Descriptor('ip')

    def __init__(self, ip):
        self.ip = ip

    def __getattr__(self, item):  # for not implemented attributes only
        print('Get attr {}'.format(item))
        return 'not implemented'

    #   def __getattribute__(self, item):
    #        print("Get attribute: {}".format(item))
    #        return super().__getattribute__(item)

    def connect(self):
        # Connection via supported connection type
        # password = getpass.getpass()
        # create connection to host
        self.connected = True

    def close_connection(self):
        # Close supported connection type
        self.connected = False

    def wait_for_connection(self, timeout, polling=0.1):
        print('wait for connection..')

    def execute(self, timeout, polling=0.1):
        print('wait for connection..')


ssh1 = SSH('192.168.1.1')
ssh1.connect()


class SshTest(unittest.TestCase):
    def test_octets(self):
        with self.assertRaises(ValueError):
            SSH('192.168.1')

    def test_int(self):
        with self.assertRaises(ValueError):
            SSH('192.168.abc.2')

    def test_str(self):
        with self.assertRaises(ValueError):
            SSH('localhost')

    def test_combination(self):
        with self.assertRaises(ValueError):
            SSH('192.168.1.1.abc')

if __name__=='__main__':
    unittest.main(verbosity=2)