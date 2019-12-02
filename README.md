# word2vec

**this project use hanlp crf segment corpus use gensim word2vec train**

1. use python3<br>
   pip3 install pyhanlp<br>
   pip3 install gensim<br>
   
2. download wiki dump https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2

3. python3 process_wiki.py

4. opencc -c t2s.json -i inputPath/wiki.zn.txt -o outputPath/wiki.zn.t2s.txt

5. iconv -c -t UTF-8 < wiki.zn.t2s.txt > wiki.zn.t2s.utf8.txt

6. hanlp segment  --config HaNLPDataPath/hanlp.properties   < wiki.zn.t2s.utf8.txt > wiki.zn.t2s.utf8.split.txt

7. python3 train.py

8. python3 infer.py




