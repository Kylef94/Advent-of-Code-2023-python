
def get_input():
    data = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            data.append(l.strip())
    return data
    
def get_digits(line):
    num = ""
    chars = list(line)
    
    for c in chars:
        if c.isdigit():
            num += c
            break
    
    for c in chars[::-1]:
        if c.isdigit():
            num += c
            break
            
    return int(num)

if __name__ == "__main__":
    data = get_input()
    nums = sum([get_digits(line) for line in data])
    print(nums)