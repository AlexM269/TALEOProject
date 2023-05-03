import recherche
import indexation

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    req = ((1,0,1,0.5),(0,0.5,0,1))
    doc = ((1,0.25,0.90,0.6),(0.2,0.6,0.1,0.9))
    print(recherche.similarity_evaluation(req, doc, 0.5))

