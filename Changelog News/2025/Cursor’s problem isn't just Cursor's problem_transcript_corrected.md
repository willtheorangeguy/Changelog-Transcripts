**Jerold Santo:**

What is up, nerds? I'm Jerold and this is Changelog News for the week of Monday, August 18th, 2025.

The *Hacker of the Week*™️ award goes to Gabor Nikki, who is running [a website](https://vim.gabornyeki.com) off nine Neovim buffers on his old ThinkPad. Yup, Gabor wrote a Neovim plugin in Lua that serves HTTP requests from open buffers. It has zero dependencies and runs faster than Nginx. What have you coded lately? 😉

Ok, let's get into this week's news.

**Break:**

**Jerold Santo:**

[Cursor’s problem isn't just Cursor's problem](https://docs.google.com/document/d/1q3O7niwoxsyfJ5zSx8dgYzipEgBkUqXzLejQQ-PQNWs/mobilebasic)

Based on their usage/growth, which has been astounding, Cursor has product-market fit (PMF), But have they also found business-model–product fit (BMPF)? Most likely not. The discrepancy: subsidies

> Cursor has relied on a subscription model that historically allowed for “unlimited” use. That’s a fixed revenue, variable cost setup. Insurance companies are the canonical example, and they employ actuaries to accurately price risk and segment users. Hypergrowth startups rarely have that muscle. When variable costs scale with intensity of usage, but revenue doesn’t, you’re not selling software, you’re underwriting risk.

The question is whether Cursor can transition to sustainable revenue without losing their users, and since they don't own/control their frontier models, their cost of goods sold (COGS) are pinned to OpenAI and Anthropic. That's a problem. They must change their pricing model to scale with their costs. Then they'll have the answer to the burning question that should nag all VC-backed founders:

> Do I have demand for my product—or for my subsidies?

And a corollary for those of us who use/consume VC-backed dev tools to ask ourselves:

> Do I actually want this product—or just its subsidies?

**Break:**

**Jerold Santo:**

[A .txt file beats every to-do app](https://www.al3rez.com/todo-txt-journey)

Alireza Bashir tried 'em all: Notion, Todoist, Things 3, Omni Focus, Asana, Trello, Any. Do, Tick Tick. He even built his own (unfinished) to-do app once. After years of to-do app hopping, he's back where he started: todo.txt

> My productivity journey started like everyone else’s. I’d devour blog posts about getting things done or spot a cool app and think “this is it, this will finally organize me.” I’d burn hours building the perfect system, creating categories, tags, projects, labels. Setting it up felt like work.
>
> Then reality hits. The app wants $9.99/month. The sync breaks. The company sells out and dies. Or worse - I waste more time managing the system than working.

I gave up on to-do apps many moons ago. In fact, here's me in 2010 documenting my [minimally awesome to-dos](https://jerodsanto.net/2010/12/minimally-awesome-todos/) system that centred around a plaintext file. I don't use that anymore, but I'm still on the plaintext (markdown) kick. I have friends that swear by specific apps and ways they've figured out to use them, but to me, it seems like they spend more time managing their systems than they spend actually *getting stuff done*. Alireza had a similar experience:

> I’m more productive now than when I had all those fancy apps. Turns out the best productivity system is the one you actually use. And I use this one because there’s nothing to figure out. It’s just a list.

**Break:**

**Jerold Santo:**

[Building my offline AI workspace](https://instavm.io/blog/building-my-offline-ai-workspace)

Manish (and friends) wanted everything local – no cloud, no remote execution. 

> With so many LLMs being open source / open weights, shouldn't it be possible to do all that locally? But just local LLM is not enough, we need a truly isolated environment to run code as well.

What they came up with was a combo of [llama](https://ollama.com) (for local models), [assistant](https://github.com/assistant-ui/assistant-ui) (frontend), Apple's [container](https://github.com/apple/container) tool (sandboxed VM runtime), [code runner](https://github.com/instavm/coderunner) (orchestration), and [Playwright](https://playwright.dev/) (browser automation). The end result looks pretty nice!

> This is more than a just an experiment. It's a philosophy shift bringing compute and agency back to your machine. No cloud dependency. No privacy tradeoffs. While the best models will probably be always with the giants, we hope that we will still have local tools which can get our day-to-day work done with the privacy we deserve.

**Break:**

**Jerold Santo:**

It's now time for sponsored news!

[Vibe coding at work](https://www.coderabbit.ai/blog/vibe-coding-because-who-doesnt-love-surprise-technical-debt)

Vibe coding is fun. You’re in flow, ideas are pouring out, code ships fast. But those sessions often come with a side of “surprise” technical debt.

CodeRabbit’s latest post makes the case for vibe coding *with guardrails*. Their AI reviews run in flow — code, review, commit — all inside your IDE. It’s like having a senior engineer pair with you in real-time: flagging bugs, smells, and missed tests before they snowball.

We use CodeRabbit here at Changelog. [Check our PRs](https://github.com/thechangelog/changelog.com/pulls?q=is%3Apr+is%3Aclosed) — it’s our last mile defence against merging bad code... vibed or not.

Learn more at [CodeRabbit.ai](https://www.coderabbit.ai/blog/vibe-coding-because-who-doesnt-love-surprise-technical-debt) and read the blog post by following the link in the newsletter.

**Break:**

**Jerold Santo:**

[A WYSIWYG editor that's just a textarea](https://overtype.dev)

Overhype looks SWEET! The author calls it an "under-engineered solution." I call it a breath of fresh-air. It works by rendering a preview pane behind the textarea and keeping the two elements perfectly aligned.

> It's a rich markdown editor that's really just a textarea. The key insight was that once you solve the alignment challenges, you get everything native textareas provide for free: undo/redo, mobile keyboard, accessibility, and native performance.

Overhype is 45KB total, takes minutes to understand, minutes to customize, and at the end of the day... it's just a textarea. More like this, please!

**Break:**

**Jerold Santo:**

[Bring your .RC files with you when you ssh](https://github.com/cdown/sshrc)

SSR works just like ssh, but it also sources the ~/.SSR on your local computer after logging in remotely. That may not seem like much, but it's actually super cool. 

> You can use this to set environment variables, define functions, and run post-login commands. It's that simple, and it won't impact other users on the server - even if they use SSR too.

This is a killer setup for folks who share a server with multiple users or manage multiple servers and don't want to configure each environment individually. The best part? It's just a shell script and clocks in at less than 100 lines. Simplicity FTW, again!

**Break:**

**Jerold Santo:**

That's the news for now, but go and subscribe to the Changelog Newsletter for the full scoop of links worth clicking on. Such as:

- [Everyone knows what an email address is, right?](https://email.wtf)
- [Tech Debt? I don't believe it exists](https://dadrian.io/blog/posts/tech-debt/)
- [A curated gallery of pricing page designs](https://pricingpages.design/)

Get in on the newsletter at changelog. News

last week on the pod we sat down 

Have a great week! Like, subscribe, and leave us a 5-star review if you dig the show, and I'll talk to you again real soon.
