import requests
import time
import json
from iplist import list2
import threading
from multiprocessing import Pool

print(list2)






class ipcheck():

    def yanzheng(self,i):

        try:
            self.proxies = {
                "http":i
            }
            self.resq()

            self.ip_list.append(i)
            print(self.ip_list)

        except:
            pass

    def resq(self):

        url1='http://ip.chinaz.com/getip.aspx'
        response=requests.get(url1,proxies=self.proxies)
        print(response.text)
    def main(self):





        self.ip_list = []
        p = Pool(8)

        for i in list2:
            # t = threading.Thread(target=self.yanzheng,args=(i,))
            # t.start()
            # t.join()
            p.apply_async(self.yanzheng,args=(i,))
        p.close()
        p.join()
        print(self.ip_list)

if __name__ == '__main__':

    obj=ipcheck()
    obj.main()

