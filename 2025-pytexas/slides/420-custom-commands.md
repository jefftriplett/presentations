## Slash Commands

`/init` - lets Claude Code scan your project and create a `CLAUDE.md` (memory)
`/clear` - will clear your working context 
`/context` - insight into what is in Claude's context and how full it is
`/exit` - exits Claude Code
`#` - adds a memory to your `CLAUDE.md` file

--- 

## 🎯 The Archery Analogy

Does our prompt take us in the direction we want to go?

---

## Custom Slash Commands

- Create custom prompts for repeated tasks
- Basic but highly extensible
- Easy to customize for your workflow
- Makes routine tasks faster

---

## `/clean_filler_words`

```shell
➜ cat ~/.claude/commands/clean_filler_words.md

Please review the following text and remove filler words like 'um,' 'uh,' and any unnecessary repetitions. 
Keep the sentences clear and concise.

# accessible as "/clean_filler_words" in Claude Code...
```
