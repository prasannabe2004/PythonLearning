import string

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def getGuid(self):
        return self.guid
    def getTitle(self):
        return self.title
    def getSubject(self):
        return self.subject
    def getSummary(self):
        return self.summary
    def getLink(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def isWordIn(self, text):
        word = self.word.lower()
        text = text.lower()
        for i in string.punctuation:
            if i in text:
                text = text.replace(i, ' ')
        text = text.split()

        if word in text:
            return True
        else:
            return False


class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())


class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())


class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())


class NotTrigger(Trigger):
    def __init__(self, t1):
        self.t1 = t1

    def evaluate(self, story):
        return not self.t1.evaluate(story)

class AndTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)

class OrTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)

class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        self.phrase = phrase

    def evaluate(self, story):
        if self.phrase in story.getTitle():
            return True
        if self.phrase in story.getSubject():
            return True
        if self.phrase in story.getSummary():
            return True
        return False


koala = NewsStory('', "Koala bear's are soft and cuddly", '', '', '')
s1 = TitleTrigger('bear')
print s1.evaluate(koala)
pillow = NewsStory('', '', 'I prefer pillows that are soft.', '', '')
s2 = SubjectTrigger('soft')
print s2.evaluate(pillow)
soda = NewsStory('', '', '', 'Soft drinks are great', '')
s3 = SummaryTrigger('soft')
print s3.evaluate(soda)

# Not Trigger
koala = NewsStory('', "Koala bear's are soft and cuddly", '', '', '')
s4 = TitleTrigger('bear')
n = NotTrigger(s4)
print n.evaluate(koala)

#And Trigger
koala = NewsStory('', "Koala bear's are soft and cuddly", '', '', '')
s5 = TitleTrigger('bear')
pillow = NewsStory('', '', 'I prefer pillows that are soft.', '', '')
s6 = SubjectTrigger('soft')

result = AndTrigger(s5,s6)

soda = NewsStory('', "Koala bear's are soft and cuddly", 'I prefer pillows that are soft.', '', '')
print result.evaluate(soda)

#Or Trigger
koala = NewsStory('', "Koala bear's are soft and cuddly", '', '', '')
s5 = TitleTrigger('bear')
pillow = NewsStory('', '', 'I prefer pillows that are soft.', '', '')
s6 = SubjectTrigger('soft')

result = OrTrigger(s5,s6)

soda = NewsStory('', "Koala bear's are soft and cuddly", 'I prefer pillows that are soft.', '', '')
print result.evaluate(soda)

#Phase Trigger
pt = PhraseTrigger("New York City")
a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
noa = NewsStory('', "something something new york city", '', '', '')
nob = NewsStory('', '', "something something new york city", '', '')
noc = NewsStory('', '', '', "something something new york city", '')

pt.evaluate(a)
pt.evaluate(b)
pt.evaluate(c)

