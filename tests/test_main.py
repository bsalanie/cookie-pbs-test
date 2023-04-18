from cookie_pbs_test.main import main


def test_main():
    assert main("Bernard") == "Hello from main, Bernard"
