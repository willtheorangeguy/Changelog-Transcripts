[0.00 → 14.24] what up nerds I'm jarred and this is changelog news for the week of monday, October 13th 2025
[14.24 → 22.48] I'm getting back into reading not audible not e-ink I'm talking physical books held in my
[22.48 → 29.48] physical hands scanned by my physical eyeballs cue Olivia newton john in her iconic white headband
[29.48 → 38.80] I need your recommends please comment with the best book you've read in the last 10 years
[38.80 → 47.82] fiction non-fiction whatever okay let's get into this week's news the great software quality collapse
[47.82 → 54.44] Dennis Stetson describes how we've normalized catastrophe in the software industry quote
[54.44 → 60.88] we've normalized software catastrophes to the point where a calculator leaking 32 gigabytes of ram
[60.88 → 68.04] barely makes the news this isn't about AI the quality crisis started years before ChatGPT existed
[68.04 → 74.88] AI just weaponized existing incompetence end quote Dennis has been tracking software quality metrics
[74.88 → 80.08] for three years in this post he cites nine plus examples from across the industry where memory
[80.08 → 86.20] consumption has lost all meaning and system level failures have become routine what exactly is to
[86.20 → 93.42] blame not one single factor but Dennis says the abstraction tax compounds exponentially like this
[93.42 → 99.74] quote modern software is built on towers of abstractions each one making development easier
[99.74 → 106.70] while adding overhead today's chain is reacted to electron to chromium to docker to Kubernetes to VM
[106.70 → 114.24] to manage dB to API gateways and each layer adds only 20 to 30 percent but compound a handful, and you're
[114.24 → 120.72] at 2 to 6x overhead for the same behaviour that's how a calculator ends up leaking 32 gigabytes not
[120.72 → 126.42] because someone wanted it to but because nobody noticed the cumulative cost until users started
[126.42 → 132.72] complaining end quote Dennis says we need to ask ourselves some hard questions when did we accept that a
[132.72 → 138.82] calculator leaking 32 gigabytes is normal how many abstraction layers are actually necessary and what
[138.82 → 144.88] happens when we can't buy our way out any more click through for his proposed path forward and the bottom
[144.88 → 153.02] line it can't be all bad can it the new home for react and React Native meta is officially handing react
[153.02 → 160.40] and React Native as well as supporting projects like JSX over to a foundation quote the React foundation's
[160.40 → 165.54] mission is to help the React community and its members the React foundation will maintain reacts
[165.54 → 171.04] infrastructure organize react cone and create initiatives to support the React ecosystem the
[171.04 → 176.64] react foundation will be part of the Linux foundation which has long fostered a vendor neutral environment
[176.64 → 183.28] for open source projects end quote meta isn't abandoning the projects at least not, yet they've committed to a
[183.28 → 188.98] five-year partnership with the newly formed foundation including three plus million dollars in funding and
[188.98 → 196.42] dedicated engineering support GitHub prioritizes azure migration over features here's Frederick
[196.42 → 203.46] larcenous apologize on the pronunciation reporting for the new stack quote with GitHub CEO Thomas dome
[203.46 → 208.90] leaving the company this august and GitHub being folded more deeply into Microsoft's organizational
[208.90 → 215.62] structure GitHub lost that independence now according to internal GitHub documents the new stack has seen
[215.62 → 221.14] the next step of this deeper integration into the Microsoft structure is moving all of GitHub's
[221.14 → 227.38] infrastructure to azure even at the cost of delaying work on new features end quote I'm not at all
[227.38 → 232.66] surprised by this but I am certainly disappointed my first thought we can walk and chew gum at the same
[232.66 → 239.46] time why not do both quote while GitHub had previously started work on migrating parts of its service to
[239.46 → 245.38] azure our understanding is that these migrations have been halting and sometimes failed end quote
[245.38 → 251.94] yikes this is terrible optics for azure even a Microsoft owned entity struggles to migrate to it
[251.94 → 257.14] and has to pull people off other features to make the transition even happen I've said it a few times this
[257.14 → 263.38] year I'll say it again GitHub is primed for disruption where will that disruption come from I'm not sure but
[263.38 → 271.86] we'll know it when we see it, it's now time for sponsored news Claude sonnet 4.5 versus opus 4.1
[272.18 → 279.06] code rabbit just ran a head-to-head between Claude sonnet 4.5 and opus 4.1 and the results are
[279.06 → 286.66] fascinating sonnet 4.5 isn't just faster it's cheaper and in many real world dev tasks smarter but
[286.66 → 293.06] here's the paradox even with stronger reasoning and better latency most teams still default to bigger
[293.06 → 299.54] slower models out of habit the hidden gem code rabbits data shows sonnet 4.5 matches opus level
[299.54 → 306.10] performance on code reviews debugging and refactors at a fraction of the cost it's a reminder that more
[306.10 → 312.58] tokens don't always mean more value this opens the door for teams to run cheaper faster better AI
[312.58 → 319.30] assisted reviews and maybe rethink what top tier really means get all the details at coderabit.ai and
[319.30 → 323.86] read the full blog post by following the link in this week's companion newsletter, and you can find
[323.86 → 325.78] that at changelog.news.com
[325.78 → 335.86] python 3.14 is here how fast is it python 3.14 with the free threaded now officially supported
[335.86 → 343.78] was released on October 8th 2025 so Miguel grin berg put it through its paces but first a warning quote
[343.78 → 348.82] running these benchmarks is fun and that's why I do it, but it is really impossible to build an
[348.82 → 353.78] accurate performance profile of something as complex as the python interpreter just from
[353.78 → 358.50] running a couple of silly little scripts have a look at my benchmark but consider it just one data
[358.50 → 364.66] point and not the last word on python performance end quote okay with that out of the way what did
[364.66 → 371.78] Miguel find click through for the individual benchmarks but his conclusions were one c python 3.14 appears to be
[371.78 → 378.58] the fastest of all the c pythons two its JIT interpreter doesn't appear to provide any significant
[378.58 → 386.02] speed gains three its free threading interpreter is faster for CPU heavy multithreaded apps and four
[386.02 → 391.38] PyPI is insanely fast that last bullet point was the main thing I noticed when scrolling through the
[391.38 → 398.50] results while 3.14 beats previous versions PyPI blows all c pythons out of the water while competing with
[398.50 → 405.78] note and rust alternatives let's talk about AI art the oatmeal's Matthew Inman published a take on AI
[405.78 → 411.70] art that's making the rounds maybe you haven't seen it yet quote when I consume art it evokes a feeling
[411.70 → 420.82] good bad neutral whatever when I consume AI art it also evokes a feeling good bad neutral whatever until i
[420.82 → 428.18] find out that it's AI art then I feel deflated grossed out, and maybe a little bit bored end quote I'm not
[428.18 → 434.42] so sure about grossed out but deflated and bored both track with how I felt when realizing a piece
[434.42 → 440.98] of art is actually AI art but on the other hand I've also seen some pretty imaginative stuff and had a
[440.98 → 446.66] lot of fun bringing my own imaginations to life too I've hemmed and I've hawed about AI art but I'm
[446.66 → 452.42] starting to think the right approach is to adapt my stance on other AI tools which is use AI to help you
[452.42 → 459.30] think not to think for you take that and apply it to the wonderful world of art and creative expression
[459.30 → 465.78] and it's use AI to help you make art not to make art for you that's the news for now but go and
[465.78 → 473.06] subscribe to the change log newsletter for the full scoop of links worth clicking on such as notes on
[473.06 → 482.98] switching to helix from vim a memory upgrade for your coding agent and a rust based CLI utility toolbox
[483.86 → 491.22] get in on that newsletter at changelog. News last week on the pod Evan you joined me to discuss meet's
[491.22 → 497.78] past and future and José valid told us all about tide wave his new direction for AI developer tooling
[497.78 → 504.18] find those in your feed and stay tuned this week when Deepak Singh from AWS's Kirk team joins us on
[504.18 → 511.38] Wednesday and on Friday change logging friends with Justin series and mike McQuade have a great week
[511.38 → 525.78] like subscribe and five-star review us if you dig the show and I'll talk to you again real soon
