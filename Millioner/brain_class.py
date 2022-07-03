import random
class Brain:
    def __init__(self,question_list):
        
        self.question_list=question_list
        self.prize = 0
        self.game_is_on = True
        self.hint=['50 на 50','Звонок другу','Право на ошибку']
        
    
    
    def next_question(self,question_number):
        def prepare_answers(answers_tuple):
            """
            Данная функция перемешивает список ответов и возвращает новый
            список и индекс правильного ответа в этом списке
            """
            right_answer = answers_tuple[0]
            answers = list(answers_tuple)
            random.shuffle(answers)
            right_answer_position=answers.index(right_answer)
            for i in range(0,4):
                print(f'{i+1}. {answers[i]}')
            
            return answers,right_answer_position
        
        question_fee = [500,1000,2500,5000,10000,25000,50000,100000,250000,500000,1000000]
        print('-'*20)
        print(f'{question_number+1} ВОПРОС. {self.question_list[question_number].text}')
        answers_list,right_answer_index = prepare_answers(self.question_list[question_number].answers)
        right_answer_position= right_answer_index + 1
        
        for j in range(5,len(self.hint)+5):
            print(f'{j}. {self.hint[j-5]}')
        answer = int(input('Ваш ответ: '))
        final_answer = 0
        if answer>4:
            if self.hint[answer-5] == '50 на 50':
                def fifty_fifty(answers,right_index):
                    """
                    Данная функция убирает 2 неверных ответа из списка
                    """
                    start = True
                    while start:
                        remain_index = random.randint(0,3)
                        if remain_index != right_index:
                            start = False
                    if remain_index > right_index:
                        print(f'{right_index+1}. {answers[right_index]}')
                        print(f'{remain_index+1}. {answers[remain_index]}')
                    else:
                        print(f'{remain_index+1}. {answers[remain_index]}')
                        print(f'{right_index+1}. {answers[right_index]}')
                print('Компьютер убрал два неверных варианта ответа')
                fifty_fifty(answers_list,right_answer_index)
                final_answer = int(input('Ваш окончательный ответ: '))
                
            if self.hint[answer-5] == 'Право на ошибку':
                print('Вы можете использовать право на ошибку')
                try_answer = int(input('Как вы думаете, какой ответ: '))
                
                if try_answer != right_answer_position:
                    final_answer = int(input('Вы не угадали, попробуйте ещё раз: '))
                else:
                    final_answer = try_answer
                
            if self.hint[answer-5] == 'Звонок другу':   
                print(f'Мы позвонили вашему другу Алесею и он абсолютно уверен, что правильный ответ под номером {right_answer_position}')
                final_answer = int(input('Ваш окончательный ответ: '))
            del self.hint[answer-5]
        if (answer == right_answer_position) or (final_answer == right_answer_position):
            
            print(f'Правильно, вы заработали {question_fee[question_number]} рублей')
            if (question_fee[question_number]>=100000) and (question_fee[question_number] <1000000):
                print('Несгораемая сумма 100000')
                self.prize += 100000
            if question_fee[question_number] == 1000000:
                print('Поздравляю, вы стали миллионером!!!')
                self.game_is_on = False
        else:
             self.game_is_on = False
             print('Вы проиграли')
             if self.prize > 0:
                 print('Но вы получили несгораемую сумму 100000 рублей')