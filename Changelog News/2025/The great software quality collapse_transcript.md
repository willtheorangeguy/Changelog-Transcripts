[0.00 --> 14.24]  what up nerds i'm jared and this is changelog news for the week of monday october 13th 2025
[14.24 --> 22.48]  i'm getting back into reading not audible not e-ink i'm talking physical books held in my
[22.48 --> 29.48]  physical hands scanned by my physical eyeballs cue olivia newton john in her iconic white headband
[29.48 --> 38.80]  i need your recommends please comment with the best book you've read in the last 10 years
[38.80 --> 47.82]  fiction non-fiction whatever okay let's get in to this week's news the great software quality collapse
[47.82 --> 54.44]  dennis stetskov describes how we've normalized catastrophe in the software industry quote
[54.44 --> 60.88]  we've normalized software catastrophes to the point where a calculator leaking 32 gigabytes of ram
[60.88 --> 68.04]  barely makes the news this isn't about ai the quality crisis started years before chat gpt existed
[68.04 --> 74.88]  ai just weaponized existing incompetence end quote dennis has been tracking software quality metrics
[74.88 --> 80.08]  for three years in this post he cites nine plus examples from across the industry where memory
[80.08 --> 86.20]  consumption has lost all meaning and system level failures have become routine what exactly is to
[86.20 --> 93.42]  blame not one single factor but dennis says the abstraction tax compounds exponentially like this
[93.42 --> 99.74]  quote modern software is built on towers of abstractions each one making development easier
[99.74 --> 106.70]  while adding overhead today's chain is react to electron to chromium to docker to kubernetes to vm
[106.70 --> 114.24]  to manage db to api gateways and each layer adds only 20 to 30 percent but compound a handful and you're
[114.24 --> 120.72]  at 2 to 6x overhead for the same behavior that's how a calculator ends up leaking 32 gigabytes not
[120.72 --> 126.42]  because someone wanted it to but because nobody noticed the cumulative cost until users started
[126.42 --> 132.72]  complaining end quote dennis says we need to ask ourselves some hard questions when did we accept that a
[132.72 --> 138.82]  calculator leaking 32 gigabytes is normal how many abstraction layers are actually necessary and what
[138.82 --> 144.88]  happens when we can't buy our way out anymore click through for his proposed path forward and the bottom
[144.88 --> 153.02]  line it can't be all bad can it the new home for react and react native meta is officially handing react
[153.02 --> 160.40]  and react native as well as supporting projects like jsx over to a foundation quote the react foundation's
[160.40 --> 165.54]  mission is to help the react community and its members the react foundation will maintain react's
[165.54 --> 171.04]  infrastructure organize react conf and create initiatives to support the react ecosystem the
[171.04 --> 176.64]  react foundation will be part of the linux foundation which has long fostered a vendor neutral environment
[176.64 --> 183.28]  for open source projects end quote meta isn't abandoning the projects at least not yet they've committed to a
[183.28 --> 188.98]  five-year partnership with the newly formed foundation including three plus million dollars in funding and
[188.98 --> 196.42]  dedicated engineering support github prioritizes azure migration over features here's frederick
[196.42 --> 203.46]  lardenoise apologize on the pronunciation reporting for the new stack quote with github ceo thomas domke
[203.46 --> 208.90]  leaving the company this august and github being folded more deeply into microsoft's organizational
[208.90 --> 215.62]  structure github lost that independence now according to internal github documents the new stack has seen
[215.62 --> 221.14]  the next step of this deeper integration into the microsoft structure is moving all of github's
[221.14 --> 227.38]  infrastructure to azure even at the cost of delaying work on new features end quote i'm not at all
[227.38 --> 232.66]  surprised by this but i am certainly disappointed my first thought we can walk and chew gum at the same
[232.66 --> 239.46]  time why not do both quote while github had previously started work on migrating parts of its service to
[239.46 --> 245.38]  azure our understanding is that these migrations have been halting and sometimes failed end quote
[245.38 --> 251.94]  yikes this is terrible optics for azure even a microsoft owned entity struggles to migrate to it
[251.94 --> 257.14]  and has to pull people off other features to make the transition even happen i've said it a few times this
[257.14 --> 263.38]  year i'll say it again github is primed for disruption where will that disruption come from i'm not sure but
[263.38 --> 271.86]  we'll know it when we see it it's now time for sponsored news claude sonnet 4.5 versus opus 4.1
[272.18 --> 279.06]  code rabbit just ran a head-to-head between claude sonnet 4.5 and opus 4.1 and the results are
[279.06 --> 286.66]  fascinating sonnet 4.5 isn't just faster it's cheaper and in many real world dev tasks smarter but
[286.66 --> 293.06]  here's the paradox even with stronger reasoning and better latency most teams still default to bigger
[293.06 --> 299.54]  slower models out of habit the hidden gem code rabbits data shows sonnet 4.5 matches opus level
[299.54 --> 306.10]  performance on code reviews debugging and refactors at a fraction of the cost it's a reminder that more
[306.10 --> 312.58]  tokens don't always mean more value this opens the door for teams to run cheaper faster better ai
[312.58 --> 319.30]  assisted reviews and maybe rethink what top tier really means get all the details at coderabit.ai and
[319.30 --> 323.86]  read the full blog post by following the link in this week's companion newsletter and you can find
[323.86 --> 325.78]  that at changelog.news.com
[325.78 --> 335.86]  python 3.14 is here how fast is it python 3.14 with the free threaded now officially supported
[335.86 --> 343.78]  was released on october 8th 2025 so miguel grinberg put it through its paces but first a warning quote
[343.78 --> 348.82]  running these benchmarks is fun and that's why i do it but it is really impossible to build an
[348.82 --> 353.78]  accurate performance profile of something as complex as the python interpreter just from
[353.78 --> 358.50]  running a couple of silly little scripts have a look at my benchmark but consider it just one data
[358.50 --> 364.66]  point and not the last word on python performance end quote okay with that out of the way what did
[364.66 --> 371.78]  miguel find click through for the individual benchmarks but his conclusions were one c python 3.14 appears to be
[371.78 --> 378.58]  the fastest of all the c pythons two its jit interpreter doesn't appear to provide any significant
[378.58 --> 386.02]  speed gains three its free threading interpreter is faster for cpu heavy multi-threaded apps and four
[386.02 --> 391.38]  pypi is insanely fast that last bullet point was the main thing i noticed when scrolling through the
[391.38 --> 398.50]  results while 3.14 beats previous versions pypi blows all c pythons out of the water while competing with
[398.50 --> 405.78]  note and rust alternatives let's talk about ai art the oatmeal's matthew inman published a take on ai
[405.78 --> 411.70]  art that's making the rounds maybe you haven't seen it yet quote when i consume art it evokes a feeling
[411.70 --> 420.82]  good bad neutral whatever when i consume ai art it also evokes a feeling good bad neutral whatever until i
[420.82 --> 428.18]  find out that it's ai art then i feel deflated grossed out and maybe a little bit bored end quote i'm not
[428.18 --> 434.42]  so sure about grossed out but deflated and bored both track with how i felt when realizing a piece
[434.42 --> 440.98]  of art is actually ai art but on the other hand i've also seen some pretty imaginative stuff and had a
[440.98 --> 446.66]  lot of fun bringing my own imaginations to life too i've hemmed and i've hawed about ai art but i'm
[446.66 --> 452.42]  starting to think the right approach is to adapt my stance on other ai tools which is use ai to help you
[452.42 --> 459.30]  think not to think for you take that and apply it to the wonderful world of art and creative expression
[459.30 --> 465.78]  and it's use ai to help you make art not to make art for you that's the news for now but go and
[465.78 --> 473.06]  subscribe to the change log newsletter for the full scoop of links worth clicking on such as notes on
[473.06 --> 482.98]  switching to helix from vim a memory upgrade for your coding agent and a rust based cli utility toolbox
[483.86 --> 491.22]  get in on that newsletter at changelog.news last week on the pod evan you joined me to discuss veet's
[491.22 --> 497.78]  past and future and jose valim told us all about tidewave his new direction for ai developer tooling
[497.78 --> 504.18]  find those in your feed and stay tuned this week when deepak singh from aws's kiro team joins us on
[504.18 --> 511.38]  wednesday and on friday change logging friends with justin searles and mike mcquade have a great week
[511.38 --> 525.78]  like subscribe and five-star review us if you dig the show and i'll talk to you again real soon
