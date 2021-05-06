# py-diffie-hellman

[![PyPI](https://img.shields.io/pypi/v/py-diffie-hellman?style=for-the-badge)](https://pypi.org/project/py-diffie-hellman/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000?style=for-the-badge)](https://github.com/psf/black)

Python implementation of the [Diffie-Hellman key exchange protocol](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange).

Supports RFC 3526 MODP Groups 5, 14, 15, 16, 17, 18 (1536 to 8192 bit) and RFC 2409 Groups 1 and 2 (768 and 1024 bit).
The default group is 14 (2048-bit).

The key length in bits may be supplied to the constructor, defaults to 540-bit.

## Example
Encryption
```python
from diffiehellman import DiffieHellman

# automatically generate two key pairs
dh1 = DiffieHellman(group=14, key_bits=540)
dh2 = DiffieHellman(group=14, key_bits=540)

# get both public keys
dh1_public = dh1.get_public_key()
dh2_public = dh2.get_public_key()

# generate shared key based on the other side's public key
dh1_shared = dh1.generate_shared_key(dh2_public)
dh2_shared = dh2.generate_shared_key(dh1_public)

# the shared keys should be equal
assert dh1_shared == dh2_shared
```
