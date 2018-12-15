import re
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO
import pandas as pd
import os
from model import Model
from langdetect import detect

model = Model('english-partut-ud-2.0-170801.udpipe')


def create_df_from_conllu(conllu):
    conllu = re.sub('# .+?\n', '', conllu)
    l = conllu.split('\n')
    string = 'Id\tForm\tLemma\tUPosTag\tXPosTag\tFeats\tHead\tDepRel\tDeps\tMisc\n'
    string += "\n".join(l)
    TESTDATA = StringIO(string)
    df = pd.read_csv(TESTDATA, sep="\t")
    return df


def delete_from_df(df):
    to_drop = []
    for index, row in df.iterrows():
        if '-' in str(row['Id']):
            num = len(row['Id'].split('-'))
            for x in range(num):
                if num != 0:
                    to_drop.append(index + num)
                    num -= 1
    return to_drop


def parsing(text):
    sentences = model.tokenize(text)
    for s in sentences:
        model.tag(s)
        model.parse(s)
    conllu = model.write(sentences, "conllu")
    return conllu
    
    
def opening(text):
    if '\ufeff' in text:
        text = re.sub('\n', '\r\n', text)
    return text


def df_changing(text):
    conllu = parsing(text)
    df = create_df_from_conllu(conllu)
    to_drop = delete_from_df(df)
    df = df.drop(df.index[to_drop])
    return df

def start_end(df, text):
    starts = []
    ends = []
    end = 0
    for index, row in df.iterrows():
        form = row['Form']
        start = end + text.find(form)
        end = start + len(form)
        text = text[text.find(form)+len(form):]
        starts.append(start)
        ends.append(end)
    return starts, ends


def itog(text):
    text = opening(text)
    df = df_changing(text)
    starts, ends = start_end(df, text)
    df['START'] = starts
    df['END'] = ends
    return df