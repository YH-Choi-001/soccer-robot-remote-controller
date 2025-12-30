"""
Control a soccer robot from your mobile phone via Bluetooth.
"""

import toga
from toga.style.pack import COLUMN, ROW
from .btconn import BTConn


class SoccerRobotRemoteController(toga.App):
    def __init__(self, btconn: BTConn):
        self.btconn = btconn
        super().__init__()

    def startup(self):
        self.main_box = toga.Box(direction=COLUMN)

        name_label = toga.Label(
            "Your name: ",
            margin=(0, 5),
        )
        self.name_input = toga.TextInput(flex=1)

        name_box = toga.Box(direction=ROW, margin=5)
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Scan Devices",
            on_press=self.scan_devices_callback,
            margin=5
        )

        self.devices_box = toga.Box(direction=COLUMN, margin=5)

        self.main_box.add(name_box)
        self.main_box.add(button)
        self.main_box.add(self.devices_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    async def scan_devices_callback(self, widget) -> None:
        indicator = toga.ActivityIndicator()
        self.devices_box.clear()
        self.main_box.replace(self.devices_box, indicator)
        indicator.start()
        devices = await self.btconn.scan_devices()
        for (_, (device, _)) in devices.items():
            label_str: str = device.address
            if device.name is not None:
                label_str += f" ({device.name})"
            label = toga.Label(label_str, flex=1)
            self.devices_box.add(label)
        indicator.stop()
        self.main_box.replace(indicator, self.devices_box)


def main(btconn: BTConn):
    return SoccerRobotRemoteController(btconn)
