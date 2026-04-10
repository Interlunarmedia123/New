# Social Media Content Creator

A simple command-line tool that uses Claude (by Anthropic) to generate social media content for Twitter/X, LinkedIn, and Instagram.

## What it can do

- **Generate posts** from any topic — tailored to each platform's style and length
- **Generate hashtags** for a topic or post
- **Repurpose long-form content** (like a blog post) into short social media posts

---

## Setup (one-time)

### 1. Make sure Python is installed

Open your terminal and run:
```
python --version
```
If you see a version number (e.g. `Python 3.10.0`), you're good. If not, download Python from https://python.org.

### 2. Install the required packages

In your terminal, navigate to this folder:
```
cd social-media-content
```
Then run:
```
pip install -r requirements.txt
```

### 3. Add your Claude API key

1. Get a free API key at https://console.anthropic.com/
2. Copy the example env file:
   ```
   cp .env.example .env
   ```
3. Open the new `.env` file in any text editor and replace `your_api_key_here` with your real key.

---

## How to use it

Run the tool with:
```
python main.py
```

You'll see a menu like this:
```
==================================================
  Social Media Content Creator (powered by Claude)
==================================================

What would you like to do?
  [1] Generate a post from a topic
  [2] Generate hashtags
  [3] Repurpose long-form content for social media
  [4] Exit
```

Just type a number and press Enter, then follow the on-screen prompts.

---

## Example

**Input:** Topic = `"tips for working from home"`

**Output (Twitter/X):**
> Working from home? Set a hard stop time and stick to it. Your couch doesn't need to become your office forever. #RemoteWork #WFH #Productivity

**Output (LinkedIn):**
> Remote work has fundamentally changed how we define the "office." After years of working from home, here are the three habits that made the biggest difference for me...

**Output (Instagram):**
> Home office vibes only! Here are my top tips for staying productive when your living room is also your workplace...
> #WorkFromHome #RemoteLife #HomeOffice #Productivity #WFH
