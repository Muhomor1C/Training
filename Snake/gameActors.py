class Snake:

    def __init__(self, width, hight, volume, color):
        self.bodyLenght = 1 #Длина змеи в клетках. При старте == 1
        self.headPosition_x = int(width/2) #  Начальные координаты головы ---
        self.headPosition_y = int(hight/2)
        self.bodyPosition = [] # Список с Координатами всех клеток змеи
        self.bodyPosition.append((self.headPosition_x, self.headPosition_y))
        self.direction = "STOP" # Пока не нажали одну из клавиш управления - стоим. Далее - направление
        self.volume = volume  # Размер клетки
        self.width = width # Доступная ширина поля
        self.hight = hight # Доступная высота поля
        self.color = color


    def move(self):
        """Обеспечивает один шаг в нужном направлении
            и актуализирует список bodyPosition"""
        direction = self.direction
        if direction == "STOP":
            return
        if len(self.bodyPosition) > self.bodyLenght: # Если змея занимает места больше чем положено
            self.bodyPosition.pop(0)  # Удаляем из списка bodyPosition клетку хвоста
        volume = self.volume
        hight = self.hight
        width = self.width

        if direction == "UP":
            self.headPosition_y -= volume
            if self.headPosition_y < 0:
                self.headPosition_y = hight - volume
        elif direction == "DOWN":
            self.headPosition_y += volume
            if self.headPosition_y == hight:
                self.headPosition_y = 0
        elif direction == "LEFT":
            self.headPosition_x -= volume
            if self.headPosition_x < 0:
                self.headPosition_x = width - volume
        elif direction == "RIGHT":
            self.headPosition_x += volume
            if self.headPosition_x == width:
                self.headPosition_x = 0

        self.bodyPosition.append((self.headPosition_x, self.headPosition_y)) # Добавляем координаты головы




