from geometry import area_circle, area_rectangle

def main():
    print("Area Calculator")

    r = float(input("Enter radius of circle: "))
    print("Area of circle:", area_circle(r))

    l = float(input("Enter length of rectangle: "))
    w = float(input("Enter width of rectangle: "))
    print("Area of rectangle:", area_rectangle(l, w))

if __name__ == "__main__":
    main()
