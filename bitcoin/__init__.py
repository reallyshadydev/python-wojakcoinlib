# Copyright (C) The python-bitcoinlib developers
# Fork for Wojakcoin (WJK): python-wojakcoinlib
#
# This file is part of python-wojakcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-wojakcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.


import bitcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.12.2'

# Wojakcoin (WJK) chain parameters - match wojakcore chainparams
# Mainnet: magic 0x6f8da579, address prefix 0x49 (W), script 0x05, WIF 0xc9, bech32 'bc'
class MainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\x6f\x8d\xa5\x79'
    DEFAULT_PORT = 20761
    RPC_PORT = 20760
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR': 0x49,
                       'SCRIPT_ADDR': 5,
                       'SECRET_KEY': 0xc9}
    BECH32_HRP = 'bc'

class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x4d\xaa\x61\xf9'
    DEFAULT_PORT = 30761
    RPC_PORT = 30760
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR': 111,
                       'SCRIPT_ADDR': 196,
                       'SECRET_KEY': 239}
    BECH32_HRP = 'tb'

class SigNetParams(bitcoin.core.CoreSigNetParams):
    MESSAGE_START = b'\xfc\xc1\xb7\xdc'
    DEFAULT_PORT = 30761
    RPC_PORT = 30760
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR': 111,
                       'SCRIPT_ADDR': 196,
                       'SECRET_KEY': 239}
    BECH32_HRP = 'tb'

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 30761
    RPC_PORT = 30760
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR': 111,
                       'SCRIPT_ADDR': 196,
                       'SECRET_KEY': 239}
    BECH32_HRP = 'bcrt'

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', 'regtest', or 'signet'

    Default chain is 'mainnet' (Wojakcoin).
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = bitcoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = bitcoin.core.coreparams = RegTestParams()
    elif name == 'signet':
        params = bitcoin.core.coreparams = SigNetParams()
    else:
        raise ValueError('Unknown chain %r' % name)
