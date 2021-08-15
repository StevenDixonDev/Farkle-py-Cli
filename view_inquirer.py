from typing import Any
from PyInquirer import prompt

class View():
  def __init__(self):
    pass

  def display_list_prompt(self, message: str, choices: list) -> any:
    questions = {
        'type': 'list',
        'name': 'question',
        'message': message,
        'choices': choices
    }
    answer = prompt(questions)
    return answer['question']

  def display_single_prompt(self, message: str) -> any:
    questions = {
        'type': 'list',
        'name': 'question',
        'message': message,
    }
    answer = prompt(questions)
    return answer['question']

  def display_message(self, message: str) -> None:
    print(message)
  

