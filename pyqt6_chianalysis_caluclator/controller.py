"""
controller py
"""
def get_results(expected_one: float, expected_two: float, expected_three: float, expected_four: float, 
                observed_one: float, observed_two: float, observed_three: float, observed_four: float,
                number: float) -> str:
    results =""    
    chi_analysis_number = (((observed_one-expected_one)**2/expected_one)+
                           ((observed_two-expected_two)**2/expected_two)+((observed_three-expected_three)**2/
                           expected_three)+((observed_four-expected_four)**2/expected_four))
    
    if chi_analysis_number > number:
        results = f"Biased."
    else:
        results = f"Unbiased."

    return results
def get_total(expected_one: float, expected_two: float, expected_three: float, expected_four: float, 
                observed_one: float, observed_two: float, observed_three: float, observed_four: float) -> int:
    total = ""
    total_number = (((observed_one-expected_one)**2/expected_one)+
                           ((observed_two-expected_two)**2/expected_two)+((observed_three-expected_three)**2/
                           expected_three)+((observed_four-expected_four)**2/expected_four))
    
    total = total_number
    return total 
    
#Global Scope
if __name__ == "__main__":
    results = get_results(559,186,186,62,556,184,193,61,7.82)
    print(results)

    total = get_total(559,186,186,62,556,184,193,61)
    print(total)
