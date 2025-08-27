# convert_bold_subscript.py
import os
import re
import argparse

def convert_bold_subscript_in_file(file_path, dry_run=False):
    """
    读取文件，查找所有 \mathbf{...}_{...} 格式的 LaTeX 表达式，
    并将其转换为 \mathbf{...}\_{...} 的格式。

    例如：将 \mathbf{E}_{0R} 转换为 \mathbf{E}\_{0R}
          将 \mathbf{F}_x   转换为 \mathbf{F}\_{x}
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # 正则表达式，用于查找 \mathbf{主干}_{下标} 模式
        # 它能处理带花括号的下标 (_{...}) 和不带花括号的单字符下标 (_.)
        # 捕获组:
        # 1: (.+?)            - \mathbf{...} 中，花括号内的主要内容, 例如 'E'
        # 2: (?:\{(.+?)\}|([a-zA-Z0-9])) - 这是一个非捕获组，它匹配两种情况：
        #    - \{ (.+?) \}   - 匹配花括号内的下标，并捕获内容到 组3, 例如 '0R'
        #    - ([a-zA-Z0-9]) - 匹配单个字符的下标，并捕获到 组4, 例如 'x'
        pattern = re.compile(r"\\mathbf\{(.+?)\}_\s*(?:\{(.+?)\}|([a-zA-Z0-9]))")

        def replacer(match):
            """这个函数会根据匹配到的内容，将其重新组合成目标格式。"""
            main_part = match.group(1)
            subscript_braced = match.group(2)
            subscript_unbraced = match.group(3)

            # 优先使用在花括号中捕获到的下标内容
            subscript = subscript_braced if subscript_braced is not None else subscript_unbraced

            # 重新组合成目标格式: \mathbf{主干}\_{下标}
            # 确保下标部分总是被花括号包围，以保持一致性
            return f"\\mathbf{{{main_part}}}\\_{{{subscript}}}"

        new_content = pattern.sub(replacer, original_content)

        if new_content != original_content:
            print(f"  - 在文件 [{os.path.basename(file_path)}] 中发现并转换了 \\mathbf 记法。")
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
        description="自动将 LaTeX 中的 \\mathbf{...}_{...} 记法转换为 \\mathbf{...}\\\_{...} 格式。",
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
        if convert_bold_subscript_in_file(file_path, args.dry_run):
            total_files_changed += 1

    print("\n--- 处理完成 ---")
    if total_files_changed > 0:
        if args.dry_run:
            print(f"✅ 发现 {total_files_changed} 个文件可以被转换。")
        else:
            print(f"✅ 成功修改了 {total_files_changed} 个文件。")
    else:
        print("🎉 在指定文件中没有找到需要转换的 \\mathbf 记法。")

if __name__ == "__main__":
    main()