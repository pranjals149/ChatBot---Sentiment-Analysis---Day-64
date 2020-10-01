import random
from textblob import TextBlob

print('Hello, What is your name ?')
name = input()
print('-' * 30)
print('Do you have nickname ?')
ans = input()
print('-' * 30)
if 'y' in ans.lower():
    nick = input('What is your Nickname ?')
    print('Hello,Nice to meet you ' + nick)
    print('-' * 30)
else:
    nick = name
    print('Okay then, I will call you ' + nick)
    print('-' * 30)
greetings = [
    'How are you' + nick + '?',
    'How are you feeling ' + nick,
    "What's up " + nick + '?',
    'Greetings, are you well ?',
    'How are things going ?'
]
print('-' * 30)
print(random.choice(greetings))
ans = input()

topics = [
    'Twitter',
    'Cricket',
    'Python',
    'Flutter',
    'Back-end Devlopment',
    'Games'
]

questions = [
    'What is your views on ',
    'What do you think about ',
    'How do you feel about ',
    'I would like your opinion on ',
    'What is your favourite '
]
for i in range(0, random.randint(3,5)):
    question = random.choice(questions)
    questions.remove(question)
    topic = random.choice(topics)
    topics.remove(topic)
    print(question + topic + '?') 

    ans = input()
    print('-' * 30)
    blob = TextBlob(ans)

    if blob.polarity > 0.5:
        print('OMG, you really love ' + topic)
    elif blob.polarity > 0.1:
        print('Well, you clearly like ' + topic)
    elif blob.polarity < -0.5:
        print('You totally hate ' + topic)
    elif blob.polarity < -0.1:
        print("So, you don't like " + topic)
    else:
        print('That is a very neutral view on ' + topic)

    if blob.subjectivity > 0.6:
        print('and you are so biased !!')
    elif blob.subjectivity > 0.3:
        print('and you are a bit biased !!')
    else:
        print('and quite objective !!')

goodbyes = [
    "Pleasure talking to you Mr." + nick + "I gotta go now",
    "Ok I am bored now, I will  watch  netflix",
    'Bye Bye, I gotta go now',
    'Yaaawn ...... I gotta go now',
    'Catch you later, ' + nick 
]

print(random.choice(goodbyes))
