"""Notify template service notification service."""
import logging

import voluptuous as vol

from homeassistant.components.notify import (
    ATTR_DATA,
    PLATFORM_SCHEMA,
    BaseNotificationService,
)
from homeassistant.const import CONF_SERVICE
from homeassistant.core import HomeAssistant, split_entity_id
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

# PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({vol.Required(CONF_API_KEY): cv.string})
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({vol.Required(CONF_SERVICE): cv.string})


async def async_get_service(hass, config, discovery_info=None):
    """Set up the service notification service."""
    return ServiceNotificationService(hass, config[CONF_SERVICE])


class ServiceNotificationService(BaseNotificationService):
    """Define the logic of the service notification service."""

    def __init__(self, hass: HomeAssistant, service):
        """Initialize the service."""
        self._hass = hass
        self._service = service

    async def async_send_message(self, message, **kwargs):
        """Actually call the service."""
        domain, object_id = split_entity_id(self._service)

        data = kwargs.get(ATTR_DATA)

        await self._hass.services.async_call(
            domain,
            object_id,
            data,
        )
