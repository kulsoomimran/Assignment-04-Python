SENTENCE_START: str = "Once upon a time, there was a " 

def main():
    
    adjective: str = input("Please enter an adjective: ")
    
    noun: str = input("Please enter a noun: ")
    
    verb: str = input("Please enter a verb: ")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

if __name__ == '__main__':
    main()