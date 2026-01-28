import logging

import GlobalConfigs  # noqa: F401

from src.main import hello_world, main


def test_hello_world():
    assert hello_world() == "Hello, World!"


def test_main_logging(caplog):
    """main() 함수가 모든 레벨의 로그를 올바르게 출력하는지 테스트합니다."""
    with caplog.at_level(logging.DEBUG):
        main()

    assert "Debugging information" in caplog.text
    assert "This is a hypermodern Python application." in caplog.text
    assert "This is a warning message." in caplog.text
    assert "An error has occurred." in caplog.text
    assert "Critical issue encountered." in caplog.text
