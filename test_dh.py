#  Copyright (c) Kuba Szczodrzyński 2021-5-5.

import pytest

from diffiehellman import DiffieHellman
from diffiehellman.primes import PRIMES


@pytest.mark.parametrize("group", PRIMES.keys())
def test_shared_key(group: int):
    dh1 = DiffieHellman(group=group)
    dh2 = DiffieHellman(group=group)

    dh1_public = dh1.get_public_key()
    dh2_public = dh2.get_public_key()

    dh1_shared = dh1.generate_shared_key(dh2_public)
    dh2_shared = dh2.generate_shared_key(dh1_public)

    assert dh1_shared == dh2_shared
