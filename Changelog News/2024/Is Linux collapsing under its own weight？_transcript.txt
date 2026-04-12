[0.00 --> 14.68]  what up nerds i'm jared and this is changelog news for the week of monday september 9th 2024
[14.68 --> 22.52]  after our conversation with alia abbott last week we decided to try zulip in earnest for a while
[22.52 --> 29.64]  so far so good the overall experience isn't quite as polished as slack but it's nerd built
[29.64 --> 35.28]  and you can tell they've put a lot of love into it if you'd like to kick the tires with us i'll put
[35.28 --> 41.62]  the link to join at the top of this week's newsletter okay let's get into the news is linux
[41.62 --> 49.90]  collapsing under its own weight a rust for linux developer wedsen almeda filehoe resigned from the
[49.90 --> 56.46]  project after an unfortunate interaction with another maintainer wedsen's parting words quote
[56.46 --> 63.04]  i am retiring from the project after almost four years i find myself lacking the energy and
[63.04 --> 69.98]  enthusiasm i once had to respond to some of the non-technical nonsense so it's best to leave it
[69.98 --> 77.00]  up to those who still have it in them end quote after that asahi lina who is a developer of the
[77.00 --> 84.50]  apple gpu drivers for linux sounded off with her own frustrations with maintainers and rust from the
[84.50 --> 91.06]  drm perspective her conclusion quote but i get that feeling that some linux kernel maintainers
[91.06 --> 97.56]  just don't care about future code quality or about stability or security anymore they just want to
[97.56 --> 103.28]  keep their c code and wish us rust folks would go away and that's really sad and isn't helping make
[103.28 --> 110.42]  linux better end quote the post i'm linking to is in response to those two events the author who goes by
[110.42 --> 118.76]  cb thinks they quote signal deeper issues in linux both technical and cultural end quote some of the
[118.76 --> 123.60]  technical and cultural issues are explained in the post what does this mean though for the rust for
[123.60 --> 130.80]  linux project cb says i think rust for linux as a project is in danger not because of technical reasons
[130.80 --> 136.42]  but because of social ones it's trivial for a maintainer who doesn't want rust to sandbag
[136.42 --> 141.30]  integration efforts for their subsystem for whatever reason not liking it not wanting the
[141.30 --> 147.08]  workload etc just refusing to help end quote so what does this mean for the future of linux
[147.08 --> 156.20]  the author seems to believe an eventual fork is likely brett victor introduces dynamic land brett victor
[156.20 --> 161.74]  a well-known interface designer and computer scientist who's best known for his amazing talks on the future
[161.74 --> 169.42]  of technology has been working quietly on a new project dynamic land for many years turns out he's done being quiet about it
[169.42 --> 177.06]  dynamic land is essentially making the real world computational then giving people what they need to compute it
[177.06 --> 183.52]  however they like you really should watch the six minute introduction video which is filled with amazing statements like
[183.52 --> 189.26]  you don't have to simulate a virtual world when the real world simulates itself and this one which is just bonkers
[189.26 --> 195.02]  so everything i've shown is taking place in our communal computing system called real talk and this is it
[195.02 --> 202.74]  real talk is not a code base it's a poster gallery or a bulletin board or a binder to call this endeavor
[202.74 --> 208.26]  ambitious would be an understatement here's the sum which if they pull it off and maybe they already have
[208.26 --> 213.96]  would be a big technical achievement and an enormous cultural achievement dynamic land is non-profit
[213.96 --> 219.72]  and real talk is not a product you don't buy communal computing you don't download communal computing
[219.72 --> 225.24]  our goal is to invent a form of computation which local communities of non-specialists can make for
[225.24 --> 230.50]  themselves from the ground up for their own needs which they fully understand and control
[230.50 --> 236.88]  a form of computation which is learned and taught not downloaded and used like reading and writing
[236.88 --> 245.44]  or mathematics or the arts not a product but a practice sre doesn't mean anything useful anymore
[245.44 --> 253.76]  rachel by the bay laments her realization that site reliability engineer sre has become useless as a way
[253.76 --> 259.82]  to categorize people with a very particular set of skills much like every other title has before it
[259.82 --> 266.12]  quote clearly somewhere along the line someone lost the thread and it has completely destroyed any
[266.12 --> 271.76]  notion of what an sre was supposed to be just so we're operating on a level playing ground here
[271.76 --> 277.54]  i'll lay down my own personal definition of the term and what i expect from people in that role and what
[277.54 --> 284.96]  i expected from myself to me an sre is both a sys admin and a programmer developer whatever you want
[284.96 --> 292.30]  to call it it's a logical and not an xor end quote she goes on to detail what is meant by sys admin
[292.30 --> 297.88]  and what is meant by programmer but what she's been seeing in her attempts to hire are sres who are
[297.88 --> 304.30]  just ops people i agree with rachel but not just about sres i found most job titles in the software
[304.30 --> 311.68]  world to be relatively useless and so much more so as each title ages let's do some sponsored news
[311.68 --> 319.46]  3.7 million fake github stars how much weight do you put into a project's github star count
[319.46 --> 326.02]  no matter how much it is it's probably too much socket researchers have uncovered 3.7 million
[326.02 --> 332.94]  fake github stars highlighting a growing threat linked to scams fraud and malware with these
[332.94 --> 338.64]  campaigns rapidly increasing over the last six months based on this research socket is launching
[338.64 --> 345.32]  a new suspicious stars on github alert that utilizes the low activity and clustering heuristics
[345.32 --> 351.84]  to detect packages associated with repos that have fake stars if you want to get proactive alerts
[351.84 --> 358.44]  and check your entire organization for suspicious star packages plus 70 more indicators of supply
[358.44 --> 364.70]  chain risk install the free socket for github app in just two clicks whenever a new dependency is added
[364.70 --> 371.34]  or updated in a pull request socket analyzes the package's behavior and security risk alerting you
[371.34 --> 377.38]  before any malicious code has the chance to land in your project check it out by following the link
[377.38 --> 384.64]  in the newsletter and thank you to socket for sponsoring changelog news your company needs junior
[384.64 --> 391.60]  devs doug turnball does a good job laying out the case for hiring junior devs a drum that i've been
[391.60 --> 399.24]  beating off and on for years quote lately big tech only wants elite squads of staff devs that can quote
[399.24 --> 405.56]  hit the ground running on the big often ai initiative it's been remarked over and over that ai will
[405.56 --> 413.00]  completely replace junior developers juniors after all exist to do code monkey work easily replaced
[413.00 --> 419.86]  with an llm however that misses the mark on why we have junior employees coaching junior employees
[419.86 --> 426.60]  becomes its own force multiplier for innovating at scale it's not about the added labor it's about a
[426.60 --> 433.20]  psychologically safe culture that values teaching and learning and the innovation that this unlocks
[433.20 --> 439.44]  end quote doug makes a lot of great points in this article i'll add one junior developers are
[439.44 --> 444.98]  plenteous that means you can take your time and find the ones that will really gel with your
[444.98 --> 451.12]  organizational culture also you don't have to pay them as much while you train them up and make them
[451.12 --> 456.56]  more valuable so you can pay them more you may be asking that age-old question but what if we train
[456.56 --> 463.70]  them up and they leave the answer to that is what if you don't train them up and they stay the llm
[463.70 --> 471.46]  honeymoon phase is about to end balder bjarnison has been consistently bearish on the current crop of ai
[471.46 --> 476.62]  tools and products since i've been following him i don't agree with him in all aspects but he does a good
[476.62 --> 483.10]  job of arguing his position so i appreciate his writing on the subject in this latest post balder
[483.10 --> 489.38]  explains how weaknesses and how llm's work are making them great targets for manipulation quote
[489.38 --> 495.06]  we've also known for a while that prompts are effectively impossible to secure it should not
[495.06 --> 501.02]  come as a surprise that some researchers decided to see if prompt security could be bypassed with a
[501.02 --> 507.36]  malicious token stream that completely bypasses the whole comprehensible language part the process for
[507.36 --> 512.62]  discovering these malicious token streams is quite similar to what profound the company mentioned
[512.62 --> 519.38]  earlier seems to be doing you automate a process of shoving customized prompts into one end of the llm
[519.38 --> 525.90]  black box and you map the output to discover token streams that have an unusually big impact on the output
[525.90 --> 532.88]  end quote given the opportunity for businesses to gain an unfair advantage we all know what they'll do
[532.88 --> 539.12]  with it balder thinks this is going to go from bad to much much worse as these techniques are uncovered
[539.12 --> 547.70]  quote this is going to get automated weaponized and industrialized tech companies have placed chatbots at
[547.70 --> 553.08]  the center of our information ecosystems and butchered their products to push them front and center
[553.08 --> 558.84]  the incentives for bad actors to try to game them are enormous and they are capable of making
[558.84 --> 567.24]  incredibly sophisticated tools for their purposes that is the news for now but also scan this week's
[567.24 --> 573.82]  changelog newsletter for even more news worth your attention like creating a git commit the hard way
[573.82 --> 579.62]  and grippability as an underrated code metric plus a whole lot more get in on that newsletter by
[579.62 --> 586.48]  popping your email address in at changelog.com slash news we have some great episodes coming up this
[586.48 --> 594.52]  week on wednesday eres zuckerman talking ergonomic keyboards and on friday natalie pisanovic from go time
[594.52 --> 601.66]  talking ai coding tools have a great week leave us a five-star review if you want some free stickers
[601.66 --> 604.26]  and i'll talk to you again real soon
[604.26 --> 611.50]  you
[616.50 --> 617.12]  you
[617.12 --> 621.28]  you
