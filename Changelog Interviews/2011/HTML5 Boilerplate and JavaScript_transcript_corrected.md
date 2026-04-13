[0.00 → 2.66] This week's show is brought to you by Paste Interactive.
[3.20 → 6.16] Paste Interactive makes apps that help people perfect their lives.
[6.76 → 9.82] They create a jump chart for wiring content into websites,
[10.54 → 12.18] Station for staying on task together,
[12.64 → 15.26] and Paprika for tracking your text and to-dos.
[15.98 → 18.36] Check out Paste at pasteinteractive.com.
[19.08 → 19.96] And by Gobble.
[20.48 → 22.34] Gobble has a job opening I want to let you know about.
[22.82 → 26.52] At Gobble, you can write code that feeds people, learn a lot, and deploy every day.
[26.84 → 29.50] Gobble.com connects people with neighbourhood chefs,
[30.00 → 33.18] and the engineering team at Gobble is looking to hire programmers
[33.18 → 37.54] that are dedicated to good code, learning, and skill sharing with each other.
[37.84 → 40.64] They achieve continual learning through weekly retrospectives,
[41.12 → 43.44] code review, and the occasional pairing session.
[43.92 → 49.02] If Rails, Spec, Tamil, SAS, and jQuery strike your fancy, apply today.
[49.60 → 51.58] Gobble is located in Palo Alto, California,
[52.02 → 54.48] and they're open to relocating people from around the country.
[60.00 → 61.50] Gobble is located in Palo Alto, California, and the other.
[61.50 → 73.00] Welcome to the Changelog episode 0.6.7.
[73.10 → 74.06] I'm Adam Stachowiak.
[74.44 → 75.32] And I'm Wynne Evelin.
[75.46 → 76.52] This is the Changelog.
[76.54 → 78.30] We cover what's fresh and new and open source.
[78.64 → 81.84] If you found us on iTunes, we're also on the web at thechangelog.com.
[81.92 → 82.98] We're also up on GitHub.
[82.98 → 85.72] And if you head to GitHub.com slash explore,
[85.82 → 88.68] you'll find some trending repos, some feature repos from our blog,
[88.76 → 90.06] as well as our audio podcast.
[90.44 → 93.30] And if you're on Twitter, follow Changelog Show and me, Adam Stack.
[93.84 → 96.32] And I'm Penguin, P-E-N-G-W-Y-N-N.
[97.26 → 98.00] Fun episode this week.
[98.08 → 102.56] Talk to Paul Irish over at Google about HTML5 and other stuff.
[102.98 → 104.12] Other stuff for sure.
[104.62 → 108.52] We're a couple of fanboys since we, I guess, talk about this stuff all the time.
[108.66 → 110.56] You perked up a bit on this episode.
[111.12 → 113.32] It's actually, you know, a lot of the shows.
[113.42 → 114.84] I mean, RVM, I get that, right?
[114.94 → 117.10] But you go to BDSM, and I'm lost.
[117.26 → 121.66] And thank God for Steve to come on that show because that wouldn't have been my place.
[121.82 → 123.60] But shows like this I can have fun with.
[124.02 → 124.74] For sure.
[125.14 → 125.76] I had a week off.
[125.86 → 130.00] We took a week down at Lone Star Rubicon down in Austin.
[130.10 → 132.74] Got to meet our buddy Steve Flank face-to-face.
[132.74 → 135.44] He brought the house down with his talk on shoes
[135.44 → 139.64] and how we need to support those that give to open source,
[139.64 → 142.50] like Wayne and some others that we've had on the show recently
[142.50 → 146.68] that have just poured out their blood, sweat, and tears into apps that we use every day
[146.68 → 150.60] and just give props to folks that make our lives easier.
[150.70 → 152.48] And I think that's what we're trying to do here on The Change Log
[152.48 → 156.68] is just shined a light on folks that are giving away software.
[157.00 → 157.36] That's right.
[157.42 → 161.16] Shine the spotlight on the people that are moving and shaking this world.
[161.72 → 162.16] Absolutely.
[163.20 → 165.26] Back to the web this week with Paul.
[165.26 → 168.90] But if you've got other ideas for who we should have on the show, let us know.
[169.32 → 171.38] Hope to get some NoSQL on the show soon.
[171.60 → 175.40] And I'm trying to track down the folks behind TMUX
[175.40 → 178.82] and some of the other command line goodies that you and I have gotten into lately.
[178.96 → 180.78] So hopefully we'll switch gears a bit.
[180.98 → 183.72] That little session we had today in the terminal was pretty fun.
[183.82 → 185.06] So that would be a fun conversation.
[185.42 → 186.98] I wowed you with the TMUX, didn't I?
[187.22 → 187.70] You did.
[188.52 → 189.28] Fun episode this week.
[189.32 → 189.84] Should we get to it?
[190.18 → 190.72] Let's do it.
[190.72 → 191.22] Let's do it.
[199.78 → 202.66] Chatting today with Paul Irish from Google.
[202.82 → 204.08] So Paul, for those that don't know you,
[204.12 → 206.62] why don't you introduce yourself a little bit about your role over there?
[206.96 → 207.14] Sure.
[207.80 → 211.92] So I'm on the Google Chrome Developer Relations team.
[212.64 → 220.70] And essentially what I do on my team is I engage with the wider web developer community
[220.70 → 224.62] and make sure that everyone knows kind of what's capable,
[225.18 → 226.56] what are the capabilities of browsers,
[226.74 → 229.12] like what are the features inside there, what you can get away with,
[229.16 → 235.34] and basically like what can we do to make really like engaging, compelling experiences.
[235.76 → 240.54] And then I also publish a lot of tutorials, guides, screencasts,
[240.54 → 246.46] and software to help people do that kind of stuff and do it well.
[247.10 → 249.36] So that's kind of pretty much what I do.
[249.76 → 251.46] I got a glimpse of that at Southwest.
[251.68 → 255.80] I guess you had the Google event down there where you're doing some demos up on stage.
[256.48 → 257.00] Yeah, totally.
[257.32 → 264.48] Yeah, I got to talk about, give a brief overview of the HML5 Umbrellas feature set
[264.48 → 268.66] and then also talked a little bit about some of the newer features in the Chrome developer tools.
[269.70 → 269.84] Yeah.
[270.20 → 273.40] You might be the best person to define this.
[273.40 → 276.26] No, we'll stop hogging the mic in a second when Adam asked a question.
[276.42 → 278.22] But HTML5, what's it mean to you?
[278.74 → 278.96] Ah.
[279.92 → 282.80] Uh, uh, ooh, uh.
[284.96 → 289.78] Alex, so I think like Dion Meyer said that it was,
[290.36 → 295.06] HTML5 is everything after HTML4, which is nice.
[295.06 → 301.36] It's, I, in general, like, the I'm not too pedantic when it comes to the definition of HTML5.
[301.44 → 303.44] I certainly don't think that it's what's in the spec.
[303.94 → 311.82] Um, I'm fine with clarifying that CSS3 is not HTML5, but it's really hard to make a HTML5 demo without using CSS3,
[311.88 → 313.02] because you want it to look good.
[313.08 → 320.16] Like, you're not going to release something with, with web sockets and, uh, and, uh, local storage and not make it look good.
[320.16 → 323.20] So, anyway, they, they all kind of get mixed up, and I think that's okay.
[323.50 → 329.98] Um, HTML5 is the term that kind of, like, carries the flag and has the logo and, like, and that's what all the excitement is about.
[330.10 → 340.16] And sure, it's a little bit messy, but I don't think it's, like, it's very harmful that we use the term HTML5 to mean things that are not technically HTML5.
[340.16 → 344.78] HTML5, I, so, I, I'm pretty fine with an ambiguous definition there.
[345.16 → 349.22] I'm curious how, well, HTML5, you know, has that military stripe logo.
[349.58 → 351.12] The CSS3 is like Air Force.
[351.48 → 351.70] Yeah.
[351.70 → 352.68] Like, the Army and the Air Force.
[352.72 → 353.24] What's that about?
[353.40 → 354.38] I don't, I don't know.
[354.46 → 356.08] You know, I actually saw, where was it?
[356.16 → 364.58] I saw someone made a new, uh, CSS3 logo, and they took kind of, like, the typography of the five,
[364.58 → 369.44] and then made a three out of it and put it on, like, a blue badge instead of an orange badge,
[369.46 → 371.12] and it actually looked really, perfect.
[371.88 → 374.20] Um, I don't know what the iconography is about.
[374.54 → 377.68] Uh, I don't, I, I, I like the HTML5 logo.
[377.88 → 382.38] The other, those other smaller icons, I don't really have much of a use for myself.
[383.00 → 384.56] Um, so, whatever.
[386.14 → 389.86] When you're quoting Dion, I thought you were going with, um, the quote that he said,
[389.90 → 392.04] HTML5's a jewel that we need to cut into a weapon.
[392.34 → 393.22] Oh, yeah, yeah.
[393.22 → 396.68] Uh, yeah, it's, uh, it's Yehuda Katz's, uh, Twitter bio.
[396.88 → 403.76] It's, uh, HTML5 is the, the gem that we need to cut in, or, yeah, yeah, yeah, yeah, it is, um,
[404.28 → 406.12] the gem that we need to cut into a weapon.
[406.50 → 414.54] Um, but I agree, like, uh, I think a lot of us, uh, a lot of developers are, are really engaged,
[414.54 → 417.22] uh, and really excited about the web platform.
[417.22 → 425.32] And I think, um, I think it's important that we make the web platform be, uh, competitive
[425.32 → 430.46] with what people are doing on native mobile platforms.
[430.84 → 437.06] Um, and, you know, I hate it when people think that native apps look and feel better than what
[437.06 → 437.98] we can do with web apps.
[437.98 → 440.38] I think that's like, that sucks.
[440.94 → 441.62] That does suck.
[441.62 → 448.10] And I, I think that, um, you know, web apps, certainly a lot of people, you know, are
[448.10 → 449.48] completely delighted by web apps.
[449.48 → 452.98] And so it's terrible when you hear things like that, because in general, I think that
[452.98 → 457.30] not only have people experienced web apps that are, that have kind of changed their,
[457.42 → 463.52] their view of what you can do in a browser, but, um, but the capabilities, uh, that someone
[463.52 → 464.78] might not even know are there.
[464.78 → 469.26] Like I, I was talking to one of my old friends, and she was like, yeah, I'm thinking of making
[469.26 → 471.56] an app, uh, an iPhone app.
[471.58 → 472.44] And I was like, why?
[472.58 → 476.28] And she's like, well, it's going to be like a to-do list, something, something, but I want
[476.28 → 478.34] it to work when, when I'm not connected.
[478.74 → 482.66] And I was like, well, it turns out you can make a web app that works when you're not connected.
[482.70 → 483.52] And she's like, really?
[483.66 → 484.84] I was like, yeah.
[484.98 → 490.64] Like it might seem weird that you would open up mobile Safari on your iPhone to access a web
[490.64 → 491.94] app, even though you're not connected.
[491.94 → 498.08] Like I can understand the cognitive, uh, disconnect there, but, uh, but there's certainly capability
[498.08 → 502.02] that, um, that we're not kind of exploring as developers right now.
[502.22 → 507.70] Well, the, the browser certainly expanded to do far more than I think the very first iteration
[507.70 → 509.22] of it was intended to do.
[509.88 → 515.12] So it just makes sense that as the web progresses and as technology progresses and as the backend
[515.12 → 520.10] meets the front end and all these things start to collide as we go into this newer space
[520.10 → 524.96] of the web and how it's morphing from app to web app to you name it, um, that the, the
[524.96 → 527.44] browsers catch up and allow for a more native experience.
[527.96 → 528.36] Yeah.
[528.72 → 528.98] Yeah.
[529.38 → 533.66] And I, and I think it's actually like interesting, you know, GitHub is a really actually interesting
[533.66 → 540.06] example because there are conversations around, uh, websites versus web apps and GitHub is
[540.06 → 545.52] like, it's like half-and-half, you know, they were the first to really make use of HTML5 history
[545.52 → 549.76] and push state to, to do the cool URL rewriting with a state change and the transition looks
[549.76 → 552.80] perfect, works extremely well, um, falls back.
[552.80 → 556.74] It's like the most progressively enhancement D friendly thing ever.
[557.52 → 564.34] Um, and it works, but like, I don't want to call GitHub an app because it's not just like
[564.34 → 565.30] a single page app.
[565.30 → 568.84] Like there are certainly pages, but it's not just a straight-up site.
[568.84 → 572.06] Like they, they, it's almost like a hybrid, but I don't want to call it a hybrid.
[572.14 → 575.66] It just like delivers a good user experience and like, that's what they're focused on.
[575.66 → 581.66] So like making a good user experience is more important to them than qualifying, uh, their
[581.66 → 583.54] product as an app, which I think is rad.
[583.90 → 584.26] Yeah.
[584.32 → 587.88] Not to go too deep on GitHub and glorifying those guys because they are awesome.
[587.98 → 591.94] We did, we do know that, but I about did two backflips yesterday when I realized I couldn't,
[592.02 → 594.68] I could push what's the key win E to go into the editor.
[594.68 → 595.44] Right.
[595.56 → 598.54] You know, I was like, wow, that is just insanely sexy.
[598.68 → 603.44] And there are many times I want to just edit a read me and, or just do a one simple commit
[603.44 → 604.20] to help somebody out.
[604.60 → 609.82] And you either don't do it because you don't want to pull the repo down and do the change
[609.82 → 615.08] and push it back up and do the whole, you know, terminal slash push scenario.
[615.08 → 617.48] Then you got to just in the web browser, just sexy.
[617.58 → 618.24] It's just awesome.
[618.46 → 623.40] But, um, Paul, I think you're probably most known for, or at least that's what I knew you
[623.40 → 625.66] for it first was, uh, HTML5 boilerplate.
[625.76 → 627.36] What's the story behind that, and how did it come about?
[628.14 → 628.30] Sure.
[628.82 → 638.18] Uh, well, so before I was here at Google, I, uh, worked at an interactive agency, um, in
[638.18 → 639.58] Boston, it's called ISO bar.
[639.58 → 648.48] And, uh, it is, we, we made web apps and websites for everyone, uh, for Nike and Nikon and Reebok
[648.48 → 649.12] and things like that.
[649.12 → 653.50] And I, you know, over the course of making a number of different web projects, I realized
[653.50 → 659.06] that I was always taking, uh, clever snippets of code from old projects and then bringing
[659.06 → 659.96] it into new ones.
[659.96 → 665.06] And so I just started kind of developing, uh, uh, a little template of files of HTML and
[665.06 → 672.70] CSS and JavaScript that made a lot of sense to just like use as a default, um, kept on
[672.70 → 673.34] growing that.
[673.60 → 678.40] Uh, and we kind of made it the default way that we, uh, built sites inside the agency.
[679.08 → 686.48] Um, and then, uh, I was like, I decided that we should probably, you know, share that externally.
[686.48 → 693.52] Um, for a while it was called front end, no pro front end, pro front end template, I think.
[694.10 → 698.94] Um, which is very accurate, but I didn't feel it had a perfect name.
[699.38 → 702.42] And so I was trying to find a new name, HTML5 boilerplate.
[703.26 → 705.74] Because it was like somewhat HTML5y though.
[705.76 → 708.50] It's mostly like a front end developers thing.
[708.52 → 714.96] It's not specific to HTML5, and it's certainly not boilerplate as far as like the, the definition
[714.96 → 716.56] of boilerplate code goes.
[716.72 → 721.18] Like it's not the minimal, uh, amount that you need, but it works.
[721.46 → 723.42] Um, it's a reference library more or less, right?
[723.62 → 726.16] I mean, I, well, so I'm fine.
[726.18 → 727.78] Like I think it works really well.
[727.82 → 733.36] And, and the idea is that it's not too codependent on, on each other, and you're completely free
[733.36 → 734.58] to like to pull things out of it.
[734.86 → 739.32] Um, it's documented well enough so that you can feel comfortable, um, pulling parts.
[739.32 → 745.98] But, um, but I think it works really well just like as, as grabbing, uh, the whole boilerplate,
[745.98 → 751.82] um, and, and deleting a few things that you might not be too keen on and just using it,
[751.82 → 752.70] uh, from the start.
[752.96 → 756.98] You know, I think the important thing is to understand what you're pulling and what you're
[756.98 → 758.60] leading as developers.
[758.60 → 762.26] I think we are more prone than any other profession to cargo cult.
[762.50 → 763.44] Yeah, totally.
[763.62 → 767.98] Like, yeah, there are plenty of things that have just like been kind of good practice or the
[767.98 → 770.62] thing you do, uh, or the thing you don't do.
[770.80 → 773.82] And, and a lot of times we don't really understand why.
[774.76 → 780.90] Um, so yeah, it's interesting because H1F boilerplate, you know, I, I created it and I released
[780.90 → 783.42] it as a way to save people time when starting a new project.
[784.08 → 790.06] And, um, and what it ended up, uh, also having effect on is, is more of like an educational
[790.06 → 790.40] thing.
[790.40 → 794.94] There are a lot of techniques in there that, um, uh, a lot of people have worked on refined
[794.94 → 798.26] and, uh, and, and are smart.
[798.26 → 804.06] And we, we made sure to keep things documented well enough so that you understand it.
[804.14 → 809.20] You can go and find the links, uh, about it, read more and figure out, like, understand
[809.20 → 811.98] the, the justification why you would want to do something like this.
[812.32 → 816.46] So H2F boilerplate, you know, it's, it's this thing you can kind of pull things from,
[816.56 → 820.28] but at the same time, you've got some other kind of cool little niceties that, that fall
[820.28 → 820.78] in there as well.
[820.78 → 824.72] You're using respond JS in there and something that I thought was kind of cool too, because
[824.72 → 829.94] I've been using a reset for a number of years now, but, um, when I kind of bash brains of
[829.94 → 834.60] the day, and we're like, why do we keep resetting our CSS to this complete reset?
[834.80 → 836.82] But then we have to go back in and add bold for certain things.
[836.96 → 840.12] So you also brought in normalized CSS for that as well.
[840.16 → 844.26] What was, how, how long has normalized been in the HTML5 boilerplate?
[844.98 → 849.82] Uh, it's only been shipping, uh, with, uh, boilerplate for the last, I don't know,
[849.82 → 854.18] what was it three weeks, I think three weeks ago is when we, when we shipped 2.0 boilerplate.
[854.82 → 859.78] Um, but it was in GitHub for the last, uh, four or five months.
[860.08 → 861.32] How did you find out about it?
[861.94 → 869.36] Well, uh, so the, the long story about it was that, you know, people have doing, been
[869.36 → 870.50] doing resets for a long time.
[870.50 → 875.40] Um, and the first time I started using resets, I was really keen on it.
[875.44 → 882.60] And my, the number of, um, edge case bugs that popped up in only one browser that dropped
[882.60 → 885.34] to zero so quick when I started using resets.
[885.34 → 890.58] And I just like, I really knew that this was a lot better than, um, than not resetting
[890.58 → 890.94] at all.
[890.94 → 895.46] Um, but as time went on, then you realize, you know, it is kind of annoying that we have
[895.46 → 901.90] to, uh, put font weight, uh, bold on our bees and our strong all over again and our headlines.
[901.90 → 906.64] And it's like, this is kind of silly that we're like bulldoze ring everything, building
[906.64 → 907.44] it all back up.
[907.88 → 914.44] And so the of course the, the better approach and what's at the foundation of normalize
[914.44 → 919.02] is only changed the things that are different and make sure that they're the same.
[919.02 → 926.00] But what that means is that you need to take inventory of the default way that every browser
[926.00 → 933.62] styles their, uh, elements by default and, uh, and then change them accordingly.
[933.62 → 935.86] And so that requires quite a bit of research.
[936.10 → 942.46] Um, uh, WebKit and, and Gecko since they're open source, you can just go and find their default
[942.46 → 943.62] user agent style sheet.
[943.74 → 946.98] But for IE, uh, it takes a little bit more work and same with Opera.
[946.98 → 955.36] So, um, Jonathan Neal, who, uh, who actually does the music for the Acre podcast, um, but
[955.36 → 957.26] he's also a really talented front end developer.
[957.72 → 961.68] Uh, he, uh, started digging into this.
[961.76 → 962.56] He did a lot of the research.
[962.56 → 969.14] If you go to IECSS.com, you can see the default style sheets of, uh, the IE browsers and also
[969.14 → 970.34] the other browsers as well.
[970.34 → 976.98] Um, and then, uh, Nicholas Gallagher, who's a, uh, London based developer started digging
[976.98 → 977.94] into this as well.
[978.02 → 980.28] So it was a collaboration, uh, between the two of them at start.
[980.44 → 985.50] And then Nicholas took it on, uh, as his own project later on.
[985.90 → 990.50] Um, and so it's basically, yeah, it's, it's finding out the differences between the user
[990.50 → 992.56] agent style sheets only changing what you need to.
[992.56 → 1000.52] Um, at the end of the day, you get a, uh, uh, style, styling file that is smaller than
[1000.52 → 1000.96] a reset.
[1001.56 → 1008.50] Um, plus, uh, because you don't have to, uh, re you know, build all that styles back up.
[1009.00 → 1012.22] And, uh, and it also feels a lot nicer.
[1012.76 → 1019.50] Um, I think, I think people are, we're kind of getting tired of, of feeling so redundant
[1019.50 → 1022.46] in, uh, the reset approach of styling.
[1022.86 → 1027.48] Well, I, I'm sad because I was just so close to being almost as famous as you because I
[1027.48 → 1029.30] was just about the release on reset.
[1029.68 → 1030.26] Oh yeah.
[1030.44 → 1030.74] Yeah.
[1031.62 → 1035.30] That's a joke to like, you know, reset it.
[1035.32 → 1037.56] And then there's a separate project to unrest it.
[1037.62 → 1039.76] I was, cause that's what I was doing every time I was going crazy.
[1039.76 → 1043.82] Every time I would reset this, our styles for a new project, I'd be like, I'm putting
[1043.82 → 1046.36] bolds and all these other things that you really do want.
[1046.92 → 1049.38] But yeah, you know, I was so close.
[1049.84 → 1055.06] It's like, its Yahoo had the, uh, Yahoo had a reset, and they had a base dot CSS, which
[1055.06 → 1056.72] was basically an unrest.
[1057.12 → 1062.62] And, um, and it's funny because it's like, it duplicates all, uh, all the effort that
[1062.62 → 1063.88] the user agent style sheet already does.
[1064.14 → 1069.06] The thing that I actually like most about the project, uh, is that now when you're looking
[1069.06 → 1073.46] inside Chrome dev tools or firebug, and you like select, you know, an H one or whatever,
[1073.46 → 1080.88] or, or a P tag, there's not this enormous list of, um, of cascading rules that all got overridden
[1080.88 → 1081.92] and things like that.
[1081.92 → 1083.98] Like it's just going back.
[1083.98 → 1088.44] Like there's maybe two styles that are inherited that you see on the right-hand pane and that's
[1088.44 → 1091.40] it, which makes for a much more like cleaner developer experience.
[1091.48 → 1091.94] I like that.
[1091.94 → 1098.66] And I guess probably the next thing that comes along with HTML5 bullet plate is, is modernizer.
[1098.66 → 1105.14] And that is such a cool project that I don't think I fully understand and or tap into.
[1105.22 → 1108.76] And I'm not really sure why, but I think Adobe has done something pretty cool with it recently.
[1108.76 → 1111.04] But how did a modernizer come about?
[1111.92 → 1113.36] Um, it's funny.
[1113.44 → 1122.34] Modernizer, uh, so I work on it with Farouk, Ates and Alex Sexton and Farouk launched it,
[1122.46 → 1125.38] uh, maybe two years ago or three years ago.
[1125.48 → 1126.00] I'm not sure.
[1126.00 → 1131.52] Uh, and I remember when it came out, and I was like, um, I don't know, it just has a
[1131.52 → 1134.02] pink website, and it says it modernizes.
[1134.16 → 1136.04] And I was like, all right, sounds cool.
[1136.64 → 1137.08] Whatever.
[1137.54 → 1142.12] And then like two months later I was, I was doing some, some work with some CSS three and
[1142.12 → 1146.68] I was probably like doing something with a box shadow and I put a box shadow on.
[1146.72 → 1151.60] And then I was like thinking about what happens when I'm in a browser that doesn't have native,
[1151.74 → 1153.30] native box shadow support.
[1153.30 → 1156.66] And I probably actually want to do something a little bit differently.
[1157.26 → 1159.26] And I was like, Hmm, how to do this?
[1159.32 → 1162.20] I wonder if like I could use JavaScript to like figure that out.
[1162.30 → 1165.24] And then I like went back, and I looked at the modernizer side.
[1165.32 → 1167.92] I was like, Oh, it does exactly that.
[1168.02 → 1169.32] And I was like, cool.
[1169.32 → 1174.70] And then, and then I, I looked at the JavaScript behind it, and I was like, Oh, this is terrible.
[1174.96 → 1176.02] This is no.
[1176.92 → 1182.64] And then, so me and my friend Ben Allman, we rewrote the entire thing, um, and told Farouk
[1182.64 → 1183.84] and he's like, Oh, cool.
[1183.92 → 1184.20] Okay.
[1184.28 → 1188.96] And then, so then I joined the project, uh, after telling him that his code was terrible.
[1188.96 → 1191.76] Um, but now, yeah, it's perfect.
[1191.86 → 1198.08] So modernizer basically detects all these sorts of CSS three things and lets you kind of style
[1198.08 → 1199.74] the page differently if you're, if it's not there.
[1199.92 → 1205.72] And it also does a really robust detection of all sorts of HTML5 and other features that
[1205.72 → 1207.10] you want to know that are there.
[1207.10 → 1208.70] And it gets tricky.
[1208.94 → 1216.36] Like, um, user agent sniffing gets a really, uh, bad rap and much of that is deserved.
[1216.76 → 1220.70] But one of the trickiest parts, I mean, one of the worst parts about user agent sniffing
[1220.70 → 1222.30] is because everyone does it their own way.
[1222.94 → 1228.56] And, um, and a lot of times when you do things your own way, you do it wrong the first time
[1228.56 → 1229.58] and the second time.
[1230.28 → 1234.56] And, uh, with feature detection, it's, it's, it can also be quite similar.
[1234.56 → 1238.38] Um, a lot of times writing your own feature detects, you're going to do it the wrong way.
[1238.56 → 1241.22] Um, like detecting for HTML5 forms.
[1241.46 → 1245.38] Um, a lot of the published techniques for that are flawed at this point.
[1245.92 → 1250.52] Um, and so modernizer is kind of the clearing house for feature detects.
[1250.52 → 1257.76] And we make sure that our detects work across everywhere that we can, um, and tackle all sorts
[1257.76 → 1263.06] of edge case bugs that pop up in like, uh, there's a really nasty one in IE8 that runs
[1263.06 → 1271.78] on Windows server 2000, uh, without the media, the entertainment media service pack installed.
[1272.74 → 1274.22] You'll get, you'll get an exception.
[1274.54 → 1280.10] If you look for a, uh, audio elements can play type function, it'll just like blow up
[1280.10 → 1280.68] in your face.
[1280.80 → 1283.40] You know, we've been using modernizer in the changelog for a while.
[1283.40 → 1287.32] And when we first, uh, put it on there, we were getting a lot of complaints about it.
[1287.32 → 1289.84] Uh, trying to test for local storage.
[1290.12 → 1290.72] Ah, yeah.
[1290.72 → 1290.88] Yeah.
[1290.88 → 1291.66] You guys have tweaked that.
[1292.04 → 1294.98] Yeah, that, yeah, we changed, uh, we changed that.
[1295.08 → 1301.94] There was a, um, uh, there was a Safari setting, uh, that, well, there are two ones.
[1302.00 → 1304.46] There's, there's one, a, a Firefox problem.
[1304.82 → 1307.24] If you have your security settings really high.
[1307.56 → 1309.04] Um, and we nerfed that.
[1309.04 → 1312.44] And then there was also a Safari preference where if you change your preferences, then it
[1312.44 → 1318.34] always asks you if, if you, uh, if this thing can use your local storage, and you have to
[1318.34 → 1319.20] say yes.
[1319.34 → 1323.10] And that's equivalent to like, okay, in every single cookie that gets placed on your browser.
[1323.10 → 1330.44] So I don't know, but the cool thing now with modernizer is that there is no default production
[1330.44 → 1331.30] ready version.
[1331.30 → 1335.36] It's like, you know, jQuery has the, the new minified version.
[1335.48 → 1336.46] You grab that you're good.
[1336.88 → 1339.30] Um, there's nothing like that for modernizer.
[1339.30 → 1345.84] So with modernizer two, which we put out a few months ago, your build will be custom.
[1346.02 → 1348.06] You select only the features that you want to detect.
[1348.28 → 1351.48] Uh, we make the spot, the file as small as it can be.
[1352.00 → 1357.36] Um, and so it goes as fast as it can and the files, uh, really tiny.
[1357.36 → 1361.54] So, uh, I really liked that method of kind of distribution for now.
[1361.66 → 1365.42] Just curious if you've seen a rack modernizer from Marshall, you're a friend of the show.
[1365.84 → 1366.24] Yeah.
[1366.24 → 1369.28] Uh, yeah, I, there, there's actually, um, I think it's a lot of, uh,
[1369.30 → 1374.98] I think there's three total, um, projects that, that take modernizer and kind of enable
[1374.98 → 1376.64] that visibility on the server side.
[1376.84 → 1379.30] And I think that's a, I think that's a really cool approach.
[1379.42 → 1384.26] It's like the old browse caps, except not doing a user agent sniffing and feature detection.
[1384.40 → 1384.60] Yeah.
[1384.72 → 1384.94] Yeah.
[1384.94 → 1386.10] I really like that.
[1386.16 → 1387.44] I think that's really a wise way.
[1387.52 → 1390.80] Um, you have a lot more control, so you don't have to rely on JavaScript to, to manage
[1390.80 → 1391.58] everything for you.
[1391.80 → 1392.56] That's really cool.
[1392.56 → 1397.22] I think the first time that I came across, uh, your name in a memorable way, I'm sure
[1397.22 → 1402.72] passed across before that was, uh, did you coin the term Out or did you?
[1402.96 → 1403.32] Yeah.
[1403.52 → 1403.98] Yeah, I did.
[1404.90 → 1406.16] Flash of unstyled text.
[1406.30 → 1406.88] Yeah, totally.
[1407.28 → 1411.24] Um, that I got, I got really into web fonts a few years ago.
[1411.24 → 1420.48] And, um, and at the time the, the behaviour for web fonts in Firefox was, uh, to, um, that
[1420.48 → 1427.64] you would get a default, you would get a like Ariel or Times New Roman or something font.
[1427.80 → 1432.14] And then the web font would download, and then you would get the new upgraded font.
[1432.32 → 1437.68] And there was that little flash of going from the regular boring font to the new font.
[1437.92 → 1439.38] And a lot of people hated that.
[1439.38 → 1443.48] And a lot of people actually prefer that because the web kit behaviour is that it's all invisible
[1443.48 → 1444.70] and then you get the new one.
[1445.54 → 1450.76] Um, what's really cool is that there, so there were a lot of conversations around this because
[1450.76 → 1452.18] people felt strongly in different ways.
[1452.18 → 1456.14] And so now, uh, moving forward, there's a new kind of hybrid approach.
[1456.70 → 1464.00] Uh, so what was adopted in Firefox, this shipped in Firefox four, um, and we'll actually be landing
[1464.00 → 1469.36] as a, as a modification to the, to the behaviour and web kit soon is, uh, the text is
[1469.36 → 1471.06] invisible for three seconds.
[1471.52 → 1475.44] And after three seconds, if that web font has still not downloaded, then it goes back
[1475.44 → 1479.60] and it goes to the fallback font and then eventually to the web font whenever that's ready.
[1480.26 → 1485.42] Um, but so it's like invisible up to a certain threshold, and then you're like, okay, I actually
[1485.42 → 1487.08] want to read the text on this website.
[1487.08 → 1488.16] It finally gives it to you.
[1488.64 → 1490.64] Um, and so you're, you're pretty much covered.
[1491.16 → 1493.46] Uh, so that's kind of where things are going.
[1493.46 → 1499.58] Um, I'm convinced that the, uh, the CSS three spec is kept, uh, JavaScript developers employed
[1499.58 → 1500.84] more than anybody else.
[1500.84 → 1506.28] You know, we have the, uh, Google font loader, um, that can load fonts, both from Google font
[1506.28 → 1510.74] directory or your own or type kit does some of that as well.
[1510.74 → 1514.14] If you need a polyfill for, uh, your other browser.
[1514.14 → 1518.56] So speaking of polyfills, um, are they, is the universe growing or shrinking?
[1518.68 → 1519.54] Are we needing these less?
[1519.54 → 1521.66] Or are we finding more ways that we need these things?
[1522.12 → 1526.80] Uh, more, probably more like I just saw yesterday.
[1526.80 → 1527.74] Uh, what is that?
[1527.96 → 1529.64] It's IE webgl.com.
[1529.78 → 1538.32] It's a plugin that, uh, enables the use of web GL content in IE, uh, which is pretty cool.
[1538.32 → 1540.02] And apparently their performance is really great.
[1540.44 → 1545.20] Um, although thinking about it, like if you're going to have your user, your IE user install
[1545.20 → 1549.52] a plugin, uh, to view your web GL content, you might as well make that plugin Chrome
[1549.52 → 1554.16] frame so that it's so that they get all the other benefits beyond just web GL.
[1554.50 → 1559.22] But I think, you know, to be honest, so I maintain this list of polyfills on the modernizer
[1559.22 → 1566.36] wiki and a lot of stuff comes in there, um, that give you functionality of HTML5 stuff and
[1566.36 → 1567.20] CSS3 stuff.
[1567.86 → 1569.50] Um, a lot of it's really cool.
[1569.50 → 1576.30] Uh, like I, I like using, um, input type equals range polyfills so that I get a slider in Firefox
[1576.30 → 1578.52] instead of, uh, a not a slider.
[1579.80 → 1586.24] Um, but the polyfills that I use the most are actually, uh, ECMAScript polyfills.
[1586.24 → 1594.06] So I really like, uh, function prototype bind and I like, um, my array extras and I like
[1594.06 → 1596.78] object. Keys, um, and things like that.
[1596.88 → 1603.10] I ended up using those, uh, polyfills quite a bit, uh, more, probably a considerable amount
[1603.10 → 1607.02] more than the, than the more robust HTML5 and CSS3 ones.
[1607.02 → 1610.00] You mentioned the, uh, input type range I've found lately.
[1610.00 → 1614.06] I've had to adjust CSS selectors when doing forms and things used to, you could just get
[1614.06 → 1615.78] by with the input type text and a text area.
[1615.78 → 1620.66] Now it seems like you need to select anything that has a type and then opt out of input type
[1620.66 → 1623.08] button or, or, uh, submit or reset.
[1623.28 → 1625.20] Cause there's just a growing number of those now.
[1625.62 → 1625.82] Yeah.
[1625.92 → 1626.14] Yeah.
[1626.24 → 1627.70] Styling form controls is really tough.
[1627.70 → 1632.00] And I mean, that's styling form controls is the reason that, uh, because it is so tough.
[1632.10 → 1636.90] That's the reason that, that Mozilla has not yet, um, implemented some of the
[1636.90 → 1641.54] new form types is because they want to make sure that, that you have the ability to make
[1641.54 → 1643.14] those look like you want.
[1643.72 → 1648.72] Um, and so once they figure that out, then we'll be seeing, uh, a few more of those coming
[1648.72 → 1649.36] into Firefox.
[1649.86 → 1656.16] So prior to moving to Google, were you a, uh, a WebKit guy or a Firefox firebug guy?
[1656.68 → 1659.24] Um, I both.
[1659.68 → 1661.46] What's the biggest jump moving?
[1661.68 → 1663.56] I'm assuming at some point you were a firebug.
[1663.56 → 1670.14] Like most of us started out moving from firebug is your everyday, um, development tool to,
[1670.20 → 1670.78] uh, to WebKit.
[1670.84 → 1673.04] I'm assuming your camped out in Chrome for the most part now.
[1673.14 → 1673.36] Yeah.
[1673.42 → 1673.64] Yeah.
[1673.64 → 1676.04] I was, I was an enormous firebug advocate.
[1676.04 → 1679.88] Um, I gave presentations on how to use firebug more effectively.
[1680.12 → 1687.10] And, um, I collected every single like tutorial, uh, that was ever posted on, on firebug online.
[1687.10 → 1688.62] I was like all about it.
[1688.62 → 1693.58] Um, because like, to be honest, everyone, there were a lot of features that people didn't
[1693.58 → 1696.22] know about in firebug, and it was incredibly powerful.
[1696.54 → 1699.68] Um, even like three years ago when I was, when I was all into it.
[1700.18 → 1705.68] Um, but you know, I think the way that it's happened for a lot of web developers is they
[1705.68 → 1709.62] end up switching over to Chrome because, uh, they'd really like the browsing experience.
[1709.62 → 1715.48] And, uh, and then what, since they're already in it, then they'd open up the dev tools and
[1715.48 → 1718.10] then they figure out if, if they can make that work.
[1718.30 → 1723.18] And for a while I came for the JavaScript console, just as I found it, the autocomplete
[1723.18 → 1724.92] a lot better than firebug.
[1725.22 → 1727.78] I hated the CSS inspection and things.
[1727.82 → 1729.20] That's got a lot better lately.
[1729.36 → 1729.62] Yeah.
[1729.74 → 1733.96] Uh, the one thing that still bugs me, and I don't know if it, if it's just me as user
[1733.96 → 1738.80] error or what, it takes me about 10 clicks to actually select element style.
[1738.80 → 1743.66] We were supposed to click in there to put styling on a, on a particular element over
[1743.66 → 1744.50] in the inspector.
[1745.10 → 1745.50] Yeah.
[1745.66 → 1747.48] It takes, it takes a good amount.
[1747.66 → 1752.48] So, um, look, yeah, there are a few things that we're thinking about.
[1752.56 → 1756.42] One of the things that we're thinking about is, uh, so like it definitely has gotten a
[1756.42 → 1756.76] lot better.
[1756.76 → 1760.56] Like a year and a half ago, if you said that you hated manipulating styles, I would totally
[1760.56 → 1761.24] agree with you.
[1761.30 → 1765.84] Um, but now we have autocomplete on everything and, and tabbing between property and value is
[1765.84 → 1766.54] a piece of cake.
[1766.54 → 1770.42] And, and a lot of that has gotten quite a bit better from a like a just a usability
[1770.42 → 1770.92] standpoint.
[1771.44 → 1776.24] Um, one of the things that we're thinking about doing, uh, a small little difference
[1776.24 → 1781.50] in behaviour between what people have seen in firebug and what, what we have is that when
[1781.50 → 1787.22] you're, uh, clicking to either, either with elements, you're manipulating attribute names
[1787.22 → 1792.66] and values or in the styles, um, you're playing with styles and, uh, and firebug, it's only
[1792.66 → 1794.94] a single click, and then you're in edit mode.
[1795.60 → 1800.20] Um, and it always in the web kit inspector, it's always been double click to enter into
[1800.20 → 1800.86] edit mode.
[1801.58 → 1806.96] And, and I wonder if if that's, if single click is better.
[1807.16 → 1811.82] Um, and so we're, we're thinking about kind of experimenting with that and seeing if that
[1811.82 → 1813.16] makes for a more usable product.
[1813.16 → 1817.88] Uh, that's funny you say that because it's, it's something that I kind of battle recently.
[1817.98 → 1824.22] I, like when said, I pretty much camp out in, uh, either Firefox and or Chrome or Safari
[1824.22 → 1826.88] and pretty much in a web kit or a gecko browser more or less.
[1826.88 → 1830.06] And I'm using either firebug or the dev tools in Chrome.
[1830.06 → 1835.68] And, and I find that now that you just say that now I realize why I think Chrome is a
[1835.68 → 1840.26] little unusual for me is because that one small thing, it's not a huge thing, but I sometimes think
[1840.26 → 1844.30] I have an element selected, like I have it highlighted in blue, and then I want to jump
[1844.30 → 1846.32] into an attribute and like a single click should work then.
[1846.50 → 1851.20] But you know, this isn't a, a stage for me to give you feedback on that particular feature,
[1851.20 → 1853.04] but I do see that disconnect.
[1853.66 → 1855.12] How much of that is Chrome's influence?
[1855.12 → 1859.26] How much of it do you share with web kit and Safari and every other web kit browser?
[1859.26 → 1866.84] Uh, so, um, the, the, the large majority of the commits that are going into the, uh, web
[1866.84 → 1869.12] kit inspector are coming from the Chrome team right now.
[1869.74 → 1876.22] Uh, but, uh, uh, pretty much 95% of their work.
[1876.76 → 1881.48] Um, the work that that team is doing is going at, into the web kit level.
[1881.60 → 1884.44] There are a number of features that, uh, are specific to Chrome.
[1884.44 → 1890.70] Like, uh, our heap snapshots for memory, uh, memory leak detection or the ability to live
[1890.70 → 1894.64] edit JavaScript is unique to how we have, uh, V8 working.
[1895.12 → 1899.86] Um, but most, pretty much everything else, uh, is happening at the web kit level, which
[1899.86 → 1904.44] means that Safari gets that, um, and all the mobile web kit ports as well.
[1904.44 → 1909.34] Um, so one of the features that we announced at Google IO was remote debugging.
[1909.92 → 1918.08] So, uh, you have the ability to do, to basically, uh, your, your, your host browser or your, your
[1918.08 → 1925.06] client browser can run a little, uh, a web server, which hosts the dev tools, and you can open up,
[1925.06 → 1928.46] um, the dev tools in your desktop machines' browser.
[1928.46 → 1935.24] And, uh, and then look at like the network info or like do full script debugging, um, that's
[1935.24 → 1938.94] happening on your, on your, either your phone or your tablet.
[1939.20 → 1942.34] So the yeah, the Blackberry playbook is already shipping with that.
[1943.16 → 1947.84] Um, currently no other devices are, uh, but if you're on a Blackberry playbook, you can totally
[1947.84 → 1952.14] just use your machine and debug that, uh, the JavaScript on that tablet, which is really
[1952.14 → 1952.46] rad.
[1952.46 → 1957.66] Uh, and we're expecting, you know, since it's at the web kit level, everyone that every
[1957.66 → 1961.46] manufacturer that ships that can, can have that functionality.
[1961.46 → 1965.40] So the next, uh, year or so we're going to see a lot more devices with that.
[1967.34 → 1974.46] Now switching gears a little bit, uh, to, to use wind's phrase so eloquently, uh, a little
[1974.46 → 1975.28] inside joke there.
[1975.28 → 1979.34] I can tell that you're a little bit into CSS three, at least from what I can tell just from
[1979.34 → 1980.16] your social profile.
[1980.16 → 1983.02] Um, and you've created a few pretty neat tools.
[1983.14 → 1984.24] One CSS three please.
[1984.52 → 1988.80] And the other one, mother effing text shadow.
[1988.96 → 1991.08] That's a pretty cool little website there.
[1991.60 → 1997.64] And you kind of dive into these fun little ways to uniquely show off some very skilled
[1997.64 → 2001.26] design talents from what I can see too, but these make micro apps look huge.
[2001.26 → 2001.50] Yeah.
[2001.64 → 2007.22] I mean, this, um, I like, I like this for one, the styles, I'm going to compliment you
[2007.22 → 2010.56] there, but what I want to come into is the state of CSS three.
[2011.14 → 2015.34] Um, and just kind of what is really fun after the people are really just using well, what,
[2015.86 → 2019.80] what is overrefining in CSS three and what is, what is to come from CSS three?
[2019.80 → 2028.34] Uh, I think, you know, so I think you forgot mother effing HSL, uh, which is also pretty
[2028.34 → 2028.60] rad.
[2028.70 → 2031.78] I really like HSL as a way to pick colours way better than RGB.
[2032.66 → 2034.84] Um, so check that out if you want.
[2034.94 → 2037.38] Our favourite actually is HSL picker.
[2038.24 → 2039.36] I don't know if you've seen that one.
[2039.82 → 2040.12] Whatever.
[2040.44 → 2042.12] That name sucks, man.
[2042.66 → 2043.68] It's some work.
[2043.68 → 2049.02] Uh, but anyway, uh, some of the most exciting things are happening.
[2049.76 → 2051.70] Uh, yeah.
[2052.10 → 2055.12] I mean, cause you said that you can't even launch an H you can't even use HTML five
[2055.12 → 2058.86] bullet plate and or do an HTML five demo without including CSS three.
[2058.96 → 2063.68] So there's got to be some fun things that are just being bolted onto the, the design
[2063.68 → 2068.16] experience we now have and now are capable of with this brand-new tool that's being far
[2068.16 → 2070.10] more supportive than in the past.
[2070.10 → 2075.82] It was just difficult to even get the most oddities of bugs fixed in IE and your obscure
[2075.82 → 2078.30] browsers, but it's a whole different world there now.
[2078.60 → 2079.44] Yeah, totally.
[2079.62 → 2084.08] And we're finding a lot more bugs, I think like, like because the styling, uh, possibilities
[2084.08 → 2086.32] are, are getting so crazy.
[2086.32 → 2090.08] You know, like I actually have a fixed landed today in web kit that I've been watching for
[2090.08 → 2095.52] a while, which was if you put a 2d transform a scale on an iframe, there's some really weird
[2095.52 → 2095.84] clipping.
[2097.02 → 2098.24] You're using iframes.
[2098.42 → 2099.04] Oh yeah.
[2099.04 → 2103.70] Well, what I had is like, I do all my slides, my presentations, my slide decks are in HTML
[2103.70 → 2104.20] five.
[2104.60 → 2108.28] And on each slide, sometimes I would like just iframe in a website, and it'd be like talking
[2108.28 → 2109.88] about, you know, modernizer for instance.
[2109.88 → 2113.94] So I would have the iframe, but I would want to shrink it down so that it fits inside the
[2113.94 → 2114.60] slide.
[2114.88 → 2118.08] So I do a scale like 0.7 or something.
[2118.08 → 2119.82] And so it looks perfect inside the slide.
[2119.82 → 2121.24] But there was this weird behaviour.
[2121.24 → 2126.84] Um, so like there are edge case, uh, situations where things don't work the way that you'd expect
[2126.84 → 2127.32] and those get fixed.
[2127.32 → 2129.32] But there are a lot of exciting places.
[2129.32 → 2134.32] Um, one of the things that comes to mind is, uh, Lea Baron's CSS gradients gallery.
[2134.98 → 2139.60] Um, which showcases a lot of gradients that she's made and other, uh, CSS experts have
[2139.60 → 2143.96] been making, you know, in gradients, there's just linear gradients and radial gradients.
[2143.96 → 2148.42] And yet they're able to make these incredible like plaid patterns and patterns that come
[2148.42 → 2152.16] from pottery, um, and really impressive stuff.
[2152.30 → 2157.02] Uh, and so I really like the people who, who decide that they're just going to take, you
[2157.02 → 2162.60] know, a small feature, whether it's like box shadows or gradients and like really explore,
[2162.60 → 2164.12] uh, the boundaries of it.
[2164.54 → 2164.72] Yeah.
[2164.72 → 2165.26] I was doing that.
[2165.26 → 2168.46] I'm writing a chapter for the, the SAS book on a drop shadows.
[2168.46 → 2170.34] And so I was trying to see what shapes I can make.
[2170.34 → 2175.18] So even from one circle, I was able to create like the old Simon says game via just different
[2175.18 → 2175.90] colour drop shadows.
[2175.90 → 2176.16] Yeah.
[2176.16 → 2178.78] I was curious on a mother effing tech shadow here.
[2178.88 → 2181.58] How come I can only go on one, uh, one axis?
[2182.14 → 2182.50] What?
[2182.70 → 2184.28] You can go in four accesses.
[2184.32 → 2184.54] Yeah.
[2184.54 → 2185.66] One at a time.
[2185.78 → 2187.90] Oh, hit the WTF checkbox.
[2188.06 → 2188.76] Ah, okay.
[2188.76 → 2191.30] Well then, yeah, but then, okay, there you go.
[2191.40 → 2191.76] Okay.
[2191.88 → 2192.28] Nice.
[2192.40 → 2192.76] Clearly.
[2192.98 → 2193.34] Yeah.
[2194.18 → 2194.42] Yeah.
[2194.42 → 2196.14] Did you make sure to hit the all the way button?
[2197.10 → 2197.82] Oh, the rainbows.
[2198.14 → 2198.50] Yeah.
[2198.82 → 2199.62] That was nice.
[2199.62 → 2200.84] And you're also welcome.
[2201.02 → 2205.12] We have, we have content editable on that text, so you can just click into the text and
[2205.12 → 2207.30] change it to change log.
[2208.10 → 2208.50] Yeah.
[2208.86 → 2210.70] That looks definitely going in the show notes.
[2211.12 → 2211.88] Oh yeah.
[2212.94 → 2215.00] Uh, one of the things, oh, sorry.
[2215.36 → 2220.08] Uh, one of the things that I'm really, really excited about in CSS three or CSS four actually
[2220.08 → 2221.74] is what it's going to be is filters.
[2221.74 → 2227.12] Um, filters are coming in kind of from the SVG side of things, but it's going to be really
[2227.12 → 2228.82] pretty trivial in CSS.
[2229.28 → 2235.88] So we'll be able to like in regular styles, we'll be able to say like blur, uh, 20 pixels
[2235.88 → 2240.18] and we'll get a 20 pixel radius blur on that content, which is like blur is something that
[2240.18 → 2241.56] we wanted in CSS for a while.
[2241.56 → 2248.50] Or like, um, we'll be able to like desaturate the colours of whatever HTML content that is,
[2248.50 → 2253.78] or like, um, do all sorts of like the filters that you know from Photoshop.
[2253.78 → 2257.32] Uh, we were able to do in like just a line of CSS.
[2257.56 → 2258.74] I'm really excited about that stuff.
[2258.84 → 2260.84] Somewhere the IE team though is laughing at us.
[2261.46 → 2261.98] Oh yeah.
[2262.04 → 2262.60] And their filters.
[2262.82 → 2264.20] I mean, they were, they were right.
[2264.34 → 2270.68] Uh, I mean that, that API was absolutely horrible, but that feature set was super cool.
[2271.58 → 2275.14] There's got to be some, you know, newbie developer that's getting into this, and they're seeing
[2275.14 → 2279.98] some sort of, uh, you know, polyfill for doing some of those things in older browsers,
[2280.08 → 2283.14] older versions of IE and just think to themselves, what is DirectX?
[2283.14 → 2283.78] Yeah.
[2285.20 → 2285.56] Yeah.
[2286.14 → 2287.76] There's, there's a lot of legacy.
[2287.76 → 2288.56] That's a bad word.
[2289.34 → 2289.82] Mm-hmm.
[2290.06 → 2290.64] Mm-hmm.
[2291.26 → 2296.68] So on the notion of CSS3, I think this is kind of cool that you have mother effing tech
[2296.68 → 2298.30] shadow, and you've got CSS3 please.
[2298.40 → 2301.86] But the first thing that comes to mind since Wynn just mentioned his SAS book that he's
[2301.86 → 2305.26] writing is the fact that we're both just SAS lovers in general.
[2306.00 → 2312.28] And these tools are always useful to us, but, um, they don't give us SAS mix-ins to, to,
[2312.28 → 2312.98] to this stuff.
[2313.06 → 2316.60] Like, that's what kind of drives me crazy that all this stuff just spits out a CSS and
[2316.60 → 2324.34] it's almost as if the CSS3 world just, just, uh, doesn't appreciate, doesn't look at, doesn't
[2324.34 → 2326.60] care for what SAS is doing for CSS3.
[2326.60 → 2327.60] Yeah.
[2327.60 → 2328.60] Yeah.
[2328.60 → 2334.76] You know, so, uh, I do.
[2334.76 → 2335.76] Okay.
[2335.76 → 2341.82] Um, I really, I really like, uh, the, the authoring experience that SAS gives.
[2341.82 → 2343.82] I love the feature set that compass provides.
[2343.82 → 2347.90] Um, I really like, uh, authoring in, in CSS.
[2348.56 → 2354.46] And I think that, and, and, and you might've seen that, uh, there are proposals from the WebKit,
[2354.46 → 2362.52] uh, team to bring a lot of the same types of things of variables and mix-ins, uh, hierarchy,
[2362.52 → 2368.26] uh, into WebKit's implementation of CSS and getting that specified so that other browsers
[2368.26 → 2368.80] can do it.
[2368.80 → 2375.94] And so there was recently a face-to-face, um, uh, meetup of the CSS working group and they
[2375.94 → 2382.60] spent, uh, a lot of time talking about if they can, uh, make that happen in the standards
[2382.60 → 2383.16] process.
[2383.30 → 2385.86] So that's, that's moving ahead.
[2386.16 → 2393.40] Um, I think part of it, as far as the CSS community getting on adopting SAS and, and learning
[2393.40 → 2398.86] how nice it is and how much time it saves is like, you know, people are scared, scared
[2398.86 → 2399.72] of the command line.
[2399.72 → 2404.82] I think that like, that takes care of pretty much 90% of the problem.
[2405.56 → 2413.16] Um, but, but, uh, but I totally agree that, um, those tools are extremely valuable, especially
[2413.16 → 2414.24] for this type of work.
[2415.44 → 2418.36] So it sounds like you're a SAS and compass user then.
[2419.14 → 2422.18] Uh, uh, sort of.
[2422.28 → 2422.64] No.
[2422.64 → 2424.30] I mean, sort of enough.
[2424.46 → 2424.84] Yes.
[2425.66 → 2429.64] Not often, but I would, if I needed to.
[2432.06 → 2433.74] How do server side code do you sling?
[2434.48 → 2434.96] Yeah.
[2435.16 → 2437.72] Uh, oh, I don't, I don't sling any at all.
[2437.92 → 2440.70] I know JavaScript and I don't know anything else.
[2441.36 → 2442.74] Um, not even node.
[2443.44 → 2450.02] Well, I mean, I could write, no, I've done, I've done like three hours worth of node work.
[2450.44 → 2452.20] Um, so there's that.
[2452.20 → 2456.20] Um, but in general, I really like being inside a browser.
[2457.20 → 2459.16] And so that's where I spend my development time.
[2461.16 → 2462.18] I feel the same way.
[2462.82 → 2465.28] Um, switching gears to one other thing.
[2465.28 → 2469.90] It seems like, you know, also with propping up HTML5 bullet plate, you, what you're really
[2469.90 → 2472.90] about at the core is about standards more or less.
[2472.90 → 2475.10] And you've got this very cool website.
[2475.20 → 2478.36] I just found because we're doing this interview with you, which is W3 fools.
[2478.36 → 2484.08] And then not only that, but you also have, um, you also have, what is this one called?
[2484.14 → 2484.92] It's ISO bar.
[2485.40 → 2485.76] Yeah.
[2485.96 → 2489.70] The ISO bar web standards and best practices document.
[2489.90 → 2490.06] Yeah.
[2490.06 → 2490.58] I love this.
[2490.58 → 2492.74] I mean, is this pretty well-kept up and current?
[2493.50 → 2494.12] Uh, yeah.
[2494.30 → 2498.44] So, um, that was with my old agency, but they just, uh, they've been maintaining it and they
[2498.44 → 2501.46] released a new version of it, uh, like two months ago or so.
[2501.90 → 2503.02] Uh, so that's being maintained.
[2503.02 → 2507.44] And, um, that was developed around the same time that the genesis of HTML5 boilerplate,
[2507.56 → 2509.38] uh, was kind of percolating.
[2509.66 → 2515.20] And, um, it just has kind of coding guidelines and, and things that make it easier for a team
[2515.20 → 2519.72] to kind of, uh, write maintainable code because they all kind of follow the same practices.
[2520.22 → 2522.02] Uh, and, and I think that's wise.
[2522.40 → 2531.80] Um, but yeah, you know, I, I think it's important that more important to me than, uh, the like
[2531.80 → 2535.94] semantic class names, I don't really care for semantic class names a lot.
[2536.10 → 2539.18] I care about like, is this maintainable for me in the future?
[2539.28 → 2541.04] Is this maintainable for the person that takes over?
[2541.18 → 2545.84] And if I'm developing this on a team, I want to make sure that the team can develop it without
[2545.84 → 2548.30] like asking all sorts of questions and that it makes sense.
[2548.30 → 2553.60] And so I think a lot of that is documentation and kind of the spreading of best practices,
[2553.82 → 2556.90] not only within your team, but like of the entire community.
[2557.62 → 2557.68] Right.
[2557.92 → 2558.18] Yeah.
[2558.18 → 2561.66] From your profile, it's linked to as front end coding standards, which I think is
[2561.66 → 2565.34] maybe a little bit better name than ISO bar, but that's the name of the company.
[2565.48 → 2566.78] But yeah, that'd be three schools.
[2566.78 → 2572.10] I think, I hope nobody listening to this podcast actually uses W3 schools, but from what you
[2572.10 → 2575.60] say here that they're in trouble and that they have refused to swap the name because
[2575.60 → 2577.12] they are not in connection with W3.
[2577.66 → 2579.54] Um, I think that's just, just super wild.
[2579.66 → 2583.70] But I mean, from a standards point of view, what is it that drives you crazy about people
[2583.70 → 2587.60] that, um, do things like this or don't even follow standards or just don't have any
[2587.60 → 2589.74] ideas about what standards are, like you said, semantic classes.
[2589.74 → 2593.20] And that's when people talk standards, that's nine times out of 10, what they're talking
[2593.20 → 2595.04] about is a semantic class name or something like that.
[2595.56 → 2595.80] Yeah.
[2595.92 → 2598.06] Well, you know, it's, it's really complicated.
[2598.40 → 2605.92] So, um, I think a lot of us got into, uh, believing in web standards and learn that XHTML
[2605.92 → 2607.74] was, was the right way to do things.
[2607.86 → 2608.62] Tables were terrible.
[2608.78 → 2609.98] You should write it in XHTML.
[2609.98 → 2611.74] All your class names should be semantic.
[2612.48 → 2613.86] Um, those sorts of things.
[2614.06 → 2619.46] I think that now there's a lot of people, uh, finding out that, that, that might not
[2619.46 → 2621.34] have been the best use of their time.
[2621.88 → 2625.86] Um, and so there's an interesting thing there, uh, where kind of people are running
[2625.86 → 2632.18] into the reality of what, uh, front end authoring means and what are actually the
[2632.18 → 2636.16] consumers of, uh, that, of what we're working on.
[2636.68 → 2642.62] Um, and so, yeah, so I'm actually really, you know, excited about people doing things
[2642.62 → 2648.52] the right way and doing things the best way in, in a way that's, you know, um, time efficient
[2648.52 → 2650.40] for them and has a big payoff.
[2650.98 → 2655.50] And, uh, and so I want to make sure that the people are, are developing in the most effective
[2655.50 → 2655.80] way.
[2655.86 → 2657.42] At the same time, I don't want to see them waste time.
[2657.42 → 2662.04] So I don't want to see them waste time with bad documentation and that's how the W3 fools
[2662.04 → 2662.80] site came about.
[2663.06 → 2667.38] Um, I, I should say that, uh, W3 schools has gotten better.
[2667.68 → 2670.76] Um, we kind of were their bug tracker for a good number of months.
[2670.76 → 2672.48] And so they fixed things up.
[2672.48 → 2677.56] And now at the bottom of every page on W3 schools is a, uh, if you find an error on this page,
[2677.56 → 2678.48] please submit this form.
[2678.48 → 2681.48] And it's right there on every single page, which is a huge improvement.
[2682.20 → 2685.50] Um, before it was just an email address that you, it was really hard to find.
[2685.50 → 2688.44] So things actually are better there at the same time.
[2688.44 → 2693.06] I'm still a huge proponent of people looking up documentation on, uh, Mozilla's, uh, developer
[2693.06 → 2693.34] centre.
[2693.76 → 2698.74] Um, I contribute to it almost daily as do many, many other really smart people.
[2698.74 → 2702.90] So that's where I think people should get their, get their reference information from.
[2705.10 → 2706.76] Game for some questions from Twitter.
[2708.70 → 2709.18] Sure.
[2709.44 → 2710.48] These are always interesting.
[2711.24 → 2714.26] When will Chrome add view source to the view menu?
[2714.26 → 2715.56] Joe Devon wants to know.
[2715.88 → 2716.26] Wow.
[2717.00 → 2718.30] I guess that makes sense.
[2719.16 → 2719.52] So.
[2720.88 → 2722.38] It's there if you under developer.
[2722.72 → 2723.42] Yeah, I'm looking at it.
[2723.42 → 2726.66] It's under you view developer, and then you have three options.
[2726.76 → 2727.80] One of which is view source.
[2728.76 → 2729.32] I don't know.
[2729.32 → 2732.82] I think using a mouse is pretty slow, bro.
[2733.12 → 2734.64] It's command alt J, right?
[2734.82 → 2736.92] Uh, command alt U for the, for the source.
[2737.12 → 2737.50] The view source.
[2737.62 → 2739.26] And then J for the I'm always going to the JavaScript console.
[2740.10 → 2740.32] Exactly.
[2740.32 → 2742.58] So I don't know.
[2742.80 → 2747.02] They're not, uh, is my answer and learn the keyboard shortcut and stop clicking.
[2751.44 → 2753.84] Red dirt JS wants to know if you'll come and speak.
[2754.58 → 2759.14] Uh, is that, that sounds like in the, in the middle of the country somewhere, right?
[2759.80 → 2760.28] Oklahoma.
[2761.30 → 2761.78] Cool.
[2761.78 → 2762.96] It's like North of Texas.
[2762.96 → 2763.48] Middle of the country.
[2763.78 → 2766.20] I'm, I'm down to come speak as long as I can.
[2766.34 → 2766.66] Sure.
[2766.90 → 2767.22] Okay.
[2768.00 → 2769.74] We'll convey the message that you're down.
[2769.92 → 2770.38] I'm down.
[2771.16 → 2774.24] Brian, the coder wants to know who's going to win the GOP nomination.
[2774.78 → 2775.22] Wow.
[2775.76 → 2783.74] Um, uh, did you guys see that?
[2783.84 → 2784.32] Ron Paul.
[2784.60 → 2784.96] Yeah.
[2784.96 → 2791.00] You guys see what's home girl, something O'Donnell O'Donnelly, the girl who walked out on Piers
[2791.00 → 2792.86] Morgan's, uh, interview.
[2793.40 → 2795.24] She was like, I don't like interviews.
[2795.36 → 2796.66] I'm going to stand up now.
[2797.48 → 2799.18] I think she's going to win it.
[2800.32 → 2800.70] Rosie.
[2801.28 → 2803.32] She's got tacked with, uh, sure.
[2803.64 → 2804.22] Is that Rosie?
[2804.38 → 2804.94] Rosie O'Donnell?
[2805.38 → 2806.32] No, no, no.
[2806.42 → 2809.02] She's like a Delaware tea party.
[2809.36 → 2809.54] Oh.
[2809.54 → 2809.64] No.
[2810.04 → 2811.90] She's not actually, she's not actually running it.
[2811.90 → 2812.00] Lost.
[2812.16 → 2812.28] Yeah.
[2812.52 → 2814.94] Um, but she's got, she's got promise.
[2816.94 → 2823.34] DJ or DG Combs wants to know any chance HTML5, Canvas, CSS, sprites will allow native animation?
[2825.78 → 2826.94] Adam, you want to take this one?
[2828.06 → 2831.82] He's got a nice, uh, we may have been Rick rolled with this one.
[2831.82 → 2834.84] He includes a YouTube link to a Mickey Mouse video.
[2834.98 → 2837.92] Yeah, I was, I saw this before, and I was a little curious.
[2838.04 → 2840.90] I really, native web animation, right?
[2842.10 → 2844.92] I mean, you can, you can animate.
[2845.52 → 2852.20] So CSS animation, which is in WebKit and now Firefox, uh, you can actually animate a background
[2852.20 → 2856.46] position of an image sprite and make it animated.
[2856.46 → 2861.64] And you can like to have like a little contra character walking across the screen, and he's
[2861.64 → 2863.76] like walking, and you can do it only with CSS.
[2864.30 → 2865.16] That's pretty cool.
[2865.52 → 2866.64] And that's native web animation.
[2866.94 → 2868.34] Of course you can animate on a canvas.
[2868.48 → 2871.44] You can animate, uh, anything with CSS transitions.
[2871.88 → 2876.92] So we, we've seen web animation for a while now, I guess.
[2880.08 → 2881.92] What's the scoop on WebM?
[2881.92 → 2885.92] Uh, WebM, uh, is...
[2886.48 → 2886.96] WebM?
[2887.18 → 2888.06] Dang near killed him.
[2888.78 → 2889.16] Mm.
[2890.74 → 2894.08] Uh, we, uh, I don't know.
[2894.38 → 2898.72] Um, so we have WebM support in Chrome and Firefox and Opera.
[2899.28 → 2903.84] Um, we don't have it in, uh, Safari or IE.
[2904.54 → 2909.38] Uh, IE and Safari support HG64.
[2909.38 → 2914.00] And, uh, Chrome still does actually, but, uh, Firefox and Opera do not.
[2914.84 → 2921.42] Um, and if you're doing video, uh, that you want to distribute via HTML5 video, you need
[2921.42 → 2925.92] to be encoding in those two formats and those two formats only.
[2926.28 → 2928.90] Um, and that's just how it's going to be.
[2928.90 → 2935.84] It's like, I don't know, just like make sure that your workflow makes it, uh, really, uh,
[2935.92 → 2938.22] efficient to always be encoding to two formats.
[2938.60 → 2940.28] Um, because that's just how it's going to be.
[2940.90 → 2946.06] Unless you want to like to manage the, the flash fallback or like, or whatever, um, which is
[2946.06 → 2947.82] totally an option as well if you want to do that.
[2948.00 → 2950.40] Um, but yeah.
[2950.40 → 2952.48] Or you're not going to get it on iOS, I suppose.
[2952.76 → 2955.46] So it takes a little bit of work to be honest.
[2955.62 → 2960.76] Like, um, Zen Coder, I know Zen Coder and there's a few other video serving, uh, video
[2960.76 → 2965.48] services that kind of, you give it one file, and it makes HTML5 video work everywhere for
[2965.48 → 2965.72] you.
[2966.24 → 2969.12] Uh, those services are actually really nice.
[2969.12 → 2970.26] Um, save you a lot of headaches.
[2970.36 → 2971.18] It's like web fonts.
[2971.24 → 2972.76] Web fonts are also really a pain.
[2973.08 → 2974.32] There are a lot of edge cases.
[2974.32 → 2980.60] And so using, um, things like Google web fonts, uh, saves you quite a bit of, uh, headaches.
[2980.72 → 2981.82] So, yeah.
[2982.06 → 2988.14] So speaking of, uh, HTML5 audio and video, um, what can we expect advancements in the shadow
[2988.14 → 2992.46] Dom and some of the, uh, below the, the surface things we can style?
[2992.66 → 2993.06] Yeah.
[2993.06 → 3001.30] So, um, there's a shadow Dom, uh, set up in web kit, but right now, uh, none of it is really,
[3001.30 → 3003.70] uh, developer facing at the moment.
[3003.70 → 3007.58] Um, there is some really exciting stuff going on.
[3007.70 → 3010.44] Uh, it's called, it's, it's very much related.
[3010.56 → 3011.84] It's called the component model.
[3012.04 → 3017.66] And if you check it out on the, what we G, uh, what working groups' wiki, uh, you
[3017.66 → 3020.04] can dig into the component model.
[3020.48 → 3025.50] And it's kind of a new way of structuring, um, elements into reusable components.
[3025.92 → 3029.84] It's kind of what we've always been doing, but like, it's basically baking it into the
[3029.84 → 3032.62] browser as a native way to, to build components.
[3032.62 → 3033.86] And I think it's really, really exciting.
[3034.04 → 3036.76] So right now it's being proposed kind of to the standards' community.
[3037.56 → 3041.60] Uh, I'd love to see developers, uh, take a look into it and see if it makes sense and,
[3041.60 → 3045.32] and, and post their feedback if they think there's, uh, changes that should be made or
[3045.32 → 3045.60] whatever.
[3045.60 → 3051.14] Um, but it looks really promising from here, and it looks like a wise way to move, kind
[3051.14 → 3053.28] of move the web platform, uh, forward.
[3053.54 → 3058.76] What about web kit support for styling those, uh, HTML five validation bubbles?
[3059.26 → 3059.94] Ah, yes.
[3059.94 → 3068.12] So there's a, uh, on the, uh, so the wiki, sorry, the web kit bug tracker is hosted on
[3068.12 → 3069.70] track and track has a wiki there.
[3069.84 → 3075.14] And there's this one page called like styling form controls on the web kit track wiki.
[3075.14 → 3080.06] And it has all the details on styling those, uh, things.
[3080.30 → 3088.38] So, um, I know Nathan Smith, uh, who made formalize, um, he was working a lot on, on those validation
[3088.38 → 3088.66] things.
[3088.72 → 3093.34] I pointed him to that page, and he was able to figure out the, uh, the last of his styling
[3093.34 → 3093.78] woes.
[3093.78 → 3097.02] So, uh, so that's the page that you want to check out.
[3097.46 → 3101.04] You know, sadly I've turned them off on our pages just because, uh, Firefox doesn't allow
[3101.04 → 3101.80] you to style them.
[3101.84 → 3103.36] Although they do look nicer by default.
[3103.46 → 3107.76] The black ones on Firefox, the ugly, uh, pink things that come back with a web kit.
[3107.86 → 3110.68] So I've just kind of turned those off for now just because that's fine.
[3111.12 → 3117.00] I, to be honest, I'm not, I'm not too, um, aggressive on adopting HTML five form validation
[3117.00 → 3117.56] right now.
[3117.56 → 3124.56] I think that, um, I, I would not yet really go all crazy on that just yet.
[3126.38 → 3127.24] All right.
[3127.26 → 3132.08] So we're, we're near the end of our show, which is, has just been a pleasure to have this
[3132.08 → 3136.02] chat with you about HTML five CSS three and all these fun, fun things with browsers and
[3136.02 → 3137.74] the future more or less.
[3137.80 → 3140.58] And I particularly liked when you mentioned CSS four.
[3140.74 → 3142.80] So that was, I did a back.
[3142.80 → 3143.36] Yeah, man.
[3143.42 → 3144.76] CSS level four, man.
[3145.10 → 3146.38] It's already in draft.
[3146.50 → 3146.82] It's coming.
[3146.82 → 3147.74] There you go.
[3148.02 → 3152.84] So I imagine you have to have some sort of hero out there that you just, uh, are either
[3152.84 → 3157.02] dying to work with on a project or throw up one of these microsites like you do for these
[3157.02 → 3157.74] fun tools that you make.
[3157.80 → 3164.34] Like you mentioned, uh, mother effing HSL and tech shadowing and, uh, even CSS three,
[3164.48 → 3164.70] please.
[3164.82 → 3167.06] So, so sites like this or just fun things that you do.
[3167.12 → 3170.26] Is there anybody out there that is just a hero to you or somebody that you'd like to
[3170.26 → 3171.98] pair with that you can mention here on the show?
[3172.60 → 3176.02] Uh, the, the person who has been like blowing my mind recently.
[3176.02 → 3179.02] Is Chris Coyer of CSS tricks.
[3179.02 → 3184.74] Uh, Chris has just been like dominating for the past, like four years, like writing on
[3184.74 → 3190.78] his blog about totally crazy advanced CSS and also like CSS fundamentals and like tackling
[3190.78 → 3195.72] the entire spectrum of like, uh, of web design and development professionals.
[3195.72 → 3200.80] Um, really just like puts a lot of effort into sharing everything that he learns.
[3200.80 → 3206.88] And I, I think it's really inspiring to me that he's so, um, big into publishing everything
[3206.88 → 3207.42] that he learns.
[3207.52 → 3209.96] You know, that's something that I try and do, and he excels at that.
[3210.08 → 3212.28] So he is at the top of that list right now.
[3212.66 → 3214.96] What do you think about that new skin he's got on his site?
[3215.84 → 3216.86] Oh yeah, it's hot.
[3216.86 → 3221.48] I told him, I told him that, uh, so when you re, when you resize the browser, there's
[3221.48 → 3225.24] all these kinds of transitions when it like switches into the media queries and, and there's
[3225.24 → 3231.52] all these transitions when things kind of rearrange and the search box at the top has a 1.2 second
[3231.52 → 3235.00] transition as it moves from the left to the top and back again.
[3235.00 → 3240.12] And I was like, Chris, you really, that's 1.2 seconds is really long.
[3240.12 → 3242.42] And, and, and he like vetoed it.
[3242.42 → 3243.86] I told him, and he's like, veto.
[3244.46 → 3246.06] So he's not changing that.
[3246.26 → 3250.70] But aside from that one terrible, terrible thing, uh, the sites are really hot.
[3251.18 → 3251.52] It is.
[3251.58 → 3252.12] It's pretty hot.
[3252.24 → 3254.34] It uses, it uses, uh, the new modernizer.
[3254.46 → 3255.26] It uses respond.
[3255.82 → 3258.20] Uh, it uses a bunch of tricks from H-Mobile boilerplate.
[3258.36 → 3260.62] It's got, it's got a lot of good stuff going on inside of it.
[3261.30 → 3261.88] Good stuff.
[3262.26 → 3264.98] Well, um, I think the other question we asked, and we probably have at least a
[3264.98 → 3266.18] least one more second to do it.
[3266.20 → 3270.34] Is there anything besides HTML5, CSS3, and the common things that you mentioned that
[3270.34 → 3271.52] you're well known for?
[3271.60 → 3276.00] Is there anything else out there in open source that, uh, that if you had extra time or a
[3276.00 → 3279.58] free moment, you're just dying to play with that we haven't talked about today?
[3280.80 → 3284.54] Um, anything out there in open source that I'm dying to play with?
[3286.22 → 3287.60] Sass, Compass.
[3288.88 → 3290.06] Yes, both of those.
[3290.70 → 3294.72] Um, I would also point out that, uh, one of the projects that I don't,
[3294.98 → 3298.48] talk about too much, um, that I'm really keen on.
[3298.60 → 3300.28] I have a, a repo on GitHub.
[3300.84 → 3302.72] Uh, it's called lazy web requests.
[3303.12 → 3309.24] And it's just, uh, things that would be really helpful for the developer community if they
[3309.24 → 3313.00] existed, like a screenshotting service that you could just pass it.
[3313.00 → 3317.12] Like, um, screenshot thing.com slash.
[3317.12 → 3320.50] And then you pass it a URL and you like say what the width is.
[3320.50 → 3324.16] And then it gives you a screenshot back, um, in that width.
[3324.16 → 3326.30] And it takes a screenshot with like a perfect browser.
[3326.30 → 3331.72] So it like can handle everything or, you know, um, uh,
[3331.72 → 3335.04] Jeffrey Grossenbach's doing that on the peep code blog, except he's doing it in the command
[3335.04 → 3337.28] line with the web or web kit to PNG.
[3337.28 → 3337.72] Okay.
[3338.72 → 3339.12] Yeah.
[3339.20 → 3342.42] Well, that's, yeah, that uses pretty old legacy stuff.
[3342.50 → 3346.90] I want to, I, someone actually, so, so I posted this as a as something on lazy web requests
[3346.90 → 3352.38] and someone actually made it, um, with phantom JS and, and node, uh, like three days ago.
[3352.38 → 3354.40] So, so that idea is already taken.
[3354.70 → 3358.74] Um, but, but on the repo, it was a bunch of other stuff that, uh, that would really help
[3358.74 → 3359.00] everyone.
[3359.00 → 3361.40] So it's kind of like a bunch of weekend projects.
[3361.40 → 3362.84] And what's the repo called again?
[3363.26 → 3364.28] It's called lazy web requests.
[3364.28 → 3364.56] Yeah.
[3364.56 → 3364.68] Yeah.
[3364.68 → 3364.92] Yeah.
[3365.02 → 3368.10] And so, uh, there's a lot of good stuff in there and a lot of the projects have already
[3368.10 → 3371.84] been, people have taken them on and like basically finished them.
[3372.14 → 3375.66] And so I kind of have to clear out the bug tracker because, uh, a lot of the things are
[3375.66 → 3379.18] done, but, um, but there's still plenty of cool stuff in there.
[3379.30 → 3380.72] So if you're looking for a project.
[3380.72 → 3384.24] Yeah, that's awesome because young programmers, a lot of times, you know, when we first get into
[3384.24 → 3386.84] this, you're like, you know, I've got all this energy of, I feel like I've got some
[3386.84 → 3387.96] skills, but what do I make?
[3387.98 → 3388.18] Right.
[3388.20 → 3392.44] And as I get older, I'm like, when do I have time to do half the ideas I come up with?
[3392.44 → 3392.72] Yeah.
[3394.28 → 3395.28] So this is awesome.
[3395.56 → 3395.68] Cool.
[3395.88 → 3399.90] And it's actually all issue based, and they can respond to it and do a fork and check
[3399.90 → 3401.14] it in, and it closes it out.
[3401.60 → 3402.00] Yep.
[3402.18 → 3405.04] That's, this is, I love the way that GitHub has grown.
[3405.14 → 3406.24] I mean, give them more kudos.
[3406.36 → 3406.70] Why don't we?
[3406.74 → 3411.62] But, um, I know for a while in our day job, we used at least the first month we used their
[3411.62 → 3416.64] issue tracking, uh, in lieu of deciding to move to pivotal tracker, but, and it worked
[3416.64 → 3417.12] well for us.
[3417.12 → 3421.32] It did its, it did its job and on commit closing issues, and they've just done a phenomenal
[3421.32 → 3424.64] job with this in general, but very cool.
[3424.74 → 3428.58] Well, Paul, I think I speak for, for when and probably everybody listened to this podcast.
[3428.70 → 3432.46] We certainly appreciate, uh, the efforts that you put into your work and your passion around
[3432.46 → 3432.64] it.
[3432.64 → 3437.74] And we appreciate the mother effing things that you do, whatever they might be, uh, out
[3437.74 → 3438.02] there.
[3438.30 → 3440.00] And just thanks for coming on the show.
[3440.50 → 3440.66] Cool.
[3440.72 → 3440.86] Yeah.
[3440.90 → 3441.50] Thanks a lot guys.
[3441.54 → 3442.10] This has been awesome.
[3442.10 → 3453.16] Solid title.
[3453.16 → 3483.14] Thank you.
