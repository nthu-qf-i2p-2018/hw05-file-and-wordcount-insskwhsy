import string

def main(filename):
    fileobj = open(filename)
    lines = fileobj.readlines()
    
    all_words = []

    for line in lines:
        words = line.split()
        
        for word in words:
            word = word.strip(string.punctuation)
            
            if word != " " :
                all_words.append(word)
    from collections import Counter
    counter = Counter(all_words)

    import csv
    with open('wordcount.csv','w',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        for i in all_words:
            writer.writerow([i,all_words.count(i)])
        csv_file.close()
    
    import json
    with open('wordcount.json','w') as json_file:
        json.dump(counter,json_file)
        json_file.close()
    
    import pickle
    x = open('wordcount.pkl','wb')
    pickle.dump(counter,x)
    x.close()

if __name__ == '__main__':
    main("i_have_a_dream.txt")
