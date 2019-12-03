from gensim.models import Word2Vec
import config
import time
from gensim.models.word2vec import LineSentence, PathLineSentences
from gensim.models.callbacks import CallbackAny2Vec
from multiprocessing import cpu_count


class callback(CallbackAny2Vec):
    def __init__(self):
        self.epoch = 0

    def on_epoch_end(self, model):
        loss = model.get_latest_training_loss()
        print('Loss after epoch {} {}: {}'.format(time.strftime('%Y-%m-%d %H:%M:%S %p'), self.epoch, loss))
        self.epoch += 1


def train(data_path, model_path, model_txt_path):
    start_time = time.time()
    # sentences = word2vec.PathLineSentences(segment_dir)
    # train_model = Word2Vec(LineSentence(data_path), sg=1, window=10, workers=cpu_count(), iter=20, compute_loss=True,
    #                       callbacks=[callback()])
    train_model = Word2Vec(LineSentence(data_path), workers=cpu_count(), iter=20, compute_loss=True, callbacks=[callback()])
    train_model.callbacks = {}
    train_model.save(model_path)
    train_model.wv.save_word2vec_format(model_txt_path, binary=False)
    end_time = time.time()
    print("train done", (end_time - start_time))


if __name__ == '__main__':
    train(config.data_path, config.model_path, config.model_txt_path)
