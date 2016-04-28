positive_words = set()
with open('positive-words.txt') as fpositive:
    for positive in fpositive:
        positive_words.add(positive.strip())
negative_words = set()
with open('negative-words.txt') as fnegative:
    for negative in fnegative:
        negative_words.add(negative.strip())


def PNrate(text):
    pos= [po for po in str(text).split() if po in positive_words]
    neg = [ne for ne in str(text).split() if ne in negative_words]
    return (len(pos),len(neg))
