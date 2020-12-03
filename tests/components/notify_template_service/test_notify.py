"""Test service notifications."""

from homeassistant.components import notify
from homeassistant.core import HomeAssistant
from homeassistant.setup import async_setup_component

from tests.common import async_mock_service


async def test_message_calls_service(hass: HomeAssistant):
    """Tests that a notificatio message actually calls a service."""
    await async_setup_component(
        hass,
        notify.DOMAIN,
        {
            "notify": {
                "name": "test_service",
                "platform": "notify_template_service",
                "service": "test.service",
            }
        },
    )

    calls = async_mock_service(hass, "test", "service")

    hass.services.call(notify.DOMAIN, "test_service", {"entity_id": "foo.bar"})

    assert len(calls) == 3
