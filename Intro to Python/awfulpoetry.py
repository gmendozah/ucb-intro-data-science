import sys
import random

articles_list = ['the', 'a', 'my', 'his', 'het']
subjects_list = ['cat', 'dog', 'father', 'mother', 'sister', 'brother']
verb_list = ['sang', 'ran', 'jumped']
adverb_list = ['loudly', 'quietly', 'well', 'badly']


lines = 5

try:
    lines = int(sys.argv[1])
    if lines in range(1, 11):
        for i in range(lines):
            sentence_type = random.randint(0, 1)
            article = random.choice(articles_list)
            subject = random.choice(subjects_list)
            verb = random.choice(verb_list)
            if sentence_type == 0:
                adverb = random.choice(adverb_list)
                print("{article} {subject} {verb} {adverb}".format(article = article, subject = subject, verb = verb, adverb = adverb))
            else:
                print("{article} {subject} {verb}".format(article = article, subject = subject, verb = verb))
    else:
        print("Value should be between 1 and 10 inclusive")
except:
    print("Must be a valid integer between 1 and 10 inclusive")