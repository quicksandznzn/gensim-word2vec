from gensim.models import Word2Vec
import config
import time
from gensim.models.word2vec import LineSentence, PathLineSentences


def train(data_path, model_path, model_txt_path):
    start_time = start_time = time.time()
    # sentences = word2vec.PathLineSentences(segment_dir)
    sentences = LineSentence(data_path)
    train_model = Word2Vec(sentences, size=100, window=5, min_count=1, workers=8)
    train_model.save(model_path)
    train_model.wv.save_word2vec_format(model_txt_path, binary=False)
    end_time = start_time = time.time()
    print("train done", (start_time - end_time))


if __name__ == '__main__':
    train(config.data_path, config.model_path, config.model_txt_path)
