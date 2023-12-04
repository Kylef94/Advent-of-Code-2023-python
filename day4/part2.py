
def get_input():
    data = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            l = l.split(':')
            data.append(l[1].strip())
    return data

def get_ans(data):
    copies = [1] * len(data)
    
    for c, card in enumerate(data):
        card = card.split("|")
        lnums = set([x for x in card[0].split(" ") if x != ''])
        rnums = set([x for x in card[1].split(" ") if x != ''])
        wins = lnums & rnums
        
        if wins:
            for i in range(c + 1, c + len(wins) + 1):
                copies[i] += 1 * copies[c]
                
    return sum(copies)
    

if __name__ == "__main__":
    data = get_input()
    print(get_ans(data))