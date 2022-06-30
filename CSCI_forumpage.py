import datetime
import pandas as pd
import random
import numpy as np

class Forum_Page:

    def __init__(self, name):
        self.__name = name
        self.__board = pd.DataFrame(columns = ['Title','Date', 'Author', 'Post', 'Votes'])
        self.__board.set_index('Title', inplace = True)
        self.__board['Votes'] = self.__board['Votes'].astype('int')
        self.__anon_words = self.__process('words.txt')
        
    
    def __process(self, filename):
        with open(filename,'r', encoding = 'UTF8') as file:
           result = [line.rstrip() for line in file]
        return result
        
    def __exists(self, title):
        return title in self.__board.index
    
    def checker(self):
        return self.__board.copy()

    def __generate_anon(self):
        words = random.sample(self.__anon_words, k=2)
        numbers = random.choices(range(0,10), k=2)
        username = words[0] + '_' + words[1] + '_' + str(numbers[0]) + str(numbers[1])
        ok = False
        while not ok:
            if username in self.__board['Author']:
                words = random.sample(self.__anon_words, k=2)
                numbers = random.choices(range(0,10), k=2)
                username = words[0] + '_' + words[1] + '_' + str(numbers[0]) + str(numbers[1])
            else:
                ok = True
        return username
        
    def add_post(self, title, post, author = None):
        if self.__exists(title) is False:
            date = str(datetime.date.today())
            if author is None:
                author = self.__generate_anon()
            self.__board.loc[title] = [date, author, post, 0]
    
    def delete_post(self, title):
        if self.__exists(title) is True:
            self.__board.loc[title, 'Author'] = np.nan
            self.__board.loc[title, 'Post'] = np.nan

    def vote_post(self, title, up = True):
        status = self.__board.loc[title, 'Author']
        if self.__exists(title) is True and pd.isnull(status) is False:
            votes = self.__board.loc[title,'Votes']
            if up is True:
                votes += 1
            else:
                votes -= 1
            self.__board.loc[title, 'Votes'] = votes

    def top_voted(self):
        if len(self.__board) == 0:
            return None
        else:
            votes = self.__board['Votes']
            max_votes = votes.max()
            top = self.__board.groupby('Votes').get_group(max_votes)
            return top
        
    def get_titles(self):
        if len(self.__board) == 0:
            return None
        else:
            y = self.__board.index
            titles = list(y)
            return titles
        
    def get_post_info(self, title):
        if self.__exists(title) is True:
            x = self.__board.loc[title]
            info = list(x)
            return info
    
    def get_name(self):
        return self.__name
        
    def __str__(self):
        active_posts = self.__board.loc[self.__board['Post'].notnull()]
        active_num = len(active_posts)
        return str(active_num) + ' active posts on ' + str(self.get_name())