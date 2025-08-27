# pad_math_blocks.py
import os
import re
import argparse

def add_padding_to_math_blocks(file_path, dry_run=False):
    """
    读取文件，为所有由 $$...$$ 定义的 LaTeX 公式块确保其上下文都有一行空行。
    这有助于防止 Markdown 解析器错误地渲染它们。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # 步骤 1: 找到所有由 $$ 包围的块，并在其前后强制添加换行符
        # - `(^\s*\$\$.*?^\s*\$\$)` 是一个捕获组:
        #   - `^\s*\$\$`     : 匹配以可选空格和 $$ 开头的行。
        #   - `.*?`          : 非贪婪地匹配任何字符，包括换行符。
        #   - `^\s*\$\$`     : 匹配另一个以可选空格和 $$ 开头的行作为结束。
        # - `re.DOTALL` 标志让 `.` 可以匹配换行符。
        # - `re.MULTILINE` 标志让 `^` 可以匹配每一行的开头。
        # - 替换字符串 `\n\g<0>\n` 会在整个匹配到的块 ( \g<0> ) 的前后都加上换行符。
        pattern = re.compile(r"(^\s*\$\$.*?^\s*\$\$)", re.DOTALL | re.MULTILINE)
        
        # 强制在每个块前后都加上换行符
        padded_content = pattern.sub(r"\n\g<0>\n", original_content)
        
        # 步骤 2: 清理多余的空行。将三个或更多的连续换行符替换为两个。
        # 这可以处理文件开头/结尾或已有空行的情况，使格式更整洁。
        new_content = re.sub(r'\n{3,}', r'\n\n', padded_content)

        if new_content != original_content:
            print(f"  - 在文件 [{os.path.basename(file_path)}] 中为公式块添加了空行。")
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
        description="自动为 LaTeX 公式块 ($$ ... $$) 的上下文添加空行，以确保 Markdown 正确渲染。",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "files",
        nargs='+',
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
        if add_padding_to_math_blocks(file_path, args.dry_run):
            total_files_changed += 1

    print("\n--- 处理完成 ---")
    if total_files_changed > 0:
        if args.dry_run:
            print(f"✅ 发现 {total_files_changed} 个文件可以被修正。")
        else:
            print(f"✅ 成功修改了 {total_files_changed} 个文件。")
    else:
        print("🎉 在指定文件中没有找到需要添加空行的公式块。")

if __name__ == "__main__":
    main()