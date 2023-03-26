word_dictionary = {
    "brotherhood" : "a sense of unity that goes beyond individual differences, where members work together to achieve common goals and aspirations.",

    "cross" : "a symbol of sacrifice and suffering, representing the idea that one must endure pain and hardship to achieve a greater good.",

    "star" : " a symbol of achievement, often used to represent success or excellence in a particular field or activity."
}


def main():
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])
    
main()