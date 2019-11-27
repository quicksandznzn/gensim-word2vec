from pyhanlp import *
import config
import time


def parse_file(file_path):
    start_time = time.time()
    CRFLexicalAnalyzer = JClass(config.hanlp_crf_class)
    # if you don't crf model(see https://github.com/hankcs/HanLP) remove  config.crf_path
    analyzer = CRFLexicalAnalyzer(config.crf_path)
    data_list = []
    with open(file_path, 'r', encoding='utf-8') as input_f:
        for line in input_f:
            sb = ""
            for term in analyzer.seg(line):
                sb += (term.word + ' ')
            sb = sb.translate(str.maketrans('', '', config.string_reg))
            data_list.append(sb)
    end_time = time.time()
    print("save done", (start_time - end_time))
    return data_list;


def save_data(data_path, data_list):
    start_time = time.time()
    with open(data_path, 'w', encoding='utf-8') as f:
        for data in data_list:
            f.write(data + " ")
    end_time = time.time()
    print("save done", (start_time - end_time))


if __name__ == '__main__':
    data_list = parse_file(config.file_path)
    save_data(config.data_path, data_list)
