import os

pwd_path = os.path.abspath(os.path.dirname(__file__))


output_dir = os.path.join(pwd_path, 'output')
file_path = output_dir+ "/corpus/sougou/test.txt"
data_path = output_dir + "/corpus/sougou/test_split.txt"
crf_path = output_dir + "/crf/cws.txt"
model_path = output_dir + "/model/model"
model_txt_path = output_dir + "/model/model.txt"

# https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
wiki_path = output_dir + "/corpus/wiki/zhwiki-latest-pages-articles.xml.bz2"
wiki_txt_path = output_dir + "/corpus/wiki/wiki.zn.txt"

string_reg = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）“”‘’》《；＃】【〗＜＝┨〉．：]+"


hanlp_crf_class = "com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer"
