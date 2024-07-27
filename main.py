# Скрипт расчета A/B подготовлен командой EXPF специально для лекций по A/B
# Курс по A/B-тестированиям expf.ru/ab_course
# A/B-платформа по подписке expf.ru/sigma

import pandas as pd

import config as cfg
from metric_builder import _load_yaml_preset
from report import build_experiment_report
import time


logger = cfg.logger
start_time = time.time()

# Мини-версия таблицы с данными по эксперименту, количество строк = 10000
# df = pd.read_csv("data/csv/df_sample.csv")

# Боевые данные (parquet)
df = pd.read_parquet(f'data/parquet/df.parquet')

logger.info("Data loaded")

experiment_report = build_experiment_report(
    df=df,
    metric_config=_load_yaml_preset()
)
experiment_report.to_csv(f"experiment_report.csv")

cfg.logger.info(time.time() - start_time)
