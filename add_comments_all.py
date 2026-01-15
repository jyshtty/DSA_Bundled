import os

def add_generic_comments(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.py'):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, 'r') as f:
                        content = f.read()
                        lines = content.split('\n')
                        if lines and lines[0].startswith('#'):
                            continue
                        # Generate problem name from filename
                        problem_name = filename.replace('.py', '').replace('_', ' ').title()
                        # Check if in Leetcode folder
                        if 'leetcode' in dirpath.lower():
                            link = f"https://leetcode.com/problems/{problem_name.lower().replace(' ', '-')}/"
                        else:
                            link = ""
                        comment = f"# {problem_name}\n"
                        if link:
                            comment += f"# {link}\n"
                        comment += f"# Description: Solve the {problem_name.lower()} problem.\n"
                        comment += f"# Approach: Implement the standard algorithm.\n"
                        comment += f"# Time Complexity: O(n)\n"
                        comment += f"# Space Complexity: O(1)\n"
                        comment += f"# Implementation:\n\n"
                        new_content = comment + content
                        with open(filepath, 'w') as f:
                            f.write(new_content)
                        print(f"Added comments to {filepath}")
                except Exception as e:
                    print(f"Error with {filepath}: {e}")

add_generic_comments('/workspaces/DSA_Bundled')