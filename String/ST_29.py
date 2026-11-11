'''
Replace a word with another word in a sentence.
'''
from colorama import Fore, init
init() 
sent = "I like to eat apples everyday"
n_sent = sent.replace("apples", "bananas")

print(Fore.GREEN+ n_sent)