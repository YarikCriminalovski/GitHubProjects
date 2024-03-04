import random as r
import string as s
import time as t

password_length = int
password = str


def randomize(length=int):
    passw = ''.join([r.choice(s.ascii_letters + s.digits +
                              s.punctuation) for _ in range(length)])
    return passw


def main(loop=True, passik=str, pass_length=int):
    while loop:
        t.sleep(1)
        print("[CONSOLE]: Please input password length: (or 'quit' to quit)")
        try:
            pass_length = int(input())
        except ValueError:
            t.sleep(1)
            print("[----] PROGRAM FINISHED [----]")
            loop = False
            break
        passik = randomize(pass_length)
        t.sleep(1)
        print(f"[CONSOLE]: This is your password '{passik}'")


print("[----] PASSWORD GENERATOR [----]")
t.sleep(1)
print("[----] AUTHOR: YAROSLAV ZHYMAN [----]")
t.sleep(1)
main(passik=password, pass_length=password_length)
