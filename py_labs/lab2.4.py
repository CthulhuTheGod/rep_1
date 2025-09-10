from collections import OrderedDict


text_to_analyze = str(input('Input text to analyze: '))
count_symbols = 0
count_words = 0
count_sentences = 0
stat_dict = dict()
for symbol in text_to_analyze:
    count_symbols += 1
    if symbol == ' ':
        count_words += 1
    if symbol == '.' or symbol == '!' or symbol == '?':
        count_sentences += 1
text_to_analyze = list(text_to_analyze.split())
my_dict = {}
for word in text_to_analyze:
    if my_dict.__contains__(word.lower()):
        my_dict[word.lower()] += 1
    else:
        my_dict[word.lower()] = 1

my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:5])

print('In your sentence: ')
print('symbols: ', count_symbols)
print('words: ', count_words)
print('sentences: ', count_sentences)
print(f'\nTop 5 words: \n{my_dict}')




