import asyncio
from bleak import BleakScanner

class BTConn:
    def __init__(self):
        pass

    async def scan_devices(self):
        return await BleakScanner.discover(timeout=5.0, return_adv=True)
