from gensim.models import Word2Vec
from gensim.models.word2vec import Word2VecKeyedVectors
import config



def infer(model_path):
    # this load func is too slow
    # model = Word2VecKeyedVectors.load_word2vec_format("/data1/services/word2vec/output/test/all.txt")
    model = Word2Vec.load(model_path)
    # vector
    # print(model['北京'])
    print(model.most_similar('北京', topn=20))
    print(model.similarity('重庆市', '青岛市'))


if __name__ == '__main__':
    infer(config.model_path)
