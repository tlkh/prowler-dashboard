import eel

eel.init('web')
print("Initialised Eel")

@eel.expose
def get_device_counts():
    global devices_ssh
    global devices_vnc
    global devices_weak
    global devices_other
    devices_total = devices_ssh + devices_vnc + devices_other
    return devices_ssh, devices_vnc, devices_weak, devices_total

devices_ssh = 7
devices_vnc = 3
devices_weak = 1
devices_other = 0

devices_total = devices_ssh + devices_vnc + devices_other

eel.get_devices_status(devices_ssh, devices_vnc, devices_weak, devices_total)

print("Serving page...")
eel.start('index.html')
