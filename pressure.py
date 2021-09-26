# program regulujący ciśnienie

from time import sleep
from random import randint


def control_pressure():
    while True:
        pressure = measure_pressure()
        if pressure > 700:
            run_critical_safeties()
        elif 500 < pressure <= 700:
            run_standard_safeties()
        elif pressure <= 500:
            break
    print("The system is fine!")


def measure_pressure():
    pressure = randint(490, 800)
    print(f"psi={pressure}", end="; ")      ## end="; " zastępuje znak nowej linii
    return pressure


def run_standard_safeties():
    print("Running standard safeties...")
    sleep(0.5)


def run_critical_safeties():
    print("Running critical safeties...")
    sleep(1.2)


if __name__ == "__main__":
    control_pressure()
