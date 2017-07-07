# coding: utf-8
import random

import numpy as np
import matplotlib.pyplot as plt


# PSO参数设置
class PSO():
    def __init__(self, pN, dim, max_iter):
        # w代表惯性权值
        self.w = 0.8
        # c1和c2表示学习参数
        self.c1 = 2
        self.c2 = 2
        # r1 和 r2代表随机值
        self.r1 = 0.6
        self.r2 = 0.3
        # 粒子数量
        self.pN = pN
        # 搜索维度
        self.dim = dim
        # 迭代次数
        self.max_iter = max_iter
        # 所有粒子的位置和速度
        self.X = np.zeros((self.pN, self.dim))
        self.V = np.zeros((self.pN, self.dim))
        # 个体经历的最佳位置和全局最佳位置
        self.pbest = np.zeros((self.pN, self.dim))
        self.gbest = np.zeros((1, self.dim))
        # 每个个体的历史最佳适应值
        self.p_fit = np.zeros(self.pN)
        # 全局最佳适应值
        self.fit = 1e10

    # 目标函数Sphere函数
    def function(self, x):
        sum = 0
        length = len(x)
        x = x ** 2
        for i in range(length):
            sum += x[i]
        return sum

    # 初始化种群
    def init_Population(self):
        for i in range(self.pN):
            for j in range(self.dim):
                self.X[i][j] = random.uniform(0, 1)
                self.V[i][j] = random.uniform(0, 1)
            self.pbest[i] = self.X[i]
            tmp = self.function(self.X[i])
            self.p_fit[i] = tmp
            if (tmp < self.fit):
                self.fit = tmp
                self.gbest = self.X[i]

    # 更新粒子位置
    def iterator(self):
        fitness = []
        for t in range(self.max_iter):
            # 更新gbest\pbest
            for i in range(self.pN):  
                temp = self.function(self.X[i])
                # 更新个体最优
                if (temp < self.p_fit[i]):  
                    self.p_fit[i] = temp
                    self.pbest[i] = self.X[i]
                    # 更新全局最优
                    if (self.p_fit[i] < self.fit):  
                        self.gbest = self.X[i]
                        self.fit = self.p_fit[i]
            for i in range(self.pN):
                self.V[i] = self.w * self.V[i] + self.c1 * self.r1 * (self.pbest[i] - self.X[i]) \
                            + self.c2 * self.r2 * (self.gbest - self.X[i])
                self.X[i] = self.X[i] + self.V[i]
            fitness.append(self.fit)
            # 输出最优值
            # print(self.fit)
        return fitness


# 程序执行
my_pso = PSO(pN=30, dim=5, max_iter=100)
my_pso.init_Population()
fitness = my_pso.iterator()
# 画图
plt.figure(1)
plt.title("Figure1")
plt.xlabel("iterators", size=14)
plt.ylabel("fitness", size=14)
t = np.array([t for t in range(0, 100)])
fitness = np.array(fitness)
print(fitness)
plt.plot(t, fitness, color='b', linewidth=3)
plt.show()
