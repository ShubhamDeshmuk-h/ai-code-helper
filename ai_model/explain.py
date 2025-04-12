# explain.py
"""
This module generates natural-language explanations for bug fixes or refactoring.
Currently, it provides mock logic and can be extended with AI-based summarizers later.
"""

def generate_explanation(original_code: str, modified_code: str, action_type: str, lang: str) -> str:
    """
    Generate a simple explanation for the code transformation.
    
    Parameters:
        original_code (str): Original code snippet.
        modified_code (str): Modified code snippet (fixed/refactored).
        action_type (str): 'bug_fix' or 'refactor'.
        lang (str): Programming language used.
    
    Returns:
        str: Explanation of what changed.
    """

    if action_type == 'bug_fix':
        explanation = "Analyzed the code for common bugs in {}.\n".format(lang)
        if "pritn" in original_code and "print" in modified_code:
            explanation += "- Fixed a typo: 'pritn' was corrected to 'print'.\n"
        else:
            explanation += "- No obvious syntax or logical bugs detected.\n"
        explanation += "Code now follows basic language syntax rules and should run without errors."
    
    elif action_type == 'refactor':
        explanation = "Reviewed and optimized the {} code structure.\n".format(lang)
        if original_code.strip() != modified_code.strip():
            explanation += "- Reformatted indentation for better readability.\n"
            explanation += "- Added meaningful comments or headers.\n"
        else:
            explanation += "- No significant improvements were necessary.\n"
        explanation += "Refactored code is now easier to maintain and understand."
    
    else:
        explanation = "No action specified for explanation."

    return explanation
