import ga

engine = ga.GA(items_cnt=1)
# размеры картинок
objs = [[100,100],
        [50,90],
        [102,200],
        [60,100],
        [100,120],
        [120,102]
        ]
engine.initialisation(objs)