class GA:
	items = [] #особи [top, left, width, height]
	generation = 0 #поколение текущее
	generations_cnt = 1000 #максимум поколений
	mutation_pc = 30 #процент мутирующих особей
	outbriding_pc = 10 #сколько особей не из лучших попадут в следжущее поколение
	items_cnt = 100 #размер поппуляции(количество особей)
	
	def _console(self, text:str):
		print(text)
	
	def __init__(self, 
				 mutation_pc = 30, 
				 items_cnt = 100, 
				 outbriding_pc = 10,
				 generations_cnt = 1000):
		self.mutation_pc = mutation_pc
		self.items_cnt = items_cnt
		self.outbriding_pc = outbriding_pc
		self.generations_cnt = generations_cnt
	
	def initialisation(self, objects):
		"""зарождение начальной поппуляции
		создадим нужное количество объектов случайно их раскидав по полю
		"""
		#отсортируем массив объектов по уменьшению площади
		sorted_objects = sorted(objects, key=lambda it: it[0]*it[1], reverse=True)
		#цыкл по особям
		for i in range(self.items_cnt):
			item = [] #сдесь будут координаты всех объектов для текущей особи
			#карта занятости пространства. размером х2 самой большой картинки. заполнили значениями 1000
			map_wieght = [ [1000] * sorted_objects[0][0] * 2 ] * sorted_objects[0][1] * 2 
			self._console(map_wieght)
			#цыкл по объектам(картинкам)
			for obj in sorted_objects: 
				#добавим координаты
				obj_1 = [0,0,*obj]
				max_size = max(*obj) #максимальная сторона
				obj_1_rate = int(max_size / 2) + 1
				item.append(obj_1)
				
				
			
	
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