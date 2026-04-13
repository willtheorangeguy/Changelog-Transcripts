[0.00 --> 21.32]  Welcome to Changelog and friends, a weekly talk show about modular EV trucks.
[21.78 --> 28.24]  Big thanks to our partners at Fly.io, the public cloud, built for developers who ship.
[28.24 --> 33.04]  Try Fly like we did, and you may find yourself deploying all your apps there like we do.
[33.20 --> 33.98]  Fly to I.O.
[34.56 --> 36.18]  Okay, let's talk.
[41.68 --> 46.84]  Well, friends, I'm here with Terrence Lee talking about what's coming for the next generation of Heroku.
[47.14 --> 48.86]  They're calling this next gen Fur.
[49.16 --> 55.64]  Terrence, one of the biggest moves for Fur in this next generation of Heroku, it's being built on open standards and cloud native.
[55.74 --> 57.72]  What can you share about this journey?
[57.72 --> 62.62]  If you look at the last half a decade or so, like there's been a lot that's changed in the industry.
[62.88 --> 73.52]  A lot of the 12 factorisms that have been popularized and are well accepted, even outside the Ruby community, are things that are, I think, table stakes for building modern applications, right?
[73.62 --> 82.10]  And so being able to take all those things from kind of 10, 14 years ago, being able to revisit and be like, okay, we helped popularize a lot of these things.
[82.10 --> 84.66]  We now don't need to be our own island of this stuff.
[84.86 --> 87.22]  And it's just better to be part of the broader ecosystem.
[87.66 --> 91.62]  Like you said, since Heroku's existence, there's been people who've been trying to rebuild Heroku.
[91.78 --> 95.32]  I feel like there's a good Kelsey quote, where are we going to stop trying to rebuild Heroku?
[95.32 --> 102.16]  It's like people keep trying to build their own version of Heroku internally at their own company, let alone the public offerings out there.
[102.28 --> 105.50]  I mean, I feel like Heroku's been the gold standard.
[105.98 --> 117.50]  Yeah, I mean, I think it's the gold standard because there's a thing that Heroku's hit this piece of magic around developer experience, but giving you enough flexibility and power to do what you need to do.
[117.50 --> 123.36]  Okay, so part of Fur and this next generation of Heroku is adding support for .NET.
[123.76 --> 125.00]  What can you share about that?
[125.10 --> 126.96]  Why .NET and why now?
[127.24 --> 130.58]  I think if you look at .NET over the last decade, it's changed a lot.
[130.82 --> 133.40]  .NET is known for being this Windows-only platform.
[133.58 --> 137.60]  You have WinForms, use it to build Windows stuff, double IS.
[138.36 --> 141.42]  And it's moved well beyond that over the last decade.
[141.60 --> 144.26]  You can build .NET on Linux, on Mac.
[144.26 --> 151.04]  There's this whole cross-platform open-source ecosystem, and it's become this juggernaut of an ecosystem around it.
[151.10 --> 155.32]  And we've gotten this ask to support .NET for a long time, and it isn't a new ask.
[155.66 --> 161.12]  And regardless of our support of it, people have been running .NET on Heroku in production today.
[161.36 --> 171.80]  There's been a mono-billpack since the early days when you couldn't run .NET on Linux, and now with .NET Core, the fact that it's cross-platform, this .NET Core billpack that people are using to run their apps on Heroku.
[171.80 --> 175.56]  The kind of shift now is to take it from that to a first-class citizen.
[175.88 --> 178.62]  And so what that means for Heroku is we have this languages team.
[179.02 --> 183.68]  We're now staffing someone to basically live, breathe, and eat being a .NET person, right?
[183.74 --> 193.18]  Someone from the community that we've plucked to be this person to provide that day zero support for the language and runtimes that you expect, and like we have for all of our languages, right?
[193.18 --> 204.14]  To answer your support and deal with all those things when you open support tickets on Heroku, and kind of all the documentation that you expect for having quality language support in the platform.
[204.14 --> 216.50]  In addition to that, one of the things that it means to be first class is that when we are building out new features and things, it is now one of the languages as part of this ecosystem that we're going to test and make sure runs smoothly, right?
[216.50 --> 218.26]  So you can get this kind of N10 experience.
[218.68 --> 219.74]  You can go to DevCenter.
[220.14 --> 222.92]  There's a .NET icon to find all the .NET documentation.
[223.50 --> 227.84]  Take your app, create a new Heroku app, run Git Push Heroku Main, and you're off to the races.
[227.84 --> 242.74]  So with the coming release of Fur and this next generation of Heroku, .NET is officially a first class language on the platform, dedicated support, dedicated documentation, all the things.
[242.98 --> 249.88]  If you haven't yet, go to Heroku.com slash changelog podcast and get excited about what's to come for Heroku.
[250.18 --> 254.24]  Once again, Heroku.com slash changelog podcast.
[257.84 --> 262.34]  So Zeno Rocha is back on the show.
[262.42 --> 262.94]  Welcome, Zeno.
[263.34 --> 263.74]  Yeah.
[264.02 --> 264.78]  Hey, Adam.
[264.92 --> 265.48]  Hey, Jared.
[265.74 --> 267.02]  Super happy to be here.
[267.40 --> 272.84]  I told the team that was going to chat with you two today, they were like, oh my gosh, the changelog, folks.
[272.86 --> 274.84]  It's our favorite podcast.
[275.70 --> 277.02]  That's our favorite thing to hear.
[277.56 --> 278.50]  It's been a bit, man.
[278.52 --> 279.02]  How you been?
[280.26 --> 282.02]  Yeah, it's been wild.
[282.02 --> 282.82]  How long has it been?
[283.82 --> 284.50]  A year?
[285.38 --> 286.48]  A year, year and a half.
[287.08 --> 287.48]  Yeah.
[287.84 --> 288.78]  I think so.
[289.64 --> 290.76]  That's too long, man.
[291.54 --> 292.04]  What a shame.
[292.34 --> 292.60]  Yeah.
[293.04 --> 295.72]  The last time, though, I want to say like, okay, so this is Friends.
[295.88 --> 296.92]  We're not interviewing Zeno.
[297.10 --> 298.34]  We're just digging into some details.
[298.48 --> 299.68]  But the last time, I want to go deep.
[300.54 --> 301.94]  We went to Getting to Resend.
[302.04 --> 302.82]  That was the last time on the show.
[302.82 --> 303.06]  That's right.
[303.18 --> 303.32]  Getting to Resend.
[303.32 --> 304.12]  We went through all the history.
[305.08 --> 306.06]  Getting to Resend.
[306.12 --> 308.92]  So if you want to know that journey for Zeno, check that podcast out.
[311.08 --> 314.16]  Sadly, that was before we were video first on YouTube and stuff.
[314.26 --> 316.14]  So you won't see his face, but today you will.
[316.14 --> 316.18]  Yeah.
[316.66 --> 317.46]  That is a shame.
[317.56 --> 318.44]  Because look at that face.
[318.98 --> 319.72]  Look at that face.
[319.84 --> 321.42]  You got to have that face in there.
[321.50 --> 322.32]  I don't got to have it.
[322.50 --> 325.04]  I've been seeing your face a lot on LinkedIn lately.
[325.18 --> 327.96]  Are you like a LinkedIn guy now?
[328.04 --> 329.54]  Or are you just on all the platforms?
[330.28 --> 331.54]  You know what's crazy?
[331.54 --> 333.64]  I'm definitely not on LinkedIn.
[334.16 --> 336.34]  What I do is I'm on X.
[336.42 --> 336.98]  I'm on Twitter.
[337.72 --> 339.58]  That's my home.
[340.26 --> 342.50]  And then I just repost stuff on LinkedIn.
[342.84 --> 345.12]  But somehow the algorithm is...
[345.12 --> 346.00]  I've been hearing that a lot.
[346.10 --> 346.84]  Like, oh, you're...
[346.84 --> 348.20]  I see you all the time on LinkedIn.
[348.30 --> 349.86]  I'm like, it's not my fault.
[349.98 --> 351.32]  I'm just reposting stuff.
[351.62 --> 352.44]  Like, it's not my fault.
[352.96 --> 354.12]  Well, you should be happy about it.
[354.28 --> 354.98]  It's a good thing.
[354.98 --> 357.74]  I swear every time I log in, I see a new post from you.
[357.82 --> 360.24]  And then I realize, no, this was three weeks ago.
[360.38 --> 365.02]  Because LinkedIn didn't care at all about recency, which is strange to me.
[365.98 --> 366.96]  But they care about Zeno.
[367.10 --> 368.86]  They're like, is there like a special trigger in there?
[368.90 --> 369.78]  Is this a Zeno post?
[369.82 --> 371.76]  Because we're going to put it back at the top of your feed.
[372.90 --> 376.12]  Yeah, I wonder if it's because you use a mixture of mixed media.
[376.24 --> 378.04]  Like, I've seen videos of you all in there.
[378.08 --> 382.98]  I've seen, you know, obviously your marketing images you attach to announcements and stuff,
[382.98 --> 385.04]  which I think is, you know, just super well done.
[385.18 --> 387.88]  Are you the originating designer of Resyn?
[387.94 --> 388.72]  I feel like you are.
[389.14 --> 398.76]  Man, I would never in a million years introduce myself as a designer because I'm an engineer
[398.76 --> 400.16]  that loves design.
[400.46 --> 402.44]  I feel like that's the best way of putting it.
[402.68 --> 402.86]  Oh my gosh.
[403.40 --> 404.86]  My sister's a designer.
[405.14 --> 405.42]  Imposter syndrome.
[406.14 --> 407.24]  Yeah, I think so.
[407.50 --> 410.16]  Dude, you designed the Dracula theme and the website, right?
[410.96 --> 412.18]  True, but still.
[412.18 --> 415.70]  Man, no, designers.
[416.02 --> 419.94]  You have more design skills in your right pinky than I have in my entire body.
[420.72 --> 421.32]  No way.
[421.92 --> 422.38]  No way.
[423.88 --> 424.32]  No way.
[424.48 --> 428.60]  Well, I've been following Resyn since the beginning, and I feel like the design started,
[428.98 --> 431.48]  obviously, your original co-founder or founder.
[431.48 --> 436.40]  So I think I've always seen you as the designer for your things.
[436.40 --> 442.66]  And then I just assumed that you established the foundation, let's just say, of the design
[442.66 --> 444.14]  process for Resyn.
[444.22 --> 445.98]  So it looks a lot like your stuff, in my opinion.
[445.98 --> 446.42]  Yeah.
[446.42 --> 446.74]  Yeah.
[446.88 --> 451.60]  Well, we had a lot of folks helping us, so I can definitely not take the credit.
[451.60 --> 456.90]  But I feel like what we really were trying to do is like, man, there's so many competitors
[456.90 --> 457.56]  out there.
[457.68 --> 460.14]  We're not the first email API in the world.
[460.14 --> 462.02]  So how can we differentiate?
[462.48 --> 466.78]  And branding was the thing that we're like, we got to double down branding.
[467.06 --> 468.70]  Otherwise, yeah.
[468.70 --> 472.94]  Like people need to go to the website and they need to see those cover posts and be
[472.94 --> 473.60]  like, oh, okay.
[473.74 --> 477.98]  That's something that Syngrid wouldn't do, Mayo Gun wouldn't do, and so on.
[477.98 --> 478.28]  Right.
[478.90 --> 481.56]  So the Resyn design is really solid.
[481.84 --> 482.70]  I like it a lot.
[483.10 --> 486.64]  It's definitely of an era or an ilk.
[486.78 --> 491.68]  Like it's very much in the linear kind of the, is it S-Shah DCN?
[491.72 --> 492.06]  I don't know.
[492.16 --> 494.94]  Like the, like whatever that toolkit is.
[494.94 --> 502.50]  I don't know the initials, which produces really polished, really kind of high quality
[502.50 --> 510.34]  black, mostly in dark mode, mostly designs, which have been very popular the last five
[510.34 --> 510.72]  years.
[511.06 --> 515.70]  And I don't keep up with design trends, but I'm starting to, I mean, I keep up with
[515.70 --> 519.52]  them as far as I eventually notice them, but I'm not like at the front end of that.
[519.96 --> 524.22]  But I wonder a company starting today, if you were starting to Resend today, would it
[524.22 --> 529.84]  look like this or is, cause you always tend to be at the very front edge, I think of,
[529.92 --> 537.34]  of trends or would it look more what's new and going on in, in design world that's going
[537.34 --> 538.80]  to be trending maybe next year?
[539.54 --> 539.80]  Yeah.
[540.18 --> 546.22]  I feel like when you're getting started, you should try to lean on the trendy movement
[546.22 --> 551.52]  movement because you want to position yourself as this modern player in the market.
[551.84 --> 554.12]  So following the trend is actually a good thing.
[554.78 --> 558.84]  As you evolve, just like linear, you go to the linear website.
[558.84 --> 564.14]  Now it's way less fancy than it used to be because now you can afford to build more timeless
[564.14 --> 564.76]  design.
[564.76 --> 571.26]  Once you establish yourself, once you establish the brand, which probably, you know, is a step
[571.26 --> 574.34]  that we might take a year or two from now, something like that.
[574.78 --> 577.26]  But you need to show that you're different.
[577.44 --> 581.96]  So for us, it was like, yeah, let's go dark mode first, dark mode only.
[582.68 --> 584.88]  And that's just a different move.
[584.96 --> 591.24]  Let's go with like a WebGL on the hero because, you know, we need to show right away that we're
[591.24 --> 591.62]  different.
[591.62 --> 597.08]  Uh, so those were decisions that we made that were very intentional and the covers on social
[597.08 --> 603.12]  too, because it's like, okay, we know that developers, they appreciate when there's other
[603.12 --> 604.66]  developers ships a lot, right?
[604.70 --> 608.70]  So that's something that when we see other companies doing or other developers doing,
[608.78 --> 610.00]  you're like, wow, this is so great.
[610.02 --> 613.50]  Like they, it's a, they're always moving, always shipping.
[613.50 --> 616.04]  So we wanted to get that feeling of like always shipping.
[616.36 --> 621.60]  So every day we got a post, like that's a part of, uh, like there are days that are
[621.60 --> 622.92]  eight and I don't want to post.
[623.06 --> 626.34]  Uh, but I feel like it's my duty as a founder.
[626.60 --> 632.80]  It's my duty to be investing on my personal brand along with the company brand.
[633.10 --> 638.00]  Uh, and those two need to evolve, uh, in different ways, but they need to exist both.
[638.00 --> 641.30]  Is there anybody breaking that rule?
[641.46 --> 645.38]  Because I, I definitely feel like that's true.
[646.06 --> 652.48]  And yet I imagine there's probably founders out there who never post and just do their
[652.48 --> 654.36]  thing and are still killing it for some reason.
[654.36 --> 657.06]  But it's so hard to get attention nowadays.
[657.06 --> 658.14]  How would you do it?
[658.16 --> 659.58]  And so you have to post, I don't know.
[659.70 --> 663.16]  Is there anybody who just, and this is not necessarily for you, I know, but even Adam,
[663.16 --> 670.62]  like, is there a startup or a scale up that just kills it and doesn't have constant marketing
[670.62 --> 672.26]  and social media stuff going on?
[673.04 --> 675.56]  Or is it pretty much part of the game now?
[676.36 --> 677.68]  I think it's part of the game personally.
[678.32 --> 678.56]  Yeah.
[679.56 --> 679.92]  Yeah.
[679.96 --> 683.74]  It's, it's been my biggest fear for a decade now that eventually everybody will have to
[683.74 --> 685.40]  become some version of a media company.
[686.40 --> 690.16]  Uh, I mean, I was even looking at this, like, uh, as you know, Jared, I've recently gotten
[690.16 --> 696.38]  back into golf, my brother visited and we toured some golf courses and, you know, it's a connection
[696.38 --> 697.06]  point for us.
[697.12 --> 700.12]  I'm trying to improve my game, you know?
[700.62 --> 700.84]  Yeah.
[700.90 --> 706.54]  And I'm just learning that, wow, like TaylorMade and Ping and Titleist and these major brands,
[706.54 --> 708.02]  they are basically media companies.
[708.12 --> 711.22]  Now, if you go on YouTube and you look at this stuff, you just see, you obviously see
[711.22 --> 718.32]  the PGA tour stuff, but you see the brand specific things, even like this thing called
[718.32 --> 723.64]  TrackMan, that it's a hardware slash software product that's used to track your swing and
[723.64 --> 725.12]  ball and speed and stuff like that.
[725.82 --> 731.70]  Like they are a, you know, hardware, software manufacturer for the golf industry.
[732.14 --> 734.78]  And you go to their YouTube, they've got really good content.
[734.84 --> 737.80]  And the reason why they have really good content is because they're focused on creating media
[737.80 --> 739.02]  that pulls people in.
[739.54 --> 743.78]  And I kind of feel like it's funny you ask this question because like literally last night
[743.78 --> 749.02]  I was thinking to myself, there are infinite channels in this world to subscribe to.
[749.46 --> 754.22]  As I said, just got back into golf and I'm just discovering this whole new world of content.
[754.44 --> 757.44]  It's just there waiting for you, you know, tap into the channel.
[758.22 --> 759.44]  Man, that's so true.
[759.56 --> 765.20]  I'm glad you brought that up because I'm thinking about a lot, about that a lot recently.
[765.20 --> 774.44]  Um, I even, uh, I chatted with Gary Tan from YC last Friday because I was like, man, this
[774.44 --> 775.74]  is so top of mind for me.
[775.78 --> 782.38]  And I feel like when he joined YC, he brought up that, you know, uh, he was a solo character
[782.38 --> 787.14]  on his, uh, initialized fund, uh, before he joined YC.
[787.24 --> 790.80]  So he was, he had his YouTube channel, he was doing his thing.
[790.80 --> 797.22]  But then when he joined YC, he could have just doubled down on the PGSA type of content
[797.22 --> 802.06]  because that's a proven content strategy, you know, for the past 20 years.
[802.50 --> 807.00]  But no, they just revamped their whole YouTube thing.
[807.10 --> 812.54]  And now you can definitely tell YC is a media company and you'll see they have multiple shows
[812.54 --> 813.84]  with multiple characters.
[814.48 --> 817.40]  Each character plays a different type of role.
[817.40 --> 820.38]  Michael Sebo is different than Dalton.
[820.80 --> 824.60]  And so it's just, yeah, for me, it's extremely inspiring.
[825.10 --> 832.04]  Uh, and that's a playbook that HubSpot did, Ahrefs, like other companies, maybe outside of
[832.04 --> 836.80]  DevTools, but I can totally see DevTools going down that path too.
[838.18 --> 838.74]  Yeah.
[838.74 --> 838.86]  Yeah.
[839.26 --> 841.00]  It has to be media though.
[841.14 --> 848.64]  Content for not a sales content, content to show off who you are, to tell your story,
[848.70 --> 853.46]  to tell your customer story, to tell the, the bottleneck, the breakage story, the it's
[853.46 --> 854.78]  broken story kind of thing.
[854.84 --> 856.68]  Not this let's buy a thing.
[856.76 --> 857.48]  Here's how it works.
[857.56 --> 858.36]  Only story.
[858.44 --> 865.26]  I feel like that's where, uh, maybe folks will hear us talk about this and go and explore
[865.26 --> 867.72]  and examine themselves and come back and say, Oh, we should do this.
[867.78 --> 869.88]  Let's just sell our stuff on YouTube.
[869.88 --> 871.46]  I think that's not the way to do it.
[871.50 --> 876.76]  I think you need to talk about your world and your, your ecosystem, but not here's how
[876.76 --> 877.44]  you buy our thing.
[877.72 --> 882.40]  There may be a channel for that, but I feel like that's a specific layer of the funnel
[882.40 --> 883.34]  that you address.
[883.34 --> 884.76]  And that's more like sales content.
[884.86 --> 885.26]  Literally.
[885.78 --> 886.84]  Can it live in YouTube?
[887.04 --> 887.26]  Sure.
[887.26 --> 893.44]  But I wouldn't, I wouldn't overly saturate that channel with, you know, two different
[893.44 --> 897.24]  types of content because now you got this, let's capture some people.
[897.24 --> 898.16]  Let's get some attention.
[898.30 --> 904.08]  Let's, uh, you know, kind of distribution to become more exposed to certain folks in
[904.08 --> 904.40]  the world.
[904.74 --> 907.56]  And then you have, you know, Hey, I want to buy your thing.
[907.62 --> 908.52]  Help me buy your thing.
[908.60 --> 911.64]  That's a whole different content slice, but do they belong in the same channel?
[911.66 --> 912.36]  I don't know about that.
[912.82 --> 913.08]  Yeah.
[913.62 --> 917.08]  And it's definitely not about YouTube, right?
[917.08 --> 922.00]  Like what we're talking here is about storytelling and where do you do that?
[922.24 --> 923.18]  Uh, does it matter?
[923.44 --> 929.36]  Uh, like you see all these indie hackers going down that path, building in public, which is
[929.36 --> 929.72]  amazing.
[929.72 --> 930.72]  They should do that.
[931.00 --> 932.34]  They're inspired by levels.
[932.46 --> 933.74]  They're inspired by Mark Liu.
[933.94 --> 934.78]  And it's amazing.
[935.54 --> 941.74]  Um, I guess what people typically fail is like, they just do the, they just show the good
[941.74 --> 942.36]  side of things.
[942.36 --> 942.56]  Right.
[942.56 --> 944.56]  So they are always promoting like, Oh, this is great.
[944.60 --> 945.10]  This is great.
[945.16 --> 945.92]  This is amazing.
[945.92 --> 951.98]  Uh, and if you're never vulnerable, then there's no way I can connect with you on a
[951.98 --> 952.58]  human level.
[952.58 --> 952.86]  Right.
[952.88 --> 954.10]  It's just sales.
[954.68 --> 958.98]  And, you know, that's the, that's the challenge though is like how it, not that I'm not honest
[958.98 --> 966.00]  with the world, but how, how much of the filter do I want to remove from not so much the
[966.00 --> 970.48]  perfectness or the perfectness, uh, casting this perfect vision of who I am or what I
[970.48 --> 973.34]  do or what this business does or somebody else's business does.
[973.34 --> 981.38]  Like it's scary to remove that filter to sort of only post the good stuff and not show the
[981.38 --> 981.86]  bad stuff.
[981.88 --> 986.46]  It's a little scary to do the bad stuff or the, the, the, the challenges, not so much
[986.46 --> 991.28]  like, Oh, we're, we're stuck or sunken or whatever, but more like, here's a, whoa, not
[991.28 --> 992.74]  just here's a high moment.
[993.12 --> 993.60]  Yeah.
[994.04 --> 995.36]  There's a paradox.
[995.58 --> 1002.30]  I forgot the name now, but there's a Wikipedia page on this where you can transform a bad
[1002.30 --> 1004.64]  experience into something that's actually good.
[1004.64 --> 1009.42]  Uh, and that's the, the paradox, like you go for something super bad, like an incident,
[1009.42 --> 1015.10]  but because you do the postmortem, because you're transparent about the issues that caused,
[1015.10 --> 1017.70]  because you, you show like, Hey, here are the next steps.
[1018.02 --> 1019.96]  Then that actually creates more trust.
[1020.54 --> 1025.92]  So something that was bad, a downtime becomes a good thing because of the transparency, because
[1025.92 --> 1028.86]  of the accountability and ownership and all that.
[1029.58 --> 1034.46]  But when you're in the middle of the fire, uh, it's hard to, you know, like,
[1034.64 --> 1036.06]  you want to be vulnerable.
[1036.06 --> 1040.00]  Like, and there, there's a line between like, okay, I can only go so far.
[1040.12 --> 1045.78]  Like if I cross this line, then, um, yeah, it's super tricky, super difficult.
[1046.44 --> 1050.36]  I think that Wikipedia page is called when life gives you lemons, you make lemonade.
[1050.80 --> 1051.32]  Is that right?
[1051.72 --> 1052.46]  That's the page.
[1053.04 --> 1053.80]  Oh my gosh.
[1053.82 --> 1054.60]  Did you see that?
[1054.66 --> 1055.74]  Uh, I don't watch the show.
[1055.80 --> 1058.78]  I think it's from millions or billions.
[1058.88 --> 1059.82]  I don't know what this show is.
[1060.00 --> 1061.12]  I don't even know the actor.
[1061.26 --> 1061.96]  It's gotta be billions.
[1061.96 --> 1063.60]  Cause millions is not impressive anymore.
[1063.76 --> 1064.26]  No, it's not.
[1064.64 --> 1068.30]  But they said that he's like, Hey, when life, well, when life gives you lemons, make lemonade.
[1068.42 --> 1070.46]  He's like, no, when life gives you lemons.
[1071.22 --> 1072.26]  And then he goes on.
[1072.44 --> 1075.58]  First, you roll out a multimedia campaign to convince people.
[1075.70 --> 1078.40]  Lemons are incredibly scarce, which only works.
[1078.40 --> 1082.42]  If you stockpile lemons, control the supply, then I'm a media blitz.
[1083.70 --> 1085.52]  Lemons are the only way to say, I love you.
[1085.56 --> 1089.58]  The must have accessory for engagements or anniversaries.
[1089.80 --> 1090.60]  Roses are out.
[1090.60 --> 1092.48]  Lemons are in.
[1092.48 --> 1096.08]  And billboards that say she won't have sex with you unless you've got lemons.
[1096.08 --> 1097.42]  You cut the beers in on it.
[1098.18 --> 1099.84]  Limited edition lemon bracelets.
[1100.10 --> 1101.90]  Yellow diamonds called lemon drops.
[1102.02 --> 1104.90]  You get Apple to call their new operating system OS Lemon.
[1105.54 --> 1107.20]  Little accent over the O.
[1107.20 --> 1109.38]  You charge 40% more for organic lemons.
[1109.82 --> 1112.08]  50% more for conflict-free lemons.
[1112.18 --> 1114.08]  You pack the capital with lemon lobbyists.
[1114.16 --> 1117.28]  You get a Kardashian to suck a lemon wedge and a leaked sex tape.
[1119.12 --> 1122.20]  Timothee Chalamet wears lemon shoes at Cannes.
[1123.78 --> 1124.98]  Get a hashtag campaign.
[1125.20 --> 1127.88]  Something isn't cool or tight or awesome.
[1128.04 --> 1129.24]  No, it's lemon.
[1129.24 --> 1131.68]  Did you see that movie?
[1131.84 --> 1133.02]  Did you go to that concert?
[1133.10 --> 1134.56]  It was effing lemon.
[1136.02 --> 1137.06]  Billy Eilish.
[1137.34 --> 1137.82]  OMG.
[1138.18 --> 1138.82]  Hashtag.
[1139.52 --> 1139.88]  Lemon.
[1141.44 --> 1147.06]  You get Dr. Oz to recommend four lemons a day and a lemon suppository supplement to get rid of toxins
[1147.06 --> 1150.44]  because there is nothing scarier than toxins.
[1150.76 --> 1151.84]  Then you patent the seeds.
[1151.84 --> 1158.86]  You write a line of genetic code that makes lemons look just a little more like tits.
[1159.32 --> 1162.66]  And you get a gene patent for the tit lemon DNA sequence.
[1163.04 --> 1164.20]  You cross-pollinate.
[1165.28 --> 1167.40]  You get those seeds circulating in the wild.
[1168.04 --> 1173.04]  And then you sue the farmers for copyright infringement when that genetic code shows up on their land.
[1173.82 --> 1174.44]  Sit back.
[1174.94 --> 1175.72]  Rake in the millions.
[1175.72 --> 1183.70]  And then when you're done and you've sold your lempire for a few billion dollars then and only then you make some f***ing lemonade.
[1184.26 --> 1184.52]  Yeah.
[1184.68 --> 1186.28]  Life, lemons, lemonade.
[1186.70 --> 1186.82]  Sure.
[1186.98 --> 1187.18]  Yeah.
[1189.30 --> 1190.78]  So you're selling lemonade.
[1191.18 --> 1194.58]  So Zeno, what are some failures you posted?
[1194.96 --> 1195.64]  Oh boy.
[1196.44 --> 1197.60]  You're willing to talk about.
[1197.78 --> 1204.18]  What are some, you got an incident, you got a fail, bad decision, bad hire, don't name names.
[1204.18 --> 1204.76]  What do you got?
[1205.26 --> 1205.80]  Something vulnerable.
[1206.02 --> 1208.28]  Man, so many of those.
[1208.72 --> 1214.82]  I think the incidents is a good one because, you know, I think we went through some pretty bad stuff.
[1214.98 --> 1217.74]  Like there was one last chance.
[1217.76 --> 1220.64]  So it's been more than a year since we had those two incidents.
[1220.98 --> 1223.64]  But the timing of them were terrible.
[1223.82 --> 1227.80]  Like so there was one incident where it happened right before our launch week.
[1227.80 --> 1232.70]  And then this other incident that happened after we were announcing something else.
[1233.12 --> 1237.82]  And it's so weird because I remember when the incident was happening.
[1238.60 --> 1241.32]  So one of them was related to data being leaked.
[1241.54 --> 1245.88]  So that's like the worst possible type of incident because it's not just a downtime.
[1246.10 --> 1251.02]  It's like you're actually, you know, and it was so hard to navigate those moments.
[1251.02 --> 1252.68]  And I felt like, okay, this is it.
[1252.78 --> 1254.78]  Like there's no way we're going to recover from them.
[1254.78 --> 1254.82]  Yeah.
[1255.08 --> 1256.34]  There's absolutely no way.
[1258.04 --> 1261.60]  But then you're like, okay, this is what I'm doing.
[1261.90 --> 1263.82]  And yeah, like what I'm going to do.
[1263.92 --> 1271.04]  Am I going to hide or just like go with it and trying to make the most out of it and learn it?
[1271.04 --> 1279.88]  So the weird thing about the bad stuff is that when you look back in retrospect, everything is different.
[1280.60 --> 1289.06]  Today, I'm extremely grateful for those things to happen in the very early days of recent because it changed the way I see security.
[1289.06 --> 1296.58]  How often I run pen tests and so many other things like how often we run stuff on the CI.
[1296.78 --> 1298.80]  So we detect stuff before it goes to production.
[1298.80 --> 1301.88]  And I could, you know, say so many things about this.
[1301.98 --> 1308.96]  But yeah, I feel like when bad stuff happens, you always have to try to see the good side.
[1309.82 --> 1313.20]  Otherwise, yeah, you don't recover from it.
[1313.20 --> 1319.42]  I heard it said maybe it was Adam that said this that and maybe an Adam original, maybe not.
[1319.58 --> 1322.78]  But you're it's only a failure if you don't learn anything.
[1322.88 --> 1323.98]  Like if you don't learn.
[1324.18 --> 1324.74]  That's an Adam original.
[1325.22 --> 1326.04]  Is that an Adam original?
[1326.20 --> 1326.82]  I don't know.
[1326.88 --> 1327.44]  It sounds good.
[1327.60 --> 1328.06]  I like it.
[1328.06 --> 1328.66]  Yeah, it sounds like.
[1328.84 --> 1329.00]  Go on.
[1329.18 --> 1330.70]  I'll not say that one.
[1331.00 --> 1331.68]  Say it again fresh.
[1332.08 --> 1334.06]  It's only a failure if you don't learn something.
[1335.54 --> 1336.42]  Yeah, that's an Adam original.
[1336.76 --> 1339.08]  If you learn from your failure, then it's not a failure anymore.
[1339.10 --> 1340.80]  You've actually turned it into lemonade.
[1340.94 --> 1341.16]  Really?
[1341.60 --> 1341.94]  Yeah.
[1341.94 --> 1347.52]  And I mean, the fact that you can be thankful for what was potentially a catastrophic incident
[1347.52 --> 1355.70]  shows that you actually learned and adjusted and are now more resilient than you would have been
[1355.70 --> 1358.44]  had you not had that situation.
[1358.68 --> 1360.06]  So that's all good.
[1360.84 --> 1363.64]  Now, if it actually kills you, then it's not good, right?
[1363.72 --> 1364.94]  Whatever doesn't kill us.
[1366.00 --> 1366.96]  Make you stronger, right?
[1366.96 --> 1367.26]  Make you stronger.
[1367.60 --> 1369.28]  But if it kills us, then it's not.
[1369.58 --> 1370.58]  No, you're not thankful anymore.
[1370.58 --> 1370.82]  Now we're dead.
[1371.26 --> 1371.38]  Yeah.
[1371.38 --> 1371.52]  Yeah.
[1371.94 --> 1373.54]  So many catchphrases, right?
[1374.76 --> 1375.12]  Yeah.
[1375.24 --> 1378.14]  Like, remember Twitter back in 2010?
[1378.48 --> 1381.18]  Like, the blue whale, like, all the time.
[1381.34 --> 1381.58]  Oh, yeah.
[1381.64 --> 1382.12]  The fail whale.
[1382.76 --> 1383.02]  Yeah.
[1383.08 --> 1385.70]  It was so unstable.
[1386.56 --> 1388.74]  Today, we don't even think about it anymore.
[1389.00 --> 1389.24]  You know?
[1389.32 --> 1390.98]  Like, it's just works.
[1393.10 --> 1393.72]  But, yeah.
[1393.72 --> 1394.72]  I think about that a lot.
[1394.72 --> 1395.86]  I think about that a lot.
[1395.98 --> 1398.96]  Like, there was something about the fail whale that it became cultural.
[1399.12 --> 1400.40]  It became like Twitter culture.
[1400.40 --> 1408.18]  And it also produced this, not FOMO, but like, fear because we're all missing out.
[1408.18 --> 1411.68]  Like, you're basically, you're hitting refresh, waiting for the fail whale to go away.
[1411.68 --> 1413.56]  Because, like, you want the site to come back up.
[1413.64 --> 1418.08]  And so it was almost, made you want to use it more, even in a weird way.
[1418.08 --> 1419.92]  Because you're like, oh, it's down, you know?
[1420.86 --> 1421.18]  Yeah.
[1421.40 --> 1428.70]  So that was kind of a weird deal where it kind of produced more demand, which probably was really bad for the engineers that were trying to get it back up again.
[1428.76 --> 1430.24]  Like, stop hitting refresh, guys.
[1431.22 --> 1431.62]  Yeah.
[1431.92 --> 1432.62]  For sure.
[1432.62 --> 1438.66]  As far as the addiction factor, I think it probably helped us all get addicted to it back in the early days.
[1439.22 --> 1443.18]  Because sometimes you don't realize the addiction until something gets pulled away from you, you know?
[1443.54 --> 1444.06]  Oh, yeah.
[1444.44 --> 1444.80]  Oh, yeah.
[1444.82 --> 1445.82]  That's so true.
[1446.48 --> 1448.72]  Well, friends, it's all about faster builds.
[1448.98 --> 1453.46]  Teams with faster builds ship faster and win over the competition.
[1453.88 --> 1454.68]  It's just science.
[1455.08 --> 1458.58]  And I'm here with Kyle Galbraith, co-founder and CEO of Depot.
[1458.58 --> 1464.74]  Okay, so Kyle, based on the premise that most teams want faster builds, that's probably a truth.
[1464.88 --> 1469.58]  If they're using CI providers with their stock configuration or GitHub actions, are they wrong?
[1469.74 --> 1471.56]  Are they not getting the fastest builds possible?
[1472.02 --> 1477.86]  I would take it a step further and say if you're using any CI provider with just the basic things that they give you,
[1477.98 --> 1485.80]  which is if you think about a CI provider, it is, in essence, a lowest common denominator generic VM.
[1485.80 --> 1491.38]  And then you're left to your own devices to essentially configure that VM and configure your build pipeline.
[1491.68 --> 1498.42]  Effectively pushing down to you, the developer, the responsibility of optimizing and making those builds fast.
[1498.76 --> 1503.40]  Making them fast, making them secure, making them cost effective, like all pushed down to you.
[1503.40 --> 1517.12]  The problem with modern day CI providers is there's still a set of features and a set of capabilities that a CI provider could give a developer that makes their builds more performant out of the box,
[1517.32 --> 1522.48]  makes their builds more cost effective out of the box and more secure out of the box.
[1522.48 --> 1530.56]  I think a lot of folks adopt GitHub actions for its ease of implementation and being close to where their source code already lives inside of GitHub.
[1531.12 --> 1535.40]  And they do care about build performance and they do put in the work to optimize those builds.
[1535.58 --> 1539.80]  But fundamentally, CI providers today don't prioritize performance.
[1540.04 --> 1543.94]  Performance is not a top level entity inside of generic CI providers.
[1543.94 --> 1544.62]  Yes.
[1545.06 --> 1545.86]  Okay, friends.
[1546.16 --> 1546.80]  Save your time.
[1546.94 --> 1556.00]  Get faster builds with Depot, Docker builds, faster GitHub action runners, and distributed remote caching for Bazel, Go, Gradle, Turbo Repo, and more.
[1556.46 --> 1562.68]  Depot is on a mission to give you back your dev time and help you get faster build times with a one-line code change.
[1563.00 --> 1564.66]  Learn more at depot.dev.
[1564.78 --> 1566.48]  Get started with a seven-day free trial.
[1566.90 --> 1568.36]  No credit card required.
[1568.52 --> 1570.92]  Again, depot.dev.
[1570.92 --> 1576.28]  Who here is addicted to their phone?
[1577.62 --> 1578.10]  Probably.
[1579.50 --> 1580.76]  Don't want to admit it.
[1581.80 --> 1582.84]  I'm happy to admit it.
[1582.90 --> 1592.98]  I mean, I'm not happy to admit it, but I'm happy to admit that at least I'm aware because if I don't have this black mirror near me, I'm like, can I do life?
[1592.98 --> 1599.66]  And I think it's just because it's become this tool that I use in so many ways.
[1599.80 --> 1599.86]  Right.
[1599.86 --> 1608.84]  It's a necessary thing to navigate my daily life, but it's also my boredom, you know, antidote, so to speak.
[1608.84 --> 1608.86]  Right.
[1608.94 --> 1609.26]  You know?
[1609.70 --> 1617.56]  And so there's a fine line between utility tool and, you know, the other thing, which is not a good thing.
[1618.08 --> 1618.30]  Right.
[1618.30 --> 1621.54]  And that's why it's such a mixed bag is because it's both.
[1621.68 --> 1622.98]  I mean, some things are tools.
[1623.12 --> 1624.16]  Other things are entertainment.
[1625.20 --> 1628.40]  But your phone is like a thousand and one things.
[1628.40 --> 1636.04]  And so, yeah, I've left it at home and had to stop and think like, am I turning around the car or am I just going, you know?
[1636.04 --> 1637.38]  How do I get there?
[1637.38 --> 1639.30]  And that's what I can live without the entertainment part.
[1639.60 --> 1643.90]  But then you're like, yeah, but what if somebody has to get a hold?
[1643.92 --> 1645.16]  I mean, it's always that, right?
[1645.30 --> 1645.44]  Yeah.
[1645.82 --> 1647.46]  What if somebody has to get a hold of me?
[1647.48 --> 1650.10]  And it's like, they probably don't.
[1650.44 --> 1651.76]  And they'll find a way.
[1652.20 --> 1653.78]  And that's the one time they will, though.
[1654.10 --> 1654.46]  I know.
[1654.54 --> 1659.56]  But you know that people lived, you know, hundreds of centuries without these things and life continued.
[1659.56 --> 1660.00]  Yes.
[1661.68 --> 1665.78]  Like, even in the 90s, when we were kids, pagers.
[1666.86 --> 1667.18]  Yeah.
[1667.34 --> 1667.70]  Maybe.
[1668.04 --> 1668.52]  Coolest.
[1669.14 --> 1670.30]  Well, you had a pager.
[1670.46 --> 1670.98]  The coolest.
[1671.14 --> 1675.36]  Yeah, pagers are awesome because you didn't, they had a plausible deniability built right in, you know?
[1676.14 --> 1679.36]  Because you can page somebody, but that doesn't mean they have a phone to actually call you back.
[1679.48 --> 1682.34]  And so, they always had a reason to be like, sorry, I couldn't find a phone.
[1682.66 --> 1685.02]  And you just can't argue against that.
[1685.20 --> 1688.50]  But life went on.
[1688.58 --> 1689.20]  Life was fine.
[1689.20 --> 1690.10]  Maybe it was even better.
[1691.06 --> 1692.56]  Where did you buy your pager, Jared?
[1692.64 --> 1692.98]  Do you know?
[1693.46 --> 1693.90]  Do you recall?
[1694.48 --> 1695.74]  I didn't, I wasn't cool enough.
[1695.82 --> 1696.54]  I didn't have a pager.
[1696.86 --> 1697.14]  You didn't have a pager?
[1698.10 --> 1700.38]  I had a friend who had a pager, which is even better.
[1701.46 --> 1702.10]  Page Cody.
[1702.46 --> 1704.02]  You know, if you don't have to go hold me, Page Cody.
[1704.24 --> 1705.86]  Now he's like my personal assistant.
[1705.86 --> 1706.16]  Page Cody, Jared.
[1706.62 --> 1706.82]  Yeah.
[1708.88 --> 1711.76]  I was right on the cusp of like flip phones and pagers.
[1711.76 --> 1713.24]  So, pagers were just going out.
[1713.24 --> 1719.36]  And my first personal device was like a little Motorola flip phone.
[1720.86 --> 1723.20]  At probably the age of 15 or 16.
[1723.46 --> 1724.00]  What about you, Zeno?
[1724.56 --> 1726.20]  Yeah, I got the flip phones too.
[1726.94 --> 1727.12]  Yeah.
[1727.38 --> 1727.66]  Yeah.
[1727.66 --> 1733.40]  Man, I can totally relate to that feeling of like, almost like addiction, borderline addiction, right?
[1733.40 --> 1738.52]  Like I remember last year, Twitter was blocked in Brazil.
[1738.52 --> 1743.06]  Like there was like a whole thing between like Elon Musk and the government.
[1743.06 --> 1745.74]  And then they blocked all the internet providers.
[1746.18 --> 1747.62]  So, then I traveled there.
[1747.86 --> 1748.74]  I arrived at the airport.
[1748.88 --> 1752.22]  And I have like a few hours in between flights.
[1752.86 --> 1754.40]  And I noticed this thing.
[1754.58 --> 1757.72]  Like whenever I was going to do a task, I was like doing something.
[1757.82 --> 1761.26]  And then if I had to wait for like three seconds for the thing to finish,
[1761.58 --> 1766.84]  then I would go to the browser and be like, okay, command T, TW enter.
[1766.84 --> 1769.70]  And that was just like a movement I would do.
[1769.90 --> 1772.40]  So, I would always go to Twitter in between tasks.
[1773.22 --> 1778.24]  But because the website was blocked, then I would always get like this page of like, no, it's offline.
[1778.36 --> 1778.82]  It's offline.
[1779.50 --> 1784.18]  To the moment where like I was doing that for like 30 minutes, I'm like, okay, I just need to get into a VPN.
[1784.74 --> 1786.46]  Because I have to go there.
[1786.58 --> 1789.44]  Like it's just so, so addicting.
[1789.66 --> 1790.28]  It's crazy.
[1791.34 --> 1791.62]  Yeah.
[1791.62 --> 1799.48]  I definitely have the pull to refresh thing like ingrained deep down in there where I'll do it without thinking about it sometimes.
[1799.84 --> 1804.88]  Because I don't let my mail, I don't let my email just come in.
[1805.30 --> 1806.36]  I have to go check it.
[1806.88 --> 1808.64]  Because I don't want to just be pushed.
[1809.04 --> 1810.36]  But at the same time, I check it all the time.
[1810.44 --> 1811.22]  So, it's pretty stupid.
[1811.22 --> 1814.90]  But, you know, I open the mail app and I pull to refresh.
[1815.30 --> 1819.80]  And I'll do that just habitually without even thinking about it, you know.
[1820.18 --> 1822.28]  And that's when you know something's tightly ingrained.
[1823.10 --> 1823.74]  Email, man.
[1823.82 --> 1827.28]  Email is necessary, as you can probably assume.
[1827.94 --> 1828.62]  But is it though?
[1829.60 --> 1830.68]  But is it though?
[1830.96 --> 1832.72]  Do they have to get a hold of me right then?
[1832.80 --> 1833.22]  You know.
[1833.32 --> 1833.62]  You know.
[1834.02 --> 1835.18]  I'm kind of with you on that.
[1835.18 --> 1847.20]  I think it was David Heimer Hansen one time that talked about this around the Hay Launch or somewhere along their storyline discussing this idea.
[1847.44 --> 1847.70]  I think.
[1847.82 --> 1848.60]  I'm not too familiar.
[1848.74 --> 1850.06]  They have like an M box, right?
[1850.12 --> 1851.36]  Where it's like not an N box.
[1851.60 --> 1852.90]  It's an M box.
[1853.30 --> 1853.86]  What's that mean?
[1854.50 --> 1855.44]  I think it's actually IM.
[1855.76 --> 1856.22]  I don't know.
[1856.28 --> 1857.42]  I don't know their terminology.
[1857.64 --> 1858.78]  I'm not going to try and sell the product.
[1858.78 --> 1859.34]  Okay.
[1859.80 --> 1860.10]  Oh, yeah.
[1860.10 --> 1865.14]  The idea was essentially that just because you email me, does that mean I owe you my time?
[1865.18 --> 1866.08]  As a response.
[1866.98 --> 1874.56]  You know, I feel like there's this, you know, just because you can find my email on the internet or maybe even book time on my cow.
[1875.56 --> 1877.02]  You know, because we have links out there.
[1877.10 --> 1878.42]  I'm like, yeah, people do that sometimes.
[1878.48 --> 1879.64]  I'm like, who is this person?
[1879.72 --> 1880.76]  It's like, no, I'm sorry.
[1880.84 --> 1881.76]  That's not how this works.
[1881.94 --> 1882.26]  Right.
[1882.36 --> 1883.36]  You know, you have to be invited.
[1883.58 --> 1885.06]  You can't just get on my calendar.
[1886.16 --> 1887.44]  I think it's the same thing with email.
[1887.44 --> 1892.54]  Just because you emailed me, does that mean I owe you my time to respond to you?
[1892.54 --> 1892.66]  No.
[1893.66 --> 1896.90]  And it's a little pretentious to think that way, I think.
[1897.40 --> 1899.42]  But I think we have to be protectors of our.
[1900.68 --> 1905.56]  I would say probably our most important asset to manage is time.
[1905.82 --> 1907.08]  You can't get it back.
[1907.16 --> 1909.08]  This moment we're sharing now is gone forever.
[1909.84 --> 1913.64]  You know, this is time you cannot rewind and do differently.
[1914.22 --> 1917.36]  And so you dedicate that time to something that you think is important.
[1917.36 --> 1920.60]  Does that mean I have to dedicate it to responding to you because you email me?
[1920.72 --> 1921.32]  I'd say no.
[1921.72 --> 1921.92]  No.
[1922.54 --> 1924.14]  And it's so hard to say no, right?
[1924.62 --> 1924.96]  Yeah.
[1926.08 --> 1929.94]  And I do not reply to every email, but I read almost all of them, you know.
[1931.72 --> 1932.76]  And that upsets me too.
[1932.78 --> 1933.48]  That's an even different question.
[1933.60 --> 1938.52]  Like, do I, do I owe you the time to read your email?
[1940.56 --> 1940.92]  Exactly.
[1941.62 --> 1942.00]  Gosh.
[1942.10 --> 1944.56]  You know, I think it's like the sixth time that you sent it.
[1945.00 --> 1945.94]  Just following up.
[1947.18 --> 1948.20]  Oh my gosh.
[1948.80 --> 1953.48]  And so Adam and I get a lot of the same emails because we share editors at changelog.com.
[1953.82 --> 1954.16]  Oh gosh.
[1954.26 --> 1955.60]  And so many of them are pitches.
[1955.90 --> 1957.42]  And so many of them are so bad.
[1957.94 --> 1958.32]  So bad.
[1958.32 --> 1960.54]  And so many of them follow up without response.
[1960.54 --> 1964.78]  Like we have not said a word, but they'll send four, five, six emails.
[1965.12 --> 1967.12]  Just professional courtesies, they call it.
[1967.12 --> 1971.26]  And so every once in a while, one of us will reply with an all caps unsubscribe.
[1971.64 --> 1979.02]  But one person who neither one of us engaged with at all, finally emailed back for like
[1979.02 --> 1983.22]  the fifth time with no response and accused us of ghosting them.
[1984.70 --> 1987.34]  I was like, you can't ghost somebody you've never talked to.
[1987.62 --> 1990.24]  You know, like, what are you talking about ghosting you?
[1990.50 --> 1992.22]  We've just ignored your emails.
[1992.22 --> 1998.20]  It's like, that's the first for me is like being accused of like mistreatment from somebody
[1998.20 --> 2004.02]  I've never met and has only stolen like, you know, 30 seconds of my time, five times.
[2005.16 --> 2005.94]  That's I don't know.
[2006.00 --> 2006.78]  We're talking about it now though.
[2006.80 --> 2007.60]  Can I read it verbatim?
[2007.66 --> 2008.24]  I have it pulled up.
[2008.24 --> 2009.28]  I'm turning it into lemonade.
[2009.46 --> 2011.02]  You see, I've created content out of this.
[2011.26 --> 2011.80]  Yeah, you are.
[2012.06 --> 2013.92]  And now I'm, ha ha, I win.
[2014.30 --> 2015.66]  Can I read this email verbatim?
[2015.74 --> 2016.62]  Just for context?
[2016.92 --> 2017.02]  Sure.
[2017.52 --> 2019.72]  We're going to get our, yes.
[2019.72 --> 2024.12]  It says, Adam and Jared, this week, my last email I send to you.
[2025.50 --> 2026.20]  Come on.
[2026.62 --> 2027.92]  Forgot finally some good news.
[2028.24 --> 2033.10]  Either you ghosted me or you don't want so-and-so on your podcast.
[2033.60 --> 2035.00]  If anything changes, let me know.
[2035.38 --> 2035.58]  Yeah.
[2035.74 --> 2037.12]  I mean, I applaud their efforts.
[2037.18 --> 2037.62]  I really do.
[2037.70 --> 2039.02]  I mean, they're getting creative at least.
[2039.56 --> 2039.84]  Yeah.
[2040.10 --> 2042.82]  But we never ghosted you.
[2043.24 --> 2043.62]  No.
[2044.12 --> 2045.10]  Because we never talked.
[2045.62 --> 2046.34]  That's right.
[2046.34 --> 2052.04]  You've only stolen our time here in this podcast and in our emails five or so times.
[2052.24 --> 2052.90]  Oh, gosh.
[2052.98 --> 2053.60]  And we've never engaged with you.
[2054.62 --> 2059.26]  And just because we create podcasts and invite people on our shows doesn't mean we owe you a response.
[2059.62 --> 2060.08]  That's right.
[2060.24 --> 2062.24]  And then we have a phone number on our website, Zeno.
[2062.74 --> 2063.74]  And they call us.
[2063.92 --> 2065.08]  I got a phone call last feature.
[2065.22 --> 2065.32]  Well, that's your fault.
[2065.32 --> 2066.48]  You put our phone number on our website.
[2067.58 --> 2068.42]  It's been useful.
[2068.66 --> 2071.20]  It's my fault.
[2071.46 --> 2072.04]  It's my fault.
[2072.34 --> 2072.70]  All right.
[2072.70 --> 2075.88]  So we can't complain too much when people call that phone number, you know?
[2076.16 --> 2076.48]  No.
[2076.56 --> 2081.94]  But then they call and they're like, hey, I've emailed a few times about getting so-and-so on your podcast.
[2082.24 --> 2085.04]  Are you guys taking accepting guests?
[2085.92 --> 2088.96]  And I'm like, well, if you've emailed us, we haven't responded.
[2090.16 --> 2093.42]  It's unlikely that either we're to your email or we're interested.
[2093.42 --> 2096.64]  So it's just like, don't call.
[2096.76 --> 2097.20]  Come on.
[2097.94 --> 2099.38]  No, I've definitely cold emailed people.
[2099.50 --> 2101.92]  I'm sure, Zeno, you have as well in our lives.
[2101.92 --> 2113.32]  And sent them an email and asked them for something or to come on our show and tell them why, you know, it'd be a good idea and why we would appreciate it and have gotten no response back.
[2113.98 --> 2120.96]  And maybe a couple of times, maybe like six months later, when they come back across my radar and I'll be like, you know what?
[2120.98 --> 2121.70]  They never replied.
[2121.76 --> 2122.56]  I'll try one more time.
[2123.00 --> 2126.60]  Maybe I'll try another time, especially if I really want them to come on the show.
[2127.38 --> 2128.60]  Guido, Van Rossum.
[2128.70 --> 2129.36]  I mean, come on, man.
[2130.24 --> 2131.06]  Many others.
[2131.06 --> 2131.46]  Yeah.
[2132.82 --> 2134.68]  But I couldn't.
[2134.84 --> 2140.86]  And I appreciate the hustle, but I do not appreciate somebody who's going to send the same person five unanswered emails.
[2141.98 --> 2142.80]  What's your limits?
[2142.88 --> 2143.12]  I know.
[2143.30 --> 2146.22]  How many emails would you send somebody if you don't get a response?
[2147.02 --> 2153.00]  I, as a receiver, my technique is like, I just block the domain.
[2153.00 --> 2169.30]  So if people are like sending me these extremely like automated code emails, like zero contacts, they're offering me a position as a software engineer or something.
[2169.30 --> 2170.42]  I'm like, what the hell?
[2170.42 --> 2171.78]  Like, I'm not interested.
[2171.94 --> 2172.70]  That's not me.
[2173.12 --> 2176.34]  I don't know how you really put me on this list.
[2176.34 --> 2181.70]  And then if you can tell when the follow-ups are automated, right?
[2183.02 --> 2189.20]  Because like one thing is like what you were doing is like, okay, as a human, I really want you on the show.
[2189.34 --> 2196.90]  And then you come in, you're explaining why and all that versus like, you know, you're in a sequence.
[2196.90 --> 2198.32]  Like it's just so clear.
[2198.50 --> 2201.58]  And people have these hooks that get your attention.
[2201.84 --> 2203.34]  Like, oh, you're ghosting me.
[2203.40 --> 2205.08]  And then you're like, no, I don't want to ghost you.
[2205.24 --> 2212.50]  So then you reply because now they, like they trigger something on your psyche that that makes you want to reply.
[2212.60 --> 2214.58]  Or there's the subject line that they use, right?
[2215.08 --> 2216.18]  To get your attention.
[2216.66 --> 2218.60]  I've seen all sorts of crazy things.
[2218.60 --> 2222.58]  Like people sending emails with typos on purpose.
[2222.58 --> 2226.98]  And then they send a follow-up email suddenly like, oh, I fixed that.
[2228.12 --> 2229.62]  But then they get your attention.
[2229.86 --> 2234.90]  That's actually hilarious because, so I just had Kendall Miller on the show a couple weeks ago.
[2235.08 --> 2235.48]  That's true.
[2235.66 --> 2239.34]  And he was given some top tips about how to get people's attention.
[2239.44 --> 2240.30]  And one of them was that.
[2240.38 --> 2244.82]  He's like, you can just spell their name wrong on purpose, which shows them that you're a real person.
[2245.12 --> 2249.64]  Like that was his reason why he does it is to just get past that immediate.
[2249.64 --> 2254.78]  Because we all have that Bayesian filter where it's like, this is just spam, you know?
[2255.28 --> 2259.16]  But like a typo is kind of proof that you hand typed it.
[2259.40 --> 2262.66]  And so you're just, and personally, I wouldn't do that.
[2262.80 --> 2263.82]  I'm with you on it.
[2264.38 --> 2266.88]  But it's certainly a technique that people do.
[2267.06 --> 2270.24]  And Kendall seems like he's okay getting that one out there if it's effective.
[2270.54 --> 2277.70]  So we all have our little borders of where we think is, you know, over the line and is kosher.
[2277.70 --> 2287.22]  Let me go on record too and say, well, I want to say like, even though I'm personally and we all are collectively, I would say loosely just like griping about this.
[2287.52 --> 2290.30]  As someone who's an encourager, keep going.
[2290.78 --> 2291.38]  Don't stop.
[2291.64 --> 2292.36]  Do that stuff.
[2292.72 --> 2293.68]  You may upset me.
[2294.08 --> 2298.50]  I may go on a podcast and not name you, but literally verbatim read your email out loud.
[2299.82 --> 2303.52]  I might ghost you.
[2303.84 --> 2304.24]  I'm just saying.
[2304.24 --> 2304.42]  Right.
[2305.26 --> 2306.38]  But still do it, man.
[2306.44 --> 2308.76]  Like push whatever buttons you got to by any means necessary.
[2308.94 --> 2310.66]  Push through those boundaries and find your way.
[2310.92 --> 2311.08]  Right.
[2311.14 --> 2314.72]  But we get to push back, you know, like we get to come on a show and say, this is not cool.
[2315.54 --> 2315.80]  That's right.
[2315.82 --> 2316.82]  And that's just part of life.
[2316.84 --> 2319.00]  Like that's just, that's just how it works.
[2319.48 --> 2325.42]  There's definitely something beautiful about a protocol that you can reach anyone in the world.
[2325.42 --> 2329.84]  And if you know that one, that there's just something beautiful.
[2329.84 --> 2330.18]  Right.
[2330.22 --> 2331.92]  And then you can try your shot.
[2332.00 --> 2335.56]  Like, oh, let me see if I can get a hold of Jeff Bezos.
[2336.00 --> 2336.56]  I don't know.
[2336.80 --> 2343.96]  But I'm sure he has an email and there's an executive assistant that like triages that.
[2343.96 --> 2350.80]  But yeah, like you hear stories of like Tim Cook answering stuff like, like you can always just try your luck.
[2351.32 --> 2353.16]  That is so true.
[2353.38 --> 2365.24]  And it's such a, an equalizing technology where it's like, as long as you can get the email address and craft the email in a proper way.
[2365.24 --> 2373.66]  Like if you can find the magic combination of characters to put into this little box and send it, you can get the attention of anybody in the world.
[2374.22 --> 2374.70]  That is true.
[2374.80 --> 2376.54]  I mean, theoretically, but yeah.
[2376.54 --> 2376.72]  Yeah.
[2377.20 --> 2377.60]  Theoretically.
[2377.72 --> 2378.52]  I mean, it happens.
[2378.68 --> 2382.24]  Although it also doesn't happen, you know, like sometimes they ghost you.
[2383.26 --> 2383.70]  Sometimes.
[2388.56 --> 2389.68]  Oh, that's hilarious.
[2389.92 --> 2393.66]  But yeah, I, I mean, email is probably to this day.
[2394.66 --> 2394.70]  Yeah.
[2395.24 --> 2397.64]  Like top five coolest things in technology, right?
[2397.68 --> 2399.06]  Like the way it works.
[2399.76 --> 2400.16]  Yes.
[2400.22 --> 2407.36]  It hasn't, you know, of course it has its problems that I'm sure, you know, all of them very well as a email sending provider.
[2407.58 --> 2410.58]  You know, a lot of the technical problems, of course, spam is an issue.
[2410.72 --> 2412.00]  I mean, there's so many issues.
[2413.64 --> 2416.04]  But it's not siloed.
[2417.32 --> 2420.02]  It's federated in like old school ways.
[2420.70 --> 2421.54]  It works.
[2422.96 --> 2424.88]  And yeah, you can reach anybody in the world.
[2424.88 --> 2426.38]  Just by having their address.
[2426.78 --> 2428.68]  And theoretically, nobody owns it.
[2428.74 --> 2431.04]  And maybe you can speak to the deliverability aspect.
[2431.16 --> 2434.04]  I think there's some layer of ownership or centralization.
[2434.04 --> 2440.22]  It's like there's a cabal, so to speak, that gate keeps the protocol to some degree.
[2440.22 --> 2442.26]  Google and Microsoft, basically.
[2443.14 --> 2446.88]  You know, like I imagine deliverability is probably the biggest thing.
[2446.94 --> 2449.36]  And like somebody controls deliverability of email.
[2449.42 --> 2456.68]  And if you don't send from a certain IP address or a range of IP addresses, you have less likely the ability to actually utilize the protocol.
[2456.68 --> 2458.08]  You may send it to the ether.
[2458.08 --> 2458.24]  Yeah.
[2458.24 --> 2462.74]  But it won't actually arrive because the system says no, essentially.
[2462.74 --> 2464.66]  Which is that fair, Zeno?
[2464.76 --> 2470.70]  Is it basically Gmail and Outlook or Yahoo?
[2470.96 --> 2480.86]  I mean, there's probably just a few centralized providers who have so many people's emails hosted that if they lock you out for whatever reason, they think that you're a bad actor.
[2480.86 --> 2487.38]  Then you're kind of locked out and you can't hit, you know, a third of email addresses in the world.
[2487.48 --> 2488.66]  I mean, Gmail is so massive.
[2488.86 --> 2493.36]  I'm not sure how big Microsoft's email hosting is, but I'm sure it's just massive.
[2493.94 --> 2495.40]  And I'm sure there's other big players like that.
[2495.42 --> 2496.46]  But those are the two that come to mind.
[2497.20 --> 2498.48]  Yeah, you're absolutely right.
[2499.20 --> 2501.44]  Like Gmail definitely dominates.
[2502.80 --> 2507.62]  And then you have like Yahoo is super popular in Japan, for example, still.
[2507.62 --> 2512.84]  And then Outlook still and Hotmail, like those ones, like for Microsoft.
[2513.38 --> 2513.90]  Hotmail, yeah.
[2514.36 --> 2522.78]  What is cool about them and not cool, too, is like they have to keep improving their game.
[2522.96 --> 2525.34]  Otherwise, their products get obsolete.
[2525.96 --> 2532.30]  And especially now with AI, you can generate like so many different emails and they're highly personalized.
[2532.74 --> 2535.88]  And it gets even more tricky, right?
[2535.88 --> 2542.10]  But I think the beauty is like or the challenge for them is like, OK, how do we evolve?
[2542.34 --> 2545.18]  And in the beginning, you're totally right, Adam.
[2545.30 --> 2547.88]  Like there was a lot of emphasis on the IP level.
[2548.66 --> 2550.08]  So then you would have like an IP.
[2550.54 --> 2556.28]  If the reputation of that IP is good, then just let all those emails go through.
[2556.96 --> 2564.04]  And then email providers came up and they're like, OK, now I have this big IP pool and I just shove people there.
[2564.04 --> 2567.72]  And then the good actors balance the bad actors.
[2568.50 --> 2581.08]  So then these inbox providers, they're like, oh, OK, so now we have to, you know, go up the different abstraction layer and look at the domain more than just the IP.
[2581.94 --> 2583.36]  And they have like different techniques.
[2583.36 --> 2585.76]  Like they look at how fast you send emails.
[2585.98 --> 2590.96]  And that's something that dictates like, are we going to throttle the emails or not?
[2591.28 --> 2595.60]  They look at the engagement early on for like emails that are coming to the inbox.
[2595.74 --> 2599.46]  And based on that, they dictate like the inbox placement.
[2599.58 --> 2603.38]  Are we going to keep it on the primary inbox, the promotional tab, the spam folder?
[2603.38 --> 2608.02]  And those things are constantly evolving.
[2608.50 --> 2618.30]  But what my the thing I don't like is like I wish they would evolve as fast as the web, for example, because I feel like the web was like super slow.
[2618.30 --> 2627.94]  Maybe like the 2000s and then 2010, HTML5 comes in and CSS3 and ECMAScript 6.
[2628.18 --> 2630.10]  And it's like, oh, wow, like there's so much movement.
[2630.46 --> 2639.66]  And now we don't care so much about like how this website looks on Opera versus Firefox versus IE6.
[2639.98 --> 2642.26]  Like it's just like the same website.
[2642.38 --> 2645.60]  Very little things like that are different in Safari than Chrome.
[2645.86 --> 2646.12]  Right.
[2646.12 --> 2651.20]  But with email is still, man, so hard.
[2651.86 --> 2652.72]  Tell me about it.
[2652.76 --> 2663.18]  I'm facing an uphill battle right now because Gmail just decided that they're going to start ignoring our styles in our newsletter with zero changes for me.
[2663.30 --> 2664.56]  Like it's the exact same thing.
[2664.60 --> 2665.68]  It worked fine last week.
[2665.84 --> 2668.14]  I can I can send the same email I sent two weeks ago.
[2668.56 --> 2673.74]  And if I go in my archive, the two weeks ago one looks like it looks like in every other email client.
[2673.74 --> 2679.06]  And if I resend the same exact content today, it looks different.
[2679.06 --> 2683.76]  Specifically, they're ignoring our fonts and our link colors.
[2683.76 --> 2688.92]  The form like the actual form of the email is still there, but it just looks kind of whack.
[2689.80 --> 2690.92]  And there's no announcements.
[2690.92 --> 2691.62]  There's no nothing.
[2691.74 --> 2694.82]  It's just like, you know, they just change the way they handle rendering.
[2694.82 --> 2701.82]  And now I have to go chasing down whatever it is different in order to get my rules to work.
[2702.96 --> 2706.34]  And that just makes me mad, you know, and there's I mean, I can't ignore it.
[2706.40 --> 2706.70]  It's Gmail.
[2707.24 --> 2711.82]  And at least with browsers like, you know, there's an engine behind and that engine is open source.
[2711.82 --> 2716.68]  So you're like, OK, Gecko for Firefox and Blink for Chrome.
[2716.68 --> 2720.66]  And then there's an actual change log publicly available.
[2721.70 --> 2723.00]  But for those right.
[2723.20 --> 2723.38]  Yeah.
[2723.62 --> 2728.96]  Email engines like, no, there's nothing that's like, oh, here's what we change in terms of rendering.
[2729.36 --> 2731.38]  No, like you cannot find it.
[2731.38 --> 2736.82]  I want to pause for a second just and just reflect on the idea that Jared just said resend.
[2736.98 --> 2738.52]  And then you just said change log.
[2738.52 --> 2742.28]  I just think that's kind of cool how both brand names show up in natural conversation.
[2742.48 --> 2742.80]  Wow.
[2742.92 --> 2743.74]  That's just beautiful.
[2744.00 --> 2745.58]  You know, that's good naming by us.
[2745.80 --> 2746.22]  By all of us.
[2746.36 --> 2747.12]  I do like that a lot.
[2747.72 --> 2752.52]  And I had to go sign in, Jared, to Gmail and look at it because like, you're right.
[2752.62 --> 2754.16]  Like it looks fine.
[2754.24 --> 2757.16]  It's not the worst ever, but it's not respecting the styles.
[2757.16 --> 2760.62]  It's respecting the overall framework of how the email looks and stuff.
[2760.82 --> 2761.04]  Yes.
[2761.16 --> 2761.98]  It's all gone.
[2762.46 --> 2763.22]  What's up with that?
[2763.84 --> 2764.36]  They're over.
[2764.48 --> 2765.84]  They're using their own fonts.
[2766.04 --> 2767.02]  It's like they care more.
[2767.02 --> 2768.70]  And Microsoft has done this a while.
[2768.82 --> 2786.98]  Specifically, like if you log into whatever it is, live 365, or if you use like the Microsoft Office in the cloud thing and read the email there, it's also ugly because they want to look like their UI inside their web app.
[2787.78 --> 2790.52]  And so like all the links are blue because that's what Microsoft wants.
[2790.52 --> 2801.40]  Now, if you read that same email, still hosted by Microsoft, but inside of Outlook.app, you know, the .exe.
[2801.56 --> 2802.98]  Sorry, I haven't been on Windows in a while.
[2803.38 --> 2804.68]  Forgot what their extension was.
[2805.08 --> 2805.84]  Outlook.exe.
[2805.90 --> 2806.54]  It'll look fine.
[2806.64 --> 2808.74]  It'll look just like it does everywhere else.
[2808.88 --> 2811.14]  But in the web app specifically, they override things.
[2811.14 --> 2820.90]  And Google, I think, just started doing that as my guess because Gmail just this last couple of weeks now, it's like Roboto Sans or Google Sans.
[2821.02 --> 2821.36]  I don't know.
[2821.46 --> 2822.34]  They're using their own fonts.
[2823.42 --> 2824.90]  I'm surprised this is news to you, Zeno.
[2825.16 --> 2826.52]  Has anybody else told you this?
[2826.92 --> 2827.54]  Oh, he knows this.
[2827.54 --> 2827.92]  No, man.
[2828.92 --> 2830.10]  He knows this.
[2830.84 --> 2831.62]  You don't know this?
[2833.22 --> 2834.08]  I haven't heard this.
[2834.08 --> 2834.88]  I hear that all the time.
[2834.88 --> 2835.10]  You know this.
[2835.10 --> 2837.12]  I hear that all the time.
[2837.90 --> 2841.44]  And then Superhuman does their thing as well.
[2842.00 --> 2842.32]  Right.
[2842.98 --> 2853.54]  And the Gmail mobile app will invert the colors to be like if you're using dark mode on your phone, then there's absolutely no control.
[2853.90 --> 2855.60]  But they will invert everything.
[2855.88 --> 2860.70]  And then you just hope that they will invert right with their inversion algorithm too.
[2860.70 --> 2871.18]  So it's just crazy like how, yeah, you just have to, still feels like super archaic even though he knows around for like 20 plus years, right?
[2871.44 --> 2872.46]  30 plus years.
[2872.58 --> 2877.98]  And I've been talking with my research assistants, ChatGPT, I've asked Grok.
[2878.80 --> 2881.00]  I think those are the only two that I asked this particular question.
[2881.76 --> 2883.24]  What I can do about this.
[2883.50 --> 2884.48]  Is there anything that they know?
[2884.56 --> 2887.04]  And they both have pushed me towards Litmus.
[2887.86 --> 2888.08]  Yep.
[2888.50 --> 2889.96]  Which is a commercial product.
[2889.96 --> 2891.60]  Are you aware of that one?
[2892.00 --> 2892.56]  Do I know Litmus?
[2893.48 --> 2896.02]  They do take the guesswork out of email marketing.
[2897.32 --> 2904.72]  And so what I want is like a way I can like send my preview email into like all of the weirdest places that might be rendered and see how it looks.
[2904.88 --> 2907.10]  And then like somehow open a dev tools kind of thing.
[2907.16 --> 2909.30]  And I think Litmus offers you something like this.
[2910.06 --> 2911.90]  But, you know, I'm just a guy with a newsletter.
[2911.90 --> 2919.80]  I'm not like an enterprise where Litmus is like, come get our suite of tools for 150 bucks a month or whatever it is.
[2920.36 --> 2922.18]  And it doesn't feel like a product for me.
[2922.18 --> 2924.74]  And so that brings me up two thoughts.
[2925.10 --> 2929.50]  A, as a recent guy, like what is there in this world?
[2929.50 --> 2931.06]  Or are you guys trying to solve this problem?
[2931.06 --> 2939.06]  And then B, I think this leads us into our AI SEO because both Grok and ChatGPT push me towards Litmus.
[2939.14 --> 2940.66]  That's great for Litmus, right?
[2940.66 --> 2946.44]  A potential new customer because they were the thing that showed up that these things knew about.
[2946.88 --> 2949.40]  So let's start with the email side.
[2949.94 --> 2957.68]  Like what's out there for people to be able to send a preview email into like all the weird places it might render and look at it.
[2958.48 --> 2958.60]  Yeah.
[2958.96 --> 2962.14]  So yeah, Litmus is definitely the most popular one.
[2962.22 --> 2965.56]  And it's almost like a browser stack kind of product.
[2965.56 --> 2970.76]  Like they run VMs that take screenshots and then you see how it renders.
[2971.48 --> 2973.04]  So that saves you time.
[2973.16 --> 2977.02]  Like you don't need another Windows machine to check how things look on Outlook.
[2977.12 --> 2977.74]  So that's great.
[2978.20 --> 2981.42]  But it's still like, okay, now I see that it's different.
[2981.52 --> 2982.14]  What do I do?
[2982.60 --> 2994.56]  So there are other tools like can I email, which is the alternative to can I use where it shows like, okay, here's how this like is Flexbox supported?
[2994.56 --> 2995.82]  Flexbox supported or not.
[2996.18 --> 2997.12]  And then they will tell you.
[2997.22 --> 2999.54]  So it's like, just like can I use but for email.
[3000.10 --> 3000.42]  Exactly.
[3000.42 --> 3000.84]  That's cool.
[3001.30 --> 3002.16]  It's like SVG.
[3002.36 --> 3004.60]  You still cannot use SVG on emails.
[3004.78 --> 3007.62]  So then the tool will tell you like, no, you cannot do that.
[3008.24 --> 3009.34]  So that helps.
[3009.60 --> 3014.88]  And then if you try to, like we try to put things like that in the product.
[3014.98 --> 3022.16]  Like, okay, let's add a linter, a compatibility checker powered by can I email on React email.
[3022.16 --> 3029.30]  So we try to shove as much tooling on the email template creation process.
[3029.42 --> 3034.44]  So then when you go live, you don't see as much inconsistencies.
[3034.56 --> 3037.30]  But there's always like a little thing here and there.
[3038.06 --> 3038.36]  That's cool.
[3038.52 --> 3039.34]  I'll link that one up.
[3039.38 --> 3045.42]  Of course, if you can, if you know, can I use replace use with email and you'll hit the website.
[3045.58 --> 3047.42]  So I'll definitely bookmark that.
[3047.42 --> 3051.90]  And I don't think it helps me with my particular problem because I'm not using anything weird.
[3052.04 --> 3058.70]  And it's just like what I might need to do is I'm putting my styles not in line on the elements but in the head.
[3058.70 --> 3063.06]  And I think that perhaps if I inline them, I mean, that's inlined.
[3063.36 --> 3066.62]  It's not a separate style sheet that you're building, like a separate resource.
[3066.92 --> 3068.26]  But it is in the head.
[3068.32 --> 3075.22]  And maybe I need to get them even closer and inline everything and just bloat out all my elements and see if that fixes it.
[3075.74 --> 3077.86]  That's probably my next step is to do that.
[3077.86 --> 3094.60]  But then let's take up this other thing, which you've put some work into and I've been sharing some of your findings on is, you know, Litmus is probably very happy that when I said I got this problem that these LLMs are sending me to Litmus because I didn't know about their product prior.
[3095.84 --> 3097.00]  And there was one other one.
[3097.24 --> 3101.50]  I think it was like, I forgot what it was.
[3101.78 --> 3103.56]  It wasn't as memorable of a product name.
[3104.84 --> 3105.74]  So they lose.
[3105.74 --> 3114.18]  But when people ask for like the best developer podcast, I would love for the changelog to be the answer, right?
[3114.76 --> 3116.44]  Let's just get down to brass tacks.
[3118.42 --> 3119.74]  So how do we do that?
[3119.80 --> 3120.74]  Help us do that.
[3121.24 --> 3125.20]  How do we get our stuff at the top of AI's SEO?
[3125.92 --> 3129.92]  Yeah, I think everyone is trying to answer that question right now.
[3130.68 --> 3130.88]  Yeah.
[3131.58 --> 3133.62]  Man, for me, what really clicked.
[3133.62 --> 3141.00]  So I've been ignoring AI for the past two years, not like from a company perspective.
[3141.00 --> 3144.14]  As an individual, I use AI a ton.
[3144.26 --> 3144.80]  I love it.
[3144.86 --> 3146.52]  I'm optimistic about it.
[3146.54 --> 3147.22]  I think it's great.
[3147.64 --> 3152.30]  But like on a company level, I was like, man, we just need to find product market fit.
[3152.52 --> 3153.42]  Nothing else matters.
[3154.00 --> 3157.18]  Let's just ship stuff that is, you know, that's going to help users.
[3157.18 --> 3165.22]  And, you know, but then in January this year, I just started seeing like some stuff that I couldn't ignore.
[3165.56 --> 3171.94]  So what do we do now is like every time someone signs up for resend, we send an welcome email.
[3172.14 --> 3173.78]  And that welcome email comes from me.
[3173.78 --> 3176.32]  And when they reply, it's very personal.
[3176.70 --> 3179.36]  So then when they reply, it comes to me and then I reply as well.
[3180.60 --> 3188.78]  And then this one day I'm just like waiting, like I started to get into running and then I'm like waiting for this Nike store to open.
[3188.90 --> 3189.84]  So I'm just sitting there.
[3189.94 --> 3191.74]  It's like 30 minutes until the store opens.
[3192.42 --> 3193.82]  I'm just replying to those emails.
[3194.04 --> 3197.32]  And then one person is like, oh, I came from Lovable.
[3197.68 --> 3199.52]  Like, oh, it's cool to reply that.
[3199.52 --> 3203.44]  Next person is like, oh, Claude recommended you reply.
[3204.36 --> 3205.68]  ChatDpt recommended you.
[3206.22 --> 3207.46]  VZero recommended you.
[3207.54 --> 3207.92]  Bolt.
[3208.28 --> 3209.68]  I just started seeing those things.
[3210.00 --> 3213.42]  And it was like six or seven emails in a row.
[3213.94 --> 3217.28]  So I was like, whoa, there's just something here.
[3217.36 --> 3218.42]  I don't know what changed.
[3219.18 --> 3221.78]  It is the new model, like a new version of the LLA.
[3221.88 --> 3222.32]  I don't know.
[3222.76 --> 3223.90]  But something clicked.
[3224.56 --> 3228.92]  And I was like, okay, I cannot ignore this anymore from a company perspective.
[3228.92 --> 3231.48]  I just have to keep pulling that thread.
[3232.68 --> 3238.34]  And then I started finding like, okay, who is thinking about this problem?
[3238.46 --> 3239.88]  Who is like digging into that?
[3239.96 --> 3242.10]  And, you know, it's a huge rabbit hole.
[3242.88 --> 3246.50]  And then what are the techniques to, you know, what are you saying?
[3246.56 --> 3247.70]  I just want more of that.
[3247.70 --> 3252.66]  Like, I want changelog to be the default solution here.
[3253.16 --> 3253.94]  Default answer.
[3254.80 --> 3256.76]  And man, like there's so many interesting things.
[3256.86 --> 3260.86]  Like, for example, from a SEO perspective, we care a lot about Google.
[3261.00 --> 3267.40]  And we care about Google Search Console as the tool to see how we're doing in terms of SEO.
[3267.40 --> 3276.36]  So, turns out, if you want to be the first one in ChatGPT, you've got to care about Bing.
[3276.74 --> 3282.52]  Because Bing, it's what's powering ChatGPT because of the Microsoft partnership.
[3282.52 --> 3290.84]  So, that's how the whole indexing of the web came from Bing as the data source for ChatGPT.
[3291.48 --> 3293.62]  So, then, okay, now that's different.
[3293.78 --> 3298.06]  How do I rank number one on Bing versus Google?
[3298.68 --> 3301.90]  Which is something you would never really pay attention to.
[3301.90 --> 3309.26]  And then you have to start thinking about how do I structure my content on my website?
[3309.50 --> 3313.16]  Because people are asking questions to LLMs.
[3313.42 --> 3318.28]  So, if they're asking questions, then it's a Q&A type of format.
[3318.28 --> 3324.84]  So, then what we started doing was let's just have more FAQs on every single page we have.
[3325.06 --> 3331.76]  And let's turn our knowledge base to be more of a question and answer to feed the LLM.
[3332.80 --> 3345.60]  And then, yeah, just start playing with like LLMs.txt, which is like this protocol for you to like just strip all the HTML and just have the content ready for LLMs to consume.
[3345.74 --> 3346.84]  So, we did that as well.
[3347.58 --> 3352.18]  And, man, just start going down that path using tools like Profound.
[3352.40 --> 3356.94]  So, there's a tryprofound.com tool that shows you like all the traffic.
[3357.68 --> 3359.46]  This one is fascinating, by the way.
[3359.46 --> 3365.74]  So, the way this works is like they hook you, like they hook into your server.
[3366.10 --> 3376.02]  And then whenever the server gets a hit, they will look at the origin of the request and then break it down between like, okay, where is this request coming from?
[3376.02 --> 3383.46]  And the reason why that works is because when you ask ChatGPT, what is recent pricing?
[3383.70 --> 3389.92]  For example, if you do that now, like ChatGPT wasn't trained in that data, right?
[3389.92 --> 3392.76]  So, like there's no way that they know that.
[3393.60 --> 3397.90]  So, that's different than if you ask ChatGPT, like write me a poem.
[3398.26 --> 3402.36]  No, they can do that without using the trained data.
[3402.36 --> 3406.76]  But if you ask pricing for any product, they need to look at the web.
[3407.14 --> 3411.74]  So, because they are able to search the web nowadays, you get a citation.
[3412.58 --> 3417.04]  And then when you get a citation, it's basically them crawling your website, getting the information.
[3417.74 --> 3418.98]  So, then you get that request.
[3419.16 --> 3423.06]  You see like, okay, ChatGPT went to my pricing page.
[3423.06 --> 3427.26]  And then you can start like looking at the breakdown between every model.
[3428.14 --> 3433.46]  Like, okay, cloud users, they actually go to this page and ChatGPT users go here.
[3433.72 --> 3435.62]  And it's just fascinating.
[3435.78 --> 3439.04]  It's a completely new way of looking into SEO.
[3439.44 --> 3440.14]  That's for sure.
[3440.98 --> 3441.54]  That is cool.
[3441.66 --> 3445.04]  So, are you using this Profound platform with Resend?
[3445.18 --> 3446.20]  Yeah, we are.
[3447.32 --> 3448.40]  Is it worth it?
[3448.40 --> 3453.44]  Man, right now, you got to try everything, right?
[3453.78 --> 3461.64]  I think what I love about Profound gives me the information.
[3461.92 --> 3469.76]  I think they still have a long way to go in terms of like, how do I take the beautiful graph and turn into action points?
[3469.96 --> 3474.54]  So, then I can, as a team, I can be like, okay, let's change this content.
[3474.68 --> 3475.22]  Let's do this.
[3475.30 --> 3475.90]  Let's do that.
[3475.90 --> 3478.62]  Now you get the data.
[3479.12 --> 3483.76]  So, you still have to parse the data yourself, I guess.
[3484.88 --> 3496.26]  While we were discussing these things, I couldn't help myself but go to Claude and ChatGPT4O and say, what are the best software developer podcasts?
[3497.26 --> 3499.62]  And we'll start with Claude because that's the one that made me smile.
[3500.10 --> 3501.12]  The very first one.
[3501.28 --> 3502.06]  The changelog.
[3502.44 --> 3502.76]  Woo!
[3502.98 --> 3503.46]  Nice.
[3503.56 --> 3503.80]  Nothing else.
[3503.80 --> 3504.32]  Just kidding.
[3504.42 --> 3505.04]  There's several.
[3505.38 --> 3505.84]  Nothing else.
[3506.36 --> 3507.08]  Nothing else.
[3507.16 --> 3508.12]  Number two, resend.
[3508.20 --> 3508.36]  Wait.
[3509.08 --> 3509.54]  That's right.
[3509.98 --> 3512.18]  There was 10 listed, but we were first.
[3512.34 --> 3513.24]  I couldn't believe it.
[3513.30 --> 3516.26]  I was like, do you know who I am?
[3516.26 --> 3516.80]  I was going to say, you logged in.
[3516.96 --> 3517.12]  Yeah.
[3517.14 --> 3517.86]  Do you know who I am?
[3518.08 --> 3519.36]  Is it in sycophant mode?
[3519.50 --> 3520.44]  That's the thing this week.
[3520.74 --> 3523.18]  You know, ChatGPT is too sycophant-y.
[3523.58 --> 3528.58]  And then ChatGPT had software engineering daily first and then us second.
[3529.26 --> 3529.60]  Okay.
[3529.60 --> 3532.18]  Which is just as good as first, in my opinion.
[3532.18 --> 3534.68]  And what's fascinating is like...
[3534.68 --> 3535.24]  Second is just as good as first.
[3536.88 --> 3545.52]  If you have the same prompt in like Cursor or Windsurf, those models, they cannot do web search.
[3545.52 --> 3550.34]  So then you will get different answers than the ones like when you use the web.
[3550.34 --> 3556.16]  So you can rank differently depending on where you're asking stuff.
[3556.32 --> 3559.06]  And yeah, just it's crazy, man.
[3559.46 --> 3564.38]  I've been really curious about how this will all play out because I think we've talked about this several times here.
[3564.42 --> 3571.10]  I think you said recently on these podcasts you produce that you don't really Google much anymore.
[3571.18 --> 3573.24]  You pretty much go right to the LLM, right?
[3573.28 --> 3574.02]  To ask a question.
[3574.80 --> 3575.88]  For the most part.
[3575.88 --> 3577.64]  For the most part.
[3577.84 --> 3580.24]  When you're asking questions, not finding things.
[3580.48 --> 3580.72]  Yeah.
[3580.82 --> 3584.86]  I mean, I will Google if I know I can just get...
[3584.86 --> 3590.08]  Like sometimes you're searching for something and you know it's the first hit on Google as long as you just type it in.
[3590.96 --> 3594.02]  And so that will be faster than going and asking.
[3594.30 --> 3596.08]  And it'll save the world some energy.
[3596.96 --> 3602.96]  I heard recently that every ChatGPT question is 10x the cost of a Google search.
[3602.96 --> 3605.54]  We're just talking about not the training but the inference cost.
[3605.88 --> 3607.22]  Of energy.
[3607.38 --> 3608.36]  And I'm thinking that makes sense.
[3608.42 --> 3610.84]  It's basically a database lookup versus an inference call.
[3611.56 --> 3613.06]  And so if I can save...
[3613.06 --> 3615.48]  If I can do a database lookup, I'll do it.
[3615.70 --> 3623.94]  But anything serious or that I don't know the answer to or I can't find it quickly, then yeah, I'll pretty much ask an LLM first.
[3623.94 --> 3627.34]  And I have noticed that they started to push me towards...
[3627.34 --> 3627.60]  I don't know.
[3627.68 --> 3628.64]  I mean, push me is okay.
[3628.74 --> 3629.94]  That's an implied...
[3630.52 --> 3631.94]  Like I'm adding that a little bit of...
[3633.06 --> 3636.94]  Although I hear they just added today shopping results.
[3637.98 --> 3638.30]  Yep.
[3638.30 --> 3644.32]  And people are complaining that they're getting like really heavily pushed towards products on questions that don't have to do with that.
[3644.40 --> 3646.20]  I haven't used much today, so I can't say.
[3646.84 --> 3651.48]  But that's kind of a topic that's hitting the social web right now.
[3651.48 --> 3658.82]  And so maybe it's really going to push you towards products here now that they've added some shopping stuff into ChatGPT specifically.
[3660.10 --> 3665.94]  But I have noticed that like whereas in the past it would try to answer my question, but it was always very generic.
[3666.28 --> 3672.14]  Now it's like here are some potential things you could buy, you know?
[3672.14 --> 3676.58]  Like I was trying to get my DJI Spark's batteries to work again.
[3676.64 --> 3679.64]  I'm not sure if you guys know about this because I sure as heck didn't.
[3679.76 --> 3690.36]  But the DJI Spark, which is their small drone, has these batteries, rechargeable batteries, that if you don't use them for a while, and I haven't used my drone for maybe two years.
[3690.48 --> 3690.88]  I don't know.
[3691.00 --> 3694.44]  It's been sitting in the drawer until we just got it out.
[3694.50 --> 3698.80]  If you don't use these batteries for a long time, they go into like hibernation mode and they won't charge.
[3699.14 --> 3699.40]  Really?
[3699.98 --> 3700.76]  That's good, I guess.
[3700.76 --> 3703.48]  It's supposed to save the battery life.
[3703.74 --> 3703.88]  Yeah.
[3703.98 --> 3711.98]  But really all it does is make me think as a guy who doesn't want to go open it up and do surgery on it, like my drone is worthless unless I buy new batteries.
[3712.16 --> 3713.36]  I can't get it to charge.
[3714.30 --> 3720.22]  So on, so of course I'm talking to ChatGPT about this and it takes me down this long road of figuring out here's different things you can try.
[3720.22 --> 3725.96]  At the end it's like you're going to have to buy this little, I don't know, gizmo and a cable.
[3725.96 --> 3733.24]  And I can give you links to ones that you can go buy on Alibaba or somewhere.
[3734.78 --> 3741.62]  And whereas it not used to do that, but here it's like, here's an actual product you should go buy, you know, which is very helpful if I'm going to, if I'm going to go do that.
[3741.62 --> 3746.18]  But anyways, I started just ranting after you asked me a simple question, Adam.
[3746.30 --> 3747.64]  And the answer was yes.
[3747.78 --> 3749.02]  I asked the LLM.
[3749.98 --> 3754.88]  Well, I don't even know what I was going to say, but I think more of this is like five minutes ago.
[3755.04 --> 3755.26]  I'm sorry.
[3755.40 --> 3755.64]  That's okay.
[3755.72 --> 3756.28]  No, that's okay.
[3756.34 --> 3756.94]  That's totally fine.
[3757.00 --> 3758.44]  I think this is definitely a conversation.
[3758.44 --> 3766.44]  I think when it comes to the way I find out what I'm curious about, let's just say there's two places I go.
[3766.92 --> 3767.52]  An LLM.
[3768.18 --> 3770.56]  Lately it's been Claude first, then ChatGPT.
[3772.18 --> 3773.44]  And then obviously YouTube.
[3773.58 --> 3775.26]  Those are the two places I tend to go.
[3775.54 --> 3775.74]  Sure.
[3775.80 --> 3777.12]  Because I highly research.
[3777.20 --> 3779.18]  Like I, I just bought some new clubs.
[3780.36 --> 3781.26]  I'm going to admit it.
[3781.30 --> 3783.08]  You know, they were more than I wanted to spend.
[3784.50 --> 3785.86]  Because that's just how it works.
[3786.66 --> 3787.80]  But I researched them.
[3787.80 --> 3788.76]  Because he researched it.
[3788.78 --> 3789.48]  I researched them.
[3789.62 --> 3794.28]  And then I just wonder like if, if the research isn't just confirmation bias.
[3795.00 --> 3796.02]  Sometimes it is.
[3796.22 --> 3796.50]  For sure.
[3796.66 --> 3801.66]  But you know, how do you research the things you want to buy or consume or enjoy in the world?
[3801.66 --> 3814.16]  And I, I really feel like the place I go to learn, I'm more conversationally asking questions to this thing versus just throwing in keywords into Google and hoping I get a webpage that may help me out.
[3814.16 --> 3822.16]  I feel like the internet is dramatically changing as we speak in so far as how we find information.
[3822.16 --> 3827.06]  And I wonder how that will impact publishing of information.
[3827.58 --> 3831.74]  You know, because like if you don't go to the website anymore to get the info and the LLM just consumes it.
[3832.46 --> 3838.76]  In a case like Resend, it's, you know, like care because you're just trying to get them to become a customer and enjoy your product.
[3838.76 --> 3852.90]  But in the case of something else, you may really want them to come to your website because that's the value to your brain is like a, a captured consumer, whether they're a curious person, an advocate, a customer, you name it.
[3852.90 --> 3854.94]  I just wonder how this is going to change things.
[3855.76 --> 3856.00]  Yeah.
[3856.18 --> 3879.90]  I was just thinking like how much of a buying decision is just confirmation bias, you know, like I think like I, I bought a new barbecue this weekend and I remember watching a lot of YouTube videos just so I had more excuses to buy that one barbecue that I wanted to buy.
[3879.90 --> 3880.22]  Right.
[3880.28 --> 3894.24]  Like, like, oh, now that I know the specs, now that I know this one thing or another, now I can justify to my engineer brain that I'm allowed to spend that much money at a barbecue.
[3895.70 --> 3899.60]  Well, especially the way that, so I've been, I've been mostly a chat GPT user.
[3899.98 --> 3903.74]  I've tried Llama, I've tried all these other things, but I keep coming back to that one.
[3904.36 --> 3909.72]  And I have found recently, so I brought up the sycophant mode, which they're working on.
[3909.90 --> 3916.38]  But I found recently that it's been way too affirmational to my ideas and to my plans.
[3917.70 --> 3919.70]  And I'm like, I don't really want that.
[3919.80 --> 3922.10]  I don't want you to just tell me that I'm right all the time.
[3922.10 --> 3923.48]  Because talk about confirmation bias.
[3923.48 --> 3925.68]  Like, yes, you should buy this thing that you want to buy.
[3926.32 --> 3929.38]  Like, I'd rather just have the truth and not a yes man.
[3929.38 --> 3930.56]  Mm-hmm.
[3930.64 --> 3938.28]  And so that made me start to think like, wow, these people who run these companies have so much power right now.
[3938.98 --> 3941.08]  Because all it takes is a little tweak to that algorithm.
[3941.08 --> 3949.44]  And all of a sudden, I got a sycophant and I'm detached from reality because I got a yes man that I didn't, that wasn't a yes man yesterday.
[3949.44 --> 3950.54]  But today it is.
[3950.54 --> 3956.00]  You know, or that wasn't pushing certain grocery products yesterday, but today it is.
[3956.74 --> 3956.82]  Yeah.
[3956.90 --> 3958.36]  And so that's just very concerning.
[3959.22 --> 3961.88]  That's why I've been using Grok today because I want to just use them both.
[3962.44 --> 3968.34]  Because there's like, you know, Grok, you know, a different company, obviously, and different purpose.
[3968.72 --> 3974.56]  You know, like the idea being truth should be the ultimate goal.
[3974.66 --> 3978.84]  I mean, that's, of course, the idealistic spin that Elon Musk puts on it.
[3979.26 --> 3984.36]  But I feel like if I can use both those two, then maybe I'll get the truth out of one of them or something.
[3984.46 --> 3984.80]  I don't know.
[3984.80 --> 3991.68]  I keep coming back to like, yeah, like how is this different than traditional SEO?
[3992.18 --> 3996.58]  And when Google came out, I guess it was the same concern, right?
[3996.58 --> 4007.62]  And then when, oh, like before I could just go to the web and now Google is like putting more results in front of me and it's influencing what I see.
[4008.08 --> 4014.12]  And then social media comes up and you were like, oh, yeah, now there's this algorithm controlling what I consume.
[4014.80 --> 4018.92]  Um, yeah, there's it's it's always scabry, right?
[4019.58 --> 4019.82]  Yeah.
[4020.46 --> 4021.88]  Maybe we just leave the phones at home.
[4022.18 --> 4026.64]  You know, maybe that's sometimes it's just let it go ahead and.
[4028.22 --> 4030.38]  Go out there and touch grass, as the kids say.
[4031.04 --> 4033.56]  OK, well, at least that is good information.
[4033.76 --> 4036.70]  I'm glad you've done that research on how to position yourself.
[4036.70 --> 4038.78]  I didn't know about that profound platform.
[4038.88 --> 4041.84]  I didn't know that being was the backing for that.
[4042.64 --> 4046.56]  And I'm sure that this is an ever evolving landscape.
[4046.56 --> 4053.98]  And one that every Internet phasing business is going to want to engage with.
[4053.98 --> 4054.40]  Right.
[4055.66 --> 4068.70]  And just like SEO, even though it became such a snake oil business, was such an important business because everybody needed to rank well on Google to exist.
[4068.70 --> 4069.14]  Yeah.
[4070.14 --> 4071.30]  And I think that.
[4072.96 --> 4076.24]  Whether we like it or not, that's going to be the case over the next five, 10 years.
[4076.24 --> 4079.24]  Like if you are not getting surfaced by one of these tools.
[4080.18 --> 4081.68]  You are not going to exist.
[4083.62 --> 4084.30]  Which is sad.
[4084.52 --> 4084.88]  If you are.
[4085.38 --> 4086.28]  That's so true.
[4086.28 --> 4091.18]  Like if you are number one right now, like you guys are, then you want more of that.
[4091.28 --> 4094.52]  Like you definitely want to be number one in every LLM.
[4094.58 --> 4094.94]  Stay there.
[4095.22 --> 4095.40]  Yeah.
[4095.78 --> 4103.02]  I bet there's, I mean, I guess profound might do this, but you need like a, you know, like here's how you rank and all these different ones.
[4103.20 --> 4106.44]  Is that one of the screens they give you on that profound thing?
[4107.06 --> 4107.26]  Yeah.
[4107.26 --> 4114.98]  They show you like not exactly where you rank, but like how each LLM is consuming your data.
[4114.98 --> 4115.12]  Right.
[4116.06 --> 4119.90]  Consuming you, but not necessarily pushing you out there.
[4120.34 --> 4122.22]  Because they don't have access to the prompts, right?
[4122.76 --> 4123.48]  None of us have.
[4124.00 --> 4126.20]  We don't know what people are asking necessarily.
[4126.46 --> 4131.24]  Well, they could ask them, like you could plug in, like what I would like to have is here's my prompt.
[4131.94 --> 4133.52]  What are the best developer podcasts?
[4134.20 --> 4137.04]  What are my best email sending platforms or whatever?
[4137.52 --> 4139.40]  Who should I use for sending my email?
[4139.40 --> 4144.16]  And then just something monitors, like here's where you are on Claude.
[4144.24 --> 4146.18]  Here's where you're on this, this, this, this, this.
[4147.32 --> 4152.64]  And they could do that by just having an account and just asking it the question or something without needing the prompts necessarily.
[4153.32 --> 4157.84]  But yeah, they could sort of like host the prompt for you that sort of triggers like a cron job almost.
[4158.06 --> 4158.68]  That's all it is.
[4158.72 --> 4162.88]  I mean, it's basically an API key and a cron job across a set of providers.
[4163.32 --> 4164.92]  This is probably an open source tool already.
[4164.92 --> 4166.44]  Yeah, there's a YC company.
[4166.44 --> 4168.28]  Somebody out there is screaming into the podcast.
[4168.44 --> 4169.12]  There's a YC company?
[4169.66 --> 4169.82]  Yeah.
[4169.94 --> 4170.12]  Yeah.
[4170.12 --> 4171.58]  There's someone screaming into the podcast.
[4173.60 --> 4175.70]  Productrank.ai is the one.
[4176.54 --> 4177.68]  Productrank.ai.
[4177.98 --> 4179.28]  See, Zeno has all the links.
[4179.28 --> 4180.10]  Come on, Zeno.
[4180.80 --> 4184.22]  This guy's like an LLM with good training data.
[4184.58 --> 4184.94]  There you go.
[4185.00 --> 4185.88]  AI product rankings.
[4186.06 --> 4190.60]  Understand how the top AI models promote products and brands with citations.
[4191.76 --> 4192.56]  Show notes.
[4192.56 --> 4198.22]  Well, you know, the point I think you're bringing up, though, Jared, I think is important, which is this bias.
[4199.48 --> 4199.86]  Right?
[4199.92 --> 4203.74]  This new technology ushered onto the world.
[4204.06 --> 4208.10]  I mean, humanity has changed because of this.
[4208.48 --> 4211.76]  At least the ones that are in, like, first world countries using this.
[4211.76 --> 4218.10]  I don't know how to describe, you know, access and availability to the world in this idea I'm sharing.
[4218.24 --> 4228.98]  But just that if you've got access to these models and you're using stuff, there's a lot of things you can do that isn't just generate the best email or find the best podcast or email platforms to send with.
[4228.98 --> 4233.70]  But a lot more stuff that I go back to golf, man.
[4233.74 --> 4242.42]  I mean, I literally made a club inventory list with lofts and field notes for myself because I'm a new golfer and back to being a new golfer again.
[4243.24 --> 4245.80]  And I'm reminding myself, like, when do I use my wedge?
[4245.84 --> 4246.82]  When do I use my gap?
[4246.90 --> 4250.48]  You know, how should I stand with my seven wood kind of thing?
[4250.48 --> 4252.26]  Like, different things like that.
[4252.32 --> 4253.92]  And so I'm, like, making my club inventory.
[4254.30 --> 4263.14]  And this thing is, like, rather than me type it all up and make the spreadsheet and create the table and all this tedious stuff is doing it for me and with me.
[4263.28 --> 4268.56]  And it's a very much, I would say, to some degree, collaborative in the fact that I know what I want.
[4268.64 --> 4269.78]  I'm asking it to produce it.
[4270.16 --> 4272.58]  But it's not just generating an email kind of thing.
[4272.94 --> 4275.06]  But it knows a lot of this stuff.
[4275.06 --> 4284.76]  And if there's bias injected into this new magic box we all have access to, like, from yesterday.
[4284.94 --> 4287.32]  Like, yesterday it wasn't promoting this and today it is.
[4288.14 --> 4293.32]  I'm just, I don't want it to ruin what they are.
[4293.70 --> 4297.56]  Like, search has been ruined, I would say, over the years.
[4297.70 --> 4304.52]  Like, search is not, it's reliable in the fact that, like you said before, Jared, if you know kind of what you're looking for, you can find it pretty easily.
[4305.06 --> 4309.68]  But you've got seven sponsored before you even get to the real content.
[4309.80 --> 4312.62]  The real content is there because it was gamed in so many shape or form.
[4312.70 --> 4316.60]  They've done things with backlinks and all this trickery to get there.
[4317.02 --> 4318.46]  Maybe they've earned it because they are the brand.
[4318.52 --> 4319.00]  Who knows?
[4319.52 --> 4325.26]  And then you get this sidebar and it's just become just icky.
[4325.60 --> 4330.70]  And I don't want this newfound thing that humanity has to be ickified like that.
[4330.94 --> 4334.48]  I think we should assume that's what's going to happen.
[4335.06 --> 4340.32]  The same way that, you know, Google didn't have ads and then it introduced ads.
[4340.86 --> 4342.62]  ChatGPT doesn't have ads today.
[4343.16 --> 4346.80]  But Entropic is playing with ads for their results.
[4347.08 --> 4349.78]  It's like a private beta program or something.
[4349.78 --> 4356.46]  So I think you will have to pay to be among like the first ones to be.
[4356.86 --> 4358.48]  But hopefully they show as an ad.
[4358.48 --> 4369.02]  But then something else will come and they, once it starts to be so bad, then a new disruption will come up.
[4369.02 --> 4369.42]  Yeah.
[4370.54 --> 4373.18]  Don't you think this is where open models could win though?
[4373.28 --> 4376.76]  I mean, there was not an open alternative to Google search.
[4376.76 --> 4380.10]  I mean, that was comparable.
[4381.44 --> 4401.90]  But the current technology, at least with transformer models, there's ample opportunity and slight leads by the proprietary models for the open models to be used by somebody to come along and productize a model.
[4401.90 --> 4406.52]  And create an actual product that you want to use, not just a model you can call.
[4407.86 --> 4413.72]  That could be that disconnected, quote unquote unbiased.
[4414.00 --> 4414.90]  It's not going to be perfect.
[4415.12 --> 4418.96]  But not like in shitified, which is what we're all afraid of.
[4420.12 --> 4420.56]  Right?
[4420.64 --> 4421.40]  That's what we're afraid of.
[4421.46 --> 4424.92]  Is this going the way that everything else has gone over time?
[4424.92 --> 4428.56]  I think that that's a possibility because there's open models.
[4428.68 --> 4429.82]  There was not an open Google.
[4430.02 --> 4431.06]  There just wasn't.
[4431.06 --> 4432.10]  That could compete.
[4432.50 --> 4437.46]  There was an attempt to create an alternative product like DuckDuckGo.
[4438.12 --> 4439.22]  Great attempt.
[4439.94 --> 4444.58]  But maybe this time around we'll have options.
[4444.58 --> 4457.34]  And maybe those options will actually keep the proprietors more honest, less crappy because they'll have more competition and people just won't put up with it.
[4457.42 --> 4459.80]  But, I mean, Google's been a search monopoly for a very long time.
[4460.32 --> 4461.18]  We haven't had options.
[4461.74 --> 4462.54]  No, we haven't.
[4463.14 --> 4470.14]  You know, you may be really sad when you said that because I was trying to think, like, OK, the next thing coming out is ad-supported Claude.
[4470.14 --> 4472.40]  And that just makes me super sad.
[4472.50 --> 4480.58]  It's like, well, now you're going to have a tier that, sure, maybe it may be affordable, but I'm just so tired of these things coming out with, like, here's the ad-supported version of it.
[4480.64 --> 4483.82]  Like, do you want to spend the double money to get the non-ad-supported version of it?
[4483.88 --> 4484.12]  Maybe.
[4484.80 --> 4488.44]  It might actually backfire with this kind of product because it is so personal and real.
[4489.02 --> 4492.52]  Whereas, like, Google search is a list of results.
[4492.94 --> 4499.60]  And it's like, yes, you can pay money to just be listed before these other results, but we all know that that's what's going on.
[4499.60 --> 4507.28]  But, like, the way you treat Claude or ChatGPT or Grok or whatever it is you're using, you treat it like your little research assistant.
[4507.58 --> 4510.76]  I don't know why it's so little to us, but I'm like, here's a little guy, you know?
[4510.94 --> 4512.26]  And you treat it like a friend.
[4513.44 --> 4524.46]  And when you come to a friend for something and they're shoving sponsored stuff as answers, like, that's so unappealing and so unattractive as a friend.
[4524.46 --> 4525.34]  And, like, I wouldn't do that.
[4525.34 --> 4531.38]  Like, you know, if you came to me and I was like, you should use Resend because I'm an affiliate, you know?
[4531.70 --> 4533.32]  I'm like, maybe I'll tell you, hey, I'm an affiliate.
[4533.50 --> 4534.86]  Use Resend and I'll get 10 bucks.
[4534.92 --> 4536.08]  I'll give you five or whatever.
[4536.68 --> 4537.98]  That's friends do that kind of stuff.
[4538.24 --> 4545.74]  But if, like, everything I told you as far as advice in life was just a sponsored piece of advice, I wouldn't be your friend anymore.
[4545.74 --> 4547.68]  Like, you'd be so turned off by that, wouldn't you?
[4548.24 --> 4552.42]  And maybe what changed is the memory portion of it, right?
[4553.56 --> 4564.32]  I see my wife using it and it's just so interesting because she builds, like, these little coaches for her.
[4564.42 --> 4566.42]  So she was like, oh, I want to improve my health.
[4567.00 --> 4570.04]  Can you tell me, like, health tips every day?
[4570.04 --> 4580.58]  And then she already fed the memory with, like, you know, the fact that she's married and that she has a daughter and the model knows their name.
[4580.70 --> 4590.30]  So they would tell, like, okay, maybe you should go with Zeno and Victoria to a brunch and just drink more water than normal.
[4590.92 --> 4594.56]  And the voice and tone, it cheers her up.
[4594.68 --> 4596.38]  And I'm like, that's crazy.
[4596.46 --> 4598.94]  That's beautiful because it has memory now.
[4598.94 --> 4600.14]  Uh-huh.
[4600.38 --> 4600.68]  Mm-hmm.
[4601.20 --> 4606.22]  And maybe that's the moat, you know, like, if people keep talking about, like, oh, what's the moat for LLens?
[4606.30 --> 4608.22]  Like, maybe that's what's going to be.
[4608.34 --> 4617.46]  Like, the fact that now they have memory, the one that has the best memory, the one that knows, like, okay, Jared, like, I just want the truth.
[4617.80 --> 4621.36]  Don't try to be nice, like, no fluff.
[4621.54 --> 4621.66]  Right.
[4622.12 --> 4623.14]  Get me to the truth.
[4623.20 --> 4626.10]  Okay, I know that's how I'm going to communicate with him.
[4626.44 --> 4628.16]  And I would just follow that, right?
[4628.94 --> 4629.78]  Um, no.
[4629.78 --> 4630.00]  Yes.
[4630.52 --> 4635.82]  I did try putting, there are prompts you can put in that have been a little disabled sick of font mode, by the way.
[4635.92 --> 4636.42]  But go ahead, Adam.
[4636.74 --> 4641.84]  I was going to say, I agree with you, Jared, on this front, because you want the LLM to be for you.
[4642.02 --> 4644.32]  And I guess you could say your friend in a way, or friendly.
[4645.02 --> 4645.30]  Yeah.
[4646.18 --> 4646.50]  Helpful.
[4646.50 --> 4647.10]  Yeah.
[4647.10 --> 4648.64]  Like, for me, not against me.
[4648.76 --> 4661.66]  And I would say, if you're advertising to me, if you've got some sort of alternative motive that you're suggesting things for, like, help me find the version of truth I'm trying to seek.
[4661.66 --> 4669.16]  Whether it's health tips or business advice or what's the best podcast or email platform to consider.
[4669.94 --> 4685.36]  You know, I want, I want whatever the consensus of the world, I suppose, deems as truthful and honorable versus, you know, not fabricated or made up or for some sort of I get paid behind the scenes motive kind of thing.
[4685.36 --> 4686.72]  I want the real.
[4687.22 --> 4694.02]  And I would, I would probably immediately stop using whatever doesn't respect that.
[4695.08 --> 4699.20]  And then I would use the one that does, obviously.
[4699.30 --> 4699.54]  Right.
[4700.84 --> 4701.48]  And I'd pay more.
[4701.64 --> 4702.62]  I'd probably pay more for that.
[4702.72 --> 4705.32]  I hate to even say that, because I feel like everything is rented, man.
[4705.34 --> 4706.18]  They said it before.
[4707.22 --> 4712.58]  You will, you will, you will, you will, you will own nothing and, and, and be happy.
[4712.58 --> 4715.68]  Everything is rented.
[4716.68 --> 4717.30]  That's great.
[4717.36 --> 4719.14]  Everything is a service and a rent.
[4720.10 --> 4720.84]  Tired of it.
[4721.00 --> 4721.72]  I'm over it.
[4722.22 --> 4723.78]  You didn't rent those golf clubs, did you?
[4724.46 --> 4725.52]  I bought them.
[4726.06 --> 4727.96]  Those are, but I mean, like.
[4727.96 --> 4731.12]  Did you buy a license to use those for a certain amount of time?
[4731.30 --> 4731.90]  Yeah, I didn't.
[4731.98 --> 4735.66]  I mean, honestly, though, I think golf clubs are one of those things.
[4735.70 --> 4739.96]  They're too personal that you couldn't, you really couldn't rent them.
[4740.38 --> 4741.52]  Not if you're a serious golfer.
[4741.52 --> 4742.40]  You wouldn't rent clubs.
[4742.58 --> 4742.98]  No.
[4743.30 --> 4747.98]  You certainly rent a golf cart to go on the course, because who the heck's going to take
[4747.98 --> 4750.76]  their golf clubs and their cart to the course?
[4750.84 --> 4753.38]  That's just, that doesn't make any sense.
[4753.70 --> 4755.60]  Like, like, wait, wait, wait, wait.
[4755.66 --> 4758.82]  Do you drive the cart to the course or you got like a trailer?
[4758.98 --> 4760.12]  You pull the cart and trailer?
[4760.76 --> 4761.12]  Exactly.
[4761.24 --> 4761.96]  Like, who would do that?
[4762.30 --> 4763.14]  No one would do that.
[4763.18 --> 4764.10]  This is my cart.
[4764.80 --> 4765.00]  Yeah.
[4765.20 --> 4766.10]  Can I bring my own cart?
[4766.30 --> 4766.98]  Hey, if you want to.
[4767.02 --> 4768.94]  That's kind of, I mean, like, you're really committed.
[4769.38 --> 4773.38]  The only time you rent clubs is when you're in like Maui or something and you didn't bring
[4773.38 --> 4774.08]  your clubs with you.
[4774.08 --> 4776.44]  Because, you know, traveling with clubs is a pain in the butt.
[4776.66 --> 4777.12]  It is.
[4777.12 --> 4781.08]  Now, I will say that a serious golfer will take their clubs with them.
[4781.08 --> 4783.06]  A hundred percent, but it's still a pain in the butt.
[4783.66 --> 4787.56]  I've rented a mountain bike before when I was in Sedona and I have my own mountain bike.
[4787.60 --> 4788.26]  I didn't send mine there.
[4788.32 --> 4792.74]  I'm like, it's impractical to send my mountain bike to Sedona so I can ride it in Sedona.
[4793.12 --> 4796.88]  I'll rent the exact same one that's owned by a bike shop there.
[4796.94 --> 4797.32]  And I did.
[4797.38 --> 4802.52]  I rented my literal same bike, same travel, most of the same specs, but it was pretty
[4802.52 --> 4806.58]  much on par for, to use a pun, pretty much on par for what I actually own.
[4806.66 --> 4808.16]  So it was like renting my bike.
[4808.48 --> 4808.86]  Close enough.
[4808.86 --> 4810.70]  But in Sedona, which is kind of cool.
[4811.08 --> 4811.72]  Mm-hmm.
[4813.58 --> 4814.40]  Oh, man.
[4814.90 --> 4815.72]  Oh, boy.
[4816.98 --> 4819.76]  Why do we always end up dystopian when we're talking about AI?
[4819.86 --> 4823.58]  We always kind of end up a little depressed about where it might be going.
[4824.04 --> 4826.54]  I think it's kind of overwhelming because we just don't know.
[4827.06 --> 4827.34]  Yeah.
[4827.86 --> 4836.72]  And there's, we have such a history of things going from like great to worse that, I mean,
[4836.74 --> 4839.66]  the internet's gone, I think, from great to worse in many small and big ways.
[4839.66 --> 4845.12]  And I think Cory Doctorow's done a good job of documenting a lot of that.
[4846.20 --> 4846.40]  Mm-hmm.
[4846.40 --> 4852.86]  And so we can't help to be a little bit skeptical or cynical or whatever the term is, dystopian
[4852.86 --> 4854.04]  with where we think it's going to go.
[4854.04 --> 4860.28]  I mean, in the small, though, like I'm not pessimistic in the small, but when I think
[4860.28 --> 4864.28]  about the bigger pictures and like the implications, it starts to overwhelm.
[4864.38 --> 4865.78]  And a lot of it's because we don't know.
[4866.14 --> 4867.94]  And so, you know, what you don't know is scary.
[4868.94 --> 4869.64]  That's my take.
[4869.76 --> 4869.80]  Yeah.
[4869.80 --> 4873.62]  Why do you think we always, although Zeno's not always here, so he doesn't realize that
[4873.62 --> 4874.66]  we always tend to do this.
[4874.76 --> 4875.46]  We always get to here.
[4875.58 --> 4875.90]  Oh, okay.
[4876.02 --> 4876.84]  Here we are at the end of the show.
[4876.94 --> 4880.12]  We're all a little bit like contemplative and concerned.
[4880.78 --> 4881.14]  Yeah.
[4881.14 --> 4885.92]  Why is it important to think about the end result of a technology?
[4886.44 --> 4887.40]  Maybe it isn't.
[4888.08 --> 4890.30]  Like right now it works great.
[4890.84 --> 4898.16]  Right now I can come in and ask, based on what you know about me, give me your sincere
[4898.16 --> 4902.38]  opinion on my flaws and then it will give something.
[4904.26 --> 4905.38]  Maybe it's great.
[4905.48 --> 4906.22]  Maybe it's not.
[4906.32 --> 4907.20]  Maybe it's just fluff.
[4909.10 --> 4910.68]  Right now there are no ads.
[4911.14 --> 4914.06]  Let's just enjoy it while that's the case, you know.
[4914.42 --> 4915.20]  Let's just enjoy it.
[4916.52 --> 4918.12]  Well, it's still called today.
[4918.28 --> 4919.64]  We will enjoy today.
[4919.92 --> 4925.40]  I would say that life is better with these tools than it is without these tools.
[4925.90 --> 4926.34]  Yeah.
[4926.70 --> 4932.88]  And that's why we all have our phone addictions because our phone has actually provided so
[4932.88 --> 4936.90]  much value to us on a recurring basis that we become addicted to it.
[4937.54 --> 4939.98]  I mean, you can take your phone and nothing else.
[4939.98 --> 4942.14]  And travel the world.
[4942.76 --> 4943.12]  Okay.
[4943.18 --> 4945.90]  That'd be a big stretch because there's parts of the world that probably wouldn't work.
[4946.22 --> 4946.80]  But right.
[4946.88 --> 4947.92]  You have to plan for that.
[4947.98 --> 4948.84]  You can travel America.
[4949.04 --> 4949.22]  Let's go.
[4949.22 --> 4949.72]  And a charger.
[4950.38 --> 4950.74]  Yeah.
[4950.74 --> 4951.28]  You need a charge.
[4952.74 --> 4953.34]  Take a charger.
[4953.76 --> 4954.54]  That's about it though.
[4954.54 --> 4957.98]  No, actually most hotels will have a charger for you or whatever.
[4958.26 --> 4967.74]  You know, I'm just saying like, okay, you know, maps, communications, emergencies, transactions,
[4968.72 --> 4970.56]  local touristy questions.
[4970.56 --> 4971.74]  Like what could you not get?
[4971.84 --> 4973.20]  Like what would you, else would you need?
[4974.08 --> 4975.12]  Obviously you need to eat.
[4975.62 --> 4976.44]  That's about it.
[4976.60 --> 4978.00]  So it's a pretty valuable thing.
[4978.00 --> 4980.44]  Like that's, that's amazing.
[4981.14 --> 4981.30]  Yeah.
[4981.40 --> 4982.20]  Provide you're connected.
[4982.46 --> 4983.18]  Provide you're connected.
[4983.30 --> 4984.06]  You have access.
[4984.54 --> 4989.18]  I'd rather have that than a book with the map and carry that with me.
[4989.40 --> 4989.66]  Right.
[4989.84 --> 4990.02]  So.
[4990.02 --> 4994.44]  Well, it's kind of like that iPad commercial gone bad where they were smashing all the
[4994.44 --> 4994.80]  stuff.
[4994.96 --> 4998.44]  They're smashing the creative stuff and all the creatives got mad about it.
[4998.52 --> 5002.74]  I wasn't mad about it, but apparently maybe I'm not creative enough, but it was a good
[5002.74 --> 5006.46]  idea like in concept because it has replaced.
[5006.54 --> 5010.22]  I think there's a better one where it's like sitting on a desk and like the phone replaces
[5010.22 --> 5012.10]  all the different things you used to have on your desk.
[5012.80 --> 5014.16]  And they really have done that.
[5014.16 --> 5018.76]  They've just, they can be so many different things that, yeah, you don't want to have a
[5018.76 --> 5024.36]  giant map and you're, you know, your shotgun person sitting next to you in the driver's
[5024.36 --> 5028.02]  seat, you know, they've got the map open real wide and they're trying to find where
[5028.02 --> 5030.12]  you are, but then they're holding it upside down.
[5030.18 --> 5033.30]  And, you know, like it used to be rough.
[5034.12 --> 5035.06]  It used to be rough.
[5035.96 --> 5040.16]  Then you, then you leave your wallet on a, you're filling up gas and you leave your wallet
[5040.16 --> 5042.50]  sitting there and you drive away to the gas station.
[5043.08 --> 5045.06]  Not speaking from personal experience or anything.
[5045.06 --> 5050.36]  You know, I was, uh, this weekend we had, um, a, uh, this thing called founders weekend
[5050.36 --> 5052.68]  founders day here in dripping Springs where I live at.
[5052.98 --> 5057.52]  And it's this big old festival, basically, you know, Friday, Saturday, Sunday, it's like
[5057.52 --> 5058.58]  all, everybody's there.
[5058.64 --> 5059.28]  The whole town's there.
[5059.34 --> 5059.92]  It's a small town.
[5060.00 --> 5060.52]  Everybody's there.
[5061.38 --> 5065.86]  And, uh, and I thought I lost my phone and I freaked out.
[5065.86 --> 5070.88]  Like I was like, I was like, I didn't like cry and fall down and you know, whatever,
[5071.16 --> 5074.84]  but I was like, I was like, I knew where I left it.
[5074.94 --> 5078.66]  I knew I set it down and I was just praying when I got back, it was there still yet.
[5078.80 --> 5081.50]  But the whole time I'm like, Oh my gosh, like, what would I do?
[5081.78 --> 5082.12]  Sure.
[5082.12 --> 5087.58]  I can go get a new one, but like, you know, I don't have the thing and it's got all my
[5087.58 --> 5087.82]  information.
[5088.02 --> 5089.96]  I was just like, this cannot happen.
[5090.00 --> 5093.56]  I've never literally lost my phone like this ever in my life today.
[5093.64 --> 5094.54]  Can't be the day.
[5094.54 --> 5095.66]  No, no, no.
[5095.82 --> 5099.60]  You know, I don't know what I would do if I lost my phone.
[5099.66 --> 5100.50]  I would be pretty sad.
[5100.62 --> 5103.42]  And I'd have to wait for this new one to come in, which would probably be days.
[5103.82 --> 5106.04]  So here's me days without a phone.
[5106.14 --> 5106.88]  Could you imagine that?
[5106.94 --> 5109.08]  Like, nah, let's not do that.
[5109.48 --> 5109.56]  Yeah.
[5109.56 --> 5111.58]  I can do hours, but I wouldn't want to do days.
[5111.86 --> 5112.20]  Too valuable.
[5112.46 --> 5112.56]  Yeah.
[5113.04 --> 5113.68]  Then you're jealous.
[5113.80 --> 5114.86]  You're like, look at them.
[5114.92 --> 5115.92]  They got their phone over there.
[5116.10 --> 5116.42]  They got their phone.
[5116.86 --> 5117.72]  She's got their phone.
[5117.78 --> 5118.52]  He's got his phone.
[5118.72 --> 5119.34]  Where's my phone?
[5119.86 --> 5120.42]  Where's my phone?
[5121.36 --> 5121.94]  I don't know.
[5121.94 --> 5127.26]  Well, Zeno, your goal is to make Resend so valuable that people talk about it.
[5127.26 --> 5128.32]  Like we talk about our phones.
[5128.40 --> 5129.36]  Like, where's my Resend?
[5129.44 --> 5129.68]  Come on.
[5129.70 --> 5130.64]  That guy's using Resend.
[5130.76 --> 5131.76]  She's using Resend.
[5132.00 --> 5132.74]  Where's my Resend?
[5133.84 --> 5135.66]  If you do that, you'll be a very rich man.
[5136.62 --> 5137.18]  Oh, man.
[5137.26 --> 5138.56]  On his way, I would say.
[5138.74 --> 5139.42]  On his way.
[5140.30 --> 5140.88]  What's left?
[5141.00 --> 5141.92]  What's left unsaid?
[5142.36 --> 5143.38]  What else could we be friends about?
[5143.88 --> 5145.22]  You guys want to talk about that new car?
[5146.26 --> 5146.92]  What car is that?
[5146.92 --> 5150.54]  The new Slate Auto.
[5151.48 --> 5152.72]  Oh, I didn't see that.
[5153.24 --> 5153.60]  All right.
[5153.70 --> 5155.26]  Slate.auto.
[5155.60 --> 5155.92]  I'm on it.
[5155.96 --> 5159.14]  This truck can be anything, even an SUV.
[5159.44 --> 5160.92]  This is a brand new company.
[5161.02 --> 5162.64]  I think they're about three years old.
[5163.10 --> 5165.54]  Just came out of Stealth.
[5166.92 --> 5168.92]  Based in Michigan, I believe.
[5169.46 --> 5174.52]  But their factory is going to be in Indiana.
[5174.52 --> 5178.44]  So it's all U.S.-based, mostly American-made.
[5179.26 --> 5184.38]  A Slate is a radically simple electric pickup truck that can change into whatever you need
[5184.38 --> 5184.90]  it to be.
[5185.46 --> 5190.52]  So the idea here is, as an EV, it does not have great...
[5190.52 --> 5192.28]  It's not really called gas mileage anymore.
[5192.74 --> 5193.68]  It's still mileage, though.
[5194.34 --> 5194.70]  Range.
[5195.02 --> 5196.06]  Yeah, it doesn't have great range.
[5196.16 --> 5196.52]  Thank you.
[5196.66 --> 5197.76]  I'm not up to date on my EV.
[5197.76 --> 5198.36]  Mileage might be good, too.
[5198.50 --> 5198.74]  Mileage.
[5199.42 --> 5200.32]  Yeah, it doesn't have great range.
[5200.36 --> 5203.02]  I think it's like 150 to 200, but you can buy a bigger battery.
[5203.02 --> 5205.50]  But the idea here is, it's cheap.
[5206.04 --> 5208.18]  It's less than $20,000 for a truck.
[5208.28 --> 5209.46]  Now, this is a small truck.
[5209.72 --> 5210.76]  It's a two-seater.
[5211.20 --> 5211.84]  No way.
[5211.98 --> 5212.76]  Yeah, less than 20.
[5213.04 --> 5214.04]  After EV credits.
[5214.30 --> 5216.80]  So probably like in the range of 25 to start.
[5216.86 --> 5217.06]  Okay.
[5218.02 --> 5220.44]  And it's bare bones on purpose.
[5220.56 --> 5221.54]  It's completely bare bones.
[5221.64 --> 5222.48]  There's nothing to it.
[5222.54 --> 5222.82]  Wow.
[5222.94 --> 5225.82]  There's no like dash with a computer screen.
[5226.02 --> 5226.82]  It's not even painted.
[5227.22 --> 5228.34]  It's like carbon fiber.
[5228.34 --> 5232.60]  And so it's built to be wrapped, not painted, because that's kind of the cool thing nowadays,
[5232.76 --> 5233.02]  too.
[5233.46 --> 5234.60]  It's like, get your car wrapped.
[5235.46 --> 5237.92]  And they call it slate because it's a blank slate.
[5238.06 --> 5238.40]  Get it?
[5238.68 --> 5241.12]  You're supposed to customize the heck out of it.
[5241.20 --> 5242.10]  So it's like modular.
[5242.40 --> 5243.42]  You can buy different parts.
[5243.48 --> 5244.02]  You can add.
[5244.40 --> 5247.60]  You can turn it into an SUV by buying the SUV add-on.
[5248.34 --> 5249.12]  You can add battery.
[5249.80 --> 5251.08]  You can add like roof racks.
[5251.14 --> 5252.22]  Like you can do that in regular cars.
[5252.38 --> 5253.54]  But you name it.
[5253.58 --> 5254.26]  Like the dash.
[5254.32 --> 5255.30]  You can do stuff.
[5255.48 --> 5256.44]  And then you can wrap it.
[5256.52 --> 5257.00]  And you can even.
[5257.58 --> 5258.58]  It's so easy to wrap.
[5258.68 --> 5260.36]  They're saying this is all just marketing fluff.
[5260.40 --> 5261.22]  It doesn't exist yet.
[5261.82 --> 5265.56]  The truck exists, but not anywhere that you can buy it.
[5266.14 --> 5267.26]  You can only reserve it.
[5268.00 --> 5273.74]  But it's so easy to wrap that you can actually do it yourself in an afternoon.
[5273.88 --> 5277.40]  Like you don't have to actually have a professional is what they're saying is the plan.
[5277.60 --> 5280.16]  And then like everything is self-maintained.
[5280.26 --> 5287.78]  So like if you break off your rearview mirror, they're just going to ship you a new rearview mirror and a little tutorial on how to like put the other one in.
[5288.84 --> 5294.46]  So it's kind of a cool new take, I think, on reinventing the personal vehicle.
[5296.16 --> 5297.88]  And I'm into the idea.
[5298.00 --> 5301.44]  I'm not sure if I'm into the product because time will tell.
[5301.96 --> 5304.38]  I think it doesn't ship until like end of 2026.
[5306.04 --> 5307.02]  But that's the slate.
[5307.02 --> 5307.58]  What do you guys think?
[5308.28 --> 5309.66]  I almost bought one just now.
[5312.86 --> 5313.86]  This is a big truck.
[5313.98 --> 5314.82]  This is a little truck.
[5315.18 --> 5316.10]  Well, no, I know that.
[5316.24 --> 5318.50]  So I think there is it's very popular.
[5319.94 --> 5320.84]  Not in the US.
[5321.02 --> 5327.16]  I want to say like Japan, maybe even China, India, places like that, that they have this tiny little truck.
[5327.16 --> 5329.24]  And I think they only make them there.
[5329.34 --> 5331.78]  And there's been a few imported to the US.
[5331.78 --> 5335.26]  And you can like, you can even like buy it on the internet for like 10 grand.
[5335.46 --> 5336.26]  It just arrives.
[5336.34 --> 5337.62]  You just unbox this truck.
[5337.62 --> 5339.16]  It reminds me of that.
[5339.22 --> 5341.00]  This little simplistic thing.
[5341.00 --> 5343.58]  I think this is a revolutionary idea.
[5343.58 --> 5344.68]  Like this is the way it should be.
[5344.68 --> 5346.08]  Give me a bare bones vehicle.
[5346.08 --> 5348.30]  That just drives.
[5348.30 --> 5349.30]  That's modular.
[5349.80 --> 5350.06]  Yeah.
[5350.10 --> 5350.92]  That I can maintain.
[5351.34 --> 5353.84]  That doesn't cost Tesla prices.
[5353.84 --> 5359.04]  And that you can spend more if you want to spend more and upgrade it, you know, and put all kinds of stuff on it.
[5359.38 --> 5362.54]  But if you go through the little customizer, I mean, it's pretty cool.
[5362.98 --> 5365.64]  Like you can pick these different wraps, pick your color.
[5366.04 --> 5374.20]  They'll show you some different examples of people who have, you know, not real people have customized it, but what real people might do to really make it your own.
[5374.20 --> 5381.44]  And I feel like my phone is like a no case standard bog standard iPhone.
[5382.42 --> 5389.96]  And I'm a weirdo because so many people have like cases and designs and like they want to trick out their phone because we all have one.
[5390.08 --> 5391.68]  You want yours to be yours.
[5392.30 --> 5393.44]  I'm just a boring loser.
[5393.58 --> 5394.30]  So I just leave it.
[5394.30 --> 5404.80]  But I feel like with these slate trucks, potentially it could be very popular with people that want to customize and not spend an arm on a leg doing it.
[5405.66 --> 5411.16]  I mean, you customize a Tesla and it's like, well, I spent 50K on the Tesla and now I got to get it wrapped for another 5K or whatever.
[5412.22 --> 5414.08]  Like this is so much cheaper.
[5414.98 --> 5415.10]  Yeah.
[5415.22 --> 5418.18]  I think that this will be very popular with younger folks for sure.
[5418.18 --> 5426.20]  Especially the way young folks that I know of at least like to stand out or be different or go counterculture, so to speak.
[5427.88 --> 5431.14]  It's, uh, it kind of reminds me of like the, the model T.
[5431.30 --> 5438.54]  I mean, I wasn't alive in those days, but it reminds me of like when the Ford truck first came out, the model T is like, you can have any color you want as long as it's black.
[5439.12 --> 5439.40]  Yeah.
[5439.60 --> 5444.16]  It's like, you can have any of these you want as long as it's simple when we give it to you and then you can do whatever you want to at that point.
[5444.60 --> 5446.42]  You know, here's how simple it is.
[5446.42 --> 5447.82]  And this might be like a bridge too far.
[5448.18 --> 5454.28]  For some people, you actually have to, uh, wind the window down like with the old windy thing.
[5455.18 --> 5455.58]  Yeah.
[5456.38 --> 5456.70]  Yeah.
[5456.70 --> 5458.30]  That might be a deal breaker for me.
[5459.72 --> 5460.12]  Okay.
[5460.40 --> 5461.46]  That's too simple.
[5462.04 --> 5462.86]  That's how simple it is.
[5462.92 --> 5463.70]  No seatbelts.
[5463.78 --> 5464.26]  No, just kidding.
[5464.74 --> 5466.00]  I'm not sure they have seatbelts, but.
[5467.94 --> 5468.32]  What do you think?
[5468.42 --> 5470.48]  Are you going to, uh, you buy one of these?
[5470.78 --> 5471.26]  Would you get one?
[5471.50 --> 5476.96]  I've been an optimistic this whole podcast and I'm going to be the skeptical one now.
[5477.30 --> 5477.70]  Okay.
[5478.18 --> 5480.84]  I remember seeing the modular phones.
[5481.14 --> 5481.78]  Remember those?
[5481.98 --> 5482.10]  Right.
[5482.34 --> 5482.96]  Uh, right.
[5483.50 --> 5490.70]  It's just so tricky to build like super highly niched modular products.
[5491.02 --> 5493.04]  Uh, I love the idea.
[5493.60 --> 5494.22]  Uh, yeah.
[5494.22 --> 5502.22]  Uh, but I feel like people want, they like the idea of personalization more than they actually
[5502.22 --> 5503.86]  personalize things themselves.
[5504.32 --> 5508.46]  Uh, so maybe it's great that it has an option.
[5509.10 --> 5509.20]  Yeah.
[5509.20 --> 5509.96]  I think that's true.
[5509.96 --> 5513.12]  I think that I would be with you if it wasn't so cheap.
[5514.08 --> 5514.44]  Yeah.
[5514.52 --> 5515.22]  Super cheap.
[5515.22 --> 5519.38]  To get into a, to get in, to get an EV truck.
[5519.42 --> 5519.64]  Yeah.
[5520.26 --> 5521.36]  For under 20 K.
[5522.50 --> 5523.10]  That's wild.
[5523.26 --> 5526.50]  That's bringing in the price into a lot of people's wheelhouses who wouldn't otherwise
[5526.50 --> 5527.70]  not be able to afford it.
[5527.76 --> 5531.52]  So I feel like that's probably why I'm more bullish, but yeah, I agree.
[5531.60 --> 5537.46]  I think customization people want, but completely modular ends up having like a Lego feel to
[5537.46 --> 5537.98]  it or something.
[5537.98 --> 5541.92]  Like it just doesn't like when things kind of snap together, you're like, oh, can I even
[5541.92 --> 5542.54]  trust this?
[5542.66 --> 5545.66]  So yeah, I can understand your skepticism.
[5546.70 --> 5548.36]  It has different charging options too.
[5548.40 --> 5551.40]  Like you plug it into a normal plug, a normal 120 volt plug.
[5552.28 --> 5552.72]  Yeah.
[5553.38 --> 5554.30]  It takes a little longer.
[5554.30 --> 5555.52]  I think it charges longer.
[5556.12 --> 5560.28]  I appreciate a company that comes out and just like really does think about everything
[5560.28 --> 5560.66]  differently.
[5560.66 --> 5562.22]  Like let's throw out every assumption.
[5562.22 --> 5563.44]  Like here's an assumption.
[5563.58 --> 5564.56]  You have to paint your car.
[5564.62 --> 5565.38]  Like, no, you don't.
[5565.44 --> 5566.62]  Here's some carbon fiber.
[5566.62 --> 5568.94]  Or maybe you want to wrap it, maybe not.
[5569.64 --> 5569.86]  Yeah.
[5570.76 --> 5573.24]  Like, so that's cool.
[5574.94 --> 5576.90]  The company is kind of interesting.
[5578.34 --> 5582.54]  I think there's two women at the top, founders.
[5585.60 --> 5595.16]  And there's some backing by, it hasn't been confirmed, but Jeff Bezos allegedly has, is an
[5595.16 --> 5595.86]  early investor.
[5596.62 --> 5602.36]  And so it's kind of a, you know, a Tesla competitor in that way and every way that Bezos wants to
[5602.36 --> 5604.08]  compete with Musk.
[5604.54 --> 5609.32]  And so there's some of that going on, but they're very young, three years.
[5609.66 --> 5611.36]  Who knows if they can even ship this thing.
[5611.88 --> 5616.16]  But yeah, I'm, I think it's a cool, different take on trucks.
[5616.16 --> 5621.50]  And like you said, Zeno, whether win, lose or draw, I think it's cool that it exists and
[5621.50 --> 5622.16]  that they're trying it.
[5622.40 --> 5623.58]  I think it needs to exist.
[5623.66 --> 5623.96]  Honestly.
[5624.06 --> 5624.46]  What was that?
[5624.66 --> 5626.36]  There's like a Kia Soul or something like that.
[5626.40 --> 5628.36]  This like little ugly little box thing.
[5628.38 --> 5631.86]  It's so popular with young folks like that they're buying their first vehicle.
[5631.96 --> 5633.14]  This is going to be like that.
[5633.14 --> 5636.52]  I think it's, there's no way they can not succeed.
[5637.28 --> 5638.22]  I'll say this now.
[5638.32 --> 5640.16]  So you're, you're the most bullish of all of us.
[5640.16 --> 5644.14]  I think the world needs the simplest choice to get a vehicle.
[5644.14 --> 5644.74]  Cause I mean, that's.
[5644.86 --> 5646.02]  Would you, would you invest?
[5646.62 --> 5647.72]  Yeah, I'd invest.
[5648.04 --> 5648.40]  Okay.
[5648.50 --> 5649.70]  I'd, I'd invest right this second.
[5649.98 --> 5650.46]  Right this second.
[5650.46 --> 5650.92]  Would you buy one?
[5650.92 --> 5651.66]  Right this second.
[5651.76 --> 5652.86]  I got, I got, I got my.
[5652.98 --> 5653.50]  You buy one, yeah.
[5653.52 --> 5654.58]  I got Apple Pay right here.
[5656.26 --> 5658.14]  Um, I think, no, I really do.
[5658.18 --> 5660.36]  I think that this is a, I agree with you, Drew.
[5660.38 --> 5667.62]  I think I applaud new companies like, not just like this specifically, but ones that throw
[5667.62 --> 5670.46]  out all the rules and say, is that true?
[5671.04 --> 5672.46]  Do you really need to paint your car?
[5672.66 --> 5674.74]  Do you really need power windows?
[5674.94 --> 5675.88]  I think that's the yes.
[5675.94 --> 5676.88]  That's a yes for me.
[5677.02 --> 5678.76]  I mean, I want some power windows.
[5679.26 --> 5679.36]  Yeah.
[5679.36 --> 5680.46]  That's a bridge too far.
[5680.86 --> 5683.54]  But maybe that actually, I mean, the eighties is a big thing.
[5683.54 --> 5684.34]  Like I was just.
[5684.56 --> 5684.86]  There's no stereo.
[5685.84 --> 5686.74]  There's no stereo.
[5687.34 --> 5687.66]  Nope.
[5687.96 --> 5688.68]  Oh gosh.
[5688.90 --> 5689.28]  Add on.
[5692.78 --> 5696.08]  I love how the optimism is like dropping.
[5696.08 --> 5698.78]  I'm still, I'm still optimistic.
[5699.44 --> 5702.84]  I did see that actually when I was watching, I was looking at some of these photos and I
[5702.84 --> 5704.96]  saw like a JBL kind of speaker.
[5705.34 --> 5708.78]  Well, they're like, if you want, if there's like the basis to put things, like things can
[5708.78 --> 5709.86]  snap into the dash.
[5709.96 --> 5710.44]  Yeah, totally.
[5711.12 --> 5715.16]  But they're like, they're like, you can buy one of ours or bring your own Bluetooth stereo
[5715.16 --> 5716.82]  and just like set it in the dash.
[5716.86 --> 5719.28]  I'm like, this is crazy, but you know, it just might work.
[5719.76 --> 5720.46]  I'm still for it.
[5720.46 --> 5721.68]  I think this is a good thing.
[5721.68 --> 5726.54]  I think worst case, in my opinion, is this a great place to begin.
[5727.22 --> 5729.36]  They'll probably have always this model.
[5729.42 --> 5730.40]  That's like, you know what?
[5730.46 --> 5731.32]  It's bare bones.
[5731.60 --> 5732.60]  It's the OG.
[5733.56 --> 5738.78]  It's just like ZSA and our friend, you know, with the Voyager, the original Ergodox, the
[5738.78 --> 5739.64]  keyboard kind of thing.
[5739.74 --> 5740.76]  Go back in the day.
[5740.82 --> 5742.48]  You've got the OG Ergodox, right?
[5742.94 --> 5745.16]  But here you've got this OG simplistic.
[5745.40 --> 5747.04]  Everybody can afford it for the most part.
[5747.04 --> 5752.62]  Like it's in the, if you're in a certain income bracket or below a certain income bracket,
[5752.68 --> 5757.20]  you can likely afford this thing and plug it into your 120 volt outlet.
[5757.38 --> 5758.04]  It's that accessible.
[5758.88 --> 5760.24]  You don't really need a radio.
[5760.76 --> 5762.06]  It's nice to have it.
[5762.10 --> 5762.66]  You don't need it.
[5762.88 --> 5764.16]  You don't really need power windows.
[5764.22 --> 5764.76]  It's nice to have it.
[5764.80 --> 5765.26]  You don't need it.
[5765.82 --> 5768.80]  You don't really need the dashboard and all this stuff to show you maps.
[5768.92 --> 5769.82]  You don't need it.
[5770.08 --> 5770.68]  You have a phone.
[5771.28 --> 5772.32]  It's nice to have.
[5773.16 --> 5773.26]  Right.
[5773.36 --> 5775.06]  I think this will spark something new for them.
[5775.06 --> 5778.74]  They will probably come out with slate, other slate versions of it.
[5779.04 --> 5779.52]  Yeah.
[5779.60 --> 5783.04]  But this will be a good, a good baseline to build from, I believe.
[5783.68 --> 5784.54]  I think so.
[5785.12 --> 5789.12]  And not that I'm a nationalist or U.S. only.
[5789.56 --> 5796.18]  One thing they say that is touching to me as an American forever is that on their about page,
[5796.24 --> 5801.90]  they say, we believe an American vehicle should be engineered and manufactured in America with slate.
[5801.90 --> 5804.88]  We're proud to bring manufacturing jobs back to the Midwest.
[5805.94 --> 5806.46]  And that's cool.
[5806.62 --> 5809.06]  I mean, I don't, I, I, I admire that.
[5809.24 --> 5811.32]  It's born in the USA, made in the USA.
[5812.16 --> 5812.96]  Cool, cool, cool.
[5813.08 --> 5814.98]  So Adam has reserved his.
[5815.70 --> 5816.22]  Mm-hmm.
[5816.80 --> 5818.12]  Is waiting to see what happens.
[5818.12 --> 5819.24]  He's not skeptical.
[5819.76 --> 5820.50]  I'm in the middle.
[5820.70 --> 5823.34]  I, uh, I think it's cool.
[5824.00 --> 5827.42]  I showed it to my wife and she's like, that's the, that does not fit into our life anywhere.
[5827.52 --> 5828.68]  Of course I got six kids.
[5828.68 --> 5831.90]  So I'm never going to drive anywhere with just me and one other person.
[5832.02 --> 5833.08]  And it's a two seater.
[5833.58 --> 5839.06]  And so as much as I think I like that form factor, I like the idea of a small truck because
[5839.06 --> 5843.32]  it's so useful, but you're also not like this big, massive thing on the, on the road.
[5844.04 --> 5845.50]  Uh, probably not.
[5845.62 --> 5846.46]  She's probably right.
[5846.46 --> 5851.50]  Even though, you know, under 20 K, why not grab a couple of them just for the, just for,
[5851.64 --> 5853.88]  just for giggles, you know, let's, I'll take two.
[5854.30 --> 5855.00]  I'll tell you one thing.
[5855.04 --> 5861.22]  It's the, it seems like a great first car for a son or a daughter, right?
[5861.74 --> 5867.16]  Like if it's roadworthy, safe, reliable, I would love to see the crush test on it.
[5867.18 --> 5867.70]  Things like that.
[5867.70 --> 5874.60]  Like where you, like if it, if it's safe for the person, but bare bones as a vehicle, that's
[5874.60 --> 5874.98]  great.
[5874.98 --> 5876.84]  I'd buy that for my son any day.
[5876.96 --> 5880.16]  In the verge, they asked about safety and they said they're shooting for a five-star
[5880.16 --> 5880.94]  safety rating.
[5881.24 --> 5883.74]  And then I thought to myself, who wouldn't shoot for a five-star?
[5884.06 --> 5885.58]  You know, like that's the baseline.
[5885.82 --> 5886.56]  We're going for three.
[5886.94 --> 5887.30]  Okay.
[5887.80 --> 5888.10]  Three.
[5888.10 --> 5889.12]  We're going for it.
[5889.62 --> 5889.98]  Yeah.
[5890.04 --> 5893.00]  So they're shooting for it, but yeah, I don't know.
[5893.14 --> 5893.68]  Carbon fiber.
[5893.94 --> 5894.24]  I don't know.
[5894.68 --> 5894.80]  Yeah.
[5894.80 --> 5895.86]  I'm glad you brought this up, man.
[5895.86 --> 5896.78]  This has been a fun conversation.
[5896.78 --> 5899.46]  I think, I think the world needs this slate.
[5901.32 --> 5901.68]  Dot auto.
[5901.88 --> 5902.38]  So cool.
[5902.46 --> 5903.72]  We should get them on the pod if they can.
[5903.82 --> 5904.96]  I mean, I'd love to talk to engineers.
[5904.98 --> 5905.94]  I'm not hearing anybody there.
[5906.74 --> 5906.98]  Yeah.
[5907.00 --> 5910.64]  If you know somebody, tell them to search Claude for us.
[5910.76 --> 5911.24]  We're first.
[5912.24 --> 5912.68]  There you go.
[5913.20 --> 5913.70]  All right, guys.
[5913.74 --> 5914.74]  Should we call it a show?
[5915.50 --> 5915.88]  That's it.
[5916.60 --> 5917.12]  That's it.
[5917.22 --> 5917.66]  That was awesome.
[5917.66 --> 5918.08]  That's it.
[5918.08 --> 5919.62]  Thanks so much for hanging out with us.
[5920.18 --> 5920.34]  Yeah.
[5920.42 --> 5921.38]  Good to see you again, man.
[5921.68 --> 5922.76]  Check out Resend, y'all.
[5922.90 --> 5927.86]  It's the best email service, according to all the LLMs.
[5928.46 --> 5928.98]  Bye, friends.
[5929.62 --> 5930.00]  Bye.
[5930.64 --> 5930.94]  See ya.
[5933.82 --> 5936.14]  That is Changelog for this week.
[5936.14 --> 5938.52]  Unless you are a Plus Plus member.
[5938.64 --> 5942.28]  In that case, we have a bonus for you right after this.
[5942.64 --> 5946.14]  Zeno updates Adam on the state of the Dracula theme.
[5946.14 --> 5951.84]  And if you're not a Changelog Plus Plus member, now's a good time to sign up, to ditch the ads,
[5952.18 --> 5958.46]  to get bonus content like this, to receive free stickers in the mail, and to directly support our work.
[5958.80 --> 5962.38]  Learn more about it at changelog.com slash plus plus.
[5962.38 --> 5969.36]  Thanks once again to our partners at fly.io, to our sponsors of this episode, Heroku and Depot,
[5969.80 --> 5974.56]  and to our mysterious friend, Breakmaster Cylinder, for these dope beats.
[5975.06 --> 5980.70]  Oh, and did you know, BMC will be joining us on Friends for a game of Pound to Find.
[5981.16 --> 5982.64]  Get excited for that one.
[5982.88 --> 5983.52]  I know I am.
[5983.52 --> 5986.32]  Next week on the Changelog.
[5986.68 --> 5987.44]  News on Monday.
[5987.80 --> 5990.20]  Nathan Sobo from Zed on Wednesday.
[5990.80 --> 5995.00]  And Gerhard Lazu returns for Kaizen 19 on Friday.
[5995.38 --> 5996.48]  Have a great weekend.
[5996.96 --> 6000.16]  Send the Changelog to your friends, who might dig it.
[6000.68 --> 6002.54]  And let's talk again real soon.
[6008.54 --> 6009.62]  Game on.
