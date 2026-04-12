[0.00 → 11.98] What up nerds? I'm Jared and this is Changelog News for the week of Tuesday, December 8th,
[11.98 → 19.14] 2025. We are quickly approaching last call for state of the log voicemails. We record the show
[19.14 → 23.82] in a week, and we have to give BMC time to make the remixes. So if you're thinking about sending
[23.82 → 31.64] one in, and you should, now is the best time. Submit yours today at changelog.fm slash S-O-T-L.
[31.98 → 39.62] Okay, let's get into this week's news. The confident idiot problem or why AI needs hard rules,
[39.62 → 45.46] not vibe checks. If you've been following how do we actually use AI in production
[45.46 → 51.24] conversation stream, you've probably heard people propose a strategy where one LLM checks another
[51.24 → 58.96] LLM's results. But will that work? Quote, we are told to ask GPT-4-0 to grade GPT-3.5. We are told
[58.96 → 64.94] to fix the vibes, but this creates a dangerous circular dependency. If the underlying models
[64.94 → 70.26] suffer from sycophancy, which is agreeing with the user, or hallucination, a judge model often
[70.26 → 76.48] hallucinates a passing grade. We are trying to fix probability with more probability. That is a
[76.48 → 82.44] losing game. End quote. One possible way of dealing with these confident idiots we've introduced into
[82.44 → 88.36] our software stacks the last few years is to stop treating agents like magic boxes and start treating
[88.36 → 95.32] them like software. Hence, the Steer SDK was created. Quote, Steer is an open source Python library that
[95.32 → 102.54] intercepts agent failures, such as hallucinations, bad JSON, PII leaks, etc. And allows you to inject
[102.54 → 108.96] fixes via a local dashboard without changing your code. End quote. Another way of dealing with these
[108.96 → 115.26] confident idiots in our software stacks is removed them. But that might not be possible anymore.
[115.98 → 122.24] Bun is joining Anthropic. The company behind Bun, which is the open source runtime for Cloud Code,
[122.34 → 128.52] is joining Anthropic. We discussed the big acquisition slash aqua hire on last week's Friends episode,
[128.52 → 134.14] but at the time I hadn't quite considered this move and how contrary it is to Anthropic's party line
[134.14 → 139.42] that AI agents are replacing software engineers. From Anthropic's announcement, quote,
[139.74 → 144.50] we've been a close partner of Bun for many months. Our collaboration has been central to the rapid
[144.50 → 149.92] execution of the Cloud Code team, and it directly drove the recent launch of Cloud Code's native installer.
[150.22 → 154.52] We know the Bun team is building from the same vantage point that we do at Anthropic,
[154.52 → 160.60] with a focus on rethinking the developer experience and building innovative, useful products. End quote.
[160.94 → 165.48] Bun is open source. Why not just fork it and have a Cloud Code-powered engineer
[165.48 → 170.00] make all the necessary changes and upgrades to the runtime that Anthropic needs?
[170.40 → 174.14] Perhaps because there's no getting there from here. At least not yet.
[174.42 → 180.26] Jared Sumner and the Bun team's expertise is what's so valuable. Still, even to Anthropic.
[180.26 → 187.72] Cloud can't recreate classic Space Jam site. Jonah Glover tried to recreate everyone's favourite 1996
[187.72 → 193.76] website by giving Cloud Code, which is running Opus 4.1, a screenshot of the site and all the
[193.76 → 199.52] associated assets. It failed repeatedly in all the ways I would expect from my own front-end and
[199.52 → 203.58] design attempts with the tool. Jonah's finding, which is quite relatable, quote,
[203.58 → 209.10] Once Cloud's version existed, every grid overlay, every comparison step, every precise adjustment
[209.10 → 213.94] was anchored to his layout, not the real one. At the end of all of this, I'm left with the
[213.94 → 219.44] irritating fact that, like many engineers, he's wrong, and he thinks he's right. What this teaches
[219.44 → 224.92] me is that Cloud is actually kind of a liar, or at least, Cloud is confused. However, for the drama,
[225.22 → 227.66] I'll assume Cloud is a liar. End quote.
[227.66 → 232.92] I've been giving Cloud Code a lot of props lately, but I've also been giving it a lot of tasks that it
[232.92 → 238.94] can't quite accomplish. This process starts off as fun and interesting, but each time it ends in failure,
[239.14 → 245.48] I am perplexed by all the possible failure paths. Was it me? Am I prompting? Was it the agent? Was it the
[245.48 → 251.64] model? Or perhaps I'm asking for things that aren't easily accomplished with today's tech. I can be quite
[251.64 → 257.26] demanding. This all makes me yearn for the days when the only one to blame for my failures was me.
[257.66 → 259.90] It's now time for sponsored news.
[260.84 → 263.28] Depot's Advent of Code 2025.
[263.94 → 270.12] Depot is running a community leaderboard for Advent of Code 2025, and they're putting real money behind it.
[270.44 → 275.40] The top five finishers each direct $1,000 to a registered charity of their choice.
[275.76 → 281.40] If you pick a charity supporting STEM education or the developer ecosystem, Depot adds a 50% bonus.
[282.16 → 285.22] They've already generated $7,500 in donations.
[285.22 → 291.68] Here's the format. 12 days of puzzles, unlocking daily at midnight Eastern, starting December 1st.
[291.88 → 296.96] Solve at your own pace? There's no time limit. Any language, any skill level, each day brings a
[296.96 → 302.12] two-part programming challenge from Eric Waste's Advent of Code. To join Depot's private leaderboard,
[302.34 → 307.10] request access on their events page. They'll send you a code. Whether you're competing for the top five
[307.10 → 311.94] or just want to sharpen your skills alongside other devs, it's a good excuse to write some code this month.
[311.94 → 320.72] Check it out at depot.dev slash events slash advent dash of dash code dash 2025, or just follow the link in the newsletter.
[321.10 → 325.16] It's also in your chapter data. Thank you to Depot for sponsoring Changelog News.
[325.68 → 328.40] Google skills JPEG XL.
[328.40 → 329.36] Quote,
[329.36 → 336.60] In a dramatic turn of events, the Chromium team has reversed its obsolete tag and has decided to support the format in Blink,
[336.72 → 339.78] which is the engine behind Chrome, Chromium, and Edge.
[340.28 → 347.50] Given Chrome's position in the browser market share, I predict the format will become a de facto standard for images in the near future.
[347.80 → 348.14] End quote.
[348.52 → 353.98] We're used to things being killed by Google, but unchilled? This is a trend I can get behind.
[353.98 → 360.78] Here's my unchilled requests. It's time to bring back Zeitgeist, Dodgeball, and of course, Google Reader.
[361.14 → 364.16] The next generation of Linux gaming.
[364.54 → 373.86] If the mythical year of the Linux desktop is ever to materialize, it will first be preceded by a sea change in gaming options for the venerable open source OS.
[374.22 → 381.22] The gaming sea change appears to be in full swing, with Steam on Linux hitting an all-time high of over 3% usage last month.
[381.22 → 387.48] Enter Barite, a Fedora-based Linux distro that's hyper-focused on making gaming awesome.
[387.74 → 388.00] Quote,
[388.24 → 395.62] Barite is designed for Linux newcomers and enthusiasts alike with Steam pre-installed, HDR and VRR support,
[396.02 → 405.26] improved CPU schedulers for responsive gameplay, and numerous community-developed tools and tweaks to streamline your gaming and streaming experience.
[405.46 → 405.82] End quote.
[405.82 → 414.50] The project began back in 2023, but it appears to be maturing and aiming at sustainability by setting up ways to donate with its latest update.
[414.82 → 415.08] Quote,
[415.20 → 426.04] As Barite matures, we begin to tackle more ambitious projects, such as proper Secure Boot, support for more handheld devices, and conference attendance, which means more costs for us.
[426.40 → 429.56] And we would gladly appreciate the help in covering them.
[429.56 → 437.56] That is the news for now, but go and subscribe to the Changelog newsletter for the full scoop of links worth clicking on, such as...
[437.56 → 440.56] Why I ignore the spotlight as a staff engineer...
[441.52 → 443.56] Vanilla CSS is all that you need...
[444.70 → 448.56] And what happens when you take an xkcd joke too literally...
[449.28 → 451.56] Get in on the newsletter at changelog.news.
[451.56 → 453.94] Have yourself a great week!
[454.36 → 460.06] Like, subscribe, and 5-star review us if you dig the show, and I'll talk to you again real soon.
