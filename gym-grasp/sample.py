import gym
import gym_grasp # This includes GraspBlock-v0

gym.logger.set_level(40)

env = gym.make('GraspObject-v0')

env.reset()

# 0  : fftip
# 1  : mftip
# 2  : rftip
# 3  : lftip
# 4  : thtip
# 5  : ffmdl
# 6  : ffprx
# 7  : mfmdl
# 8  : mfprx
# 9  : rfmdl
# 10 : rfprx
# 11 : lfmdl
# 12 : lfprx
# 13 : thmdl
# 14 : thprx
# 15 : palm

while True:
    action = env.action_space.sample()
    obs, reward, done, _ = env.step(action)
    # print(env.sim.data.sensordata[-16:])

    env.render()
    if done:
        obs = env.reset()
