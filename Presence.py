# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Presence.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/21 20:39:17 by vordynsk          #+#    #+#              #
#    Updated: 2020/01/30 19:55:13 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json
from Request import *

class   Presence(Request):

    '''class to access "Presence" Cisco API'''

    site_id = "api/config/v1/sites"
    sum_of_conn_vis = "api/presence/v1/connected/total/?"
    repeat_visitors = "api/presence/v1/repeatvisitors/count/?"
    passers_by = "api/presence/v1/passerby/total?"
    dwell_c = "api/presence/v1/dwell/count/?"
    dwell_a = "api/presence/v1/dwell/average/?"

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

    def get_info(self, start_date, end_date, info):
        if self.site_id == None:
            logging.warning('could not process sum_of_connected_visitors request. no site_id. terminating...')
            return
        if info == "connected":
            return self.get_request(self.sum_of_conn_vis + "siteId=" + str(self.s_id) + "&startDate=" + start_date + "&endDate=" + end_date, None)
        if info == "repeat":
            return self.get_request(self.repeat_visitors + "siteId=" + str(self.s_id) + "&startDate=" + start_date + "&endDate=" + end_date, None)
        if info == "passerby":
            return self.get_request(self.passers_by + "siteId=" + str(self.s_id) + "&startDate=" + start_date + "&endDate=" + end_date, None)
        if info == "dwell_count":
            return self.get_request(self.dwell_c + "siteId=" + str(self.s_id) + "&startDate=" + start_date + "&endDate=" + end_date, None)
        if info == "dwell_average":
            return self.get_request(self.dwell_a + "siteId=" + str(self.s_id) + "&startDate=" + start_date + "&endDate=" + end_date, None)

if __name__ == '__main__':
    P = Presence()
    print (P.get_site_id())
    print (P.get_info("2020-01-26", "2020-01-26", "connected"))
    print (P.get_info("2020-01-26", "2020-01-26", "repeat"))
    print (P.get_info("2020-01-26", "2020-01-26", "passerby"))
    print (P.get_info("2020-01-26", "2020-01-26", "dwell_count"))
    print (P.get_info("2020-01-26", "2020-01-26", "dwell_average"))
