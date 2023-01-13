# Chap 4

limits = 20
tweets = "pass" * 6
diff = limits - len(tweets)
# if diff := limits - len(tweets) >= 0:
if diff >= 0:
    print(tweets)
else:
    print(f'글자 수 {abs(diff)} 초과')

a = []
print(bool(a))
a.append(5)
print(bool(a))
print(bool(set()))
print(bool(dict()))
print(bool())

vowels = 'aeiou'
letter = 'u'
if letter not in vowels:
    print("실행 안됨!")
