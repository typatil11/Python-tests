import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_program(Setup):
    msg="hello"
    assert msg=="hello"

@pytest.fixture()
def setup(Setup):
    print(" i will  be executing first")

def test_fixdemo():
    print(" i will=-========")