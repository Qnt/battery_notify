import psutil
from pynotifier import Notification
# from collections import namedtuple

battery = psutil.sensors_battery();
Notification(
	title='Battery percentage',
	description=str(battery.percent),
	# icon_path='/absolute/path/to/image/icon.png',
	duration=5,
	urgency='normal'
).send()
