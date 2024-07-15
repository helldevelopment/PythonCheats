# offsets are outdated, still trying to figure them out.

import pymem

def hack(displayname: str, walkspeed: float = 40.0):
    proc: pymem.Pymem
    humpattern: bytes = bytes.fromhex("D0032689F77F0000")

    try:
        proc = pymem.Pymem("RobloxPlayerBeta.exe")
    except pymem.exception.ProcessNotFound:
        print("failed to hack roblox :(")
        exit(1)

    hum = proc.patternscan_all(hum_pattern + display_name.encode(errors="ignore"))

    if hum:
         ws_a = hum + 0x1b0
         ws_b = hum + 0x388

         proc.write_float(ws_a, walkspeed)
         proc.write_float(ws_b, walkspeed)
    else:
         print("no humanoid exists")

         proc.close_process() # close process handle

if __name == "__main":
    user_input = input("your display name? ")
    speed_input = input("how fast are you? ")
    print("so fucking basically it gives error idk")


    target_speed = float(speed_input)

    if (len(user_input) > 0 and target_speed):
        print("hacking roblox...")
        hack(user_input, target_speed)

        print("done hacked")
    else:
        print("something wrong with your input")
