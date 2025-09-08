# 🧠 Smart File Organizer

<div align="center">

![Python](https://img.shields.io/badge/Made%20with-Python-%23FFD343?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Project%20Status-Awesome%20AF-brightgreen)
![Files Organized](https://img.shields.io/badge/Files%20Organized-1000%2B%20daily-blue)

**Tired of your messy downloads folder? Me too. Let's fix that together.**

[Features](#-what-it-does) • [Quick Start](#-try-it-now) • [Customize](#-make-it-yours) • [Help Out](#-want-to-help)

![Before and After](https://via.placeholder.com/800x400.png?text=Before:+Chaos++++++After:+Beautiful+Order)

</div>

## 👋 Hey there!

Let's be real - we've all been there. That moment when you need to find a specific file in your downloads folder and it's like trying to find a needle in a haystack. PDFs mixed with images, videos hiding between spreadsheets... it's a mess.

I built this because I was tired of wasting time searching for files. This little Python script has saved me hours of frustration, and now I'm sharing it with you.

## 🎯 What it does

In plain English: it automatically sorts your files into folders based on what they are. 

- **PDFs, Word docs, text files** → go to `Documents`
- **Photos and images** → go to `Images` 
- **Videos** → go to `Videos`
- **Code files** → go to `Code`
- **Anything else** → goes to `Misc` (so nothing gets lost)

It's like having a super-organized friend who comes over and cleans up your digital clutter while you sleep.

## 🚀 Try it now

### Step 1: Grab the code
```bash
# Copy this to your terminal
git clone https://github.com/harshbhimra01/Smart_File_Organizer
cd smart-file-organizer
```

### Step 2: Test it safely first
```python
# Open the file and change this line to point to a TEST folder:
source_dir = "/path/to/test/folder"  # ← Change this to a test folder!
```

### Step 3: Run it!
```bash
python organizer.py
```

Watch the magic happen. Your files will organize themselves. No kidding.

## ⚙️ Make it your own

The default settings work great, but you might want to tweak things:

```python
# Want to add support for Photoshop files? Easy!
extension_to_folder = {
    '.psd': 'Design Files',  # ← Add this line
    '.ai': 'Design Files',   # ← And this one
    # ... keep the rest of your existing extensions
}

# Want to change where something goes?
extension_to_folder = {
    '.mp3': 'Music',        # Changed from 'Audio'
    '.wav': 'Music',        # Also changed
    # ... you get the idea
}
```

## 🛡️ But is it safe?

**Heck yes.** I built this to be safe:

- It only moves files - never deletes anything
- You can test it first with a dummy folder
- It tells you exactly what it's doing every step of the way
- If something goes wrong (it won't), your files are still right there

## 🤝 Want to help?

Found a bug? Have an idea to make it better? Awesome! Here's how you can help:

1. **Try it out** - The best help is testing it and telling me what works and what doesn't
2. **Add support for more file types** - Know a file format I missed? Add it!
3. **Make it prettier** - If you're good at making things look nice, help with the documentation
4. **Tell your friends** - Seriously, the more people use this, the better it gets

No pressure though - even if you just use it and enjoy it, that makes me happy.

## 📝 License

Do whatever you want with this! MIT license means you can use it, change it, share it - no strings attached.

## 🎊 Final words

I built this because I needed it. Now I'm sharing it because maybe you need it too. It's not the fanciest tool in the world, but it works and it might just save you some headache.

Give it a try. What's the worst that could happen? (Spoiler: your files will become organized)

---

**Happy organizing!** 🎉

*– [Harsh Bhimra]*

---

<div align="center">

*Made with ❤️ and probably too much coffee*

![Lines of code](https://img.shields.io/badge/Lines%20of%20code-157%20(and%20counting)-blue)
![Bugs fixed](https://img.shields.io/badge/Bugs%20squished-12%20and%20counting-red)

</div>

---
