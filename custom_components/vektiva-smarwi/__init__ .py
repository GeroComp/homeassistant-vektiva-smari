"""The Vektiva Smarwi integration."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

PLATFORMS: list[str] = ["cover"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Vektiva Smarwi from a config entry."""
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}

    # Pokud by se inicializovalo API nebo koordinátor, uloží se sem
    # hass.data[DOMAIN][entry.entry_id] = SmarwiApi(...)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        # Použijeme bezpečné odstranění, aby nevznikl KeyError
        hass.data.get(DOMAIN, {}).pop(entry.entry_id, None)
    return unload_ok
