import os
from typing import Optional

from pyarcticspas import AsyncSpa

singleton_spa: Optional[AsyncSpa] = None


def get_spa():
    global singleton_spa
    if singleton_spa is None:
        token = os.environ.get("ARCTICSPAS_TOKEN")
        assert token is not None
        singleton_spa = AsyncSpa(token)
    return singleton_spa


async def test_connected():
    spa = get_spa()
    status = await spa.status()
    assert status.connected is True
