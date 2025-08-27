# fix_math_targeted.py
import os
import re
import argparse

def preprocess_delimiters(text):
    """
    根据用户指定的精确规则，预处理文本以修复和调整分隔符。
    """
    # 规则 1: 处理用户指定的 $$$$ -> $$ \n $$ 拆分规则。
    processed_text = text.replace('$$$$', '$$\n$$')

    # 规则 2: 将常见的 $$$ 书写错误修正为标准的 $$。
    processed_text = processed_text.replace('$$$', '$$')
    
    # 注意: 移除了过于激进的 '$$\s*$$' -> '$$' 规则，以修复“吞噬”bug。
    return processed_text

def process_math_block(match):
    """
    核心处理函数，根据用户最新的精确规则对数学块进行操作。
    """
    # 从原始匹配中获取内容
    original_block = match.group(0)
    inner_content = match.group(1)

    # 规则 3: 仅当公式块内包含 `\\` 作为分行符时才执行修复。
    # 如果没有 `\\`，则直接返回原始块，不做任何更改。
    if '\\\\' not in inner_content:
        return original_block

    # --- 从这里开始，是针对包含 `\\` 的块的修复逻辑 ---
    
    # 清理并统一环境为 aligned
    content_to_process = inner_content.strip()
    content_to_process = re.sub(r'\\begin\{align\*?\}', r'\\begin{aligned}', content_to_process)
    content_to_process = re.sub(r'\\end\{align\*?\}', r'\\end{aligned}', content_to_process)

    # 移除已有的 aligned 环境包裹，以便我们处理原始的行
    if content_to_process.startswith('\\begin{aligned}'):
        content_to_process = re.sub(r'\\begin\{aligned\}', '', content_to_process, 1)
        content_to_process = re.sub(r'\\end\{aligned\}', '', content_to_process, 1)
        content_to_process = content_to_process.strip()

    # BUG 修复: 先将物理行合并为逻辑行，再按 `\\` 分割
    # 1. 将源文件中的换行符合并为空格，防止将单个公式错误拆分
    content_merged_lines = re.sub(r'\s*\n\s*', ' ', content_to_process)
    # 2. 仅根据 LaTeX 的换行命令 `\\` 进行拆分
    lines = re.split(r'\\{2,4}', content_merged_lines)
    
    processed_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        # 应用精确的对齐规则
        if '&' not in line:
            # 寻找第一个不在{}中的等号
            equals_index = -1
            brace_level = 0
            for idx, char in enumerate(line):
                if char == '{':
                    brace_level += 1
                elif char == '}':
                    if brace_level > 0:
                        brace_level -= 1
                elif char == '=' and brace_level == 0:
                    equals_index = idx
                    break

            if equals_index != -1:
                line = line[:equals_index] + '&' + line[equals_index:]
            elif i == 0:
                line = '&' + line
        
        processed_lines.append(line)

    # 使用 ` \\\\` (四个反斜杠) 重新连接所有处理过的行
    final_content = " \\\\\\\\\n".join(processed_lines)

    # 用 `aligned` 环境和 `$$` 包裹最终内容
    return f"$$\n\\begin{{aligned}}\n{final_content}\n\\end{{aligned}}\n$$"


def process_markdown_file(file_path, dry_run=False):
    """
    读取、处理并可能保存指定的 Markdown 文件。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        content = preprocess_delimiters(original_content)
        
        pattern = re.compile(r'\$\$(.*?)\$\$', re.DOTALL)
        content = pattern.sub(process_math_block, content)

        if content != original_content:
            print(f"  - 在文件 [{os.path.basename(file_path)}] 中发现并修复了问题。")
            if not dry_run:
                print(f"    -> 正在写入更改...")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
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
        description="针对指定的Markdown文件或目录，进行精确的LaTeX数学区块修复。",
        formatter_class=argparse.RawTextHelpFormatter
    )
    # 参数现在是 'path'，可以接受一个文件或目录，默认为当前目录
    parser.add_argument(
        "path", 
        nargs='?', # '?' 表示0个或1个参数
        default='.', # 如果不提供参数，则默认为 '.' (当前目录)
        help="要处理的文件或目录的路径 (默认为当前目录)。"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="演习模式：仅显示将要更改的文件，不实际修改。"
    )
    args = parser.parse_args()

    target_path = args.path

    if args.dry_run:
        print("--- 演习模式 (DRY RUN) 已开启：将不会对文件进行任何修改。 ---\n")

    files_to_process = []
    # 检查路径是目录、文件还是不存在
    if os.path.isdir(target_path):
        print(f"🚀 正在扫描目录: {os.path.abspath(target_path)}")
        for root, _, files in os.walk(target_path):
            for file_name in files:
                if file_name.endswith('.md'):
                    files_to_process.append(os.path.join(root, file_name))
    elif os.path.isfile(target_path):
        if target_path.endswith('.md'):
            files_to_process.append(target_path)
        else:
            print(f"错误: 文件 '{target_path}' 不是一个Markdown (.md) 文件。")
            return
    else:
        print(f"错误: 路径 '{target_path}' 不是一个有效的文件或目录。")
        return

    if not files_to_process:
        print("在指定路径中没有找到要处理的 .md 文件。")
        return

    total_files_changed = 0
    total_files_scanned = len(files_to_process)

    # 循环处理收集到的所有文件
    for file_path in files_to_process:
        print(f"🔎 正在处理文件: {file_path}")
        if process_markdown_file(file_path, args.dry_run):
            total_files_changed += 1
    
    print("\n--- 处理完成 ---")
    print(f"总共扫描了 {total_files_scanned} 个 Markdown 文件。")
    if total_files_changed > 0:
        if args.dry_run:
            print(f"✅ 发现 {total_files_changed} 个文件可以被修复。")
        else:
            print(f"✅ 成功修改了 {total_files_changed} 个文件。")
    else:
        print("🎉 没有文件需要修复或所有扫描文件都已符合规范。")

if __name__ == "__main__":
    main()
