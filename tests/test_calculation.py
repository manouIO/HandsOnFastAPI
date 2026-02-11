import pytest
from app.calculations import add, BankAccount, InsufficientFundsError

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (5, 3, 8),
    (4, 4, 8),
    (0, 0, 0)])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected #this is one way to test multiple cases for the add function using pytest's parametrize decorator, which allows us to run the same test with different inputs and expected outputs.


# @pytest.mark.parametrize("num1, num2, expected", [
#     (2, 3, 6),
#     (5, 3, 12),
#     (4, 4, 18),
#     (0, 0, 0)])
# def test_multiplication(num1, num2, expected):
#     print("Testing multiplication function...")
#     assert num1 * num2 == expected #this is one way to test multiple cases for the multiplication function using pytest's parametrize decorator, which allows us to run the same test with different inputs and expected outputs.



#fixtures are a way to set up some data or state before running a test.
@pytest.fixture
def zero_bank_account():
    print("Creating a bank account with zero balance...")
    return BankAccount() #this will create a new bank account with a default balance of 0 before each test that uses this fixture.

@pytest.fixture
def bank_account(): 
    return BankAccount(100) #this will create a new bank account with a balance of 100 before each test that uses this fixture.


def test_bank_set_initial_balance(bank_account):
    assert bank_account.balance == 100

def test_bank_default_initial_balance(zero_bank_account):
    assert zero_bank_account.balance == 0 

def test_bank_deposit(zero_bank_account):
    zero_bank_account.deposit(50)
    assert zero_bank_account.balance == 50    

def test_bank_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest() 
    assert round(bank_account.balance ,6)== 110 #we round to 6 decimal places to avoid floating point precision issues



def test_bank_withdraw_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(400)   

@pytest.mark.parametrize("deposit_amount, withdraw_amount, expected_balance", [
    (200, 50, 150),
    (100, 20, 80)])
    #(10, 30, 20)]) #for scenario like, we need a different test function to handle exceptions 
                          
def test_bank_transaction_sequence(zero_bank_account,deposit_amount, withdraw_amount, expected_balance):
    zero_bank_account.deposit(deposit_amount)
    zero_bank_account.withdraw(withdraw_amount)
    #zero_bank_account.collect_interest()
    assert round(zero_bank_account.balance, 6) == expected_balance


