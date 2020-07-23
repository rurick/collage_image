import ga

engine = ga.GA(items_cnt=1)
# размеры картинок
objs = [[10,10],
        [5,9],
        [12,20],
        [6,10],
        [10,12],
        [12,12]
        ]
engine.initialisation(objs)