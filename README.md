# word2vec


1. use python3<br>
   pip3 install pyhanlp<br>
   pip3 install gensim<br>
   
2. download wiki dump https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2 put /output/corpus/wiki

3. python3 process_wiki.py

4. opencc -c t2s.json -i ./output/corpus/wiki/wiki.zn.txt -o ./output/corpus/wiki/wiki.zn.t2s.txt

5. iconv -c -t UTF-8 < ./output/corpus/wiki/wiki.zn.t2s.txt > ./output/corpus/wiki/wiki.zn.t2s.utf8.txt

6. hanlp segment  --config /usr/local/lib/python3.6/site-packages/pyhanlp/static/hanlp.properties   < wiki.zn.t2s.utf8.txt > wiki.zn.t2s.utf8.split.txt

7. args:sg 0=cbow 1=skip default=0<br>
   python3 train.py<br>

8. python3 infer.py




