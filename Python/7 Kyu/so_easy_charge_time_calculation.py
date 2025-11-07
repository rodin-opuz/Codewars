def calculate_time(battery,charger):
    fast = (battery * 0.85) / charger
    decrease = (battery * 0.1) / (charger * 0.5)
    trickle = (battery * 0.05) / (charger * 0.2)
    return round(fast + decrease + trickle, 2)
