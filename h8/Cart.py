import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)
steps = 0

def policy(observation):
    a, w = observation[2], observation[3]
    if abs(a) < 0.03: 
        return 0 if w < 0 else 1  
    else:
        return 0 if a < 0 else 1  

for _ in range(10000):  
    env.render()
    action = policy(observation)
    observation, reward, terminated, truncated, info = env.step(action)
    steps += 1
    if terminated or truncated:
        observation, info = env.reset()
        print('steps:', steps)
        steps = 0

env.close()
