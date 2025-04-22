# Problem 1: Count Even Numbers in a List
nums = [2, 3, 5, 8, 10, 13, 16]
# Count how many are even
count = 0
for num in nums:
    if(num%2==0):
        count += 1
# print(count)
        
   
#  Problem 2: Reverse a String       
s = "hello"
s_rev = s[::-1]
# print(s_rev)


#  Problem 3: Frequency of Each Word in a Sentence
sentence = "this is a test this is only a test"
# Count how many times each word appears

word_list = sentence.split()
frequencies = {}

for word in word_list:
    if word in frequencies:
        frequencies[word] += 1
    else:
        frequencies[word] = 1
        
# print(frequencies)
        
# Problem 4: Check if Two Strings are Anagrams

s1 = "triangle"
s2 = "integral"

# if (sorted(s1) == sorted(s2)):
#     # print(f"{s1} and {s2} are anagrams.")
# else:
#     # print("They are not anagrams.")

   
# Problem 5: Find the Maximum in a List

nums = [4, 9, 2, 10, 3]

max_val = 0

for num in nums:
    if num > max_val:
        max_val = num
# print(max_val)

# Frequency Count logic

num = str(1122345112)
numbers = {}

for digit in num:
    if (digit not in numbers):
        numbers[digit] = 1
    else:
        numbers[digit] += 1

# print(numbers)


