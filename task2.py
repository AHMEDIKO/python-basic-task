import time

m = int(input("enter test minutes: "))
s = int(input("enter test seconds: "))

total = (m * 60) + s

if m < 0 or s < 0 or s > 59 or total == 0:
    print("invalid duration.")
else:
    if total > 300:
        print("Safety limit exceeded test duration capped to 05:00.")
        total = 300
    while total > 0:
        m_left = total // 60
        s_left = total % 60
        t_str = f"{m_left:02d}:{s_left:02d}"
        if total > 30:
            msg = f"POWER ON | Remaining: {t_str}"
        elif total > 10:
            msg = f"STABILIZING SYSTEM | Remaining: {t_str}"
        else:
            msg = f"COOLDOWN PHASE | Do not touch | {t_str}"
        print(f"\r{msg}", end="", flush=True)
        time.sleep(1)
        total -= 1
    print("\nPower test completed successfully.")