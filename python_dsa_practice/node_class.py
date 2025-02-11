class Node: 
    def __init__(self, value, neighbours = []):
        self.value = value
        self.neighbours = neighbours
        
    def __str__(self):
        return f"Node({self.value})"
    
    def display(self):
        connections = [node.value for node in self.neighbours]
        return f"{self.value} is connected to: {connections}"