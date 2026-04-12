**Jerold Santo:**

What is up, nerds? I'm Jerold and this is Changelog News for the week of Monday, February 17th, 2025.

If you listen to our shows, and you haven't [joined](https://changelog.com/community) our (totally free) Zulip community... let's fix that bug! It's always more fun to discuss things you've heard with friends, and the commentary around our recent episodes has been SO GOOD. [See for yourself](https://changelog.zulipchat.com/#narrow/channel/455613-friends) by following the link in the newsletter and sign up today at changelog.com/community

Ok, let's get into the news.

**Break:**

**Jerold Santo:**

[AI is stifling tech adoption](https://vale.rocks/posts/ai-is-stifling-tech-adoption)

Declan Chid low proposes that:

> the advent and integration of AI models into the workflows of developers has stifled the adoption of new and potentially superior technologies due to training data cutoffs and system prompt influence.

I've been worried about this very thing ever since I first realized its possibility during [our conversation](https://changelog.am/28) with Elixir-creator, José Valid, last January (starting at chapter 13: "On long-term relevance"). Declan says:

> I have noticed a bias towards specific technologies in multiple popular models and have noted anecdotally in conversation and online discussion people choosing technology based on how well AI tooling can assist with its usage or implementation.
>
> While it has long been the case that developers have considered documentation and support availability when choosing software, AI’s influence dramatically amplifies this factor in decision-making, often in ways that aren’t immediately apparent and with undisclosed influence.

I'd hate to live in a world where the overwhelming majority of new software projects are written in Python and TypeScript just because LLMs are best at outputting Python and TypeScript...

*(Not that there's anything wrong with that (with Python 😏))*


**Break:**

**Jerold Santo:**

[Leading successful product teams](https://arie.ls/2023/leading-successful-product-teams/)

Ariel Saline shares 17 pieces of advice she's learned about leading successful product teams after two decades in the web industry and 8+ years building design systems.

> Running a design systems team has some minor differences compared to a more traditional product team setup, but there’s still enough overlap that all of these rules can be considered universal and applied to almost any product team out there.

Ariel's entire list rings of wisdom, but the last three items were absolute bangers, IMO:

15. Don’t be afraid to throw things away.
16. Shipped is better than perfect.
17. Be kind.

**Break:**

**Jerold Santo:**

[Wichita is a testament to internet creation](https://arstechnica.com/gadgets/2025/02/new-wikitok-web-app-allows-infinite-tiktok-style-scroll-of-wikipedia/)

Ben Edwards tells the story of Wichita, an "endless Wikipedia feed to fight algorithm addiction", created in the most internet-y way that a thing could be created:

> The original idea for Wichita originated from developer Tyler Anger ton Monday evening when he [tweeted](https://x.com/tylerangert/status/1886560290864533983), "insane project idea: all of Wikipedia on a single, scrollable page." Bloomberg Beta VC James Cham [replied](https://x.com/jamescham), "Even better, an infinitely scrolling Wikipedia page based on whatever you are interested in next?" and Anger [coined](https://x.com/tylerangert/status/1886560560654794930) "Wichita" in a follow-up post.

> Early the next morning, at 12:28 am, writer Grant Latton [quote-tweeted](https://x.com/GrantSlatton/status/1886647932252020984) the Wichita discussion, and that's where Gomal came in. "I saw it from [Latton's] quote retweet," he told Ar's. "I immediately thought, 'Wow I can build an MVP and this could take off.'"

> Gomal started his project at 12:30 am, and with help from AI coding tools like [Anthropic's Claude](https://arstechnica.com/information-technology/2024/06/anthropics-latest-best-ai-model-is-twice-as-fast-and-still-terrible-at-dad-jokes/) and [Cursor](https://www.cursor.com/), he finished a prototype by 2 am and [posted the results](https://x.com/Aizkmusic/status/1886669151516705028) on X. Someone later [announced](https://news.ycombinator.com/item?id=42936723) Wichita on Y Combinator's Hacker News, where it topped the site's list of daily news items.

An idea jumps through five people and multiple LLMs to its creation (and world-wide distribution) in just 90 minutes. We live in trying times, for sure, but we also live in *amazing* times. [/src](https://github.com/IsaacGemal/wikitok)

**Break:**

**Jerold Santo:**

It's now time for Sponsored News!

[Meet the people shaping the future of engineering](https://temporal.io/blog/meet-speakers-shaping-future-of-engineering-replay-25)

Here's Lauren Bennett from Temporal:

> The difference between a backend that hums and one that crumbles under pressure isn’t a lucky break: it’s engineering. The best solutions don’t come from you working in isolation, staring at logs, or fretting over your codebase. They come from people wrestling with real-world scaling problems, learning through failure, and designing for a future that isn’t yet written.

At [Replay 2025](https://replay.temporal.io/), those engineers will take the stage to tell you how they’re pushing workflow orchestration, Durable Execution, and modernization efforts forward. Lauren outlines some of the talks that'll be given, and they look great! Here's a few that caught our attention:

- Building Systems That Can’t Afford to Fail
- Salesforce migrating a monolithic cloud with Temporal
- Resilience, Reliability, and Real-Time Response

> You can read case studies, watch talks online, and even swap war stories on Slack, but nothing replaces being in the room with the minds who’ve already solved the problems you’re facing.

Thanks to Temporal for sponsoring Changelog News and definitely check out Replay '25 by following the link in the newsletter.

**Break:**

**Jerold Santo:**

[Sunsetting "Create React App"](https://react.dev/blog/2025/02/14/sunsetting-create-react-app)

 Matt Carroll and Ricky Hanson from the React team say:

> Today, we’re deprecating Create React App for new apps, and encouraging existing apps to migrate to a framework. We’re also providing docs for when a framework isn’t a good fit for your project, or you prefer to start by building a framework.

Their official stance going forward is you should [start with a framework](https://react.dev/learn/creating-a-react-app) but I do appreciate that they have a page dedicated to how to [build your own framework](https://react.dev/learn/building-a-react-framework), if for no other reason than you can quickly grok all the things frameworks provide out of the box.

**Break:**

**Jerold Santo:**

[Boring tech is mature, not old](https://rubenerd.com/boring-tech-is-mature-not-old/)

Ruben Shade:

> I’ve talked before about how I think NetBSD is “boring”, and that it’s among the highest forms of praise I can give tech as a sysadmin and architect. But I’ve never elaborated why that is.

On this week's upcoming show with Tail Scale co-founder, David Crashaw, Adam thought he might offend David by telling him that Tail Scale has become boring in his eyes. David took that as high praise, as would I!

> Boring tech behaves in predictable ways. It’s a well trodden path others have evaluated, optimized, troubleshooted, and understood. Using tech that has been subjected to all those people hours of use means you’re less likely to run into edge cases, unexpected behaviour, or attributes and features that lack documentation or community knowledge.

Ruben isn't saying there's no room for innovation. His overarching point is that "it pays to make informed decisions, and that often times the understood, reliable, boring tech will get you there over something new, shiny or propped up with marketing spin."

**Break:**

**Jerold Santo:**

That's the news for now, but also scan the companion newsletter to get the links and even more stories worth your attention. Such as: Hector Martin resigning as Asa hi Linux lead, Rust Owl, a tool that visualizes ownership and lifetimes in Rust, and the story of an undergrad who upended a 40-year-old computer science principle...

We had some great episodes last week! Scroll back in your feed for Arun Gupta on fostering open source culture. One listener said:

> Loved the discussion; and I love the 'garden analogy' ending, Arun!

And also for Jimmy Miller on Discovery Coding. AJ Kerrigan liked it enough to call the episode 'beautiful', so that's cool!

We also have some great episodes coming up

**On Wednesday**: David Crashaw joins us to discuss [how he programs with LLMs](https://crawshaw.io/blog/programming-with-llms)

and **On Friday**: Adam and I discuss the news, including [a great post on changing your mind over the years](https://chriskiehl.com/article/thoughts-after-10-years)

Have a great week! Leave us a 5-star review if you dig our work, and I'll talk to you again real soon.
