class Head:
    def __init__(self):
        self.brain = "Brain"

class Hand:
    def __init__(self):
        self.fingers = 5

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Torso:
    def __init__(self, head, right_arm, left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm

class Leg:
    def __init__(self, foot):
        self.foot = foot

class Foot:
    def __init__(self):
        self.toes = 5

class Human:
    def __init__(self, name):
        self.name = name
        self.head = Head()
        self.right_hand = Hand()
        self.left_hand = Hand()
        self.right_arm = Arm(self.right_hand)
        self.left_arm = Arm(self.left_hand)
        self.torso = Torso(self.head, self.right_arm, self.left_arm)
        self.right_foot = Foot()
        self.left_foot = Foot()
        self.right_leg = Leg(self.right_foot)
        self.left_leg = Leg(self.left_foot)
    
    def descriprion(self):
        print(f"Nombre del humano: {self.name}")
        print(f"La cabeza contiene: {self.head.brain}")
        print(f"La mano derecha tiene {self.right_hand.fingers} dedos")
        print(f"La mano izquierda tiene {self.left_hand.fingers} dedos")
        print(f"El pie derecho tiene {self.right_foot.toes} dedos")
        print(f"El pie izquierdo tiene {self.left_foot.toes} dedos")

person = Human('Anthony')
person.descriprion()