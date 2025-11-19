"""Control classes for Vektiva Smarwi."""

import aiohttp
import logging

_LOGGER = logging.getLogger(__name__)


class SmarwiControl:
    """Control class for multiple Smarwi devices."""

    def __init__(self, hosts: str):
        """Initialize with comma-separated list of hosts."""
        self.hosts = [x.strip() for x in hosts.split(",")]
        self.title = ", ".join([x.split(".")[0] for x in self.hosts])

    async def authenticate(self) -> bool:
        """Test if we can authenticate with all hosts."""
        try:
            for host in self.hosts:
                ctl = SmarwiControlItem(host)
                await ctl.get_status()
            return True
        except Exception as err:
            _LOGGER.error("Authentication failed: %s", err)
            return False

    def list(self) -> list:
        """Return list of SmarwiControlItem objects."""
        return [SmarwiControlItem(host) for host in self.hosts]


class SmarwiControlItem:
    """Control class for a single Smarwi device."""

    def __init__(self, host: str):
        self.host = host
        self.name = host.split(".")[0]
        self.id = host  # unikátní identifikátor
        self.fw = None

    async def __request(self, path: str) -> str:
        """Send request to device and return response text."""
        url = f"http://{self.host}/{path}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    raise ValueError(f"Request failed with {resp.status}/{resp.reason}")
                return await resp.text()

    async def open(self):
        """Open window fully."""
        await self.__request("cmd/open/100")

    async def set_position(self, pos: int):
        """Set window position (0–100)."""
        if pos > 1:
            await self.__request(f"cmd/open/{pos}")
        else:
            await self.close()

    async def close(self):
        """Close window."""
        await self.__request("cmd/close")

    async def stop(self):
        """Stop window movement."""
        await self.__request("cmd/stop")

    async def get_status(self) -> dict:
        """Get current device status."""
        response = await self.__request("statusn")
        result = {}
        for item in response.split("\n"):
            if ":" in item:
                key, value = item.split(":", maxsplit=1)
                result[key.strip()] = value.strip()
        return result
