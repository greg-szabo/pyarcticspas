import os
from typing import Optional

import pytest

from pyarcticspas import Pump, PumpState, Spa

singleton_spa: Optional[Spa] = None
pytest_plugins = ("pytest_asyncio",)


def get_spa():
    global singleton_spa
    if singleton_spa is None:
        token = os.environ.get("ARCTICSPAS_TOKEN")
        assert token is not None
        singleton_spa = Spa(token)
    return singleton_spa


# Todo: async calls are not working as expected. There is some issue with the underlying httpx reporting an exception.
# @pytest.mark.asyncio
# async def test_async_connected():
#     spa = get_spa()
#     status = await spa.async_status()
#     assert status.connected is True


@pytest.mark.asyncio
async def test_async_pump_turn_off():
    spa = get_spa()
    spa_status = await spa.async_status()
    assert spa_status.connected is True
    assert spa_status.pump1 == PumpState["ON"] or spa_status.pump1 == PumpState["OFF"]

    if spa_status.pump1 == PumpState["ON"]:
        await spa.async_set_pumps(Pump["VALUE_0"], PumpState["OFF"])

        spa_new_status = await spa.async_status()
        assert spa_new_status.pump1 == PumpState["OFF"]
