import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from utils.string_utils import is_valid_email, capitalize_words

def test_is_valid_email():
    assert is_valid_email('test@example.com') == True
    assert is_valid_email('invalid email') == False

def test_capitalize_words():
    assert capitalize_words('hello world') == 'Hello World'

def test_user_email_is_valid(sample_use):
    assert is_valid_email(sample_use['email']) == True