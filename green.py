import nltk
from nltk.corpus import cmudict
from nltk.tag.stanford import StanfordNERTagger

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('cmudict')

PATH_TO_JAR='./static/stanford-ner-2020-11-17/stanford-ner.jar'
PATH_TO_MODEL = './static/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz'

tagger = StanfordNERTagger(model_filename=PATH_TO_MODEL, path_to_jar=PATH_TO_JAR, encoding='utf-8')


uncountable = ['advice', 'aggression', 'assistance', 'attention', 'accommodation', 'advertising', 'air', 'athletics', 'access', 'adulthood', 'alcohol', 'applause', 'agriculture', 'atmosphere', 'anger', 'art', 'absence', 'aid', 'arithmetic', 'age', 'beauty', 'beef', 'bravery', 'business', 'blood', 'botany', 'bacon', 'baggage', 'ballet', 'butter', 'biology', 'beer', 'bread', 'behaviour', 'cake', 'cash', 'chaos', 'clothing', 'confidence', 'compassion', 'calm', 'corruption', 'courage', 'comprehension', 'cheese', 'currency', 'carbon', 'cardboard', 'chalk', 'chess', 'coal', 'commerce', 'confusion', 'cookery', 'countryside', 'crockery', 'cutlery', 'chocolate', 'content', 'cotton', 'childhood', 'coffee', 'danger', 'data', 'dancing', 'democracy', 'damage', 'darkness', 'determination', 'delight', 'depression', 'driving', 'dignity', 'dessert', 'design', 'dust', 'distribution', 'dirt', 'duty', 'education', 'economics', 'equipment', 'earth', 'expense', 'energy', 'electricity', 'enthusiasm', 'environment', 'enjoyment', 'envy', 'evil', 'engineering', 'entertainment', 'evolution', 'existence', 'ethics', 'evidence', 'employment', 'experience', 'failure', 'fire', 'fiction', 'fashion', 'forgiveness', 'faith', 'flour', 'flu', 'fear', 'fun', 'fame', 'freedom', 'food', 'finance', 'fruit', 'fuel', 'friendship', 'furniture', 'flesh', 'gasoline', 'genetics', 'garbage', 'growth', 'grief', 'grammar', 'garlic', 'gossip', 'gold', 'gymnastics', 'glass', 'grass', 'golf', 'gratitude', 'ground', 'guilt', 'harm', 'hair', 'hardware', 'hydrogen', 'help', 'happiness', 'health', 'hate', 'hope', 'hospitality', 'homework', 'heat', 'hatred', 'hunger', 'honey', 'humour', 'honesty', 'height', 'housework', 'history', 'ice', 'imagination', 'information', 'independence', 'infrastructure', 'ice cream', 'importance', 'intelligence', 'industry', 'irony', 'injustice', 'innocence', 'iron', 'insurance', 'inflation', 'judo', 'jealousy', 'jam', 'jewelery', 'joy', 'juice', 'justice', 'kindness', 'knowledge', 'karate', 'laughter', 'labour', 'lava', 'livestock', 'luggage', 'lightning', 'land', 'leather', 'linguistics', 'light', 'loneliness', 'lack', 'litter', 'luck', 'love', 'leisure', 'logic', 'literature', 'machinery', 'mail', 'mankind', 'marriage', 'money', 'magic', 'marble', 'mercy', 'music', 'meat', 'management', 'mathematics', 'moonlight', 'methane', 'milk', 'metal', 'mayonnaise', 'mud', 'mist', 'motivation', 'motherhood', 'measles', 'nature', 'nitrogen', 'nutrition', 'noise', 'news', 'nonsense', 'news', 'nonsense', 'nurture', 'obedience', 'obesity', 'oxygen', 'oil', 'paper', 'passion', 'poetry', 'parking', 'pressure', 'perfume', 'physics', 'psychology', 'peel', 'pepper', 'patience', 'permission', 'peace', 'philosophy', 'plastic', 'progress', 'production', 'pollution', 'pleasure', 'pork', 'petrol', 'pronunciation', 'pride', 'policy', 'purity', 'poverty', 'punctuation', 'power', 'produce', 'protection', 'publicity', 'pasta', 'pay', 'pain', 'painting', 'quartz', 'quality', 'quantity', 'reliability', 'rum', 'recreation', 'reality', 'rubbish', 'revenge', 'racism', 'rice', 'relief', 'respect', 'rain', 'relaxtion', 'research', 'religion', 'salt', 'safety', 'salad', 'scaffolding', 'soil', 'satisfaction', 'sand', 'satire', 'security', 'sorrow', 'seafood', 'speed', 'scenery', 'sewing', 'strength', 'spece', 'software', 'seaside', 'stream', 'stupidity', 'shopping', 'stress', 'shame', 'spite', 'steam', 'silence', 'sunshine', 'sleep', 'status', 'success', 'soup', 'snow', 'smoking', 'silver', 'symmetry', 'spaghetti', 'spelling', 'soap', 'sport', 'stuff', 'sugar', 'smoke', 'tea', 'tolerance', 'thirst', 'technology', 'trousers', 'tennis', 'trade', 'timber', 'turbulence', 'toothpaste', 'time', 'traffic', 'travel', 'toast', 'thunder', 'transportation', 'trust', 'trouble', 'temperature', 'understanding', 'usage', 'underwear', 'unemployment', 'unity', 'violence', 'veal', 'validity', 'vitality', 'vinegar', 'vision', 'vegetation', 'vegetarianism', 'vengeance', 'warmth', 'weight', 'whiskey', 'weather', 'wildlife', 'water', 'welfare', 'wine', 'wisdom', 'wood', 'wealth', 'wheat', 'wool', 'width', 'work', 'yoga', 'youth', 'yeast', 'zoology', 'zinc']

# list of noun types
typeOfNoun = ['NN', 'NNS', 'NNP', 'NNPS']
# list of common nouns
common = ['NN', 'NNS']
# vowel letter
vowelLetter = ['a', 'i', 'u', 'e', 'o']
# pronunciation dictionary
pron = cmudict.dict()
# To check if it has already been out once
already = dict()
# Insert the results of the decision.
result = []

def vowel(word):
    if word[1] == 'NNS':
        if word[0] in already:
            return ("the",)
        else:
            already[word[0]] = True
            return (None)
    else:
        if word[0] in already:
            return ("the",)
        else:
            already[word[0]] = True
            return ("an", "the")

def consonant(word):
    if word[1] == 'NNS':
        if word[0] in already:
            return ("the",)
        else:
            already[word[0]] = True
            return (None)
    else:
        if word[0] in already:
            return ("the",)
        else:
            already[word[0]] = True
            return ("a", "the")

def pronunciation_detect(word):
    if pron[word][0][0][0].lower() in vowelLetter:
        return True
    else:
        return False

def article_identifier(engText):

    # If there are any blanks left in the sentence,
    # the POS classification will not be correct,
    # so fill in the blanks with a random article to
    # correctly identify the noun.
    engText = engText.replace('_', 'a')
    print(engText)
    # tokenize
    morph = nltk.word_tokenize(engText)
    # get pos
    pos = nltk.pos_tag(morph)
    # get people name
    people = [i[0] for i in tagger.tag(morph) if i[1] == 'PERSON']
    # get noun
    nouns = [i for i in pos if i[1] in typeOfNoun]

    for word in nouns:
        if word[1] in common:
            if word[0] in uncountable:
                if word[0] in already:
                    result.append((word[0], ("the",)))
                else:
                    already[word[0]] = True
                    result.append((word[0], (None,)))
            else:
                if word[0][0] in vowelLetter:
                    if not pronunciation_detect(word[0]):
                        result.append((word[0], consonant(word)))
                    else:
                        result.append((word[0], vowel(word)))
                else:
                    if pronunciation_detect(word[0]):
                        result.append((word[0], vowel(word)))
                    else:
                        result.append((word[0], consonant(word)))
        else:
            if word[0] in people:# word is people name
                result.append((word[0], ("a", "the", None)))
            else:
                result.append((word[0], ("the", None)))
    print(result)
    return result
