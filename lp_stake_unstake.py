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
    assert key_reserve_list is not None
    krl=len(key_reserve_list)
    idx = randint(0,krl-1)
    w3_instance = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + key_reserve_list[idx]))
    for i in range(len(key_reserve_list)-1):
        try:
            if w3_instance.isConnected():
                if debug:
                    print("Connected with :",key_reserve_list[idx])
                return w3_instance
            else:
                idx = randint(0, krl - 1)
                w3_instance = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + key_reserve_list[idx]))
        except:
            idx = randint(0, krl - 1)
            w3_instance = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + key_reserve_list[idx]))
    if w3_instance.isConnected():
        if debug:
            print("Connected with :", key_reserve_list[idx])
        return w3_instance
    else:
        print("Error : None of w3 keys are working.")
        raise ValueError


def create_stake_contract(w3=None):
    if w3 is None:
        w3 = create_w3_from_reserve(key_reserve_list=INFURA_KEY_RESERVE)
    stake_addr = "0xdE4C0eC4e7b0593060C4D46cD797bD7ab0D80E99"
    stake_abi_str = '[{"inputs":[{"internalType":"address","name":"_swap","type":"address"},{"internalType":"address","name":"_storage","type":"address"},{"internalType":"address","name":"_price","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"amt_lp_balance","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amt_eth","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lp_usd_unit","type":"uint256"}],"name":"StakeEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"amt_lp_balance","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amt_eth","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lp_usd_unit","type":"uint256"}],"name":"WithdrawEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"bool","name":"isProfit","type":"bool"},{"indexed":false,"internalType":"uint256","name":"profit","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"eth","type":"uint256"}],"name":"WithdrawProfitEvent","type":"event"},{"inputs":[{"internalType":"address","name":"_pair","type":"address"}],"name":"CheckTokensFromPair","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"MinAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_target1","type":"address"},{"internalType":"address","name":"_target2","type":"address"},{"internalType":"address","name":"_target3","type":"address"},{"internalType":"address","name":"_target4","type":"address"},{"internalType":"address","name":"_target5","type":"address"}],"name":"SetPara","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_pair_list","type":"address[]"},{"internalType":"uint256[]","name":"_amt_list","type":"uint256[]"},{"internalType":"uint256","name":"_max_slippage","type":"uint256"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"StakeList","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_pair_list","type":"address[]"},{"internalType":"uint256[]","name":"_amt_list","type":"uint256[]"},{"internalType":"uint256","name":"_max_slippage","type":"uint256"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"UnstakeList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"deadline","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"emergencyTokenWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"kill","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"maxSlippage","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"percentage_unit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rout","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"storage_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"swap_","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

    stake_abi = json.loads(stake_abi_str)
    stake = w3.eth.contract(address=stake_addr, abi=stake_abi)
    return stake



def unstake(w3, lp_list=None, withdraw_list=None, walletID=None, stake_contract_w3=None, max_sliappage=250,
              walletPrivateKey=None, gas_buff=1.05, chain_id=42,td=4000):
    # chain id 42 : kovan testnet
    # chain id 1 : mainnnet
    if stake_contract_w3 is None:
        stake_contract_w3 = create_stake_contract(w3 = w3)

    nonce = w3.eth.getTransactionCount(walletID)
    current_gas = requests.get("https://ethgasstation.info/api/ethgasAPI.json").json()

    gasPrice = int((current_gas['average']) / 10)
    gasPrice = Web3.toWei(gasPrice, 'gwei')

    gas_est = stake_contract_w3.functions.UnstakeList(lp_list, withdraw_list,
                                                      max_sliappage, int(datetime.utcnow().timestamp() + 4000) + td*len(lp_list)) \
        .estimateGas({'from': walletID,
                      #'chainId': chain_id,
                      })
    tx = stake_contract_w3.functions.UnstakeList(lp_list, withdraw_list,
                                                 max_sliappage, int(datetime.utcnow().timestamp() + 4000) + td*len(lp_list)) \
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
def get_all_lp_balance(pair_list=None, w3=None, wallet_addr=None):
    pair_cont_list = []
    uniswap_pair_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
    uniswap_pair_abi = json.loads(uniswap_pair_abi)
    for p in pair_list:
        pair_cont_list.append(w3.eth.contract(address=p, abi=uniswap_pair_abi))
    lp_balance_list = []
    for pc in pair_cont_list:
        lp_balance_list.append(pc.functions.balanceOf(wallet_addr).call())
    return lp_balance_list
def create_storage_contract(w3=None):
    if w3 is None:
        w3 = create_w3_from_reserve(key_reserve_list=INFURA_KEY_RESERVE)
    storage_addr = "0xC3eDf24036150B7d90724007a767644812C5973B"
    storage_abi_str = '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_target","type":"address"}],"name":"Log","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"WhitelistAdminAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"WhitelistAdminRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"WhitelistedAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"WhitelistedRemoved","type":"event"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"address","name":"_pair","type":"address"},{"internalType":"uint256","name":"_amt","type":"uint256"}],"name":"AddTokenBalance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"address","name":"_pair","type":"address"},{"internalType":"uint256","name":"_amt","type":"uint256"}],"name":"AddUSDUnitPrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"GetInvestList","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"address","name":"_pair","type":"address"}],"name":"GetTokenBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"address","name":"_pair","type":"address"}],"name":"GetUSDUnitPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"address","name":"_target","type":"address"},{"internalType":"uint256","name":"_amt","type":"uint256"}],"name":"Send","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"address","name":"_pair","type":"address"},{"internalType":"uint256","name":"_new_balance","type":"uint256"}],"name":"SetTokenBalance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"address","name":"_pair","type":"address"},{"internalType":"uint256","name":"_amt","type":"uint256"}],"name":"SubUSDUnitPrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"address","name":"_pair","type":"address"},{"internalType":"uint256","name":"_amt","type":"uint256"},{"internalType":"uint256","name":"_amtUSD","type":"uint256"}],"name":"UpdateUSDUnitPrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"addWhitelistAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"addWhitelisted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"emergencyETHWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"emergencyTokenWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isWhitelistAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isWhitelisted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"removeWhitelisted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceWhitelistAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceWhitelisted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"selfDesturctor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
    storage_abi = json.loads(storage_abi_str)
    storage = w3.eth.contract(address=storage_addr, abi=storage_abi)
    return storage
def create_withdraw_lp_list(walletID=None, storage_contract_w3=None):
    if storage_contract_w3 is None:
        storage_contract_w3 = create_storage_contract()
    lp_list = storage_contract_w3.functions.GetInvestList(walletID).call()
    rl = []
    for l in lp_list:
        if (l != '0x0000000000000000000000000000000000000000'):
            rl.append(l)
    return rl


def create_withdraw_lists(lp_list=None, walletID=None, storage_contract_w3=None, ratio=1.0):
    assert ratio <= 1.0 and ratio > 0
    if storage_contract_w3 is None:
        storage_contract_w3 = create_storage_contract()
    rl = []
    for l in lp_list:
        cur_balance = storage_contract_w3.functions.GetTokenBalance(walletID, l).call()
        rl.append(int(round(ratio * cur_balance)))
    return rl

def stake(w3, pair_list=None, wei_list=None, walletID=None, stake_contract_w3=None, max_sliappage=200,
            walletPrivateKey=None, gas_buff=1.05, chain_id=42):
    if stake_contract_w3 is None:
        stake_contract_w3 = create_stake_contract(w3 = w3)
    nonce = w3.eth.getTransactionCount(walletID)
    print("Chain ID: ", chain_id)
    current_gas = requests.get("https://ethgasstation.info/api/ethgasAPI.json").json()
    # avgGasPrice = int((current_gas['average']) / 10)
    # fastGasPrice = int((current_gas['fast']) / 10)
    current_gas = requests.get("https://ethgasstation.info/api/ethgasAPI.json").json()

    gasPrice = int((current_gas['average']) / 10)
    gasPrice = Web3.toWei(gasPrice, 'gwei')

    amount_wei = int(sum(wei_list))
    gas_est = stake_contract_w3.functions.StakeList(pair_list, wei_list, max_sliappage, int(
        datetime.utcnow().timestamp() * 1000) + 4000*len(pair_list)) \
        .estimateGas({'from': walletID,
                      #'chainId': chain_id,
                      'value': amount_wei
                      })
    print(gas_est)
    #exit()
    tx = stake_contract_w3.functions.StakeList(pair_list, wei_list, max_sliappage, int(
        datetime.utcnow().timestamp() * 1000) + 4000*len(pair_list)) \
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

def get_all_lp_bal_2(walletID=None, storage_contract_w3=None, lpl=None):
    if lpl is None:
        lpl = create_withdraw_lp_list(walletID=walletID, storage_contract_w3=storage_contract_w3)
    wdl = create_withdraw_lists(lp_list=lpl, walletID=walletID, storage_contract_w3=storage_contract_w3, ratio=1.0)
    return lpl, wdl
def show_balance(wallet_addr):
    w3= create_w3_from_reserve(key_reserve_list=INFURA_KEY_RESERVE)
    st_addr ="0xC3eDf24036150B7d90724007a767644812C5973B"
    storage_abi_str = '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_target","type":"address"}],' \
                      '"name":"Log","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address",' \
                      '"name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner",' \
                      '"type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":' \
                      '[{"indexed":true,"internalType":"address","name":"account","type":"address"}],"name":"WhitelistAdminAdded"' \
                      ',"type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account",' \
                      '"type":"address"}],"name":"WhitelistAdminRemoved","type":"event"},{"anonymous":false,"i' \
                      'nputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],' \
                      '"name":"WhitelistedAdded","type":"event"},{"anonymous":false,' \
                      '"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"}],' \
                      '"name":"WhitelistedRemoved","type":"event"},{"inputs":[{"internalType":"address",' \
                      '"name":"_target","type":"address"},{"internalType":"address","name":"_pair",' \
                      '"type":"address"},{"internalType":"uint256","name":"_amt","type":"uint256"}],' \
                      '"name":"AddTokenBalance","outputs":[],"stateMutability":"nonpayable",' \
                      '"type":"function"},{"inputs":[{"internalType":"address","name":"' \
                      '_target","type":"address"},{"internalType":"address","name":"_pair","type":"address"}' \
                      ',{"internalType":"uint256","name":"_amt","type":"uint256"}],"name":"AddUSDUnitPrice",' \
                      '"outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":' \
                      '[{"internalType":"address","name":"user","type":"address"}],"name":"GetInvestList"' \
                      ',"outputs":[{"internalType":"address[]","name":"","type":"address[]"}],' \
                      '"stateMutability":"view","type":"function"},' \
                      '{"inputs":[{"internalType":"address","name":"_target","type":"address"},' \
                      '{"internalType":"address","name":"_pair","type":"address"}],' \
                      '"name":"GetTokenBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
                      '"stateMutability":"view","type":"function"},' \
                      '{"inputs":[{"internalType":"address","name":"_target","type":"address"},' \
                      '{"internalType":"address","name":"_pair","type":"address"}],' \
                      '"name":"GetUSDUnitPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
                      '"stateMutability":"view","type":"function"},' \
                      '{"inputs":[{"internalType":"address","name":"_token","type":"address"},' \
                      '{"internalType":"address","name":"_target","type":"address"},' \
                      '{"internalType":"uint256","name":"_amt","type":"uint256"}],' \
                      '"name":"Send","outputs":[],"stateMutability":"nonpayable","type":"function"},' \
                      '{"inputs":[{"internalType":"address","name":"_target","type":"address"},' \
                      '{"internalType":"address","name":"_pair","type":"address"},' \
                      '{"internalType":"uint256","name":"_new_balance","type":"uint256"}],' \
                      '"name":"SetTokenBalance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"address","name":"_pair","type":"address"},{"internalType":"uint256","name":"_amt","type":"uint256"}],"name":"SubUSDUnitPrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_target","type":"address"},{"internalType":"address","name":"_pair","type":"address"},{"internalType":"uint256","name":"_amt","type":"uint256"},{"internalType":"uint256","name":"_amtUSD","type":"uint256"}],"name":"UpdateUSDUnitPrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"addWhitelistAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"addWhitelisted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"emergencyETHWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"emergencyTokenWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isWhitelistAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isWhitelisted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"removeWhitelisted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceWhitelistAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceWhitelisted","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"selfDesturctor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
    storage_abi = json.loads(storage_abi_str)
    storage = w3.eth.contract(address=st_addr, abi=storage_abi)

    lp_list = storage.functions.GetInvestList(wallet_addr).call()
    tb=[]
    for lp in lp_list:
        tb.append(storage.functions.GetTokenBalance(wallet_addr, lp).call())
    price_addr = "0x6Ff2BB2f92E29a2A2E5Fc17e1d0aE5beD4D46240"
    # price_abi_str = '[{"inputs":[],"name":"emergencyETHWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"emergencyTokenWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"selfDesturctor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetETHthreshold","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"SetFactory","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetFeeUnit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetPoolFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"SetRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetStakeVolFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetSwapFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetUnstakeProfitFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetUnstakeVolFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_target1","type":"address"},{"internalType":"address","name":"_target2","type":"address"},{"internalType":"address","name":"_target3","type":"address"}],"name":"SetUSD","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"},{"inputs":[],"name":"DAI","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"eth_thr","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"qty","type":"uint256"},{"internalType":"address","name":"crypto","type":"address"}],"name":"getEstimatedETHforToken","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"qty","type":"uint256"},{"internalType":"address","name":"crypto","type":"address"}],"name":"getEstimatedTokenForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pair","type":"address"},{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"GetLPPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_pair","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"GetLPWorth","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pair","type":"address"}],"name":"GetPairName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pair","type":"address"}],"name":"GetReserves","outputs":[{"internalType":"uint112","name":"reserve0","type":"uint112"},{"internalType":"uint112","name":"reserve1","type":"uint112"},{"internalType":"uint32","name":"blockTimestampLast","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pair","type":"address"}],"name":"GetTotal","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lp_stake_vol_fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lp_unstake_profit_fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lp_unstake_vol_fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"percentage_unit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pool_fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rout","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"swap_fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"TakeStakeVolFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"TakeSwapFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"invest_amt","type":"uint256"},{"internalType":"uint256","name":"curr_amt","type":"uint256"}],"name":"TakeUnstakeProfitFee","outputs":[{"internalType":"bool","name":"","type":"bool"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"TakeUnstakeVolFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"USD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"USDC","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"USDT","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'
    price_abi_str = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"DAI","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pair","type":"address"},{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"GetLPPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_pair","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"GetLPWorth","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pair","type":"address"}],"name":"GetPairName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pair","type":"address"}],"name":"GetReserves","outputs":[{"internalType":"uint112","name":"reserve0","type":"uint112"},{"internalType":"uint112","name":"reserve1","type":"uint112"},{"internalType":"uint32","name":"blockTimestampLast","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pair","type":"address"}],"name":"GetTotal","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetETHthreshold","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"SetFactory","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetFeeUnit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetPoolFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"SetRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetStakeVolFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetSwapFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_target1","type":"address"},{"internalType":"address","name":"_target2","type":"address"},{"internalType":"address","name":"_target3","type":"address"}],"name":"SetUSD","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetUnstakeProfitFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"target","type":"uint256"}],"name":"SetUnstakeVolFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"TakeStakeVolFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"TakeSwapFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"invest_amt","type":"uint256"},{"internalType":"uint256","name":"curr_amt","type":"uint256"}],"name":"TakeUnstakeProfitFee","outputs":[{"internalType":"bool","name":"","type":"bool"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"TakeUnstakeVolFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"USD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"USDC","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"USDT","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"emergencyETHWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"emergencyTokenWithdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"eth_thr","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"qty","type":"uint256"},{"internalType":"address","name":"crypto","type":"address"}],"name":"getEstimatedETHforToken","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"qty","type":"uint256"},{"internalType":"address","name":"crypto","type":"address"}],"name":"getEstimatedTokenForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lp_stake_vol_fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lp_unstake_profit_fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lp_unstake_vol_fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"percentage_unit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pool_fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rout","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"selfDesturctor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swap_fee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
    price_abi = json.loads(price_abi_str)
    price = w3.eth.contract(address=price_addr, abi=price_abi)
    lp_price=[]
    profits=[]
    invested=[]

    for pair_addr,amount in zip(lp_list,tb):
        # single_lp_price = price.functions.GetLPPrice(pair_addr,amount ).call()
        # single_lp_price = price.functions.GetLPPrice(pair_addr,amount ).call()
        single_lp_price = price.functions.GetLPPrice(pair_addr, int(math.pow(10, 24))).call() / math.pow(10, 24)
        lp_price.append(single_lp_price*amount)
        invested_usd = storage.functions.GetUSDUnitPrice(wallet_addr, pair_addr).call() \
                       / math.pow(10, 18) *amount
        invested.append(invested_usd)
        profits.append((single_lp_price*amount-invested_usd)/invested_usd)

    print(len(lp_list))
    print(lp_list)
    print(tb)
    print(profits)
    print(invested)
    print("shown ",lp_price)
    print("Total wealth in USD : ",np.sum(lp_price))
    return zip(lp_list,tb)
#
stake_cont = None
stor_cont = None
stor_addr="0xC3eDf24036150B7d90724007a767644812C5973B"

id='0x-------' # wallet address
pk='' # private key
w3=create_w3_from_reserve(key_reserve_list=INFURA_KEY_RESERVE)
block_number = w3.eth.getBlock('latest')['number']

print(block_number)

######### staking
investment_amount_eth = 5 # investing 5 ETH
BTC_ETH = to_checksum("0xbb2b8038a1640196fbe3e38816f3e67cba72d940")
ETH_USDT = to_checksum("0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852")
max_slippage = 200 # 200 = 20%
pair_list = [BTC_ETH,ETH_USDT]
num_splits = len(pair_list)
print("Investing in :", pair_list)
pair_n_l = []

print(pair_n_l)
print("Commence staking {} ETH....".format(investment_amount_eth))
stake_start_time = time.time()
wei_list = []
inv_indv = math.floor(investment_amount_eth * 1e18 / num_splits)
for i in range(num_splits):
    wei_list.append(inv_indv)
status, hash = stake(w3, pair_list=pair_list, wei_list=wei_list, walletID=id,
                               stake_contract_w3=stake_cont,
                               max_sliappage=max_slippage, walletPrivateKey=pk, gas_buff=1.2,
                               chain_id=1)
print("$$$$$$$$$$$$$$$$$")
print(hash) # can copy and paste to look up from etherscan
print(status) # 1 = success
print("$$$$$$$$$$$$$$$$$")

################## end staking
print("exiting here")
exit()

#### show balance
info=show_balance(id)
print("done showing balance in USD")

###### end show balance
print("exiting here")
exit()
#### unstake
if stake_cont is None:
    stake_cont = create_stake_contract(w3=w3)
if stor_cont is None:
    stor_cont = create_storage_contract(w3=w3)
lp_lists, lp_balances = get_all_lp_bal_2(walletID=id, storage_contract_w3=stor_cont)
print(lp_lists,lp_balances)
print("########################################")


print("LP pair lists:", lp_lists)
print("recorded user balance in contract:", lp_balances)
cont_balances=get_all_lp_balance(wallet_addr=stor_addr, pair_list=lp_lists, w3=w3)
print("balances of contract",cont_balances)
print("exiting here")
exit()

# lpl= [to_checksum("0xa478c2975ab1ea89e8196811f51a7b7ade33eb11"), to_checksum("0x86fef14c27c78deaeb4349fd959caa11fc5b5d75")] # pair address that you already staked. the LP token is in the smart contract, not in your wallet.
# wdl=[10000000, 10000000] # lp amount. it's usually a really big number.

# it's rare but sometimes there are weird pools among the ones tha take token as fees. in that case you need to withdraw smaller portion than 100% of the lp_balance, like 99~99.7%
status,hash = unstake(w3,lp_list=lp_lists, withdraw_list=lp_balances, walletID=id, stake_contract_w3=None, max_sliappage=100,
                walletPrivateKey=pk,gas_buff=1.2,chain_id=1,td=100000)

print("$$$$$$$$$$$$$$$$$")
print(hash) # can copy and paste to look up from etherscan
print(status) # 1 = success
print("$$$$$$$$$$$$$$$$$")