# patterns.py

snares = "5-S,13-S,21-S,29-S,"

patterns = {
    "pattern01": "1-K,9-K,17-K,25-K",
    "pattern02": "1-K,9-K,17-K,25-K,27-K,30-K",
    "pattern03": "1-K,9-K,11-K,17-K,23-K,27-K",
    "pattern04": "1-K,3-K,7-K,11-K,15-K,19-K,23-K,25-K,27-K,28-K",
    "pattern05": "1-K,3-K,7-K,9-K,12-K,15-K,18-K,20-K,23-K,25-K,27-K,31-K",
    "pattern06": "1-K,9-K,15-K,17-K,19-K,20-K,23-K,25-K,27-K,31-K",
    "pattern07": "1-K,3-K,4-K,7-K,9-K,12-K,15-K,19-K,20-K,23-K,24-K,26-K,28-K,31-K",
    "pattern08": "1-K,3-K,9-K,11-K,17-K,19-K,23-K,27-K",
    "pattern09": "1-K,9-K,15-K,19-K,23-K,25-K",
    "pattern10": "1-K,9-K,17-K,19-K,23-K,27-K",
    "pattern11": "1-K,7-K,8-K,9-K,11-K,15-K,19-K,20-K,23-K,25-K,27-K,31-K",
    "pattern12": "1-K,3-K,7-K,11-K,15-K,17-K,19-K,23-K,27-K,32-K",
    "pattern13": "1-K,7-K,11-K,19-K,25-K,27-K"
}

def get_pattern_with_snares(pattern_id):
    if pattern_id not in patterns:
        raise ValueError(f"Pattern '{pattern_id}' not found.")
    return snares + patterns[pattern_id]

