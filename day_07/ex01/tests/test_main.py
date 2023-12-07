import sys
import os
sys.path.append(os.path.abspath('../../ex00'))
import main as tested_file
import parameters as params
import pytest


def test_get_choice(monkeypatch):
    user_input = ["", "6", "2", "1"]
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))
    choice = tested_file.get_choice()
    assert choice == "2"

def test_get_choice_sec(monkeypatch):
    user_input = ["a", "3", "-3", "1"]
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))
    choice = tested_file.get_choice()
    assert choice == '1'

def test_print_question(capsys):
    question = {
        "question": "What is your favorite color?",
        "answers": [
            {"answer": "Red"},
            {"answer": "Blue"},
            {"answer": "Green"}
        ]
    }
    expected_output = 'What is your favorite color?1: Red2: Blue3: Green'
    tested_file.print_question(question)
    captured = capsys.readouterr().out.strip().replace('\n', '').replace('\t', '')
    assert captured == expected_output

def test_decide(capsys):
    tested_file.decide(tested_file.MAX_POINT / 2)
    captured = capsys.readouterr().out.strip().replace('\n', '').replace('\t', '')
    assert captured == 'replicant'

    tested_file.decide(tested_file.MAX_POINT / 2 + 1)
    captured = capsys.readouterr().out.strip().replace('\n', '').replace('\t', '')
    assert captured == 'human'

    with pytest.raises(TypeError):
        tested_file.decide()

def test_get_param_from_user_invalid_input(monkeypatch):
    user_input = ["abc", "0", "-42", "42"]
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))
    asker = params.Params()
    result = asker.get_param_from_user("param")
    assert result == 42

def test_params():
    asker = params.Params()
    out = asker.evaluate_params()
    assert out == -1

def test_evaluate_params(monkeypatch):
    user_input = ["42"]
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))

    asker = params.Params()
    asker.set_etalon_params({"param": 42})
    out = asker.evaluate_params()
    assert out == 1 * params.DOWN_C

def test_evaluate_params(monkeypatch):
    user_input = ["42", "-500", "abc", "35"]
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))
    asker = params.Params()
    asker.set_etalon_params({"param": 42, "param_2": 34})

    out = asker.evaluate_params()
    assert out == 1 * params.DOWN_C * params.UP_C


def test_validator():
    validator = params.ResultValidator()
    assert validator.validate_result(1, "param") == True
    assert validator.validate_result(1, "blushing level") == True
    assert validator.validate_result(0, "blushing level") == False
    assert validator.validate_result(7, "blushing level") == False
    assert validator.validate_result(9, "pupillary dilation") == False
    assert validator.validate_result(1, "pupillary dilation") == False
    assert validator.validate_result(2, "pupillary dilation") == True

def test_main(monkeypatch, capsys):
    user_input = ["1", "16", "60", "1", "2",
                  "1", "16", "60", "1", "2",
                  "1", "16", "60", "1", "2",
                  "1", "16", "60", "1", "2",
                  "1", "16", "60", "1", "2",
                  "1", "16", "60", "1", "2",
                  "1", "16", "60", "1", "2",
                  "1", "16", "60", "1", "2",
                  "1", "16", "60", "1", "2",
                  "1", "16", "60", "1", "2"
                  ]
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))
    tested_file.main()
    index = capsys.readouterr().out.strip().rfind("replicant")
    assert index != -1

def test_main_sec(monkeypatch, capsys):
    user_input = ["1", "17", "65", "3", "6",
                    "1", "17", "65", "3", "6",
                    "1", "17", "65", "3", "6",
                    "1", "17", "65", "3", "6",
                    "1", "17", "65", "3", "6",
                    "1", "17", "65", "3", "6",
                    "1", "17", "65", "3", "6",
                    "1", "17", "65", "3", "6",
                    "1", "17", "65", "3", "6",
                    "1", "17", "65", "3", "6"
                  ]
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))
    tested_file.main()
    index = capsys.readouterr().out.strip().rfind("human")
    assert index != -1
