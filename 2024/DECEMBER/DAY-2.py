#--------------------------------------------------------------------------------------------------
#PART - ONE
#--------------------------------------------------------------------------------------------------
def is_safe_report(report):
    increasing = True
    decreasing = True
    
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        
        if not (1 <= abs(diff) <= 3):
            return False
        
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False
            
    return increasing or decreasing

def analyze_reports(filename):
    with open(filename, "r") as file:
        reports = file.readlines()
    
    safe_count = 0
    for line in reports:
        levels = list(map(int, line.split()))
        if is_safe_report(levels):
            safe_count += 1
    
    return safe_count

input_file = "2024/DEC-INPUTS/DEC-DAY-2.1.txt"
safe_reports = analyze_reports(input_file)
print(f"SAFE REPORTS: {safe_reports}")
#--------------------------------------------------------------------------------------------------
#PART - TWO
#--------------------------------------------------------------------------------------------------
def is_safe_report(report):
    increasing = True
    decreasing = True
    
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        
        if not (1 <= abs(diff) <= 3):
            return False

        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False
            
    return increasing or decreasing

def is_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False

def analyze_reports_with_dampener(filename):
    with open(filename, "r") as file:
        reports = file.readlines()
    
    safe_count = 0
    for line in reports:
        levels = list(map(int, line.split()))
        
        if is_safe_report(levels) or is_safe_with_dampener(levels):
            safe_count += 1
    
    return safe_count

input_file = "2024/DEC-INPUTS/DEC-DAY-2.2.txt"
safe_reports = analyze_reports_with_dampener(input_file)
print(f"SAFE REPORTS: {safe_reports}")
#--------------------------------------------------------------------------------------------------