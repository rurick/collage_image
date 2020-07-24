import random

class GA:
	items = [] #особи [top, left, width, height]
	generation = 0 #поколение текущее
	generations_cnt = 1000 #максимум поколений
	mutation_pc = 30 #процент мутирующих особей
	outbriding_pc = 10 #сколько особей не из лучших попадут в следжущее поколение
	items_cnt = 100 #размер поппуляции(количество особей)
	
	def _console(self, text:str):
		print(text)
	def _out(self, m):
		for r in m:
			print(''.join([chr(32+v) for v in r]))
		print("\n")
	
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
		#преобразуем объекты разделив каждый на 10 чтобы укрупнить пиксель и чтобы размеры были нечетными для того чтобы был центр
		for obj in objects:
			obj[0] = int(obj[0]/10)
			obj[1] = int(obj[1]/10)
			if obj[0] % 2 == 0: obj[0] += 1
			if obj[1] % 2 == 0: obj[1] += 1
		#отсортируем массив объектов по уменьшению площади
		sorted_objects = sorted(objects, key=lambda it: it[0]*it[1], reverse=True)
		#цыкл по особям
		for idx in range(self.items_cnt):
			item = [] #сдесь будут координаты всех объектов для текущей особи
			#карта занятости пространства. размером  самой большой картинки. заполнили значениями 1000
			map_wieght = [ [1000] * sorted_objects[0][0] ] * sorted_objects[0][1] 
			self._out(map_wieght)
			i, j = 0, 0
			#перемешаем случайно координаты кроме 0,0
			line = []
			while i < len(map_wieght):
				while j < len(map_wieght[0]):
					line.append((i,j))
			line.pop(0)
			random.shuffle(line)
			line.insert(0,(0,0))
							
			self._console(map_wieght)
			#цыкл по объектам(картинкам)
			for obj in sorted_objects: 
				#добавим координаты
				obj_1 = [0,0,*obj]
				max_size = max(*obj) #максимальная сторона
				obj_1_rate = int(max_size / 2) + 1 #вес объекта
				#найдём подходящее место (чтобы его вес был больше чем вес объекта)
				i = 0
				while True:
					if map_wieght[line[i][0]][line[i][1]] > obj_1_rate:
						#найдено
						break
					i += 1
				obj_1[0:2] = line[i] #записали координаты найденые	
				item.append(obj_1) #добавили объект в список
				# проверим влазит ли в границы по Х
				delta = obj_1[0] - obj_1[2]
				if delta < 0:
					#на дельту расширим массив  влево
					map_wieght = [[1000]*delta + r for r in map_wieght]
					#увеличим все координаты х объектов
					for it in item:
						it[0] += delta
				if obj_1[0] + obj_1[2] > len(map_wieght):
					map_wieght = [r + [1000]*delta for r in map_wieght]
					
				# проверим влазит ли в границы по Y
				delta = obj_1[1] - obj_1[3]
				if delta < 0:
					#на дельту расширим массив  вверх
					map_wieght = [[1000]*len(map_wieght) * delta] + map_wieght
					#увеличим все координаты y объектов
					for it in item:
						it[1] += delta
				delta = obj_1[1] + obj_1[3]
				if delta > len(map_wieght[1]):	
					map_wieght = map_wieght + [[1000]*len(map_wieght) * delta]
				
				#запишем данные
				i, j = 0, 0
				while i < obj_1[2]:
					while j < obj_1[3]:
						map_wieght[obj_1[0] - int(obj_1[2]/2 + i)][obj_1[1] - int(obj_1[3]/2 + j)] = 0
					
				self._out(map_wieght)
					
				
				
	
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