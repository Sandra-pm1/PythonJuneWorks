# check the given word is anagram(same charater and count) or not

source_word="listen"

target_word="silent"


srt_source_word=sorted(source_word)

srt_target_word=sorted(target_word)

print(srt_source_word==srt_target_word)      