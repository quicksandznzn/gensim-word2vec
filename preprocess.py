from pyhanlp import *
import config
import datetime


def parse_file(file_path):
    start_time = datetime.datetime.now()
    CRFLexicalAnalyzer = JClass(config.hanlp_crf_class)
    # if you don't crf model remove  config.crf_path
    analyzer = CRFLexicalAnalyzer(config.crf_path)
    data_list = []

    with open(file_path, 'r', encoding='utf-8') as input_f:
        for line in input_f:
            sb = ""
            for term in analyzer.seg(line):
                sb += (term.word + ' ')
            sb = sb.translate(str.maketrans('', '', "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）“”‘’》《；＃】【〗＜＝┨〉．：]+"))
            print(sb)
            data_list.append(sb)
    end_time = datetime.datetime.now()
    print("save done", (start_time - end_time).seconds)
    return data_list;


def save_data(data_path, data_list):
    start_time = datetime.datetime.now()
    with open(data_path, 'w', encoding='utf-8') as f:
        for data in data_list:
            f.write(data + " ")
    end_time = datetime.datetime.now()
    print("save done", (start_time - end_time).seconds)


if __name__ == '__main__':
    data_list = parse_file(config.file_path)
    save_data(config.data_path, data_list)
