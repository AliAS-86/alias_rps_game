import functools
import sys, signal

def keyboardInterruptHandler(func):
    """
    This decorator wrapper handle the keyboardInerrupt for the whole script runtime
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\nexecution interrupted by user. Exiting the game...")
            return None
    return wrapper

# def handle_keyboard_interrupt(signum, frame):
#     print("\nExecution interrupted by user. Exiting the game gracefully.")
#     sys.exit(1)

def input_with_interruption(prompt=""):
    """placeholder"""
    user_input = spaces_trimmer(input(prompt).lower())
    try:
        if user_input in ["q", "quit", "exit", "bye"]:
            print("Exiting the game, thanks for playing AliAS_RPS")
            raise SystemExit
        return user_input
    except KeyboardInterrupt:
        print("Exiting the game, thanks for playing AliAS_RPS")
        raise
    finally:
        print("....")

def spaces_trimmer(string=""):
    """placeholder"""
    return string.strip()

def input_validator(user_input, validation_data):
    """placeholder"""
    # valid_inputs = ["1", "2", "q", "quit", "exit", "bye"]
    if isinstance(validation_data, list):
        if user_input in validation_data:
            return True
        return False
    # if isinstance(validation_data, int):
    #     if user_input is int:
    #         return True
    #     return False