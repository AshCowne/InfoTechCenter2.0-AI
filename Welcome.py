import time
import sys

# Constants
WELCOME_MESSAGE = "\n\nWelcome to InfoTech Center V1.0\n"
BOOT_MESSAGE = "Infotech Center System Booting"
COMPLETION_MESSAGE = "\n\nOperating System Booted Up - Retina Scanned - Access Granted!"
LOADING_MESSAGE = "InfoTech Center Operating System Loading..."
ITERATIONS = 20
TIME_TO_SLEEP = 1
ELLIPSIS_DELAY = 0.5

def display_progress(percent):
    """Display boot-up progress."""
    message = f"{BOOT_MESSAGE} {percent}% complete"
    sys.stdout.write("\r" + message)
    sys.stdout.flush()

def boot_up():
    """Simulate system boot-up process."""
    print(WELCOME_MESSAGE)
    time.sleep(TIME_TO_SLEEP)

    for x in range(1, ITERATIONS + 1):
        percent_complete = (x / ITERATIONS) * 100
        display_progress(int(percent_complete))
        time.sleep(ELLIPSIS_DELAY)

    print(COMPLETION_MESSAGE)

def main():
    """Main function."""
    boot_up()
    print(LOADING_MESSAGE)

if __name__ == "__main__":
    main()
