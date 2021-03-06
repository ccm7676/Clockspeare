import sys, pygame, random
from datetime import datetime

quotes = ['Have more than you show, Speak less than you know.',
'What a terrible era in which idiots govern the blind.',
'When I got enough confidence, the stage was gone. When I was sure of losing, I won. When I needed people the most, they left me. When I learnt to dry my tears, I found a shoulder to cry on. And when I mastered the art of hating, somebody started loving me.',
'The Eyes are the window to your soul',
'There is nothing so confining as the prisons of our own perceptions.',
'Never play with the feelings of others, because you may win the game but the risk is that you will surely lose the person for life time',
'Laughing faces do not mean that there is absence of sorrow! But it means that they have the ability to deal with it',
'If we are true to ourselves, we can not be false to anyone.',
'Love all, trust a few, do wrong to none.',
'Hell is empty and all the devils are here.',
'Go wisely and slowly. Those who rush stumble and fall.',
'Nothing comes from doing nothing.',
'No legacy is so rich as honesty.',
'Give thanks for what you are today and go on fighting for what you gone be tomorrow',
'We suffer a lot the few things we lack and we enjoy too little the many things we have.',
'Things sweet to taste prove in digestion sour.',
'I wasted time, and now doth time waste me.',
'I would challenge you to a battle of wits, but I see you are unarmed!',
'The best is yet to come.',
"Don't trust the person who has broken faith once.",
'What my tongue dares not that my heart shall say',
'This above all; to thine own self be true.',
'You know who you are, but know not who you could be.',
'Smooth runs the water where the brook is deep.',
'Some are born great, some achieve greatness, and some have greatness thrust upon them.',
'Listen to many, speak to a few.',
'A fool thinks himself to be wise, but a wise man knows himself to be a fool.',
'To climb steep hills requires a slow pace at first.',
"Tis the times' plague, when madmen lead the blind.",
'A light heart lives long.',
'Every why has a wherefore.',
'Words spoken can not be recalled so think twice before you speak.',
'Our doubts are traitors and make us lose the good we oft might win by fearing to attempt.',
'Strong reasons make strong actions.',
"This thing of darkness I acknowlege mine. There is nothing more confining than the prison we don't know we are in.",
'It is not in the stars to hold our destiny but in ourselves.',
'To be, or not to be, that is the question',
"She's beautiful, and therefore to be wooed; She is a woman, therefore to be won.",
'Lord, what fools these mortals be!',
'A smile cures the wounding of a frown.',
'There is plenty of time to sleep in the grave',
'O Lord that lends me life, Lend me a heart replete with thankfulness!',
'Wisdom cries out in the streets, and no man regards it.',
"Instead of weeping when a tragedy occurs in a songbird's life, it sings away its grief. I believe we could well follow the pattern of our feathered friends.",
'Love sought is good, but given unsought, is better.',
'Some rise by sin, and some by virtue fall.',
'Affection is a coal that must be cooled; else, suffered, it will set the heart on fire.',
"Sit by my side, and let the world slip: we shall ne'er be younger.",
'Love does not see with the eyes, but with the soul.',
"To me, fair friend, you never can be old, For as you were when first your eye I ey'd, Such seems your beauty still.",
'The empty vessel makes the loudest sound.',
'Defer no time, delays have dangerous ends.',
"Let's go hand in hand, not one before another.",
'We know what we are, but know not what we may be.',
'Conversation should be pleasant without scurrility, witty without affectation, free without indecency, learned without conceitedness, novel without falsehood.',
"True hope is swift, and flies with swallow's wings.",
'Tears water our growth.',
'There is nothing either good or bad but thinking makes it so.',
"A good heart 'is worth gold.",
"I'll note you in my book of memory.",
'Pleasure and action make the hours seem short.',
"Don't waste your love on somebody, who doesn't value it.",
'Women speak two languages - one of which is verbal.',
'Be great in act, as you have been in thought.',
'I do desire we may be better strangers.',
'Speak what we feel, not what we ought to say.',
'People???s good deeds we write in water. The evil deeds are etched in brass.',
"Life's but a walking shadow, a poor player, that struts and frets his hour upon the stage, and then is heard no more; it is a tale told by an idiot, full of sound and fury, signifying nothing.",
'My crown is in my heart, not on my head; not decked with diamonds and Indian stones, nor to be seen: my crown is called content, a crown it is that seldom kings enjoy.',
'One may smile, and smile, and be a villain.',
'Frame your mind to mirth and merriment which bars a thousand harms and lengthens life.',
'To unpathed waters, undreamed shores.',
'The object of Art is to give life a shape.',
'All things are ready, if our mind be so.',
'God shall be my hope, my stay, my guide and lantern to my feet.',
'Your gentleness shall force More than your force move us to gentleness.',
"All the world's a stage, and all the men and women merely players: they have their exits and their entrances; and one man in his time plays many parts, his acts being seven ages.",
'Love asks me no questions, and gives me endless support.',
'Let every man be master of his time.',
"There's many a man hath more hair than wit.",
'One touch of nature makes the whole world kin.',
'Desperate times breed desperate measures',
'If you prick us do we not bleed? If you tickle us do we not laugh? If you poison us do we not die? And if you wrong us shall we not revenge?',
'False face must hide what the false heart doth know.',
'When sorrows come, they come not single spies, but in battalions.',
'Kindness in women, not their beauteous looks, Shall win my love.',
'We are such stuff as dreams are made on; and our little life is rounded with a sleep.',
'God has given you one face, and you make yourself another.',
'Ignorance is the curse of God; knowledge is the wing wherewith we fly to heaven.',
'Love is the greatest of dreams, yet the worst of nightmares.',
'Her passions are made of nothing but the finest part of pure love',
'Make use of time, let not advantage slip.',
'Words are easy, like the wind; Faithful friends are hard to find.',
'Lawless are they that make their wills their law.',
'Give thy thoughts no tongue.',
'You will never age for me, nor fade, nor die.',
]


pygame.init()


screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
black = (0,0,0)
white = (255,255,255)

pygame.mouse.set_visible(False)

font1 = pygame.font.Font('Roboto-Regular.ttf', 48)
font2 = pygame.font.Font('Roboto-Regular.ttf', 24)
lastdate = 0
new_quote = "wweee"


bg = pygame.image.load("bg.png")
bgrect = bg.get_rect()

def quotus_maximus(str, startx,starty,maxx):
    quoteWord = str.split(" ")
    newx = startx
    newy = starty
    space = 10
    marginy = 3

    for i in range(len(quoteWord)):
        quoteTxt = font2.render(quoteWord[i], True, black, white)
        quoteTxtRect = quoteTxt.get_rect()
        
        if(newx + space + quoteTxtRect.width >= maxx):
            newy += quoteTxtRect.height + marginy
            quoteTxtRect.topleft = (startx,newy)
            newx = startx + quoteTxtRect.width + space
        
        else:
            quoteTxtRect.topleft = (newx,newy)
            newx += quoteTxtRect.width + space
        
        screen.blit(quoteTxt,quoteTxtRect)
        print(screen)

def blitz():
    now = datetime.now()

    text = font1.render(now.strftime("%H:%M"), True, black)
    textRect = text.get_rect()
    textRect.center = (80,100)
    screen.blit(text,textRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.blit(bg,bgrect)
    now = datetime.now()

    text = font1.render(now.strftime("%H:%M"), True, black)
    textRect = text.get_rect()
    textRect.center = (80,100)

    if(lastdate != now.strftime("%d")):
        lastdate = now.strftime("%d")
        new_quote = random.choice(quotes)
        
    blitz()
    quotus_maximus(new_quote,20,180,470)
    pygame.display.flip()
