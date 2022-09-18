#!/usr/bin/env python3
r'''
SecondPip module
'''


def hello():
    r'''
    Hello function
    '''
    return 'Hello, World!'

def exponente(m):
    exp=(-1)**m  
    return exp


if __name__ == '__main__':  #En el main se guardan todas las funciones para que el programa consulte
    r'''
    Hello main
    '''
    hello()
    exponente(m)
