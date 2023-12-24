def test_consecutive_letters():
    """测试用户输入的内容是否为连续的三个字母
    如果有就把他们匹配出来，没有不做处理"""
    lists = [chr(letter).lower() for letter in range(65, 91)]
    file = input('请输入你的内容')
    for i in range(len(file) - 2):
        if file[i:i+3:]:
            index_num = lists.index(file[i:i+3:][0])
            if file[i:i+3:] == "".join(lists[index_num: index_num+3]):
                print('连续的字母:%s' % file[i:i+3:])


test_consecutive_letters()