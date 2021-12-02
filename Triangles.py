def cosAlpha(a,b,c):
	return (b**2 + c**2 - a**2)/(2*b*c)


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

	alpha = cosAlpha(a,b,c)
	beta = cosAlpha(b,a,c)
	gamma = cosAlpha(c,a,b)

	if(alpha == 0 or beta == 0 or gamma == 0):
		print("Прямоугольный")
	elif(alpha > 0 and beta > 0 and gamma > 0):
		print("Остроугольный")
	else:
		print("Тупоугольный")
else:
	print("треугольник не существует")