from flask import Flask, jsonify
from flask_restful import Api, Resource, request
import pandas as pd
import json
from flask_cors import CORS
from collections import defaultdict

app = Flask(__name__)
CORS(app)
api = Api(app)
port = 80

class MainBase(Resource):
    def get(self):
        return {'data': 'combined 7 apis', 'inputs': ['test1 (personality explorer)', 'test2 (interest explorer)','test3 (career explorer)','test4 (Career motivation)', 'test5 (EQ explorer)', 'test6 (Learning style explorer)', 'test7 (subject analysis)']}
        
api.add_resource(MainBase, '/')

      
###################################### Test 1 Personality Start #############################        
class Base1(Resource):
    def get(self):
        return {'DATA':'PERSONALITY EXPLORER API', 'Input':[{'questions':'Get 64 questions'},{'answers':'64 responses between 1 to 5'}]}#,{'bar':'Get Bar Plot'},{'pie':'Get Pie Plot'}]}

class Questions1(Resource):
    def get(self):
        df = pd.read_excel('data_cat.xlsx')
        return df['Q'].to_list()

class test1(Resource):   
    def get(self,s):
        #s = "4 2 3 5 3 5 2 2 4 2 4 3 4 4 4 4 4 3 4 4 4 4 3 4 5 3 3 5 3 3 1 1 2 4 2 2 2 2 2 1 3 5 2 3 2 4 4 2 5 4 2 4 3 2 3 4 4 2 4 4 3 2 4 4"
        s = s.split()
        t = ['Extravert','Extravert','Extravert','Extravert','Extravert','Extravert','Extravert','Extravert','Extravert','Feeling','Feeling','Feeling','Feeling','Feeling','Feeling','Feeling','Feeling','Feeling','Feeling','Introvert','Introvert','Introvert','Introvert','Introvert','Introvert','Introvert','Intuitive','Intuitive','Intuitive','Intuitive','Intuitive','Intuitive','Intuitive','Intuitive','Judging','Judging','Judging','Judging','Judging','Judging','Judging','Judging','Perceiving','Perceiving','Perceiving','Perceiving','Perceiving','Perceiving','Perceiving','Perceiving','Sensing','Sensing','Sensing','Sensing','Sensing','Sensing','Sensing','Sensing','Thinking','Thinking','Thinking','Thinking','Thinking','Thinking']
        
        interest_scores = {'Extravert': 0, 'Feeling': 0, 'Introvert': 0, 'Intuitive': 0, 'Judging': 0, 'Perceiving': 0, 'Sensing': 0, 'Thinking': 0}
        for decision,j in zip(s,t):
          if decision == "1":
            interest_scores[j] += 1
          elif decision == "2":
            interest_scores[j] += 2
          elif decision == "3":
            interest_scores[j] += 3
          elif decision == "4":
            interest_scores[j] += 4
          else:
            interest_scores[j] += 5
            
        test1_dict = interest_scores

        string = ""
        if interest_scores['Extravert'] >= interest_scores['Introvert']:
          string += "E"
        else:
          string += "I"
        if interest_scores['Sensing'] >= interest_scores['Intuitive']:
          string += "S"
        else:
          string += "N"
        if interest_scores['Thinking'] >= interest_scores['Feeling']:
          string += "T"
        else:
          string += "F"
        if interest_scores['Judging'] >= interest_scores['Perceiving']:
          string += "J"
        else:
          string += "P"
        f = open('mbti.json',)
  
        data = json.load(f)

        a1 = test1_dict
        a2 = data[string]
        keymax1 = max(a1, key=a1.get)
        # return {"Attribute":keymax1,"Score":a1, "Analysis":a2}
        return (a2)

api.add_resource(Base1, '/test1')
api.add_resource(Questions1, '/test1/questions')
api.add_resource(test1, '/test1/answers/<string:s>')
###################################### Test 1 Personality end #############################        


###################################### Test 2 Interest Start ################################
class Base2(Resource):
    def get(self):
        return {'DATA':'Interest Explorer API', 'Input':[{'questions':'Get 60 questions'},{'answers':'60 responses between 1 to 5'}]}#,{'bar':'Get Bar Plot'},{'pie':'Get Pie Plot'}]}

class Questions2(Resource):
    def get(self):
        df = pd.read_excel('Interest_questions.xlsx')
        return df['Question'].to_list()

class test2(Resource):
        
    def get(self,s):
        #s = "3 5 2 2 4 2 4 3 4 4 4 4 4 3 4 4 4 4 3 4 5 3 3 5 3 3 1 1 2 4 2 2 2 2 2 1 3 5 2 3 2 4 4 2 5 4 2 4 3 2 3 4 4 2 4 4 3 2 4 4"
        t = ['Realistic','Realistic','Realistic','Realistic','Realistic','Realistic','Realistic','Realistic','Realistic','Realistic','Social','Social','Social','Social','Social','Social','Social','Social','Social','Social','Investigative','Investigative','Investigative','Investigative','Investigative','Investigative','Investigative','Investigative','Investigative','Investigative','Artistic','Artistic','Artistic','Artistic','Artistic','Artistic','Artistic','Artistic','Artistic','Artistic','Enterprising','Enterprising','Enterprising','Enterprising','Enterprising','Enterprising','Enterprising','Enterprising','Enterprising','Enterprising','Conventional','Conventional','Conventional','Conventional','Conventional','Conventional','Conventional','Conventional','Conventional','Conventional']
        interest_scores = {'Artistic' :0,'Conventional':0,'Enterprising':0,'Investigative':0,'Realistic':0,'Social':0}
        for decision,j in zip(s,t):
          if decision == "1":
            interest_scores[j] += 1
          elif decision == "2":
            interest_scores[j] += 2
          elif decision == "3":
            interest_scores[j] += 3
          elif decision == "4":
            interest_scores[j] += 4
          else:
            interest_scores[j] += 5
        
        test2_dict = interest_scores
        
        dict1 = interest_scores
        sorted_dict = {}
        sorted_keys = sorted(dict1, key=dict1.get, reverse=True)  
        sorted_keys = sorted_keys[:3]
        for w in sorted_keys:
            sorted_dict[w] = dict1[w]
        #return sorted_dict

        df = pd.read_excel('Description.xlsx')
        x = df.columns
        data = {}
        attr = list(sorted_dict.keys())
        for i in range(len(df)):
            data[df.iloc[i,0].strip()] = {x[1].strip():df.iloc[i,1], x[2].strip():df.iloc[i,2].split('\n'), x[3].strip():df.iloc[i,3].split('\n'), x[4].strip():df.iloc[i,4].split('\n'),x[5].strip():df.iloc[i,5], x[6].strip():df.iloc[i,6].split('\n'),x[7].strip():df.iloc[i,7].split('\n')}
        
        keymax2 = max(test2_dict, key=test2_dict.get)
        return {"Attribute":keymax2, "score":test2_dict, 'Primary Interest':{attr[0]:data[attr[0]]},'Secondary Interest':{attr[1]:data[attr[1]]},'Tertiary Interest':{attr[2]:data[attr[2]]}}

api.add_resource(Base2, '/test2')
api.add_resource(test2, '/test2/answers/<string:s>')
api.add_resource(Questions2, '/test2/questions')
###################################### Test 2 interest end #############################       



###################################### Test 3 career start #############################
df3 = pd.read_excel('carrier.xls')
df3.set_index("Key")

d3 = {'Act in a TV show or movie': 'A', 'Analyze handwriting': 'D', 'Analyze reports and records': 'E', 'Answer customer questions': 'H', 'Appraise the value of a house': 'N', 'Assemble cars': 'F', 'Assess student progress': 'M', 'Audit taxes for the government': 'K', 'Balance a checkbook': 'N', 'Be in charge of replanting forests': 'C', 'Broadcast the news': 'A', 'Build an airport': 'E', 'Build kitchen cabinets': 'L', 'Build toys with written instructions': 'E', 'Care for injured animals': 'Q', 'Care for young children': 'M', 'Check products for quality': 'F', 'Choreograph a dance': 'A', 'Collect rocks': 'B', 'Design a book cover': 'A', 'Design a freeway': 'L', 'Design a website': 'P', 'Design an airplane': 'L', 'Design indoor sprinkler systems': 'B', 'Design landscaping': 'C', 'Develop personnel policies': 'G', 'Direct the takeoff/landing of planes': 'R', 'Draft a blueprint': 'L', 'Drive a taxi': 'R', 'Enter data': 'P', 'Fight fires': 'D', 'Figure out why someone is sick': 'B', 'File books at the library': 'M', 'Fix a control panel': 'F', 'Fix a television set': 'E', 'Fly an airplane': 'R', 'Give shots': 'O', 'Give tech support to computer users': 'P', 'Guard an office building': 'D', 'Guard money in an armored car': 'D', 'Guide an international tour group': 'I', 'Help former prison inmates find work': 'J', 'Help friends with personal problems': 'J', 'Help people at a mental health clinic': 'O', 'Hire new staff': 'G', 'Keep company business records': 'G', 'Keep payroll records for a company': 'G', 'Lead others': 'K', 'Learn about ethnic groups': 'I', 'Learn how things grow and stay alive': 'C', 'Lobby or show support for a cause': 'K', 'Locate a missing person': 'D', 'Make three-dimensional items': 'E', 'Manage a fish hatchery': 'Q', 'Manage a veterinary clinic': 'Q', 'Manage an information system': 'P', 'Operate a cash register': 'G', 'Operate a machine': 'F', 'Operate a printing press': 'A', 'Operate heavy equipment': 'E', 'Oversee a logging crew': 'C', 'Pack boxes at a warehouse': 'R', 'Plan activities for adult day care': 'J', 'Plan educational lessons': 'M', 'Plan estate disbursements/payments': 'N', 'Plan special diets': 'O', 'Plant and harvest crops': 'C', 'Play an instrument': 'A', 'Play the stock market': 'N', 'Protect our borders': 'K', 'Protect the environment': 'C', 'Provide consumer information': 'J', 'Provide spiritual guidance to others': 'J', 'Put together small tools': 'F', 'Refinance a mortgage': 'N', 'Remodel old houses': 'L', 'Replace a car window and fender': 'R', 'Research soybean use in paint': 'C', 'Run a department store': 'H', 'Run a factory sewing machine': 'F', 'Run a school': 'M', 'Run ventilators/breathing machines': 'O', 'Sell cars': 'H', 'Sell clothes': 'H', 'Sell insurance': 'N', 'Serve meals to customers': 'I', 'Sing in a concert': 'A', 'Solve a burglary': 'D', 'Solve technical problems': 'P', 'Sort and date dinosaur bones': 'B', 'Start a business': 'G', 'Sterilize surgical instruments': 'O', 'Study human behavior': 'B', 'Study soil conditions': 'B', 'Study the causes of earthquakes': 'B', 'Study weather conditions': 'B', 'Take an X-ray': 'O', 'Take care of children': 'J', 'Teach dancing': 'A', 'Train animals': 'Q', 'Train racehorses': 'Q', 'Tutor students': 'M', 'Use a calculator': 'G', 'Work as a restaurant host or hostess': 'I', 'Work at a zoo': 'Q', 'Work at an amusement park': 'I', 'Work in a courtroom': 'D', 'Work in a nursing home': 'J', 'Work in an office': 'G', 'Work with your hands': 'E', 'Wrap a sprained ankle': 'O', 'Write a computer program': 'P', 'Write for a newspaper': 'A', 'Write reports': 'D'}

class base3(Resource):
  def get(self):
    return {'DATA':'Career Explorer API', 'Input':[{'questions':'Get 114 questions'},{'answers':'114 binary responses 0 or 1'}]}

class Questions3(Resource):
    def get(self):
        return list(d3.keys())    

class Answers3(Resource):        
    def get(self,responses):
        ans = dict()
        score3 = defaultdict(int)
        for i,j in zip(d3.values(),responses):
            if j == '1':
                score3[i]+=1
        m = sorted(score3, key=score3.get, reverse=True)[:1]
        p = df3[df3['Key']==m[0]]
        ans['Stream']= p.iloc[0][3]
        ans['Career Clusters'] = p.iloc[0][5]
        ans['Career Clusters']=ans['Career Clusters'].split('\n')
        return ans

api.add_resource(base3, '/test3')
api.add_resource(Questions3, '/test3/questions')
api.add_resource(Answers3, '/test3/answers/<string:responses>')
###################################### Test 3 career end #############################    



###################################### Test 4 career motivate start ############################# 
df4 = pd.read_excel(r'data/wvt.xls')

f = open('test4.json',)
data4 = json.load(f)

dc4 =  dict(df4.values.tolist())
def scorecal(name,score4):
    x = ''
    if score4<=9 and score4<=19:
        x = data4[name]['Low']
    elif score4>= 20 and score4<=39:
        x = data4[name]['Medium']
    elif score4>= 40 and score4<=49:
        x = data4[name]['High']
    return x


class base(Resource):
    def get(self):
        return {'Data':'TEST 6 Work Value Test API','Parameters':['Altruism', 'Autonomy', 'Creativity', 'Financial Reward', 'Influence', 'Performance', 'Prestige', 'Security', 'Self-Development', 'Structure', 'Variety', 'Work Life Balance', 'Work Relationships', 'Work Conditions'],
                'Input':['questions','answer']}
    

class Questions(Resource):
    def get(self):
        return {'Questions':list(dc4.keys())}
    

class Answer_List(Resource):
    def get(self):
        return {'Enter responses to 140 Questions':{'1':'indicates that you ABSOLUTELY DISAGREE with the statement',
                                                   '2':'indicates that you DISAGREE with the statement',
                                                   '3':'indicates that you are UNSURE of the statement',
                                                   '4':'indicates that you AGREE with the statement',
                                                   '5':'indicates that you ABSOLUTELY AGREE with the statement'}}

class Answers(Resource):
    def get(self,responses):
        if responses != 'favicon.ico':
            def Convert4(string):
                li = list(string.split())
                return li
            responses = (Convert4(responses))
            score4 = defaultdict(int)
            d4 = {}
            for i,j in zip(dc4.values(),responses):
        
                if j == '1':
                    score4[i]+=1
                elif j == '2':
                    score4[i]+=2
                elif j == '3':
                    score4[i]+=3
                elif j == '4':
                    score4[i]+=4
                elif j == '5':
                    score4[i]+=5
            
            ss = sorted(score4.items(), key=lambda x:x[1],reverse=True)
            sorted_score4 = dict(ss)
            for i,j in sorted_score4.items():
                if i == 'Structure':
                    d4[i] = scorecal(i,j)    
                elif i == 'Prestige':
                    d4[i] = scorecal(i,j)
                elif i == 'Influence':
                    d4[i] = scorecal(i,j)
                elif i == 'Altruism':
                    d4[i] = scorecal(i,j)
                elif i == 'Performance':
                    d4[i] = scorecal(i,j)
                elif i == 'Creativity':
                    d4[i] = scorecal(i,j)
                elif i == 'Variety':
                    d4[i] = scorecal(i,j)
                elif i == 'Financial Reward':
                    d4[i] = scorecal(i,j)
                elif i == 'Autonomy':
                    d4[i] = scorecal(i,j)
                elif i == 'Work Life Balance':
                    d4[i] = scorecal(i,j)
                elif i == 'Self-Development':
                    d4[i] = scorecal(i,j)
                elif i == 'Work Relationships':
                    d4[i] = scorecal(i,j)
                elif i == 'Work Conditions':
                    d4[i] = scorecal(i,j)
                elif i == 'Security':
                    d4[i] = scorecal(i,j)
                    
        keymax4 = max(sorted_score4, key=sorted_score4.get)            
        return {"Attribute":keymax4, 'Score':sorted_score4,'Analysis':d4}

api.add_resource(base,'/test4') 
api.add_resource(Questions,'/test4/questions')     
api.add_resource(Answer_List,'/test4/answers')  
api.add_resource(Answers,'/test4/answers/<string:responses>')
###################################### Test 4 career start ############################# 



###################################### Test 5 EQ start ############################# 
questions5 = {'I realise immediately when I lose my temper': 'Self Perception', "I can 'reframe' bad situations quickly": 'Self Conduct', "I am always able to see things from the other person's viewpoint": 'Social Consciousness', 'I am an excellent listener': 'Social Conduct', 'I know when I am happy': 'Self Perception', "I do not wear my 'heart on my sleeve'": 'Self Conduct', "I am excellent at empathising with someone else's problem": 'Social Consciousness', "I never interrupt other people's conversations": 'Social Conduct', 'I usually recognise when I am stressed': 'Self Perception', 'Others can rarely tell what kind of mood I am in': 'Self Conduct', 'I can tell if someone is not happy with me': 'Social Consciousness', 'I am good at adapting and mixing with a variety of people': 'Social Conduct', "When I am being 'emotional' I am aware of this": 'Self Perception', "I rarely 'fly off the handle' at other people": 'Self Conduct', 'I can tell if a team of people are not getting along with each other': 'Social Consciousness', 'People are the most interesting thing in life for me': 'Social Conduct', 'When I feel anxious I usually can account for the reason(s)': 'Self Perception', 'Difficult people do not annoy me': 'Self Conduct', 'I can usually understand why people are being difficult towards me': 'Social Consciousness', "I love to meet new people and get to know what makes them 'tick'": 'Social Conduct', "I always know when I'm being unreasonable": 'Self Perception', 'I can consciously alter my frame of mind or mood': 'Self Conduct', "Other individuals are not 'difficult' just 'different'": 'Social Consciousness', 'I need a variety of work colleagues to make my job interesting': 'Social Conduct', 'Awareness of my own emotions is very important to me at all times': 'Self Perception', 'I do not let stressful situations or people affect me once I have left work': 'Self Conduct', 'I can understand if I am being unreasonable': 'Social Consciousness', 'I like to ask questions to find out what it is important to people': 'Social Conduct', 'I can tell if someone has upset or annoyed me': 'Self Perception', 'I rarely worry about work or life in general': 'Self Conduct', 'I can understand why my actions sometimes offend others': 'Social Consciousness', 'I see working with difficult people as simply a challenge to win them over': 'Social Conduct', "I can let anger 'go' quickly so that it no longer affects me": 'Self Perception', 'I can suppress my emotions when I need to': 'Self Conduct', "I can sometimes see things from others' point of view": 'Social Consciousness', 'I am good at reconciling differences with other people': 'Social Conduct', 'I know what makes me happy': 'Self Perception', 'Others often do not know how I am feeling about things': 'Self Conduct', 'Reasons for disagreements are always clear to me': 'Social Consciousness', 'I generally build solid relationships with those I work with': 'Social Conduct'}
data5 = {'Self Perception': {'Brief': ['This literally forms the heart of Emotional Intelligence. It consists of three competencies namely emotional self perception, accurate self - assessment and self confidence. The entrance and key of these areas is the ability to be critically self-reflective. Let’s go through each of these components in brief.'], 'Emotions': ['Emotional Self Perception - is where you are able to read and understand your emotions as well as recognise their effect on work performance and relationships.', 'Accurate Self Assessment - is where you are able to give a realistic evaluation or test of your strengths and weaknesses.', 'Self Confidence - is where you have a positive and strong sense of one’s self-worth.'], 'Remember!!': ['To understand and enhance self - perception, one must learn to be mindful. It involves focusing on the current moment as well as how you’re feeling.', 'Maintain a daily journal or a diary where you can freely put down your emotions while also analysing them, on a day to day basis.', 'In order to build self perception, you need to understand your strengths and weaknesses.', 'You could also conduct a SWOT analysis yourself, and seek help and feedback from your superiors, colleagues, friends, family and so on.']}, 'Self Conduct': {'Brief': ['Self conduct is your ability to manage stress, stay true (to yourself and others), take responsibility for your work performance and behaviour, handle change, be open to new ideas, work under pressure and so on. The main components under this competency are self-discipline, clarity, resilience, performance oriented and initiative. Let’s look at what each of these components actually mean.'], 'Emotions': ['Self - Discipline - is what keeps disruptive or riotous emotions and impulses under control.', 'Clarity - involves maintaining standards of honesty and integrity, while managing yourself and responsibilities.', 'Resilience - means being dynamic, and flexibly adapting to changing situations and overcoming challenges.', 'Performance oriented - is the steering push to meet an internal standard of excellence.', 'Initiative - simply means being ready to seize opportunities as and when they come and take instantaneous action.'], 'Remember!!': ['If anger is something that affects you oftenly, note down what triggers you, and ponder upon why this is happening.', 'Use techniques such as deep breathing, or slowly counting from 1-10 to calm yourself.', "Give yourself time to pause and calmly think before you respond to emails or requests, so that you don't say something that you'll later regret.", 'Apart from anger, you may get affected by other harmful emotions such as anxiety, pressure and stress. You must learn how to cope up with these emotions and effectively come out of that negative bubble.']}, 'Social Consciousness': {'Brief': ['Social consciousness indicates your ability to recognise how others around you feel, anticipate people’s needs, work with various types of people, understand why others act in certain ways. The primary competencies under social consciousness are empathy, operational awareness and service orientation. Let’s study these in brief.'], 'Emotions': ['Empathy - is understanding others, putting yourself in their shoes and taking an active interest in what concerns them.', 'Operational awareness - is the ability to analyse and be updated with the flow of an organisational life, build decision networks and navigate politics.', 'Service orientation - which is recognising and meeting customers needs.'], 'Remember!!': ["To develop empathy, start by simply thinking from people's point of view. Imagine how they may be feeling, what they may be going through and make sure you actively listen to them to understand them fully when they express their emotions to you.", 'Put yourself into their shoes and you’ll learn the value of empathy.', 'Try not to interrupt or talk about your own feelings during the conversation.', "You must learn to study their body language - it can tell you a lot about their emotions. If you watch and listen to others, you'll quickly become attuned to how they feel."]}, 'Social Conduct': {'Brief': ['Social conduct indicates your ability to effectively communicate, influence and lead others. It also involves causing a positive change, managing conflicts, building bonds with others through proper communication skills. The competencies under this cluster are given as visionary, social development, impact, change stimulant, conflict handler, building fellowship and team spirit. Here’s a brief about each of these competencies.'], 'Emotions': ['Visionary - means motivating and driving groups as well as individuals.', 'Social development - is the tendency to strengthen and support the abilities of others through proper feedback and counsel.', 'Impact - is defined as the ability to exercise a wide range of persuasive strategies with integrity, and also includes listening and sending messages that are easy to understand and follow.', 'Change stimulant - is the skill of generating new ideas and leading people in a new direction.', 'Conflict handler - is resolving disagreements, disputes within the organisation and collectively developing solutions;', 'Building fellowship - means building, nurturing and maintaining relationships with peers;', 'Team spirit - is the promotion of cooperation, building teams and working in unison in an organisation.'], 'Remember!!': ['Learn to develop trust and rapport with your peers - this is an indispensable aspect of building good work relations.', "Don't shy away from negative situations, either. Learn how to deal with conflict and other difficult situations effectively.", "If you're uncomfortable in social situations, work on building self-confidence. Start slowly, but then look for opportunities to practise your skills with larger groups."]}}


class base5(Resource):
  def get(self):
    return {'DATA':'EQ Explorer API','Emotion Intelligence Test':"This self-assessment questionnaire is designed to get you thinking about the various competences of emotional intelligence as they apply to you.", 'inputs':['questions','answers']}
        

class Questions5(Resource):
    def get(self):
        return {'questions':list(questions5.keys())}   

class Answers_list5(Resource):
    def get(self):
        return {'Enter responses to 50 questions':{'0':'indicates that the statement does NOT apply at all',
                                                   '1':'indicates that the statement applies about HALF the time',
                                                   '2':'indicates that the statement ALWAYS applies to you'}}
    
class Answers5(Resource):        
    def get(self,responses):
        responses =responses.split()
        score5 = defaultdict(int)

        for i,j in zip(questions5.values(),responses):
        
            if j == '1':
                score5[i]+=1
            elif j == '2':
                score5[i]+=2
            elif j == '0':
                score5[i]+=0
        
        ss5 = sorted(score5.items(), key=lambda x:x[1],reverse=True)
        sorted_score5 = dict(ss5)
        keymax5 = max(sorted_score5, key=sorted_score5.get)
        return {"Attribute":keymax5, 'Score':sorted_score5, 'Analysis':data5[list(sorted_score5.keys())[0]]}
       
api.add_resource(base5, '/test5')
api.add_resource(Questions5, '/test5/questions')
api.add_resource(Answers_list5, '/test5/answers')
api.add_resource(Answers5, '/test5/answers/<string:responses>')
###################################### Test 5 EQ end ############################# 



###################################### Test 6 Learning start #############################    
info6 = {'Auditory Learner': {'Advice': ['1. Sit at such a position, where you can hear.',   '2. Have your hearing checked on a regular basis.',   '3. Use flashcards to learn new words; read them out loud.',   '4. Make it a habit to read stories, assignments, or directions out loud.',   '5. Record yourself spelling out words and then listen to the recording.',   '6. Have test questions read to you out loud.',   '7. Study new material by reading it out loud.'],  'Brief explanation': ['1. As an auditory learner, you learn by hearing and listening. You understand and remember things you have heard. You store information by the way it sounds, and you have an easier time understanding spoken instructions than written ones. You often learn by reading out loud because you have to hear it or speak it in order to know it.',   '2. As an auditory learner, you probably hum or talk to yourself or others when bored. People may think you are not paying attention, even though you may be listening and understanding every line that is being spoken.'],  'Characteristics': ['1. You are good at remembering people by their names',   '2. You recall spoken information with ease, and are skilled at speaking',   '3. You are well aware of and easily distracted by sounds',   '4. You enjoy listening to audio books, storytelling and podcasts',   '5. You prefer classes in lecture format',   '6. You may record lectures to hear again later ',   '7. You, at all times, benefit from reading out loud',   '8. You enjoy rhymes and rhythmic pattern in language',   '9. According to you, one can benefit from group discussions']}, 'Kinesthetic Learner': {'Advice': ['1. Participate in activities that involve touching, building, moving, or drawing.',   '2. Do lots of hands-on activities like completing art projects, taking walks, or acting out stories.',   "3. It's OK to chew gum, walk around, or rock in a chair while reading or studying.",   '4. Use flashcards and arrange them appropriately in groups to show relationships between ideas.',   '5. Trace words with your finger to learn spelling (finger - spelling).',   '6. Take frequent breaks during reading or studying periods (frequent and small but not long).',   '7. Use a computer to reinforce learning through the sense of touch.'],  'Brief explanation': ['1. As a kinesthetic learner, you learn by touching and doing. You understand and remember things through physical movement. You are a ‘hands-on’ learner who prefers to touch, move, build, or draw what you learn, and you tend to learn better when some type of physical activity is involved. You need to be active and take frequent breaks, you often speak with your hands and with gestures, and you may have difficulty sitting still.',   '2. As a kinesthetic learner, you like to take  and you tend to find reasons to tinker or move around when you become bored. You may have great coordination and good athletic skills. You can easily remember things that were done but may have difficulty remembering what you saw or heard in the process. You often communicate by touching, and you appreciate physically expressed forms of encouragement, such as a pat on the back.'],  'Characteristics': ['1. You are good at and mostly prefer learning through hands-on experience',   '2. You may get bored with traditional textbook learning',   '3. You enjoy moving around and exploring the environment',   '4. You usually enjoy athletics and physical education; and would rather participate than watch',   '5. You appreciate opportunities to go on field trips',   '6. You get satisfaction from building with your hands',   '7. You enjoy classes with physical experiments and can get restless without physical activities.']}, 'Visual Learner': {'Advice': ["1. Sit among the front of the classroom. (no that doesn't make you the teacher's pet!)",   '2. Check your eyesight regularly.',   '3. Learn new words with the help of flash cards, be concise',   '4. Try to visualise and imagine things that you hear or things that are read to you',   '5. Write down or highlight key words, ideas, or instructions',   '6. Draw pictures or charts, diagrams and mind maps to help explain new concepts and then explain the pictures.',   '7. Try to colour code things.',   '8. Avoid distractions during study times.'],  'Brief explanation': ['1. As a visual learner, you learn by reading or seeing pictures. You understand and remember things by sight. You can picture what you are learning in your head, and you learn best by using methods that are primarily visual. While learning you like to draw a picture of what is said or asked of you, inside your head.',   '2. As a visual learner, you are usually neat and clean. You often close your eyes to visualise or remember something, and you may have difficulty with spoken directions and may be easily distracted by sounds. You are attracted to colours and to spoken languages (for eg. stories) that are rich in imagery and diagrams.'],  'Characteristics': ['1. You are good at remembering people by their face',   '2. You can accurately recognise body language and facial expressions',   '3. You are good at taking notes in the form of text and doodles',   '4. You are most likely to comprehend visual information such as charts, graphs and diagrams',   '5. You recall appearances with ease',   '6. You enjoy learning from video presentations and flash cards',   '7. You have an eye for detail; you are most likely to notice visual details that others might miss.']}}


class Home6(Resource):
    def get(self):
        return {'data':'Learning Style Explorer API', 'inputs':['questions','responses','info']}

class Questions6(Resource):
    def get(self):
        df6 = pd.read_excel('LST_dataset.xls')
        q_dict = df6.to_dict('records')
        return q_dict

class responceinfo6(Resource):
    def get(self):
        return {'data': 'Enter space separated 25 numbers from 1 to 3'}

class Response6(Resource):
    def get(self, res):
        scores6 = {'Visual Learner':0, 'Auditory Learner':0, 'Kinesthetic Learner':0}
        lst = list(res)
        for i in lst:
            if i == '1':
                scores6['Visual Learner'] += 1
            elif i == '2':
                scores6['Auditory Learner'] += 1
            elif i == '3':
                scores6['Kinesthetic Learner'] += 1
        scores6 = sorted(scores6.items(), key=lambda x:x[1], reverse=True)
        sorted_dict6 = dict(scores6)
        mykey = str(list(sorted_dict6.keys())[0])
        dict6_analysis = {mykey:info6[mykey]}
        #sorted_dict4['analysis'] = info4[mykey]
        keymax6 = max(sorted_dict6, key=sorted_dict6.get)
        return {"Attribute":keymax6, "Score": sorted_dict6, "Analysis":dict6_analysis}

class infoinput6(Resource):
    def get(self):
        return {'input': ['Visual Learner', 'Auditory Learner','Kinesthetic Learner']}

class Info6(Resource):
    def get(self, name):
        return info6[name]

api.add_resource(Home6, '/test6')
api.add_resource(Questions6, '/test6/questions')
api.add_resource(responceinfo6, '/test6/responses/')
api.add_resource(Response6, '/test6/responses/<string:res>')
api.add_resource(infoinput6, '/test6/info/')
api.add_resource(Info6, '/test6/info/<string:name>')
###################################### Test 6 learning end #############################



###################################### Test 7 subject start #############################
data7 = dict()
with open('DATA.json') as f7:
    data7 = json.load(f7)

d7 = dict()
def initialize():
  for i in data7.keys():
    de7 = dict()
    for j in data7[i].keys():
      df7 = pd.DataFrame.from_dict(data7[i][j])
      df7 = df7.sample(frac=1)
      df7 = df7.head(10)
      de7[j] = df7.to_dict('records')
    d7[i] = de7

class test7home(Resource):
    def get(self):
      return jsonify({'data':'Test 7 Api', 'inputs':['class', 'subject', 'space separated 10 responses A B C']})

class test7Standard(Resource):
    def get(self,class_):
      initialize()
      return jsonify(d7[class_])

class test7Subjects(Resource):
    def get(self,class_,subject):
      initialize()
      return jsonify(d7[class_][subject])
      
class test7Check(Resource):
    def get(self,class_,subject,ans):
      count = 0
      ans = list(ans.split())
      for i,j in zip(ans,d7[class_][subject]):
         if i==j['Solution']:
           count += 1
      return {'count':count}

api.add_resource(test7home, '/test7')
api.add_resource(test7Standard, '/test7/<string:class_>')
api.add_resource(test7Subjects, '/test7/<string:class_>/<string:subject>')
api.add_resource(test7Check, '/test7/<string:class_>/<string:subject>/<string:ans>')
###################################### Test 7 subject end #############################


if __name__=="__main__":
    app.run(host='0.0.0.0',port=port)
    # app.run(debug=True)
