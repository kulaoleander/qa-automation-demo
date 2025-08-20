# logger.py  —— 统一的日志工具，别处直接 import 用
import logging
import os

def get_logger(name="qa"):
    os.makedirs("reports", exist_ok=True)
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # 已经设置过就直接用

    logger.setLevel(logging.INFO)

    # 输出到文件
    file_handler = logging.FileHandler("reports/run.log", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    file_handler.setFormatter(file_fmt)

    # 输出到控制台（可选）
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(file_fmt)

    logger.addHandler(file_handler)
    logger.addHandler(console)
    return logger
