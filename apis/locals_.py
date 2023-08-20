# -*- coding: cp1252 -*-
"""
Contains functions that are not online APIs.
"""

import random
import urllib2
import requests
from bs4 import BeautifulSoup
import json
import re #added for movie


def getJokes():

    url = "https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke"

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['setup']
    answer = resp_dict['punchline']
    return results + '\n' + 'Answer:' + answer



def getMovie(title):
    
    re.sub(' ','',title) #helloworld (remove all spaces)
    re.sub('  ',' ',title) #hello world (remove double spaces)
    title = title.replace(' ', '+')
    url = "http://www.omdbapi.com/?t=" + title + "&apikey=7bdc1e74"
    out = requests.get(url).text
    resp_dict = json.loads(out)
    results = resp_dict['Plot']
    return 'Plot:\n' + results

def getHyde():

	quo = ['Quiet minds cannot be perplexed or frightened but go on in fortune or misfortune at their own private pace, like a clock during a thunderstorm.',

	'If he be Mr. Hyde\" he had thought, \"I shall be Mr. Seek.',
	'If I am the chief of sinners, I am the chief of sufferers also.',
	'It is one thing to mortify curiosity, another to conquer it. ',
	'You must suffer me to go my own dark way.',
	'With every day, and from both sides of my intelligence, the moral and the intellectual, I thus drew steadily nearer to the truth, by whose partial discovery I have been doomed to such a dreadful shipwreck: that man is not truly one, but truly two.',
	'I learned to recognise the thorough and primitive duality of man; I saw that, of the two natures that contended in the field of my consciousness, even if I could rightly be said to be either, it was only because I was radically both.',
	'I sat in the sun on a bench; the animal within me licking the chops of memory; the spiritual side a little drowsed, promising subsequent penitence, but not yet moved to begin.',
	'There comes an end to all things; the most capacious measure is filled at last; and this brief condescension to evil finally destroyed the balance of my soul.',
	'All human beings, as we meet them, are commingled out of good and evil: and Edward Hyde, alone, in the ranks of mankind, was pure evil.',
	'You start a question, and it\'s like starting a stone. You sit quietly on the top of a hill; and away the stone goes, starting others...',
	'She had an evil face, smoothed by hypocrisy; but her manners were excellent.',
	'Jekyll had more than a father\'s interest; Hyde had more than a son\'s indifference.',
	'Here then, as I lay down the pen and proceed to seal up my confession, I bring the life of that unhappy Henry Jekyll to an end.',
	'I incline to Cain\'s heresy,"he used to say quaintly:" I let my brother go to the devil in his own way.',
	'The less I understood of this farrago, the less I was in a position to judge of its importance.',
	'I have been made to learn that the doom and burden of our life is bound forever on man’s shoulders; and when the attempt is made to cast it off, it but returns upon us with more unfamiliar and more awful pressure.',
	'The secret to a happiness is a small ego. And a big wallet. Good wine helps, too. But that\'s not really a secret, is it?',
	'O my poor old Harry Jekyll, if ever I read Satan\'s signature upon a face, it is on that of your new friend.',
	'I sometimes think if we knew all, we should be more glad to get away.',
	'It was for one minute that I saw him, but the hair stood upon my head like quills. Sir, if that was my master, why had he a mask upon his face?',
	'His affections, like ivy, were the growth of time, they implied no aptness in the object.']


	return random.choice(quo)

def getOneliner():

    answers = ['Are you a magician? Because whenever I look at you, everyone else disappears!',
                'Are you a camera? Because every time I look at you, I smile.',
                'Do you have a Band-Aid? Because I just scraped my knee falling for you.',
                'I\'m not a photographer, but I can picture me and you together.',
                'Do you work at Starbucks? Because I like you a latte.',
                'If you were a vegetable you\'d be a cute-cumber.',
                'Are you religious? Because you\'re the answer to all my prayers.',
                'If I were a cat I\'d spend all 9 lives with you.',
                'Do you play soccer? Because you\'re a keeper!',
                'Are you African? Because you\'re a frican babe.',
                'Are you an interior decorator? Because when I saw you, the entire room became beautiful.',
                'Let me tie your shoes, cause I don\'t want you falling for anyone else.',
                'Are you an omelette? Because you\'re making me egg-cited!',
                'Are you a pirate? Cause I’ve got a lot of semen waiting for you!',
                'Touch your toes and I will show u where the rocket goes!',
                'How do you like your eggs: poached, scrambled, or fertilized?',
                'I’m a mindreader and Yes I will sleep with you',
                'A-B-C-D-E-F-G R-U-D-T-F with me?',
                'Did you grow up on a farm? Cause you sure know how to raise a good cock.',
                'I could’ve called heaven and asked for an angel, but I was hoping you’re a slut instead.',
                'When you eat water melon, do you spit or swallow the seeds?',
                'I’m not a dick in real life, but I’ll play one in you tonight',
                'Wow, you’re stunning, I think I just found the cure for impotence']
    return random.choice(answers)
def getScope(month):

    url = "http://horoscope-api.herokuapp.com/horoscope/today/" + month

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['horoscope']
    return results
def getNumber(number):

    url = "http://numbersapi.com/102" + number + "?json"

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['text']
    return results
def getTrump():

    url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['message']
    return results
def getMom():

    url = "http://api.yomomma.info/"

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['joke']
    return results   
def getbitcoin():

    url = "https://api.cryptowat.ch/markets/kraken/btcusd/price"

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['result']['price']
    return results
def getlitecoins():

    url = "https://api.cryptowat.ch/markets/kraken/ltcusd/price"

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['result']['price']
    return results
def geteth():

    url = "https://api.cryptowat.ch/markets/kraken/ethusd/price"

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['result']['price']
    return results
def getsia():

    url = "https://api.cryptowat.ch/markets/poloniex/scbtc/price"

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['result']['price']
    return results
def getxmr():

    url = "https://api.cryptowat.ch/markets/kraken/xmrusd/price"

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['result']['price']
    return results
def getpot():

    url = "https://api.cryptowat.ch/markets/kraken/potusd/price"

    out = requests.get(url).text

    resp_dict = json.loads(out)
    results = resp_dict['allowance']['cost']
    return results

def getGeek():

    url = "https://geek-jokes.sameerkumar.website/api"

    out = requests.get(url).text

    return out

def advice():
    """
    Random sentences of advice.
    :return:
    """
    #url = "http://api.adviceslip.com/advice"

    #out = requests.get(url).text

    #resp_dict = json.loads(out)
    #results = resp_dict['slip']['advice']
    #return results


    answers = ['What you\'re supposed to do when you don\'t like a thing is change it. If you can\'t change it, change the way you think about it. Don\'t complain.',

    'Try to be a rainbow in someone\'s cloud.',
    'Never miss a good chance to shut up.',
    'If a man will begin with certainties, he shall end in doubts; but if he will be content to begin with doubts, he shall end in certainties.',
    'Here\'s some advice. Stay alive.',
    'We cannot change the cards we are dealt, just how we play the hand.',
    'Accept what life offers you and try to drink from every cup. All wines should be tasted; some should only be sipped, but with others, drink the whole bottle.',
    'Never ruin an apology with an excuse.',
    'I don\'t care if you\'re black, white, straight, bisexual, gay, lesbian, short, tall, fat, skinny, rich or poor. If you\'re nice to me, I\'ll be nice to you. Simple as that.',
    'A mathematical formula for happiness:Reality divided by Expectations.There were two ways to be happy:improve your reality or lower your expectations.',
    'Don\'t ever take a fence down until you know why it was put up.',
    'Don\'t leave a piece of jewelry at his house so you can go back and get it later, he may be with his real girlfriend.',
    'Be impeccable with your word.',
    'Dont take anything personally.',
    'Dont make assumptions.',
    'Always do your best. ',
    'I always pass on good advice. It is the only thing to do with it. It is never of any use to oneself.',
    'Write with the door closed, rewrite with the door open.',
    'Do not complain beneath the stars about the lack of bright spots in your life.',
    'A wise man gets more use from his enemies than a fool from his friends.',
    'Adapt what is useful, reject what is useless, and add what is specifically your own.',
    'You have to be burning with an idea, or a problem, or a wrong that you want to right. If you\'re not passionate enough from the start, you\'ll never stick it out.',
    '“Always speak politely to an enraged dragon.',
    'Don\'t own so much clutter that you will be relieved to see your house catch fire.',
    'How do I know what I think until I see what I say?',
    'Don\'t believe anything you read on the net. Except this. Well, including this, I suppose.',
    'I am glad that I paid so little attention to good advice; had I abided by it I might have been saved from some of my most valuable mistakes.']


    return random.choice(answers)
def eight_ball():
    
	
    answers = [
    unicode('[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]', 'utf-8'),
                'It is certain',
                'It is decidedly so',
                'Without a doubt',
                'Yes definitely',
                'You may rely on it',
                'As I see it, yes',
                'Most likely',
                'Outlooks good',
                'Yes',
                'Signs point to yes',
                'Signs point to no',
                'Don\'t count on it', 
                'My reply is no',
                'My sources say no',
                'Outlook not so good',
                'Very doubtful',
                'Why do you need to ask?',
                'Negative', 'Indeed',
                'Sorry Boo', 
                'Doubt JSD cares.',
                'Don\'t go Full retarded',
                'Is Ed \"Too Tall\" Jones too tall?',
                'Does Charlie Daniels play a mean fiddle?',
                'Does Elmer Fudd have trouble with the letter R?',
                'Did The Waltons take way too long to say good night?',
                'Does a ten-pound bag of flour make a really big biscuit?',
                'Did the caveman invent fire?',
                'Was Abe Lincoln honest?',
                'Is having a snowball fight with pitching great Randy Johnson a bad idea?',
                'Is a bird in the hand worth two in the bush?',
                'Can fútbol announcer Andrés Cantor make any sport exciting?',
                'Does a former drill sergeant make a terrible therapist?',
                'Do woodchucks chuck wood?',
                'Did the little piggy really cry \"wee wee wee\"" all the way home?',
                'Does it take two to tango?',
                'What, do you live under a rock?',
                'Does the buck stop here?',
                'Do dogs chase cats?',
                'Would Foghorn Leghorn make a really bad book narrator?',
                'Is the pen mightier than the sword?',
                'Do people use smartphones to do dumb things?',
                'Would helium make opera sound less stuffy?',
                'Do mimes make even less sense when you can\'t see them?']


    return random.choice(answers)
def get_mood():

    moods = ['Happier than Gallagher at a Farmer\'s market.',
    'Happier than a Bodybuilder Directing Traffic.',
    'Happier than Christopher Columbus with Speedboats',
    'Happier than Eddie Money running a travel agency.',
    'Happier than a Witch at a Broom Factory',
    'Happier than a Slinky on an Escalator.',
    'Happier than an Antelope with Nightvision Goggles.',
    'Happier than Dikembe Mutombo Blocking a Shot.',
    'Happier than Paul Revere with a Cell phone.',
    'Happier than Dracula Volunteering at a Blood Drive.',
    'Happier than the Pillsbury Doughboy on his way to a Baking Convention.',
    'Happier than a Camel on Wednesday/Hump Day.']

    return random.choice(moods)
def fortune():

    
    answers = [ 
    unicode('Pass Go, Collect [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅] !', 'utf-8'),
                'When in anger, sing the alphabet.','About time i got out of that cookie.', 'Avoid taking unnecessary gambles. Luck numbers 2,12,10,15,6,5.', 'Ask your mom.',
                'I cannot help you, I am just a cookie.', 'Ignore previous fortune cookies.', 'Ignore future fortune cookies.', 'The fortune you seek is in another cookie.',
                'Some fortune cookies contain no fortune.', 'Always think something can go wrong, then you will always be right.', 'Found the mistake in the code..', 'Ask again later',
		        'If Hakuna Matata dont work, then no worries', 'Maybe whoever has this will feel better? ~Matt~', 'Tell x0r hes pretty, might save his life some day.']
    return random.choice(answers)
def get_joke():

    jokes = ['I threw a boomerang many years ago. I now live in constant fear.',
             'You\'re like the first piece of bread in the loaf... everyone touches you but no one wants you',
             'There is a husband and a wife. The husband dies, and during the funeral, the wife starts to laugh. Everybody starts to ask her why, and she says, \'This is the first time that I know where my husband is going.\'',
             'How do you make a rednecks dick hurt. Kick his sister\'s jaw.',
             'Some guy called me a tool. So I got hammered and nailed his girlfriend, guess he was right.',
             'Where do you send a Jew with ADHD? A Concentration camp.',
             'I saw two guys wearing matching clothing and I asked if they were gay. They quickly arrested me.',
             'A lion will never cheat on his wife, But a Tiger Wood!',
             'Did you hear about the kidnapping at school? It\'s ok, he woke up.',
             'Can a kangaroo jump higher than a house? Of course a house doesn\'t jump at all',
             'My dog used to chase people on a bike alot. It got so bad, i had to take his bike away.',
             'My neighbors are listening to great music. Whether they like it or not.',
             'Sometimes i drink water - just to surprise my liver.',
             'Hearing voices in your head is normal. Listening to them is quite common. Arguing with them – acceptable. It is only when you lose that argument that you get in real trouble.',
             'There was a blonde, a redhead, and a brunette. They were all trapped on an island and the nearest shore was 50 miles away. The redhead swam trying to make it to the other shore she swam 15 miles, drowned, and died. The brunette swam 24 miles, drowned, and died. The blonde swam 25 miles, got tired, and swam back.',
             
             'A science teacher tells his class, \"Oxygen is a must for breathing and life. It was discovered in 1773.\" A blonde student responds, \"Thank God I was born after 1773! Otherwise I would have died without it.\"',
             'A police officer stops a blonde for speeding and asks if he could see her license. She replied in a huff, \"I wish you guys could get your act together. Just yesterday you take away my license and then today you expect me to show it to you.\"',
             'This jokes not funny...'
        ]

    return random.choice(jokes)
def get_Animal():
    
    facts = ['the peacock mantis shrimp can throw a punch at 50 mph, accelerating quicker than a 22 caliber bullet.',
             'studies have shown that wild chimps in guinea drink fermented palm sap, which contains about 3 percent alcohol by volume.',
             'the chevrotain is an animal that looks like a tiny deer with fangs. ',
             'capuchin monkeys pee on their hands to wash their feet.',
             'only the males are called peacocks. females are called peahens.',
             'dragonflies and damselflies form a heart with their tails when they mate.',
             'baby elephants suck their trunks for comfort.',
             'tigers have striped skin as well. each pattern is as unique as a fingerprint.',
             'there was once a type of crocodile that could gallop.',
             'sea otters hold hands while they\'re sleeping so they don\'t drift apart.',
             'prairie dogs say hello by kissing.',
             'animal behaviorists have concluded that cats dont meow as a way to communicate with each other. its a method they use for getting attention from humans.',
             'despite their appearance, elephant shrews are more closely related to elephants than shrews.',
             'flamingos are naturally white—their diet of brine shrimp and algae turns them pink.',
             'alberta, canada is the largest rat-free populated area in the world.',
             'red-eyed tree frog eggs can hatch early if they sense danger.',
             'whitetail deer can sprint at speeds up to 30 miles per hour.',
             'blue jays mimic hawks calls to scare away other birds',
             'in the uk, the british monarch legally owns all unmarked mute swans in open water.',
             'all clownfish are born male—some turn female to enable mating.',
             'moray eels have a second set of jaws that extends from their throats.',
             'male ring-tailed lemurs will \"stink fight\" by wafting scent at each other.']
    return random.choice(facts).lower()
def flip_coin():
    
	
    coin = ['Heads', 'Tails']
    return random.choice(coin) 
def roll_dice():
    
	
    numbers = ['1', '2', '3', '4', '5', '6']
    return random.choice(numbers)


       
