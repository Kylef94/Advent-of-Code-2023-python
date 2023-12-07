from collections import namedtuple

Map = namedtuple(typename="Map", field_names=["dest", "source", "length", "destmax", "sourcemax"])

def get_input():
    with open("input.txt", "r") as f:
        text = f.read()
        data = text.split("\n\n")
    
    res = []
    res.append([int(x) for x in data[0].strip('seeds: \n').split(' ')])
    for d in data[1:]:
        intervals = []
        tmp = d.split('\n')[1:]
        
        for t in tmp:
            dest, source, length = t.split(' ')
            dest, source, length = int(dest), int(source), int(length)
            destmax = dest + length
            sourcemax = source + length
            intervals.append(Map(dest, source, length, destmax, sourcemax))
        res.append(intervals)
    return res

def convert(seed, mapx):
    for m in mapx:
        if seed >= m.source and seed <= m.sourcemax:
            return m.dest - m.source + seed
        
    return seed

def get_ans(data):
    res = []
    seeds = data[0]
    maps = data[1:]
    
    for s in seeds:
        for m in maps:
            s = convert(s, m)
        res.append(s)
    
    return min(res)

if __name__ == "__main__":
    data = get_input()
    # for d in data:
    #     print(d)
    print(get_ans(data))
        

    
    