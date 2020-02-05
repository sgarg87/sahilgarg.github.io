class Config(object):
    # 6 in Transformer Paper
    N = 1
    # 512 in Transformer Paper
    d_model = 256
    # 2048 in Transformer Paper
    d_ff = 512
    h = 8
    dropout = 0.1
    output_size = 4
    lr = 0.0003
    max_epochs = 35
    batch_size = 128
    max_sen_len = 60
