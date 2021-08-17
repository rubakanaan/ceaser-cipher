from ceaser_cipher.ceaser_cipher import encrypt, decrypt,crack


def test_encrypt():
    actual=encrypt("Hello world",5)
    expected="mjqqt btwqi"
    assert actual == expected
    
def test_decrypt():
    actual=decrypt("mjqqt btwqi",5)
    expected="hello world"
    assert actual == expected
    
def test_encrypt_upper_case():
    actual=encrypt("HELLO WORLD",5)
    expected="mjqqt btwqi"
    assert actual == expected
    
def test_encrypt_lower_case():
    actual=encrypt("hello world",5)
    expected="mjqqt btwqi"
    assert actual == expected
    
def test_encrypt_non_alpha():
    actual=encrypt("hello world!",5)
    expected="mjqqt btwqi!"
    assert actual == expected
    
def test_crack():
    actual = crack('xi lph iwt qthi du ixbth, xi lph iwt ldghi du ixbth.')
    expected='it was the best of times, it was the worst of times.'
    assert actual == expected