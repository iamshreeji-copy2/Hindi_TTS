import os

dataset_root = "/media/aaa/Seagate/Datasets/Hindi_TTS_Dataset/Merged/"
metadata_path = os.path.join(dataset_root, "metadata.csv")
output_list_path = "train.list"

speaker_name = "Hindi_Female"
language = "hi"

with open(metadata_path, 'r', encoding='utf-8') as f_in, \
     open(output_list_path, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        parts = line.strip().split('|')
        if len(parts) < 2:
            continue
        
        rel_path = parts[0]
        text = parts[1]
        
        # Construct absolute path
        abs_path = os.path.join(dataset_root, rel_path)
        
        # GPT-SoVITS format: path|speaker|language|text
        new_line = f"{abs_path}|{speaker_name}|{language}|{text}\n"
        f_out.write(new_line)

print(f"Successfully generated {output_list_path}")
