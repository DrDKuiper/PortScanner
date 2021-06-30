#!/usr/bin/python3
# coding: utf-8

from socket import *
import time

startTime = time.time()

if __name__ == '__main__':
    target = input('Informe o endereço de IP: ')
    t_IP = gethostbyname(target)
    print('Iniciando varredura em: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('Port %d: ABERTA' % (i,))
        s.close()
print('Tempo:', time.time() - startTime)