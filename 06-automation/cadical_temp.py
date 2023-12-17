import os
import re
from collections import Counter

def check_process_and_real_time(file_content):
    find_process_time = re.search(r'total process time since initialization:\s*(\d+(\.\d+)?)\s*seconds', file_content)
    find_real_time = re.search(r'total real time since initialization:\s*(\d+(\.\d+)?)\s*seconds', file_content)
    process_time = float(find_process_time.group(1))
    real_time = float(find_real_time.group(1))

    # checking if both the time in the file is greater than 10 sec or no
    if process_time > 10 and real_time > 10:
        return True

# a dictionary to keep all the values acquired
bump_dict = {}

# a function to acquire all the percentage values of bump and converting it to float
def find_bump_percentage(file_content):
    find_bump = re.search(r'\b(\d+\.\d+)%\s+bump\b', file_content)

    if find_bump:
        return float(find_bump.group(1))
    return None

if __name__ == '__main__':

    # the working directory
    directory_path = "D:\\Course_Content\\Missing_semester\\Exercise_6\\cadical1.9-0j\\cadical1.9-0j"
    for filename in os.listdir(directory_path):

        # trying to get the contents from all the files having .log extension
        if filename.endswith(".log"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                file_content = file.read()
                is_valid = check_process_and_real_time(file_content)

                # if both the time is > 10 sec continue with finding percentage of phase in that file
                if is_valid:
                    percentage = find_bump_percentage(file_content)

                    # store acquired percentage in a dict for easy sorting later
                    if percentage is not None:
                        bump_dict[filename] = percentage

    # print different values
    print(min(bump_dict.values()))
    print(max(bump_dict.values()))
    highest_percentage = Counter(bump_dict).most_common(3)
    print(highest_percentage)
    least_percentage = Counter(bump_dict).most_common()[:-4:-1]
    print(least_percentage)