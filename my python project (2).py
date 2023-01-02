import random

questionset = {
    "What is the capital of China ?": "Beijing",
    "What is the capital of USA ?": "Washington DC",
    "What is the capital of Japan ?": "Tokyo",
    "What is the capital of UK ?": "London",
    "What is the capital of Bhutan ?": "Thimpu",
    "What is the capital of North Korea ?": "Pyongyang",
    "What is the capital of Sri Lanka ?": "Colombo",
    "What is the capital of Nepal ?": "Kathmandu",
    "What is the capital of South Korea ?": "Seoul",
    "What is the capital of Bangladesh ?": "Dhaka",
}

ans = 0
country, capital = random.choice(list(questionset.items()))
print("Q1", country)
n = input("Enter your answer: ")
if n.lower() == capital.lower():
    print("Correct")
    ans += 1
else:
    print("Incorrect")

print()

country, capital = random.choice(list(questionset.items()))
print("Q2", country)
n = input("Enter your answer: ")
if n.lower() == capital.lower():
    print("Correct")
    ans += 1
else:
    print("Incorrect")

print()

country, capital = random.choice(list(questionset.items()))
print("Q3", country)
n = input("Enter your answer: ")
if n.lower() == capital.lower():
    print("Correct")
    ans += 1
else:
    print("Incorrect")

print()

country, capital = random.choice(list(questionset.items()))
print("Q4", country)
n = input("Enter your answer: ")
if n.lower() == capital.lower():
    print("Correct")
    ans += 1
else:
    print("Incorrect")

print()

country, capital = random.choice(list(questionset.items()))
print("Q5", country)
n = input("Enter your answer: ")
if n.lower() == capital.lower():
    print("Correct")
    ans += 1
else:
    print("Incorrect")

print()

print("Your score is: ", ans)