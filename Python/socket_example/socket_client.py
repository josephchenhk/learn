# -*- coding: utf-8 -*-
# @Time    : 8/5/2019 9:05 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: socket_client.py
# @Software: PyCharm

import json
import threading
import socket
import time
import ast
import uuid
from functools import partial
import requests

HOST = '192.168.8.17'
PORT = 15566
API_PORT = 15565

class SocketClient():
    """
    params: iuid_list, broker_id, account_id, tick_callback, orderbook_callback, order_callback, execution_callback
    pass the ones you need

    E.g.

        c = SocketClient(iuid_list=['CN_10_000001','CN_10_600000'],
                 broker_id='101',
                 account_id='1888000385',
                 tick_callback=lambda x: print(f"I receive tick: {x}"),
                 orderbook_callback=lambda x: print(f"I receive orderbook: {x}"),
                 order_callback=lambda x: print(f"I receive order: {x}"),
                 execution_callback=lambda x: print(f"I receive execution: {x}"),)
        time.sleep(120)
        print(c.tick_data)
        print(c.orderbook_data)
        print(c.order_data)
        print(c.execution_data)
    """

    def __init__(self, **kwargs):
        """Pass the parameters you need.

        Parameters
        ----------
        iuid_list : list, optional
            A list of iuids
        broker_id : str, optional
            Has to be with account_id if passed
        account_id : int, optional
            Has to be with broker_id if passed
        tick_callback : function, optional
        orderbook_callback : function, optional
        order_callback : function, optional
        execution_callback : function, optional
        """
        assert bool(kwargs.get('iuid_list')) >= bool(
            kwargs.get('tick_callback')), "You provided tick_callback without proving iuid_list."
        assert bool(kwargs.get('iuid_list')) >= bool(
            kwargs.get('orderbook_callback')), "You provided orderbook_callback without proving iuid_list."
        assert bool(kwargs.get('broker_id')) == bool(
            kwargs.get('account_id')), "You should provide both / none of broker_id and account_id."
        assert bool(kwargs.get('broker_id')) >= bool(
            kwargs.get('order_callback')), "You provided order_callback without proving broker_id & account_id."
        assert bool(kwargs.get('broker_id')) >= bool(
            kwargs.get('execution_callback')), "You provided execution_callback without proving broker_id & account_id."

        self.tick_args = {
            'name': 'tick',
            'exchange': 'market.tick',
            'routing_keys': [
                id.replace("_", ".") if not "full" in id else id.replace("_", ".").replace(".full", "_full") for id in
                kwargs.get('iuid_list')],
            'callback': kwargs.get('tick_callback') if kwargs.get('tick_callback') else (lambda x: x)
        } if kwargs.get('iuid_list') else None

        self.orderbook_args = {
            'name': 'orderbook',
            'exchange': 'market.orderbook',
            'routing_keys': self.tick_args['routing_keys'],
            'callback': kwargs.get('orderbook_callback') if kwargs.get('orderbook_callback') else (lambda x: x)
        } if kwargs.get('iuid_list') else None

        self.order_args = {
            'name': 'order',
            'exchange': 'trading',
            'routing_keys': ["order.{}.{}".format(kwargs.get('broker_id'), kwargs.get('account_id'))],
            'callback': kwargs.get('order_callback') if kwargs.get('order_callback') else (lambda x: x)
        } if kwargs.get('broker_id') else None

        self.execution_args = {
            'name': 'execution',
            'exchange': 'trading',
            'routing_keys': ["execution.{}.{}".format(kwargs.get('broker_id'), kwargs.get('account_id'))],
            'callback': kwargs.get('execution_callback') if kwargs.get('execution_callback') else (lambda x: x)
        } if kwargs.get('broker_id') else None

        self.args = {
            k: v for k, v in (
            ('tick', self.tick_args),
            ('orderbook', self.orderbook_args),
            ('order', self.order_args),
            ('execution', self.execution_args)
        ) if v is not None
        }

        self.data = {
            'tick': {},
            'orderbook': {},
            'order': {},
            'execution': {}
        }

        if kwargs.get('iuid_list'):
            self.iuid_list = kwargs.get('iuid_list')

        self.callback = partial(self._callback, ch=None, properties=None)
        self._init_socket()

    def _init_socket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((HOST, PORT))
        except ConnectionRefusedError as e:
            raise ConnectionError(f"Socket client fails to start because {e}.")
        if hasattr(self, 'iuid_list'):
            self.update_subscribe_list(self.iuid_list)
        t = threading.Thread(target=self.start_consuming)
        t.setDaemon(True)
        t.start()

    def start_consuming(self):
        n = 0
        data = ''
        while True:
            streamBytes = self.s.recv(1024)
            data += streamBytes.decode()
            #TODO: change to while loop in order to consume the meassage immediately
            if '\n' in streamBytes.decode():
                # print(n, repr(data))
                data, *tmp = data.split("\n")
                data += "\n"
                data_dict = ast.literal_eval(data)
                if data_dict.get('quoteId'):
                    iuid = data_dict.get('iuid').replace("_", ".")
                    Method = type('Method', (object,), dict(routing_key=iuid))
                    self.callback(method=Method(), body=data, message_type='tick')
                    self.callback(method=Method(), body=data, message_type='orderbook')
                if data_dict.get('localId'):
                    broker_id = data_dict.get('brokerId')
                    broker_account = data_dict.get('brokerAccount')
                    if data_dict.get('extExecutionId'):
                        Method = type('Method', (object,), dict(routing_key=f"execution.{broker_id}.{broker_account}"))
                        self.callback(method=Method(), body=data, message_type='execution')
                    elif data_dict.get('extOrderId'):
                        Method = type('Method', (object,), dict(routing_key=f"order.{broker_id}.{broker_account}"))
                        self.callback(method=Method(), body=data, message_type='order')
                data = "\n".join(tmp)
                n += 1

    def _callback(self, ch, method, properties, body, message_type=None):
        data = json.loads(body) # ast.literal_eval(data)
        # print(methpod.routing_key, message_tye)
        # print(data)
        if data.get('iuid'):  # tick and orderbook
            self.data[message_type][method.routing_key.replace(".", "_")] = data
        else:                 # order and execution
            self.data[message_type][method.routing_key.replace(".", "_") + "_" + str(data.get('id'))] = data
        self.args[message_type]['callback'](data)

    def update_subscribe_list(self, iuid_list):
        """subscribe the needed info (i.e., orderbook, tick, trades) from data vendors (i.e., futu, Bloomberg) before using them by `self.callback` function.
        """
        url = f"http://{HOST}:{API_PORT}/api/v3/market/subscribe"
        params = {'iuids': ",".join(iuid_list)}
        req_id = uuid.uuid4().hex
        headers = {'Content-Type': 'application/json', 'x-request-id': req_id}
        with requests.Session() as sess:
            print(f"If you find the subscription is not successful, please send the following string to the person in charge: {req_id}")
            resp = sess.post(url, params=params, headers=headers).json()
            print(resp)
            for iuid in iuid_list:
                self.s.sendall(f'{iuid}\n'.encode())

    def disconnect_client(self):
        close_res = self.s.close()
        return close_res

    @property
    def tick_data(self):
        return self.data['tick']

    @property
    def orderbook_data(self):
        return self.data['orderbook']

    @property
    def order_data(self):
        return self.data['order']

    @property
    def execution_data(self):
        return self.data['execution']


if __name__ == "__main__":
    c = SocketClient(iuid_list=['CN_10_000007', 'CN_10_159901', 'CN_10_600009', 'CN_10_600028', 'CN_10_000002', 'CN_10_600006', 'CN_10_600007', 'CN_10_510050'], # ['CN_10_000001', 'CN_10_600000'],
                     broker_id='101',
                     account_id='1888000385',
                     tick_callback=lambda x: print(f"I receive tick: {x}"),
                     orderbook_callback=lambda x: print(f"I receive orderbook: {x}"),
                     order_callback=lambda x: print(f"I receive order: {x}"),
                     execution_callback=lambda x: print(f"I receive execution: {x}"), )
    time.sleep(60)

