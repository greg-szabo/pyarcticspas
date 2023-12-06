import os
import time
from typing import Optional

from pyarcticspas import LightState, Spa

singleton_spa: Optional[Spa] = None


def get_spa():
    global singleton_spa
    if singleton_spa is None:
        token = os.environ.get("ARCTICSPAS_TOKEN")
        assert token is not None
        singleton_spa = Spa(token)
    return singleton_spa


def test_connected():
    spa = get_spa()
    status = spa.status()
    assert status.connected is True


def test_lights():
    # Query light status
    spa = get_spa()
    spa_status = spa.status()
    assert spa_status.lights == LightState["ON"] or spa_status.lights == LightState["OFF"]

    # Create expected new state
    new_light_state = LightState["ON"]
    if spa_status.lights == LightState["ON"]:
        new_light_state = LightState["OFF"]

    # Send expected new state
    spa.set_lights(new_light_state)

    # Query light status again
    time.sleep(2)
    new_spa_status = spa.status()
    assert new_spa_status.lights == new_light_state.value
