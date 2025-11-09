import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--id', dest='id', required=True, type=str, help='problemID. eg: 2167B')
args = parser.parse_args()

directory = os.path.join(os.getcwd(), 'cf_solves/')
if not os.path.exists(directory):
    os.makedirs(directory)

print("Sure!! Let's go! Let's try for 20 minutes...\n")

lang = input("Input language extension: eg: 'cpp', 'py' etc.\n")

if lang == 'py':
    file = args.id + '.py'
    path = os.path.join(directory, f"{file}")
    if not os.path.isfile(path):
        with open('py_template.txt', 'r') as template, open(path, 'w') as cf_file:
            cf_file.write(template.read())
elif lang == 'cpp':
    file = args.id + '.cpp'
    path = os.path.join(directory, f"{file}")
    if not os.path.isfile(path):
        with open('cpp_template.txt', 'r') as template, open(path, 'w') as cf_file:
            cf_file.write(template.read())


os.system(f"code {path}")
os.system(f"timeout -t 1200")

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
            print("\ncool...'r'+'enter' to run again.\n")
        elif x == 'g':
            print(f"Pushing {file} to Github")
            os.chdir("cf_solves")
            os.system(f"git add {file}")
            os.system(f'git commit -m "solved {args.id}"')
            os.system(f"git push origin main")
            os.chdir("..")
            break
        elif x == 'q':
            print("quitting...\n")
            break
    except Exception as e:
        print(e)
