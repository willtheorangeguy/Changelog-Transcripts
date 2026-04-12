**Jerold Santo:**

What is up, nerds? I'm Jerold and this is Changelog News for the week of Monday, November 24th, 2025.

[Turns out](https://sherwood.news/culture/the-worlds-most-common-passwords-usually-follow-the-same-formula) Gen Z has a weaker top password choice than every older generation except the 80+ crowd. Don't get cocky Boomers, Gen Users, and Millennials. It's pretty rocky for us, too. 

According to [a new report](https://nordpass.com/most-common-passwords-list/), the most commonly leaked Gen Z password is "12345", while the most commonly leaked passwords for the other age groups is "12345**6**" 

This proves that you can be both a winner and a loser at the same time.

Ok, let's get into this week's news.

**Break:**

**Jerold Santo:**

[What is a tech bubble anyway?](https://commoncog.com/what-is-a-tech-bubble/)

Cedric Chin says comparisons of our current AI *maybe-bubble* to the dot-com bubble and the 2008 GFC are limiting:

> First, the 2008 crisis wasn’t a technology bubble. Second, the dot-com bubble was idiosyncratic for a number of reasons, the biggest one being that going public has since become an order-magnitude more difficult...
>
> it shouldn’t come as a surprise that the hottest AI companies today are all private companies, unavailable to the retail investor. That’s different enough from 1999 that it should, I think, give you pause.

Cedric also believes that calling this a bubble or not doesn't really matter. What really matters is, "*what should I do?*" That, of course, depends on whom *you* are and what *you* are trying to accomplish. Leaving the subjective aside, I'm linking up Cedric's post because he provides five bullet points that lay out a pattern we can use to see what might come next.

Unfortunately, each bullet point is too long to inline here and not long enough to summarize in a useful way. So, I'm not going to *"save you a click"* on this one.

**Break:**

**Jerold Santo:**

[The Cloudflare outage, unwrapped](https://blog.cloudflare.com/18-november-2025-outage/)

*Filed Under: "Stories You Most Likely Already Know All About"*

Cloudflare CEO, Matthew Prince, posted an excellently transparent post-mortem of their "significant failures to deliver core network traffic" last week which brought much of the internet to its knees (and our AI agents with it). The details are fascinating. [Murphy's law](https://en.wikipedia.org/wiki/Murphy's_law) was in full effect that day:

> Throwing us off and making us believe this might have been an attack was another apparent symptom we observed: Cloudflare’s status page went down. The status page is hosted completely off Cloudflare’s infrastructure with no dependencies on Cloudflare. While it turned out to be a coincidence, it led some of the team diagnosing the issue to believe that an attacker may be targeting both our systems and our status page.

The smoking gun at the end of this murder mystery was a single line of Rust code which executes a single method: ".unwrap()"

It just so happens that "unwrap", which assumes an operation succeeded and extracts data from its inner value, is considered by many Crustaceans to be one of the language's few foot guns. Cloudflare engineering shot themselves with it. And the internet felt the pain.

**Break:**

**Jerold Santo:**

[A high-performance log viewer for humans](https://github.com/pamburus/hl)

"HL" is a fast, powerful log viewer / processor that converts JSON and loft logs into a clear, human-readable format before we do our own parsing and analysis. It has paging built in, can handle streaming logs, lets you filter by fields, log levels, or timestamps, includes a follow mode, and more.

This isn't the first "log viewer for humans" on the block, but it does stand out from the crowd in their [provided benchmark](https://github.com/pamburus/hl?tab=readme-ov-file#performance) comparing "HL" to alternatives on a 2.3 GB log file. "HL" opened the 6M line log in ~1.1 seconds compared to [logo](https://github.com/ssgreg/hlogf)'s ~8.7 seconds, [Humalog](https://github.com/humanlogio/humanlog)'s ~79 seconds, and [blog](https://github.com/brocode/fblog)'s ~34 seconds.

**Break:**

**Jerold Santo:**

It's now time for sponsored news!

[Give your GitHub Actions a serious speed boost](https://namespace.so)

Your current GitHub Actions setup is doing the job, but it's also taking way longer than it should. Every time you push code, you're watching the spinner on 10+ minute builds. Not fun. Namespace flips the script by giving you infrastructure designed from the ground up for fast builds.

All you have to do is point your existing workflows at Namespace runners instead of the default GitHub-hosted runners, and instantly those 10+ minute builds drop to minutes. Behind the scenes, Namespace is handling incremental caching, parallel execution of independent jobs, and optimized Docker layer caching.

The cost difference is also dramatic. Namespace's model gives you predictable pricing, and they're built for teams that ship constantly. Instead of watching spinners, they're shipping features.

Head to [Namespace.so](https://namespace.so), stop watching spinners, get faster builds, and get more of your time back for real work.

**Break:**

**Jerold Santo:**

[Continuum 93](https://enthusiastguy.itch.io/continuum93)

This is kinda insane...

> Continuum 93 is an emulator of a classic retro computer that never existed before and is designed for retro games programming in native assembly code.

Yes, you heard that correctly. This is a *fantasy* computer emulator, which means it is emulating a computer that never was, but certainly *could* have been, and perhaps *should* have been, but again: it was not. But now it is? My head hurts.

Continuum 93 was recently open sourced, runs on "Windows, Mac, Linux, all 64 bit Raspberry Pi and Steam Deck", and is created by a guy whose handle is "Enthusiast Guy", which is so apropos my headache went away.

**Break:**

**Jerold Santo:**

[Things that aren't doing the thing](https://strangestloop.io/essays/things-that-arent-doing-the-thing)

The only thing that is doing the thing is doing the thing. You already know that. I already know that. But sometimes we need a reminder, don't we? Here's your reminder!

> Making a to-do list for the thing isn't doing the thing.

> Telling people you're going to do the thing isn't doing the thing.

> Fantasizing about all the adoration you'll receive once you do the thing isn't doing the thing.

You get the point, but if you want to drill it in to your head by reading even more things that aren't the thing, click through. Or, stop reading Changelog News and just go do the thing ;)


## 📰 The Classifieds

✨ This is a new segment creating opportunity to share your startup, passion project, opinion, big idea, upcoming event, etc, with your fellow 25k+ readers and 30k+ listeners. Feedback welcome! ✨

- [Shareable Claude Code sessions](https://www.aviator.co/runbooks?utm_source=changelog&utm_medium=content&utm_campaign=q4-2025-changelog-runbooks&utm_term=net-new&utm_content=awareness)
- [Style frame — Type-safe Composable CSS](https://www.styleframe.dev/)
- [AI Requirements software that just works. Battle-proven.](https://storywi.se)
- [Excalibur – Your friendly TypeScript 2D game engine for the web.](https://excaliburjs.com)

👉 *[Book a classified ad for $50](https://forms.gle/yCJirHRCWkdbG5qK6)* 👈

**Break:**

**Jerold Santo:**

That's the news for now, but go and subscribe to the Changelog Newsletter for the full scoop of links worth clicking on. Such as:

- [Building a simple search engine that actually works](https://karboosx.net/post/4eZxhBon/building-a-simple-search-engine-that-actually-works)
- [300+ NPM packages, 27K+ repos infected via fake Bun runtime](https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24)
- [Android can now AirDrop to iPhones](https://blog.google/products/android/quick-share-airdrop/)

Get in on the newsletter at changelog. News

Last week on the pod: Spencer Chang from the alive internet theory and internet sculptures joined me for an interview and Practical AI's Chris Benson was on Changelog & Friends explaining to us what is not a swarm.

Find those in your feed and stay tuned because we have some great episodes coming up! On Wednesday we're joined by **Bill Butler**, a real-life Wikipedia expert, to (figuratively) gaze upon the 8th wonder of the world. And on Friday, our old friend **Lars Wickman** joins us from the west coast of Sweden.

Have a great week! Like, subscribe, and leave us a 5-star review if you dig the show, and I'll talk to you again real soon.
