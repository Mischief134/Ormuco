from compare import Compare
import sys
def main():
    print("Input first version:")
    ver1 = sys.stdin.readline().strip()
    print("Input second version:")
    ver2 = sys.stdin.readline().strip()
    obj = Compare(ver1,ver2)
    res =obj.compare()
    print(res)

    

    


if __name__ == '__main__':
    main()