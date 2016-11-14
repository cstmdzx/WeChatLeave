import re

pattern = re.compile(u'\u56e0([\u4e00-\u9fa5]+)\u8bf7\u5047([0-9]\.[0-9]([\u4e00-\u9fa5]+))')
strLeave = u'\u5404\u4f4d\u8001\u5e08\u540c\u5b66\uff0c\u9a6c\u96ea\u6674\u56e0\u79c1\u8bf7\u50471.5\u5c0f\u65f6\uff0c\u8c22\u8c22'
match = pattern.search(strLeave)
if match:
    print(match.group(2))
