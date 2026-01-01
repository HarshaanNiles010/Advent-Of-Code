def main():
    with open('input.txt') as f:
        triangles = [i.strip().split() for i in f.readlines()]
    def validate_triangle(a: int, b: int, c: int) -> bool:
        return (a + b > c) and (a + c > b) and (b + c > a)
    count = 0
    for triangle in triangles:
        if validate_triangle(int(triangle[0]), int(triangle[1]), int(triangle[2])):count += 1
        else: continue
    print(count)

if __name__ == '__main__':
    main()
