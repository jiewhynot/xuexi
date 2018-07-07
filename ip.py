import requests
import time
import json




class ipcheck(object):



    def yanzheng(self):

        try:
            self.proxies = {
                "http":self.ippool[self.i-1]
            }
            self.resq()

            self.ip_list.append(self.ippool[self.i-1])

        except:
            pass





    def resq(self):

        url1='http://ip.chinaz.com/getip.aspx'
        response=requests.get(url1,proxies=self.proxies)
        print(response.text)
    def main(self):
        self.ippool = ["101.236.35.98:8866", "101.236.23.202:8866", "114.250.25.19:80", "121.42.167.160:3128", ]
        self.ip_list = []

        for self.i in range(1, 5):
            self.yanzheng()
        print(self.ip_list)

if __name__ == '__main__':
    obj=ipcheck()
    obj.main()




