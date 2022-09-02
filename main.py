import random

def read_txt_into_list(file_name):
    with open(file_name) as f:
        return f.read().splitlines()

def main():
    # Read the colours and nouns into lists
    colours = read_txt_into_list('colours.txt')
    nouns = read_txt_into_list('nouns.txt')

    # Randomly pick one noun and uppercase it
    noun = random.choice(nouns).upper()

    # Randomly pick one colour and uppercase it
    colour = random.choice(colours).upper()

    # Print the colour and noun
    print(colour + ' ' + noun)

if __name__ == '__main__':
    main()