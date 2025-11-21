import os.path

probId = input('Problem ID: (eg. 2160B): ')
lang = input("Enter language extension: (eg: 'cpp'/'py'): ")

directory = os.path.join(os.getcwd(), 'cf_solves/')
if not os.path.exists(directory):
    os.makedirs(directory)

if lang == 'py':
    file = probId + '.py'
    path = os.path.join(directory, f"{file}")
    if not os.path.isfile(path):
        with open('py_template.txt', 'r') as template, open(path, 'w') as cf_file:
            cf_file.write(template.read())
elif lang == 'cpp':
    file = probId + '.cpp'
    path = os.path.join(directory, f"{file}")
    if not os.path.isfile(path):
        with open('cpp_template.txt', 'r') as template, open(path, 'w') as cf_file:
            cf_file.write(template.read())

os.system(f"code {path}")
os.system(f"timeout -t 1200")
print("Sure!! Let's go! Let's try for 20 minutes...\n")

if lang == 'py':
    print("\t-'r'+'enter' to run code \n\t-'g' for git push \n\t-and 'q'+'enter' to quit\n")
elif lang == 'cpp':
    print("\t-'c'+'enter' to compile code \n\t-'r'+'enter' to run code \n\t-'g' for git push \n\t-and 'q'+'enter' to quit\n")

while True:
    try:
        x = input()
        if x == 'c':
            if lang == 'cpp':
                os.system(f'g++ -std=c++14 {path}')
                print('Compiled Successfully')
            elif lang == 'py':
                print('Compilation not needed.')
        if x == 'r':
            print('input here:\n')
            if lang == 'cpp':
                os.system('a')
                print()
            elif lang == 'py':
                os.system(f"python {path}")
            print("\ncool...'r'+'enter' to run again.\nHowever, if solved, 'g' + enter to push to github.\n")
        elif x == 'g':
            print(f"Adding {file} to Git")
            os.chdir("cf_solves")
            os.system(f"git add {file}")
            os.system(f'git commit -m "solved {probId}"')

            print("Pulling latest changes...")
            os.system("git pull --rebase --autostash")

            print("Pushing to GitHub...")
            os.system(f"git push origin main")
            os.chdir("..")
            break
        elif x == 'q':
            print("quitting...\n")
            break
    except Exception as e:
        print(e)
