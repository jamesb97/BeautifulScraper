import anthropic
import sys

client = anthropic.Anthropic()

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python claude.py arg1 arg2")
    sys.exit(1)

input_variable = sys.argv[1] #query string

try:
    temp_variable = float(sys.argv[2]) #temperature (how creative the AI will be 0.1-1, 1 being most creative)
except ValueError:
    print("Error: Temperature must be a valid number between 0.0 and 1.0")
    sys.exit(1)

# Validate temperature range
if not (0.0 <= temp_variable <= 1.0):
    print("Error: Temperature must be between 0.0 and 1.0")
    sys.exit(1)

print("Input: ", input_variable)
print("Temperature: ", temp_variable)

try:
    with client.messages.stream(
        max_tokens=1024,
        temperature=temp_variable,
        system="You're an advanced AI assistant here to help me in anything I need.",
        messages=[
            {
                "role": "user",
                "content": input_variable
            },
            # {
            #     "role": "assistant",
                # "content": "Here is the most professional approach:" # This is a prompt to help start the AI answers, uncomment to use
            # }
        ],
        model="claude-3-opus-20240229",
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
except anthropic.AuthenticationError:
    print("\nError: Authentication failed. Please check your ANTHROPIC_API_KEY environment variable.", file=sys.stderr)
    sys.exit(1)
except anthropic.RateLimitError:
    print("\nError: Rate limit exceeded. Please wait a moment and try again.", file=sys.stderr)
    sys.exit(1)
except anthropic.APIError as e:
    print(f"\nError: Anthropic API error: {e}", file=sys.stderr)
    sys.exit(1)
except KeyboardInterrupt:
    print("\n\nInterrupted by user.", file=sys.stderr)
    sys.exit(130)
except Exception as e:
    print(f"\nError: Unexpected error occurred: {e}", file=sys.stderr)
    sys.exit(1)