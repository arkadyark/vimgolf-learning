from environment.vim_env import VimEnv

if __name__ == '__main__':
    env = VimEnv()
    done = True

    i = 0
    while True:
        print(i)
        if done:
            i = 0
            obs = env.reset()
        env.render()
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        i += 1
