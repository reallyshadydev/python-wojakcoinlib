# python-wojakcoinlib

Fork of [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib) for **Wojakcoin (WJK)**.

This Python3 library provides an easy interface to Wojakcoin data structures and protocol. The approach is low-level and "ground up", with a focus on providing tools to manipulate the internals of how Wojakcoin works.

## Requirements

    sudo apt-get install libssl-dev

The RPC interface, `bitcoin.rpc`, should work with **Wojakcoin Core (wojakcoind)** v1.x or later. By default it looks for config and cookie file under `~/.wojakcoin/` (Linux), `~/Library/Application Support/Wojakcoin/` (macOS), or `%APPDATA%\Wojakcoin` (Windows).

## Chain parameters (Wojakcoin)

- **Mainnet**: RPC port 20760, P2P port 20761, magic `0x6f8da579`, address prefix 0x49 (W), bech32 `bc`
- **Testnet / Signet / Regtest**: RPC port 30760, P2P 30761

## Structure

Everything consensus critical is found in the modules under bitcoin.core. Non-consensus critical modules:

- `bitcoin`          - Chain selection (Wojakcoin mainnet/testnet/regtest/signet)
- `bitcoin.base58`   - Base58 encoding
- `bitcoin.bech32`   - Bech32
- `bitcoin.rpc`      - Wojakcoin Core RPC interface support
- `bitcoin.wallet`   - Address and private key support

## Selecting the chain

    import bitcoin
    bitcoin.SelectParams('mainnet')   # Wojakcoin mainnet (default)
    bitcoin.SelectParams('testnet')
    bitcoin.SelectParams('regtest')
    bitcoin.SelectParams('signet')

## Unit tests

    python3 -m unittest discover

Or with Tox:

    ./runtests.sh

## License

Same as python-bitcoinlib (see LICENSE). This fork is maintained for Wojakcoin at [github.com/reallyshadydev/python-wojakcoinlib](https://github.com/reallyshadydev/python-wojakcoinlib).
