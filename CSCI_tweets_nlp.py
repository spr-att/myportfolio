import string

with open('stopwords.txt','r',encoding = 'UTF-8') as stops:
    eng_words = [line.rstrip() for line in stops]
#printe(eng_words)

def distill_tweet(tweet):
    tweet = tweet.translate(tweet.maketrans("’-'","   ",'.!?"')).lower().split()
    result = []
    for word in tweet:
        if word not in eng_words and not word.startswith('http') and not word.isnumeric():
            result.append(word)
    return result

def tweet_lists(filename):
    result = []
    cur_name = ''
    with open(filename, 'r', encoding = 'UTF8') as file:
        for line in file:
            line = line.split('\t')
            user = line[1]
            tweet = line[2]
            if user == cur_name:
                cur = open(user + '.txt', 'a')
            else:
                if cur_name != '':
                    cur.close()
                cur_name = user
                result += [user]
                cur = open(user + '.txt', 'w')
            cur.writelines(tweet + '\n')
            cur.close()
    return result

def tweets_from_file(filename): 
    with open(filename,'r', encoding = 'UTF8') as raw_tweets:
        tweets = []
        for line in raw_tweets:
            line_tweets = line.rstrip().split('\n')
            tweets.extend(line_tweets)
    return tweets

def top_entries(tweets, num_cutoff = 1, hashes = False, mentions = False):
    filtered_tweets = []
    entries = {}
    for tweet in tweets:
        filtered_tweets.extend(distill_tweet(tweet))
    if hashes == True:
        k = [token for token in filtered_tweets if token.startswith('#')]
        for token in k:
            if token not in entries:
                entries[token] = 1
            else:
                old = entries[token]
                new = old + 1
                entries[token] = new
    elif hashes == False and mentions == True:
        k = [token for token in filtered_tweets if token.startswith('@')]
        for token in k:
            if token not in entries:
                entries[token] = 1
            else:
                old = entries[token]
                new = old + 1
                entries[token] = new
    elif hashes == False and mentions == False:
        k = [token for token in filtered_tweets if not token.startswith('#') and not token.startswith('@')]
        for token in k:
            if token not in entries:
                entries[token] = 1
            else:
                old = entries[token]
                new = old + 1
                entries[token] = new
    top_entries = {key:val for key, val in entries.items() if val >= num_cutoff}
    return top_entries
