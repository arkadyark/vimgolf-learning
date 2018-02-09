import tensorflow as tf
import params
import constants

input_encoder_cell = tf.nn.rnn_cell.BasicLSTMCell(params.INPUT_ENCODER_NUM_UNITS)
output_encoder_cell = tf.nn.rnn_cell.BasicLSTMCell(params.OUTPUT_ENCODER_NUM_UNITS)
register_cells = [tf.nn.rnn_cell.BasicLSTMCell(params.REGISTER_ENCODER_NUM_UNITS) for i in range(constants.NUM_REGISTERS)]
