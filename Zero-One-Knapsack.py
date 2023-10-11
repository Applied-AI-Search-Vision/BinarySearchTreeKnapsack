import math
import time

toggle=False
insertion = 1

class Node:
    max_reward=0 
    max_capacity=0
    
    def __init__(self, weight, reward):
        global toggle
        self.left = None
        self.right = None
        self.weight = weight
        self.reward = reward
        self.included = toggle
        self.total_reward = 0
        self.total_weight = 0
        toggle = not toggle


    def insert(temporary_node, w, p): 
        q = []
        q.append(temporary_node)
        while (len(q)): 
            temporary_node = q.pop(0) 

            if not temporary_node.left: 
                temporary_node.left = Node(w, p)
                if(temporary_node.left.included):
                    temporary_node.left.total_reward = temporary_node.total_reward + temporary_node.left.reward
                    temporary_node.left.total_weight = temporary_node.total_weight + temporary_node.left.weight
                else:
                    temporary_node.left.total_reward = temporary_node.total_reward
                    temporary_node.left.total_weight = temporary_node.total_weight 
                break
            else:
                q.append(temporary_node.left)

            if (not temporary_node.right):
                temporary_node.right = Node(w, p)
                if(temporary_node.right.included):
                    temporary_node.right.total_reward = temporary_node.total_reward + temporary_node.right.reward
                    temporary_node.right.total_weight = temporary_node.total_weight + temporary_node.right.weight
                else:
                    temporary_node.right.total_reward = temporary_node.total_reward
                    temporary_node.right.total_weight = temporary_node.total_weight
                break
            else:
                q.append(temporary_node.right)

    def bfs(self, root, capacity):
        queue = [root]
        print(queue[0])
        max_reward = 0
        max_capacity = 0 
        while len(queue) > 0:
            cur_node = queue.pop(0)
            if cur_node.total_weight <= capacity and max_reward < cur_node.total_reward:
                max_reward = cur_node.total_reward
                max_capacity = cur_node.total_weight
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        print("USING BFS THE TOTAL reward AND WEIGHT ARE: " + str(max_reward) + " " + str(max_capacity))

    def dfs(self, root, capacity):
        if root:
            root.dfs(root.left, capacity)
            if(root.total_weight <= capacity and Node.max_reward < root.total_reward):
                Node.max_reward = root.total_reward
                Node.max_capacity = root.total_weight
            root.dfs(root.right, capacity)

rewards = [20, 40, 50, 36, 26, 64, 54, 18, 46, 28, 25]
weights = [15, 32, 60, 80, 43, 120, 77, 6, 93, 35, 37]
capacity = 420


root = Node(0, 0)
i = 0
while(i != (len(rewards))):
    for j in range(0, int(math.pow(2, insertion))):
        root.insert(weights[i], rewards[i])
    i += 1
    insertion += 1

second1 = time.time()
root.bfs(root=root, capacity=capacity)
second2 = time.time()
print("Time to execute BFS is ",second2-second1," secs")

Node.max_capacity=0
Node.max_reward=0
second1=time.time()
root.dfs(root,capacity)
print()
print("USING DFS THE TOTAL reward AND WEIGHT ARE: "+str(Node.max_reward) + " "+str(Node.max_capacity))
second2=time.time()
print("Time to execute DFS is ",second2-second1," secs")