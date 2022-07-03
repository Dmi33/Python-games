class Question:
    """
    Данный класс будет создавать вопросы и список ответов,
    первый элемент списка - правильный ответ
    """
    def __init__(self,text,answers):
        self.text = text
        self.answers = answers