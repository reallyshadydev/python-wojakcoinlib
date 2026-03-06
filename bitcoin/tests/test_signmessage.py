# Copyright (C) The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.


import unittest
import os
import json

from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.signmessage import BitcoinMessage, VerifyMessage, SignMessage


def _wif_to_wojak_wif(wif_str):
    """Decode any base58check WIF and re-encode with current (Wojakcoin) SECRET_KEY version."""
    from bitcoin.base58 import decode
    from bitcoin.core import Hash
    raw = decode(wif_str)
    if raw[-4:] != Hash(raw[:-4])[:4]:
        raise ValueError('Invalid WIF checksum')
    secret = raw[1:33]
    compressed = len(raw) == 38 and raw[33] == 1
    return str(CBitcoinSecret.from_secret_bytes(secret, compressed))


def load_test_vectors(name):
    with open(os.path.dirname(__file__) + '/data/' + name, 'r') as fd:
        return json.load(fd)


class Test_SignVerifyMessage(unittest.TestCase):
    def test_verify_message_simple(self):
        """Verify a message signed with Wojakcoin key and message magic."""
        wojak_wif = _wif_to_wojak_wif("L4vB5fomsK8L95wQ7GFzvErYGht49JsCPJyJMHpB4xGM6xgi2jvG")
        key = CBitcoinSecret(wojak_wif)
        address = str(P2PKHBitcoinAddress.from_pubkey(key.pub))
        message = BitcoinMessage(address)
        signature = SignMessage(key, message)
        self.assertTrue(signature)
        self.assertTrue(VerifyMessage(address, message, signature))

    @unittest.skip("Bitcoin signmessage vectors; use Wojakcoin-specific vectors to test")
    def test_verify_message_vectors(self):
        for vector in load_test_vectors('signmessage.json'):
            message = BitcoinMessage(vector['address'])
            self.assertTrue(VerifyMessage(vector['address'], message, vector['signature']))

    def test_sign_message_simple(self):
        wojak_wif = _wif_to_wojak_wif("L4vB5fomsK8L95wQ7GFzvErYGht49JsCPJyJMHpB4xGM6xgi2jvG")
        key = CBitcoinSecret(wojak_wif)
        address = str(P2PKHBitcoinAddress.from_pubkey(key.pub))
        message = BitcoinMessage(address)
        signature = SignMessage(key, message)

        self.assertTrue(signature)
        self.assertTrue(VerifyMessage(address, message, signature))

    @unittest.skip("Bitcoin signmessage vectors; use Wojakcoin-specific vectors to test")
    def test_sign_message_vectors(self):
        for vector in load_test_vectors('signmessage.json'):
            key = CBitcoinSecret(vector['wif'])
            message = BitcoinMessage(vector['address'])

            signature = SignMessage(key, message)

            self.assertTrue(signature, "Failed to sign for [%s]" % vector['address'])
            self.assertTrue(VerifyMessage(vector['address'], message, vector['signature']), "Failed to verify signature for [%s]" % vector['address'])


if __name__ == "__main__":
    unittest.main()
