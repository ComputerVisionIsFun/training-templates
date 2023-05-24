from termcolor import colored


def show_train_info(title:str, parameters:dict):
    print(colored('*'*13 + title + '*'*13, 'yellow'))
    for para in parameters:
        print(colored(para + ': ', 'cyan') + str(parameters[para]))
    

    print(colored('*'*13 +'*'*13, 'yellow'))