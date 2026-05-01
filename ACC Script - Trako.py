# 🖱️ FreePIE — Mouse & Keyboard Wheel Simulator

A FreePIE script that turns your **mouse and keyboard into a virtual steering wheel** for racing simulators like Assetto Corsa Competizione (ACC), Assetto Corsa, and others.

No wheel needed. Just plug in FreePIE + vJoy and go.

---

## 🎮 Controls

| Input | Action |
|---|---|
| Mouse X | Steering |
| `W` | Throttle |
| `S` | Brake |
| `SPACE` | Handbrake |
| `Q` | Shift up |
| `E` | Shift down |
| `Z` | Look left |
| `X` | Look right |
| `R` | Reset car |

---

## 🎚️ Analog Intensity System

One of the key features of this script is the **3-level intensity system** for throttle and brake. Instead of on/off digital inputs, you get analog-like control by holding a modifier key:

| Modifier | Intensity | Use case |
|---|---|---|
| `CTRL` (left) | 25% | Gentle input — slow corners, trail braking |
| *(none)* | 65% | Normal driving |
| `SHIFT` | 100% | Full throttle / emergency braking |

> If `SHIFT` and `CTRL` are pressed simultaneously, `SHIFT` wins (100%).

The handbrake always fires at 100% regardless of the modifier.

---

## ⚙️ Configuration

All tunable values are at the top of the script, clearly marked with comments.

### Mouse sensitivity
```python
mouse_sensitivity = 2        # Higher = faster steering (recommended: 1–10)
sensitivity_center_reduction = 1.0  # 1.0 = linear | lower = softer near center
```

### Intensity levels
```python
intensity_low  = 0.25   # CTRL modifier
intensity_mid  = 0.65   # No modifier
intensity_high = 1.00   # SHIFT modifier
```

### Ramp times (milliseconds)
Controls how fast each axis builds up and releases:
```python
throttle_increase_time = 100
throttle_decrease_time = 150

braking_increase_time  = 120
braking_decrease_time  = 120

hbrake_increase_time   = 100
hbrake_decrease_time   = 100
```

---

## 🛠️ Requirements

- [FreePIE](https://andersmalmgren.github.io/FreePIE/) — scripting engine
- [vJoy](https://sourceforge.net/projects/vjoystick/) — virtual joystick driver

### vJoy setup
In the vJoy configurator, make sure the following axes are enabled:
- `X` — Steering
- `Y` — Throttle
- `Z` — Brake
- `RY` — Handbrake
- At least **5 buttons**

---

## 🚀 How to use

1. Install vJoy and FreePIE
2. Open FreePIE and load the script
3. Press **F5** to run
4. In your game, bind the vJoy device axes and buttons as usual
5. Set your steering wheel range in-game (recommended: 180°–360°)

---

## 📝 Notes

- The script runs at **5ms intervals** using a high-resolution system timer for smooth analog output
- Axis mapping uses a 14-bit signed range for maximum precision
- The mouse cursor is locked off-screen during use so it doesn't interfere with the game
- Tested on **Assetto Corsa Competizione** — should work on any game that supports vJoy

---

## 📄 License

MIT — do whatever you want with it.
