normal_words=set()
with open('OnlineDictionary.txt') as fnormal:
    for normal in fnormal:
        normal_words.add(normal.strip())

def find_words(instring):
    solutions ={}
    if instring in normal_words:
        return [instring]
    if instring in solutions:
        return solutions[instring]
    best_solution = None
    for i in range(1, len(instring) - 1):
        part1 = find_words(instring[:i])
        part2 = find_words(instring[i:])
        if part1 is None or part2 is None:
            continue
        solution = part1 + part2
        if best_solution is None or len(solution) < len(best_solution):
            best_solution = solution
    solutions[instring] = best_solution
    return best_solution

def check_unsplited_word(txt):
    splited_sentence=[]
    for w in txt.split():
        if w not in normal_words:
            result = find_words(w)
            if result is not None:
                splited = ' '.join(result)
                splited_sentence.append(splited)
            else:
                splited_sentence.append(w)
        else:
            splited_sentence.append(w)
    return ' '.join(splited_sentence)    
