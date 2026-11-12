from pathlib import Path
from datetime import date
from dotenv import load_dotenv
import anthropic

# Load the API key from the .env file
load_dotenv()

# Read the briefing and the notice from their files
system_prompt = Path("system_prompt.md").read_text(encoding="utf-8")
notice_text = Path("sample_notice.txt").read_text(encoding="utf-8")

# The servicer profile we're testing with
profile = """Servicer profile:
- Institution type: Nonbank servicer
- Portfolio size: More than 5,000 loans"""

# Today's date, so Claude can apply the priority rules
today = date.today().strftime("%B %d, %Y")

# Connect to Claude
client = anthropic.Anthropic()

# Send the briefing, date, profile, and notice to Claude
response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=4000,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": f"Today's date: {today}\n\n{profile}\n\n<document>\n{notice_text}\n</document>",
        }
    ],
)

# Print Claude's answer, skipping the reasoning blocks
for block in response.content:
    if block.type == "text":
        print(block.text)