from tika import parser

raw = parser.from_file('./Rounds/Set1/Round1.pdf')
myRound = raw['content']
roundClean = myRound[myRound.index("TOSS-UP"):]
qs = roundClean.replace("\n","").split("TOSS-UP")[1:]

class Question:
    def __init__(self, text):
        if text[1] == ")":
            self.number = int(text[0])
            text = text[4:]
        else:
            self.number = int(text[:2])
            text = text[5:]

        tossup_text = text.split("BONUS")[0].strip()
        bonus_text = text.split("BONUS")[1].strip()
            
        toss_split_sa = tossup_text.split("Short Answer")
        if len(toss_split_sa) > 1:
            self.tossup_type = "Short Answer"
            self.subject = toss_split_sa[0].strip()
        else:
            self.tossup_type = "Multiple Choice"
            self.subject = tossup_text.split("Multiple Choice")[0].strip()

        self.tossup_answer = tossup_text.split("ANSWER:")[1].strip()

        if bonus_text[1] == ")":
            bonus_text = bonus_text[4:]
        else:
            bonus_text = bonus_text[5:]

        bonus_text = bonus_text.split(self.subject)[1].strip()


        bonus_split_sa = tossup_text.split("Short Answer")
        if len(bonus_split_sa) > 1:
            self.bonus_type = "Short Answer"
        else:
            self.bonus_type = "Multiple Choice"

        self.bonus_answer = bonus_text.split("ANSWER:")[1].strip().split("Middle School")[0]

        print("Number:", self.number)
        print("Subject:", self.subject)
        print("Toss-Up Type:", self.tossup_type)
        print("Toss-Up Answer:", self.tossup_answer)
        print("Bonus Type:", self.bonus_type)
        print("Bonus Answer:", self.bonus_answer)
        print("--------------------")
        #print(text, end="\n\n-----------\n\n")


questions = []
for q in qs:
    questions.append(Question(q.strip()))
    #print(q, end="\n\n")