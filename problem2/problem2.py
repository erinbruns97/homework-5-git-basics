def date_format(date_str: str) -> str:
    month, day, year = date_str.split('/')
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"