#!/usr/bin/env python3
import re
import os
import requests
import json
import platform

# define function that fetchs rpc creds from .conf
def def_credentials(chain):
    operating_system = platform.system()
    if operating_system == 'Darwin':
        ac_dir = os.environ['HOME'] + '/Library/Application Support/Komodo'
    elif operating_system == 'Linux':
        ac_dir = os.environ['HOME'] + '/.komodo'
    elif operating_system == 'Win64':
        ac_dir = "dont have windows machine now to test"
    # define config file path
    if chain == 'KMD':
        coin_config_file = str(ac_dir + '/komodo.conf')
    else:
        coin_config_file = str(ac_dir + '/' + chain + '/' + chain + '.conf')
    #define rpc creds
    with open(coin_config_file, 'r') as f:
        #print("Reading config file for credentials:", coin_config_file)
        for line in f:
            l = line.rstrip()
            if re.search('rpcuser', l):
                rpcuser = l.replace('rpcuser=', '')
            elif re.search('rpcpassword', l):
                rpcpassword = l.replace('rpcpassword=', '')
            elif re.search('rpcport', l):
                rpcport = l.replace('rpcport=', '')
    return('http://' + rpcuser + ':' + rpcpassword + '@127.0.0.1:' + rpcport)

# define function that posts json data
def post_rpc(url, payload, auth=None):
    try:
        r = requests.post(url, data=json.dumps(payload), auth=auth)
        return(json.loads(r.text))
    except Exception as e:
        raise Exception("Couldn't connect to " + url + ": ", e)

# dicebet rpc
def dicebet_rpc(chain, name, fundingtxid, amount, odds):
    dicebet_payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "dicebet",
        "params": [
            name,
            fundingtxid,
            str(amount),
            str(odds)]}
    dicebet_result = post_rpc(def_credentials(chain), dicebet_payload)
    return(dicebet_result['result'])

# Send raw transaction rpc
def sendrawtx_rpc(chain, rawtx):
    sendrawtx_payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": "sendrawtransaction",
        "params": [rawtx]}
    #rpcurl = def_credentials(chain)
    return(post_rpc(def_credentials(chain), sendrawtx_payload))
