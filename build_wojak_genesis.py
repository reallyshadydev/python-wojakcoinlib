#!/usr/bin/env python3
"""Build Wojakcoin mainnet genesis block from wojakcore chainparams and print hex.
   Match: CreateGenesisBlock(1501724714, 1252099851, 0x1d00ffff, 1, 100*COIN)
   timestamp "382017 Price Phillip Retires", pubkey 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
   Expected hash: 000000004536a4f8fa9d88f0001ca9f9825f8d9fd3ba6383a2f030c0427bf085
"""
import sys
sys.path.insert(0, '.')

from bitcoin.core import (
    COIN, x, lx, b2lx, CBlock, CBlockHeader, CTransaction, CTxIn, CTxOut,
    COutPoint, CMutableTransaction, CMutableTxIn, CMutableTxOut,
    Hash, CTxWitness,
)
from bitcoin.core.script import CScript, OP_CHECKSIG

# Coinbase scriptSig: 486604799, 4, "382017 Price Phillip Retires"
scriptSig = CScript(
    bytes([0x04]) + (486604799).to_bytes(4, 'little') +  # push 4 bytes (nBits)
    bytes([0x04]) +  # CScriptNum(4)
    bytes([0x1a]) + b"382017 Price Phillip Retires"  # push 26 bytes
)
# scriptPubKey: pubkey OP_CHECKSIG
pubkey = bytes.fromhex("04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f")
scriptPubKey = CScript([pubkey, OP_CHECKSIG])

coinbase = CTransaction(
    vin=[CTxIn(prevout=COutPoint(), scriptSig=scriptSig, nSequence=0xffffffff)],
    vout=[CTxOut(nValue=100 * COIN, scriptPubKey=scriptPubKey)],
    nLockTime=0,
    nVersion=1,
    witness=CTxWitness(),
)
txid = coinbase.GetTxid()
# Merkle root for single-tx block is the txid
merkle_root = txid

header = CBlockHeader(
    nVersion=1,
    hashPrevBlock=b'\x00'*32,
    hashMerkleRoot=merkle_root,
    nTime=1501724714,
    nBits=0x1d00ffff,
    nNonce=1252099851,
)
genesis = CBlock(
    nVersion=1,
    hashPrevBlock=b'\x00'*32,
    hashMerkleRoot=merkle_root,
    nTime=1501724714,
    nBits=0x1d00ffff,
    nNonce=1252099851,
    vtx=[coinbase],
)

genesis_hex = genesis.serialize().hex()
print("GENESIS_HEX:", genesis_hex)
print("Block hash:", b2lx(genesis.GetHash()))
expected = "000000004536a4f8fa9d88f0001ca9f9825f8d9fd3ba6383a2f030c0427bf085"
actual = b2lx(genesis.GetHash())
if actual == expected:
    print("Hash matches wojakcore genesis.")
else:
    print("Expected:", expected)
    sys.exit(1)
