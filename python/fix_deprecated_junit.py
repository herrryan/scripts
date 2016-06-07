#!/user/bin/python
import sys
import os

path = "/home/taagufe1/EIMULEPOC"
OLD_STRING = "import junit.framework.Assert;"
NEW_STRING = "import org.junit.Assert;"

def main():
    javafiles = [os.path.join(root, name)
             for root, dirs, files in os.walk(path)
             for name in files
             if name.endswith((".java"))]
    for src_file in javafiles:
        is_deprecated_lib_and_replace_with_new(src_file);

def is_deprecated_lib_and_replace_with_new(src_file):
	file_data = None;
	with open(src_file, 'r') as file:
		file_data = file.read();
		if (OLD_STRING) in file_data:
			file_data = file_data.replace(OLD_STRING, NEW_STRING);
	
	with open(src_file, 'w') as file:
  		file.write(file_data);

if __name__ == "__main__":
	main();
