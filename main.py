import pandas as pd

from Play import Play

users_path = 'Users.csv'
state = 'First Page'
username = ''


def Login():
    global state
    global username
    df = pd.read_csv(users_path, index_col='ID')
    while True:
        user = input('Please Enter Your Username: ')
        if not (df['Username'] == user).any():
            print('No Such User with Username!\n' +
                  'Try again or register first!')
            state = input('Select an Item by writing its name:\n' +
                          'Login\n' + 'Sign up\n')
            if state.__eq__('Sign up'):
                return
        else:
            user_info = df[['Username', 'Password']][df['Username'] == user]
            if input('Please enter Your Password: ').__eq__(user_info.Password.values[0]):
                state = 'Play'
                username = user
                return
            else:
                print('Wrong Password!\n' +
                      'Try again or register first!')
                state = input('Select an Item by writing its name:\n' +
                              'Login\n' + 'Sign up\n')
                if state.__eq__('Sign up'):
                    return


def Register():
    global state
    df = pd.read_csv(users_path, index_col='ID')
    while True:
        username = input('Please Enter Your Username: ')
        if (df['Username'] == username).any():
            print('This Username Already Exist!!\n' +
                  'Try again or register first!')
            state = input('Select an Item by writing its name:\n' +
                          'Login\n' + 'Sign up\n')
            if state.__eq__('Login'):
                return
        else:
            password = input('Please Enter a Password: ')
            df.loc[len(df)] = [username, password, 0]
            df.to_csv(users_path)
            state = input('Select an Item by writing its name:\n' +
                          'Login\n' + 'First Page\n')
            return


def Show_scores():
    print('Scores: ')
    df = pd.read_csv(users_path, index_col='ID')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df[['Username', 'Score']])


while not state.__eq__('Exit'):
    if state.__eq__('First Page'):
        print('**************************** First Page *******************************')
        print('Game Logic: first we show a 10*10 table to player.\n' +
              'In some indexes of this table we have some mins, and the player \n' +
              'should find this mins by the information that he is given by the \n' +
              'neighbors indexes.\n' +
              'And he should avoid clicking on this indexes containing mins.')

        state = input('Select an Item by writing its name:\n' +
                      'Login\n' + 'Sign up\n' + 'Score Board\n')
    elif state.__eq__('Login'):
        print('**************************** Login Page *******************************')
        state = input('Select an Item by writing its name:\n' +
                      'Login(Entering Data)\n' + 'Sign up\n' + 'Score Board\n')
        if state.__eq__('Login'):
            Login()
    elif state.__eq__('Sign up'):
        print('**************************** Sign up Page *******************************')
        state = input('Select an Item by writing its name:\n' +
                      'Login(Entering Data)\n' + 'Sign up\n' + 'Score Board\n')
        if state.__eq__('Sign up'):
            Register()
    elif state.__eq__('Play'):
        print('**************************** Play Page *******************************')
        play = Play()
        score = play.start() * 10
        df = pd.read_csv(users_path, index_col='ID')
        df.loc[df['Username'] == username, 'Score'] += score
        df.to_csv(users_path)
        state = 'Score Board'
    elif state.__eq__('Score Board'):
        print('**************************** Score Board Page *******************************')
        Show_scores()
        state = 'First Page'