class GA:
	items = [] #особи [top, left, width, height]
	iteration = 0 #поколение
	mutation_pc = 30 #процент мутирующих особей
	outbriding_pc = 10 #сколько особей не из лучших попадут в следжущее поколение
	items_cnt = 100 #размер поппуляции(количество особей)
	
	def __init__(self, 
				 mutation_pc = 30, 
				 items_cnt = 100, 
				 outbriding_pc = 10):
		self.mutation_pc = mutation_pc
		self.items_cnt = items_cnt
		self.outbriding_pc = outbriding_pc
	
	def initialisation(self):
		"""зарождение начальной поппуляции
		создадим нужное количество объектов случайно их раскидав по полю
		"""
		for i in range(self.items_cnt):
			
	
	def analise(self):
		"""целевая функция. Просчитыает приспособленность моделей и сортирует их в порядке возрастания значения
		критерием является итоговая площадь колажа"""
		pass
	
	def mutation(self):
		"""осуществляет мутации в поппуляции"""
		pass
	
	def sex(self):
		"""скрещивание особей"""
		pass