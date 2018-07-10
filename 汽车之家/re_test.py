import re

string = '<a href="http://www.汽车之家.com/link?url=CJS85CU2eYiyEaaSqNkiC3YUZ3qcqr4t1cM_ve5SVTNFMVKgeVurHAg8dptbs72fN1nsjzWj3oLmwhf2b4mIbPHKfobomxJuxbGkDuG4o0u6bYp95SzYqThjYMvEAPni522S7XwK_Dd0VLvouupQsz71dvOdKNL8mzQiGm09_sMcnqpOCLdYjukfwSyjRehRtQ647FLcU2eJyMD6MRlyCPBlPxzpbMV3LVhWWf8nr5i" target="_blank"><em>中国</em>_百度百科</a>'
# 构建一个正则对象
pattern = re.compile('href.*link')
# 使用分组也就是小括号，就会只返回小括号里的匹配项
pattern1 = re.compile('href="(.*?)"')

# result = re.findall(pattern1, string)
# print(result)pattern1

result2 = re.sub(pattern1, 'href="abc"',string)
print(result2)
