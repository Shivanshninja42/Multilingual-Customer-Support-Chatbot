import openai
import os
from transformers import GPT2Tokenizer

openai.api_key = os.environ.get("")

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

with open("pto/pto.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = text.split('\n\n')
ntokens = [len(tokenizer.encode(chunk)) for chunk in chunks]

def split_into_subchunks(chunk, max_tokens=1000):
    subchunks = [chunk[i:i + max_tokens] for i in range(0, len(chunk), max_tokens)]
    return subchunks

def group_chunks(chunks, ntokens, max_len=1000, hard_max_len=3000):
    batches = []
    
    for chunk, ntoken in zip(chunks, ntokens):
        if ntoken > hard_max_len:
            print(f"Warning: Chunk discarded for being too long ({ntoken} tokens > {hard_max_len} token limit). Preview: '{chunk[:50]}...'")
            continue

        if ntoken > max_len:
            subchunks = split_into_subchunks(chunk, max_tokens=max_len)
            batches.extend(subchunks)
        else:
            batches.append(chunk)
            
    return batches

chunks = group_chunks(chunks, ntokens)
len(chunks)

def translate_chunk(chunk, model='gpt-3.5-turbo', dest_language='English', sample_translation=("Sample source text", "Sample translated text")):
    prompt = f'''Translate only the text from the following LaTeX document into {dest_language}. Leave all LaTeX commands unchanged

"""
{sample_translation[0]}
{chunk}"""

{sample_translation[1]}
'''
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0,
        top_p=1,
        max_tokens=1500,
    )
    result = response['choices'][0]['text'].strip()
    result = result.replace('"""', '')
    return result

index_to_translate = 5000

if 0 <= index_to_translate < len(chunks):
    translated_text = translate_chunk(chunks[index_to_translate], model='gpt-3.5-turbo', dest_language='English')
    print(translated_text)
else:
    print("Index out of range: Chunks list doesn't have enough elements.")
