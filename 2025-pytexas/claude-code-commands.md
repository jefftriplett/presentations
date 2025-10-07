# Claude Code Commands & Features

## Essential Commands

### `/init` - Initialize Project Context
Intelligently analyzes your project and adds relevant files/directories to context automatically.

**Usage:**
```bash
/init
```

**When to use:**
- Starting work on a new project
- Let Claude discover project structure automatically
- Faster than manually adding directories
- Claude reads README, package files, config files

**What it does:**
- Scans project structure
- Identifies important files
- Adds relevant context automatically
- Understands framework patterns (Django, FastAPI, etc.)

**Example:**
```bash
/init
# Claude automatically finds and reads:
# - README.md
# - pyproject.toml / package.json
# - src/ or app/ directories
# - Configuration files
```

---

### `/add-dir` - Add Directory Context
Adds an entire directory to the conversation context, allowing Claude to see all files within it.

**Usage:**
```bash
/add-dir path/to/directory
```

**When to use:**
- Starting work on a new project
- Need Claude to understand entire codebase structure
- Working across multiple related files
- Want to give Claude full project visibility

**Example:**
```bash
/add-dir src/
/add-dir tests/
```

---

### `/clear` - Clear Conversation
Clears the current conversation history and starts fresh.

**Usage:**
```bash
/clear
```

**When to use:**
- Switching to a completely different task
- Conversation context is getting too large
- Need to reset and start over
- Want to reduce token usage

**Note:** This removes all conversation history but doesn't affect your files or code changes.

---

### `/context` - View Current Context ⭐ NEW
Shows what files, directories, and information Claude currently has in its context.

**Usage:**
```bash
/context
```

**When to use:**
- Check what Claude can currently see
- Verify if files/directories were added correctly
- Understand why Claude might be missing information
- Debug context issues

**Output shows:**
- Added directories
- Individual files in context
- Current working directory
- Memory entries (if any)

**Note:** This is a new command that provides visibility into Claude's working context.

---

### `/rewind` - Rewind Conversation ⭐ NEW
Rewinds the conversation to a previous state, undoing recent exchanges.

**Usage:**
```bash
/rewind
/rewind 3  # Rewind 3 exchanges
```

**When to use:**
- Claude made changes you want to undo
- Conversation went in wrong direction
- Want to try a different approach
- Made a mistake in your prompt

**What it does:**
- Removes recent conversation exchanges
- Restores previous conversation state
- Keeps file changes visible in git
- Allows you to try alternative approaches

**Example Workflow:**
```bash
# Claude makes unwanted changes
/rewind

# Or rewind multiple exchanges
/rewind 5

# Then try again with better prompt
"Actually, let's use a different approach..."
```

**Note:** File changes are still visible in your git history/diff, so you can review what was changed even after rewinding.

---

## Memory Feature

### `# ` - Add to Local Memory
Use `#` followed by a space to make notes that Claude can add to your local memory.

**How it works:**
1. You write a note starting with `# `
2. Claude reads your note
3. Claude decides if it should be saved to memory
4. If saved, it persists across all future conversations
5. Memory is stored locally on your machine

**Syntax:**
```bash
# [your preference, fact, or instruction]
```

**Examples:**
```bash
# I prefer pytest with function-based tests over unittest class-based tests
# Use Tailwind CSS for all styling
# This project uses uv for dependency management
# Always run tests before committing
# Format code with ruff before committing
```

**Key Benefits:**
- Memories persist across all conversations
- No need to repeat preferences
- Claude learns your coding style
- Consistent behavior across projects
- Stored locally, not in the cloud
- Can be project-specific or global

**Important Notes:**
- Claude interprets your `# ` notes and decides what to remember
- Not every `# ` note becomes a memory (Claude uses judgment)
- Memories are stored locally on your machine
- Use clear, actionable statements for best results

**Best Practices:**
- Be specific and clear
- Use early in a project
- Document coding preferences
- Include testing preferences
- Note deployment requirements
- Specify formatting rules

**View Memories:**
Use `/context` to see all active memories

**Remove Memories:**
Ask Claude to forget specific items, or manage through Claude Code settings

---

## Workflow Tips

### Effective Context Management
1. Start with `/init` or `/add-dir` for project overview
2. Use `/context` to verify what's loaded
3. Create `# ` notes for preferences that should be remembered
4. Use `/clear` when switching tasks
5. Use `/rewind` to undo unwanted changes

**📚 Learn More:**
For a comprehensive guide on context management best practices, see:
https://www.anthropic.com/news/context-management

This guide covers:
- How context windows work
- Best practices for managing context
- Tips for optimizing Claude Code performance
- Strategies for large codebases

### Example Workflow
```bash
# Start new project (quick way)
/init
# Use Django 5.1 patterns
# Prefer function-based views over class-based views

# OR manual way
/clear
/add-dir src/
/add-dir tests/

# Set preferences
# Always include docstrings

# Verify context
/context

# Start coding
"Add a new user profile view with tests"

# If Claude goes wrong direction
/rewind
"Actually, use a different approach..."
```

---

## CLAUDE.md Integration

While not a command, `CLAUDE.md` works alongside these features:

**CLAUDE.md file:**
- Project-level instructions
- Lives in repository root
- Checked into version control
- Shared with team

**`# ` Memory notes:**
- Personal preferences
- Per-user settings
- Stored locally on your machine
- Not in version control
- Specific to your workflow

**Best practice:** Use both together
- `CLAUDE.md` for team standards
- `# ` notes for personal preferences
