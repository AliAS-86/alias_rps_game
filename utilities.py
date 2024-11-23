import functools
import os, json

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

def data_validator(user_input, key, target_json):
    """placeholder"""
    data_set = get_json_data_set(key, target_json)
    print(f"data set: {data_set}")
    if isinstance(data_set, list):
        if user_input in data_set:
            return True
        return False
    # if isinstance(validation_data, int):
    #     if user_input is int:
    #         return True
    #     return False

def get_json_data_set(key, target_json):
    # construct file path for the target JSON file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, target_json)

    # Load the JSON file
    with open(json_file_path, "r") as json_file:
        data_set_collection = json.load(json_file)

        if key in data_set_collection["validation_data"]:
            return data_set_collection["validation_data"][key]
        else:
            raise KeyError(f"Key {key} not found in {target_json}")