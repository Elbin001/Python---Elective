""" Given two dictionaries say D1 and D2.
    Write a program to print all common keys in both D1 and D2"""

n1 = int(input("\nEnter no.of keys in D1 :"))
D1 = {}
for i in range(n1):
    key = input("\nEnter key for D1 : ")
    value = input("Enter value for D1 : ")
    D1[key] = value
    
n2 = int(input("\nEnter no.of keys in D2 :"))
D2 = {}
for i in range(n2):
    key = input("\nEnter key for D2 : ")
    value = input("Enter value for D2 : ")
    D2[key] = value

print("\nDictionary D1 : ",D1)
print("Dictionary D2 : ",D2)

common_Keys = []
for key in D1.keys():
    if key in D2.keys():
        common_Keys.append(key)

print("\nCommon Keys : ",common_Keys)
        
