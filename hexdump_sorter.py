import argparse
import re

def hexdump_sorter(hexdump, bytes_per_output=None, custom_range=None):
    """
    Sorts and formats a hexdump string.

    Args:
        hexdump (str): The input hexdump string (e.g., "89 23 45 66 77").
        bytes_per_output (int, optional): The number of bytes to group in the output. Defaults to None.
        custom_range (str, optional): A custom range of bytes to extract (e.g., "3:4"). Defaults to None.

    Returns:
        str: The formatted output string.
    """
    cleaned_hex = "".join(hexdump.split())
    output = ""

    if custom_range:
        try:
            start, end = map(int, custom_range.split(':'))
            if 1 <= start <= len(cleaned_hex) // 2 and 1 <= end <= len(cleaned_hex) // 2 and start <= end:
                extracted_bytes = [cleaned_hex[i*2:(i+1)*2] for i in range(start - 1, end)]
                output = " ".join(extracted_bytes)
            else:
                output = "Invalid custom range."
        except ValueError:
            output = "Invalid custom range format. Use 'start:end'."
    elif bytes_per_output is not None:
        hex_pairs = [cleaned_hex[i:i+2] for i in range(0, len(cleaned_hex), 2)]
        grouped_bytes = [" ".join(hex_pairs[i:i + bytes_per_output]) for i in range(0, len(hex_pairs), bytes_per_output)]
        output = "\n".join(grouped_bytes)
    else:
        output = f"Cleaned hex= {cleaned_hex}"

    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort and format hexdump data.")
    parser.add_argument("-i", "--hexdump", required=True, help="The hexdump string to process.")
    parser.add_argument("-b", "--bytes", type=int, help="Number of bytes to group in the output.")
    parser.add_argument("-c", "--custom", help="Custom byte range to extract (e.g., '3:4').")

    args = parser.parse_args()

    result = hexdump_sorter(args.hexdump, args.bytes, args.custom)
    print(result)
