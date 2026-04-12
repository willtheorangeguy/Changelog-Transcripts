**Jerold Santo:**

What is up, nerds? I'm Jerold and this is Changelog News for the week of Monday, May 12th, 2025.

Did you know that [Claude's system prompt](https://github.com/asgeirtj/system_prompts_leaks/blob/main/claude.txt) is over 24k tokens?! That's some serious prompt engineering. It's actually kind of fun to read, especially if you imagine Claude standing in front of the mirror, giving itself a pep talk before work:

"Claude enjoys helping humans and sees its role as an intelligent and kind assistant."
"Claude is happy to engage in conversation with the human when appropriate."
"Claude often illustrates difficult concepts or ideas with relevant examples."
"Claude does not provide information that could be used to make chemical or biological or nuclear weapons"

Now go get 'em, you brilliant golden retriever on acid 😏

Ok, let's get into the news.

**Break:**

**Jerold Santo:**

[A critical look at MCP](https://raz.sh/blog/2025-05-02_a_critical_look_at_mcp)

Rasmus Hold is astonished by the "apparent lack of mature engineering practices" he sees as all the major players roll out Model Context Protocol servers at a blistering pace.

> All the major players spend billions of dollars on training and tuning their models, only to turn around and, from what I can tell, have an intern write the documentation, providing subpar SDKs and very little in terms of implementation guidance.
> 
> This trend seems to have continued with MCP, resulting in some very strange design decisions, poor documentation, and an even worse specification of the actual protocols.

His conclusion after diving deep into his own implementation of the protocol in Go, Rasmus was gobsmacked by what he found.

> I don't know, just kind of feel sad about it all... It seems like the industry is peeing their pants at the moment ― it feels great now, but it's going to be hard to deal with later.

If peeing your pants is cool, consider the tech industry Miles Davis. [(src)](https://www.youtube.com/watch?v=siCNdfH9U40)

**Break:**

**Jerold Santo:**

[Strongly Typed](https://www.stefanjudis.com/blog/stringly-typed/)

I learned a new software development term from Stefan Judi's who learned it from Scott Hansel man, who describes "strongly typed" as follows:

> \[whenever\] you are passing strings around when a better type exists.

In a language like TypeScript, this is rare in first party code. But when dealing with OPC (other people's code) via an API, you're often still stuck with strongly typed things. This makes Stefan mad:

> After building all these Spas connecting to APIs being maintained by different teams, I've never considered it to be a huge problem, but now that I have a name for this pattern, "strongly typed" interfaces started to bother me.
>
> I realize that I want type safety over the network and I don't want to deal with "strongly typed" apps at all. I want all the types!

Whether you agree with Stefan or not (I tend not to), the term itself might prove useful to you. And if you heard it here first, prepend me to the list of people you learned it from. Then tell a friend and get your name prepended to the list too. 😎

**Break:**

**Jerold Santo:**

[The curse of knowing how](https://notashelf.dev/posts/curse-of-knowing)

RAF beautifully describes the plight of the enlightened who don't just use computers, but have the ability to program them:

> Before I could program, broken software was frustrating but ignorable. For years, I’ve simply “used” a computer, as a consumer. I was what companies were concerned with tricking into buying their products, or subscribing to their services. Not the technical geek that they prefer to avoid with their software releases, or banning from their games based on an OS.
>
> Now it has become *provocative*. I can see the patterns that I wish I couldn’t, find oversights that I can attribute to a certain understanding (or the lack thereof) of a certain concept and I can hear what has been echoing in the head of the computer illiterate person who conjured the program I have to debug.

This is problematic for a bunch of reasons. One of which, as RAF states, is that pesky thing called entropy:

> Software doesn’t stay solved. Every solution you write starts to rot the moment it exists. Not now, not later, but eventually. Libraries deprecate. APIs change. Performance regressions creep in. Your once-perfect tool breaks silently because lib foo.so is now lib foo.so.2.

Sadly, just because we can fix computers, we can't fix *everything*. Even with computers. So what's a dev to do?

> After the excitement. After the obsession. After the burnout. I’m trying to let things stay a little broken. Because I’ve realized I don’t want to fix everything. I just want to feel OK in a world that often isn’t. I can fix something, but not everything.
>
> You learn how to program. You learn how to fix things. But the hardest thing you’ll ever learn is when to leave them broken.
>
> And maybe that’s the most human skill of all.

**Break:**

**Jerold Santo:**

It's now time for sponsored news!

[Terence Lee shares his thoughts on the next generation of Heroku](https://blog.heroku.com/planting-new-platform-roots-cloud-native-fir?utm_source=changelog&utm_medium=newsletter&utm_campaign=changelog-news)

Adam had a chance to sit down with Terence Lee to talk about what's coming for the next generation of Heroku being built on open source standards. Here's what Terence had to say.

**Break:**

**Jerold Santo:**

[The open source Cursor alternative](https://github.com/voideditor/void)

Welcome to Void. A fork of VS Code (everything is these days) to use AI agents on your codebase, checkpoint and visualize changes, and bring any model or host locally. You know, a lot like Cursor. Except it's not Cursor. Void is entirely open source, and Void sends messages directly to providers without retaining your data. [Here's the roadmap](https://github.com/orgs/voideditor/projects/2).

Void is also, strangely enough, backed by Y Combinator. So while it's all open / free / Sumbawa *today*, something's got to give. I don't know what, and I don't know when, but I do know there will be more to Void's story that we don't know yet.

**Break:**

**Jerold Santo:**

[React Jam is back!](http://reactjam.com/)

If you’re a React developer (or a game dev looking to try something a little different) check out the 6th edition of [React Jam](https://reactjam.com). It’s a 10-day online event **starting May 16th** where devs build games using, you guessed it, React.

Sure, React isn’t the go-to tool for game dev, but that's the fun / challenge! Past entries have included everything from simple board games to impressive 3D stuff using [react-three-fibre](https://r3f.docs.pmnd.rs/getting-started/introduction).

It's all fun and games (literally), but there are also **cash prizes up for grabs**. Oh, and I'll be judging once again, so don't you *dare* try to bribe me with 5-star reviews in every podcast directory. Don't. Even. Try. 😉

**Break:**

**Jerold Santo:**

That's the news for now, but go and subscribe to the Changelog Newsletter for the full scoop of links worth clicking on. Such as:

- [Our Slack is dead. Long live Zulip!](https://changelog.com/posts/our-slack-is-dead-long-live-zulip)
- [The Open Source Maintenance Fee](https://robmensching.com/blog/posts/2025/02/26/introducing-the-open source-maintenance-fee/)
- [The magic of software](https://moxie.org/2024/09/23/a-good-engineer.html)

Get in on the newsletter at changelog.com/news

This week on the pod:

**Wednesday**: Derek Collision from Nadia talking NATO vs the CNCF
**Friday**: Our award-worthy #define [game show](https://changelog.com/topic/games) returns with mystery guests

Have a great week! Like, subscribe, and leave us a 5-star review if you dig the show, and I'll talk to you again real soon.