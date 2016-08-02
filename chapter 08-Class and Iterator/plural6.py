import re

def build_match_and_apply_functions(pattern, search, replace):

    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)


class LazyRules:
    # LazyRules 类的所有实例共享 rules_filename 变量
    rules_filename = 'plural6-rules.txt'

    def __init__(self):
        # 打开模式文件
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        # 初始化缓存
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        # self.cache_index 记录我们下一步返回的缓存条目???
        self.cache_index += 1
        if (len(self.cache) >= self.cache_index):
            # 可以从缓存中返回匹配和应用功能而不是从无到有创建
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()

        if not line:
            slef.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(pattern, search, replace)

        self.cache.append(funcs)
        return funcs

rules = LazyRules()
