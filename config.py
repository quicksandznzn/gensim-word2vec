import os

pwd_path = os.path.abspath(os.path.dirname(__file__))


output_dir = os.path.join(pwd_path, 'output')
file_path = output_dir+ "/test.txt"
data_path = output_dir + "/test_split.txt"
crf_path = output_dir + "/crf/cws.txt"
model_path = output_dir + "/model/model"
model_txt_path = output_dir + "/model/model.txt"



hanlp_crf_class = "com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer"
