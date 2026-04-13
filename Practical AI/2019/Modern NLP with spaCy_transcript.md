[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.24 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.04]  And unlike standard droplets, which use shared virtual CPU threads,
[29.04 --> 32.88]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.42 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 --> 45.20]  So if you have build boxes, CICD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.20 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.16 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.30]  And now onto the show.
[106.78 --> 110.32]  Welcome to another episode of Practical AI.
[110.74 --> 112.50]  This is Daniel Whitenack.
[112.62 --> 115.20]  I'm a data scientist with SIL International,
[115.62 --> 119.28]  and I am joined as always by my co-host, Chris Benson,
[119.78 --> 122.82]  who is a principal AI strategist at Lockheed Martin.
[123.00 --> 123.64]  How are you doing, Chris?
[123.84 --> 124.58]  I am doing great.
[124.62 --> 125.42]  How's it going today, Daniel?
[125.42 --> 127.40]  It's going really good.
[127.50 --> 128.44]  It's been a busy week.
[128.58 --> 132.84]  Had calls with teams in India, and if you're listening, hello earlier in the week,
[132.96 --> 135.44]  and that kind of got my schedule off.
[135.52 --> 137.20]  So I'm a little bit tired.
[137.34 --> 138.98]  We'll see how the conversations go.
[139.12 --> 139.98]  I think it'll be all right.
[140.24 --> 142.14]  I think this conversation is going to wake you up,
[142.18 --> 145.06]  because we're talking about what I think of as your favorite topic in AI.
[145.56 --> 147.04]  It definitely is.
[147.04 --> 150.28]  As you know, I'm always doing language-related things,
[150.38 --> 151.84]  natural language-related things.
[151.84 --> 152.98]  And I'm really excited.
[153.14 --> 155.88]  I hope you are able to get some questions in today,
[155.96 --> 157.44]  because I have all sorts of questions.
[157.68 --> 159.80]  I'll pause every once in a while to let you get one in.
[160.00 --> 162.88]  Yeah, I'm guessing this is the last moment listeners are going to hear my voice.
[164.14 --> 169.36]  But today we're joined by a couple of the core developers of Spacey
[169.36 --> 172.54]  and co-founders of Explosion.
[172.54 --> 177.32]  And we're joined by Enes Montani and Matthew Hannibal.
[177.46 --> 177.72]  Welcome.
[178.42 --> 178.64]  Hey.
[178.88 --> 179.14]  Hey.
[179.52 --> 179.86]  Thanks.
[180.20 --> 182.54]  Yeah, great to have you both on the podcast.
[182.74 --> 188.30]  Appreciate you taking time out of, I'm sure, the busy development of Spacey to join us.
[188.36 --> 190.18]  Really excited to talk about everything.
[190.48 --> 191.12]  No problem.
[191.32 --> 192.10]  Glad to be here.
[192.30 --> 192.62]  Yeah.
[192.96 --> 194.74]  I was telling you before the podcast,
[194.88 --> 199.94]  I recently got your latest Spacey stickers and have them proudly on my laptop.
[200.26 --> 201.40]  Oh, that's so cool.
[201.40 --> 204.40]  I'm still actually waiting to really see them in the wild.
[204.78 --> 204.88]  Yeah.
[205.00 --> 208.76]  Because this round, we've sent like over a thousand sticker packs.
[209.40 --> 210.72]  And so they're everywhere.
[211.38 --> 215.34]  And I'm like waiting for the day where I'm like sitting in a cafe and someone has my sticker.
[215.50 --> 216.28]  And I'm like, oh my God.
[217.40 --> 217.60]  Yeah.
[217.76 --> 220.40]  So for our listeners who don't know, every once in a while,
[220.44 --> 222.02]  and I don't know how many times you've done this,
[222.10 --> 228.02]  but you kind of just put out the call for anybody that wants stickers to send you some info
[228.02 --> 229.42]  and you'll send them stickers.
[229.42 --> 233.82]  And I saw it on Twitter and I was like, yeah, that's, I've got to get in on that right away.
[234.08 --> 235.52]  And they're really great stickers too.
[235.80 --> 240.26]  There's a couple like related to like Prodigy and data annotation,
[240.26 --> 243.52]  but then there's some NLP tattoos, I would say.
[243.90 --> 245.42]  Is that the way to characterize it?
[246.24 --> 246.36]  Yeah.
[246.36 --> 248.16]  Kind of like the old school tattoo style.
[248.30 --> 248.38]  Yeah.
[248.52 --> 248.82]  Yeah.
[248.92 --> 249.16]  Yeah.
[249.16 --> 250.26]  Really nice design.
[250.82 --> 251.02]  Yeah.
[251.02 --> 253.24]  Sort of like, I think of it as a sailor sort of style.
[253.68 --> 253.88]  Yeah.
[254.12 --> 257.76]  I was kind of, I've been joking that like, I don't know how many retweets should I ask for
[257.76 --> 259.44]  to like get it actually tattooed on me?
[259.64 --> 263.92]  Because I'm at a level where I have enough tattoos that it kind of doesn't matter as much
[263.92 --> 264.30]  anymore.
[264.50 --> 265.54]  And I'm like, well, yeah, sure.
[265.60 --> 267.26]  I totally walk into, walk in and I get it.
[267.26 --> 267.56]  Yeah.
[267.56 --> 269.84]  I mean, I guess threshold would be far fewer retweets than me.
[269.92 --> 271.68]  Like, you know, it'd be the first tattoo for me.
[271.68 --> 273.32]  Please don't get a tattoo.
[273.48 --> 274.58]  Like it's so unique to not.
[276.90 --> 282.52]  On that note, I would love to hear about both of your backgrounds outside of tattoos.
[283.18 --> 286.94]  Would you want to give a little bit of your background and then, and then maybe Matthew
[286.94 --> 287.34]  as well?
[287.58 --> 288.10]  Yeah, actually.
[288.14 --> 291.98]  I mean, we kind of need to start with Matt actually, because that's kind of a better story.
[292.04 --> 292.90]  Or should I start with it?
[292.90 --> 298.34]  Yeah, actually, I guess when we normally describe this first.
[298.34 --> 302.96]  So I'd been working on natural language processing for a long time.
[303.12 --> 309.08]  I started my PhD in 2005 and graduated from that in like, you know, 2009, 2010.
[309.42 --> 313.22]  And then I was doing research on this for a few years after that, as well as a postdoc.
[313.66 --> 317.84]  So basically, like as the technologies improved and there was more and more interest in this,
[317.90 --> 321.66]  I saw there were companies who were trying to use my research code.
[322.12 --> 324.92]  So, you know, I'd written some blog posts that had gotten some attention.
[324.92 --> 327.88]  And so, you know, I just had a GitHub repo sitting there.
[328.02 --> 329.58]  And so people were trying to use this.
[329.66 --> 333.24]  And I was like, well, it really was just supposed to print results and exit.
[333.36 --> 334.78]  That was like its mission in life.
[334.86 --> 338.56]  And, you know, I designed it quite tightly around that like core task.
[339.40 --> 343.54]  So I thought that there was actually a need for in the software ecosystem for more production
[343.54 --> 346.80]  ready stuff and things that could, you know, basically cross that gap.
[346.90 --> 351.38]  And so I was, you know, I was at about the level where I was supposed to be writing grant
[351.38 --> 353.52]  proposals, which wasn't really my thing.
[353.52 --> 358.98]  And so I decided, well, OK, if I leave this, I can have a go at starting a company and starting
[358.98 --> 359.68]  something with that.
[360.20 --> 362.28]  And then soon after this, I met Innes.
[362.42 --> 364.98]  And then we started working on, I think it was the display.
[365.14 --> 365.26]  Yeah.
[365.48 --> 365.88]  Yeah.
[365.88 --> 369.90]  I mean, I think actually, yeah, because we met and I'd always done like, so I actually,
[369.98 --> 371.94]  I started making websites when I was a teenager.
[371.94 --> 373.54]  So that's kind of how I got into programming.
[373.54 --> 375.84]  And my degree is also partly linguistics.
[376.08 --> 378.92]  So I kind of had a good idea of what Matt was doing there.
[379.00 --> 382.14]  And like, yeah, he always wanted to have a visualizer and have like better user experience.
[382.14 --> 384.16]  And at that time I was working as a freelancer.
[384.26 --> 387.86]  And I remember like the first thing I actually said was like, look, I totally know what you,
[388.24 --> 390.24]  what you're looking for there, but it sounds a bit boring.
[390.36 --> 391.50]  I don't know if I want to work on that.
[391.64 --> 392.86]  I have other things to do.
[393.12 --> 394.56]  So that was actually my first reaction.
[394.90 --> 396.42]  But I ended up doing it.
[396.84 --> 397.24]  Validation.
[399.14 --> 400.78]  So, yeah, we did end up working together.
[400.78 --> 405.38]  And we very quickly saw that there was like, I don't know, a lot we could do with both
[405.38 --> 406.70]  our skills kind of combined.
[406.84 --> 410.48]  And I started working on the core libraries basically shortly after that.
[410.68 --> 412.62]  And that was kind of when it was first released.
[413.22 --> 413.96]  And yeah.
[414.16 --> 414.38]  Yeah.
[414.42 --> 415.38]  So when was that?
[415.78 --> 416.92]  Early 2015.
[417.60 --> 417.84]  Okay.
[417.98 --> 418.16]  Wow.
[418.22 --> 420.36]  So that's like, that's quite a long time ago.
[420.60 --> 420.78]  Yeah.
[421.38 --> 421.86]  Yeah.
[421.86 --> 427.10]  And in terms of the initial ideas, did the company and sort of consulting things and
[427.10 --> 428.56]  other stuff like that come first?
[428.56 --> 431.32]  Or was the initial idea really to build the library?
[432.26 --> 438.08]  So when I was thinking about leaving academia, I had, I guess, a, you know, a range of ideas
[438.08 --> 439.58]  for exactly what I could do.
[439.92 --> 444.12]  One of them was actually to work on software to assist language learners.
[444.48 --> 449.48]  So, you know, I sorted, well, okay, the tools for, you know, learning another language are
[449.48 --> 453.02]  kind of primitive and there's kind of a computational linguistic angle on that.
[453.32 --> 457.66]  Then I quickly saw, well, okay, it wasn't quite what I wanted to do, but, you know, and
[457.66 --> 461.84]  I saw, okay, there's, you know, a gap in the software ecosystem for a library like this.
[462.20 --> 466.92]  So it was very much around like, okay, well, there's a potential for having something there
[466.92 --> 469.64]  that's going to be useful to people in a commercial context.
[469.64 --> 473.64]  And I think that the way it would be most useful to people would be if it was open source,
[474.00 --> 478.88]  because I feel like this type of technology, if it's closed source, or if it's like under
[478.88 --> 480.96]  an API or something, it's just not as useful.
[481.22 --> 485.72]  And I thought, well, okay, if we can make the software useful to people, then there'll
[485.72 --> 488.84]  be a range of ways that we can support it commercially as well.
[489.08 --> 494.14]  Especially if we, you know, keep it relatively small and don't try to build it as like, you
[494.14 --> 498.34]  know, don't try to necessarily have a story for how it could be the biggest company in
[498.34 --> 499.10]  the world or something.
[499.68 --> 504.42]  There would be plenty of like, you know, interest from companies to, you know, make their usage
[504.42 --> 508.06]  of it a bit better and gain something and have a commercial opportunity around it.
[508.06 --> 510.70]  So like, yeah, Spacey was definitely there first.
[511.06 --> 513.76]  And then when we started the company, that's when we thought about, okay, how are we going
[513.76 --> 514.80]  to make money?
[514.80 --> 516.84]  Or even we had ideas for products we wanted to build.
[517.04 --> 518.08]  We didn't want to take venture.
[518.48 --> 522.20]  So we were like, well, okay, we have users who want to use our stuff.
[522.50 --> 525.26]  And so we put out kind of a call for consulting.
[525.42 --> 529.42]  And we had quite a few companies applying and that we ended up working with.
[529.82 --> 534.40]  And that's how we initially bootstrapped Explosion when we first started for like the first
[534.40 --> 535.00]  six months.
[535.00 --> 536.32]  I think we did consulting.
[536.32 --> 536.76]  Yeah.
[537.64 --> 542.92]  And that was enough to get our first product developed, Prodigy, which is an annotation
[542.92 --> 548.40]  tool that, you know, is on a sort of old school software licensing where you pay for it and
[548.40 --> 549.34]  then you keep it.
[549.54 --> 552.90]  And, you know, instead of like renting it, like most software is these days.
[553.30 --> 557.60]  And that's been enough to keep the bills paid and then some since, and the team's been growing
[557.60 --> 559.22]  slowly since then as well.
[559.22 --> 561.08]  So I've got a question.
[561.24 --> 564.94]  I know Daniel has been intimately involved in using Spacey.
[565.12 --> 568.66]  I'm kind of curious as a newbie though, why is it called Spacey?
[570.38 --> 576.00]  So initially the very first idea that I had was around tokenization because I thought that
[576.00 --> 580.10]  the tools for data weren't really up to production grade.
[580.48 --> 585.08]  And it's the first thing that anybody ever needs to do in natural language is split the
[585.08 --> 586.28]  text into tokens.
[586.28 --> 588.02]  So I was like, well, it's based on spaces.
[588.36 --> 589.88]  It was short and it wasn't taken.
[590.60 --> 595.18]  And, you know, I had been working in Scython for a while and I liked, you know, basically
[595.18 --> 599.88]  developing it as a Scython program with like, you know, basically a Python API.
[600.52 --> 605.22]  And so that also, you know, emphasized the sort of speed aspect and the Scython aspect.
[605.50 --> 610.74]  So, you know, the same way things are like everything Py, this was like ending in Psy.
[610.88 --> 612.64]  And so I was like, okay, Spacey, it works.
[612.64 --> 613.08]  Yeah.
[614.28 --> 615.06]  Yeah, definitely.
[615.40 --> 619.90]  And just for our listeners, we'll try to clarify for those that aren't familiar with
[619.90 --> 622.30]  natural language stuff, some jargon throughout.
[622.58 --> 624.16]  So tokens and that sort of thing.
[624.28 --> 627.46]  I'm going to keep you honest there because I'm the only person here who's not an NLP
[627.46 --> 627.96]  expert.
[628.36 --> 628.78]  So yeah.
[628.92 --> 632.26]  So like tokenization and tokens, you mentioned like spaces.
[632.26 --> 637.68]  So you've got text and you've got, you know, words in that text and tokenization would
[637.68 --> 638.04]  be what?
[638.04 --> 638.76]  Yeah.
[638.76 --> 641.76]  Well, tokenization would be to split the text into words.
[641.92 --> 645.42]  And it sounds, if you just look at it, it sounds very simple, but it's actually once
[645.42 --> 652.34]  you get to things like punctuation, more complex ways of phrasing things, contractions, yeah,
[652.38 --> 655.28]  in English, for example, that gets a lot more complicated.
[655.58 --> 657.20]  And then there are also different definitions.
[657.48 --> 657.64]  Okay.
[657.66 --> 658.42]  What's a token?
[658.94 --> 661.04]  A token is not always necessarily a word.
[661.44 --> 661.68]  Okay.
[661.68 --> 664.82]  In English, you just have lots of like small words that form bigger words.
[664.82 --> 669.70]  In German, for instance, a lot of these would be like one word or that's where all these
[669.70 --> 674.10]  jokes about the German language come from, that we have these like massive words that
[674.10 --> 675.60]  express something very, very specific.
[676.88 --> 681.74]  Well, but, you know, in languages like English, we still have the same things of terminology.
[681.98 --> 684.88]  It's just the terminology is, you know, written with spaces in it.
[685.16 --> 685.26]  Yeah.
[685.26 --> 690.68]  So, you know, natural language processing is a term that we use and we call it that specific
[690.68 --> 691.12]  thing.
[691.12 --> 694.64]  And in German, that would be written without spaces, but it doesn't actually.
[694.64 --> 696.82]  I do think I would, there would be probably one space in it.
[697.06 --> 697.28]  Oh, okay.
[697.30 --> 699.44]  But it's more like income tax returns or something.
[699.60 --> 699.72]  Sure.
[699.98 --> 700.16]  Yeah.
[700.28 --> 701.54]  That's definitely one word in German.
[701.54 --> 701.72]  Yeah.
[701.80 --> 704.70]  Or federal income tax rebate guarantee or something.
[704.78 --> 705.12]  I don't know.
[705.26 --> 705.46]  Yeah.
[706.24 --> 707.44]  Pretty sure that's one word.
[707.74 --> 708.00]  Yeah.
[708.82 --> 709.22]  Yeah.
[709.22 --> 713.74]  Like you say, it creates all of these complexities that you don't realize first, because in certain
[713.74 --> 717.38]  languages, right, that certain things are said with a certain number of words and other
[717.38 --> 719.14]  languages, it's not the same number.
[719.14 --> 724.70]  So people might, for example, think of translation as, you know, from one word to another, just
[724.70 --> 726.10]  this sort of word to word thing.
[726.24 --> 729.06]  But it gets much more complicated than that quickly.
[729.58 --> 730.30]  Yes, exactly.
[730.52 --> 735.24]  And these differences between languages sort of seen in the algorithms that have been
[735.24 --> 737.02]  developed in the way that people do things.
[737.64 --> 742.22]  So I often tell people that, you know, you can basically expect that any natural language
[742.22 --> 747.14]  processing technique will work best on a language depending on how similar it is to English.
[747.14 --> 751.36]  So English being the language that's most similar to English, everything works best on English.
[751.48 --> 755.48]  And it's not because there's like, I don't know, some magic property of English that makes
[755.48 --> 757.70]  it easier or more amenable to computation.
[757.70 --> 761.96]  It's just that, you know, for the last like, you know, 50 years that people have been thinking
[761.96 --> 766.12]  about these problems, the dominant language that's been the test case that people have
[766.12 --> 767.82]  been developing towards has been English.
[767.82 --> 773.08]  And so that's the way that and so you can really see that bias in the the way that the
[773.08 --> 774.32]  algorithms have unfolded.
[774.32 --> 779.38]  And so even when algorithms touted as, you know, language independent, it's like, okay,
[779.52 --> 784.30]  the algorithm doesn't have any, you know, might not have any specific thing where you need
[784.30 --> 789.84]  to have a, you know, a resource that depends on a particular language, it'll still work better
[789.84 --> 794.86]  or worse depending on the characteristics of that language and the complexity of like an individual
[794.86 --> 800.02]  word versus a, you know, how free the word order is, like all of these things will affect that.
[800.68 --> 805.42]  So one of the things before we go too much further, I was wondering is kind of, I know,
[805.60 --> 808.40]  you know, we're talking about Spacey and I know you mentioned Prodigy.
[808.70 --> 813.36]  Is there anything else that Explosion AI does or is it really focused on those?
[813.64 --> 815.44]  We mostly are a developer tools company.
[815.56 --> 818.24]  So we definitely, we have a few other open source projects that are kind of cool.
[818.24 --> 822.06]  We have like some other projects in the pipeline and products that we're working on,
[822.18 --> 823.96]  but ultimately that's what we're doing.
[823.96 --> 825.22]  We're not doing consulting anymore.
[825.64 --> 830.30]  We haven't been doing consulting for a long time and we're building products for developers
[830.30 --> 834.12]  who are developing machine learning and AI systems.
[834.64 --> 834.70]  Okay.
[834.88 --> 835.14]  Gotcha.
[835.78 --> 835.94]  Yeah.
[836.06 --> 838.96]  And Prodigy, as you mentioned, is a data labeling system.
[839.06 --> 840.60]  Is that the best way to put it?
[840.64 --> 843.90]  I know that like, it's more than just a user interface.
[843.90 --> 848.14]  It's, it actually integrates with models and other things, right?
[848.48 --> 848.72]  Yeah.
[848.78 --> 848.96]  Yeah.
[848.96 --> 850.00]  It's like a Python library.
[850.00 --> 854.76]  I mean, we sometimes refer to the whole concept as machine teaching because it's, yeah, it's
[854.76 --> 858.42]  sometimes, it's often a bit more than just like annotating or labeling because if you think
[858.42 --> 861.94]  of labeling, you think of, okay, you just get presented with something and you assign some
[861.94 --> 862.88]  label and that's it.
[863.20 --> 867.50]  Whereas, you know, Prodigy really lets you script much more complex workflows, try out
[867.50 --> 872.34]  ideas, iterate on the label schemes, really develop the models and how you want to structure
[872.34 --> 872.86]  your data.
[872.86 --> 877.32]  But yeah, essentially it's, you can download it, you can install it, pip install it just
[877.32 --> 878.38]  like any other package.
[879.08 --> 883.28]  And then it runs on your machine, on your data, just like, you know, like back in the
[883.28 --> 887.70]  old days when you would buy Photoshop and then you download Photoshop and then you have
[887.70 --> 889.84]  Photoshop and then you can keep using Photoshop.
[890.84 --> 895.86]  We were chatting a bit before jumping on the podcast and you were mentioning that both
[895.86 --> 900.80]  of you are really passionate about the sort of workflow and production details of, of
[900.80 --> 905.94]  actually doing natural language processing, machine learning in, in a practical setting.
[905.94 --> 911.22]  Is that kind of where Prodigy came about, um, that you were seeing that, that slow down
[911.22 --> 916.16]  in terms of, I guess, machine teaching and iteration around models and all those things?
[916.60 --> 916.76]  Yeah.
[916.92 --> 919.14]  So it's definitely informed by that.
[919.22 --> 924.04]  Uh, so we already had this, you know, pretty strong hunch that annotation tooling was a missing
[924.04 --> 925.58]  piece in a lot of people's workflows.
[926.04 --> 929.20]  And when we were doing the consulting, it really confirmed this as well.
[929.20 --> 934.10]  So we sort of, the data, you know, annotation was really where people were lacking in the
[934.10 --> 935.76]  terms of the success of their projects.
[935.82 --> 940.08]  And if we were thinking about why somebody would fail at a natural language processing
[940.08 --> 944.48]  project, and, you know, indeed many of these projects are going to fail because it is
[944.48 --> 945.56]  exploratory and stuff.
[945.70 --> 950.14]  It would be around these data questions and around the questions of like, okay, they couldn't
[950.14 --> 955.00]  get the annotation scheme, uh, such that they could carve up the, the problem correctly
[955.00 --> 959.28]  to make the models work well, or they didn't have the annotations at all, or they had a
[959.28 --> 963.28]  process that too slow a feedback loop between the annotations and the developers.
[963.44 --> 966.20]  And all of these things were things which we wanted to address.
[966.20 --> 966.40]  Yeah.
[966.50 --> 970.32]  For a long time, I mean, people would just like, okay, even though the data was the core
[970.32 --> 974.68]  of the application and really what the whole model depended on, they would like just throw
[974.68 --> 979.34]  this on like Amazon Mechanical Turk, uh, with some like vague instructions and like, I don't
[979.34 --> 982.66]  know, some survey that looked like early 2000s online survey.
[982.66 --> 986.18]  And then wait to get the data back, get it back two weeks later.
[986.38 --> 987.78]  And then, yeah, it wasn't that great.
[987.88 --> 988.94]  That wasn't very surprising.
[989.56 --> 989.64]  Yeah.
[989.68 --> 992.82]  A lot of effort for not much, not much useful data.
[993.12 --> 993.52]  Right.
[993.60 --> 993.94]  Exactly.
[994.16 --> 999.36]  And, you know, it's, it's sort of interesting to take a step back and think about the economic
[999.36 --> 1004.32]  irrationalism of some of this stuff, because the data science salaries are pretty sky high
[1004.32 --> 1005.92]  and they've been sky high for a long time.
[1005.92 --> 1010.92]  And now even the, the machine costs of running the experiments are quite high as well.
[1010.92 --> 1015.80]  And if you look at all of the like, you know, efficacy of those ingredients and how many
[1015.80 --> 1019.64]  thousands of dollars of investment are going into things, data should actually be pretty
[1019.64 --> 1020.00]  cheap.
[1020.08 --> 1022.24]  And, uh, the tooling is pretty cheap as well.
[1022.24 --> 1027.52]  So for want of like, you know, a thousand or $2,000 of annotation, people would be spending
[1027.52 --> 1031.70]  these, you know, tens of thousands of dollars on a project that, you know, basically will
[1031.70 --> 1032.46]  be doomed to fail.
[1032.46 --> 1039.80]  So you can spend way more computation and try to eke out like a longer hyperparameter search
[1039.80 --> 1040.82]  and get an extra 1%.
[1040.82 --> 1046.12]  Or if you annotated like four times as much data and for like about $4,000, maybe you'd
[1046.12 --> 1048.36]  get like an extra 12%, um, 10%.
[1048.36 --> 1054.38]  Uh, so it's pretty starkly far more effective to be optimizing at that end of the scale.
[1054.38 --> 1054.82]  Yeah.
[1055.06 --> 1058.90]  And so if that's what you're doing also very early on, we saw, well, the problem is not
[1058.90 --> 1060.64]  even, not the fact that we have to collect data.
[1060.68 --> 1065.30]  That's what people often, um, how people looked at this a lot, like, okay, we have to find
[1065.30 --> 1066.82]  methods like unsupervised learning.
[1066.96 --> 1068.94]  How can we like just not label anything anymore?
[1069.10 --> 1073.10]  It's like, well, labeling data is actually great because that's how you can program your
[1073.10 --> 1073.40]  model.
[1073.50 --> 1075.30]  Like you, you tell it what you wanted to predict.
[1075.62 --> 1077.36]  Um, the problem is the tooling.
[1077.46 --> 1080.28]  Like if, you know, if the tooling is bad, then yeah, okay.
[1080.28 --> 1081.44]  The data is going to be bad.
[1081.44 --> 1085.74]  And if we can improve the tooling and we can actually make it much more efficient and better
[1085.74 --> 1090.66]  to use more productive, then we can also end up with better data, better models, a better
[1090.66 --> 1091.76]  data science process.
[1092.38 --> 1096.72]  In particular, we saw that one of the problems that people had were, or one of the reasons
[1096.72 --> 1100.86]  why they hit the stumbling block on the annotation was that was often where people would hit the
[1100.86 --> 1101.94]  organizational boundaries.
[1102.64 --> 1107.38]  So that would be the part where, okay, you'd now needed to request a different type of budget
[1107.38 --> 1111.86]  or you needed to cross over into a different type of, you know, basically organizational
[1111.86 --> 1115.84]  thing, or you'd have to have a meeting with an upper level manager because the annotation
[1115.84 --> 1120.98]  team was like across an organizational boundary because they had some people who, you know,
[1120.98 --> 1122.00]  didn't have much else to do.
[1122.04 --> 1123.50]  So they became the annotation team.
[1123.82 --> 1129.26]  And so we saw that actually all of those things where you, you know, now you've got an idea and
[1129.26 --> 1130.32]  you want to train a model.
[1130.32 --> 1135.46]  And now it's like, okay, but then I have to schedule a meeting for next Wednesday, pitch
[1135.46 --> 1137.34]  my idea and get buy-in for this.
[1137.46 --> 1140.18]  And I'm not at all sure that this idea will actually succeed.
[1140.60 --> 1144.26]  So that's really where the innovation or iteration speed goes to die.
[1144.72 --> 1150.20]  And that's why we actually set it up to be much more built for rapid prototyping so that
[1150.20 --> 1154.40]  data scientists could do some of this annotation themselves and say, all right, well, if I've got
[1154.40 --> 1157.60]  an idea, I don't need to ask anybody's permission about this.
[1157.60 --> 1162.22]  I can do the annotation to test it out over, you know, between now and lunchtime.
[1162.54 --> 1166.74]  And, you know, it's just sort of part of my daily work or like, you know, okay, I experimented
[1166.74 --> 1172.12]  with this and it's not something where you need to, you know, basically taking all of your
[1172.12 --> 1175.98]  hair brand schemes up to management and pitching them in meetings because that's not a productive
[1175.98 --> 1176.60]  way to work.
[1187.60 --> 1193.38]  This episode is brought to you by Brave.
[1193.54 --> 1195.22]  Big news from the Brave team.
[1195.42 --> 1197.22]  Version 1.0 is official.
[1197.58 --> 1202.34]  That means our favorite open source, privacy focused, blazing fast browser is ready for
[1202.34 --> 1202.86]  prime time.
[1203.20 --> 1206.50]  Their brand new iOS app landed just in time for the announcement.
[1206.76 --> 1211.68]  And the Brave team is celebrating by granting 8 million basic attention tokens to the community.
[1211.68 --> 1216.14]  That means when you download the iOS app, you get 20 baht absolutely free.
[1216.44 --> 1221.40]  Put it to good use by heading to changelog.com, hitting the triangle icon in the upper right
[1221.40 --> 1223.40]  hand corner and flipping us a tip.
[1223.40 --> 1241.08]  So I'd love to switch directions just a little bit here.
[1241.08 --> 1248.34]  I saw one of your recent blog posts, which was talking about state of the art NLP models.
[1248.34 --> 1253.60]  And there's a sort of simple four step formula for a lot of these models.
[1253.60 --> 1259.76]  And I think that might be a good way to maybe introduce people to state of the art NLP.
[1260.08 --> 1265.74]  And also, I found it really useful myself to kind of have that scaffolding in my mind as
[1265.74 --> 1266.84]  I'm approaching these problems.
[1266.84 --> 1272.46]  So I was wondering if you could introduce that formula a bit for these state of the art NLP
[1272.46 --> 1272.88]  models.
[1273.54 --> 1273.70]  Sure.
[1273.94 --> 1275.12]  So let me see.
[1275.12 --> 1280.46]  So I guess one way to think about it is that these neural network models are all these sort
[1280.46 --> 1282.48]  of trainable functions that you can plug together.
[1282.68 --> 1286.26]  So the details of like exactly how they work sort of differ.
[1286.38 --> 1289.18]  And there's lots of different ideas for those individual components.
[1289.56 --> 1293.64]  But you can kind of take a step back and think about them as the input outputs of them.
[1294.04 --> 1298.26]  So one type of input that you'll have for language is, well, it's always going to kind of be a
[1298.26 --> 1299.76]  sequence of these discrete symbols.
[1300.02 --> 1301.88]  So at least if it's text data, right?
[1301.88 --> 1306.88]  So it'll either be a sequence of like characters and, you know, then you'll have an ID per character,
[1306.88 --> 1311.34]  or it'll be a sequence of words, or you could chunk it up into different segments that you've
[1311.34 --> 1312.28]  got like different IDs.
[1312.42 --> 1315.64]  But it's going to come in as this stream of like numeric identifiers.
[1315.88 --> 1320.54]  So the first transform that you want to perform if you want to apply neural networks to this
[1320.54 --> 1328.56]  type of input is you need to take somehow take those that sequence of discrete IDs and map it into a dense
[1328.56 --> 1329.06]  representation.
[1329.06 --> 1330.32]  So vectors.
[1330.54 --> 1336.14]  So the simplest way to do this is to just have sort of a lookup table where, you know, let's say you've
[1336.14 --> 1338.50]  got a vocabulary of, I don't know, 10,000 words.
[1338.66 --> 1343.06]  It'll be a table of like, you know, with 10,000 rows and say 300 dimensions.
[1343.06 --> 1348.38]  And then you'll take some word and it might be like, you know, the 50th most frequent word in
[1348.38 --> 1348.90]  your vocabulary.
[1349.42 --> 1351.52]  So you'll select like row 50 of that table.
[1352.02 --> 1354.68]  And then that embedding table will be the parameters of the model.
[1354.80 --> 1359.78]  And you'll sort of train this to have representations where similar words are sort of mapped to a similar
[1359.78 --> 1360.12]  meaning.
[1360.22 --> 1362.58]  So you'd hope that dog and puppy will have similar vectors.
[1363.20 --> 1366.34]  And I don't know, drink and eat will have similar vectors.
[1366.34 --> 1368.86]  And, you know, it'll all kind of work out as this sort of vector space.
[1369.08 --> 1370.90]  So that's the first embed step.
[1370.90 --> 1376.06]  Yeah. So basically neural networks like to act or like to operate on numbers.
[1376.34 --> 1381.66]  Right. And so when you have these sequence of symbols or characters or words or whatever it is,
[1381.88 --> 1384.20]  in some way you have to represent that in numbers.
[1384.20 --> 1384.56]  Correct.
[1385.12 --> 1389.76]  Sure. You know, in fact, every machine learning algorithm, neural or otherwise, is going to
[1389.76 --> 1391.46]  need to work on numbers in some way.
[1391.94 --> 1396.08]  The thing that was like, I guess, a puzzling challenge when I first started using neural
[1396.08 --> 1400.46]  networks as opposed to the other models which we were working with is the other models really
[1400.46 --> 1402.16]  like having sparse representations.
[1402.56 --> 1405.72]  Like, you know, you can have an idea that's sort of just a key in a dictionary and it
[1405.72 --> 1409.52]  doesn't matter how many keys you have or like doesn't matter what the total space of the
[1409.52 --> 1412.12]  keys is. You only care about which ones you happen to see.
[1412.62 --> 1413.94]  In neural networks, it's not like that.
[1414.00 --> 1418.22]  You want to have a denser representation where you've got like some relationship between
[1418.22 --> 1418.56]  those.
[1418.90 --> 1423.02]  And that's kind of nice in that, you know, even if you haven't seen many examples of a
[1423.02 --> 1426.84]  puppy, I know that it's going to have a similar representation to this other word.
[1426.84 --> 1432.28]  So you've kind of got that sort of, you know, relationship between things in a denser representation.
[1432.28 --> 1434.60]  And that's one of the advantages of neural networks.
[1434.90 --> 1439.16]  Yeah. I mean, ultimately, I think the main challenge is always there's so much knowledge
[1439.16 --> 1442.90]  about the world and the language that we kind of encode in text.
[1442.90 --> 1448.12]  And we want to be able to encode as much as possible about all of this extra knowledge
[1448.12 --> 1449.72]  in our model as well.
[1449.86 --> 1454.18]  And that's also if you look at, yeah, the recent developments in NLP, that's kind of
[1454.18 --> 1455.66]  what it all circles back to.
[1456.24 --> 1459.62]  And that's also, you know, the better the representations, the more we can do.
[1460.12 --> 1463.48]  Actually, you already said the word I was about to ask about and that was encoding.
[1463.96 --> 1466.26]  If you would go there when you're ready.
[1466.72 --> 1466.96]  Right.
[1467.22 --> 1471.30]  So the next step, you know, if you've got this fourth step, it's like embed, encode.
[1471.30 --> 1476.38]  So after we've got like, you know, a vector representation for these word IDs, well, we're
[1476.38 --> 1479.68]  still at the stage where the vectors are kind of, you know, isolated.
[1479.80 --> 1484.66]  You've just looked up this word ID and you're going to have the same representation for that
[1484.66 --> 1486.46]  word type, regardless of its context.
[1486.66 --> 1492.48]  So every time I see a word like duck, I'll have the same representation, whether it's a
[1492.48 --> 1496.64]  noun or a verb or, you know, so I'm not getting any sense of its like sense and context.
[1496.90 --> 1501.06]  So the next step that we want to do is sort of rewrite those vectors based on the words
[1501.06 --> 1505.86]  around them so that if we're based on the surrounding context, I can get another representation
[1505.86 --> 1506.34]  out.
[1506.62 --> 1512.48]  So this is a sort of input type that takes like, you know, this sequence of vectors and
[1512.48 --> 1517.26]  it outputs a sequence of vectors with, you know, taking into account the linear order
[1517.26 --> 1519.32]  of the vectors that were put in.
[1519.64 --> 1522.86]  So we take an unordered set and we output like an ordered set.
[1523.34 --> 1524.46]  Well, wait, that's not quite right.
[1524.46 --> 1530.04]  Basically, we take the same sort of dimensions of like input and output, but now we've encoded
[1530.04 --> 1531.58]  the context around it.
[1531.94 --> 1538.12]  So one way of doing this is to say, OK, I'll just concatenate the vectors for each word
[1538.12 --> 1540.10]  with some of its surrounding context.
[1540.26 --> 1543.06]  And I'll use that to recalculate that vector.
[1543.22 --> 1545.18]  So this is a convolutional operation.
[1545.66 --> 1548.28]  Or you can have a, you can read them in turn.
[1548.40 --> 1552.82]  And at each point, remember that something of the context before and rewrite the vector based
[1552.82 --> 1553.16]  on that.
[1553.24 --> 1555.10]  So that's something like a recurrent neural network.
[1555.66 --> 1559.76]  But regardless of which, you know, method you use to encode that context, we probably
[1559.76 --> 1563.80]  want something like this, because if we don't have something like that, then we're not going
[1563.80 --> 1566.72]  to be able to see the meaning of the sentence together.
[1566.72 --> 1570.78]  We'll have to just see the sentences, you know, the sum of its words or something, which
[1570.78 --> 1572.54]  is not the way that language actually behaves.
[1572.62 --> 1578.32]  Yeah, I noticed in the article, you talk about both LSTMs and GRU architectures working well
[1578.32 --> 1578.72]  for that.
[1578.82 --> 1582.80]  Do you have a preference or is there one that you would recommend over the...
[1582.82 --> 1588.28]  So these days, the transformer architecture is, you know, better than the LSTM for most
[1588.28 --> 1594.44]  situations, partly because it's just more amenable to the way that GPU performance characteristics
[1594.44 --> 1594.98]  work.
[1595.56 --> 1599.42]  So that's the one which pretty much everybody's using in place of the LSTM these days.
[1599.88 --> 1604.80]  Because we want Spacy to work well in relatively small networks that you can, you know, use it
[1604.80 --> 1608.14]  without a GPU, we use a convolutional architecture instead.
[1608.14 --> 1613.94]  But I would say that those are, you know, basically the two architecture types that I use for the
[1613.94 --> 1614.68]  encoding step.
[1615.06 --> 1618.88]  The LSTMs are still sort of useful, but in most situations, like, you know, especially
[1618.88 --> 1620.64]  for larger models, transformers work better.
[1621.46 --> 1624.18]  So you mentioned the embed and encode.
[1624.68 --> 1629.30]  Apparently, I've heard attention is all you need and you have a step that's attend.
[1629.30 --> 1631.54]  And so maybe just...
[1631.54 --> 1634.12]  So I think the two steps left are attend and predict.
[1634.36 --> 1636.54]  Why is the attend step important?
[1637.02 --> 1639.86]  So I should probably have called this reduce rather than attend.
[1640.66 --> 1645.82]  I guess I was kind of hinting at, like, you know, the attention layers were getting a lot
[1645.82 --> 1646.80]  of attention at the time.
[1646.88 --> 1649.18]  And it really would have been more useful to call it reduce.
[1649.44 --> 1654.58]  So the input and output types of this, you take, like, your matrix of things where you've
[1654.58 --> 1655.74]  got one row per word.
[1655.74 --> 1659.16]  And you basically want to get some sort of summary vector out of that.
[1659.36 --> 1663.34]  So, you know, I want a representation for the whole sentence rather than just a representation
[1663.34 --> 1665.76]  that includes all of the words of the sentence.
[1665.98 --> 1670.24]  So the simplest type of this would be just summing them all up or taking the average of
[1670.24 --> 1670.74]  them or something.
[1671.04 --> 1676.02]  But you can also take a, you know, basically more parametric ways of doing this and have
[1676.02 --> 1678.74]  one of these attention layers or something like that.
[1679.06 --> 1683.22]  You can also use an LSTM for this as well and just take the output state.
[1683.22 --> 1686.74]  So there's, again, a variety of ways of, you know, framing this.
[1687.00 --> 1691.22]  But it's essentially just a reduction operation where we take, you know, a matrix and we output
[1691.22 --> 1691.62]  a vector.
[1692.22 --> 1697.04]  And then finally, the predict step is we take a vector and we want to get an ID out.
[1697.44 --> 1701.42]  So that's kind of the last, you know, type of thing that we want to do.
[1701.98 --> 1705.94]  So, you know, if we think of those as the sort of four data types or four, like, you know,
[1706.16 --> 1708.62]  signatures that we're going to have in these networks.
[1708.62 --> 1714.16]  Well, we're probably going to be, you know, basically composing layers that look like that.
[1714.66 --> 1717.98]  And then there'll be other details for ones where you've got like, you know, two vectors
[1717.98 --> 1720.44]  as the import and then you want to attend over them.
[1720.52 --> 1722.54]  But mostly that's what we kind of want to do.
[1723.26 --> 1727.08]  And then I guess in the end, you have to predict something, right?
[1727.76 --> 1727.92]  Sure.
[1727.92 --> 1734.20]  So you've got the reduced vector outputs, a single vector, and then the prediction.
[1734.48 --> 1738.64]  Is it kind of the opposite of where you started with the embedding?
[1739.34 --> 1741.10]  Actually, you can kind of think of it that way.
[1741.28 --> 1743.76]  But you can also just think of it kind of like a linear model.
[1743.92 --> 1750.14]  And you're just going to say, all right, take a weighted sum of this input vector and
[1750.14 --> 1750.64]  some weights.
[1750.80 --> 1754.72]  And at the end of it, I'll like, you know, do some sort of max operation and say, OK,
[1754.72 --> 1756.14]  that's the one with the highest score.
[1756.14 --> 1760.00]  So it's just like other types of like, you know, machine learning models.
[1760.84 --> 1765.54]  So I'm assuming that kind of getting back to where we started with with Spacey, I'm assuming
[1765.54 --> 1772.86]  that Spacey can help you do some of the things that we've just talked about in this formula,
[1772.86 --> 1775.00]  but maybe there's other things as well.
[1775.42 --> 1779.26]  What's the sort of range of things that you can do with Spacey, I guess?
[1779.64 --> 1784.04]  Well, first, Spacey is really a library that lets you put together a whole NLP pipeline
[1784.04 --> 1787.98]  of the different things you might want to do and extract from your text.
[1788.20 --> 1791.22]  So, you know, often that's like, you know, you're not just interested in predicting one
[1791.22 --> 1791.52]  thing.
[1791.62 --> 1793.36]  You might want to read in your text.
[1793.44 --> 1794.94]  You want to find the individual sentences.
[1795.40 --> 1800.98]  You want to find out which concepts are mentioned in the text, like which person names, organizations,
[1801.74 --> 1802.12]  dates.
[1802.34 --> 1805.90]  And then you also maybe want to predict something about like what's in the text.
[1805.90 --> 1809.98]  And maybe later you want to relate these things that you've extracted to each other and
[1809.98 --> 1810.84]  compute something else.
[1810.84 --> 1815.52]  So the idea of Spacey is you have a pipeline, you can plug in functions into your pipeline.
[1815.64 --> 1818.40]  Some of them can be these machine learning models.
[1818.58 --> 1820.28]  Others can just be a function.
[1820.52 --> 1822.52]  Others, you can write some regular expressions.
[1822.78 --> 1824.20]  You can do whatever you need.
[1824.42 --> 1826.76]  And that's kind of the core principle of Spacey.
[1826.86 --> 1832.26]  We always had our own implementations that, you know, usually have a good trade-off of accuracy
[1832.26 --> 1834.80]  and speed, especially also on CPU.
[1835.04 --> 1837.98]  But you can also write your own models, plug them in.
[1837.98 --> 1843.46]  And then at the end of it, you can feed in your text and extract things from your text
[1843.46 --> 1844.40]  at a very large scale.
[1845.24 --> 1848.46]  So I guess I'm curious, like, how would you implement a pre-trained model?
[1848.56 --> 1850.98]  How does that fit into Spacey as a component?
[1851.26 --> 1855.24]  And, you know, maybe contrast that with if you were going to do it from scratch, how would
[1855.24 --> 1855.66]  you do that?
[1855.82 --> 1857.62]  How does that change the workflow for you?
[1858.16 --> 1860.84]  So it depends on exactly what you mean by pre-trained.
[1861.36 --> 1864.76]  Do you mean a model that's been trained for a particular task?
[1864.76 --> 1869.48]  Or do you mean, you know, weights that have been initialized with some language that you
[1869.48 --> 1872.00]  can then sort of leverage the knowledge from them?
[1872.80 --> 1876.20]  I think from my standpoint, I'm thinking of kind of doing transfer learning.
[1876.56 --> 1881.86]  And as the newbie in this group, if I was going to dive into it and I'm taking somebody
[1881.86 --> 1887.52]  else's model that I want to utilize for a particular task and I'm wanting to stand on
[1887.52 --> 1891.28]  the shoulders of giants before me, how would I go about doing that as a newbie versus
[1891.28 --> 1895.90]  someone like Daniel, who's done tons and tons of work in this space?
[1896.12 --> 1898.44]  And maybe he's wanting to go in and do one from scratch.
[1898.60 --> 1900.74]  How would it be different for me and Daniel?
[1901.48 --> 1901.66]  Okay.
[1901.76 --> 1904.90]  So there's a number of different technologies around this.
[1905.22 --> 1909.64]  So, you know, most of your effort is still going to be around, like, you know, creating
[1909.64 --> 1912.84]  the annotations for the specific problem that you want to do.
[1912.84 --> 1918.64]  And I would actually say that, you know, okay, you should sort of mostly be thinking about
[1918.64 --> 1922.96]  and focusing on getting the questions around that right, because there's actually a surprising
[1922.96 --> 1926.54]  number of choices to be made in how you frame the annotation problems.
[1926.80 --> 1931.66]  So, for instance, you know, we have a number of users who want to work on medical text, right?
[1931.82 --> 1935.56]  And they say, okay, I want to recognize symptoms.
[1935.56 --> 1941.32]  And so then naively, you'd say, well, okay, if this says, you know, patient suffers from
[1941.32 --> 1945.64]  asthma, that should be counted as like, you know, recognized as a symptom, and that should
[1945.64 --> 1946.16]  be highlighted.
[1946.34 --> 1950.16]  And then if I have another one where it says, you know, patient used to suffer from asthma,
[1950.16 --> 1952.84]  then that shouldn't be recognized as a symptom.
[1953.54 --> 1957.34]  And so the sort of immediate intuition is, okay, that's the annotation scheme.
[1957.40 --> 1958.44]  That's what I should annotate.
[1958.68 --> 1963.44]  But that way of framing the problem will be vastly harder to recognize for the models, because
[1963.44 --> 1968.58]  you're coupling the two pieces of information about, you know, the mention of this thing
[1968.58 --> 1971.12]  and whether it actually was exhibited or not.
[1971.50 --> 1976.06]  And if you can find ways of framing the problems that you factor out those pieces of information,
[1976.06 --> 1976.84]  it's a lot easier.
[1977.18 --> 1981.12]  So I would say as a newbie starting out, that would actually be where most of the complexity
[1981.12 --> 1981.72]  lies.
[1982.18 --> 1987.44]  Then in terms of the actual software of using the pre-training, Spacey has one facility,
[1987.58 --> 1991.26]  which is just this command pre-train, and you can either download the weight, some weights
[1991.26 --> 1992.84]  from us or use it yourself.
[1993.00 --> 1996.18]  And that will, you can use that to initialize in Spacey Train.
[1996.54 --> 2000.72]  And then we're also working on, you know, better support for transformer models in our
[2000.72 --> 2004.88]  library Spacey Transformers that you can use to BERT and ExcelNet models that have been
[2004.88 --> 2006.76]  trained on lots of text.
[2006.90 --> 2007.02]  Yeah.
[2007.10 --> 2011.22]  Or even if you're starting, just starting out, even just like plain old word vectors,
[2011.64 --> 2015.76]  like the common crawl glove vectors have been trained on a lot of text.
[2015.98 --> 2018.28]  Even that can give you like a nice little boost.
[2018.28 --> 2019.58]  And that's like super easy to use.
[2019.66 --> 2022.16]  You don't have to think much about, you know, how it interacts.
[2022.66 --> 2024.30]  You just initialize your model with that.
[2024.30 --> 2028.76]  Then you, you know, write a little script that trains your model on your data.
[2029.24 --> 2031.74]  And then hopefully you get some nice results out at the end.
[2032.52 --> 2039.48]  So I think what you emphasized before in terms of NLP often being like a series of tasks that
[2039.48 --> 2044.74]  you want to string together often, because there is so much pre-processing and there's like
[2044.74 --> 2047.62]  multiple things that you might want to infer from text.
[2047.62 --> 2050.08]  And you've mentioned a couple of things like tokenization.
[2050.50 --> 2054.26]  You've mentioned finding certain things in the text, which I think you're referring to
[2054.26 --> 2059.68]  like finding entities, like people or organizations that would like named entities in, in text.
[2059.80 --> 2065.52]  I was wondering, so those are kind of building blocks that you can put together in these pipelines.
[2065.52 --> 2070.00]  I was wondering if you could mention maybe just some of the, some of the most frequently
[2070.00 --> 2073.36]  used of those sorts of building blocks in Spacey.
[2073.36 --> 2077.82]  And I'd also be curious because I have my own perspective from different things that
[2077.82 --> 2078.12]  I've done.
[2078.20 --> 2084.90]  I was curious as you view like the community using Spacey, have you been surprised by which
[2084.90 --> 2091.10]  ones of those things have been like used most or people have found most useful?
[2091.10 --> 2094.14]  Or maybe it's the things that you thought they would find useful.
[2094.58 --> 2094.84]  Yeah.
[2095.08 --> 2096.64]  I'd be interested to hear some of that.
[2096.64 --> 2097.16]  Yeah.
[2097.16 --> 2101.52]  So I think definitely what people use the most is named entity recognition, as you just
[2101.52 --> 2105.62]  mentioned, and text classification, where you really predict one label over the whole text.
[2105.94 --> 2110.10]  We also, our default pipelines will also ship with a dependent, with a part of speech tagger.
[2110.22 --> 2115.30]  So you can, you know, predict whether a word is a verb or noun and the dependency parser.
[2115.40 --> 2117.90]  So you can predict the relationships between the words.
[2118.14 --> 2122.54]  And for example, find out what's the subject and what's the object, because that's also quite
[2122.54 --> 2123.14]  important.
[2123.14 --> 2126.78]  And that's maybe one example where we think, oh, actually, the dependency pars can in some
[2126.78 --> 2128.74]  cases be quite useful.
[2128.74 --> 2133.86]  But of course, you know, that's maybe, it's maybe not as popular as it used to be, because,
[2133.86 --> 2137.50]  you know, we now have better ways of predicting these things end to end.
[2137.74 --> 2142.84]  But definitely, it makes total sense to me why people would want to use named entity recognition
[2142.84 --> 2148.32]  and text classification, because that's, you know, the most useful information you can extract
[2148.32 --> 2152.16]  that also you can then translate into the business problem.
[2152.16 --> 2153.38]  You're actually trying to solve.
[2153.80 --> 2154.44]  And yeah.
[2154.52 --> 2157.86]  And one other thing, the rule-based entity recognition, that was actually, and the matching,
[2157.98 --> 2160.98]  that's something I'm actually quite happy to see people use more.
[2161.08 --> 2162.02]  And that's actually very popular.
[2162.42 --> 2166.24]  So you can, it's, you can think of it kind of like regular expressions, only that you can
[2166.24 --> 2170.84]  write rules that really take advantage of the token attributes and maybe even things that
[2170.84 --> 2171.72]  the model predicted.
[2171.88 --> 2178.04]  So you can say, I want the word duck, but only if it's a noun and not a verb.
[2178.04 --> 2183.70]  And then I want to also extract an adjective, if there is an adjective, otherwise not.
[2184.72 --> 2186.76]  And you can, you can basically, you can write rules like that.
[2186.78 --> 2190.46]  And then also use that to extract more complex information.
[2190.46 --> 2195.46]  And for many, many tasks, this is actually a really, really powerful tool and works much,
[2195.54 --> 2198.72]  much better than just trying to predict all of it end to end somehow.
[2198.72 --> 2204.68]  So it's nice to see people use these hybrid workflows of statistical models and rule-based
[2204.68 --> 2205.36]  systems.
[2205.68 --> 2206.28]  Yes.
[2206.44 --> 2212.98]  I'm so glad you mentioned that because I think it is often overlooked and especially for maybe
[2212.98 --> 2219.90]  cases where you don't have as much data, you know, lower resource languages or something
[2219.90 --> 2220.40]  like that.
[2220.82 --> 2223.70]  You know, statistical and rule-based approaches can be really powerful.
[2223.70 --> 2229.04]  I know recently we were trying to figure out how should we predict if a certain sentence
[2229.04 --> 2230.58]  is a question or a statement.
[2231.14 --> 2235.96]  And we looked into various things and we tried out various things like, you know, text classification
[2235.96 --> 2238.62]  and like a larger model and all these things.
[2238.74 --> 2244.96]  But it ended up just some simple rules performed pretty much as good as any model we could train.
[2245.26 --> 2248.18]  So it was like, I could see how it could be overlooked a lot.
[2248.30 --> 2251.06]  And I don't know if you see that a lot.
[2251.44 --> 2252.54]  We hear that a lot as well.
[2252.54 --> 2254.36]  Also, sometimes it comes from within the organization.
[2254.56 --> 2257.64]  Like I often talk to people who are like, oh, I need to extract digits for my text.
[2257.72 --> 2259.32]  How can I do that with the entity recognizer?
[2259.64 --> 2260.84]  And I'm like, actual digits?
[2260.96 --> 2262.88]  Well, you just write like a reg ex, right?
[2263.00 --> 2263.68]  And they're like, no, no.
[2263.74 --> 2266.24]  My manager says we need to use like NLP.
[2266.52 --> 2267.62]  But that's not as cool.
[2268.12 --> 2269.50]  Yeah, we need to train a model.
[2269.94 --> 2275.58]  And I'm like, God, that's like, you know, I'm sorry for your position in that company
[2275.58 --> 2276.50]  because that really sucks.
[2276.82 --> 2279.56]  But stuff like that, definitely.
[2279.56 --> 2283.56]  Or another thing we always try to tell people is this thing about like, okay, build at least
[2283.56 --> 2286.04]  some rule-based baseline that you're looking to beat.
[2286.16 --> 2288.72]  Like, for example, for your question task.
[2289.04 --> 2293.16]  Like, you do want to find out how far do I get if I just check whether the last character
[2293.16 --> 2297.14]  is a question mark before you start like predicting things.
[2297.16 --> 2298.60]  Which is surprisingly a long way.
[2298.60 --> 2302.78]  Yeah, and maybe you're like, whoa, that's 80% or 85%.
[2302.78 --> 2304.74]  You're like, well, okay, that's good to know.
[2304.82 --> 2309.76]  Because if your fancy machine learning model only gets 82%, out of context, that would look
[2309.76 --> 2310.18]  pretty good.
[2310.24 --> 2311.48]  And maybe, you know, you could show this off.
[2311.52 --> 2312.78]  And it's like, wow, that's great results.
[2312.90 --> 2318.18]  But if checking the last character gives you a higher accuracy, then yeah, that's probably
[2318.18 --> 2319.86]  not what you want to ship.
[2319.86 --> 2326.16]  Yeah, this is, it's especially important with the deep neural networks, because it used
[2326.16 --> 2331.44]  to be that, okay, if you can pretty much rely on some of the other models and like sort
[2331.44 --> 2335.34]  of reverse engineering or getting the accuracy that you would get from the simple rules.
[2335.50 --> 2341.52]  But you can, training a deep neural network, you're often sort of running blind and you
[2341.52 --> 2343.24]  have no idea whether the score is any good.
[2343.32 --> 2347.60]  And you can find that, okay, actually, I'm dramatically underperforming like, you know, a bag of words
[2347.60 --> 2348.52]  baseline or something.
[2348.52 --> 2353.40]  And so part of the, it's very helpful to have this sort of existence proof of knowing where
[2353.40 --> 2357.68]  you should be, because then you know, like, you know, okay, what to keep trying or when
[2357.68 --> 2359.04]  to keep trying and that sort of thing.
[2359.16 --> 2362.76]  So I definitely feel like having that sort of perspective on where you are or where you
[2362.76 --> 2364.24]  should be is very helpful.
[2364.68 --> 2369.98]  So one of the things that I was wondering was, I noticed that you talk about Spacey being
[2369.98 --> 2373.32]  designed intentionally to be blazingly fast.
[2373.74 --> 2378.50]  So it begs the question for me about, you know, kind of if you're focusing on performance,
[2378.52 --> 2382.22]  what are some of your strategies for making Spacey blazingly fast?
[2382.44 --> 2386.44]  And also, because we're talking about performance, it also makes me wonder, okay, who are your
[2386.44 --> 2391.66]  target users on that versus like, what I mean by that is, are you from a performance standpoint,
[2391.66 --> 2395.04]  are you thinking more about the data scientists that are creating the models?
[2395.18 --> 2398.82]  Are you thinking more about the engineers and the fact that for deployment and such?
[2398.82 --> 2403.02]  Because I also noticed that you, you talk about its production, you know, really focused
[2403.02 --> 2403.58]  on production.
[2403.74 --> 2407.10]  Could you speak a little bit toward performance and target users for that performance?
[2407.88 --> 2408.02]  Sure.
[2408.18 --> 2414.12]  So the things that are important for performance have kind of changed over time as the technologies
[2414.12 --> 2414.96]  have changed.
[2414.96 --> 2420.30]  So it used to be that the fact that it was, you know, basically implemented from, you know,
[2420.34 --> 2424.58]  the ground up in Scython was, you know, very important for some of the performance aspects
[2424.58 --> 2428.84]  because the actual maths that was being done in the model were kind of simple.
[2429.06 --> 2433.56]  So it was very important that all of the data structures were in, you know, basically memory
[2433.56 --> 2434.30]  managed code.
[2434.44 --> 2439.16]  Now that it's more around neural networks, some of those considerations are a bit different
[2439.16 --> 2442.70]  and there's a bit more forgiving and the Python layer can be a little bit slower because
[2442.70 --> 2446.88]  there's kind of more maths that's being done that, you know, is kind of a slower bit that
[2446.88 --> 2449.20]  masks the performance of the other parts.
[2449.76 --> 2456.84]  So I would say in terms of the sort of target use case, I think to keep in mind about natural
[2456.84 --> 2461.62]  language processing is that the problem sizes constantly get bigger and this will continue
[2461.62 --> 2464.86]  for, you know, a wide range of companies and wide range of applications.
[2465.26 --> 2470.32]  So the working set of like, you know, a problem that you're trying to handle will constantly
[2470.32 --> 2471.26]  accelerate.
[2471.26 --> 2475.86]  So let's say you're a news site or something, the volume of comments you're processing or
[2475.86 --> 2479.24]  the number of articles in your archive, all of that's growing.
[2479.52 --> 2482.14]  And in many cases, it's actually growing faster than Moore's law.
[2482.70 --> 2487.14]  So the sort of standard approach that people have for computational efficiency of, well,
[2487.16 --> 2489.86]  I'll not worry and it'll just kind of stop being a problem.
[2489.98 --> 2491.50]  It'll just kind of inflate away.
[2491.68 --> 2495.38]  It doesn't actually work so well for a lot of the problems that we want to do with natural
[2495.38 --> 2496.14]  language processing.
[2496.14 --> 2500.94]  If you want to work on the Twitter firehose or other social media monitoring, again, the
[2500.94 --> 2504.08]  problem size gets bigger faster than computation gets cheaper.
[2504.30 --> 2509.08]  So we need to actually worry about the models being quick enough to work on those things.
[2509.24 --> 2514.74]  The other consideration is that if you make the model slow, then deploying them over a
[2514.74 --> 2520.02]  very large cluster is just, it's a hassle that's never going to get easy.
[2520.02 --> 2525.06]  Like the more instances you have to spin up to just harder the problem gets, you get failures
[2525.06 --> 2529.58]  of the nodes, you get, it's just hard to be marshalling work over a very large number
[2529.58 --> 2530.12]  of workers.
[2530.66 --> 2535.00]  And so if we can make the models like, you know, 50 or a hundred times faster than the
[2535.00 --> 2539.54]  just operator expense of running things in practice gets a lot easier.
[2540.04 --> 2541.48]  And then finally, there's latency.
[2541.94 --> 2546.60]  So there's a lot of applications where you care a lot about the time to response of one
[2546.60 --> 2550.66]  or two things because you want to have the model in the loop of some sort of user facing
[2550.66 --> 2551.12]  decision.
[2551.62 --> 2553.88]  And there again, you need the models to be reasonably fast.
[2554.72 --> 2559.28]  So I'm going to switch directions a little bit here, maybe being that I'm working for
[2559.28 --> 2564.26]  an organization that, you know, whose vision it is to see people flourish in community with
[2564.26 --> 2566.00]  the languages that they use most.
[2566.16 --> 2569.74]  I would probably get fired if I didn't ask about language support.
[2569.74 --> 2576.84]  So there's a lot of languages and I'm guessing that, you know, various of these building blocks
[2576.84 --> 2580.58]  that you've discussed have support in certain languages and not other languages.
[2580.74 --> 2584.60]  I was wondering if you could speak a little bit to, I guess, first the current language
[2584.60 --> 2590.82]  support, but also what people can do to expand the language support of Spacey, how they can
[2590.82 --> 2593.12]  contribute, what's involved in that?
[2593.34 --> 2594.56]  What are the challenges of that?
[2595.04 --> 2595.26]  Yeah.
[2595.34 --> 2598.00]  So I don't actually know the number now.
[2598.00 --> 2600.84]  Like, I don't know how many languages do you support off the top of my head?
[2600.92 --> 2601.94]  I don't know.
[2602.00 --> 2605.76]  I don't know the number, but like it's in the docs, but we actually, so the base support
[2605.76 --> 2607.42]  for a lot of languages is there.
[2607.50 --> 2610.86]  And that usually just includes like, okay, just some tokenization rules, getting like
[2610.86 --> 2611.62]  basics right.
[2611.70 --> 2616.30]  But ultimately if you do anything for language and you want to train a model, that's kind
[2616.30 --> 2617.74]  of where the bottleneck is.
[2617.86 --> 2622.30]  And yeah, you can optimize algorithms for different languages, but ultimately it comes down to the
[2622.30 --> 2624.58]  data and being like a library that's used in production.
[2624.58 --> 2628.48]  And we are somewhat limited to like, okay, we need to source data.
[2628.68 --> 2632.96]  We need to source data sets that like can be used commercially that exist in the first
[2632.96 --> 2637.16]  place and that we can maybe pre-train models with, or that our users can use.
[2637.22 --> 2640.12]  And that's kind of what we're currently seeing is like the biggest problem.
[2640.12 --> 2644.86]  And that's kind of, that's not like anyone's fault directly, but like, that's kind of something
[2644.86 --> 2645.70]  we have to work with.
[2645.76 --> 2649.32]  And that's also why it's not so easy to, if people are like, oh, why don't you support,
[2649.64 --> 2653.06]  yeah, why don't you give me a perfect pre-trained model for insert language here?
[2653.20 --> 2655.94]  Or like, why does it, why can't you support this?
[2655.96 --> 2657.24]  So why is this language so bad?
[2657.26 --> 2660.82]  And it's like, well, we have to work with what's there.
[2660.90 --> 2663.28]  We have to, you know, we can run our own annotation projects.
[2663.28 --> 2665.46]  We can run our own data collection processes.
[2665.46 --> 2669.20]  But like, that's, that's really the main thing it comes down to.
[2669.90 --> 2675.00]  So have you seen contributions from various language communities around the world that
[2675.00 --> 2680.20]  really, you know, take ownership and contribute some of those models and the rules and all
[2680.20 --> 2680.62]  of that stuff?
[2681.26 --> 2683.60]  Yeah, so we've had a variety of contributions.
[2684.12 --> 2690.12]  So one that was particularly end-to-end and very effective was Janis Daris did a Google
[2690.12 --> 2693.62]  Summer of Code project where he contributed Greek support.
[2693.62 --> 2697.18]  We've had a number of people working on Indonesian.
[2697.64 --> 2700.08]  I think we had people working on Tamil.
[2700.68 --> 2704.18]  Yeah, we had like, you know, with some more custom, yeah, especially custom work.
[2704.28 --> 2709.88]  We definitely had a few users who went and used Prodigy to create their own NER annotations
[2709.88 --> 2712.58]  because that's also, you know, something that's usually lacking.
[2712.74 --> 2717.14]  We can have tree banks for dependency parsing and part of speech tagging.
[2717.32 --> 2720.74]  But like, entity recognition is like much more important to many users.
[2720.74 --> 2723.44]  And also there's not enough data we've had.
[2723.52 --> 2724.02]  What else do we have?
[2724.38 --> 2727.90]  So actually, yeah, I think some of the Nordic languages, they actually, I think Norwegian,
[2728.16 --> 2733.40]  they have like good, I think government-sponsored initiatives and publish, have published good
[2733.40 --> 2735.32]  corpora under public domain.
[2735.32 --> 2739.36]  And that's, of course, like incredibly helpful and also high quality data.
[2739.36 --> 2745.82]  And we've had users from the community who saw that and ran some experiments on it, got like pretty good results,
[2746.20 --> 2747.52]  shared that with the community.
[2747.90 --> 2751.92]  And that meant we were able to ship a Norwegian Spacey model, for example,
[2751.98 --> 2754.00]  like a base model that people can build on top of.
[2754.70 --> 2755.44]  That's awesome.
[2755.88 --> 2759.02]  Another one that's like, you know, very notable is,
[2759.20 --> 2764.02]  so the Japanese support for a long time has been driven by Paula Leary-McCann,
[2764.02 --> 2766.88]  who's now doing freelance work.
[2767.02 --> 2773.84]  So if anybody's listening and they, you know, want to work on Japanese projects and they need assistance with this,
[2774.00 --> 2776.40]  he'll be, he's a great person to get in touch with.
[2776.50 --> 2778.86]  And, you know, you can email me for the contact for him.
[2779.74 --> 2784.24]  Yeah, he's been really driving all the, yeah, all the Japanese, Spacey and Japanese stuff.
[2784.52 --> 2787.60]  There's another group in Japan who've been working with Spacey,
[2787.66 --> 2789.40]  and they've got their own library for this as well.
[2789.40 --> 2793.76]  So, you know, there's a number of contributions around that.
[2794.28 --> 2797.80]  I would say for something like, you know, the perspective of SIL,
[2798.24 --> 2800.80]  if you're thinking about the vast number of languages in the world,
[2800.96 --> 2804.66]  well, tools like Spacey are kind of designed around different use cases.
[2804.82 --> 2808.40]  Like Spacey is actually designed for, you know, written text processing.
[2808.40 --> 2811.92]  And so for a great number of languages, it's, you know,
[2812.26 --> 2814.50]  it's a little bit putting the cart before the horse because you say,
[2814.58 --> 2817.32]  okay, I can make this tool that can process lots of text,
[2817.32 --> 2820.38]  but what written text do I actually have to process?
[2820.86 --> 2824.46]  So if you're in a situation where the language actually doesn't have much written text,
[2824.80 --> 2828.64]  then, you know, okay, it'll be quite difficult to get Spacey running with things.
[2828.88 --> 2832.58]  But on the other hand, also Spacey wouldn't really be solving a useful problem for you either.
[2833.10 --> 2836.80]  And so I'd say that's actually the position of, you know, most languages, right?
[2836.96 --> 2840.58]  The other thing is that for those languages, which, you know, sort of less typically written,
[2840.90 --> 2843.96]  well, at least the writing system tends to have been designed by linguists.
[2843.96 --> 2848.18]  And so they tend to be easier to tokenize than languages with, you know,
[2848.24 --> 2850.80]  slightly more complex histories around their writing system.
[2851.38 --> 2857.70]  Sure. Yeah. And yeah, I mean, there's a lot of great efforts.
[2858.10 --> 2867.74]  I know the Masa Kanye project right now in Africa is working on NLP tools for a lot of African languages.
[2867.74 --> 2871.54]  And, you know, trying to, I think it's also the Zendi effort.
[2872.02 --> 2876.20]  There's trying to, you know, gather a bunch of data that would be relevant to this so that,
[2876.48 --> 2879.80]  you know, you would be able to start out and build something useful.
[2880.02 --> 2885.60]  But yeah, it's great to hear that you've had community contributions around that.
[2885.64 --> 2891.34]  And there's kind of thriving communities of people that are wanting to help build in that support.
[2891.34 --> 2896.24]  Yeah. And it's also, I mean, it's also part of the reason we really want to focus on like the tooling around,
[2896.32 --> 2900.32]  like creating the data, because, you know, it's one thing to talk about, like, oh, we don't have enough data.
[2900.32 --> 2905.52]  But like if you, if we can have more efficient ways to script workflows that even maybe a researcher can say,
[2905.62 --> 2910.64]  hey, I don't have any labeled examples, but I'll just create my own little set so I can run experiments
[2910.64 --> 2912.58]  and like get this moving forward.
[2912.58 --> 2914.14]  That's like, that's pretty good.
[2914.18 --> 2919.72]  And I think can have a big impact if, you know, you don't see annotation as this like huge crowdsourced effort
[2919.72 --> 2924.22]  and something focused that like is actually not actually quite easy to achieve.
[2925.28 --> 2929.90]  So it's interesting for me is, you know, is Daniel just made those comments about some of those efforts.
[2930.32 --> 2937.98]  And I'm kind of wondering as someone relatively new to this, this aspect and new to NLP compared to you guys,
[2938.08 --> 2942.18]  can you give us some perspective on general trends in natural language processing?
[2942.18 --> 2945.78]  And what are the exciting things that you see happening going forward?
[2945.92 --> 2948.08]  You know, what are you excited about over the next couple of years?
[2948.86 --> 2956.32]  So I think it's definitely exciting to see the field develop and to see so many more developers get skilled up with this.
[2956.32 --> 2961.18]  So I would say that, okay, one way to answer this is if you went back a few years,
[2961.62 --> 2967.44]  what were the questions which people were asking about how trends would develop or like what would happen?
[2967.72 --> 2971.06]  And then if you compare that to now, I think you see an interesting perspective on that.
[2971.06 --> 2978.06]  So one of the things that people were wondering a few years ago was whether people would be running the models themselves on their computers
[2978.06 --> 2980.16]  or whether everybody would just use an API.
[2980.54 --> 2985.74]  So would everybody use the one API that was like, you know, the Google Understand Language API or something?
[2985.74 --> 2989.08]  And that would just be what people would use for this.
[2989.28 --> 2995.22]  Or would it be the case that, you know, as we've seen now, actually more and more people, you know, are building the models
[2995.22 --> 2997.92]  and more and more people are involved with, you know, quite detailed libraries
[2997.92 --> 3003.54]  and have even switched over from a library like TensorFlow to something more flexible like PyTorch.
[3003.88 --> 3008.56]  And so I think that's been answered decisively in the direction of, okay, people want it to be programmable
[3008.56 --> 3010.44]  and they want to understand the workings of the model.
[3010.44 --> 3013.46]  They don't want a black box that, you know, where everything's done for them.
[3013.80 --> 3019.16]  And I think that the reason for that is that there is no sort of one answer for a lot of these things.
[3019.16 --> 3022.14]  You need to script the problem yourself.
[3022.30 --> 3025.52]  You need to, you know, have it recognize exactly what you want it to recognize
[3025.52 --> 3029.66]  and the model to work the way that you want it to work with the features that you want it to work with.
[3030.10 --> 3034.32]  And so I would say that that's definitely been a trend that we expect to continue.
[3034.32 --> 3038.90]  And we expect the, you know, general like sort of savviness and knowledge of people.
[3039.16 --> 3044.24]  And, you know, they'll want to work with basically the most effective ways of doing this
[3044.24 --> 3047.56]  rather than the ways which are like, you know, superficially the simplest.
[3047.90 --> 3048.04]  Yeah.
[3048.44 --> 3048.68]  Yeah.
[3048.70 --> 3051.82]  And I think also, even if you look at like new developments like transfer learning,
[3051.90 --> 3056.54]  that's of course very exciting because, you know, it means we can reuse knowledge better
[3056.54 --> 3059.36]  and transfer it between different things we're training.
[3059.36 --> 3065.72]  And so we do think that actually, you know, there's some trend that moves away from this idea of like,
[3065.78 --> 3069.04]  oh, we need this big, big, big data, huge operation.
[3069.20 --> 3072.50]  And we can actually, you know, work on like kind of a medium scale,
[3072.88 --> 3075.04]  try out a lot more things in the workflows.
[3075.42 --> 3080.90]  And also I do think, yeah, we see a lot of systems that like just work end to end.
[3081.06 --> 3085.32]  And, you know, people are like, well, cool, if I can just like throw like bird at it,
[3085.40 --> 3086.84]  it'll just like magically work.
[3086.84 --> 3090.42]  But I think as the field develops and also as like the problem develops,
[3090.78 --> 3094.84]  I do think there's still, you know, a lot of challenges are much more on a level of,
[3095.28 --> 3096.92]  okay, I can predict all kinds of things.
[3096.92 --> 3100.54]  I can do it very quickly without needing like too much data.
[3100.76 --> 3105.48]  But how do I really translate these predictions into my very, very specific,
[3105.66 --> 3109.18]  domain-specific problem that I have to solve for my business use case?
[3109.24 --> 3113.60]  And I don't think there's like an easy answer to this on the technology level.
[3113.60 --> 3117.92]  That's like something you need, you as an expert, you need to know what questions do I ask?
[3118.06 --> 3119.06]  What can I train?
[3119.18 --> 3119.94]  What will work?
[3120.36 --> 3122.52]  Once it works, how do I interpret the results?
[3122.52 --> 3125.64]  And how do I put it all together to answer the questions?
[3126.34 --> 3129.50]  And yeah, and that's something I think, yeah, you can't really predict end to end.
[3129.50 --> 3136.54]  So let's say that, and I hope that we have, but let's say that we've inspired some listeners out there
[3136.54 --> 3143.78]  to get hands-on with NLP, with Spacey and with Prodigy and with the other tools that you're releasing.
[3144.30 --> 3148.72]  I know that you've actually built a course for NLP with Spacey.
[3148.78 --> 3149.16]  Is that right?
[3149.38 --> 3149.58]  Yep.
[3149.90 --> 3150.46]  Yeah, it's free.
[3150.58 --> 3151.44]  It's online.
[3152.08 --> 3154.36]  And it's, yeah, it's available at course.spacey.io.
[3154.36 --> 3155.56]  And it's kind of interactive.
[3155.82 --> 3159.78]  You can, you know, you get some little prompts, you can enter code, you can check it, but it's
[3159.78 --> 3161.58]  like all, yeah, intended for self-study.
[3162.02 --> 3163.40]  But it's been very popular and well-received.
[3163.66 --> 3164.30]  So, yeah.
[3164.88 --> 3165.06]  Yeah.
[3165.10 --> 3170.70]  Would you recommend that as kind of a good place for someone who's maybe toyed around,
[3170.90 --> 3176.46]  at least with Python and done maybe some scikit-learn stuff or something like that,
[3176.46 --> 3178.76]  and then want to do something NLP related?
[3179.06 --> 3181.54]  Would that be a good place to start or are there better places?
[3181.54 --> 3186.18]  I think, of course, like I really try to design it in a way that it also explains all the
[3186.18 --> 3187.52]  concepts about NLP.
[3187.74 --> 3192.56]  So even if you've never worked with like NLP or machine learning before, I think it still,
[3192.70 --> 3195.36]  you know, gives a good perspective and gets you productive.
[3195.66 --> 3199.70]  But also if you have done a lot of machine learning and no NLP, you know, I think there's
[3199.70 --> 3202.64]  still enough in there that like, you know, it feels valuable.
[3203.30 --> 3203.42]  Yep.
[3203.52 --> 3203.76]  Awesome.
[3204.12 --> 3210.66]  And I would say that in terms of other resources for like more general machine learning stuff
[3210.66 --> 3214.20]  or understanding neural networks a bit better, the fast AI course is very good.
[3214.34 --> 3214.48]  Yeah.
[3214.48 --> 3221.56]  And then actually a little book that I recommend to some people is Machine Learning Yearning
[3221.56 --> 3222.74]  by Andrew Ng.
[3223.62 --> 3227.68]  So I don't like all of his talking points, but that little book is actually quite a useful
[3227.68 --> 3229.68]  primer in setting up machine learning projects.
[3230.28 --> 3234.60]  And it has some advice that, you know, sort of gets lost along the way about, you know,
[3234.78 --> 3235.78]  what's an evaluation set?
[3235.84 --> 3236.86]  How do we do these things?
[3236.92 --> 3237.80]  Like that sort of stuff.
[3238.06 --> 3239.58]  And it's a pretty short read.
[3239.64 --> 3241.22]  So that's also a nice background as well.
[3241.22 --> 3242.72]  So that's great.
[3242.82 --> 3248.34]  We'll definitely put the link to the course and to the book, Fast AI.
[3248.66 --> 3250.44]  Again, I think we've linked Fast AI.
[3250.70 --> 3255.02]  I don't know how many times at this point, Chris, but we're big fans.
[3255.38 --> 3256.64]  Yeah, we're big fans as well.
[3256.68 --> 3261.84]  And actually they have another course that's specifically NLP focused now.
[3261.94 --> 3266.06]  Yeah, no, that's actually, and I really liked, I kind of liked the curriculum there because
[3266.06 --> 3267.34]  it also starts with the basics.
[3267.34 --> 3271.90]  I think it looks at like a very basic rule-based approach as the whole history.
[3272.10 --> 3275.20]  And it's not just like, oh, he is like, you know, the hippest thing.
[3275.34 --> 3280.76]  And I think also it does cover a lot of ethical aspects too and bias in models, which, yeah,
[3280.78 --> 3283.90]  is also something you don't typically get from like your average programming course.
[3284.36 --> 3285.00]  Yeah, sure.
[3285.20 --> 3289.70]  Yeah, really appreciate what that community is doing and what it's all the tooling and
[3289.70 --> 3292.18]  the courses and everything has meant through the recent years.
[3292.64 --> 3295.90]  Well, thank you both for taking time to talk with us.
[3295.90 --> 3298.78]  We'll definitely link everything that we've talked about in our show notes.
[3299.24 --> 3300.46]  There's a lot to explore.
[3300.64 --> 3303.86]  There's a lot of questions that I'm sure people might have.
[3303.94 --> 3306.08]  Feel free to join us on our Slack community.
[3306.56 --> 3312.04]  You can find that at changelog.com slash community or LinkedIn or Twitter or wherever you find
[3312.04 --> 3315.38]  yourself and get plugged in with the Spacey community.
[3315.62 --> 3321.50]  Try out some things and really appreciate you both being here and looking forward to great
[3321.50 --> 3324.30]  things from Explosion and Spacey in the future.
[3324.30 --> 3324.76]  Thanks.
[3324.96 --> 3325.28]  Thanks.
[3325.90 --> 3327.92]  All right.
[3327.98 --> 3330.58]  Thank you for tuning into this episode of Practical AI.
[3330.86 --> 3332.32]  If you enjoyed this show, do us a favor.
[3332.44 --> 3333.02]  Go on iTunes.
[3333.14 --> 3333.84]  Give us a rating.
[3334.12 --> 3335.96]  Go in your podcast app and favorite it.
[3336.08 --> 3338.78]  If you are on Twitter or social network, share a link with a friend.
[3338.84 --> 3341.22]  Whatever you got to do, share the show with a friend if you enjoyed it.
[3341.50 --> 3344.18]  And bandwidth for changelog is provided by Fastly.
[3344.30 --> 3345.72]  Learn more at fastly.com.
[3345.92 --> 3349.12]  And we catch our errors before our users do here at changelog because of Rollbar.
[3349.32 --> 3351.74]  Check them out at rollbar.com slash changelog.
[3351.74 --> 3354.54]  And we're hosted on Linode cloud servers.
[3354.54 --> 3356.50]  Head to linode.com slash changelog.
[3356.58 --> 3357.06]  Check them out.
[3357.12 --> 3357.98]  Support this show.
[3357.98 --> 3361.54]  This episode is hosted by Daniel Whitenack and Chris Benson.
[3362.00 --> 3364.08]  The music is by Breakmaster Cylinder.
[3364.40 --> 3367.90]  And you can find more shows just like this at changelog.com.
[3367.90 --> 3370.02]  When you go there, pop in your email address.
[3370.32 --> 3374.70]  Get our weekly email keeping you up to date with the news and podcasts for developers in
[3374.70 --> 3376.34]  your inbox every single week.
[3376.70 --> 3377.52]  Thanks for tuning in.
[3377.66 --> 3378.40]  We'll see you next week.
