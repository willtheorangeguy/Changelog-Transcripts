[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.40 --> 17.94]  This episode is brought to you by TopTow,
[18.04 --> 20.48]  freelance development jobs for world-class engineers.
[20.78 --> 25.12]  This message is specifically for our listeners who prefer the freelance lifestyle.
[25.46 --> 28.24]  TopTow gives you the ability to work on freelance development jobs
[28.24 --> 32.38]  and projects with top clients who understand the value of elite engineering talent.
[32.76 --> 35.18]  Work with leading organizations at the rate you decide,
[35.52 --> 37.26]  be in control of your own schedule,
[37.62 --> 42.42]  and get plugged into support from a community of experts in the TopTow global network.
[42.72 --> 44.68]  TopTow handles all billing and invoicing,
[44.84 --> 46.64]  letting you fully focus on your engagements
[46.64 --> 50.36]  without negotiating terms with clients or bidding against other developers.
[50.92 --> 53.46]  TopTow is also 100% remote,
[53.46 --> 55.52]  which means you get to design your own lifestyle
[55.52 --> 57.60]  and choose projects that fit your career ambitions.
[57.60 --> 60.22]  If you're ready for an exciting remote work lifestyle,
[60.40 --> 63.70]  take the next step by joining TopTow at TopTowjobs.com.
[63.90 --> 65.92]  Again, TopTowjobs.com.
[65.92 --> 66.06]  TopTowjobs.com.
[77.06 --> 79.68]  Hello, all you party animals out there.
[80.06 --> 80.66]  Shaboy!
[80.90 --> 85.76]  What you're about to hear is a series of lightning chats from all things Open 2019.
[86.50 --> 89.96]  Emma, K-Ball, and myself did a super fun live show on stage.
[89.96 --> 93.72]  And thanks to each and every one of you who joined us at the event,
[93.84 --> 97.68]  especially the 11 of you bold enough to lightning chat with us.
[98.40 --> 100.96]  As with all live shows, we had a few surprises.
[101.40 --> 103.06]  Our audio levels weren't perfect.
[103.52 --> 104.46]  Emma was too quiet.
[104.86 --> 105.82]  K-Ball was too loud.
[106.14 --> 106.58]  And me?
[106.92 --> 108.14]  I was all over the place.
[108.94 --> 110.44]  We've cleaned it up quite a bit.
[110.54 --> 113.20]  It's definitely listenable and you don't want to miss it.
[113.20 --> 118.02]  But we are going to roll the hallway track lightning chats first because they sound the best.
[118.94 --> 122.16]  Oh, and did you know this is also our 100th episode of the show?
[122.64 --> 123.32]  Pretty cool, huh?
[123.74 --> 128.98]  We had a bunch of ambitious ideas on ways to celebrate episode 100 and here's where it all landed.
[131.42 --> 133.02]  Okay, let's get to it.
[133.02 --> 145.92]  First up, we have Jake Lundberg of Brooks Bell talking about A-B testing.
[146.98 --> 152.30]  We are number one of our booth live lightning talks.
[152.50 --> 156.04]  Yeah, so I just wanted to continue our chat, I guess, on A-B testing.
[156.72 --> 160.48]  All right, so let's actually, since this is being recorded and we may put it out,
[160.48 --> 162.88]  give us the setup.
[163.22 --> 165.00]  So A-B testing on the client side.
[165.62 --> 171.14]  Yeah, so A-B testing uses testing tools like Adobe Target or Optimizely to deliver
[171.14 --> 175.24]  essentially third-party scripts to a site, modify them in some way,
[175.36 --> 176.92]  and you can control traffic.
[177.08 --> 180.40]  So some users get the default site, some users get a different experience,
[180.78 --> 185.34]  and you can measure the impact rather than just making a change to the site
[185.34 --> 186.22]  and hoping for the best.
[186.22 --> 193.04]  But with Firefox making restrictions with ITP, or Safari making restrictions with ITP 2.1,
[194.52 --> 198.52]  CCPA coming out here January 1st, there's a lot of restrictions coming down.
[198.80 --> 201.88]  Where do you see the future of A-B testing going?
[202.76 --> 204.52]  So it's a great question.
[204.96 --> 208.52]  I think there's a number of different things inside that question.
[208.66 --> 212.40]  So we were chatting earlier about client-side versus server-side testing.
[212.40 --> 217.34]  On the client side, I see more and more things broadly, not just A-B testing,
[217.54 --> 218.90]  moving to first-party scripts.
[219.20 --> 223.60]  So I see us hopefully getting away from the load, you know,
[223.66 --> 225.54]  this tag from this site and this tag from this site,
[225.60 --> 231.84]  and the bundle that ends up creating all of these nightmarish long-download sites
[231.84 --> 233.50]  and tracking from 20 different places.
[233.90 --> 235.02]  Marketing departments love it.
[235.02 --> 240.42]  It's terrible for consumers, and I think we're finally seeing regulation pushing us
[240.42 --> 243.48]  in a way that's going to say, hey, that's not viable anymore.
[243.70 --> 248.36]  So I think for client-side testing, we are going to see things moving towards,
[248.74 --> 252.74]  instead of you just drop in a third-party script,
[252.96 --> 254.90]  you actually have to have an engineer do some work,
[255.16 --> 259.82]  and you do something that is first-party so that you have full control over it,
[259.82 --> 261.32]  and it's not restricted in the same way.
[261.32 --> 265.32]  That's probably a negative for marketing departments.
[266.08 --> 266.58]  I was about to say.
[267.16 --> 269.14]  But they're already ciphering some of that pain.
[269.42 --> 275.12]  You know, it's really hard to automatically drag and drop with a single-page app, right?
[276.10 --> 277.96]  They're already losing the capabilities,
[278.52 --> 284.26]  and so this would give us a way to get some of those capabilities back involving an engineer.
[284.26 --> 290.18]  It sounds like a company would be well-served to provide APIs,
[290.42 --> 296.12]  easy ways for engineers to build first-party without having to maybe host all of the data
[296.12 --> 297.26]  or provide their own scaffolding.
[298.12 --> 300.90]  That's been a huge challenge is not having access to APIs
[300.90 --> 302.92]  or there just not being APIs available,
[303.08 --> 305.96]  and we're scraping pages for limited data.
[306.10 --> 306.94]  That's been a big challenge.
[306.94 --> 312.48]  Yeah, I think, you know, we're going to see there hasn't been an incentive to build out,
[312.58 --> 317.70]  for example, libraries there because every company wants to own that experience.
[317.76 --> 319.68]  So they say, just drop in our script tag and go.
[319.82 --> 322.72]  Why would we create an open-source library for you to control all this stuff?
[322.80 --> 326.12]  Like, it's all hidden behind our proprietary area.
[327.10 --> 331.64]  If that goes away, suddenly we have much more reason to build out utilities
[331.64 --> 332.54]  that are going to be helpful.
[332.54 --> 339.04]  I suspect you'll also end up seeing proxying-type stuff
[339.04 --> 341.54]  where, you know, maybe you have an API over there,
[341.60 --> 344.12]  but since you don't want to touch anything that's outside of your own domain,
[344.30 --> 347.04]  you say, okay, drop this library and put this little proxy in.
[347.38 --> 351.38]  It'll keep all of the user-specific data local and first-party
[351.38 --> 354.90]  so you don't have quite as many restrictions about where you're sending things.
[354.98 --> 357.70]  You don't have to say, oh, yes, we send your data to X and Y and Z,
[357.70 --> 363.28]  but then you can offload the sort of data analysis and processing to somewhere else
[363.28 --> 366.62]  because, I mean, with A-B testing, you have kind of two big pieces of it, right?
[366.68 --> 370.60]  So you have, for each individual, you want to assign them something
[370.60 --> 372.60]  so that they get a consistent experience,
[373.12 --> 377.10]  and that is the tracking piece that is increasingly restricted.
[377.52 --> 381.08]  But then you also have data analysis, which can be anonymized, right?
[381.08 --> 384.52]  You only really need the bulk data to get the analysis piece
[384.52 --> 387.36]  to understand what is the better solution here or what's doing better.
[387.96 --> 389.56]  That could be completely anonymized.
[389.66 --> 391.98]  That could probably stay as third-party services
[391.98 --> 393.62]  that provide a bunch of value-add there
[393.62 --> 397.00]  so long as you can have that layer in the middle that's like,
[397.10 --> 400.02]  okay, I'm tracking while you're on the site so you get a consistent experience,
[400.28 --> 402.98]  but we're not sending any of your particular data anywhere.
[403.14 --> 404.46]  We anonymize it, put it in buckets,
[404.46 --> 406.86]  and send it off somewhere for processing and visualization.
[406.86 --> 411.96]  Do you foresee adding that additional layer being an additional challenge
[411.96 --> 415.48]  to accurate analytics tracking?
[416.02 --> 418.00]  Because there's already an issue with the analytics
[418.00 --> 420.30]  not necessarily being 100% accurate.
[420.62 --> 422.32]  Do you see an extra layer adding to that?
[422.98 --> 426.00]  I don't know that it makes it any worse than it already is.
[426.00 --> 432.52]  And especially as you move to a world of single-page apps
[432.52 --> 434.26]  or apps that are, you know,
[434.32 --> 437.00]  I love the universal JavaScript approach
[437.00 --> 438.26]  where you render it server-side,
[438.36 --> 440.56]  but then once it's loaded, it hydrates a single-page app.
[441.04 --> 443.24]  Like, those already have shit tons of, sorry,
[443.50 --> 446.82]  those already have tons of problems with accuracy
[446.82 --> 448.60]  and keeping track of things,
[448.64 --> 450.52]  and you've already got to have an engineer involved
[450.52 --> 451.68]  plugging that stuff in.
[451.68 --> 455.28]  I don't think it's any worse if what you're plugging in
[455.28 --> 457.72]  is a library that proxies through your local API
[457.72 --> 460.78]  as compared to just dropping in some script tag
[460.78 --> 462.68]  and then having to use their, you know,
[462.98 --> 464.36]  programming interface to plug it in.
[465.64 --> 467.14]  Gotcha. Well, thanks, guys. I really appreciate it.
[467.24 --> 467.58]  Thanks, Jake.
[473.90 --> 475.82]  Next up, we have Amal Hussain
[475.82 --> 478.30]  talking about finding your tribe at conferences.
[478.94 --> 479.56]  Take a listen.
[481.68 --> 487.82]  Hi, Jared and Kevin.
[488.26 --> 488.52]  Yo.
[488.64 --> 490.58]  I'm really excited to talk about
[490.58 --> 493.22]  what I love about going to conferences.
[493.66 --> 494.22]  Oh, yes.
[494.76 --> 496.70]  Which is, for me,
[496.92 --> 499.54]  it's an opportunity to find my tribe, you know?
[499.76 --> 499.94]  Yeah.
[500.00 --> 502.36]  And I love multi-track conferences especially
[502.36 --> 504.82]  because I think you get to find your sub-tribe.
[505.04 --> 505.34]  Ah.
[505.68 --> 508.28]  And, you know, depending on what talks you're in
[508.28 --> 511.26]  and, like, which hallway you're outside, right?
[511.26 --> 513.20]  When talks get out, you know,
[513.24 --> 515.94]  it's just a great place to kind of catch your tribe.
[516.60 --> 517.56]  And I love that.
[517.62 --> 518.28]  I like that take.
[518.40 --> 520.16]  I've always been anti-multi-track
[520.16 --> 522.92]  because I appreciate a shared experience.
[522.94 --> 523.26]  Oh, yeah.
[523.52 --> 524.00]  Same here.
[524.10 --> 526.12]  But I like that angle into multi-track.
[526.24 --> 527.18]  Find your sub-tribe.
[527.30 --> 527.58]  Yeah.
[527.78 --> 528.06]  Yeah.
[528.06 --> 530.64]  There's a wider tribe and then there's your sub-tribe.
[531.00 --> 531.88]  And, you know, I'm with you.
[532.02 --> 533.64]  There's something about single-track conferences
[533.64 --> 536.68]  that I think create for richer conversations
[536.68 --> 541.82]  around, you know, everything that we're all experiencing together.
[541.82 --> 542.62]  Yeah, we all saw it.
[542.70 --> 543.24]  We were all there.
[543.36 --> 544.46]  There's power in that.
[544.66 --> 547.36]  It's like, you know, power of the collective experience.
[547.48 --> 547.68]  Yeah.
[547.68 --> 551.10]  But, you know, but there's something about,
[551.42 --> 552.54]  there's something nice, I think,
[552.60 --> 555.22]  about being in a multi-track conference
[555.22 --> 558.46]  because, you know, you have an opportunity, I think,
[558.50 --> 561.44]  to connect and break the silos, you know, within tech, right?
[561.76 --> 563.84]  So we're all at all things open.
[564.34 --> 565.86]  And, you know, there's a DevOps track
[565.86 --> 569.00]  and there's a blockchain track.
[569.60 --> 571.18]  Guess who didn't go to any blockchain talks?
[571.58 --> 572.00]  That's me.
[572.10 --> 572.34]  This guy.
[572.34 --> 572.76]  I didn't go.
[572.92 --> 574.38]  I didn't go to any blockchain talks.
[574.40 --> 574.76]  Me neither.
[575.20 --> 576.00]  Hashtag no blockchain.
[576.46 --> 577.00]  Sorry, everyone.
[577.00 --> 578.08]  Hashtag no blockchain.
[578.72 --> 579.92]  I think there's like 22 tracks.
[579.94 --> 581.40]  There's like 22 tracks.
[581.86 --> 582.36]  Holy cow.
[582.86 --> 585.52]  And, you know, it's an opportunity for me to, you know,
[585.56 --> 587.10]  we all have a shared value here,
[587.18 --> 589.12]  which is, you know, we all are proponents
[589.12 --> 589.98]  of open source software.
[590.18 --> 592.38]  And, you know, we all leverage open technologies.
[592.38 --> 594.08]  And so we all have those shared values.
[594.08 --> 596.82]  But now I get to meet someone who's maybe doing ops work
[596.82 --> 599.06]  and get to connect with them and, you know,
[599.38 --> 601.34]  with those shared values.
[601.48 --> 604.06]  And so I think it's a silo-breaking opportunity.
[604.06 --> 607.06]  I feel like I've been finding my sub-sub-sub tribe.
[607.34 --> 608.92]  You know, the people who are techie,
[609.00 --> 610.84]  but also willing to look goofy on camera
[610.84 --> 611.72]  and dance a little bit.
[611.98 --> 612.34]  Oh, yeah.
[612.40 --> 613.46]  That's a very small group.
[613.70 --> 613.92]  Yeah.
[614.02 --> 615.04]  There's like five of us.
[615.10 --> 615.48]  Group of one.
[616.40 --> 617.14]  No, no, no.
[617.98 --> 620.16]  Tracy's expanding the crowd.
[620.54 --> 620.60]  Yeah, she's expanding that group.
[620.60 --> 621.20]  Yeah, she really is.
[621.20 --> 622.38]  Tracy really had some TikTok going on.
[622.46 --> 623.46]  K-Ball, why don't you tell the people
[623.46 --> 624.18]  what you've been up to?
[624.98 --> 625.34]  Dancing.
[625.66 --> 626.02]  Dancing.
[626.74 --> 627.68]  I like to dance.
[627.80 --> 629.74]  Did you see him dancing?
[630.64 --> 631.58]  You could be on dancing.
[631.58 --> 632.36]  On TikTok.
[632.82 --> 633.48]  Oh, my goodness.
[633.48 --> 634.36]  Dancing with the TikToks.
[634.38 --> 635.44]  I'd never heard of TikTok.
[636.06 --> 636.80]  I mean, that's not true.
[637.04 --> 637.96]  I'd sort of like heard it,
[638.00 --> 639.36]  but I hadn't understood what it is.
[639.48 --> 641.10]  But apparently it's the thing
[641.10 --> 642.28]  for the kids these days.
[642.88 --> 643.28]  Yeah.
[643.50 --> 644.30]  Showing my age.
[644.36 --> 645.86]  Which means that like no kids
[645.86 --> 647.36]  are now using TikTok, you know.
[647.36 --> 649.22]  So, I mean, once we discover it.
[649.38 --> 649.62]  Right.
[649.76 --> 650.06]  It's like.
[650.28 --> 651.36]  It's driving the kids away.
[651.52 --> 651.72]  Yeah.
[651.82 --> 653.86]  They're basically like onto the next thing.
[653.98 --> 654.22]  Right.
[654.76 --> 656.24]  They're like, oh, this guy's dancing.
[656.54 --> 656.84]  Kind of.
[656.94 --> 658.10]  Oh, he has gray hair.
[658.42 --> 658.66]  Ooh.
[659.36 --> 659.68]  Ooh.
[661.34 --> 661.66]  Yeah.
[662.54 --> 663.92]  Mom, time to get off TikTok.
[664.24 --> 665.54]  So, I spent a good part of an afternoon
[665.54 --> 667.38]  on TikTok when I first found it.
[667.64 --> 669.28]  Just trying to figure out
[669.28 --> 670.48]  what the heck was going on with this thing.
[671.08 --> 672.98]  And then I uninstalled the app from my phone.
[673.10 --> 674.44]  And I was just like, all right, I get it.
[674.50 --> 675.46]  I'm moving on with my life.
[675.56 --> 676.66]  It's a rage uninstall.
[676.86 --> 678.14]  I've done that before, too.
[678.74 --> 679.94]  Like, I don't understand this.
[679.96 --> 681.16]  This is really weird UX.
[681.46 --> 681.80]  You know.
[682.04 --> 682.24]  Yeah.
[682.24 --> 683.10]  Where are all the buttons?
[683.78 --> 684.02]  Right.
[684.20 --> 685.50]  Where's my navigation tree?
[685.56 --> 686.64]  I felt like I'd seen it all
[686.64 --> 689.16]  because it's all the remixes and stuff.
[689.20 --> 690.44]  And there wasn't that many people on it then.
[690.66 --> 691.72]  So, it's like the same thing.
[691.74 --> 692.90]  And it's funny, funny, funny.
[693.56 --> 696.24]  And it's like cute, stupid, funny.
[696.80 --> 698.24]  Then you're supposed to be like stupid, stupid, stupid.
[698.34 --> 699.24]  And you're like uninstall.
[699.52 --> 702.20]  Like there's like a downward spiral of my opinion.
[702.30 --> 703.28]  Yeah, you feel the brain cells.
[703.28 --> 704.16]  But I'm sure it's great.
[704.16 --> 704.64]  Bursting.
[705.54 --> 706.06]  I don't know.
[706.12 --> 707.08]  Apparently, Tracy likes it.
[707.10 --> 708.00]  I mean, apparently.
[708.56 --> 709.28]  Maybe K-Ball will be like a TikTok star.
[709.28 --> 711.16]  She actually made that joke in her keynote yesterday.
[711.16 --> 711.40]  No.
[711.62 --> 714.96]  She's like, my husband thinks my brain cells are shrinking because of it or something.
[715.10 --> 715.34]  Yep.
[715.62 --> 716.02]  Exactly.
[716.22 --> 720.70]  But I mean, the fun thing is, it is neat to see people who cross worlds.
[720.90 --> 721.04]  Yeah.
[721.04 --> 726.02]  So, I love the fact that she's out there getting people to be uncomfortable.
[726.02 --> 730.12]  Because as developers, a lot of times we're not very comfortable putting ourselves out there.
[730.12 --> 730.38]  Right.
[730.38 --> 733.18]  You know, shaking our body, moving our body a little bit.
[733.44 --> 733.90]  What body?
[734.18 --> 735.14]  Especially in the afternoon.
[735.80 --> 736.64]  I don't have a body.
[736.64 --> 736.90]  I know.
[736.98 --> 738.54]  We're just disembodied brains, right?
[738.62 --> 741.04]  But no, it turns out that our bodies are important.
[741.34 --> 743.60]  And you treat them well, then you can think better and code better.
[744.02 --> 745.86]  And you goof off and dance a little bit.
[745.94 --> 747.20]  And then, I don't know.
[747.86 --> 748.58]  You find your tribe?
[748.94 --> 749.14]  Yeah.
[751.94 --> 752.70]  27 seconds.
[752.78 --> 753.68]  Do you want to give any shout outs?
[753.68 --> 760.26]  Shout out to the conference organizers and all of the keynote speakers and all of the speakers.
[760.62 --> 761.34]  It's a lot of work.
[761.44 --> 762.12]  I did a talk.
[763.04 --> 764.44]  Hug your speakers, ladies and gentlemen.
[766.10 --> 766.98]  Hug your speakers.
[767.98 --> 769.04]  Tell them you like their talk.
[769.16 --> 769.46]  Yes.
[770.02 --> 770.80]  Tell them thank you.
[772.04 --> 772.38]  All right.
[772.42 --> 774.16]  Thanks so much for lightning chatting with us.
[776.88 --> 777.32]  TikTok.
[777.32 --> 777.52]  TikTok.
[777.52 --> 778.02]  TikTok.
[778.02 --> 778.16]  TikTok.
[778.16 --> 778.20]  TikTok.
[778.20 --> 778.32]  TikTok.
[778.32 --> 778.40]  TikTok.
[778.40 --> 778.44]  TikTok.
[783.68 --> 787.66]  Here's Matt Broberg asking us some hard questions.
[788.02 --> 789.82]  This guy might have a future in podcasting.
[794.68 --> 797.18]  We got five minutes on the watch here.
[797.60 --> 798.12]  Go, go, go.
[798.14 --> 798.64]  It's your show.
[798.74 --> 799.14]  What do you want to talk about?
[799.22 --> 799.60]  Oh, man.
[799.64 --> 802.24]  I've always wanted to run the show for you all.
[802.38 --> 802.54]  Okay.
[802.68 --> 804.10]  So, Jared, K-Ball.
[804.36 --> 808.92]  I was fascinated by the last one of the keynotes today that talked about full stack development.
[809.14 --> 809.66]  As was I.
[809.66 --> 814.78]  And the career development challenges that are happening where there's a consolidation on that end.
[815.08 --> 820.34]  Can you tell me a little about your personal experiences with breaking into those new boundaries?
[820.58 --> 821.96]  What do you think is happening there?
[822.50 --> 830.66]  And then ultimately, how do people that are junior that are trying to get into this industry, where do they start when it's such a big ball of things going on these days?
[831.16 --> 832.16]  That's multiple questions.
[832.24 --> 833.40]  Which one should we tackle first?
[833.70 --> 835.72]  Well, I already talked with Matt a little bit about this.
[835.82 --> 836.92]  So, I want to hear what you have to say.
[836.92 --> 837.16]  Okay.
[837.80 --> 842.30]  So, where do I fit into the ever-growing front-end full stack?
[842.30 --> 842.98]  Front-end haystack.
[843.42 --> 844.70]  The haystack developer.
[845.42 --> 853.78]  The move of the front-end developer, really, the empowerment, to a certain degree, of the front-end developer to be more full stack than traditionally we have been.
[853.82 --> 860.04]  Well, I've always considered myself relatively full stack because I've worked on teams of one, sometimes two.
[860.04 --> 860.66]  Yeah.
[860.66 --> 871.92]  And so, when I'm not full stack, I'm very much the horse image on the slide that Chris Coyer put up where I have a very immaculate back end.
[871.92 --> 872.98]  I never thought I'd say that.
[873.14 --> 873.76]  An immaculate tail.
[873.76 --> 876.96]  You have a fancy ass and kind of a horse face.
[877.04 --> 877.26]  Yeah.
[877.26 --> 881.04]  This metaphor has gone off the rails, but I hear you.
[881.16 --> 881.24]  Yeah.
[881.26 --> 882.62]  So, you're better on one end of it.
[883.72 --> 890.94]  So, I've always been on like a 90% stack where I lack a little bit in skills.
[891.08 --> 895.20]  It's usually in the CSS domain where I can hold my own, but I do not feel like an expert.
[896.06 --> 899.94]  And so, I've always been very proficient at everything else.
[900.14 --> 900.36]  Right.
[900.46 --> 904.14]  And so, I don't really know what that means for me.
[904.52 --> 906.10]  I feel like I'm just doing my thing still.
[906.82 --> 910.16]  And I was already going to learn the GraphQL and do the things.
[910.16 --> 914.84]  And so, I don't really feel like, for me, I've never considered myself a front-end engineer, just more of an engineer.
[915.24 --> 915.54]  Awesome.
[915.76 --> 917.60]  Yeah, and that makes sense for you and your point.
[917.74 --> 919.78]  So, you for the next question, K-Ball.
[919.78 --> 927.06]  So, what's it look like for junior engineers, for people that are just coming out of boot camps, just coming out of a degree, and they're pivoting into technology?
[927.36 --> 930.04]  What does it look like to be in this part of the industry?
[930.38 --> 930.62]  Yeah.
[930.76 --> 941.06]  I think it's intimidating because folks see all this stuff going on, and it's changing, and I've got to do this and that, and I've got to do a framework, and I've got to do a back-end, and I've got to do GraphQL, and what's this serverless and all that.
[941.64 --> 945.98]  And honestly, I think as a junior, you should pick one thing and focus.
[946.22 --> 946.44]  Cool.
[946.44 --> 946.48]  Cool.
[946.78 --> 951.76]  So, if you start in React, pick React and get React down.
[952.06 --> 952.70]  Understand it.
[952.76 --> 953.28]  Go deep.
[953.42 --> 959.54]  Try to get as much as you can in that, and really understand it before you start branching out.
[959.60 --> 961.44]  And I'd even say that within a specialty.
[961.70 --> 969.50]  So, I've talked to folks who are like, oh, I want to learn React, and I want to learn Vue, and I want to learn Svelte, and I want to learn Angular, and they're trying to learn all these things at once.
[970.12 --> 971.24]  They have a lot in common.
[971.24 --> 975.58]  If you go deep on one, you'll be able to branch out really easily later.
[975.58 --> 980.38]  But if you try to branch out at the beginning, you're going to get overwhelmed and never fully understand what's going on there.
[980.48 --> 982.60]  So, I would say start one place.
[983.22 --> 983.74]  Go deep.
[983.84 --> 989.62]  And this actually ends up being played out if you look at published industry career maps.
[989.62 --> 1000.22]  Like, there's a bunch of companies who have published their career maps of, oh, here's what we expect a junior developer, and here's what we expect a senior developer, and a tech lead, and going on and on and up into architects, what have you.
[1000.84 --> 1002.26]  They have this sort of progression.
[1002.66 --> 1007.58]  And in the beginning, it's learn how to learn and learn one thing deeply.
[1007.58 --> 1017.00]  And then as you get up into a senior engineering position, maybe you're four or five years in, now you're branching out and you're saying, okay, I know my deep thing, and now I need to know the things it's interacting with.
[1017.08 --> 1026.24]  And as you get into the industry for more like eight, nine, ten years, it's, okay, now you should be able to understand all the pieces and how they're fitting together and go further and further.
[1026.24 --> 1029.14]  But when you're just getting in, learn one thing.
[1029.76 --> 1032.98]  Don't be intimidated by all the stuff and feel like you have to all do that.
[1033.04 --> 1033.48]  That's hype.
[1033.62 --> 1034.16]  That's baloney.
[1034.58 --> 1036.02]  I really like that framing, right?
[1036.08 --> 1046.90]  Because it's a lot about something that we lose in our current education system, which is about, like, well, know everything to a subpar degree and then graduate and feel inferior in so many ways.
[1046.90 --> 1055.66]  As opposed to what it's like to actually work in this industry, which is enjoy the path towards mastery one thing at a time and build on top of that stack of mastery.
[1055.86 --> 1057.04]  Is that what you're seeing, Jared?
[1057.44 --> 1058.38]  I agree with that.
[1058.46 --> 1073.48]  I think what you find in practice is as you dive into one aspect of the stack and you get to know that really well, you learn the rest tangentially, osmosisly, necessarily, by interacting with folks who happen to know this part really well.
[1073.48 --> 1079.66]  Or having to interface and connect the glue bits together, you just happen, like, I didn't go study DNS.
[1080.72 --> 1082.10]  I don't know if you guys studied DNS.
[1082.78 --> 1084.26]  You just kind of, like, learn how DNS works.
[1084.36 --> 1086.62]  Like, I got to put my record in and, like, what's an A record?
[1086.78 --> 1087.40]  What's an MX record?
[1087.58 --> 1092.32]  Like, these are things that I just learned because I was running websites and, like, I wanted the mail to be delivered.
[1092.86 --> 1095.76]  And so you, but I studied certain things more deeply.
[1095.86 --> 1098.42]  And so I think you learn the rest because you have to.
[1099.00 --> 1100.20]  And I think that's a great way to go.
[1102.52 --> 1102.84]  Fantastic.
[1102.84 --> 1104.02]  Thank you so much for your time.
[1104.54 --> 1104.68]  Woo!
[1105.02 --> 1105.94]  Five minutes ain't much.
[1106.30 --> 1106.64]  No, man.
[1106.64 --> 1107.10]  Five minutes is a...
[1107.10 --> 1108.44]  Lightning talk to the three people?
[1108.80 --> 1109.56]  That's not...
[1109.56 --> 1119.34]  Crystal Williams-Brown approached the booth right before I was packing up to tell me about Code the Dream.
[1123.12 --> 1124.46]  Crystal, thanks for joining me.
[1124.54 --> 1125.94]  What would you like to talk about today?
[1126.36 --> 1127.98]  I would like to talk about Code the Dream.
[1127.98 --> 1135.52]  It's a nonprofit that offers free programming classes to remove some of the barriers that people face when getting into the tech industry.
[1135.86 --> 1136.00]  Okay.
[1136.08 --> 1141.42]  And also provide some work experience because that's another barrier for people who just recently have been trained.
[1141.42 --> 1146.08]  So they can learn how to make apps for other nonprofits or socially conscious businesses.
[1146.30 --> 1146.86]  Okay.
[1147.10 --> 1148.28]  Code the Dream.
[1148.60 --> 1149.30]  I like that.
[1149.48 --> 1149.72]  Yes.
[1150.02 --> 1151.94]  What are the barriers that are typically there?
[1152.44 --> 1160.70]  The original barrier that they were created to face was part of Uniting NC is helping people with their immigration status.
[1160.70 --> 1165.70]  And they discovered these immigrants couldn't get financial assistance to go to school.
[1165.88 --> 1166.12]  Okay.
[1166.12 --> 1167.86]  And they were having some trouble finding work.
[1168.24 --> 1180.44]  So two of the people who worked for Uniting NC, Romero and Dan, they both joined together to create Code the Dream because Romero had studied computer programming in school.
[1180.72 --> 1182.84]  Like, he has a computer science degree.
[1182.84 --> 1185.90]  And so he thought, I can teach them what I know.
[1186.86 --> 1188.92]  And at least they'll have that to work with.
[1189.04 --> 1195.78]  And you can get by a little easier in the tech industry, especially now, without having a degree, but just having the training.
[1196.14 --> 1199.96]  And then you saw people were having a hard time getting hired because they didn't have the work experience.
[1199.96 --> 1208.98]  So they created Code the Dream Lab where we can make practice apps and then make apps for other nonprofits and socially conscious business.
[1209.52 --> 1210.42]  So how did you get involved?
[1210.42 --> 1214.20]  I actually was looking for a way to learn programming for free.
[1214.34 --> 1215.08]  I was unemployed.
[1215.78 --> 1217.36]  I'd struggled with employment for a while.
[1217.44 --> 1222.50]  And I actually do have two degrees, but neither one led to any kind of gainful employment.
[1223.26 --> 1226.80]  And I was led through the Iron Yard, oddly enough.
[1226.96 --> 1230.82]  I reached out to them and I said I couldn't afford their classes, but I really wanted to learn.
[1230.88 --> 1234.38]  And they said, well, Code the Dream has free programming classes.
[1234.70 --> 1236.36]  You should look into them.
[1236.74 --> 1238.30]  And I was very grateful for that help.
[1239.38 --> 1239.78]  Awesome.
[1239.78 --> 1242.74]  For those listening, wondering what those loud noises are in the background.
[1243.70 --> 1246.94]  We are in the late afternoon of the last day here at All Things Open.
[1247.04 --> 1249.68]  And they are literally closing down shop around us.
[1250.52 --> 1253.10]  So, Crystal, how do people get involved?
[1253.20 --> 1254.26]  Who's the right person?
[1254.40 --> 1256.90]  Like if they wonder, is Code the Dream for me?
[1257.30 --> 1260.60]  Maybe I can get in on the helping side versus the receiving side.
[1261.32 --> 1262.86]  Help people guide us through that.
[1262.86 --> 1267.68]  Well, we have a website that's very helpful in guiding you in whatever direction you want to go.
[1267.74 --> 1272.92]  Because we do take in volunteers who teach classes or they can be a mentor for a student.
[1273.02 --> 1280.84]  Or you can even come in for a small session where you teach one day, just something that you know that could help out the interns that are currently in the program.
[1280.84 --> 1285.68]  And if you want to take classes, they have sessions running throughout the year.
[1285.68 --> 1287.54]  And they're in different locations.
[1287.70 --> 1290.34]  We're also branching out so that you can do it remotely.
[1290.60 --> 1292.46]  So, we have some students who are out in Chicago.
[1293.08 --> 1295.36]  And we're going to branch out into more states.
[1295.58 --> 1296.20]  So, yeah.
[1296.36 --> 1298.56]  It doesn't matter if you live in North Carolina or not.
[1298.56 --> 1298.74]  Okay.
[1298.74 --> 1299.86]  You don't have to be in North Carolina.
[1299.86 --> 1302.26]  How long has this been going on?
[1302.86 --> 1308.60]  It started in 2014, which is funnily enough when I was unemployed.
[1309.28 --> 1309.78]  Oh, really?
[1310.14 --> 1311.80]  So, it worked out really well for me.
[1311.80 --> 1312.38]  So, you have free time.
[1312.62 --> 1312.90]  Yeah.
[1313.22 --> 1314.02]  Are you employed now?
[1314.48 --> 1314.94]  I am.
[1315.00 --> 1316.36]  I'm employed by Code the Dream.
[1316.62 --> 1317.00]  Oh!
[1318.32 --> 1320.76]  So, I'm a full-time developer with them now.
[1320.88 --> 1321.56]  Very cool.
[1321.98 --> 1322.30]  Very cool.
[1322.32 --> 1323.24]  So, how many people work there?
[1323.24 --> 1323.58]  We have a few people on the staff.
[1323.72 --> 1324.48]  It grew.
[1324.80 --> 1325.84]  It started very small.
[1325.84 --> 1329.50]  But a lot of the staff is actually people who have been through the program and really
[1329.50 --> 1336.50]  showed, like, a kind of persistence and, like, an eagerness to learn and also some adeptness
[1336.50 --> 1337.04]  at learning.
[1337.24 --> 1339.86]  And they gave them more and more responsibilities.
[1340.20 --> 1343.14]  And then, finally, saw if they could bring them on full-time.
[1343.22 --> 1344.38]  They like to retain people.
[1344.58 --> 1349.36]  And we're trying to make more in-house apps that we can use to raise money for Code the
[1349.36 --> 1351.74]  Dream so that we're not so dependent upon grants.
[1351.92 --> 1353.54]  And that allows us to hire more people.
[1353.54 --> 1355.96]  So, you don't have to worry about looking if you don't want to look.
[1356.34 --> 1356.84]  You can stay.
[1357.74 --> 1361.60]  You can look or you can stay, assuming that you guys get that ball rolling.
[1361.74 --> 1362.72]  So, that's very cool.
[1363.18 --> 1364.86]  Well, you have a few seconds left.
[1364.92 --> 1369.42]  Any shout-outs you'd like to give beyond Code the Dream or maybe to your partners in crime
[1369.42 --> 1369.62]  there?
[1370.32 --> 1374.90]  Oh, well, I am working on an app called Upstate that tracks bills in North Carolina and alerts
[1374.90 --> 1376.78]  people about anything that's happening with them.
[1376.92 --> 1378.40]  And you can sign up for free.
[1378.88 --> 1381.68]  And you can also view all the actions that are happening on bills for free.
[1381.68 --> 1384.84]  It's called upstateapp.keepupstate.com.
[1385.56 --> 1386.62]  Keepupstate.com.
[1386.72 --> 1387.26]  Awesome, Crystal.
[1387.36 --> 1388.36]  Well, thanks for joining us.
[1389.84 --> 1390.62]  Thank you.
[1390.62 --> 1391.22]  Thank you.
[1399.16 --> 1401.62]  This episode is brought to you by DigitalOcean.
[1401.98 --> 1406.86]  DigitalOcean is the simplest cloud platform for developers and teams with products like
[1406.86 --> 1412.68]  droplets, spaces, Kubernetes, load balancers, block storage, and pre-built one-click apps.
[1413.00 --> 1418.62]  You can deploy, manage, and scale cloud applications faster and more efficiently on DigitalOcean.
[1418.62 --> 1423.78]  Whether you're running one virtual machine or 10,000, DigitalOcean makes managing your infrastructure
[1423.78 --> 1425.04]  way too easy.
[1425.30 --> 1427.80]  Head to do.co slash changelog.
[1428.08 --> 1430.84]  Again, do.co slash changelog.
[1436.84 --> 1438.92]  Okay, here's the live show on stage.
[1439.02 --> 1442.56]  Please bear with the audio if you can, because we have a lot of great guests that you will
[1442.56 --> 1443.38]  not want to miss.
[1443.74 --> 1444.02]  Here we go.
[1444.02 --> 1444.08]  Okay.
[1444.08 --> 1444.12]  Here we go.
[1444.12 --> 1444.14]  Here we go.
[1444.14 --> 1446.08]  Here we go.
[1446.08 --> 1448.08]  Here we go.
[1448.08 --> 1449.08]  Here we go.
[1451.08 --> 1454.84]  Okay, well, the sound of those beats means it's time for JS Party.
[1455.62 --> 1456.72]  My name is Jared Santo.
[1456.88 --> 1457.56]  Thanks for joining us.
[1457.62 --> 1459.14]  I'm joined by Kevin Ball.
[1459.22 --> 1459.94]  He goes as K-Ball.
[1460.04 --> 1460.64]  Say hi, K-Ball.
[1460.70 --> 1461.32]  Hey, I'm K-Ball.
[1461.42 --> 1462.00]  Nice to see you.
[1462.42 --> 1463.98]  And this is Emma Vettekind.
[1464.22 --> 1464.56]  Hi.
[1464.82 --> 1465.40]  Can you hear me?
[1465.48 --> 1466.16]  I can't hear me.
[1466.22 --> 1467.38]  We need to get Emma turned up.
[1468.76 --> 1469.50]  Is that better?
[1469.78 --> 1470.00]  Can you?
[1470.18 --> 1470.30]  Ooh.
[1470.52 --> 1470.82]  No?
[1471.10 --> 1471.36]  Yeah?
[1471.74 --> 1472.04]  Ooh.
[1472.04 --> 1473.74]  I can also just talk louder.
[1474.18 --> 1474.54]  Cool.
[1474.54 --> 1477.10]  And we're ready to go.
[1477.30 --> 1481.02]  So first up, we did have a, we primed the pump a little bit.
[1481.22 --> 1483.56]  First of all, I should say this is for everybody to participate in.
[1484.18 --> 1489.00]  We were afraid or concerned that perhaps nobody would come up and we'd have not much of a show.
[1489.00 --> 1494.86]  So we did prime the pump and I do have a short list of people that we've contacted before that we would love to chat with.
[1495.36 --> 1498.58]  As we make it through the list, maybe some people don't show up, maybe some people do.
[1499.04 --> 1501.22]  We'd love to open it up for everybody to come and talk.
[1501.32 --> 1507.66]  And then if we run out of time during this session, we are down on the third floor, booth 72, with the mic all set up.
[1507.92 --> 1512.58]  And we'll continue the lightning chats there if you don't get a turn here during this session.
[1512.58 --> 1516.30]  So the first person we'd like to call up on the stage is Denise Cooper.
[1516.58 --> 1519.80]  Denise is happy to join us but has a flight to catch.
[1519.88 --> 1520.84]  So she's going first.
[1521.06 --> 1521.34]  Yeah.
[1521.62 --> 1522.36]  And here comes Denise.
[1522.44 --> 1523.40]  Round of applause for Denise.
[1528.44 --> 1528.64]  Hello.
[1529.08 --> 1529.86]  Thank you for joining us.
[1529.88 --> 1530.44]  Please have a seat.
[1530.46 --> 1530.78]  You're welcome.
[1531.56 --> 1532.74]  I'm leaving my purse there.
[1533.04 --> 1533.32]  Okay.
[1533.66 --> 1534.76]  You guys have a watch.
[1534.98 --> 1535.68]  We'll keep an eye on that.
[1535.68 --> 1536.98]  I'll need it to get on the plane.
[1537.70 --> 1542.30]  So the other thing I didn't say is, maybe I did say it, but I'll say it again, is that this is a community thing.
[1542.30 --> 1544.98]  So we want to talk about anything that you want to talk about, Denise.
[1545.06 --> 1546.96]  We literally prepared nothing.
[1547.84 --> 1550.70]  And so please give us a topic and we'd be happy to chat about it with you.
[1551.66 --> 1552.06]  Okay.
[1553.26 --> 1559.82]  I normally talk about InnerSource, but after the keynotes today, I think it's important to talk about corporate responsibility.
[1561.58 --> 1564.78]  Because I was really disturbed by the AWS talk.
[1564.78 --> 1571.78]  I was disturbed because there was an implication that OSI approved licensing is somehow optional.
[1572.58 --> 1572.98]  Optional.
[1573.22 --> 1574.64]  And that is not the case.
[1575.22 --> 1577.02]  So I called him out.
[1577.10 --> 1578.24]  I called Aaron out.
[1578.38 --> 1586.52]  I don't, you know, I'm not saying Aaron's a bad guy, but I think when you let your customers decide how you're going to engage with open source,
[1586.52 --> 1594.18]  you run the risk of listening to customers that are maybe not so savvy and think that, you know, change is maybe in the air.
[1594.42 --> 1598.00]  But it's not clear to me that change needs to happen to open source.
[1598.10 --> 1604.40]  I think we got this far because we made good choices about how to make it last this long.
[1604.40 --> 1610.58]  And I think we should make changes to the licensing schemes and to the importance of licensing very, very carefully.
[1611.40 --> 1613.90]  So that's what I would like to talk about.
[1614.70 --> 1615.52]  Let's do that.
[1615.58 --> 1624.06]  So one thing to point out for those who weren't at the keynote this morning listening to the podcast is that there was a talk from AWS's Arun Gupta
[1624.06 --> 1628.36]  in which he talked about free credits for open source projects.
[1628.36 --> 1637.10]  Free credits for open source projects with a set of criteria and some of those criteria they put preferably.
[1638.50 --> 1641.50]  And in some cases I was like, that's overly restrictive.
[1641.68 --> 1645.14]  And in other cases, like the licensing you brought up, I was wondering, that seems a little.
[1645.72 --> 1646.96]  It is really dangerous.
[1647.66 --> 1656.40]  So the point that you'd like to highlight is free credits for open source projects, preferably OSI approved projects.
[1656.40 --> 1658.46]  And that preferable has to go away.
[1658.52 --> 1659.52]  Can you explain OSI?
[1659.82 --> 1660.20]  Yeah, sure.
[1660.36 --> 1665.16]  So the OSI, I worked on the OSI for 10 years, so I'm in a good position to talk about it, I think.
[1665.74 --> 1669.08]  I think I might have served longer than anybody, almost anybody else.
[1669.70 --> 1674.94]  But Michael Tiemann, local god of open source, was on that board with me too.
[1675.80 --> 1680.52]  The OSI decides whether licenses are OSD compliant.
[1680.74 --> 1682.18]  OSD is the open source definition.
[1682.40 --> 1683.62]  It's 10 clauses.
[1683.92 --> 1684.90]  It's very straightforward.
[1684.90 --> 1691.04]  It's common right now for people to be suggesting changes to open source that would make it better.
[1691.50 --> 1698.38]  We actually got a license, was submitted this week, called the vaccine license.
[1698.86 --> 1703.76]  That has a field of use restriction that only lets you use the software if you vaccinated your children.
[1704.42 --> 1708.12]  People are suggesting really silly field of use restrictions.
[1708.64 --> 1710.00]  But some of them are well-intentioned.
[1710.00 --> 1715.70]  Like, I wish that big corporations would have to pay, so I want to put a clause in the license that says that.
[1715.70 --> 1726.62]  That is a field of use restriction that automatically disqualifies you from OSI approval because that clause in the OSD says things you cannot do field of use restrictions.
[1726.74 --> 1728.96]  And we talked about this a lot 20 years ago.
[1728.96 --> 1733.18]  Most of us in those days were libertarians or at least liberal leaning.
[1733.18 --> 1739.08]  And some of us didn't want the software to be used, for instance, for nuclear power or for weaponry.
[1739.66 --> 1748.68]  But we debated it out and realized that we had to set that aside in order to not create the slippery slope of everybody needs a special carve-out.
[1748.68 --> 1761.60]  And all through the history of OSI, licenses that aren't OSD compliant come from companies that are trying to get a carve-out for their business model because they don't have a good, strong understanding that open source is not a business model.
[1761.80 --> 1763.78]  And they're going to need to change what they do.
[1764.02 --> 1765.70]  They can't have their cake and eat it, too.
[1766.06 --> 1773.82]  Either they get the halo effect of open source or they get to say how they want to run their business in ways that open source people would not appreciate.
[1774.06 --> 1775.10]  But they can't do both.
[1775.88 --> 1778.30]  And we've been fighting that fight forever now.
[1778.30 --> 1792.72]  It's really disheartening to see a major venue like AWS, who's trying to convince us that they're serious about open source, use the word preferable as though there was any other option if you're actually dealing with open source.
[1793.02 --> 1797.52]  Now, you'd be told that OSI doesn't own the trademark to the term open source.
[1797.88 --> 1802.00]  Nobody owns that trademark because the trademark office decided that it wasn't trademarkable.
[1802.00 --> 1812.76]  But they do own OSI-approved license, which tells you that that license fits within the OSD and therefore doesn't do anything to harm the open source movement.
[1813.70 --> 1813.80]  Right?
[1814.16 --> 1817.20]  So examples of things, recent things that were problematic.
[1817.48 --> 1824.28]  Facebook a few months ago now, a year ago now, put a license on React that included an extra patent clause.
[1824.28 --> 1827.90]  And Apache said a lot of people tried to talk them out of it.
[1828.08 --> 1831.24]  They were sure they had to do it to fend off piracy.
[1831.74 --> 1833.36]  I said, look, you've got deep pockets.
[1833.54 --> 1836.74]  Your job is to engage those pirates and take them to the mat.
[1837.10 --> 1838.20]  Look at what Vizio is doing.
[1838.32 --> 1842.10]  That's what you should be doing as a deep pocket, not trying to write your way around it.
[1842.30 --> 1844.68]  But in the meantime, Apache is going to say no to that.
[1844.72 --> 1845.82]  It's an additional obligation.
[1845.82 --> 1850.98]  And as soon as Apache started stripping out React code, they shifted their program.
[1851.48 --> 1851.60]  Right?
[1852.02 --> 1854.68]  That is how we have been enforcing for the last 20 years.
[1854.88 --> 1856.44]  It's not ideal, but it's what we've got.
[1857.06 --> 1857.84]  All right.
[1857.92 --> 1858.36]  All right.
[1858.42 --> 1859.80]  Everybody, round of applause for Denise.
[1860.02 --> 1861.12]  Speaker number one.
[1865.30 --> 1867.26]  All right.
[1867.88 --> 1869.30]  We thought that buzzer would be fun.
[1869.38 --> 1870.94]  Turns out it's kind of rude.
[1870.94 --> 1877.12]  And so I apologize for that because I could just hop into the code and change it, but let's not do that.
[1877.20 --> 1877.66]  Let's not go there.
[1878.08 --> 1878.36]  Okay.
[1878.50 --> 1879.50]  Is Mo Hampton here?
[1879.94 --> 1880.14]  Woo!
[1880.36 --> 1881.68]  Oh, Mo is here.
[1881.80 --> 1882.80]  Round of applause for Mo.
[1883.72 --> 1884.88]  Come on down.
[1887.20 --> 1888.52]  I feel like we need entrance music.
[1888.62 --> 1889.14]  We do need entrance music.
[1889.14 --> 1889.60]  We probably do.
[1890.10 --> 1891.18]  We'll just beatbox it, right?
[1891.28 --> 1891.48]  Okay.
[1892.12 --> 1893.22]  Oh, I didn't have intro music.
[1893.28 --> 1893.92]  That's okay, though.
[1894.12 --> 1894.54]  I'm okay.
[1894.62 --> 1895.30]  I had it in my head.
[1895.44 --> 1896.22]  Let's play this game.
[1896.28 --> 1899.34]  If you had to pick some intro music for yourself, what did you pick?
[1899.34 --> 1901.96]  Living my life like it's golden.
[1902.20 --> 1902.72]  Jill Scott.
[1902.88 --> 1904.66]  I'm living my life like it's golden.
[1904.84 --> 1906.42]  Living my life like it's golden.
[1906.58 --> 1908.24]  Living my life like it's golden.
[1908.44 --> 1910.02]  Living my life like it's golden.
[1910.26 --> 1911.86]  Living my life like it's golden.
[1912.10 --> 1912.42]  Golden.
[1912.70 --> 1913.20]  All right, Mo.
[1913.24 --> 1914.20]  Well, thanks for joining us.
[1914.30 --> 1915.54]  The five minutes on the clock.
[1915.62 --> 1916.38]  We'd love to chat with you.
[1916.46 --> 1916.68]  Perfect.
[1918.50 --> 1921.52]  So, for me, it's something dear to my heart.
[1921.62 --> 1923.10]  It's just breaking into tech.
[1923.40 --> 1926.94]  And I've done that transition about three years ago, and I love what I do.
[1927.28 --> 1928.76]  There's no other job out there for me.
[1928.76 --> 1931.64]  I'm a software engineer right now for defense.
[1932.26 --> 1933.40]  I'm a government contractor.
[1933.54 --> 1933.66]  Okay.
[1934.34 --> 1940.36]  But the thing that I think about a lot is those that have non-traditional CS backgrounds that come in.
[1940.36 --> 1947.38]  I mean, there's some that come back from chemistry or some people that have something in biology that come in,
[1947.46 --> 1949.56]  or even people with marketing and advertisement.
[1950.30 --> 1957.36]  But I know it's possible, but I don't know how others feel working with somebody who's non-CS on their team.
[1957.36 --> 1959.60]  So, I guess I can open that up.
[1959.74 --> 1963.22]  Like, how do you guys feel when we come into your space?
[1963.96 --> 1964.90]  You're one of me.
[1965.70 --> 1967.36]  First of all, you're not coming into our space.
[1967.44 --> 1968.36]  It's all of our space.
[1968.38 --> 1968.82]  That's true.
[1968.94 --> 1970.46]  That's a very non-inclusive way to say.
[1970.46 --> 1974.50]  I think we need to change the paradigm of what it means to become a developer.
[1974.50 --> 1980.70]  Because I have a CS degree, and that did put me in an advantage.
[1980.86 --> 1981.88]  I'm not going to lie about that.
[1981.96 --> 1983.42]  I do feel like that was a privilege.
[1984.06 --> 1990.88]  That being said, in terms of the things that I had to learn, I had to work hard to, like, learn those skills.
[1990.88 --> 1997.46]  And to see people coming from non-traditional backgrounds, it's – I love working with them.
[1997.58 --> 2005.30]  I feel like they bring a vantage point that I have not thought about before.
[2006.38 --> 2008.62]  I don't know how to, like, formulate my thoughts right now.
[2008.92 --> 2009.26]  Does anyone else –
[2009.26 --> 2011.06]  I 100% agree.
[2011.06 --> 2016.34]  There's a different point of view than somebody who's been traditionally through a certain pipeline or certain classes.
[2016.46 --> 2016.78]  Yes.
[2016.88 --> 2017.94]  There's a different worldview of things.
[2018.06 --> 2018.28]  Yeah.
[2018.62 --> 2018.76]  Yeah.
[2018.84 --> 2021.34]  I think it may be slightly harder to break in.
[2021.60 --> 2021.78]  Yeah.
[2021.86 --> 2026.02]  But honestly, having a more diverse background gives you an advantage once you're in the game.
[2026.42 --> 2033.98]  Because, I mean, this may be tooting my own horn because I'm not a CS background, but I feel like, you know, if you go through a CS program,
[2034.68 --> 2037.98]  yes, you understand a little bit more of a lot of the fundamental stuff,
[2037.98 --> 2041.36]  but you actually don't have that much of a perspective of how the rest of the world works.
[2042.06 --> 2048.12]  And if you're coming from another background, especially if you're coming from another professional background,
[2048.28 --> 2053.56]  that synergy of skills of I understand how this world works and now I understand the code,
[2053.94 --> 2057.60]  like, that's an incredible advantage because you can link between those things.
[2058.20 --> 2064.44]  One place where we as coders often fall down is in communication with people outside of the software world.
[2064.92 --> 2066.24]  But we're building tools for humans.
[2066.24 --> 2067.44]  We need to talk to those people.
[2067.98 --> 2068.38]  Yeah.
[2068.84 --> 2073.54]  I feel like because I went the CS route, I was very tunnel vision.
[2074.04 --> 2076.46]  And when I got to my first job, I did terribly.
[2076.64 --> 2084.72]  Like, I thought I was going to quit or, like, get fired because all I knew was, like, that bubble sort was worse run time than, you know, merge sort.
[2085.06 --> 2089.22]  I didn't understand the practicalities of working in our environment.
[2089.22 --> 2096.30]  And so people who come from alternative backgrounds to get into this role, I think, A, they're used to working harder than we are, right?
[2096.40 --> 2100.20]  Because, you know, unfortunately, they feel like they have to prove themselves more.
[2100.32 --> 2101.84]  And unfortunately, that is the case.
[2101.98 --> 2103.26]  I would love to change that.
[2103.26 --> 2112.02]  But I also feel like if you come from a boot camp, you're better prepared practicality-wise to get into development than a CS background, at least in my experience.
[2112.02 --> 2113.00]  That's true.
[2113.32 --> 2114.42]  That's a good point to bring out.
[2114.72 --> 2118.76]  And I was just thinking about, because you were saying people that come from different backgrounds or different professionals.
[2119.22 --> 2120.26]  Like, for me, I'm a veteran.
[2120.44 --> 2125.54]  So I will look at a problem set differently and kind of charge forward first.
[2125.66 --> 2127.28]  I don't know if that's the right way to do things.
[2127.36 --> 2130.74]  I go ahead first and then figure out the collateral damage later.
[2130.74 --> 2134.20]  But it's a different aspect that we all bring to the table.
[2134.44 --> 2136.72]  And I hope that people are more open towards it.
[2136.84 --> 2140.50]  But sometimes you do feel as if you have to prove yourself more.
[2140.54 --> 2144.50]  Well, degree does not equate to, like, your intelligence.
[2145.10 --> 2150.86]  I know IBM, I think, just recently started doing, like, apprenticeships.
[2150.92 --> 2158.46]  Not apprenticeships, but, like, trials for our boot camp attendees where they would bring them in and, like, hire them for a year and help them grow.
[2158.46 --> 2162.94]  So, like, even if you didn't feel like you were prepared, they would try to coach you along and help you.
[2163.00 --> 2169.14]  Because I think what's important is potential and willingness to learn as opposed to the piece of paper that you would get if you graduated.
[2170.04 --> 2176.74]  And I think it's good also because we have, like, say for me, I'm stronger probably in my soft skills and I have my hard skills in software engineering.
[2176.96 --> 2181.38]  But I do have the people that have that background in education to kind of bridge that gap.
[2181.38 --> 2188.58]  So, it's very good as long as we know our skill sets and we know the gaps that we come together and try to help each other out.
[2189.06 --> 2190.84]  So, I'm glad you guys can talk to me about that.
[2190.98 --> 2191.30]  Oh, yeah.
[2191.46 --> 2193.46]  And let's get rid of the word soft skills.
[2193.54 --> 2194.24]  They're human skills.
[2194.58 --> 2194.96]  They are.
[2195.20 --> 2196.92]  This is how we interact with humans.
[2197.10 --> 2199.66]  And that is the end goal of what we're trying to do.
[2199.72 --> 2200.68]  We're building things for people.
[2201.26 --> 2201.56]  Yeah.
[2203.00 --> 2205.24]  Oh, and I still have, like, ten seconds left, right?
[2205.56 --> 2206.22]  It does.
[2206.46 --> 2207.64]  Can I get natural music then?
[2207.64 --> 2208.36]  Give a shout-out.
[2208.44 --> 2209.38]  You got a shout-out you want to give?
[2209.42 --> 2209.98]  You got five seconds.
[2209.98 --> 2212.34]  Oh, shout-out to everybody at All Things Open.
[2212.46 --> 2213.70]  You guys are amazing for showing up.
[2214.14 --> 2214.88]  Let's hear it from Mo.
[2215.00 --> 2216.02]  Thank you for coming on.
[2216.58 --> 2217.04]  All right.
[2217.06 --> 2217.40]  Thank you.
[2217.62 --> 2218.14]  Thank you.
[2219.90 --> 2220.70]  All right.
[2221.30 --> 2223.18]  How about Maria Lamardo?
[2224.28 --> 2224.52]  Yay.
[2224.52 --> 2225.18]  Here she comes.
[2225.54 --> 2225.78]  All right.
[2225.82 --> 2226.74]  What's your intro music?
[2228.74 --> 2229.60]  I'm not singing.
[2229.62 --> 2230.24]  Don't do that.
[2231.18 --> 2231.78]  Not singing?
[2231.98 --> 2232.84]  I'm not singing.
[2232.88 --> 2234.38]  Please don't give K-Vol intro music.
[2234.40 --> 2235.36]  Nobody wants to hear that.
[2235.82 --> 2239.88]  Well, when you sit down, you can tell me if I pronounced your name correctly or you can chide me if I did not.
[2239.98 --> 2242.00]  Please, we'd love to call you by name.
[2243.06 --> 2244.02]  Maria Lamardo.
[2244.26 --> 2244.64]  Maria.
[2244.88 --> 2245.78]  Maria Lamardo.
[2246.06 --> 2246.54]  Very good.
[2247.10 --> 2247.90]  That is beautiful.
[2248.46 --> 2250.52]  I cannot say it that well, but I'll do my best.
[2251.10 --> 2252.20]  What would you like to talk about today?
[2252.38 --> 2255.62]  So I'm very passionate about web accessibility and building communities.
[2256.14 --> 2256.54]  Okay.
[2257.80 --> 2258.10]  Lovely.
[2258.38 --> 2259.44]  You want to do both of those?
[2259.52 --> 2260.18]  We've got five minutes.
[2260.28 --> 2260.94]  You want to do accessibility?
[2260.94 --> 2262.30]  Web accessibility sounds great.
[2262.42 --> 2262.72]  Okay.
[2263.14 --> 2263.66]  Very good.
[2264.54 --> 2265.54]  What got you into it?
[2265.64 --> 2267.18]  Like, what inspired you to?
[2268.30 --> 2268.74]  Yeah.
[2268.82 --> 2271.80]  So I come from a non-conventional background.
[2272.02 --> 2274.20]  So I'm actually a behavior analyst.
[2274.20 --> 2278.66]  And so I provided behavioral therapy for people with developmental disabilities for eight years
[2278.66 --> 2280.06]  before I switched into development.
[2280.76 --> 2286.18]  And while I was learning how to program, I was, like, so happy when I discovered web accessibility.
[2286.46 --> 2288.12]  And I was like, oh, yes, this is for me.
[2288.28 --> 2293.60]  So after that, I just kind of went all in on web accessibility.
[2293.60 --> 2298.98]  I think what's interesting is that we hear web accessibility, and my first thought goes to, like,
[2299.04 --> 2302.80]  screen reader compliance and, you know, keyboard navigation, like, all these things.
[2303.30 --> 2310.64]  I also feel like accessibility is broadened to thinking about who's consuming your applications
[2310.64 --> 2312.56]  and your website.
[2312.80 --> 2318.36]  So we are in a place of privilege where we have high-speed internet in this country.
[2318.60 --> 2322.92]  But if your app is being consumed by people with lower-speed internet, we need to be mindful of that.
[2322.92 --> 2324.94]  We shouldn't be shipping all of this really heavy stuff.
[2325.34 --> 2330.26]  So accessibility is not just about, you know, what we traditionally think of as accessibility,
[2330.42 --> 2336.00]  but also can people access your application from, like, a...
[2336.00 --> 2336.16]  Right.
[2336.42 --> 2337.62]  Like different hardware.
[2338.00 --> 2338.90]  Yeah, exactly.
[2339.18 --> 2339.20]  Yeah.
[2339.42 --> 2341.00]  The network speed is a huge one.
[2341.10 --> 2346.36]  I have T-Mobile, which is great because they do, they give you internet access anywhere you go, pretty much.
[2346.44 --> 2349.54]  Like, they have 200 countries or there aren't even that many countries.
[2349.66 --> 2352.52]  But essentially anywhere you go, you're going to have internet access.
[2352.92 --> 2354.12]  But it's at 2G speeds.
[2354.12 --> 2360.50]  And if you ever try to access the internet, the websites you're used to accessing from your desktop or your laptop,
[2360.68 --> 2367.78]  even over Wi-Fi or whatever, at 2G speeds on a phone from somewhere halfway across the world, it is painful.
[2368.20 --> 2368.36]  Yeah.
[2368.36 --> 2383.08]  And many of, as Emma highlights, the same practices that are going to make your application accessible to folks here who have assistive software or things like that are the same things that are going to make it accessible to folks who have really poor internet connections.
[2383.08 --> 2383.58]  Yeah.
[2383.58 --> 2383.76]  Yeah.
[2383.82 --> 2392.10]  Even thinking about creating progressive web apps where you could just launch right off your home screen and it's just that much easier, like, one-step launch.
[2392.24 --> 2394.42]  And even if you don't have great connectivity, right?
[2394.54 --> 2395.98]  So it's very important.
[2395.98 --> 2409.32]  And, you know, kind of playing off of what Mo was saying, coming from a different background really gave me a new perspective because I already had the experience from all the users who were struggling, you know, interacting with these applications.
[2409.32 --> 2414.42]  And I just didn't know that the world existed for, like, coding such things, right?
[2414.84 --> 2420.40]  So now coming into it, it's like, well, I know exactly where all the pinpoints are and now what can we do to fix it?
[2420.68 --> 2428.94]  So I do think that it's super advantageous to come in with a fresh perspective and never let, like, your different background be, like, a negative thing.
[2429.00 --> 2430.38]  I think it's always a good thing.
[2430.38 --> 2438.22]  To your point about having seen the users, I wish every developer went and looked at the users of their application and watched them use it.
[2439.34 --> 2441.28]  Like staring at them through their window or what do you mean?
[2443.50 --> 2451.42]  Bring in folks who've never used your application but are in your target audience or who do use your application every day and just watch them use it because your mind will be blown.
[2452.56 --> 2460.14]  We have these models of how our stuff works and other people, like, normal people out in the world don't have those models.
[2460.14 --> 2463.14]  Like, every time I've ever watched somebody use something I build, I'm flabbergasted.
[2463.90 --> 2464.94]  Like, you do what?
[2465.00 --> 2465.66]  You do how?
[2465.98 --> 2466.22]  Yeah.
[2466.58 --> 2470.66]  Like, it's humbling because you realize how much your stuff sucks.
[2471.02 --> 2471.22]  Yeah.
[2471.66 --> 2474.90]  Like, I thought this was really good and then I watched you try to use it and it's not good.
[2475.04 --> 2475.44]  It's not good.
[2475.46 --> 2477.78]  We make assumptions that users use our products the way we would.
[2477.78 --> 2478.40]  The way we would.
[2478.72 --> 2482.08]  Yeah, well, and we're still kind of seeing them every day as we build on them.
[2482.16 --> 2485.28]  So, like, to us, it's like, oh, well, we've definitely improved it and now it's perfect.
[2485.28 --> 2490.84]  Like, and then, you know, somebody's coming into it brand new and it's like, well, none of these make sense.
[2491.64 --> 2495.40]  Is there any real low-hanging fruit of accessibility or a gripe?
[2495.48 --> 2497.30]  Like, why does everybody get this wrong?
[2497.90 --> 2500.56]  Use buttons for buttons, links for links.
[2501.04 --> 2502.26]  Don't take a focus.
[2502.52 --> 2503.00]  Yes.
[2503.16 --> 2503.88]  Like, outline.
[2504.24 --> 2505.38]  Please just don't do it.
[2505.38 --> 2506.64]  Yes.
[2506.88 --> 2513.64]  And if you are going to create custom elements, like custom drop-downs, in instances where you can't use, like, the native semantic HTML elements,
[2513.72 --> 2519.94]  you still have to make concerns such that it functions the same way a native input would.
[2520.18 --> 2520.92]  Yeah, absolutely.
[2521.16 --> 2526.28]  Like, I would always say, like, whether you're considering accessibility or not, like, just put your mouse away.
[2527.12 --> 2531.48]  Try to navigate your entire application with the keyboard only, even if you're not turning on a screen reader.
[2531.48 --> 2536.30]  Like, just kind of go through that basic navigation with your keyboard.
[2536.46 --> 2538.08]  And you should be able to access everything.
[2538.20 --> 2540.40]  And if you can't, then there's something wrong.
[2540.70 --> 2542.22]  So try to figure that out.
[2543.28 --> 2543.98]  Thanks, Maria.
[2544.18 --> 2545.28]  Hey, let's hear it for us.
[2545.32 --> 2545.80]  Thank you, Maria.
[2549.54 --> 2551.64]  Did Brian Douglas make it?
[2551.86 --> 2553.80]  How about Eva Howe or Ava?
[2554.72 --> 2555.58]  There she is.
[2555.64 --> 2556.08]  Come on down.
[2556.70 --> 2557.56]  Let's hear it for her.
[2557.56 --> 2566.36]  As Ava is walking up, since so many people no-showed, that is an opportunity for everyone here who has a topic they want to talk about.
[2566.46 --> 2567.58]  So have that in your head.
[2567.70 --> 2569.66]  What would I talk about if I was on stage?
[2569.70 --> 2572.26]  So when Jared opens the door, you're up.
[2572.42 --> 2572.90]  You're ready.
[2574.14 --> 2575.18]  Is it Eva or Ava?
[2575.36 --> 2575.80]  It's Eva.
[2576.02 --> 2576.24]  Eva.
[2576.52 --> 2577.06]  Very good.
[2577.68 --> 2579.52]  Eva, thanks so much for joining us on stage here.
[2579.62 --> 2581.42]  We're happy to hear what you're up to, what you'd like to talk about.
[2581.42 --> 2589.30]  I work for a company called This.Labs, and we have an apprentice program where one of our big passion projects is getting more women into tech.
[2589.46 --> 2590.28]  Our founder is a woman.
[2590.66 --> 2591.86]  We have a lot of women on board.
[2592.42 --> 2600.92]  And so what we do is we take women who are coming out of boot camp, and we pair them with a mentor, and then we're a consultancy.
[2600.92 --> 2607.70]  So we contract them out together with the idea being that the woman gets mentorship that she needs.
[2608.22 --> 2613.74]  We've heard a lot of companies say they don't like to hire junior developers because they've got to deal with the mentorship aspect.
[2614.02 --> 2614.10]  Right.
[2614.20 --> 2619.94]  So we provide that by pairing them up, and the company gets 40 hours of the junior and 20 hours of the senior.
[2620.92 --> 2624.74]  And then at the end of the contract, the company has the ability to hire the woman.
[2625.36 --> 2625.76]  That's wonderful.
[2625.90 --> 2626.56]  That is awesome.
[2626.56 --> 2627.32]  Sounds very cool.
[2627.82 --> 2628.34]  That is.
[2628.34 --> 2632.08]  How does it work in terms of if you're interested in getting involved or?
[2632.22 --> 2633.24]  You can come by our booth.
[2633.34 --> 2635.54]  We have one, like, literally right outside the store.
[2635.84 --> 2638.56]  Or you can email hi at this dot dot co.
[2639.14 --> 2640.98]  How does the mentorship aspect of that work?
[2641.38 --> 2643.48]  So it varies from woman to woman.
[2643.60 --> 2645.38]  It kind of depends on the contract, too.
[2645.38 --> 2655.58]  But the idea is that the mentor is there to help unblock the woman, to check PRs so that she's not crashing anything when she merges.
[2655.58 --> 2664.78]  And then also just to help navigate being on a technical team, especially in a sense where she may be the only woman on the team.
[2665.78 --> 2672.02]  And that gets a little bit more tricky because a lot of times the senior developer will be male, and that's hard to have that do.
[2672.34 --> 2681.28]  But in that case, we like to try to plug her into her local community where she can find more mentors that are female, too, even if they're not working on that particular project.
[2681.28 --> 2682.28]  Awesome.
[2682.42 --> 2684.88]  What's the biggest challenge that you face with that?
[2686.74 --> 2689.38]  Getting companies to put their money where their mouth is.
[2690.38 --> 2693.16]  Everybody is out there talking about diversity inclusion.
[2693.40 --> 2694.52]  I live in Silicon Valley.
[2695.32 --> 2700.48]  Everybody knows that there's 25, it's like 25% of incoming software engineers are women.
[2700.48 --> 2709.70]  We've done huge, huge pushes on this, and I get calls, and people are super excited, and this is a wonderful program, and we really want to do this.
[2710.40 --> 2713.22]  And I write back, and I get radio silence.
[2713.62 --> 2721.24]  So I feel a little bit frustrated in that aspect that people are very willing to talk about it but not willing to do anything.
[2721.24 --> 2730.10]  So do the women come to you first, and then you match them with a mentor and a company, or do they go to the company?
[2730.82 --> 2740.06]  So we partner with boot camps all around the country, and we get the women applicants mainly through the boot camps, somewhat through just Twitter outreach and our website.
[2740.06 --> 2745.48]  And then the idea is that we, it's kind of a couple of moving pieces.
[2745.86 --> 2754.46]  Obviously, we want to pair the woman up with the company in that she has some basis in the technologies that they're using, and that there's a good fit with the mentor.
[2754.84 --> 2756.72]  Obviously, there's personalities there, too.
[2757.28 --> 2764.26]  And then fit them with the company, and it kind of goes back and forth to make sure that everybody is a good working fit.
[2764.50 --> 2765.22]  That's cool.
[2765.22 --> 2767.78]  I love this idea of an apprenticeship.
[2768.20 --> 2783.12]  I feel like this is something that, I mean, it is definitely important and helpful on the folks coming in, and I think from untraditional backgrounds, boot camps, women who are at a disadvantage, other underrepresented minorities who are at a disadvantage.
[2783.84 --> 2787.28]  Broadly, we as an industry suck at training people.
[2787.72 --> 2788.62]  We are terrible.
[2788.90 --> 2792.46]  I mean, boot camps have somewhat solved the getting in.
[2792.70 --> 2793.96]  I get the first step.
[2794.08 --> 2794.58]  And then what?
[2794.58 --> 2795.60]  What do I do?
[2795.68 --> 2797.36]  Every company I talk to is like, do you have seniors?
[2797.52 --> 2798.00]  Do you have seniors?
[2798.08 --> 2798.70]  Do you have senior folks?
[2799.40 --> 2801.14]  Nobody's training senior folks.
[2801.78 --> 2810.94]  Everyone's trying to hire senior folks, but we don't have this pipeline for how do I get from I just got into the industry to I'm able to lead a team or be a senior or something like that.
[2811.14 --> 2813.92]  So props to you all for doing that.
[2814.00 --> 2814.80]  That's great.
[2814.88 --> 2819.80]  And I think the diversity aspect is a key and important step, but I'd love to see this everywhere.
[2819.80 --> 2825.98]  I completely agree because I think it's really hard for juniors to get the kind of on-the-job mentorship that they need.
[2826.12 --> 2831.12]  And so many companies, for whatever reason, just aren't willing to take that on and hire juniors.
[2831.36 --> 2835.12]  I think that a lot of times either their senior engineers are not positioned to do it.
[2835.18 --> 2836.96]  They don't want to take the extra financial burden of it.
[2836.96 --> 2844.44]  I mean, there's a lot of different reasons for it, but in our case, this is a way of us taking that out of the equation.
[2844.82 --> 2847.90]  Does that typically bypass the typical whiteboarding interview as well?
[2848.54 --> 2848.88]  Yes.
[2849.96 --> 2853.64]  We do do code exercises, but it's not a whiteboard interview.
[2853.80 --> 2857.68]  We are actually a fully remote company, so it would be a little bit difficult to do a whiteboard interview.
[2857.68 --> 2863.16]  And we do other ways of measuring where she is and what technology she's good at.
[2863.86 --> 2865.56]  But no, no whiteboard interviews.
[2865.94 --> 2866.92]  I like that.
[2867.14 --> 2867.58]  Thank you.
[2867.78 --> 2867.96]  Yeah.
[2868.98 --> 2874.68]  Is it code schools only, or can you be from a different background and still apply?
[2874.92 --> 2876.98]  You can be from whatever background you want to apply.
[2877.76 --> 2884.74]  We focus mainly on boot camps just because that's where we find the majority of our non-traditional applicants are from.
[2885.26 --> 2885.82]  Sorry about that.
[2886.08 --> 2886.60]  No worries.
[2886.60 --> 2887.60]  All right.
[2887.66 --> 2888.24]  Let's hear it for Eva.
[2888.82 --> 2889.02]  Woo!
[2895.32 --> 2896.34]  We talked to Vanessa.
[2896.48 --> 2897.06]  Is Vanessa here?
[2897.96 --> 2898.72]  There's Vanessa.
[2898.86 --> 2899.84]  Come on down.
[2900.82 --> 2901.94]  Vanessa Alvarez.
[2902.80 --> 2903.42]  Give her a hand.
[2909.10 --> 2910.38]  Is that the end of your list?
[2910.80 --> 2912.02]  It is the end of your list.
[2912.04 --> 2912.84]  Y'all better get ready.
[2912.84 --> 2913.52]  Y'all be ready.
[2914.18 --> 2914.52]  Welcome.
[2914.88 --> 2915.16]  Hi.
[2915.24 --> 2915.62]  Hi.
[2915.62 --> 2916.62]  Thanks for sitting there.
[2916.62 --> 2916.64]  Thanks for sitting there.
[2916.64 --> 2921.80]  So I was thinking about talking about changing careers in the tech industry.
[2922.00 --> 2925.68]  But then the other person who was talking had a good idea about whiteboarding.
[2925.68 --> 2932.30]  And I just want to hear about what type of interview process you guys do at your current companies.
[2932.30 --> 2933.02]  Because I do.
[2933.02 --> 2935.16]  I don't like whiteboarding.
[2935.16 --> 2937.30]  No one likes whiteboarding interviews.
[2937.30 --> 2938.30]  I like whiteboarding interviews.
[2938.30 --> 2939.62]  I like whiteboarding interviews as a taker.
[2939.62 --> 2939.82]  Why?
[2939.82 --> 2941.56]  I hate it as a way to find good people.
[2941.56 --> 2942.56]  You like whiteboards.
[2942.56 --> 2943.98]  You would prefer to whiteboard?
[2943.98 --> 2944.40]  What?
[2944.40 --> 2944.98]  I wouldn't.
[2944.98 --> 2945.90]  I didn't say I'd prefer.
[2945.90 --> 2946.48]  It's fun.
[2946.48 --> 2948.86]  It's fun for me because I love goofing off.
[2948.86 --> 2949.26]  Right?
[2949.36 --> 2950.98]  So I'll get up with folks and like whiteboarding.
[2950.98 --> 2951.30]  You get to.
[2951.86 --> 2952.28]  I don't know.
[2952.28 --> 2953.64]  I like whiteboards in general.
[2953.64 --> 2954.66]  That's how I brainstorm.
[2954.66 --> 2955.60]  That's how I do whatever.
[2955.60 --> 2957.04]  I'm just a fan of whiteboards over here.
[2957.04 --> 2958.66]  I have whiteboards in my office.
[2959.12 --> 2960.74]  It's a terrible way to interview people.
[2960.92 --> 2961.04]  Yeah.
[2961.12 --> 2962.18]  It's absolutely terrible.
[2962.32 --> 2962.74]  You should have liked that.
[2962.74 --> 2963.68]  I think it's fun.
[2963.96 --> 2964.82]  It's terrible.
[2964.98 --> 2966.38]  Can you enumerate why it's terrible?
[2966.96 --> 2970.56]  Why it's terrible is because it's testing completely different things than what you care
[2970.56 --> 2971.96]  about for a candidate.
[2971.96 --> 2976.48]  So whiteboarding is testing how well do you improvise on the spot in front of people that
[2976.48 --> 2978.96]  you don't know with a marker in your hand.
[2979.10 --> 2979.66]  And communicate.
[2980.16 --> 2986.12]  And communicate with people you don't know, which communication, that part is actually
[2986.12 --> 2989.10]  in my opinion kind of valid because I think it's important that engineers can communicate.
[2989.10 --> 2992.92]  No, that's valid, but in terms of being able to eloquently communicate.
[2993.38 --> 2998.12]  On the spot, under pressure, in front of people you don't know, oftentimes with folks
[2998.12 --> 2999.94]  who are not the kindest of interviewers.
[3000.14 --> 3000.32]  Right.
[3000.32 --> 3005.34]  So yeah, it's setting folks up for failure unless they're skilled in things that are
[3005.34 --> 3006.92]  not actually helpful for their job.
[3007.08 --> 3007.34]  Yeah.
[3007.52 --> 3013.36]  I had a, it was a good experience, but it really frustrated me because it was an interview
[3013.36 --> 3016.32]  for a UX engineering role building design systems with React.
[3018.00 --> 3023.02]  And the two out of the four interviews were about algorithms.
[3023.50 --> 3027.74]  And so I had to code binary trees on a whiteboard and find the broken edge.
[3027.74 --> 3030.72]  And I'm like, how is this relevant to the job I'm going to be doing?
[3030.84 --> 3031.48]  It's not.
[3031.62 --> 3033.76]  And that is so unfair to so many candidates.
[3033.76 --> 3037.98]  Going back to the whole, what if I'm not from a traditional CS background?
[3038.50 --> 3038.58]  Yeah.
[3038.72 --> 3044.00]  How is that testing anyone's ability to like, you know, deduce information and like problem
[3044.00 --> 3045.18]  solve to a certain extent?
[3045.24 --> 3045.64]  It's not.
[3045.64 --> 3047.80]  What if English isn't my first language?
[3047.92 --> 3048.62]  I know.
[3048.88 --> 3049.82]  Well, yeah, exactly.
[3050.16 --> 3052.24]  So I would just suggest like the appropriate.
[3053.12 --> 3053.30]  Yeah.
[3053.30 --> 3053.80]  What's better?
[3054.02 --> 3055.48]  What will be better instead of the one?
[3055.48 --> 3056.74]  I like the take home exam.
[3057.12 --> 3059.52]  So I had a really great interview with Gatsby.
[3059.52 --> 3065.40]  I, it was, they gave me a few, they gave me three questions and they said, answer whichever
[3065.40 --> 3066.80]  one you feel comfortable answering.
[3067.02 --> 3069.54]  To give options to your candidates is incredible.
[3069.68 --> 3071.94]  That whole interview process was seamless.
[3072.12 --> 3077.68]  They also, like the take home assessment, first of all, they were going to pay you for
[3077.68 --> 3081.46]  it, which is amazing because often these companies put you through the ringer with the interviews
[3081.46 --> 3082.96]  and it's unpaid.
[3083.18 --> 3083.40]  Right.
[3083.40 --> 3083.72]  Right.
[3084.20 --> 3089.76]  The second piece of that is to do the tasks that you would be doing on the job.
[3090.42 --> 3091.28]  A, it's practical.
[3091.52 --> 3093.86]  B, you get to see if you even want to do this job in the first place.
[3093.96 --> 3094.10]  Yeah.
[3094.42 --> 3098.68]  So I think sticking to practical things that are also manageable because a lot of us have
[3098.68 --> 3104.62]  families and other obligations, we can't give up time to go onsite and give up a full
[3104.62 --> 3105.06]  day of work.
[3105.14 --> 3107.50]  And applying is like almost a full time job.
[3107.68 --> 3108.00]  It is.
[3108.24 --> 3108.74]  It is.
[3109.06 --> 3109.30]  Yeah.
[3109.30 --> 3114.56]  So something interesting that we've been doing in my company, we stopped the whiteboarding
[3114.56 --> 3121.14]  and right now what we're doing is basically we have a bunch of like functions and then
[3121.14 --> 3123.74]  we tell the person like, hey, just pretend that you're working.
[3123.84 --> 3124.62]  We're working together.
[3125.00 --> 3126.72]  We're collaborating just like a normal day.
[3127.26 --> 3129.40]  And just tell us what is this function doing.
[3129.84 --> 3134.88]  And then we start like talking and then if the person like, we want that engagement and
[3134.88 --> 3140.40]  we like that conversation happening, we're testing more of like, not so much of like
[3140.40 --> 3144.56]  their technical skills, yes, in a part, but more about like collaboration.
[3144.98 --> 3148.40]  We want if this person will reach to us if they have any questions.
[3148.68 --> 3148.82]  Right.
[3148.96 --> 3149.14]  Yep.
[3149.22 --> 3151.80]  And it has worked for that us very well.
[3151.80 --> 3154.22]  So like less of a test and more of a collaboration.
[3154.56 --> 3154.98]  Right.
[3155.10 --> 3157.96]  So it's like, do you read and understand this function?
[3158.12 --> 3158.38]  Yes.
[3158.48 --> 3158.86]  Okay.
[3159.42 --> 3159.80]  Awesome.
[3159.98 --> 3162.22]  And if they get stuck, what are you thinking about?
[3162.22 --> 3165.86]  Tell us, oh, this is what I'm going through my mind and that has worked better.
[3165.86 --> 3171.66]  And we have gotten them to be not so nervous and it has helped us a lot.
[3172.14 --> 3172.54]  So yeah.
[3172.66 --> 3175.08]  I also think it takes a lot of skill to be a good interviewer.
[3175.26 --> 3175.48]  Yeah.
[3175.62 --> 3176.50]  Yeah, absolutely.
[3176.86 --> 3177.78]  That's the right thing.
[3178.30 --> 3178.46]  Yeah.
[3178.96 --> 3179.80]  The closer.
[3180.40 --> 3183.40]  I was just going to say as a last point, please don't try to trick your candidates and
[3183.40 --> 3184.90]  show who's smarter in the room.
[3184.98 --> 3185.86]  That's not a good point.
[3186.70 --> 3192.06]  The closer you can get to it being what it's like to actually work here, the better of a
[3192.06 --> 3192.96]  tell you're going to be able to get.
[3193.02 --> 3196.66]  And you do want to scope that within the bounds of what's possible for that person.
[3196.66 --> 3201.12]  Like my favorite, both as an interviewer and an interviewee, my favorite way to interview
[3201.12 --> 3204.10]  someone is to do a scoped paid project.
[3204.34 --> 3204.92]  Love that.
[3204.98 --> 3207.88]  Now, that is not always possible.
[3208.22 --> 3211.50]  If you have a full-time job and you have family obligations, you may not be able to take
[3211.50 --> 3214.08]  another paid, you know, another project like that.
[3214.12 --> 3215.38]  And so you need to be accommodating.
[3215.38 --> 3220.36]  But the more you can get to this is exactly what it's actually going to be like working
[3220.36 --> 3225.64]  in this environment, the better you both have of being able to tell is this going to
[3225.64 --> 3226.22]  be a good fit.
[3226.44 --> 3226.58]  Yeah.
[3227.46 --> 3227.86]  Awesome.
[3228.24 --> 3229.20]  Well, that's our time, Vanessa.
[3229.30 --> 3230.20]  Thanks so much for sitting down.
[3230.20 --> 3230.36]  Thank you.
[3230.72 --> 3231.10]  Let's hear it.
[3236.16 --> 3237.10]  Okay, audience.
[3237.28 --> 3241.56]  If you have a project that you've been working on and you want to tell the world, if you have
[3241.56 --> 3246.08]  a passion that you care about and you'd like to chat with us, if you have a hand and you'd
[3246.08 --> 3249.30]  like to raise it high in the air, a heartbeat.
[3249.66 --> 3250.04]  We got one.
[3250.44 --> 3250.70]  Oh.
[3251.10 --> 3251.26]  Oh.
[3251.70 --> 3251.92]  All right.
[3252.02 --> 3252.36]  Either one.
[3252.44 --> 3253.28]  We'll line them up here.
[3253.62 --> 3253.78]  Yeah.
[3253.78 --> 3254.50]  Run on down.
[3254.62 --> 3257.28]  Let's hear it for the nice man who's running.
[3257.60 --> 3258.60]  I knew the Price is Right music.
[3259.26 --> 3260.74]  Come on down.
[3261.60 --> 3262.74]  If I knew it, I would sing it.
[3262.96 --> 3263.70]  I was just singing.
[3263.76 --> 3264.08]  Hello.
[3264.34 --> 3264.74]  Greetings.
[3265.20 --> 3265.48]  Hello.
[3265.68 --> 3265.92]  Hello.
[3266.28 --> 3266.82]  Thanks for joining us.
[3266.82 --> 3267.20]  Hey, guys.
[3267.40 --> 3268.38]  I'm Clinton Dreisbach.
[3268.62 --> 3269.12]  Hey, Clinton.
[3269.34 --> 3270.12]  Nice to meet you.
[3270.14 --> 3271.32]  I keep hearing people talking about boot camps up here.
[3271.32 --> 3274.82]  And I decided to run up because I co-founded one and teach it one.
[3274.98 --> 3276.34]  So I thought it would be interesting to talk.
[3276.48 --> 3276.76]  Awesome.
[3276.90 --> 3277.76]  Tell us about that.
[3278.04 --> 3278.56]  So, yeah.
[3278.80 --> 3279.96]  A bunch of my students are here.
[3280.04 --> 3281.30]  They're all in the audience, which is awesome.
[3281.42 --> 3282.22]  I hope one of them runs up here.
[3282.22 --> 3282.58]  Hi, students.
[3283.50 --> 3283.72]  Hello.
[3284.10 --> 3284.26]  Wait.
[3284.26 --> 3285.06]  What's the boot camp called?
[3285.12 --> 3285.86]  So it's called Momentum.
[3286.08 --> 3286.64]  It's local.
[3286.74 --> 3288.36]  It's just in Durham, North Carolina.
[3288.50 --> 3288.68]  Okay.
[3289.14 --> 3295.92]  But, yeah, me and co-founder, Jessica Mitch, we formed it after we both got our former boot camp
[3295.92 --> 3298.46]  closed down and we knew what we were doing and loved it.
[3298.64 --> 3301.30]  So, yeah, it's the most fulfilling and awesome thing to get to see.
[3301.32 --> 3305.08]  New developers go from nothing to, like, full awesome developers.
[3305.34 --> 3305.50]  Yeah.
[3305.84 --> 3310.28]  But, yeah, all the problems that people are talking about with not hiring junior developers.
[3310.44 --> 3312.48]  Like, I get to see this up close and personal every day.
[3312.48 --> 3319.02]  And it's, you know, it's, that's the most disheartening thing, seeing people say, oh, we only hire senior developers.
[3319.02 --> 3326.56]  Because the people that I see every day grow as developers are going to be the most amazing developers you've ever met.
[3326.64 --> 3327.52]  They're just not quite there yet.
[3327.62 --> 3327.76]  Right.
[3327.88 --> 3328.82]  But they're getting there.
[3329.52 --> 3330.74]  But, yeah, it's such a cool thing.
[3330.80 --> 3331.62]  I can answer any questions.
[3331.62 --> 3332.70]  How do we bridge that gap?
[3333.04 --> 3334.30]  I mean, there's obviously a problem.
[3334.98 --> 3337.64]  But there doesn't have to be any obvious solutions to that problem.
[3337.64 --> 3350.60]  So, the easiest way I've seen so far, and this is, this takes time, is helping companies learn that hiring junior developers and training them is pretty much the best investment they can have.
[3350.68 --> 3352.60]  You know, our industry, people change jobs so quickly.
[3352.76 --> 3352.94]  Right.
[3352.94 --> 3362.70]  But you bring someone in early and you help train them and they become a really loyal, really amazing employee that knows what's going on there, you know, as well as anyone.
[3363.66 --> 3365.12]  But, yeah, I think it's educational.
[3365.12 --> 3367.26]  The risk is that the loyalty doesn't actually stick.
[3367.46 --> 3374.96]  Because people do move around so much that if I'm going to invest three years in a person and they're going to go upgrade to a different job, that's, to me, that's a loss.
[3375.56 --> 3375.70]  Yeah.
[3376.28 --> 3380.88]  Well, I think to both of your points, you have to think about it as an investment.
[3381.08 --> 3382.08]  Investments have risks.
[3382.22 --> 3382.36]  Right.
[3382.36 --> 3383.22]  There are things.
[3383.38 --> 3392.18]  But if we're willing to put in, you know, thousands of dollars to recruiting, we should be willing to put in half of that amount to training the people we already have.
[3392.28 --> 3392.76]  Yeah, absolutely.
[3392.76 --> 3394.78]  I mean, frankly, I'd say twice that amount, right?
[3394.84 --> 3406.12]  If it costs you $10,000 to recruit a new senior developer and you have someone who is already contributing, but you can spend $10,000 to upgrade them to a senior developer, like, it's a no-brainer.
[3406.86 --> 3406.96]  Right.
[3406.96 --> 3417.16]  There's an old saying that I'll butcher, but it goes something like, what if, talking about investing training in their engineers, what if we spend all this money training them and then they leave?
[3417.24 --> 3419.72]  And then the response is, what if we don't spend it and then they stay?
[3419.72 --> 3421.86]  Like, they're going to suck forever.
[3422.60 --> 3423.24]  No, they won't.
[3423.38 --> 3425.86]  They'll still get better, but you can see that point there.
[3425.86 --> 3434.26]  And the other thing past loyalty is I think there's no better way for your senior developers to get better at being senior developers than to train junior developers.
[3434.42 --> 3436.58]  Like, what are you seeing you're in if you have no one you're teaching?
[3437.36 --> 3440.60]  People ask me all the time, like, oh, do you get bored teaching the same thing over and over?
[3441.00 --> 3441.86]  Like, you have no idea.
[3441.96 --> 3444.96]  I learn something every single day teaching new developers.
[3445.36 --> 3447.30]  They ask questions that I would have never thought of.
[3447.64 --> 3448.98]  There's new technologies I have to learn.
[3448.98 --> 3460.46]  Like, I've grown as a developer more teaching than I ever did previously, and I think that's going to be true in any company if you have your senior developers actively working to mentor people.
[3460.88 --> 3461.86]  What is your curriculum?
[3462.46 --> 3465.54]  We do JavaScript and Python, so it's a full-stack curriculum.
[3466.48 --> 3467.16]  I just switch things.
[3467.58 --> 3474.02]  I tinker all the time with it, but so we do JavaScript for the first half of the course and Python and Django for the second half of the course.
[3474.12 --> 3474.84]  And how long is it?
[3474.98 --> 3475.92]  It's 12 weeks long.
[3476.08 --> 3476.42]  Oh, nice.
[3476.84 --> 3477.00]  Yeah.
[3477.00 --> 3478.20]  Full immersion or part-time?
[3478.20 --> 3486.14]  It's full immersion, so it's all day long, you know, nine to five, like four hours of lecture, and, you know, who knows how many hours of projects every day.
[3486.90 --> 3488.40]  I kind of burn them out a little bit.
[3488.58 --> 3490.12]  We try and keep it to 60 hours a week.
[3490.20 --> 3493.26]  The folks back there know how many hours, and they're going, oh.
[3494.56 --> 3497.96]  Yeah, so they're getting a break right now because we get to come out here and see this.
[3498.14 --> 3500.74]  But I thought it was so cool to have them immersed in the industry.
[3500.92 --> 3502.22]  I love it that we have ETO here.
[3502.22 --> 3507.66]  Also, the fact that you brought them here is super cool because, like, I didn't get to go to conferences.
[3508.20 --> 3510.96]  Until I was, like, well into my first job.
[3511.22 --> 3511.42]  Yeah.
[3512.12 --> 3512.54]  That's great.
[3513.42 --> 3518.18]  So do you feel pressured to constantly be updating that curriculum, especially with how fast the industry moves?
[3518.34 --> 3518.64]  Yeah.
[3518.82 --> 3520.88]  I mean, for multiple reasons, right?
[3520.88 --> 3523.10]  I always want them to have the very best of content.
[3523.10 --> 3530.36]  And also, for me and the other instructors, it is, I mean, it sharpens our skills to constantly be revisiting what we're doing, making sure we're doing it right.
[3530.78 --> 3535.84]  But, you know, every class there's stuff that people get stuck on that I go, oh, I know a better way to teach that or a better way to learn that.
[3536.74 --> 3539.90]  Yeah, so there's some pressure, but, I mean, it's fun to do.
[3540.22 --> 3544.42]  I think, you know, teaching is hard, but if you have the bug, you never want to stop doing it.
[3544.42 --> 3546.62]  How can people apply?
[3547.72 --> 3548.86]  How can people apply?
[3549.08 --> 3551.56]  Well, they can go to MomentumLearn.com if they're interested.
[3551.86 --> 3554.36]  But, yeah, or you can just find me or anyone else around here.
[3554.84 --> 3555.40]  Very good.
[3555.64 --> 3556.14]  Thank you so much.
[3556.14 --> 3556.98]  Thank you so much.
[3556.98 --> 3586.96]  Thank you so much.
[3586.98 --> 3616.96]  Thank you.
[3616.98 --> 3620.74]  All right, let's go.
[3621.28 --> 3623.68]  I mean, we just flipped the podcast.
[3624.04 --> 3624.36]  All right.
[3624.50 --> 3625.22]  Okay, so we started.
[3625.40 --> 3626.56]  Oh, man, we just started.
[3626.56 --> 3627.60]  We're wasting your time.
[3627.60 --> 3627.92]  Oh, okay.
[3627.92 --> 3628.54]  What do you want to talk about?
[3628.62 --> 3628.98]  What would you like to talk about?
[3628.98 --> 3634.66]  Okay, so I tend to hang out in the web performance space.
[3635.00 --> 3637.24]  So I was like, oh, man, I think people are going to be bored.
[3637.36 --> 3642.58]  But I'm here to talk about something that's being worked on right now, which is the JPEG Excel.
[3642.58 --> 3644.40]  So kind of a new format.
[3644.40 --> 3644.84]  Okay.
[3644.84 --> 3649.76]  So for all the web developers out there, images are a huge problem on the web.
[3649.76 --> 3659.56]  But in fact, actually, for the person who talked about accessibility, the number two, actually, issue in accessibility is through images, which is all text.
[3660.06 --> 3662.72]  So images are a problem, like, through and through.
[3662.72 --> 3668.98]  So with the JPEG Excel, basically, what's going to happen is, well, essentially, what happened, let me backtrack.
[3669.42 --> 3672.40]  A couple years ago, is this my time up?
[3672.66 --> 3674.66]  No, that's the light going crazy.
[3674.78 --> 3675.02]  Okay.
[3675.88 --> 3686.36]  A couple years ago, to celebrate sort of the 25th anniversary of the JPEG, the joint photographics expert group put out a CFP.
[3686.36 --> 3690.38]  And because the JPEG is a format that's kind of, like, always being worked on.
[3691.30 --> 3695.08]  And so they receive seven submissions.
[3695.86 --> 3697.08]  And two are picked.
[3697.30 --> 3703.26]  So basically, they're trying to see, like, how we can go about and improve the JPEG as a format.
[3704.00 --> 3706.34]  And essentially what happened, two were selected.
[3706.70 --> 3710.36]  One, so they're going to take sort of the best of both.
[3710.36 --> 3723.02]  So one is the, I'm going to pronounce it improperly, but FWIF, which is the free universal image format, which was being developed by Cloudinary.
[3723.48 --> 3730.54]  And the second was PIK, which was another format that was sort of being experimented with by the people at Google.
[3731.20 --> 3739.96]  So the two, sort of, like, the best of both are going to be used as they sort of make their way to this new format, which is going to be called the JPEG Excel.
[3740.36 --> 3743.06]  And what are the advantages of JPEG Excel?
[3743.44 --> 3752.18]  So essentially with any sort of, like, recent format, you're going to get some improved encoding, for sure.
[3752.64 --> 3762.48]  But things like responsive web design has been a huge burden on the web, simply because a lot of people just do not get it right.
[3762.48 --> 3770.54]  So you end up having a lot of data waste being sent down the pipe to users and actually by corporations as well, because you get that wrong.
[3770.64 --> 3775.22]  Those are your servers that you have to sort of, you know, pump the resources down.
[3775.88 --> 3782.22]  So that, you know, obviously you're going to have animation, which is also a bit of an issue on the web,
[3782.22 --> 3788.24]  because a lot of people do fall back to the grossly oversized GIF.
[3788.72 --> 3789.76]  Yes, I said GIF.
[3791.76 --> 3796.76]  And so that encoding is going to be improved.
[3797.12 --> 3798.68]  Obviously, we're going to have alpha channels.
[3798.80 --> 3800.72]  They're going to have adaptive compression.
[3800.98 --> 3806.42]  So essentially parts of the images are going to be compressed a little better than the others, the ones that need it anyhow.
[3806.42 --> 3815.40]  And obviously, it's most likely going to be mostly lossy, but with the best encoding possible at the time.
[3815.58 --> 3819.16]  So you have this sort of, like, casi lossless thing going on.
[3820.18 --> 3823.80]  That's a lot of words that I don't know that much about, but I'm intrigued.
[3824.04 --> 3824.30]  Okay.
[3824.40 --> 3827.36]  Well, I mean, there's information online, for sure.
[3827.78 --> 3830.46]  If you go to, I believe, jpeg.org.
[3830.46 --> 3838.26]  But at the end of the day, I think most people know images, and most web developers certainly need to work with images.
[3839.20 --> 3849.70]  And it's just something that by, you talked about sort of having constricted data or networks and whatnot.
[3849.94 --> 3850.60]  100%.
[3850.60 --> 3851.06]  Exactly.
[3851.36 --> 3852.98]  You don't handle images properly.
[3853.36 --> 3854.70]  This is where you're going to feel it the most.
[3854.92 --> 3858.08]  Where did, how did you, your question is probably more pertinent than mine.
[3858.70 --> 3859.76]  You're wasting this time.
[3859.76 --> 3860.52]  Yeah, yeah, yeah.
[3860.92 --> 3861.32]  All of you.
[3861.32 --> 3861.52]  Come on.
[3861.56 --> 3861.92]  Come on.
[3861.92 --> 3864.68]  The question I had, actually, you brought up accessibility.
[3864.98 --> 3865.16]  Yes.
[3865.24 --> 3874.56]  And one of the things that I have seen bandied around is embedding some of that alternate text in images so that it's not dependent on the web developer.
[3874.70 --> 3875.52]  It can actually be encoded.
[3875.62 --> 3876.96]  Is that something that's included in this?
[3877.04 --> 3878.46]  So that's actually separate.
[3878.56 --> 3882.02]  It's funny you should say that because I'm preparing some approach I can talk on that.
[3882.30 --> 3886.42]  There is a push towards automation of alt text.
[3886.42 --> 3888.62]  So this is completely separate.
[3888.98 --> 3892.38]  But IG or Instagram, Facebook has been doing it for a while.
[3893.34 --> 3895.36]  Chrome in Canary as an experiment.
[3895.50 --> 3898.32]  You could actually get that done right now as we speak.
[3898.64 --> 3899.62]  But it's behind a flag.
[3899.78 --> 3902.84]  But again, that has less to do with performance, unfortunately.
[3903.22 --> 3907.18]  Yeah, that feels like something where machine learning image recognition could be super powerful.
[3907.18 --> 3907.60]  It totally is.
[3907.68 --> 3908.64]  It's happening as we speak.
[3909.52 --> 3910.26]  Thank you so much.
[3910.26 --> 3910.56]  We appreciate it.
[3910.56 --> 3911.06]  Thank you very much.
[3911.18 --> 3911.48]  Awesome.
[3911.60 --> 3911.86]  Thank you.
[3917.30 --> 3918.02]  There you go, Emma.
[3919.24 --> 3919.98]  That's all I know.
[3920.40 --> 3920.96]  All right.
[3927.42 --> 3928.20]  Come on.
[3928.20 --> 3928.38]  Go.
[3928.94 --> 3929.62]  Christ is right.
[3929.96 --> 3931.14]  We need an extra mic over here.
[3931.90 --> 3934.20]  We have a few more slots after this one if you'd like.
[3934.68 --> 3936.40]  If you're interested, come close.
[3936.56 --> 3936.78]  Yeah.
[3936.78 --> 3938.72]  So we have less awkward stalling.
[3938.80 --> 3939.00]  Hello.
[3939.64 --> 3939.84]  Hi.
[3939.90 --> 3940.32]  What's your name?
[3940.42 --> 3941.42]  What would you like to talk about?
[3941.44 --> 3942.18]  My name is Jill Burns.
[3942.66 --> 3944.46]  And first of all, love your podcast.
[3944.68 --> 3945.28]  Well, thank you.
[3945.32 --> 3945.52]  Yes.
[3945.52 --> 3946.44]  Great to meet you guys.
[3946.56 --> 3947.28]  We appreciate that.
[3948.08 --> 3953.44]  I wanted to just mention that I came into coding, well, years ago.
[3953.44 --> 3958.44]  But re-entered recently in fields through tech re-entry.
[3958.44 --> 3963.86]  I had 18 years as a computer programmer, software engineer.
[3964.04 --> 3964.30]  Wow.
[3964.62 --> 3967.08]  Took 10 years off, raised kids.
[3968.30 --> 3969.08]  Full-time job.
[3969.24 --> 3969.38]  Yeah.
[3969.72 --> 3971.32]  And moved three times.
[3971.40 --> 3971.68]  Okay.
[3972.20 --> 3976.98]  And then came back in as a software developer again.
[3977.34 --> 3981.40]  So the senior, we had an apprenticeship.
[3981.40 --> 3986.02]  I had a mentor, which was crucial to the program.
[3987.08 --> 3991.94]  But I think it's another way to bring women in that have had experience.
[3992.20 --> 3995.96]  And you know that we've done our learning at one point.
[3996.14 --> 3996.44]  Right.
[3997.74 --> 3999.74]  And then just have the opportunity.
[3999.94 --> 4001.72]  I'm so excited to be back in the field.
[4001.82 --> 4002.30]  That's beautiful.
[4002.30 --> 4005.64]  What's changed the most from your first time to now?
[4010.56 --> 4013.90]  I think the database work for me.
[4015.22 --> 4016.20]  Way easier now?
[4016.28 --> 4016.70]  Way harder?
[4016.82 --> 4017.16]  Way different?
[4017.62 --> 4025.28]  I mean, relational databases into the NoSQL was probably, I would say, my biggest leap.
[4025.54 --> 4025.76]  Okay.
[4025.76 --> 4034.00]  When I left, I was doing Java and web services, and now it's Node.js, Cloud, and NoSQL.
[4034.34 --> 4036.78]  So a couple of different jumps.
[4037.34 --> 4040.38]  But I started in the mainframe.
[4040.74 --> 4043.50]  So going from Fortran in high school.
[4043.58 --> 4043.88]  Yeah.
[4044.24 --> 4044.96]  Pascal and Cloud.
[4044.96 --> 4045.98]  We could probably learn our thing.
[4046.08 --> 4046.58]  Fortran.
[4046.64 --> 4047.06]  All right.
[4047.06 --> 4047.32]  All right.
[4047.34 --> 4047.94]  History.
[4048.12 --> 4050.16]  I was in scientific computing back in the day.
[4050.58 --> 4051.62]  What hasn't changed then?
[4051.88 --> 4053.42]  You know, you come back and you're like, what's the same?
[4053.44 --> 4053.52]  Exactly.
[4053.52 --> 4055.56]  I've seen it change a number of times.
[4055.56 --> 4056.74]  Well, what hasn't changed?
[4057.26 --> 4059.16]  Oh, you're saying everything has changed.
[4059.36 --> 4060.24]  Has anything not changed?
[4060.82 --> 4061.58]  I get it.
[4061.92 --> 4063.02]  What hasn't changed?
[4063.26 --> 4064.20]  Surely there's some constants.
[4064.44 --> 4065.72]  Change is the only constant, right?
[4066.94 --> 4067.56]  I would say...
[4068.78 --> 4073.38]  Jerry gives me this look like, you're going to back me up here, right?
[4073.48 --> 4074.40]  I just blew up his mind.
[4074.56 --> 4075.32]  Did you remind me of that?
[4075.32 --> 4076.66]  I'm not sure there are any constants.
[4077.46 --> 4080.22]  I mean, there are a lot of similarities.
[4080.52 --> 4081.88]  I will say there are a lot of similarities.
[4081.88 --> 4087.34]  But the basis of who I'm working with is getting a lot more diverse than historically.
[4087.34 --> 4087.78]  Yeah.
[4089.04 --> 4095.48]  I draw on a lot of my knowledge from other programming languages and databases.
[4096.48 --> 4098.30]  How did you get up to speed when you came back in?
[4098.30 --> 4099.88]  I started...
[4099.88 --> 4100.48]  Well, you know what?
[4100.54 --> 4104.04]  I attended conferences like this when I was out.
[4104.26 --> 4105.46]  I did attend conferences.
[4105.60 --> 4106.66]  I listened to podcasts.
[4107.06 --> 4107.46]  Excellent.
[4107.46 --> 4113.86]  I did online training when I could because it was still a full-time job raising kids.
[4113.94 --> 4114.14]  Yes.
[4115.56 --> 4116.22]  So, yeah.
[4116.52 --> 4117.86]  That was it.
[4117.92 --> 4127.28]  And then when I started, it was a 12-week apprenticeship with the option of, on both sides, being hired
[4127.28 --> 4128.44]  or not at the end.
[4128.76 --> 4132.56]  So, that was my 12-week of, okay, here's your project.
[4132.96 --> 4133.10]  Yeah.
[4133.10 --> 4136.22]  That is the best way to do it.
[4136.22 --> 4137.52]  If you can make that happen.
[4137.70 --> 4141.52]  I mean, if I'm looking for a job, that's my favorite way to interview because it's how
[4141.52 --> 4144.30]  you learn what this place is going to be like to work with.
[4144.40 --> 4147.62]  Because folks will put on their happy face when they're interviewing you and you work with
[4147.62 --> 4149.70]  them for a while and you discover it is a cesspit.
[4150.16 --> 4154.96]  Or other folks who are not super jazzed at interviews and don't do it very well, but
[4154.96 --> 4156.80]  then you work there and it's the best place ever.
[4157.16 --> 4157.46]  So, yeah.
[4157.68 --> 4158.22]  That is...
[4158.22 --> 4159.72]  That's how Europe does it.
[4159.72 --> 4164.08]  So, when I moved to Germany, they were like, oh, you're on probation for six months.
[4164.12 --> 4164.94]  And I was like, what do you mean?
[4165.66 --> 4166.92]  And they're like, no, it's a standard.
[4166.92 --> 4167.98]  So, you're on...
[4167.98 --> 4170.80]  Everyone generally joins probation for six months.
[4171.02 --> 4172.70]  At the end, either party can walk away.
[4172.98 --> 4174.96]  That's a good amount of time to, like, get your...
[4174.96 --> 4175.38]  To know.
[4175.58 --> 4175.86]  Yeah.
[4176.00 --> 4176.14]  Yeah.
[4176.28 --> 4176.90]  But that's...
[4176.90 --> 4178.56]  We should standardize that.
[4178.64 --> 4179.30]  Kind of cool idea.
[4179.50 --> 4179.78]  Yeah.
[4179.78 --> 4180.50]  Absolutely should.
[4180.54 --> 4184.16]  And I did the three-question take-home interview.
[4184.16 --> 4184.26]  Yeah.
[4184.58 --> 4185.94]  So, let's all get back in.
[4186.00 --> 4186.54]  You like that.
[4186.82 --> 4187.88]  I got the three questions.
[4187.88 --> 4188.22]  Yeah.
[4189.00 --> 4189.26]  Yeah.
[4189.50 --> 4191.58]  I think the both sides is key, too, right?
[4191.66 --> 4191.78]  Yes.
[4191.78 --> 4192.54]  Like, this is...
[4192.54 --> 4195.88]  If it's instituted as a company power play, it's terrible, right?
[4195.92 --> 4199.52]  Like, oh, we're going to be watching you for this first three months or six months.
[4199.94 --> 4201.08]  And, you know, then we decide...
[4201.08 --> 4202.30]  But probation is a weird word for me.
[4202.30 --> 4205.88]  But if you come in with it saying, like, this is a period...
[4205.88 --> 4206.74]  I do it as a consultant.
[4206.88 --> 4208.58]  I do it if I'm looking for a job.
[4208.58 --> 4210.26]  Like, I want to do a test run.
[4210.70 --> 4214.64]  And I want to figure out by working with you, is this a good place or not?
[4214.72 --> 4216.68]  And it's my decision to walk away.
[4216.68 --> 4219.02]  And, yeah, you could decide if you want me to go, too.
[4219.06 --> 4219.58]  But you won't.
[4220.24 --> 4220.90]  It's my decision.
[4220.90 --> 4221.40]  But you won't.
[4221.74 --> 4222.24]  You won't.
[4223.22 --> 4223.86]  And they get me.
[4224.48 --> 4225.08]  Yeah, there you go.
[4225.74 --> 4226.24]  That's awesome.
[4228.14 --> 4228.50]  Awesome.
[4229.34 --> 4229.54]  Yay.
[4230.02 --> 4231.12]  Jill, thanks so much for joining us.
[4231.12 --> 4231.26]  Yes, thank you.
[4231.26 --> 4232.20]  Thanks for listening to the show.
[4232.36 --> 4233.80]  And welcome back to the community.
[4233.80 --> 4234.14]  Yeah, welcome.
[4234.14 --> 4234.28]  Yeah.
[4234.28 --> 4234.84]  All those years.
[4237.34 --> 4237.66]  Okay.
[4237.66 --> 4240.36]  I did see another hand poke up and then it dropped immediately.
[4240.62 --> 4242.32]  I'm hoping that hand will go back up again.
[4242.46 --> 4243.28]  Oh, here it is right here.
[4243.78 --> 4243.86]  Oh.
[4243.92 --> 4244.72]  Yes, yes, yes.
[4244.86 --> 4245.08]  Yay.
[4245.18 --> 4245.82]  Point fingers.
[4245.82 --> 4246.82]  Point fingers.
[4247.94 --> 4248.72]  Go on, let's sing.
[4248.90 --> 4249.82]  All right, here she comes.
[4250.76 --> 4253.58]  I think she raised her hand first, but if not, she just got ball and cold.
[4254.10 --> 4254.70]  Yeah, you did.
[4254.90 --> 4255.70]  Ooh, ball and cold.
[4255.88 --> 4256.30]  I like that.
[4256.38 --> 4256.64]  Welcome.
[4257.36 --> 4257.76]  Hello.
[4257.76 --> 4258.16]  Hi.
[4258.40 --> 4258.90]  What's your name?
[4259.32 --> 4260.10]  Uh, Janay Sick.
[4261.26 --> 4261.66]  Janay.
[4261.88 --> 4262.76]  Nice to meet you, Janay.
[4262.76 --> 4263.30]  Nice to meet you.
[4263.34 --> 4264.72]  Thanks for coming up on stage with us.
[4264.98 --> 4265.94]  What would you like to talk about?
[4266.16 --> 4271.40]  I wanted to answer Vanessa's question about whiteboarding, alternatives to whiteboarding.
[4271.58 --> 4271.76]  Yay.
[4271.76 --> 4272.28]  Okay, awesome.
[4272.28 --> 4273.86]  What other companies are doing.
[4273.96 --> 4274.12]  Yeah.
[4274.12 --> 4278.28]  So, um, I guess briefly, my background is graphic design.
[4278.40 --> 4279.64]  I went to school for design.
[4280.06 --> 4284.32]  So, there are a lot of people I know who are making that jump from design into development.
[4284.46 --> 4285.44]  It's kind of natural, right?
[4285.52 --> 4286.76]  You're like, you're already on the computer.
[4287.02 --> 4287.78]  Tangential space.
[4287.78 --> 4288.22]  Exactly.
[4288.34 --> 4290.86]  People are going to ask you to do a little HTML here and there, and the next thing you
[4290.86 --> 4292.36]  know, you're like full-on development.
[4292.36 --> 4292.52]  Reactive.
[4292.52 --> 4292.88]  Yes.
[4293.26 --> 4293.40]  Yes.
[4293.40 --> 4293.54]  Yep.
[4294.50 --> 4300.00]  Um, so I actually, I took a career break, and I came back and found out, like, everything
[4300.00 --> 4303.64]  changed and had to, like, quickly get up to speed on how to code.
[4303.64 --> 4308.84]  Um, and I ended up, uh, doing a lot of job hunting.
[4309.48 --> 4315.66]  Um, and one of the places that I interviewed at was Red Ventures, and they had a booth here
[4315.66 --> 4316.96]  at ATO last year.
[4317.22 --> 4322.82]  And, um, I met a guy who was, like, who remembered my name, and when they came up for, um, looking
[4322.82 --> 4328.16]  for someone to hire, they, um, reached out to me and said, you know, we really liked you.
[4328.36 --> 4332.28]  We don't really have a role in particular, but we'd like to talk with you.
[4332.94 --> 4340.06]  So, um, they brought me in to, um, do, like, a, one of those, like, meet 10 people for six
[4340.06 --> 4340.42]  hours.
[4340.52 --> 4344.68]  Like, it was one of those big interviews, but I didn't, I did have to do whiteboarding,
[4344.90 --> 4351.56]  but I sat, um, on a panel for, um, a couple hours, and they just asked, like, explain what
[4351.56 --> 4355.50]  are you good at, and, like, why are you here, and, like, you know, and just really try to
[4355.50 --> 4360.16]  get an understanding of where my strengths are and, um, my interests, and then they were
[4360.16 --> 4365.98]  able to kind of, like, manipulate the, the interview to see exactly how I would fit in.
[4366.14 --> 4368.22]  So I did do a, a whiteboard.
[4368.34 --> 4372.46]  I really sucked at it, but they were, like, we were, we do, like, we don't expect you to
[4372.46 --> 4372.88]  be good.
[4373.00 --> 4376.40]  Like, we, we know you're going to be sweat, and we just want to, like, hear how you think,
[4376.44 --> 4380.10]  and you did well, even though you feel like you did poorly.
[4380.42 --> 4380.64]  Yeah.
[4380.64 --> 4386.34]  Um, so they were very interested, and I did end up passing on that opportunity, you know,
[4386.34 --> 4391.82]  recently, um, I got employed at another company called MedThink, and then I did another career
[4391.82 --> 4394.38]  jump, um, so I'll be starting at IBM.
[4394.66 --> 4394.94]  Yeah.
[4394.94 --> 4395.00]  Yeah.
[4395.80 --> 4396.08]  Congrats.
[4396.32 --> 4396.76]  Congratulations.
[4396.76 --> 4398.30]  Yeah, it's been a long journey.
[4398.30 --> 4400.28]  What, do you know what team, or, like, what area you're going to be?
[4400.28 --> 4401.94]  Um, under the cognitive applications.
[4402.26 --> 4402.38]  Cool.
[4402.38 --> 4406.58]  It's the larger department, and then, um, I'll be doing, uh, front-end development for them.
[4406.66 --> 4406.98]  Awesome.
[4407.24 --> 4408.82]  So, um, they had.
[4408.82 --> 4409.76]  What did you think of that interview from?
[4409.76 --> 4410.54]  It was so cool.
[4410.54 --> 4411.52]  It was very cool.
[4411.52 --> 4415.84]  And it was, um, at first I thought, I'd applied a couple times before and failed, and I was
[4415.84 --> 4417.02]  like, I'm not going to do this again.
[4417.14 --> 4418.44]  I'm just so tired, you know.
[4418.58 --> 4423.46]  Um, but a recruiter found me on LinkedIn, and, um, it was a take-home application.
[4423.86 --> 4429.56]  So, what was cool is that they didn't have a particular, um, goal.
[4429.56 --> 4435.30]  They basically gave you a very open-ended task, and they wanted to see how you thought all the
[4435.30 --> 4439.32]  way from the wireframe, UX, UI strategy into development.
[4439.32 --> 4440.32]  Mm-hmm.
[4440.32 --> 4443.46]  So, I ended up, like, to me, it felt like a fun personal pet project.
[4443.46 --> 4446.06]  So, I already went in not having that pressure.
[4446.06 --> 4446.16]  Right.
[4446.16 --> 4446.26]  Right.
[4446.26 --> 4449.60]  And, um, I just went to town on it.
[4449.60 --> 4449.70]  Yeah.
[4449.70 --> 4455.04]  Like, I threw in all my XD skills, and my wireframing, and UX, and then into my front-end development,
[4455.04 --> 4459.72]  and then even tried to do a little back-end with some Express, which, you know, it was
[4459.72 --> 4462.00]  kind of, I was afraid I wasn't going to get it.
[4462.28 --> 4469.60]  But, um, when I had the chance to come in and, um, just tell the team, because you have
[4469.60 --> 4473.82]  to sit with two or three developers, I got to explain, like, my whole process, and what
[4473.82 --> 4478.26]  I was thinking, and why I did it, and just go through all the things that I was really
[4478.26 --> 4480.92]  strong about, like, all the things that I was pretty good in.
[4480.92 --> 4487.06]  Um, and then, I think they also kind of stepped back and thought, okay, you know, like, she's
[4487.06 --> 4488.90]  pretty good with this, but probably not as strong as here.
[4488.90 --> 4490.80]  But I didn't feel that pressure.
[4491.20 --> 4493.74]  No binary tree searches, because I have gone through that.
[4493.82 --> 4494.92]  That was ridiculous.
[4495.30 --> 4495.82]  It would be not true.
[4495.88 --> 4497.78]  I, I'm a designer first, right?
[4497.84 --> 4500.00]  And then developer, so I can draw you a tree.
[4500.38 --> 4501.62]  But I'm not going to code.
[4501.92 --> 4505.34]  So, I feel like one of the things that you're highlighting here is, like, this is, this should
[4505.34 --> 4509.86]  not be, like, if you're looking at your hiring process as an employer, like, this should
[4509.86 --> 4511.12]  not be a judging process.
[4511.32 --> 4512.40]  This is dating, right?
[4512.42 --> 4513.36]  I don't go on a date.
[4513.48 --> 4517.90]  I mean, I haven't been on a date in 20 years, but I don't go on a date and be like, all right,
[4518.38 --> 4521.82]  you're a seven out of ten on this, and a nine out of ten on that, right?
[4521.88 --> 4523.38]  Like, it's looking for compatibility.
[4523.74 --> 4528.12]  It's looking for, like, are you the type of person that I want to work with, and is this,
[4528.28 --> 4529.68]  are you going to fit well in our team?
[4529.86 --> 4530.04]  Right.
[4530.14 --> 4532.96]  And I think that's the, that's probably how you can retain talent.
[4532.96 --> 4538.36]  Because if I'm coming in knowing, like, I'm going to be looked on, like, they're expecting
[4538.36 --> 4543.42]  me to do well at what I'm doing well already, then, you know, you're, you're just going to
[4543.42 --> 4545.68]  start from a point where you're going to excel.
[4546.02 --> 4547.18]  So, that's how I feel.
[4547.60 --> 4548.20]  Pretty exciting.
[4549.52 --> 4549.76]  Aw.
[4551.20 --> 4551.88]  13 seconds.
[4551.92 --> 4552.70]  Do you want to give a shout out?
[4553.16 --> 4554.46]  To anyone you like.
[4554.86 --> 4556.64]  My son, I'm going to do a talk tomorrow.
[4556.82 --> 4557.54]  He's going to be here.
[4557.62 --> 4558.10]  He's three.
[4558.50 --> 4561.56]  And we're going to do a talk about bringing minority children into STEM.
[4561.56 --> 4562.52]  I love that.
[4562.72 --> 4562.88]  Awesome.
[4563.06 --> 4563.88]  When and where is that talk?
[4563.90 --> 4565.08]  Everyone go watch your talk tomorrow.
[4565.44 --> 4565.60]  Yeah.
[4565.66 --> 4567.44]  It's 2.05.
[4567.88 --> 4570.06]  2.05 at 11.45 a.m.
[4570.12 --> 4570.48]  Okay.
[4570.92 --> 4571.74]  You heard it here.
[4571.90 --> 4572.44]  He is such a funny.
[4572.64 --> 4572.82]  Yeah.
[4573.42 --> 4574.42]  Thank you so much.
[4578.10 --> 4578.50]  Okay.
[4578.76 --> 4580.40]  That is our time.
[4580.76 --> 4585.54]  That being said, if you have a lightning chat you would like to perform, or is it a performance?
[4585.70 --> 4585.94]  I don't know.
[4585.96 --> 4590.94]  If you'd like to chat with us, we will be down in the main floor, booth 72.
[4592.36 --> 4593.74]  We're mic'd up.
[4593.82 --> 4595.44]  We're ready to continue these conversations.
[4595.64 --> 4597.90]  We'll get the timer going and everything.
[4598.42 --> 4600.90]  Any final words from my esteemed colleagues up here?
[4601.34 --> 4604.50]  I just want to say thank you to everyone that came up here and put themselves on the spot.
[4604.66 --> 4607.46]  I think that sparked some really interesting conversations.
[4609.10 --> 4609.40]  K-Ball?
[4609.70 --> 4610.36]  Y'all rock.
[4610.52 --> 4611.44]  But I want more dancing.
[4612.04 --> 4612.76]  Y'all rock.
[4613.02 --> 4613.60]  Next time.
[4613.66 --> 4614.42]  But more dancing.
[4614.54 --> 4614.76]  Okay.
[4614.84 --> 4615.52]  That's our show.
[4615.60 --> 4616.42]  That's JS Party.
[4616.42 --> 4617.98]  Thanks for joining us.
[4618.26 --> 4620.44]  And yeah, we'll see you next week.
[4620.60 --> 4622.20]  That's weird though.
[4622.40 --> 4623.42]  We'll see you next time.
[4623.42 --> 4623.82]  Thank you.
[4623.82 --> 4624.14]  Thank you.
[4624.14 --> 4624.64]  Thank you.
[4624.64 --> 4625.24]  Thank you.
[4625.24 --> 4625.48]  Thank you.
[4625.48 --> 4625.54]  Thank you.
[4625.54 --> 4630.30]  All right.
[4630.38 --> 4632.20]  Thank you for tuning in to JS Party this week.
[4632.32 --> 4635.26]  Tune in live on Thursdays at 1 p.m.
[4635.32 --> 4638.36]  U.S. Eastern at changelog.com slash live.
[4638.66 --> 4641.36]  Join the community and Slack with us in real time during the shows.
[4641.64 --> 4643.18]  Head to changelog.com slash community.
[4643.68 --> 4644.44]  And do us a favor.
[4644.58 --> 4645.76]  Share this show with a friend.
[4646.06 --> 4647.26]  We're just going to have a podcast.
[4647.46 --> 4649.04]  Go into Overcast and favorite it.
[4649.34 --> 4651.78]  And thank you to Fastly, our bandwidth partner.
[4652.12 --> 4653.64]  Head to fastly.com to learn more.
[4653.64 --> 4656.66]  And we move fast to fix things around here at changelog because of Rollbar.
[4656.84 --> 4658.58]  Check them out at rollbar.com.
[4658.84 --> 4660.90]  We're hosted on Leno cloud servers.
[4661.26 --> 4662.88]  Head to leno.com slash changelog.
[4662.94 --> 4664.32]  Check them out and support this show.
[4664.74 --> 4666.76]  Our music is produced by Breakmaster Cylinder.
[4667.14 --> 4670.22]  And you can find more shows just like this at changelog.com.
[4670.36 --> 4671.32]  Thanks for tuning in.
[4671.58 --> 4672.34]  We'll see you next week.
