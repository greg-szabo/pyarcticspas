""" Spa class creates an Arctic Spa connection for synchronous Python calls """
from http import HTTPStatus
from typing import Optional

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
from arcticspas.models import V2SpaResponse200, V2TemperatureJsonBody, V2YESSJsonBody
from arcticspas.models import V2YESSJsonBodyState as YESSState
from arcticspas.types import Response

from .const import _url
from .error import SpaConnectionError


class Spa:
    def __init__(self, token: str):
        self.__client = Client(base_url=_url, headers={"X-API-KEY": token})

    def status(self):
        response: Response[V2SpaResponse200] = v2_spa.sync_detailed(client=self.__client)
        if response.status_code == HTTPStatus.OK:
            return response.parsed
        else:
            raise SpaConnectionError(response)

    def set_temperature(self, setpoint_f: int):
        json_body = V2TemperatureJsonBody()
        json_body.setpoint_f = setpoint_f
        response: Response[V2TemperatureJsonBody] = v2_temperature.sync_detailed(
            client=self.__client, json_body=json_body
        )
        if response.status_code != HTTPStatus.OK:
            raise SpaConnectionError(response)

    def set_lights(self, state: LightState):
        json_body = V2LightJsonBody()
        json_body.state = state
        response: Response[V2LightJsonBody] = v2_light.sync_detailed(client=self.__client, json_body=json_body)
        if response.status_code != HTTPStatus.OK:
            raise SpaConnectionError(response)

    def set_pumps(self, pump: Pump, state: PumpState):
        json_body = V2PumpJsonBody()
        json_body.state = state
        response: Response[V2PumpJsonBody] = v2_pump.sync_detailed(pump=pump, client=self.__client, json_body=json_body)
        if response.status_code != HTTPStatus.OK:
            raise SpaConnectionError(response)

    def set_easymode(self, state: EasyModeState):
        json_body = V2EasyModeJsonBody()
        json_body.state = state
        response: Response[V2EasyModeJsonBody] = v2_easy_mode.sync_detailed(client=self.__client, json_body=json_body)
        if response.status_code != HTTPStatus.OK:
            raise SpaConnectionError(response)

    def set_sds(self, state: SDSState):
        json_body = V2SDSJsonBody()
        json_body.state = state
        response: Response[V2SDSJsonBody] = v2sds.sync_detailed(client=self.__client, json_body=json_body)
        if response.status_code != HTTPStatus.OK:
            raise SpaConnectionError(response)

    def set_yess(self, state: YESSState):
        json_body = V2YESSJsonBody()
        json_body.state = state
        response: Response[V2YESSJsonBody] = v2yess.sync_detailed(client=self.__client, json_body=json_body)
        if response.status_code != HTTPStatus.OK:
            raise SpaConnectionError(response)

    def boost(self):
        response: Response[V2YESSJsonBody] = v2_boost.sync_detailed(client=self.__client)
        if response.status_code != HTTPStatus.OK:
            raise SpaConnectionError(response)

    def set_fogger(self, state: FoggerState):
        json_body = V2FoggerJsonBody()
        json_body.state = state
        response: Response[V2FoggerJsonBody] = v2_fogger.sync_detailed(client=self.__client, json_body=json_body)
        if response.status_code != HTTPStatus.OK:
            raise SpaConnectionError(response)

    def set_blowers(self, blower: Blower, state: BlowerState):
        json_body = V2BlowerJsonBody()
        json_body.state = state
        response: Response[V2BlowerJsonBody] = v2_blower.sync_detailed(
            blower=blower, client=self.__client, json_body=json_body
        )
        if response.status_code != HTTPStatus.OK:
            raise SpaConnectionError(response)

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
        response: Response[V2FilterJsonBody] = v2_filter.sync_detailed(client=self.__client, json_body=json_body)
        if response.status_code != HTTPStatus.OK:
            raise SpaConnectionError(response)
