def create_row(spaces,stars):
    return " "*spaces + "*"*stars + "\n"
def diamond(n):
    if(n <= 0 or n%2==0):
        return None
    else:
        for i in range(1,n+1,2):
            print(create_row(int((n-i)/2),i))
        for i in range(n-2,0,-2):
            print(create_row(int((n-i)/2),i))
diamond(7)