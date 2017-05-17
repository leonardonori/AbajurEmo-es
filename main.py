# -*- coding: utf-8 -*-

import sys
sys.path.append("dir_path")
from _twitter import downloadTweets
from _process import *
from _connection import *
import threading
import time

'''Função para fazer o donwload dos tweets '''
def mining():
    while(1):
        downloadTweets("#ProjetoEdmito", 10)
        time.sleep(1)

'''Função para realizar a análise'''
def analisys():
    while(1):
        updateDB()
        time.sleep(2)

threads = []
t = threading.Thread(target=mining, args=())
threads.append(t)
t.start()

t = threading.Thread(target=analisys, args=())
threads.append(t)
t.start()
