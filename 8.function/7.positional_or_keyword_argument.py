def calculate_marks(maths, eng,hindi,comp=0,history=0):
    print(f"maths = {maths}")
    print(f"eng = {eng}")
    print(f"hindi = {hindi}")
    print(f"comp = {comp}")
    print(f"history = {history}")
    total_marks=maths+eng+hindi+comp+history
    print(f"Total marks scored = {total_marks}")
calculate_marks(11,22,comp=45,history=89, hindi=67)