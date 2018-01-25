class Parameters():
    # general parameters
    latent_size = 150
    num_epochs = 20
    learning_rate = 0.001
    batch_size = 30
    # for decoding
    temperature = 1.0
    #gen_length = 20
    # if greedy, choose word with the highest prob;
    # if sample, sample from multinullli distribution
    sample_gen = 'greedy' # 'greedy', 'sample', 'beam_search'
    # beam search
    #beam_search = True
    #beam_size = 3
    # encoder
    encoder_rnn_layers = 1
    encoder_hidden = 191
    keep_rate = 1.0
    # decoder
    decoder_hidden = 191
    decoder_rnn_layers = 1
    dec_keep_rate = 1.0
    embed_size = 353
    gen_max_len = 300
    gen_z_samples = 20 # according to paper (Diverse cap)
    ann_param = 1
    dec_lstm_drop = 1.0
    optimizer = 'SGD'
    # restore?
    restore = False
    # technical parameters
    LOG_DIR = './model_logs/'
    no_encoder = False
    vocab_size = 0 # need to be set during data load
    coco_dir = "/home/luoyy16/datasets-large/mscoco/coco/"
    gen_name = "00"
    checkpoint = "last_run"
    num_epochs_per_decay = 5
    cluster_vectors = False
    def parse_args(self):
        import argparse
        import os
        parser = argparse.ArgumentParser(description="Specify some parameters, "
                                         "all parameters also can be "
                                         "directly specify in the "
                                         "Parameters class")
        parser.add_argument('--lr', default=self.learning_rate,
                            help='learning rate', dest='lr')
        parser.add_argument('--embed_dim', default=self.embed_size,
                            help='embedding size', dest='embed')
        parser.add_argument('--enc_hid', default=self.encoder_hidden,
                            help='encoder state size', dest='enc_hid')
        parser.add_argument('--dec_hid', default=self.decoder_hidden,
                            help='decoder state size', dest='dec_hid')
        parser.add_argument('--latent', default=self.latent_size,
                            help='latent space size', dest='latent')
        parser.add_argument('--restore', help='whether restore',
                            action="store_true")
        parser.add_argument('--gpu', help="specify GPU number")
        parser.add_argument('--coco_dir', default=self.coco_dir,
                            help="mscoco directory")
        parser.add_argument('--epochs', default=self.num_epochs,
                            help="number of training epochs")
        parser.add_argument('--no_encoder',
                            help="use this if want to run baseline lstm",
                            action="store_true")
        parser.add_argument('--temperature', default=self.temperature,
                            help="set temperature parameter for generation")
        parser.add_argument('--gen_name', default=self.gen_name,
                            help="prefix of generated json nam")
        parser.add_argument('--dec_drop', default=self.keep_rate,
                            help="decoder caption dropout")
        parser.add_argument('--gen_z_samples', default=self.gen_z_samples,
                            help="#z samples")
        parser.add_argument('--ann_param', default=self.ann_param,
                            help="annealing speed, more slower")
        parser.add_argument('--dec_lstm_drop', default=self.dec_lstm_drop,
                            help="decoder lstm dropout")
        parser.add_argument('--sample_gen', default=self.sample_gen,
                            help="'greedy', 'sample', 'beam_search'")
        parser.add_argument('--checkpoint', default=self.checkpoint,
                            help="specify checkpoint name, default=last_run")
        parser.add_argument('--optimizer', default=self.optimizer,
                            choices=['SGD', 'Adam'], help="SGD or Adam")
        # parser.add_argument('--c_v', default=False,
        #                     help="Whether to use cluster vectors",
        #                     action="store_true")

        args = parser.parse_args()
        self.learning_rate = float(args.lr)
        self.embed_size = int(args.embed)
        self.encoder_hidden = int(args.enc_hid)
        self.decoder_hidden = int(args.dec_hid)
        self.latent_size = int(args.latent)
        self.restore = args.restore
        self.coco_dir = args.coco_dir
        self.num_epochs = int(args.epochs)
        self.no_encoder = args.no_encoder
        self.temperature = float(args.temperature)
        self.gen_name = args.gen_name
        self.dec_keep_rate = float(args.dec_drop)
        self.gen_z_samples = int(args.gen_z_samples)
        self.ann_param = float(args.ann_param)
        self.dec_lstm_drop = float(args.dec_lstm_drop)
        self.sample_gen = args.sample_gen
        self.checkpoint = args.checkpoint
        self.optimizer = args.optimizer
        # self.cluster_vectors = args.c_v
        # CUDA settings
        os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"]=args.gpu
