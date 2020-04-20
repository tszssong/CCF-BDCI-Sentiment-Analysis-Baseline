import os, sys, argparse
import numpy as np
import pandas as pd
import random
from tqdm import tqdm
label_dict = {'caijing':0, 'fangchan':1, 'fazhi':2, 'gongyi':3,
              'keji':4, 'lvyou':5, 'qiche':6, 'shehui':7, 'shizheng':8,
              'tiyu':9, 'wenhua':10, 'yule':11, 'jiaoyu':12}
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-root', type=str, default='zhh/Txts/')
    parser.add_argument('--lst', type=str, default='../lst')
    parser.add_argument('--max-len', type=int, default=500)
    parser.add_argument('--ratio', type=float, default=0.8)
    args = parser.parse_args()
    filelists = os.path.join(args.data_root, args.lst)
    print("gen train/val with maxLen=%d, ratio=%.2f"%(args.max_len, args.ratio))
    train_pd = pd.DataFrame(columns=('id','title', 'content', 'label'))
    dev_pd = pd.DataFrame(columns=('id','title', 'content', 'label'))
    with open(filelists, 'r') as fr:
        lines = fr.readlines()
        for line in lines:
            name = line.strip()
            label = name.split('_')[1]
            rfile = os.path.join(args.data_root, name)
            with open(rfile, 'r') as fr:
                txt_lines = fr.readlines()
                txt_len = len(txt_lines)
                len_train = min( int( args.ratio*len(txt_lines) ), int(args.max_len*args.ratio) )
                len_val = min( int( (1-args.ratio)*len(txt_lines) ), int((1-args.ratio)*args.max_len) )
                print("%s: len: %d, sep train/val:%d/%d"%(name, txt_len, len_train, len_val))
                for idx, texts in enumerate(txt_lines):
                    if idx > args.max_len : break
                    texts = texts.replace(',','，')
                    url, title, content = texts.strip().split('\t')
                    if idx< len_train:
                        train_pd = train_pd.append([{'id':url, 'title':title, 
                                                 'content':content,
                                                 'label':label_dict[label]}])
                    else:
                        dev_pd = dev_pd.append([{'id':url, 'title':title, 
                                                 'content':content,
                                                 'label':label_dict[label]}])
    train_pd.to_csv("train.csv")
    dev_pd.to_csv("dev.csv")