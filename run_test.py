from pathlib import Path
from datetime import date
from dotenv import load_dotenv
import anthropic

# Load the API key from the .env file
load_dotenv()

# Settings: which documents and profiles to test, how many runs, and a version label
PROFILES = {
    "nonbank": "Servicer profile:\n- Institution type: Nonbank servicer\n- Portfolio size: More than 5,000 loans",
    "bank": "Servicer profile:\n- Institution type: Bank or credit union\n- Portfolio size: More than 5,000 loans",
}
TESTS = [
    ("tests/covid_ifr.txt", "bank"),
    ("tests/nonbank_registry.txt", "nonbank"),
    ("tests/nonbank_registry.txt", "bank"),
]
RUNS = 1
VERSION = "v2"

# Read the briefing
system_prompt = Path("system_prompt.md").read_text(encoding="utf-8")
today = date.today().strftime("%B %d, %Y")

# Create a folder for the results if it doesn't exist yet
results_folder = Path("tests/results")
results_folder.mkdir(exist_ok=True)

client = anthropic.Anthropic()

# Run each document and profile combination
for test_file, label in TESTS:
    notice_text = Path(test_file).read_text(encoding="utf-8")
    test_name = Path(test_file).stem
    profile = PROFILES[label]

    for run in range(1, RUNS + 1):
        print(f"Running {test_name}, {label} profile, {VERSION}, run {run} of {RUNS}...")

        response = client.messages.create(
            model="claude-sonnet-5-5",
            max_tokens=16000,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": f"Today's date: {today}\n\n{profile}\n\n<document>\n{notice_text}\n</document>",
                }
            ],
        )

        # Keep only the answer text, skipping the reasoning blocks
        answer = "".join(block.text for block in response.content if block.type == "text")

        # Warn if the answer was cut off by the length limit
        if response.stop_reason == "max_tokens":
            answer += "\n\n**WARNING: This answer was cut off because it hit the length limit.**"
            print("  WARNING: answer was cut off")

        output_file = results_folder / f"{test_name}_{label}_{VERSION}_run{run}.md"
        output_file.write_text(answer, encoding="utf-8")
        print(f"  Saved to {output_file}")

print("Done.")