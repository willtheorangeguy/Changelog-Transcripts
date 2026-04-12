**Jerold Santo:**

What is up, nerds? I'm Jerold and this is Changelog News for the week of Monday, March 18th 2024

Did you know that poet Shel Silverstein "predicted" ChatGPT all the way back in 1981?! I present to you, The Homework Machine:

> The Homework Machine,
> Oh, the Homework Machine,
> Most perfect
> contraption that's ever been seen.
> Just put in your homework, then drop in a dime,
> Snap on the switch, and in ten seconds' time,
> Your homework comes out, quick and clean as can be.
> Here it is— 'nine plus four?' and the answer is 'three.'
> Three?
> Oh me. . .
> I guess it's not as perfect
> As I thought it would be.

Ok, let's get into the news.

**Break:**

**Jerold Santo:**

[No Maintenance Intended](https://unmaintained.tech)

 When you really think about it, [open source is a gift to the world](https://changelog.fm/444). Some gifts are ongoing efforts, sure. But other gifts are just one-offs. You build something, you give it away, and that's it. You have no intention of improving it, maintaining it, or even looking at it again. That's totally fine! But if/when that's the case, it's a good idea to clearly communicate that expectation. Enter the "No Maintenance Intended" badge. Add the badge to your hobby project and send folks to this message when they follow the link:

> If you’re here, that likely means a project linked you here.
> Thanks so much for being interested in that project!
> Open Source is rewarding- but it can also be exhausting.
> The linking project’s code is provided as-is, and is not actively maintained.
> The author(s) of that project invite you to peruse their code and even use it in your next project, provided you follow the included license!
> No guarantee of support for the code is provided, and there is no promise that pull requests will be reviewed or merged.
> It’s open source, so forking is allowed; just be sure to give credit where it’s due!

In a somewhat ironic twist, the "No Maintenance Intended" badge _project_ IS maintained and is [on GitHub](https://github.com/potch/unmaintained.tech).

**Break:**

**Jerold Santo:**

[What I learned from looking at 900 most popular open source AI tools](https://huyenchip.com//2024/03/14/ai-oss.html)

Four years ago, Chip Hu yen did an analysis of the open source ML ecosystem. Since then, the landscape has changed, so she revisited the topic. This time, she focused exclusively on the stack around foundation models.

This is a #longread, so I'll just list her personal favourite ideas for you here and let you take the deep-dive on your own time:

- Batch inference optimization: [Flex Gen](https://github.com/FMInference/FlexGen), [llama.cpp](https://github.com/ggerganov/llama.cpp/pull/1375)
- Faster decoder with techniques such as [Medusa](https://github.com/FasterDecoding/Medusa), [LookaheadDecoding](https://github.com/hao-ai-lab/LookaheadDecoding)
- Model merging: [merge kit](https://github.com/cg123/mergekit)
- Constrained sampling: [outlines](https://github.com/outlines-dev), [guidance](https://github.com/guidance-ai/guidance), [Slang](https://github.com/sgl-project/sglang)
- Seemingly niche tools that solve one problem really well, such as [minors](https://github.com/arogozhnikov/einops) and [safe tensors](https://github.com/huggingface/safetensors).

You can find most of these on her [cool-LLM-repos](https://github.com/stars/chiphuyen/lists/cool-llm-repos) list on GitHub.

**Break:**

**Jerold Santo:**

It's now time for Sponsored News!

If you are experiencing slowdowns in your application due to excessive Joins and lengthy query durations, it might be time to re-evaluate your database. Consider the power of a Graph database.

Graph databases let you model data the way it looks in the real world, instead of forcing it into the confines of traditional row and column structures.

Move beyond the limitations of relational databases for tasks they aren’t built to handle. Whether it’s managing intricate supply chains, detecting fraud, conducting real-time analytics, or powering Gena applications, graph technology excels in scenarios rich with interconnected data.

Neo4j offers the flexibility to develop using your preferred programming languages and connect via any driver, ensuring seamless integration with your existing technology stack.

People are solving some of the world’s biggest problems with graphs… Now it’s your turn.

Begin your journey at Neo4j.com/developer

Once again that's N-e-o-4-j.com/developer.

**Break:**

**Jerold Santo:**

[Laid-off techies struggle to find jobs with cuts at highest since 2001](https://www.cnbc.com/2024/03/15/laid-off-techies-struggle-to-find-jobs-with-cuts-at-highest-since-2001.html)

Alex Killer, writing for CNBC:

> Since the start of the year, more than 50,000 workers have been laid off from over 200 tech companies, according to tracking website Layoffs.FYI. It’s a continuation of the predominant theme of 2023, when more than 260,000 workers across nearly 1,200 tech companies lost their jobs.
>
> Alphabet, Amazon, Meta and Microsoft have all taken part in the downsizing this year, along with eBay, Unity Software, SAP and Cisco.

Rolling in to the new year, it seemed like sentiments were shifting positive again, but what momentum we had seems to have dried up. Adding to the layoff-based trepidation is the pending code gen AI "takeover", of which [Devin](https://www.cognition-labs.com/introducing-devin) is the newest poster child. As DHH wrote on the subject, [developers are on edge](https://world.hey.com/dhh/developers-are-on-edge-4dfcf9c1). But I'll echo his concluding words, because they're as good as any I've got on the matter:

> So while it's hard to do, it's useless to worry. The Future is out of your hands and out of your control. No profession has ever successfully resisted automation or redundancy in the face of technological advancement over the long term. Screaming at Devin will only distract you from enjoying the last glorious years of a golden run.

**Break:**

**Jerold Santo:**

[Table is a Postgres-Airtable fusion](https://github.com/teableio/teable)

> Table is a superfast, real-time, professional, developer friendly, no-code database built on Postgres. It uses a simple, spreadsheet-like interface to create complex enterprise-level database applications. Unlock efficient app development with no-code, free from the hurdles of data security and scalability.

Do you like the idea of Airtable, but would rather it is self-hosted and actually just Postgres under the hood? I sure do.

**Break:**

**Jerold Santo:**

[Announcing Target’s Open Source Fund](https://tech.target.com/blog/open source-fund)

**Break:**

**Jerold Santo:**

Brian Muenzenmeyer, on Target's tech blog:

> It's no secret that an engaged open source team yields transformative, innovative, and collaborative outcomes. As we looked to discover more ways to engage our team in open source, the success of Sentry's and Microsoft's open source fund efforts inspired us to pursue a similar program. Our efforts today, along with sustained and empowered upstream engagement, aim to strengthen the open source movement, reduce maintainer burnout, and normalize corporate contributions back into the ecosystem. We learned a lot from our first round and look forward to iterating with our community on future rounds.

The good news is that Target has _seen the light_ and is now donating to five open source projects selected through their process. Kudos to them for that!

The bad news is their 2024 donation budget is $12,500, which will hopefully move the needle for the projects selected, but doesn't seem like much from a publicly traded company with a market cap of ~$75 billion...

**Break:**

**Jerold Santo:**

That's the news for now, but also scan the companion newsletter, link in the show notes, which includes more awesome stories like the POSSE Pulse, Marker, an open source desktop app for Markdown editing, and more.

We have some _awesome_ podcast episodes coming your way later this week: Kris Moore talking True NAS and [the end of the FreeBSD version](https://go.theregister.com/feed/www.theregister.com/2024/03/18/truenas_abandons_freebsd/) and Cameron Sea from last year's [mainframes are still a big thing](https://changelog.fm/524)!

Have a great week, **leave us a 5-start review** if you dig our work q & I'll talk to you again real soon. 💚
