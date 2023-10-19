try:
    raise ValueError("Custom Error")
except ValueError as e:
    print(str(e))