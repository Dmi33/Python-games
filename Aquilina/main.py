import random
user_deck=[]
computer_deck=[]
def prepare_deck(players_deck):
    """
    После реализации данной функции для колоды игрока,
    у него на руках должно остаться по одной карте каждого номинала и
    колода должна быть перемешана
    """
    new_players_deck = []
    for player_card in players_deck:
        if player_card not in new_players_deck:
            new_players_deck.append(player_card)
    random.shuffle(new_players_deck)
    return new_players_deck

def make_move(player1_deck,player2_deck,position=random.randint(0, (len(user_deck)))):
    """
    Данная функция описывает ход каждого игрока.
    Пользователь выбирает позицию карты, которую 
    хочет взять, а компьютер выбирает рандомайзером.
    Затем игрок берёт карту сопперника и если у него есть к ней парная, 
    то обе карты уходят в сброс, а если нет - забирает карту себе
    
    """
    new_card = player2_deck[position]
    player2_deck.remove(new_card)
    print(f'Взята карта {new_card}')
    if new_card in player1_deck:
        player1_deck.remove(new_card)
        print('Найдена парная к ней - обе карты отправляются в сброс')
    else:
        player1_deck.append(new_card)
        random.shuffle(player1_deck)
        print('Не найдена парная к ней - карта берётся на руки')
        
def check_win (user_deck,computer_deck):
    """
    Данная функция проверяет наличие карт в колодах игрока и компьютера
    и если одна из них пустая - заканчивает игру
    """
    continue_game = True        
    if len(user_deck)==0:
        print('ПОЗДРАВЛЯЮ, ВЫ ПОБЕДИЛИ!!!')
        continue_game= False
    elif len(computer_deck)==0:
        print('СОБОЛЕЗНУЮ, ВЫ ПРОИГРАЛИ(')
        continue_game= False
    return continue_game
    
    
    
    
#разделим колоду между двумя игроками
spades =[6,7,8,9,10,'J','Q♠','K','A']
hearts =[6,7,8,9,10,'J','K','A'] 
diamonds =[6,7,8,9,10,'J','K','A']
clubs=[6,7,8,9,10,'J','K','A']
deck = [spades,hearts,diamonds,clubs]

for suit in deck:
    for card in suit:
        who_get = random.randint(0,1) #0-игрок,1-компьютер
        if (who_get == 0):
            if len(user_deck)<17:
                user_deck.append(card)
            else:
                computer_deck.append(card)
        else:
            if len(computer_deck)<17:
                computer_deck.append(card)
            else:
                user_deck.append(card)
        

user_deck = prepare_deck(user_deck)    
computer_deck = prepare_deck(computer_deck)    

game_is_on = True
while game_is_on:
    print('Ваша колода:')
    print(user_deck)
    print('-'*30)
    print('-'*30)
    try:
        card_position = int(input(f'Ваш ход, выбирайте позицию карты из колоды противника,у него их {len(computer_deck)}:  '))
        if card_position not in range(1,len(computer_deck)+1):
            raise Exception('Ошибка ввода')
    except Exception:
            continue
    
    
    make_move(user_deck,computer_deck,position=card_position-1)
    continue_game = check_win(user_deck,computer_deck)
    print('-'*30)
    print('-'*30)
    if continue_game:
        print('Ход компьютера:')
        make_move(computer_deck,user_deck)
        game_is_on = check_win(user_deck,computer_deck)
        print('-'*30)
        print('-'*30)
    else:
        game_is_on=False
    
