from gensim.corpora import WikiCorpus

import config

def process(inp, outp):
    """
    处理wiki dump 中文语料2019-11-30下载
    :param inp:input path
    :param outp:output path
    :return:
    """
    i = 0
    output = open(outp, 'w')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(' '.join(text) + "\n")
        i += 1
        if i % 10000 == 0:
            print("saved " + str(i) + " articles")
    print('done')

def decode_text(text):
    words = []
    for w in text:
        words.append(w.decode('utf-8'))
    return words

if __name__ == '__main__':
    process(config.wiki_path, config.wiki_txt_path)
