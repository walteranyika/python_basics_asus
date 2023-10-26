name = "Ahmed"
city = "Cairo"
age = 22
weight = 70.8

print(name + city)
print(name * 4)

print(f"I am {name}, I am {age} years old and I live in {city} and I weigh {weight} Kgs")

sentence = " these are python functions to do with strings  "

upper_case = sentence.upper()

print(upper_case, sentence)
print(sentence.upper())
print(upper_case.lower())
print(len(sentence))
print(sentence.capitalize())
print(name.swapcase())
print(sentence)
print(sentence.strip())

result = sentence.replace("functions", "methods").strip().upper()  # chaining
print(result)

