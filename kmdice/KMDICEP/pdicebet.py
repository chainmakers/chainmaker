#!/usr/bin/env python3
import sys
import ast
import kmdrpc

CHAIN = 'KMDICE'
NAME = 'KMDICE'
FUNDINGTXID = '5be49570c56d036abb08b6d084da93a8a86f58fc48db4a1086be95540d752d6f'

AMOUNT = input('Please type amount')
ODDS = input('Please type odds')

dicebet_result = kmdrpc.dicebet_rpc(CHAIN, NAME, FUNDINGTXID, AMOUNT, ODDS)
#print(dicebet_result)
dicebet_hex = (dicebet_result['hex'])
sendraw_result = kmdrpc.sendrawtx_rpc(CHAIN, dicebet_hex)
print(sendraw_result['result'])
