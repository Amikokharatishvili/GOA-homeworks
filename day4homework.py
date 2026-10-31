#                    გოა საშინაო დავალება ამიკო ხარატიშვილი.

#1)
code = input("შეიყვანეთ საიდუმლო კოდი (მინიმუმ 6 სიმბოლო): ")

#2)
start = code[:2]

#3)
end = code[-2:]

#4)
hidden_length = len(code) - 4

#5)
hashes = "#" * hidden_length

#6)
secret_result = start + hashes + end

#7)
print(secret_result)
