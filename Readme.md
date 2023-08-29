## Usage
+The application allows for translation and merging of subtitles into a single file.

+It is useful for watching movies, films, videos, clips, etc. with bilingual subtitles on devices that do not support multiple subtitles

## Installation Guide

To install this application, follow these steps:

1. Clone this repository to your machine.
2. Run the Addsub.py file.

## Configuration
To change the color of the subtitles, change the color value in the Addsub.py file
```python
```
For example: To change the color of sub 1 to #ff9980, change the following code:
```
# Add subtitles from sub1 with color #ff9980
                while i < len(lines1) and lines1[i].strip() != "":
                    combined_lines.append(f'<font color="#ff9980">{lines1[i]}</font>')
                    i += 1
```
***
## Demo
![image](https://github.com/toanvuvv/Translate_Merge_Subtitle/assets/87163954/fee48278-5eb8-4a18-af40-37161f93fb10)