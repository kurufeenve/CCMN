# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Presence.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/21 20:39:17 by vordynsk          #+#    #+#              #
#    Updated: 2020/01/26 15:46:13 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json
from Request import *

class   Presence(Request):

    '''class to access "Presence" Cisco API'''

    site_id = "api/config/v1/sites"
    sum_of_conn_vis = "api/presence/v1/connected/total/?"

    def __init__(self):
        super().__init__("https://cisco-presence.unit.ua/", "RO", "Passw0rd")
        self.s_id = self.get_site_id()

    def get_site_id(self):
        r = self.get_request(self.site_id, None)[0]['aesUId']
        if r == None:
            logging.warning('No site Id')
            return None
        else:
            #logging.info('site Id')
            return r

    def get_sum_of_connected_visitors(self, start_date, end_date):
        #https://<tenant-id>.cmxcisco.com/api/presence/v1/connected/total/?siteId=<Site ID>&startDate=<date in yyyy-mm-dd>&endDate=<date in yyyy-mm-dd>
        if self.site_id == None:
            logging.warning('could not process sum_of_connected_visitors request. no site_id. terminating...')
            return
        return self.get_request(self.sum_of_conn_vis + "siteId=" + str(self.s_id) + "&startDate=" + start_date + "&endDate=" + end_date, None)



if __name__ == '__main__':
    P = Presence()
    print (P.get_site_id())
    print (P.get_sum_of_connected_visitors("2020-01-26", "2020-01-26"))
