# fix_underscore.py
import os
import re
import argparse

def fix_underscores_in_content(content):
    """
    对给定的文本内容执行下划线转义的核心逻辑。
    它会查找所有紧跟在 '}' 后面的、且未被转义的 '_'，并将其转义。
    """
    # 使用一个偏移量来跟踪由于插入字符导致的位置变化
    offset = 0
    # 查找所有下划线的位置
    indices = [m.start() for m in re.finditer('_', content)]

    for i in indices:
        # 修正当前索引
        idx = i + offset

        # 条件 1: 检查下划线是否已经转义 (即前面是否是 '\')
        # 如果是，则跳过，防止重复转义
        if idx > 0 and content[idx - 1] == '\\':
            continue

        # 条件 2: 检查下划线是否紧跟在一个右花括号 '}' 后面
        if idx > 0 and content[idx - 1] == '}':
            # 执行转义：在下划线前插入一个反斜杠
            content = content[:idx] + '\\' + content[idx:]
            # 因为我们插入了一个字符，所以后续的索引需要增加1
            offset += 1
            
    return content

def process_markdown_file(file_path, dry_run=False):
    """
    读取文件，调用核心逻辑进行修复，然后保存更改。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        new_content = fix_underscores_in_content(original_content)

        if new_content != original_content:
            print(f"  - 在文件 [{os.path.basename(file_path)}] 中发现并修复了下划线。")
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
        description="自动转义 LaTeX 复杂表达式后的下划线，以防止 Markdown 渲染错误。",
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
        if process_markdown_file(file_path, args.dry_run):
            total_files_changed += 1
    
    print("\n--- 处理完成 ---")
    if total_files_changed > 0:
        if args.dry_run:
            print(f"✅ 发现 {total_files_changed} 个文件可以被修正。")
        else:
            print(f"✅ 成功修改了 {total_files_changed} 个文件。")
    else:
        print("🎉 在指定文件中没有找到需要修正的下划线。")

if __name__ == "__main__":
    main()
