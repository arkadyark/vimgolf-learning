# vimgolf-learning

## What is this?
Vim is quite complicated. Complicated enough to be tackled with deep learning? Maybe.
[Vimgolf](http://vimgolf.com) serves as a pretty great data set to use to train a model. 
It's got a range of difficulties in the problems, and they're well formatted and easy to scrape.

## Setup
### Python setup
Run ```pip install -r requirements.txt```. I highly recommend creating a virtualenv first.

## TODOs
- Implement an LSTM encoder to convert the state (file state, output file, registers, vim mode, cursor position) to a fixed dimension
- Implement a decoder to output a character given the fixed dimension inputs
- Expand the set of possible keys to handle the problematic ones more (', ", \, ctrl+something)
- Fix the problem where the mode and cursor position aren't updating
- Find a way to run vim in the background a bit more smoothly, currently it blinks a lot at is somewhat unstable
