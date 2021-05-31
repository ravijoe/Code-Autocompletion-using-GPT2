# !pip install git+https://github.com/huggingface/transformers
#source:- https://www.youtube.com/watch?v=vG-z-Y_Sfrw
from transformers import GPT2Config,GPT2LMHeadModel,GPT2Tokenizer
from pprint import pprint
from functools import lru_cache
# @lru_cache()
tokenizer=GPT2Tokenizer.from_pretrained("GPyT_1/GPyT_TOK_75GB")
tokenizer.add_special_tokens({
    'eos_token':'</s>',
    'bos_token':'<s>',
    'unk_token':"<unk>",
    'pad_token':"<pad>",
    'mask_token':"<mask>"
})
model = GPT2LMHeadModel.from_pretrained('GPyT_1/latest_model')

NEWLINECHAR='<N>'
def encode_newlines(inp):
    return inp.replace("\n",NEWLINECHAR)

def decode_newlines(inp):
    return inp.replace(NEWLINECHAR,"\n").replace('<pad>','')

print("all models loaded")

def get_output(inp):
    inp=encode_newlines(inp)
    newline_count=inp.count(NEWLINECHAR)
    inputs_ids=tokenizer.encode(inp,return_tensors='pt')
    model_output=model.generate(
        inputs_ids,
        max_length=100,
        num_beams=3,
        temperature=0.7,
        no_repeat_ngram_size=5,
        num_return_sequences=3,
        return_dict_in_generate=True,
        output_scores=True
    )
    sequence=model_output['sequences'][0]
    decoded=decode_newlines(tokenizer.decode(sequence))
    print(20*'-')
    # print(decoded)
    print(20*'-')
    print()
    print()
    autocomplete=''
    split=decoded.split('\n')
    # print(split)
    for s in split[:newline_count+1]:
        autocomplete+=s+'\n'
    return decoded
    # for out in model_output['sequences']:
    #     print(decode_newlines(tokenizer.decode(out)))
# print(get_output('import torch'))