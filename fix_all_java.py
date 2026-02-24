# -*- coding: utf-8 -*-
import re
import glob
import os

def fix_file(filepath):
    with open(filepath, 'rb') as f:
        raw = f.read()
    
    try:
        content = raw.decode('utf-8')
    except:
        content = raw.decode('utf-8', errors='replace')
    
    original = content
    fixes = 0
    
    # Fix Class<> without type - should be Class<?>
    if 'Class<>' in content:
        content = content.replace('Class<>', 'Class<?>')
        fixes += 1
    
    # Fix ternary operators missing ?
    # Pattern: something condition : value -> should be condition ? value
    # Match patterns like "useCustomNaming  value1 : value2"
    content = re.sub(r'(\w+)\s+(\w+)\s+(\w+)\s*:', r'\1 \2 ? \3 :', content)
    if re.search(r'\w+\s+\w+\s+:', content):
        fixes += 1
    
    # Fix unclosed strings - Chinese char followed by " then "
    # Pattern: "xxx字" -> should be "xxx"
    content = re.sub(r'"([^"]*)字"', r'"\1"', content)
    
    # Fix patterns like "true：字" -> "true"
    content = re.sub(r'true：[^"]*"', 'true"', content)
    content = re.sub(r'false：[^"]*"', 'false"', content)
    
    # More aggressive: remove any remaining " followed by Chinese and "
    content = re.sub(r'"[^"]*字"', '""', content)
    
    # Fix patterns where ? was incorrectly removed
    # Look for patterns like "xxx)" that should be "xxx")"
    content = re.sub(r'(\w+)\s+(\w+)\s+\)', r'\1 \2)', content)
    
    if content != original:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {filepath} ({fixes} fixes)")
            return True
        except Exception as e:
            print(f"Error writing {filepath}: {e}")
            return False
    return False

# Fix all Java files
java_files = glob.glob(r'c:\Users\20886\Desktop\CNT\**\*.java', recursive=True)
print(f"Checking {len(java_files)} Java files...")

fixed_count = 0
for java_file in java_files:
    if fix_file(java_file):
        fixed_count += 1

print(f"\nFixed {fixed_count} files!")
