import random

class SimpleAIAgent:
    def __init__(self, actions):
        self.actions = actions

    def choose_action(self, state=None):
        # For simplicity, choose a random action
        return random.choice(self.actions)

if __name__ == "__main__":
    actions = ['move_left', 'move_right', 'move_up', 'move_down']
    agent = SimpleAIAgent(actions)
    for step in range(5):
        action = agent.choose_action()
        print(f"Step {step+1}: Agent chooses to {action}")