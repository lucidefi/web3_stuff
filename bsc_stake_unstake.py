import requests
from web3 import Web3
import json
from random import randint
from datetime import datetime
import time
import math
import numpy as np

INFURA_KEY_RESERVE = ['',''] # if you have multiple infura keys, you can place the end part here - somethihg like '51ec326cef934ba4b4ff2850a6c74f47'

def create_w3_from_reserve(key_reserve_list=None,debug=True):
    return Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org'))

def create_trade_contract(w3=None):
    if w3 is None:
        w3=create_w3_from_reserve()
    Trade_ABI = '[{"inputs":[{"internalType":"address","name":"_swap","type":"address"},{"internalType":"address","name":"_lp","type":"address"},{"internalType":"address","name":"_price","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"investor","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"lp_amt","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amt_eth","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"usd","type":"uint256"}],"name":"BuyEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"investor","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"lp_amt","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amt_eth","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"usd","type":"uint256"}],"name":"SellEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"WhitelistAdminAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"WhitelistAdminRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"WhitelistedAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"WhitelistedRemoved","type":"event"},{"inputs":[{"internalType":"address[]","name":"lp_list","type":"address[]"},{"internalType":"uint256[]","name":"eth_list","type":"uint256[]"},{"internalType":"uint256","name":"max_slippage","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"addresspayable","name":"investor","type":"address"}],"name":"BuyLP","outputs":[{"internalType":"uint256[]","name":"num_tokens","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address[]","name":"token_list","type":"address[]"},{"internalType":"uint256[]","name":"eth_list","type":"uint256[]"},{"internalType":"uint256","name":"max_slippage","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"addresspayable","name":"investor","type":"address"}],"name":"BuyToken","outputs":[{"internalType":"uint256[]","name":"num_tokens","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"investor","type":"address"},{"internalType":"address","name":"delegate","type":"address"}],"name":"CheckDelegate","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"Delegate","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"DepositETH","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"InvestTokenAMT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"InvestTokenETH","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"InvestTokenList","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"InvestTokenUSD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"lp_list","type":"address[]"},{"internalType":"uint256[]","name":"lp_amt_list","type":"uint256[]"},{"internalType":"uint256","name":"max_slippage","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"addresspayable","name":"investor","type":"address"},{"internalType":"addresspayable","name":"receiver","type":"address"}],"name":"SellLP","outputs":[{"internalType":"uint256[]","name":"num_tokens","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address[]","name":"token_list","type":"address[]"},{"internalType":"uint256[]","name":"token_amt_list","type":"uint256[]"},{"internalType":"uint256","name":"max_slippage","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"addresspayable","name":"investor","type":"address"},{"internalType":"addresspayable","name":"receiver","type":"address"}],"name":"SellToken","outputs":[{"internalType":"uint256[]","name":"num_tokens","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_target1","type":"address"},{"internalType":"address","name":"_target2","type":"address"}],"name":"SetConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegate","type":"address"}],"name":"SetDelegate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"Withdraw","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"addWhitelistAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"addWhitelisted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"emergencyETHWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"emergencyTokenWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isWhitelistAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isWhitelisted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"kill","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"lp","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"removeWhitelisted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceWhitelistAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceWhitelisted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swap","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
    Trade_ABI = json.loads(Trade_ABI)
    Trade_Addr = '0x05B9E97680e770fE25EF6B2213EE02a50A8C175F'
    return w3.eth.contract(address=Trade_Addr, abi=Trade_ABI)


def unstake(w3, lp_list=None, withdraw_list=None, walletID=None, trade_contract_w3=None, max_sliappage=250,
              walletPrivateKey=None, gas_buff=1.05, chain_id=42,td=4000,deadline =  int(time.time()*1000) + 200000,max_slippage=250):
    # chain id 42 : kovan testnet, 56 bsc
    # chain id 1 : mainnnet
    if trade_contract_w3 is None:
        trade_contract_w3 = create_trade_contract(w3=w3)

    nonce = w3.eth.getTransactionCount(walletID)

    gasPrice = w3.eth.gas_price

    gas_est = trade_contract_w3.functions.SellLP(pair_list, withdraw_list, max_slippage, deadline, walletID, walletID) \
        .estimateGas({'from': walletID,
                      #'chainId': chain_id,
                      })
    tx = trade_contract_w3.functions.SellLP(pair_list, withdraw_list, max_slippage, deadline, walletID, walletID) \
        .buildTransaction({'from': walletID,
                           #'chainId': chain_id,
                           'nonce': nonce,
                           'gas': int(round(gas_est * gas_buff)),
                           'gasPrice': int(round(gasPrice * gas_buff))
                           })
    signed_tx = w3.eth.account.signTransaction(tx, private_key=walletPrivateKey)
    hash_val = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    result = w3.eth.waitForTransactionReceipt(hash_val, timeout=240)
    hash = hash_val.hex()
    print(hash)
    if (result['status']):
        # self.UpdateInfo()
        print("Unstake Transaction completed")
    else:
        print("Unstake Transaction failed")
    return result['status'], hash
def to_checksum(address):
    return Web3.toChecksumAddress(address)


def get_user_lp_list(wallet_address=None,trade_contract_w3=None,endofid=2000):
    lpl=[]
    for i in range(endofid):
        try:
            lpl.append(trade_contract_w3.functions.InvestTokenList(wallet_address, i).call())
        except:
            return lpl
    return lpl

def get_user_staked_lp_amount(wallet_address=None,trade_contract_w3=None,lpl=None):
    lpamt=[]
    for l in lpl:
        lpamt.append(trade_contract_w3.functions.InvestTokenAMT(wallet_address, l).call())
    return lpamt

def stake(w3, pair_list=None, wei_list=None, walletID=None, trade_contract_w3=None, max_sliappage=200,
        walletPrivateKey=None, gas_buff=1.05, chain_id=42,deadline =  int(time.time()*1000) + 200000,max_slippage=250):
    if trade_contract_w3 is None:
        trade_contract_w3 = create_trade_contract(w3 = w3)
    nonce = w3.eth.getTransactionCount(walletID)
    print("Chain ID: ", chain_id)
    gasPrice = w3.eth.gas_price

    amount_wei = int(sum(wei_list))
    gas_est = trade_contract_w3.functions.BuyLP(pair_list, wei_list, max_sliappage, deadline, walletID) \
        .estimateGas({'from': walletID,
                      'value': amount_wei})
    print(gas_est)
    #exit()
    tx = trade_contract_w3.functions.BuyLP(pair_list, wei_list, max_sliappage, deadline, walletID) \
        .buildTransaction({'from': walletID,
                           #'chainId': chain_id,
                           'value': amount_wei,
                           'nonce': nonce,
                           'gas': int(round(gas_est * gas_buff)),
                           'gasPrice': int(round(gasPrice * gas_buff))
                           })
    signed_tx = w3.eth.account.signTransaction(tx, private_key=walletPrivateKey)
    hash_val = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    result = w3.eth.waitForTransactionReceipt(hash_val, timeout=240)
    hash = hash_val.hex()
    print(hash)
    if (result['status']):
        # self.UpdateInfo()
        print("Stake Transaction completed")
    else:
        print("Stake Transaction failed")
    return result['status'], hash


#
trade_addr="0x05B9E97680e770fE25EF6B2213EE02a50A8C175F"

id='0x-------' # wallet address
pk='' # private key
w3=create_w3_from_reserve(key_reserve_list=INFURA_KEY_RESERVE)
trade_cont = create_trade_contract(w3)


######### staking
investment_amount_bnb = 1 # investing 1 bnb

CAKE_BNB= '0x0eD7e52944161450477ee417DE9Cd3a859b14fD0'
BUSD_BNB= '0x58F876857a02D6762E0101bb5C46A8c1ED44Dc16'

max_slippage = 200 # 200 = 20%
pair_list = [CAKE_BNB,BUSD_BNB]
num_splits = len(pair_list)
print("Investing in :", pair_list)

print("Commence staking {} ETH....".format(investment_amount_bnb))
stake_start_time = time.time()
wei_list = []
inv_indv = math.floor(investment_amount_bnb * 1e18 / num_splits)
for i in range(num_splits):
    wei_list.append(inv_indv)
status, hash = stake(w3, pair_list=pair_list, wei_list=wei_list, walletID=id,
                               trade_contract_w3=trade_cont,
                               max_sliappage=max_slippage, walletPrivateKey=pk, gas_buff=1.2,
                               chain_id=56)
print("$$$$$$$$$$$$$$$$$")
print(hash) # can copy and paste to look up from etherscan
print(status) # 1 = success
print("$$$$$$$$$$$$$$$$$")

################## end staking
print("exiting here")
exit()


#### show balance
if trade_cont is None:
    trade_cont = create_trade_contract(w3=w3)

lp_lists = get_user_lp_list(wallet_address=id,trade_contract_w3=trade_cont)
lp_balances = get_user_staked_lp_amount(wallet_address=id,trade_contract_w3=trade_cont,lpl=lp_lists)
print(lp_lists,lp_balances)
print("########################################")


print("LP pair lists:", lp_lists)
print("recorded user balance in contract:", lp_balances)
print("exiting here")
exit()
#### unstake

# lpl= [to_checksum("0xa478c2975ab1ea89e8196811f51a7b7ade33eb11"), to_checksum("0x86fef14c27c78deaeb4349fd959caa11fc5b5d75")] # pair address that you already staked. the LP token is in the smart contract, not in your wallet.
# wdl=[10000000, 10000000] # lp amount. it's usually a really big number.

# it's rare but sometimes there are weird pools among the ones tha take token as fees. in that case you need to withdraw smaller portion than 100% of the lp_balance, like 99~99.7%
status,hash = unstake(w3,lp_list=lp_lists, withdraw_list=lp_balances, walletID=id, trade_contract_w3=trade_cont, max_sliappage=250,
                walletPrivateKey=pk,gas_buff=1.2,chain_id=56,td=100000)

print("$$$$$$$$$$$$$$$$$")
print(hash) # can copy and paste to look up from bscscan
print(status) # 1 = success
print("$$$$$$$$$$$$$$$$$")