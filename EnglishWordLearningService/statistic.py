from . import csv_utils

def get_statistic():
    result = {}
    total_fail = csv_utils.get_total_fail()
    total_success = csv_utils.get_total_success()
    
    result["total_words"] = csv_utils.get_total_words()
    result["total_success"] = total_success
    result["total_fail"] = total_fail
    result["percent_success"] = round(total_success / (total_success + total_fail) * 100) if total_fail + total_success != 0 else 0
    result["percent_success"] = str(result["percent_success"]) + "%"

    return result
