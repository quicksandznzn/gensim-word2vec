from gensim.models import Word2Vec
import numpy as np
from collections import Counter
from gensim.models.word2vec import Word2VecKeyedVectors
import config

model = Word2Vec.load(config.cbow_model_path)


def keywords(s):
    """
    提取关键词
    :param s:
    :return:
    """
    s = [w for w in s if w in model]
    ws = {w: sum([predict_proba(u, w) for u in s]) for w in s}
    return Counter(ws).most_common()


def relative_words(word,topN):
    """
    相关-互信息
    :param word:
    :return:
    """
    r = {i: predict_proba(i, word) - 0.9 * np.log(j.count) for i, j in model.wv.vocab.items()}
    return Counter(r).most_common(topN)


def predict_proba(oword, iword):
    """
    Skip-Gram + Huffman Softmax  gensim->Word2Vec->score_sg_pair
    :param oword:
    :param iword:
    :return:
    """
    # 获取输入词的词向量
    iword_vec = model[iword]
    # 获取保存权重的词的词库
    oword = model.wv.vocab[oword]
    oword_l = model.trainables.syn[oword.point].T
    dot = np.dot(iword_vec, oword_l)
    lprob = -sum(np.logaddexp(0, -dot) + oword.code * dot)
    return lprob

    # iword_vec = model[iword]
    # oword = model.wv.vocab[oword]
    # oword_l = model.trainables.syn1[oword.point].T
    # dot = np.dot(iword_vec, oword_l)
    # lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot)
    # return lprob


def infer():
    # this load func is too slow
    # model = Word2VecKeyedVectors.load_word2vec_format("/data1/services/word2vec/output/test/all.txt")

    # vector
    print(model.most_similar('北京', topn=20))
    # print(model.similarity('重庆', '青岛'))


if __name__ == '__main__':
    infer()
