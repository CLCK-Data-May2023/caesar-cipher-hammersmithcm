message = input("Please enter a sentence:")
message = message.lower()

sub_dict = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
}

new_message = ''
for char in message:
    if char in sub_dict:
        char = sub_dict[char]
        new_message += char
    else:
        new_message += char
    
print("The encripted sentence is:" + new_message)
