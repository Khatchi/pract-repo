try:
    print(1)
    raise Exception("An error occurred")
except Exception as e:
    print(e)
finally:
    print(3)