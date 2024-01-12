def say_hello(uname:str) -> str:
	return f'Hello {uname.lower()}'

if __name__ == '__main__':
	print(say_hello(input()))
