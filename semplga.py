import ga

engine = ga.GA(items_cnt=1)
# размеры картинок
objs = [[60,30],
        [50,70],
        [30,20],
        [40,20],
        [30,20],
        [20,40]
        ]
engine.initialisation(objs)