a = int(input())
b = int(input())
c = int(input())

if(a < b + c and b < a + c and c < b + a):
	if(a == b == c):
		print("равносторонний")
	elif (a == b or a == c or b == c):
		print("равнобедренный")
	else:
		print("разносторонний")
else:
	print("треугольник не существует")