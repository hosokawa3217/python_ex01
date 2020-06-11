import ex01;

@mark.parametrize('ans', [
    "大吉です。最高♪♪♪",
    "中吉です。ラッキー♪",
    "小吉です。コツコツと…",
    "末吉です。焦らずに",
    "凶です。気をつけて！"
])
def test_ex01():
    assert ex01.uranai() == ans
    
    
