from Vowel_check import vowel_checker

sent = "Machine learning (ML) is a field of inquiry devoted to understanding and building methods that learn – that is, methods that leverage data to improve performance on some set of tasks."
count = 0
sent = sent.split(' ')
print(sent)
for i in sent:
	count += vowel_checker(i)

print(count)