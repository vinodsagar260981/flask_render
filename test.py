l=[1,2,3]
l_iter = iter(l)
print(next(l_iter))
print(next(l_iter))
print(next(l_iter))
print(next(l_iter, "end"))

print(__name__)

if __name__ == "__main__":
    print("Working")