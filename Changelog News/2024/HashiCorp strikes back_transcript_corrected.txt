**Jerold Santo:**

What is up, nerds? I'm Jerold and this is Changelog News for the week of Monday, April 8th 2024

Mates Freida wrote a very nice comment on Spotify about our [undercover generalist](https://changelog.com/friends/37) episode, but since approximately zero people read those, I figured why not give it a boost?

> Amazing episode, this is the kind of content that makes me open Spotify twice a week and come here. To hear from real developers out there making real stuff. Keep them coming Changelog.

Thanks, Mates! Ok, let's get into the news.

**Break:**

**Jerold Santo:**

[HashiCorp strikes back](https://www.linkedin.com/posts/opentofuorg_opentofu-project-was-recently-made-aware-activity-7182147077496344576-jsDQ/)

On April 3rd, Matt Away published a piece for InfoWorld titled [Open Tofu may be showing us the wrong way to fork](https://www.infoworld.com/article/3714980/opentofu-may-be-showing-us-the-wrong-way-to-fork.html). In it, he says:

> that Open Tofu may have illegally taken HashiCorp’s code to keep pace. At least, it’s hard to avoid that conclusion, perusing Open Tofu’s GitHub repositories and comparing them to HashiCorp’s.

The code in question is a new feature in Terraform 1.7 that also landed in Open Tofu as the fork maintainers work to maintain parity. Away claimed:

> Open Tofu took this BUS-licensed HashiCorp code, removed the headers, and tried to instead relicense it under the Mozilla Public License (MPL 2.0).

As a beleaguered boxer might say, "Them's is fighting words." So, it naturally prompted many armchair software copyright lawyers to analyze the code in question and determine whether it was actually copy pasta. Smart people have landed on either side of this issue. [Dan Loren](https://www.linkedin.com/in/danlorenc/) from Chain Guard says:

> I did my own audit and the samples bear no resemblance despite implementing similar functionality, which is honestly hard to do in Go where there are so few ways to do things. I can't possibly see any validity to this claim.

Meanwhile, [Joe Duffy](https://twitter.com/funcOfJoe/status/1776479584613171288) from Plum concluded:

> There are three major kinds of taint, from worst to least bad
>
> 1. Copied the code directly
> 2. Read the source and was influenced by it
> 3. Copied the functionality
>
> I’ve seen this game enough to know that if the file, function, and variable names, plus non-zero number of statements, match, you’ve probably got at least level 2 (if not level 1). And that’s a problem. That’s pretty clearly true of at least remove_statement.go.

Away later issued [this statement](https://twitter.com/mjasay/status/1776635226124632423) about his article:

> I regret how strongly I expressed myself (force of habit 😬), but grateful for those who expressed support against mob dog piling. Two are execs my post put under fire. They didn't agree w/ my conclusions but responded w/ kindness. They're the kind of OSS community I want to join

A few days later, Open Tofu posted this on their LinkedIn page:

> Open Tofu Project was recently made aware of a letter by HashiCorp’s lawyers, alleging that Open Tofu was not respecting the terms of its BSL license governing its Terraform codebase. Open Tofu vehemently disagrees with any suggestion that it misappropriated, mis-sourced, or otherwise misused HashiCorp’s BSL code. Indeed, it seems that HashiCorp may be conflating code that it had previously been open sourced under the MPL and more recently developed code it published under the BSL. Open Tofu’s maintainers have investigated this matter, and intends to issue a written response providing a more detailed explanation of its position in the coming days.

I'm excited to read Open Tofu's written response, but I have a feeling it's only going to get uglier from here. If I'm running the Open Tofu project, I'd be seriously considering a change in strategy from "feature parity" to "differentiation" from now on...

**Break:**

**Jerold Santo:**

[Polar is a creator platform for developers](https://polar.sh)

Polar is like Patreon, but tailored to software creators. Their tagline is, "get paid coding on your passion" and, I have to say, that's a compelling proposition...

They're "just getting started", but the current suite enables maintainers to offer: exclusive posts & newsletters, access to private GitHub repos, Discord invites & "Sponsorship 2.0" (logos on your Readies). There are a few things that are interesting to me about this:

1. Zero fixed costs (5% rev share + Stripe fees)
2. Issue funding and reward splits
3. Mitchell Hashimoto joined on as an advisor

Watch this space. You know I will.

**Break:**

**Jerold Santo:**

It's now time for Sponsored News!

[Rethinking Microservices](https://www.synadia.com/screencasts/rethinking-microservices)

In the linked video, Nadia's Jeremy Seen addresses the current state of overwhelm when building microservice architectures, and how a technology like NATS.io can help solve many of the current requirements for microservices within a single piece of infrastructure. Here's a sample.

**Jeremy Seen:**

Clip from [Rethinking Microservices](https://www.synadia.com/screencasts/rethinking-microservices)

**Jerold Santo:**

Watch the whole thing by following the link in the chapter data and companion newsletter, and thanks to Nadia for sponsoring Changelog News.

**Break:**

**Jerold Santo:**

[Releasing Common Corpus](https://huggingface.co/blog/Pclanglais/common-corpus)

Pierre-Carl Langland, announcing the release of [Common Corpus](https://huggingface.co/collections/PleIAs/common-corpus-65d46e3ea3980fdcd66a5613) on Hugging Face (March 20th, 2024)

> Contrary to what most large AI companies claim, the release of Common Corpus aims to show it is possible to train Large Language Model on fully open and reproducible corpus, without using copyright content. This is only an initial part of what we have collected so far, in part due to the lengthy process of copyright duration verification. In the following weeks and months, we’ll continue to publish many additional datasets also coming from other open sources, such as open data or open science.

More info about this massive dataset:

- Common Corpus is the largest public domain dataset released for training LLMs.
- Common Corpus includes 500 billion words from a wide diversity of cultural heritage initiatives.
- Common Corpus is multilingual and the largest corpus to date in English, French, Dutch, Spanish, German and Italian.
- Common Corpus shows it is possible to train fully open LLMs on sources without copyright concerns.

**Break:**

**Jerold Santo:**

[Loki is an open source tool for fact verification](https://github.com/Libr-AI/OpenFactVerification)

This Python-based tool is designed to automate the process of verifying factuality. Its list of components helps explain how it does what it does:

- **Decomposer**: Breaks down extensive texts into digestible, independent claims, setting the stage for detailed analysis.
- **Check worthy**: Assesses each claim's potential significance, filtering out vague or ambiguous statements to focus on those that truly matter.
- **Query Generator**: Transforms check-worthy claims into precise queries, ready to navigate the vast expanse of the internet in search of truth.
- **Evidence Crawler**: Ventures into the digital realm, retrieving relevant evidence that forms the foundation of informed verification.
- **Claim Verify**: Examines the gathered evidence, determining the veracity of each claim to uphold the integrity of information.

Put all that together and what you have is a python script where you can run `python factcheck.py --modal string --input "Loki is the God of Mischief"` and Loki will go out there and verify that for you.

**Break:**

**Jerold Santo:**

That is the news for now, but give this episodes' companion newsletter a scan too for more stories, including Cory Doctorow on ditching Google Search for Kai, the story of a Wi-Fi network that only works when it's raining and more.

If you don't yet receive the Changelog Newsletter, sign up today at changelog.com/news.

We have some **great episodes** coming up this week: we interview [Scott Charon](https://scottchacon.com) on Wednesday, and Break master Cylinder returns to help us deconstruct the new [Dance Party](https://changelog.com/beats/dance-party) album on Friday!

Have a great week, **leave us a 5-star review** if you dig it & I'll talk to you again real soon.
