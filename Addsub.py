import os
def combine_subtitles(sub1_path, sub2_path, output_path):
    with open(sub1_path, 'r', encoding='utf-8') as f1, open(sub2_path, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        combined_lines = []

        i, j = 0, 0
        while i < len(lines1) and j < len(lines2):
            if lines1[i].strip().isdigit() and lines2[j].strip().isdigit():
                # Add subtitle number
                combined_lines.append(lines1[i])
                i += 1
                j += 1

                # Add time range
                combined_lines.append(lines1[i])
                i += 1
                j += 1

                # Add subtitles from sub1 with color #ff9980
                while i < len(lines1) and lines1[i].strip() != "":
                    combined_lines.append(
                        f'<font color="#ff9980">{lines1[i]}</font>')
                    i += 1

                # Add subtitles from sub2 without changing color
                while j < len(lines2) and lines2[j].strip() != "":
                    combined_lines.append(lines2[j])
                    j += 1

                combined_lines.append("\n")
            else:
                i += 1
                j += 1

        with open(output_path, 'w', encoding='utf-8') as out:
            out.writelines(combined_lines)
def merge_subtitles_from_folders(folder1, folder2, output_folder):
    # Lấy danh sách tất cả các file trong mỗi folder
    files1 = sorted([f for f in os.listdir(folder1) if f.endswith('.srt')])
    files2 = sorted([f for f in os.listdir(folder2) if f.endswith('.srt')])

    # Đảm bảo output folder tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Kết hợp từng cặp file
    for f1, f2 in zip(files1, files2):
        sub1_path = os.path.join(folder1, f1)
        sub2_path = os.path.join(folder2, f2)
        combined_output_path = os.path.join(output_folder, f"combined_{f1}")
        combine_subtitles(sub1_path, sub2_path, combined_output_path)

# Sử dụng hàm
# combine_subtitles('002 What Is Node.js and Why Use It_.en.srt',
#                   '002 What Is Node.js and Why Use It_.en.vi.srt', '002 What Is Node.js and Why Use It_.combined.srt')

# Merge from folders
merge_subtitles_from_folders('en', 'vi', 'combined')