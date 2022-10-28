from roman import ToRoman, FromRoman

def example_ToRoman():
    examples = [1, 3, 4, 5, 15, 64]
    for i in examples:
        print(f"{i}\t:\t{ToRoman(i)}")

def example_FromRoman():
    examples = ["III", "IV", "VI", "LC", "IIII", "VV"] # 3, 4, 6, nonvalid nonvalid
    for i in examples:
        print(f"{i}\t:\t{FromRoman(i)}")

choice = input("Choose examples of :\n1: from base 10 to roman numerals\n2: from roman numerals to base 10\n\n: ")
examples = {"1" : example_FromRoman, "2" : example_ToRoman}
if choice in examples:
    examples[choice]()
