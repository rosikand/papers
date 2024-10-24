import sys

def format_string(sentence):
    # Split by spaces and dashes
    words = [word for part in sentence.split(' ') for word in part.split('-')]
    # Convert to lowercase and remove empty strings
    words = [word.lower() for word in words if word]
    # Join with dashes
    return '-'.join(words)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a sentence as a command line argument")
        print("Usage: python script.py \"Your Sentence Here\"")
        sys.exit(1)

    input_sentence = " ".join(sys.argv[1:])
    result = format_string(input_sentence)
    print(result)
