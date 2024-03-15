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
    # Constructing the boot-up message with the percentage completion
    message = f"{BOOT_MESSAGE} {percent}% complete"
    # Writing the message to the console, overwriting the previous one
    sys.stdout.write("\r" + message)
    sys.stdout.flush()

def boot_up():
    """Simulate system boot-up process."""
    # Printing the welcome message
    print(WELCOME_MESSAGE)
    # Sleeping for a short period to give a pause effect
    time.sleep(TIME_TO_SLEEP)

    # Looping through the boot-up process
    for x in range(1, ITERATIONS + 1):
        # Calculating the percentage completion
        percent_complete = (x / ITERATIONS) * 100
        # Displaying the progress
        display_progress(int(percent_complete))
        # Adding a short delay for visual effect
        time.sleep(ELLIPSIS_DELAY)

    # Printing the completion message after the boot-up process finishes
    print(COMPLETION_MESSAGE)

def main():
    """Main function."""
    # Calling the boot_up function to start the system boot-up process
    boot_up()
    # Printing the loading message after the boot-up process completes
    print(LOADING_MESSAGE)

if __name__ == "__main__":
    # Calling the main function when the script is executed
    main()