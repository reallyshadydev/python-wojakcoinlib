#!/usr/bin/env python3
"""Test Wojakcoin mainnet genesis block (from wojakcore chainparams)."""
import unittest
import bitcoin
from bitcoin.core import CBlock, b2lx, lx

class Test_WojakcoinGenesis(unittest.TestCase):
    def test_genesis_hash_matches_wojakcore(self):
        bitcoin.SelectParams('mainnet')
        genesis = bitcoin.params.GENESIS_BLOCK
        self.assertEqual(
            genesis.GetHash(),
            lx('000000004536a4f8fa9d88f0001ca9f9825f8d9fd3ba6383a2f030c0427bf085'),
            'Genesis block hash must match wojakcore chainparams'
        )

    def test_genesis_merkle_root(self):
        bitcoin.SelectParams('mainnet')
        genesis = bitcoin.params.GENESIS_BLOCK
        self.assertEqual(
            b2lx(genesis.hashMerkleRoot),
            '2d94b8253252a0bf3c5202b26388dd3c468ab0bec4aad107b84d46ef6e8b791a',
            'Merkle root must match wojakcore'
        )

    def test_genesis_roundtrip(self):
        bitcoin.SelectParams('mainnet')
        genesis = bitcoin.params.GENESIS_BLOCK
        ser = genesis.serialize()
        genesis2 = CBlock.deserialize(ser)
        self.assertEqual(genesis2.GetHash(), genesis.GetHash())
        self.assertEqual(genesis2.serialize(), ser)

if __name__ == '__main__':
    unittest.main()
