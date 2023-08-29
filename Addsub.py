def combine_subtitles(sub1_path, sub2_path, output_path):
    with open(sub1_path, 'r', encoding='utf-8') as f1, open(sub2_path, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        combined_lines = []

        i, j = 0, 0
        while i < len(lines1) and j < len(lines2):
            if lines1[i].strip().isdigit() and lines2[j].strip().isdigit():
                # Add subtitle number
                combined_lines.append('\033[38;2;118;181;197m' + lines1[i] + '\033[0m')
                i += 1
                j += 1

                # Add time range
                combined_lines.append(lines1[i])
                i += 1
                j += 1

                # Add subtitles from both files
                while i < len(lines1) and lines1[i].strip() != "":
                    combined_lines.append(lines1[i])
                    i += 1

                while j < len(lines2) and lines2[j].strip() != "":
                    combined_lines.append(lines2[j])
                    j += 1

                combined_lines.append("\n")
            else:
                i += 1
                j += 1

        with open(output_path, 'w', encoding='utf-8') as out:
            out.writelines(combined_lines)
# Sử dụng hàm
combine_subtitles('002 What Is Node.js and Why Use It_.en.srt', '002 What Is Node.js and Why Use It_.en.vi.srt', '002 What Is Node.js and Why Use It_.combined.srt')
