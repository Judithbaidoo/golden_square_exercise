import pytest 
from lib.password_checker import *

def test_password_checker():
    password_manager = PasswordChecker()
    result = password_manager.check("12345678")
    assert result == True

def test_error_checker():
    password_manager = PasswordChecker()
    with pytest.raises(Exception) as e :
        password_manager.check("123")
    error = str(e.value)
    assert error == "Invalid password, must be 8+ characters."