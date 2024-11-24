# import functools
# import os, json
from json_handler import JsonHandler

JSON_HANDLER = JsonHandler()

exit_keywords = ["q", "quit", "exit", "bye"]
def validated_input(prompt, validation_key):
    """a utility function that help with exiting the game triggered by specific inputs from the user """
    while True:
        user_input = input(prompt).lower().strip()
        validation_data = get_json_data(validation_key)
        if user_input in exit_keywords:
            print("Exiting the game, thanks for playing AliAS_RPS")
            raise SystemExit
        if user_input in validation_data:
            return True, user_input
        return False, None

# def data_validator(user_input, key, target_json):
#     """placeholder"""
#     data_set = get_json_data_set(key, target_json)
#     # print(f"data set: {data_set}")
#     if isinstance(data_set, list):
#         if user_input in data_set:
#             return True
#         return False
#     # if isinstance(validation_data, int):
#     #     if user_input is int:
#     #         return True
#     #     return False

def get_json_data(key):
    """Placeholder"""
    # construct file path for the target JSON file
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # json_file_path = os.path.join(current_dir, "data/" + target_json)
    # Load the JSON file
    validation_data = JSON_HANDLER.get_validation_data(key)
    return validation_data