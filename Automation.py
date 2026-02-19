#In the name of allah
import os
import shutil

def organize_my_files(folder_pass):
    pictures_folder = os.path.join(folder_pass,'pictures')
    os.makedirs(pictures_folder,exist_ok=True)
    compressed_folder = os.path.join(folder_pass,'Compressed file')
    os.makedirs(compressed_folder,exist_ok=True)
    text_folder = os.path.join(folder_pass,'texts')
    os.makedirs(text_folder,exist_ok=True)
    codes_folder = os.path.join(folder_pass, 'codes')
    os.makedirs(codes_folder,exist_ok=True)
    video_folder = os.path.join(folder_pass,'videos')
    os.makedirs(video_folder,exist_ok=True)
    other_folder = os.path.join(folder_pass , 'others')
    os.makedirs(other_folder,exist_ok=True)

    files = os.listdir(folder_pass)
    count = 0
    for file_name in files:
        file_path = os.path.join(folder_pass, file_name)
        if os.path.isdir(file_path):
            
            continue  # اگه پوشه بود، برو سراغ بعدی
        elif file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            destination = os.path.join(pictures_folder, file_name)
            shutil.move(file_path, destination)
        elif file_name.lower().endswith(('.mp4', '.mkv', '.wmv')):
            destination = os.path.join(video_folder, file_name)
            shutil.move(file_path, destination)
        elif file_name.lower().endswith(('.py', '.js', '.html')):
            destination = os.path.join(codes_folder, file_name)
            shutil.move(file_path, destination)
        elif file_name.lower().endswith(('.txt', '.pdf', '.doc')):
            destination = os.path.join(text_folder, file_name)
            shutil.move(file_path, destination)
        elif file_name.lower().endswith(('.zip', '.rar',)):
            destination = os.path.join(compressed_folder, file_name)
            shutil.move(file_path, destination)
        else:
            destination = os.path.join(other_folder, file_name)
            shutil.move(file_path, destination)   
        count += 1

    return f'numbeer of organized files : {count}'


folder = input("Enter the path of folder : \n")

if os.path.exists(folder):
    print(organize_my_files(folder))
else:
    print("There is not any folder with this path ❌ ")