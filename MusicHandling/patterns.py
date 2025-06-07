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
    "pattern13": "1-K,7-K,11-K,19-K,25-K,27-K",
    "pattern14": "1-K,9-K,17-K,25-K,27-K,30-K,1-Q,5-Q,9-Q,13-Q,17-Q,21-Q,25-Q",
    "pattern15": "1-K,9-K,17-K,25-K,27-K,30-K,1-Q,3-Q,5-Q,7-Q,9-Q,11-Q,13-Q,15-Q,17-Q,19-Q,21-Q,23-Q,25-Q,27-Q,29-Q,31-Q",
    "pattern16": "1-K,9-K,17-K,25-K,27-K,30-K,1-Q,2-Q,3-Q,4-Q,5-Q,6-Q,7-Q,8-Q,9-Q,10-Q,11-Q,12-Q,13-Q,14-Q,15-Q,16-Q,17-Q,18-Q,19-Q,20-Q,21-Q,22-Q,23-Q,24-Q,25-Q,26-Q,27-Q,28-Q,29-Q,30-Q,31-Q,32-Q",
    "pattern17": "1-K,9-K,17-K,25-K,27-K,30-K,1-O,2-Q,3-Q,4-Q,5-Q,6-Q,7-Q,8-Q,9-O,10-Q,11-Q,12-Q,13-Q,14-Q,15-Q,16-Q,17-O,18-Q,19-Q,20-Q,21-Q,22-Q,23-Q,24-Q,25-O,26-Q,27-O,28-Q,29-Q,30-O,31-Q,32-Q",
    "pattern18": "1-K,9-K,11-K,17-K,23-K,27-K, 1-O,3-Q,5-Q,7-Q,9-Q,11-O,13-Q,15-Q,17-O,19-Q,21-Q,23-O,25-Q,27-O,29-Q,31-Q",
    "pattern19": "1-K,3-K,7-K,11-K,15-K,19-K,23-K,25-K,27-K,28-K,1-C,5-C,9-C,13-C,17-C,21-C,25-C,27-C,31-C,3-O,7-O,11-O,15-O,19-O,23-O,29-O",


    "patternHiHatDemo": "1-K,3-C,5-K,7-P,9-K,11-C,13-S,15-Q,17-K,19-C,21-S,23-O,25-K,27-P,29-S,31-C"

}

def get_pattern_with_snares(pattern_id):
    if pattern_id not in patterns:
        raise ValueError(f"Pattern '{pattern_id}' not found.")
    return snares + patterns[pattern_id]

