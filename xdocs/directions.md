Of course. This is a crucial step for a smooth workshop. You are right to distinguish between your account and what a new user will experience.

The best and most direct way for your attendees to get a free API key is through **Google AI Studio**. It's designed for this exact purpose: giving developers and learners quick access.

Here is a step-by-step guide you can provide to your workshop attendees.

-----

### Pre-Workshop Checklist for Attendees

To save time, please ensure you have the following before the workshop begins:

1.  A standard Google Account (like a Gmail account).
2.  A modern web browser (like Chrome, Firefox, or Edge).

-----

### How to Get Your Free Gemini API Key (A 2-Minute Guide)

We will now generate a special key that lets our code talk to Google's AI models. This is free and perfect for our workshop today.

**Step 1: Go to Google AI Studio**

Open your web browser and navigate to:
[**aistudio.google.com**](https://aistudio.google.com)

**Step 2: Sign In**

Sign in using your regular Google Account. You may be asked to agree to the terms of service.

**Step 3: Get Your API Key**

On the AI Studio page, look for a button on the left-hand menu labeled **`<› Get API key`**. Click on it.

**Step 4: Create and Copy Your Key**

A dialog box will appear. Click the button that says **`Create API key`**.

A new key will be generated for you. It's a long string of letters and numbers.

**IMPORTANT:** Copy this key immediately and paste it into a temporary, private place (like a text file on your computer). You will not be able to see the full key again for security reasons.

**Step 5: Use the Key in Your Code**

Now, take the key you just copied and place it in the Python code where indicated:

```python
# The new, recommended way
from google import genai

# --- PASTE YOUR API KEY HERE ---
API_KEY = "YOUR_API_KEY_GOES_HERE" 
# --------------------------------

# Configure the client with your key
client = genai.Client(api_key=API_KEY)

# Now you're ready to use the model!
model = client.get_model('gemini-1.5-flash-latest')
response = model.generate_content("Tell me a fun fact about Python programming.")

print(response.text)
```

You are now all set to continue with the workshop\!

-----

### Important Advice for You as the Instructor

  * **Reassure them it's free:** The key from AI Studio grants access to the Gemini API's generous free tier (e.g., 60 queries per minute), which is more than enough for a workshop. No credit card or billing setup is required.
  * **Security Warning:** Strongly advise your attendees: **"NEVER share your API key publicly.** Do not post it on Slack, Discord, or commit it to a public GitHub repository. Treat it like a password."
  * **Have a Backup Plan:** It's wise to have one or two extra keys you generated yourself. If an attendee gets stuck or has account issues, you can privately message them a key to use just for the workshop so they don't fall behind.