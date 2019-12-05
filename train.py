from gensim.models import Word2Vec
import config
import time
from gensim.models.word2vec import LineSentence, PathLineSentences
from gensim.models.callbacks import CallbackAny2Vec
from multiprocessing import cpu_count
import argparse


class callback(CallbackAny2Vec):
    def __init__(self):
        self.epoch = 0

    def on_epoch_end(self, model):
        loss = model.get_latest_training_loss()
        print('Loss after epoch {} {}: {}'.format(time.strftime('%Y-%m-%d %H:%M:%S %p'), self.epoch, loss))
        self.epoch += 1


def train(sg):
    start_time = time.time()
    # sentences = word2vec.PathLineSentences(segment_dir)

    if sg == 0:
        train_model = Word2Vec(LineSentence(config.data_path), sg=0, workers=cpu_count(), iter=10, compute_loss=True,
                               callbacks=[callback()])
    else:
        #
        train_model = Word2Vec(LineSentence(config.data_path), sg=1, hs=1, workers=cpu_count(), iter=5,
                               compute_loss=True, callbacks=[callback()])

    if sg == 0:
        model_path = config.cbow_model_path
        # model_txt_path = config.cbow_model_path
    else:
        model_path = config.skip_model_path
        # model_txt_path = config.skip_model_path

    train_model.callbacks = {}
    train_model.save(model_path)
    # train_model.wv.save_word2vec_format(model_txt_path, binary=False)
    end_time = time.time()
    print("train done", (end_time - start_time))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    # 0 skip 1 cbow
    parser.add_argument('--sg', type=str, default=0)
    args = parser.parse_args()
    train(args.sg)
