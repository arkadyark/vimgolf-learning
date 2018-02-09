Encoder-Decoder with Attention

Inputs:
- Current file contents
- Current cursor position (x, y) - (Int, Int)
- Current register contents (0-9, a, q, z, a few more)
- Current mode (Int)
- Output file contents

Outputs (RL way):
- One keypress at a time (ascii character, including \x00 through \x1F)

Architecture:
LSTM encoder on current file contents, output file contents, and each register's contents. 256-D embedding for the file contents, 16-D for each register
Concatenate them all together (256 + 256 + 16 * 15 + 2 + 1 = ~1000)
Multiply by the attention vector (also 1000-D) produced by the attention network
Input this into an LSTM and some fully-connected layers and a softmax layer on top, which is the decoded output (choice of 100 keypresses)
Repeat, up to 200 times, or if it successfully gets a right sequence sooner than that, at which point stop.
Cost is number of timesteps + replacement distance to the desired output - should push it to learn to get there, and as quickly as possible
