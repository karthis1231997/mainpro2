import configparser

config = configparser.RawConfigParser()
config.read('C:\\Users\\hkarthis\\PycharmProjects\\mainpro2\\Configurations\\config.ini')


class Readconfig:
    @staticmethod
    def getorangeurl():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getuserid():
        userid = config.get('common info', 'username')
        return userid

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getuserid_1():
        userid = config.get('common info_1', 'username_1')
        return userid

    @staticmethod
    def getpassword_1():
        password = config.get('common info_1', 'password_1')
        return password

    @staticmethod
    def Nusername():
        Nusername1 = config.get('comman info_3', 'Nusername')
        return Nusername1

    @staticmethod
    def Npassword():
        Npassword1 = config.get('comman info_3', 'Npassword')
        return Npassword1


