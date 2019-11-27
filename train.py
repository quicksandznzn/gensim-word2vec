
from gensim.models import Word2Vec
import config
import datetime
from gensim.models.word2vec import LineSentence,PathLineSentences

def train(data_path,model_path,model_txt_path):
    start_time = datetime.datetime.now()
    # sentences=[]
    # with open(data_path, 'r', encoding='utf-8') as input_f:
    #     for line in input_f:
    #         sentences.append(line)
    # sentences = word2vec.PathLineSentences(segment_dir)
    sentences = LineSentence(data_path)
    train_model = Word2Vec(sentences, size=100, window=5, min_count=1, workers=8)
    train_model.save(model_path)
    train_model.wv.save_word2vec_format(model_txt_path, binary=False)
    end_time = datetime.datetime.now()
    print("train done",(start_time - end_time).seconds)

if __name__ == '__main__':
    train(config.data_path,config.model_path,config.model_txt_path)

