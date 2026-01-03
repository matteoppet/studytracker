def get_time_text_to_integer(time: str) -> list[int, int]:
    hour, minutes = time.split(":")
    hour = int(hour)
    minutes = int(minutes)

    return [hour, minutes]

def get_sum_in_time_format(times: list) -> list[int, int]:
    from datetime import timedelta
    
    total_delta = timedelta()
    for time in times:
        h, m = map(int, time.split(":"))
        delta = timedelta(hours=h, minutes=m)
        total_delta += delta

    total_seconds = int(total_delta.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes = remainder // 60

    return [hours, minutes]