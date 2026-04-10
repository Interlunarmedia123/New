import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

PLATFORMS = {
    "1": "Twitter/X",
    "2": "LinkedIn",
    "3": "Instagram",
    "4": "All platforms",
}

PLATFORM_GUIDELINES = {
    "Twitter/X": "Write a punchy tweet under 280 characters. You may include 1-3 hashtags inline.",
    "LinkedIn": "Write a professional LinkedIn post of 150-300 words in paragraph format. Use a strong opening line.",
    "Instagram": "Write an engaging Instagram caption. Be conversational and expressive. Add 5-10 relevant hashtags at the end on a new line.",
}


def call_claude(system_prompt: str, user_message: str) -> str:
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text


def generate_posts():
    topic = input("\nWhat is the topic or idea for your post? > ").strip()
    if not topic:
        print("No topic entered. Returning to menu.")
        return

    print("\nChoose platform(s):")
    for key, name in PLATFORMS.items():
        print(f"  [{key}] {name}")
    choice = input("Your choice > ").strip()

    if choice not in PLATFORMS:
        print("Invalid choice. Returning to menu.")
        return

    selected = PLATFORMS[choice]
    platforms_to_generate = (
        list(PLATFORM_GUIDELINES.keys()) if selected == "All platforms" else [selected]
    )

    print("\nGenerating your content...\n")
    for platform in platforms_to_generate:
        guideline = PLATFORM_GUIDELINES[platform]
        system = (
            f"You are a skilled social media copywriter. {guideline} "
            "Be creative, authentic, and engaging. Output only the post text, nothing else."
        )
        result = call_claude(system, f"Write a {platform} post about: {topic}")
        print(f"--- {platform} ---")
        print(result)
        print()


def generate_hashtags():
    topic = input("\nEnter a topic or paste your post text to get hashtags > ").strip()
    if not topic:
        print("No input entered. Returning to menu.")
        return

    print("\nGenerating hashtags...\n")
    system = (
        "You are a social media expert. Generate a list of 10-15 relevant, popular hashtags "
        "for the given topic or post. Output only the hashtags separated by spaces, nothing else."
    )
    result = call_claude(system, topic)
    print("--- Suggested Hashtags ---")
    print(result)
    print()


def repurpose_content():
    print("\nPaste your long-form content below (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    content = "\n".join(lines).strip()

    if not content:
        print("No content entered. Returning to menu.")
        return

    print("\nChoose target platform(s):")
    for key, name in PLATFORMS.items():
        print(f"  [{key}] {name}")
    choice = input("Your choice > ").strip()

    if choice not in PLATFORMS:
        print("Invalid choice. Returning to menu.")
        return

    selected = PLATFORMS[choice]
    platforms_to_generate = (
        list(PLATFORM_GUIDELINES.keys()) if selected == "All platforms" else [selected]
    )

    print("\nRepurposing your content...\n")
    for platform in platforms_to_generate:
        guideline = PLATFORM_GUIDELINES[platform]
        system = (
            f"You are a skilled social media copywriter. {guideline} "
            "Repurpose the provided long-form content into a great social media post. "
            "Output only the post text, nothing else."
        )
        result = call_claude(system, f"Repurpose this content for {platform}:\n\n{content}")
        print(f"--- {platform} ---")
        print(result)
        print()


def main():
    print("=" * 50)
    print("  Social Media Content Creator (powered by Claude)")
    print("=" * 50)

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\nERROR: ANTHROPIC_API_KEY not found.")
        print("Please copy .env.example to .env and add your API key.")
        return

    while True:
        print("\nWhat would you like to do?")
        print("  [1] Generate a post from a topic")
        print("  [2] Generate hashtags")
        print("  [3] Repurpose long-form content for social media")
        print("  [4] Exit")

        choice = input("\nYour choice > ").strip()

        if choice == "1":
            generate_posts()
        elif choice == "2":
            generate_hashtags()
        elif choice == "3":
            repurpose_content()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
