
import re
# from engine.config import ASSISTANT_NAME
#extracting the video name from the query
def extract_yt_term(command):
    command = command.lower()
    words_to_remove = ["play", "on", "youtube"]
    return remove_words(command, words_to_remove)
#removing unwanted words from the query
def remove_words(input_string, words_to_remove) :
    words = input_string.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    result_string = " ".join(filtered_words)
    return result_string
# print(extract_yt_term("play C++ tutorials on youtube"))