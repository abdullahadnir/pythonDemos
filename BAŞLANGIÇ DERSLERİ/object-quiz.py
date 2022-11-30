#Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def CheckAnswer(self, answer):
        return self.answer == answer
    

#Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
        
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}/{len(self.questions)} : {question.text}')
        
        for  q in question.choices:
            print('-'+ q)
            
        answer = input('Cevap : ')
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self,answer):
        question = self.getQuestion()
        
        if question.CheckAnswer(answer):
            self.score +=1
        self.questionIndex += 1
        
        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
            
    def showScore(self):
        print('Score : ', self.score) 
        
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalQuestion:
            print('Quiz Bitti.')
        else:
            print(f'Quesiton {questionNumber} of {totalQuestion}'.center(100,'*'))
                   
        
    
        
q1 = Question('En iyi Programlama Dili Hangisidir ? ', ['C#','Python', 'javascript', 'java'],'python')
q2 = Question('En çok İzlenen Film Hangisidir  ? ', ['Interstaller','Fight Club', 'Inception', 'The 100'],'inception')
q3 = Question('En Sevilen Ders Hanigisidir ? ', ['Matematik','Fizik', 'Kimya', 'Biyoloji'],'matematik')
q4 = Question('En iyi Programlama Dili Hangisidir ? ', ['C#','Python', 'javascript', 'java'],'python')
q5 = Question('En iyi Programlama Dili Hangisidir ? ', ['C#','Python', 'javascript', 'java'],'python')

questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)

quiz.loadQuestion()
