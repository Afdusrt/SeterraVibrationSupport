import evdev
from evdev import ecodes, InputDevice, ff
import time

def find_ff_device():
    # Find the first EV_FF capable event device
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if ecodes.EV_FF in device.capabilities():
            return device
    return None

def vibrate_controller(duration_ms=1000):
    device = find_ff_device()
    if device is None:
        print("Sorry, no FF capable device found")
        return

    print(f"Found {device.name} at {device.path}")
    print("Preparing FF effect...")

    # Define the rumble effect
    rumble = ff.Rumble(strong_magnitude=0xffff, weak_magnitude=0xffff)
    effect_type = ff.EffectType(ff_rumble_effect=rumble)

    effect = ff.Effect(
        ecodes.FF_RUMBLE,
        -1,
        0,
        ff.Trigger(0, 0),
        ff.Replay(duration_ms, 0),
        effect_type
    )

    # Upload the effect
    effect_id = device.upload_effect(effect)

    # Play the effect
    device.write(ecodes.EV_FF, effect_id, 1)

    # Wait for the effect to finish
    time.sleep(duration_ms / 1000.0)

    # Stop the effect
    device.erase_effect(effect_id)
    print("Effect stopped")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        duration_ms = int(sys.argv[1])
    else:
        duration_ms = 1000

    vibrate_controller(duration_ms=duration_ms)
