import os
from Testcase_date.getpathInfo import getpathInfo
import configparser
path=getpathInfo().get_Path()
config_path=os.path.join(path,'config.ini')
#print(config_path)
config=configparser.ConfigParser()
config.read(config_path,encoding='utf-8')
class ReadConfig():
    def get_http(self,name):
        value = config.get('HTTP',name)
        return value
    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value
if __name__ == '__main__':
    print(ReadConfig().get_http('baseurl'))
    print(ReadConfig().get_email('on_off'))



