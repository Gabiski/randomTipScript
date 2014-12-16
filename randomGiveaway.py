import praw
import random
import time


r = praw.Reddit('Giveaway script: random tips written by /u/DogeSensei')
r.login('USERNAME', 'PASSWORD') #Edit these fields, don't worry only you can see them
already_done = []
ignore = ['Bot','bot','much-wow-doge','Ninja-Clone','FrontPageDoge'] #add your username to this list the you don't try to tip yourself
total = 0
count = 0

maxPeople = 10  #this is the max number of people you will tip
low = 4 #this is the minimum tip you give
high = 35 #this is the maximum tip you give

while count < maxPeople: 
    submission = r.get_submission('SUBMISSIN_LINK') #copy and paste the URL to your giveaway here
    all_comments = submission.comments
    flat_comments = praw.helpers.flatten_tree(submission.comments)    

    for comment in flat_comments:
        if not comment.author:
            continue
        author = comment.author
        user = author.name
        cmt = comment.body
        
        if author not in already_done and user not in ignore:
            tip = random.randint(low,high)
            comment.reply('+/u/dogetipbot ' +str(tip)+ ' doge')
            already_done.append(author)
            count = count + 1
            total = total + tip
            print('You have tipped ' +str(count)+ ' people a total of ' +str(total)+ ' doge!')

    time.sleep(15)
    
if count >= maxPeople:
    print('Maximum participants met. Script ended')    
    
                   


