from pathlib import Path
from datetime import date
from dotenv import load_dotenv
import anthropic

# Load the API key from the .env file
load_dotenv()

# Settings: which document to test, which profile, and how many runs
TEST_FILE = "tests/covid_ifr.txt"
PROFILE = """Servicer profile:
- Institution type: Bank or credit union
- Portfolio size: More than 5,000 loans"""
RUNS = 3

# Read the briefing and the test document
system_prompt = Path("system_prompt.md").read_text(encoding="utf-8")
notice_text = Path(TEST_FILE).read_text(encoding="utf-8")
today = date.today().strftime("%B %d, %Y")

# Create a folder for the results if it doesn't exist yet
results_folder = Path("tests/results")
results_folder.mkdir(exist_ok=True)

client = anthropic.Anthropic()
test_name = Path(TEST_FILE).stem

# Run the same document several times and save each answer
for run in range(1, RUNS + 1):
    print(f"Running {test_name}, run {run} of {RUNS}...")

    response = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=16000,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": f"Today's date: {today}\n\n{PROFILE}\n\n<document>\n{notice_text}\n</document>",
            }
        ],
    )

    # Keep only the answer text, skipping the reasoning blocks
    answer = "".join(block.text for block in response.content if block.type == "text")

    # Warn if the answer was cut off by the length limit
    if response.stop_reason == "max_tokens":
        answer += "\n\n**WARNING: This answer was cut off because it hit the length limit.**"
        print("  WARNING: answer was cut off")

    output_file = results_folder / f"{test_name}_run{run}.md"
    output_file.write_text(answer, encoding="utf-8")
    print(f"  Saved to {output_file}")

print("Done.")