from view_inquirer import View

def main():

  view = View()

  view.display_message('hello')
  answer = view.display_list_prompt('what is your name', ['mark', 'bob'])
  view.display_message(answer)

if __name__ == '__main__':
    main()
  
