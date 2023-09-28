import pytest


@pytest.fixture()
def Setup():
    print("I will be executing first ")
    yield
    print("I will be executing last ")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["rahul","shetty","acadamy"]

@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
    return request.param
