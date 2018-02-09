from gym.envs.registration import register

register(
    id='vim-v0',
    entry_point='gym_vim.envs:VimEnv',
)
