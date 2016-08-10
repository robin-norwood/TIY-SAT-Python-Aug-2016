# coding: utf-8
name = "Nibor"
age = 32
print("My friend " + name + " is " + str(age) + " years old.")
message = "My friend {0} is {1} years old."
message.format(name, age)
greeting = "Hello, {name}. How are you {day}?"
greeting.format(name="Robin", day="Today")
greeting.format(name="Robin", day="today")
import math
math.pi
print("Today, pi is approximately {value}.".format(value=math.pi))
print("Today, pi is approximately {value:.2f}.".format(value=math.pi))
print("{num} in hex is {num:x}".format(num=230)
)
get_ipython().magic('pinfo open')
f = open('/usr/share/dict/words', 'r')
type("fasdsd")
type(f)
words = f.read()
f.close()
type(words)
len(words)
print(words[0:100])
for word in words[0:100]:
    print("A word: {0}".format(word))
    
words.split('\n')[0:10]
f = open('/usr/share/dict/words', 'r')
words = f.readlines()
f.close()
len(words)
type(words)
words[0:10]
words[5]
f = open('/usr/share/dict/words', 'r')
type(f)
for line in f:
    print(line)
    
f.close()
with open("/usr/share/dict/words", 'r') as f:
    for line in f:
        print(line)
        
