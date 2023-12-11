from collections import Counter

def get_input():
    data = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            data.append(l.strip().split(' '))
    return data

handtypes = ['HIGH', 'ONEP', 'TWOP', 'THREE', 'FULLH', 'FOUR', 'FIVE',]
      

cardranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
class Hand:
    
    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.type = self.gethand()
        
        
    def gethand(self):
        cardcount = Counter(self.cards).most_common()
        most_common_count = cardcount[0][1]
        
        if most_common_count < 5:
            second_most_common_count = cardcount[1][1]

        match most_common_count:
            case 5:
                return "FIVE"
            
            case 4:
                return "FOUR"
            
            case 3:
                if second_most_common_count == 2:
                    return 'FULLH'
                else:
                    return 'THREE'
            
            case 2:
                if second_most_common_count == 2:
                    return 'TWOP'
                else:
                    return 'ONEP'

            case 1:
                return 'HIGH'

    def __eq__(self, other) -> bool:
        if self.type != other.type:
            return False
        
        else:
            selfhand = list(self.cards)
            otherhand = list(other.cards)
            
            for h in zip(selfhand, otherhand):
                if h[0] != h[1]:
                    return False
            return True
        
    def __lt__(self, other) -> bool:
        if self.type != other.type:
            return handtypes.index(self.type) < handtypes.index(other.type)
        
        else:
            selfhand = list(self.cards)
            otherhand = list(other.cards)
            
            for h in zip(selfhand, otherhand):
                if h[0] != h[1]:
                    return cardranks.index(h[0]) < cardranks.index(h[1])
            return False
        
    def __str__(self) -> str:
        return f"HAND: cards = {self.cards}, type = {self.type}, bid = {self.bid}"
    
if __name__ == "__main__":
    data = get_input()
    hands = []
    for d in data:
        hand = Hand(d[0], d[1])

        hands.append(hand)
    hands.sort()

    total = 0
    for i in range(len(hands)):
        total += (i + 1) * hands[i].bid
    
    print(total)