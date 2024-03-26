# Program to count the frequency of words in a string:

str = input("Enter a string : ")
words = str.lower().split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for key in frequency.keys():
    print("\nFrequency of ",key," = ",frequency[key])
    
