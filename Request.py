# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Request.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 21:01:13 by vordynsk          #+#    #+#              #
#    Updated: 2020/01/18 17:32:46 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests

class   Request():
    
    '''parent class to send requests to Cisco API'''

    err200 = "<Response [200]>"

    def __init__(self, url, login, password):
        self.__url = url
        self.__login = login
        self.__password = password

    def get_request(self, req, image):
        try:
            r = requests.request("GET", self.__url + req, auth=(self.__login, self.__password), verify=False)
        except:
            print ("Something went wrong with get request to the server.\nPlease, check your login and password.\nurl = '",self.__url,"'\nrequest = '",req,"'")
            exit(1)
        if r.status_code == 200:
            print ("Success")
        else:
            error = {}
            error['error'] = str(r)[11:14]
            return error
        if image == 'image':
            return r
        return r.json()

if __name__ == '__main__':
    r = Request("https://cisco-cmx.unit.ua/", "RO", "just4reading")
    #r.get_request("api/location/v2/clients")
    print (r.get_request("api/location/v2/client"))
