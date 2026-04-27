from abc import ABC, abstractmethod

class StudyManageable(ABC): #Интерфейс для управления учебным процессом
    @abstractmethod
    def study(self, hours: int) -> str: #Учиться определённое количество часов
        pass
    
    @abstractmethod
    def take_exam(self) -> str: #Сдать экзамен
        pass


class AchievementsInterface(ABC): #Интерфейс для получения достижений и рейтинга
    @abstractmethod
    def get_achievements(self) -> list: #Получить список достижений
        pass
    
    @abstractmethod
    def get_rating(self) -> str: #"Получить рейтинг студента
        pass