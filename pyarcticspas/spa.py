""" Spa class creates an Arctic Spa connection for Python calls """
import email.message
from http import HTTPStatus
from typing import Optional
from urllib.error import HTTPError

from arcticspas import Client
from arcticspas.api.spa_control import (
    v2_blower,
    v2_boost,
    v2_easy_mode,
    v2_filter,
    v2_fogger,
    v2_light,
    v2_pump,
    v2_spa,
    v2_temperature,
    v2sds,
    v2yess,
)
from arcticspas.models import V2BlowerBlower as Blower
from arcticspas.models import V2BlowerJsonBody
from arcticspas.models import V2BlowerJsonBodyState as BlowerState
from arcticspas.models import V2EasyModeJsonBody
from arcticspas.models import V2EasyModeJsonBodyState as EasyModeState
from arcticspas.models import V2FilterJsonBody
from arcticspas.models import V2FilterJsonBodyState as FilterState
from arcticspas.models import V2FoggerJsonBody
from arcticspas.models import V2FoggerJsonBodyState as FoggerState
from arcticspas.models import V2LightJsonBody
from arcticspas.models import V2LightJsonBodyState as LightState
from arcticspas.models import V2PumpJsonBody
from arcticspas.models import V2PumpJsonBodyState as PumpState
from arcticspas.models import V2PumpPump as Pump
from arcticspas.models import V2SDSJsonBody
from arcticspas.models import V2SDSJsonBodyState as SDSState
from arcticspas.models import V2SpaResponse200 as SpaResponse
from arcticspas.models import V2TemperatureJsonBody, V2YESSJsonBody
from arcticspas.models import V2YESSJsonBodyState as YESSState
from arcticspas.types import Response

from .const import _url


def _filter_parsed(response: Response):
    """Filter out the parsed content from an API response and raise a HTTPError, if necessary."""
    if response.status_code == HTTPStatus.OK:
        return response.parsed
    else:
        msg = email.message.Message()
        for k, v in response.headers.items():
            msg.set_raw(k, v)
        raise HTTPError(_url, response.status_code, HTTPStatus(response.status_code).phrase, msg, None)


class Spa:
    def __init__(self, token: str):
        self.__client = Client(base_url=_url, headers={"X-API-KEY": token})

    def status(self) -> SpaResponse:
        return _filter_parsed(v2_spa.sync_detailed(client=self.__client))

    async def async_status(self):
        return _filter_parsed(await v2_spa.asyncio_detailed(client=self.__client))

    def set_temperature(self, setpoint_f: int):
        json_body = V2TemperatureJsonBody()
        json_body.setpoint_f = setpoint_f
        return _filter_parsed(v2_temperature.sync_detailed(client=self.__client, json_body=json_body))

    async def async_set_temperature(self, setpoint_f: int):
        json_body = V2TemperatureJsonBody()
        json_body.setpoint_f = setpoint_f
        return _filter_parsed(await v2_temperature.asyncio_detailed(client=self.__client, json_body=json_body))

    def set_lights(self, state: LightState):
        json_body = V2LightJsonBody()
        json_body.state = state
        return _filter_parsed(v2_light.sync_detailed(client=self.__client, json_body=json_body))

    async def async_set_lights(self, state: LightState):
        json_body = V2LightJsonBody()
        json_body.state = state
        return _filter_parsed(await v2_light.asyncio_detailed(client=self.__client, json_body=json_body))

    def set_pumps(self, pump: Pump, state: PumpState):
        json_body = V2PumpJsonBody()
        json_body.state = state
        return _filter_parsed(v2_pump.sync_detailed(pump=pump, client=self.__client, json_body=json_body))

    async def async_set_pumps(self, pump: Pump, state: PumpState):
        json_body = V2PumpJsonBody()
        json_body.state = state
        return _filter_parsed(await v2_pump.asyncio_detailed(pump=pump, client=self.__client, json_body=json_body))

    def set_easymode(self, state: EasyModeState):
        json_body = V2EasyModeJsonBody()
        json_body.state = state
        return _filter_parsed(v2_easy_mode.sync_detailed(client=self.__client, json_body=json_body))

    async def async_set_easymode(self, state: EasyModeState):
        json_body = V2EasyModeJsonBody()
        json_body.state = state
        return _filter_parsed(await v2_easy_mode.asyncio_detailed(client=self.__client, json_body=json_body))

    def set_sds(self, state: SDSState):
        json_body = V2SDSJsonBody()
        json_body.state = state
        return _filter_parsed(v2sds.sync_detailed(client=self.__client, json_body=json_body))

    async def async_set_sds(self, state: SDSState):
        json_body = V2SDSJsonBody()
        json_body.state = state
        return _filter_parsed(await v2sds.asyncio_detailed(client=self.__client, json_body=json_body))

    def set_yess(self, state: YESSState):
        json_body = V2YESSJsonBody()
        json_body.state = state
        return _filter_parsed(v2yess.sync_detailed(client=self.__client, json_body=json_body))

    async def async_set_yess(self, state: YESSState):
        json_body = V2YESSJsonBody()
        json_body.state = state
        return _filter_parsed(await v2yess.asyncio_detailed(client=self.__client, json_body=json_body))

    def boost(self):
        return _filter_parsed(v2_boost.sync_detailed(client=self.__client))

    async def async_boost(self):
        return _filter_parsed(await v2_boost.asyncio_detailed(client=self.__client))

    def set_fogger(self, state: FoggerState):
        json_body = V2FoggerJsonBody()
        json_body.state = state
        return _filter_parsed(v2_fogger.sync_detailed(client=self.__client, json_body=json_body))

    async def async_set_fogger(self, state: FoggerState):
        json_body = V2FoggerJsonBody()
        json_body.state = state
        return _filter_parsed(await v2_fogger.asyncio_detailed(client=self.__client, json_body=json_body))

    def set_blowers(self, blower: Blower, state: BlowerState):
        json_body = V2BlowerJsonBody()
        json_body.state = state
        return _filter_parsed(v2_blower.sync_detailed(blower=blower, client=self.__client, json_body=json_body))

    async def async_set_blowers(self, blower: Blower, state: BlowerState):
        json_body = V2BlowerJsonBody()
        json_body.state = state
        return _filter_parsed(
            await v2_blower.asyncio_detailed(blower=blower, client=self.__client, json_body=json_body)
        )

    def set_filter(
        self,
        state: Optional[FilterState] = None,
        frequency: Optional[int] = None,
        duration: Optional[int] = None,
        suspension: Optional[bool] = None,
    ):
        json_body = V2FilterJsonBody()
        if state is not None:
            json_body.state = state
        if frequency is not None:
            json_body.frequency = frequency
        if duration is not None:
            json_body.duration = duration
        if suspension is not None:
            json_body.suspension = suspension
        return _filter_parsed(v2_filter.sync_detailed(client=self.__client, json_body=json_body))

    async def async_set_filter(
        self,
        state: Optional[FilterState] = None,
        frequency: Optional[int] = None,
        duration: Optional[int] = None,
        suspension: Optional[bool] = None,
    ):
        json_body = V2FilterJsonBody()
        if state is not None:
            json_body.state = state
        if frequency is not None:
            json_body.frequency = frequency
        if duration is not None:
            json_body.duration = duration
        if suspension is not None:
            json_body.suspension = suspension
        return _filter_parsed(await v2_filter.asyncio_detailed(client=self.__client, json_body=json_body))
