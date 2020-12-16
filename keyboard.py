from pynput import keyboard

print('Press WASD to drive robot:')

with keyboard.Events() as events:
    # Block for as much as possible
    event = events.get(1e6)
    if event.key == keyboard.KeyCode.from_char('w'):
        print("Drive Forward Command")
    if event.key == keyboard.KeyCode.from_char('a'):
        print("Turn Left Command")
    if event.key == keyboard.KeyCode.from_char('s'):
        print("Drive Backward Command")
    if event.key == keyboard.KeyCode.from_char('d'):
        print("Turn Right Command")