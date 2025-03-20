import sys
import time
import rich.markdown
from rich.console import Console

console = Console()
buffer = ""  # Stores full Markdown content progressively
code_block_buffer = []  # Temporary buffer for accumulating code blocks
inside_code_block = False  # Track if inside a multi-line code block

try:
    for line in sys.stdin:
        if line.strip().startswith("```"):  # Start or end of a code block
            inside_code_block = not inside_code_block
            if not inside_code_block:  # If ending a code block, flush it
                code_block_buffer.append(line)  # Add closing ```
                full_code_block = "".join(code_block_buffer)
                console.print(rich.markdown.Markdown(full_code_block))  # Render all at once
                code_block_buffer = []  # Reset buffer
            else:
                code_block_buffer.append(line)  # Start collecting a code block
        elif inside_code_block:
            code_block_buffer.append(line)  # Keep collecting inside code block
        else:
            console.print(rich.markdown.Markdown(line), end="")  # Print regular Markdown line-by-line

        time.sleep(0.2)  # Add delay to mimic AI streaming effect

except KeyboardInterrupt:
    pass  # Handle Ctrl+C gracefully
