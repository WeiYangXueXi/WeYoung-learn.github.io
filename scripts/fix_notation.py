# fix_notation.py
import os
import re
import argparse

def fix_derivative_notation_in_file(file_path, dry_run=False):
    """
    读取文件，将 f_{x}' 或 f_{1}' 这样的导数记法替换为 f_{x}' 或 f_{1}'，然后保存更改。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # 正则表达式，用于查找 f_{x}', F_{12}'', g_{y}''' 等模式。
        # 它能同时处理不带花括号的单个字符下标 (f_{x}') 和
        # 带花括号的多字符下标 (f_{xy}')。
        # 捕获组:
        # 1: ([fFgGhHEeBb])       - 函数名 (f, F, g, G)
        # 2: ('+)           - 一个或多个撇号 (即导数阶数)
        # 3: ([^}]+?)       - 花括号内的下标内容, 例如 'xy' (非贪婪匹配)
        # 4: ([a-zA-Z0-9])   - 单个字符的下标, 例如 'x'
        pattern = re.compile(r"([fFgGhHEeBb])('+)_\s*(?:\{([^}]+?)\}|([a-zA-Z0-9]))")

        def replacer(match):
            """这个函数会根据匹配到的内容，将其重新组合成正确的顺序。"""
            func_name = match.group(1)
            primes = match.group(2)
            subscript_braced = match.group(3)
            subscript_unbraced = match.group(4)

            # 优先使用在花括号中捕获到的下标内容
            subscript = subscript_braced if subscript_braced is not None else subscript_unbraced

            # 重新组合成标准格式: f_{下标}'
            return f"{func_name}_{{{subscript}}}{primes}"

        new_content = pattern.sub(replacer, original_content)

        if new_content != original_content:
            print(f"  - 在文件 [{os.path.basename(file_path)}] 中发现并修正了导数记法。")
            if not dry_run:
                print(f"    -> 正在写入更改...")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            return True
        return False

    except FileNotFoundError:
        print(f"错误: 找不到文件 '{file_path}'")
        return False
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="自动将 LaTeX 中的导数记法从 f_{x}' 格式修正为 f_{x}' 格式。",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "files", 
        nargs='+', # '+' 表示需要一个或多个参数
        help="一个或多个要处理的 .md 文件的路径。"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="演习模式：仅显示将要执行的更改，不实际修改文件。"
    )
    args = parser.parse_args()

    if args.dry_run:
        print("--- 演习模式 (DRY RUN) 已开启：将不会对文件进行任何修改。 ---\n")

    total_files_changed = 0
    for file_path in args.files:
        if not os.path.isfile(file_path):
            print(f"跳过: '{file_path}' 不是一个有效的文件。")
            continue
        
        print(f"🚀 正在处理文件: {file_path}")
        if fix_derivative_notation_in_file(file_path, args.dry_run):
            total_files_changed += 1
    
    print("\n--- 处理完成 ---")
    if total_files_changed > 0:
        if args.dry_run:
            print(f"✅ 发现 {total_files_changed} 个文件可以被修正。")
        else:
            print(f"✅ 成功修改了 {total_files_changed} 个文件。")
    else:
        print("🎉 在指定文件中没有找到需要修正的导数记法。")

if __name__ == "__main__":
    main()
