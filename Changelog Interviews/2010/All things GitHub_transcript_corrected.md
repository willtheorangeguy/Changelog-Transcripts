[0.00 → 20.12] Hello and welcome to The Change Log, episode 0.1.0.
[20.24 → 22.04] It's our first point release.
[22.30 → 23.68] My name is Adam Stachowiak.
[24.10 → 26.86] And I am Wendell, and I'm really excited about the show today.
[26.86 → 29.94] We've got a great guest, Chris Winston from GitHub.
[30.72 → 33.46] I think we're probably pretty big fans of GitHub, wouldn't you say, Wendell?
[33.84 → 36.90] Yeah, pretty much through 95% of what we're doing at The Change Log.
[37.86 → 40.56] Probably at least 70% of what I'm doing elsewhere.
[40.90 → 41.22] Right.
[41.62 → 42.58] We share stuff there.
[42.74 → 44.00] We connect with people there.
[44.38 → 49.56] And GitHub's been huge for open source this past few years.
[49.72 → 52.72] And what they've been doing has been awesome to see the growth around software
[52.72 → 56.10] and the way that the personal relationships and exchanges happen
[56.10 → 59.00] and the way that's evolved over the last two years of their development.
[59.68 → 63.32] You know, Git and GitHub are both changing how open source is conducted.
[63.74 → 70.06] And it's just really changing the landscape for sharing and doing what GitHub claims that they're wanting to do.
[70.12 → 70.98] And that's social coding.
[71.24 → 77.98] It just brings an aspect to merging and forking projects that we just haven't seen before.
[77.98 → 83.02] There's lots of stuff Chris talks about, too, in the interview that kind of details on the social coding aspects of GitHub
[83.02 → 90.92] and the 4Q and how that proliferates software development in this open source landscape we're in.
[90.98 → 91.50] It's kind of wild.
[91.82 → 94.72] Yeah, it was interesting to hear some of the backstory of how GitHub got started
[94.72 → 97.04] and some of the success they've had.
[97.76 → 100.02] It's just been quite the success story.
[100.24 → 104.38] I guess last pre-interview, you were saying at least 30 years that they've been around, right?
[104.74 → 105.78] Yeah, right.
[107.14 → 107.98] No, they've been around.
[108.08 → 108.66] What, two years now?
[109.24 → 111.96] I guess if you're taking it internet years, though, it's 20 years.
[112.48 → 112.84] Right.
[113.24 → 117.10] And because I thought they were three years old, but I was mistaken.
[117.22 → 117.82] They're actually two.
[118.76 → 123.14] And in Chris's eyes, it's actually one because he doesn't feel they really started until they start paying themselves.
[124.12 → 127.52] And so, I mean, that's kind of cool to hear him say that, too, because, you know,
[127.52 → 130.26] they treated it like a bootstrap company, which it was for the first year.
[130.26 → 136.30] And to them, it didn't truly become real until they started to see some, you know,
[136.54 → 141.38] paychecks from their day-to-day operations and turning it into a real full-time, you know,
[141.42 → 144.86] undedicated this 100%, which they were, obviously, but it's kind of wild.
[145.18 → 149.70] Something else that's cool to see come from this is going to GitHub.com forward slash explore.
[149.70 → 155.54] Welcome to all the new listeners that are coming from the Explorer page on GitHub that took us by surprise.
[155.82 → 159.48] Chris reached out to us a couple of weeks ago and said they were putting that in the works,
[159.56 → 165.18] and we were excited about having our changelog podcast episodes up on GitHub.com slash explore.
[165.34 → 170.90] But I think the cool features of that page are the trending repos and the featured repos.
[171.12 → 171.28] Yeah.
[171.58 → 172.10] Yeah, for sure.
[172.46 → 176.94] Certainly excited to see where this goes, but what I see so far is pretty exciting.
[176.94 → 179.10] Be sure to stick around to the end of the episode.
[179.24 → 182.46] We've got kind of a big announcement, some other things that we've got,
[182.54 → 185.10] some Skunk Works projects that we've been working on,
[185.18 → 187.78] so stick around to the end of the episode for a special treat.
[188.06 → 188.90] Don't fast-forward.
[189.40 → 190.98] Don't even think about moving the dial.
[191.12 → 194.18] Just listen to the whole thing, and you'll catch it at the end.
[194.52 → 195.42] It's worth every minute.
[195.62 → 196.08] Sure is.
[196.70 → 198.32] You want to get to the episode there, Wynn?
[198.58 → 199.26] Let's get to it.
[206.94 → 210.22] We're here with Chris Wans troth.
[210.32 → 215.86] He is one of the co-founders of a very cool website we all know and love called GitHub.com.
[216.26 → 217.68] Chris, why don't you go and say hi to everybody.
[218.22 → 218.84] Hello, everybody.
[219.46 → 223.56] So, Chris, we're here in this world we call open source.
[223.64 → 224.08] We all love it.
[224.10 → 224.70] We all know it.
[224.88 → 228.22] And it's a very, very tight group that's coming along,
[228.22 → 234.12] and I think that we all know that GitHub seems to be every day more and more becoming the epicentre of open source.
[234.12 → 235.16] How do you feel about that?
[235.66 → 237.46] I feel good.
[237.66 → 240.08] It makes me happy because I do a lot of open source work,
[240.38 → 246.32] and one of the reasons we built GitHub was to make it easier to send patches and do all that sort of tedium.
[247.06 → 249.06] And I think it's coming along pretty well,
[249.14 → 252.96] and a lot of people are realizing how easy it is making their open source maintenance.
[253.34 → 257.38] Like, when you start having five or six or seven tiny open source projects
[257.38 → 260.32] that you don't care about exclusively or all that much,
[260.36 → 261.74] but you still want to make sure they're up-to-date,
[261.74 → 263.66] it can really become a time sink.
[263.74 → 267.14] You can start to have things pile up, and that's what happened to me when I was consulting.
[267.82 → 271.98] And it's great that GitHub is coming along, and it's still going in that direction.
[272.12 → 275.56] It's making open source easier for you as a maintainer or you as a contributor.
[276.22 → 279.10] And the fact that it's becoming so popular,
[279.28 → 281.60] not just something that actually works, but something that's popular,
[281.60 → 282.56] is pretty incredible.
[282.56 → 287.82] And it's great because now that I'm working more and more and focusing on GitHub,
[288.16 → 291.88] it's really easy for me to kind of keep up to date on my hobby,
[292.12 → 295.08] or one of my hobbies, which is programming, because it's right there.
[295.16 → 299.08] It's easy to see what people are talking about or something cool that just popped up
[299.08 → 300.56] because it's on GitHub, and I'm there anyway.
[300.80 → 303.94] So I'm pretty happy about it because it's a fun job,
[304.00 → 306.86] and it's a site I think I'd really be into if I didn't work there.
[306.86 → 309.82] So let's rewind and talk about Git for a second.
[309.98 → 314.52] So why Git and GitHub and not SVN Depot or Planet Mercurial or something like that?
[316.16 → 320.22] Well, Git was the first distributed version control system that I really understood.
[320.50 → 325.14] I played with a couple before and didn't really even know that's what was going on.
[325.30 → 328.10] I had used Darks the summer before,
[328.80 → 334.08] and I think I had used Mercurial to install the microformats test suite.
[334.08 → 340.14] But with Git, I saw the Torvalds video where he kind of explained it in higher level terms,
[340.38 → 341.22] and it really appealed to me.
[341.28 → 345.00] The community aspect, the fragmentation of, you know,
[345.04 → 347.94] this person can fork your project, and they can work on it without your permission,
[347.94 → 351.24] and then they can actually produce something that has a lot of value,
[351.58 → 352.82] and you didn't get in their way.
[353.12 → 354.04] That was really appealing to me,
[354.08 → 355.88] and it was also really appealing to Tom Preston Werner,
[356.04 → 358.58] who started it with me and PJ Hyatt.
[359.06 → 360.52] And I think we had a lot of the same ideas,
[360.60 → 363.24] and we were working with each other on a project as well.
[363.24 → 365.24] He had a project, and I sent him like two patches.
[365.84 → 369.70] And it was all through Git, and I was using Git for private projects.
[370.12 → 375.06] And it just seemed sort of obvious that we were going to work on a site and use Git
[375.06 → 377.98] because we weren't trying to start a coding site.
[378.08 → 380.76] We were just trying to start a site to host Git repositories.
[381.40 → 382.52] So it was kind of a no-brainer.
[382.64 → 384.32] It was like, we have these Git repositories now.
[384.38 → 385.86] We really love the philosophy behind Git.
[385.98 → 386.76] Where do we put them?
[387.22 → 389.70] And there was repo.or.cz, which is still around,
[389.70 → 392.24] but that's sort of a single serving.
[392.38 → 395.20] You just put a project up, and you can sort of publish it there.
[395.36 → 398.00] We wanted a place where we could sort of get involved
[398.00 → 401.08] in this distributed community of forking and all that sort of thing.
[401.16 → 402.92] So that's where GitHub kind of came from.
[403.58 → 405.30] Have you talked to Linus at all about Git
[405.82 → 408.64] and how GitHub may be fuelling the popularity of Git itself?
[409.64 → 410.82] I haven't talked to him.
[411.02 → 412.70] Maybe someone in GitHub might have.
[412.76 → 415.08] I'm not super involved with the Git community.
[415.74 → 417.10] We have people that do that for us.
[417.10 → 419.34] Scott Charon, who works for us, is a Git expert.
[419.46 → 420.34] He's involved in the community.
[421.00 → 422.96] He writes books on the mailing list, submits patches.
[423.12 → 426.28] So he's more the guy that's involved with Git itself.
[426.78 → 430.08] Ryan Tomek and Tom Preston-Werner are also pretty involved in Git itself,
[430.16 → 432.24] but I am just a happy user, really.
[432.98 → 435.44] It's kind of hard to go very far looking into Git
[435.44 → 437.50] and not see Scott Charon's name anywhere.
[438.04 → 439.58] He's pretty prevalent in the community.
[440.10 → 443.58] Yeah, we were very lucky to get him early on.
[444.42 → 445.16] Serendipitous, really.
[445.16 → 448.02] The fates aligned, and he became a member of GitHub
[448.02 → 450.22] way earlier than we thought we would ever be hiring anyone
[450.22 → 451.06] outside the founders.
[452.00 → 454.34] And then that's when we started doing our training business
[454.34 → 456.24] where we'll do Git training for big companies
[456.24 → 459.30] where the CTO or someone is excited about Git
[459.30 → 460.66] and wants to start moving towards it.
[460.72 → 461.98] We'll come in and do a couple classes.
[463.04 → 464.74] And so we brought Scott on board,
[464.86 → 467.12] and he said, you know, I have a class coming up.
[467.22 → 469.18] Can we make this a GitHub thing instead of a Scott Charon thing?
[469.22 → 470.12] And we said, sure, who is it?
[470.14 → 470.82] And he said, Google.
[470.98 → 472.70] We were like, okay, that works for us.
[472.84 → 473.84] They can be our first trainees.
[473.84 → 474.28] Yeah.
[476.48 → 479.22] So let's talk about the startup process, I guess,
[479.22 → 483.06] of GitHub and how that all came about.
[483.40 → 486.18] So who was your first hire, and what was that like, I guess,
[486.56 → 490.42] the bootstrapping first parts of the real company formation
[490.42 → 492.28] and where that started at?
[492.28 → 495.60] Well, our first hire technically was Scott.
[496.22 → 501.62] But before that, PJ Hyatt, Tom Preston, and me had kind of started the company
[501.62 → 506.02] in our spare time and ran it for a couple of months.
[506.50 → 510.24] We actually started developing it in October of 07,
[510.90 → 514.76] and we released the beta in January of 08.
[514.80 → 517.18] All the beta meant was that we had a place to host a site,
[517.28 → 518.86] and you could sign up if you had an invitation.
[518.86 → 520.52] That was where we drew the line.
[520.88 → 524.06] And then we launched it officially in April of 08,
[524.22 → 528.16] and all the official launch meant is that we could take your credit card number
[528.16 → 529.04] and charge you.
[529.70 → 534.40] So in the early days, we started making money right away in April.
[534.40 → 538.16] But we also had jobs, or we were living off our savings,
[538.16 → 540.34] and it was kind of a side project thing.
[540.44 → 543.64] So even then, it was a little bit difficult because you're working 40 hours or what,
[543.66 → 547.22] a week somewhere else, and you have this website that's making money
[547.22 → 548.56] and gaining traction.
[549.42 → 551.30] So believe it or not, that's actually pretty stressful
[551.30 → 553.24] because it seems like things are going well,
[553.36 → 555.16] but they're not really going the direction you want
[555.16 → 558.34] because you just want to be working on GitHub all the time.
[558.78 → 560.38] And from there, it just kind of grew.
[560.62 → 561.38] The site grew.
[561.38 → 563.38] We started making more and more money.
[563.52 → 565.52] We added stuff to be more friendly to businesses.
[566.72 → 570.74] And towards the end of 2008, we had the opportunity to hire Scott,
[570.84 → 571.86] and we brought him on board.
[572.28 → 575.36] And around that time, we started making projections.
[575.80 → 578.42] How much are we going to be making in January?
[578.56 → 579.72] How much are we going to be making in March,
[579.78 → 581.02] given our current rate of growth?
[581.46 → 586.18] And we decided around, I guess, October, sometime late 2008,
[586.38 → 588.06] that we were going to start taking salaries.
[588.06 → 589.12] We were going to start paying ourselves,
[589.12 → 591.00] but we were going to do it a little bit at a time.
[591.62 → 595.72] So we'd all start out at 10% of our goal salary.
[596.26 → 597.94] And then every month, based on the projections,
[597.94 → 601.08] if we'd hit them, we would bump it up to 20%.
[601.08 → 604.16] If we missed them, we would maybe take a month off or make it 15%.
[604.16 → 606.62] And so for the next couple of months,
[606.62 → 609.10] we were all sorts of watching the money pretty carefully,
[609.22 → 612.66] trying to do things to make sure we didn't regress in the growth,
[613.08 → 615.62] and giving ourselves raises one step at a time
[615.62 → 618.22] until finally we all were making the salaries that we wanted to make.
[618.22 → 621.08] So that, for me, is really where the business started.
[621.20 → 623.04] It started at the beginning of 2009,
[623.14 → 624.52] when we all started making full salaries,
[624.52 → 626.30] and that's when it really became a grown-up business.
[626.46 → 628.94] We had health insurance and all those benefits,
[629.18 → 632.74] because that's a lot different from 2007,
[633.00 → 634.80] working on a little Rails app in your apartment.
[635.32 → 635.52] Right.
[635.70 → 637.66] So we're basically a year old then.
[638.16 → 640.24] At the point when we were all making money?
[640.40 → 640.70] Well, yeah.
[640.86 → 642.26] So based on what you just said,
[642.30 → 643.88] you said early 2009,
[644.06 → 645.48] so around, let's say, just January.
[645.48 → 647.26] And now we're in January 2010,
[647.42 → 649.00] so we're about a year old in your eyes.
[649.00 → 650.92] Yeah, it was less than a year after we launched,
[650.96 → 653.60] and we all started paying ourselves what we wanted to be paid.
[654.04 → 654.30] Gotcha.
[655.08 → 657.58] So that was fun.
[657.70 → 658.32] That was a fun year.
[658.46 → 660.34] Because during that year, though,
[660.54 → 661.40] I want to stress,
[661.46 → 664.00] we were all sort of living off our salaries
[664.00 → 665.30] or working other jobs.
[665.30 → 668.00] So it wasn't really that great of a year, 2008,
[668.10 → 669.26] even though things were on the up and up.
[669.34 → 670.58] 2009 was a much better year.
[671.36 → 673.60] But I think that's one of the hard parts of starting a business
[673.60 → 674.54] or bootstrapping a business,
[674.90 → 676.98] is it's really easy to give up.
[677.44 → 678.14] I mean, at any point,
[678.50 → 680.32] we could have just decided,
[680.48 → 680.78] oh, you know,
[680.78 → 682.24] I'm going to take a month off
[682.24 → 683.94] and just do full-time consulting work
[683.94 → 685.30] and put GitHub on the back burner.
[685.94 → 688.70] Or a couple of us had really lucrative job offers
[688.70 → 689.52] that we could have taken
[689.52 → 690.44] and just said, you know,
[691.22 → 692.52] this GitHub thing has been taking off
[692.52 → 694.68] as fast as I hoped it would.
[695.04 → 697.74] So I think a lot of it has to do with,
[697.88 → 699.02] for us, it's just persistence.
[699.36 → 699.98] I mean, at any time,
[700.06 → 701.60] we could have given up and stopped,
[701.66 → 702.56] especially during that year
[702.56 → 704.84] of living off of no money or other money.
[705.20 → 707.26] But yeah, when you're bootstrapping yourself,
[707.40 → 708.28] that's a big challenge.
[708.84 → 710.16] When did you first start seeing
[710.16 → 711.98] higher-profile open-source projects
[711.98 → 713.54] move their repos over to GitHub?
[715.28 → 719.70] Well, Ruby on Rails moved on launch day
[719.70 → 721.00] in April 2008.
[721.00 → 723.16] So that was the first huge one for us.
[723.46 → 724.62] But, you know,
[724.66 → 725.44] we've been kind of blessed
[725.44 → 727.08] by having major open-source projects
[727.08 → 728.18] the whole way.
[728.76 → 730.22] Beta started because
[730.22 → 732.32] Yehuda and some of the Mere team
[732.32 → 734.52] wanted to start rewriting Mere 0.5,
[735.16 → 736.96] getting it ready for Mere 1.0.
[737.34 → 739.22] So they started the Mere 0.9 branch
[739.22 → 740.70] on GitHub the night we launched the beta.
[740.90 → 741.38] So right away,
[741.44 → 742.62] we already had a pretty awesome project
[742.62 → 744.40] doing substantial development on GitHub.
[744.92 → 745.54] And since then,
[745.56 → 748.20] it's just been kind of hard to keep track.
[749.26 → 750.40] You know, there were Rails
[750.40 → 751.92] and then all the JavaScript frameworks,
[752.06 → 754.84] jQuery, Prototype, Scriptaculous, GUI.
[755.44 → 756.16] And then from there,
[756.22 → 757.58] we're starting to see Cake PHP,
[757.74 → 757.98] Symphony.
[759.02 → 760.42] There are a couple of forks of
[760.42 → 763.00] ASP's MVC.net framework.
[764.00 → 765.46] It's kind of hard to keep track of, too,
[765.52 → 766.62] especially when you have projects
[766.62 → 767.70] that aren't, you know,
[767.78 → 768.76] the Linux kernel,
[768.92 → 770.28] but are still really important to you
[770.28 → 771.88] or something you use from your past
[771.88 → 772.30] coming over.
[772.40 → 773.14] It's neat to see.
[773.14 → 775.40] We recently had the TinyMCE,
[776.04 → 776.80] Rich Text,
[777.02 → 779.72] kind of WYSIWYG editor for HTML,
[780.18 → 781.64] which I used back in the day.
[782.02 → 782.70] And now it's on GitHub.
[782.82 → 784.12] So it's kind of come full circle there.
[784.66 → 785.70] So it's just kind of incredible
[785.70 → 786.38] the amount of projects
[786.38 → 787.04] that are moving over,
[787.14 → 788.48] both in terms of projects
[788.48 → 789.94] that have lots of downloads
[789.94 → 790.54] and visibility.
[791.84 → 793.68] We have Erlang's OTP
[793.68 → 794.80] is on our site
[794.80 → 795.88] and Clojure.
[796.08 → 796.88] And then other projects,
[797.02 → 797.28] just, you know,
[797.32 → 798.68] there's lots of really cool small stuff
[798.68 → 799.42] that doesn't really get
[799.42 → 800.68] the name recognition
[800.68 → 801.62] and isn't blogged about,
[801.72 → 803.30] but it's pretty solid code
[803.30 → 803.70] that's there.
[803.76 → 804.26] And all it has
[804.26 → 804.96] is the GitHub presence
[804.96 → 806.00] and sometimes that's enough.
[806.54 → 808.16] Do you guys actively evangelize
[808.16 → 809.14] or recruit those projects
[809.14 → 809.68] to come over
[809.68 → 810.30] or do they just
[810.30 → 811.22] follow the momentum?
[812.44 → 814.20] It depends on your definition
[814.20 → 815.60] of actively evangelize
[815.60 → 815.96] or recruit.
[815.98 → 816.66] How do you call up
[816.66 → 816.98] and say,
[817.12 → 818.12] hey, Messick,
[818.16 → 818.90] you need to move jQuery
[818.90 → 820.08] over to GitHub?
[821.18 → 822.62] We hassled Messick
[822.62 → 823.08] a couple of times,
[823.14 → 823.80] but that was only after
[823.80 → 825.44] we had a couple of drinks
[825.44 → 825.68] with him
[825.68 → 826.90] and we became friends.
[827.80 → 828.68] In the early days,
[828.74 → 829.58] we emailed a couple of projects.
[829.72 → 829.94] We said,
[829.94 → 831.18] hey, check this out.
[831.24 → 832.20] This would be great for you.
[832.58 → 833.52] And they said,
[833.60 → 833.80] you know,
[833.88 → 834.78] oh, no, not now.
[835.00 → 836.36] And no one we emailed
[836.36 → 837.14] moved to GitHub.
[838.12 → 839.14] But a funny thing happened
[839.14 → 842.48] is about 99% of the projects
[842.48 → 843.76] we emailed in the early days
[843.76 → 845.26] eventually came over to GitHub.
[845.82 → 846.60] And so we decided
[846.60 → 847.66] that there's just no point
[847.66 → 849.34] in us evangelizing the site.
[849.96 → 850.90] What's better for us
[850.90 → 852.24] is to evangelize Git,
[852.62 → 852.78] you know,
[853.04 → 854.12] work on Git literature
[854.12 → 855.00] and books
[855.00 → 855.92] and screencasts
[855.92 → 856.52] and that sort of thing,
[856.90 → 857.46] which we wanted to do
[857.46 → 858.06] the whole time anyway.
[858.06 → 859.82] And we found
[859.82 → 860.38] that the best way
[860.38 → 861.36] to get people to use our site
[861.36 → 862.10] is to make the site
[862.10 → 862.74] really awesome.
[862.94 → 863.66] So we focus on
[863.66 → 864.70] making the site really awesome
[864.70 → 865.66] and so far
[865.66 → 866.52] that has been
[866.52 → 867.88] the thing that brings over
[867.88 → 868.74] the big ticket items.
[869.38 → 870.14] Well, not to mention
[870.14 → 871.18] also focusing on
[871.18 → 871.96] the user happiness.
[872.10 → 872.82] I guess that does make,
[873.40 → 874.38] fall into making the site
[874.38 → 874.86] more awesome
[874.86 → 875.68] is user happiness.
[875.90 → 876.92] And if you have
[876.92 → 878.08] an army of loyalists,
[878.16 → 879.34] as a good friend of mine,
[879.58 → 880.22] Jonathan Kaye,
[880.22 → 880.56] says,
[880.94 → 882.28] if you have an army of loyalists
[882.28 → 884.60] that constantly evangelize for you,
[884.72 → 885.44] they do your job.
[885.60 → 885.80] You know,
[885.90 → 886.48] you don't have to.
[887.44 → 888.24] That is true.
[888.48 → 888.58] We,
[888.68 → 889.22] I mean,
[889.22 → 889.82] we get a lot of that.
[889.90 → 890.54] That's the thing
[890.54 → 891.18] is if you're going to try
[891.18 → 891.88] and have someone
[891.88 → 893.44] switch something
[893.44 → 894.38] as personal
[894.38 → 895.32] as version control
[895.32 → 896.64] from what they're used to,
[896.72 → 897.24] what they like,
[897.28 → 898.38] what's not getting in their way
[898.38 → 899.30] to something new
[899.30 → 900.32] and maybe a little bit
[900.32 → 901.04] harder to learn
[901.04 → 902.70] and totally radical,
[902.88 → 903.82] it's not going to be
[903.82 → 905.36] some Rails programmer
[905.36 → 905.90] on Twitter.
[905.90 → 906.34] It's going to be
[906.34 → 907.04] one of their friends
[907.04 → 908.10] or someone that they trust.
[908.60 → 909.44] So there's really
[909.44 → 910.04] almost no point
[910.04 → 910.78] in us evangelizing
[910.78 → 911.32] at this point.
[911.44 → 912.06] It's much easier
[912.06 → 912.78] for us to,
[913.18 → 913.28] you know,
[913.32 → 913.66] like I said,
[913.68 → 914.56] make the site perfect,
[914.56 → 915.72] make people really excited
[915.72 → 916.18] about the site,
[916.24 → 916.88] including ourselves,
[916.88 → 918.12] and then get those people
[918.12 → 919.32] to tell their friends
[919.32 → 919.60] about it
[919.60 → 920.24] or tell their boss
[920.24 → 921.08] or tell their co-worker
[921.08 → 921.52] or say,
[921.58 → 921.72] you know,
[921.72 → 922.40] come try to find it.
[922.40 → 922.82] I think that's absolutely right.
[922.98 → 923.24] You know,
[923.64 → 924.06] there's,
[924.16 → 925.02] we cover the open source
[925.02 → 925.52] side of GitHub
[925.52 → 927.16] on this podcast,
[927.16 → 928.60] but I know Adam and I
[928.60 → 929.48] both do client work
[929.48 → 930.68] and that's one of the
[930.68 → 931.52] stipulations I have to
[931.52 → 932.18] take on a project
[932.18 → 933.06] is your source control
[933.06 → 933.82] has to be in GitHub
[933.82 → 934.62] because I'm not going
[934.62 → 935.28] to go back
[935.28 → 936.58] to the subversion world.
[936.58 → 937.80] Yeah,
[937.90 → 938.88] I won't even work
[938.88 → 939.24] with you if you're
[939.24 → 940.00] not using Git.
[940.14 → 940.26] Like,
[940.30 → 941.00] just get out of here.
[941.62 → 942.34] No pun intended.
[944.00 → 944.70] It does seem,
[944.92 → 945.58] this is where a lot
[945.58 → 947.60] of the claims
[947.60 → 947.98] of arrogance
[947.98 → 948.48] come from
[948.48 → 949.24] because you say that.
[949.30 → 949.52] You say,
[949.58 → 950.02] I don't want to work
[950.02 → 950.36] with you if you're
[950.36 → 950.88] not using Git
[950.88 → 951.96] and to a subversion
[951.96 → 953.70] user or to another
[953.70 → 954.46] version control user,
[954.46 → 955.44] they see that as arrogance,
[955.44 → 956.70] but a Git user
[956.70 → 957.64] just sees that as,
[957.88 → 958.00] no,
[958.08 → 958.34] of course,
[958.42 → 958.82] why would I want
[958.82 → 959.40] to use subversion?
[959.52 → 960.08] That's insane.
[960.72 → 961.60] It's just a matter
[961.60 → 961.98] of fact.
[962.10 → 962.26] It's just,
[962.36 → 963.04] there are so many things
[963.04 → 964.00] that you want to do
[964.00 → 964.30] with Git
[964.30 → 964.90] that you can do
[964.90 → 966.12] that you just can't
[966.12 → 966.80] do with subversion.
[967.24 → 967.58] Oh, yeah.
[967.70 → 968.22] Your workflow
[968.22 → 969.16] completely changes
[969.16 → 970.14] like night and day.
[971.06 → 971.36] Yeah,
[971.42 → 971.72] and it's,
[971.80 → 973.02] I think it's a very nice tool.
[973.10 → 973.80] People complain about
[973.80 → 974.78] Git's user interface
[974.78 → 975.84] and say it's confusing.
[976.34 → 976.86] I think maybe some
[976.86 → 977.24] of the commands
[977.24 → 977.70] are confusing,
[977.86 → 978.46] but things like
[978.46 → 979.86] just automatically paging
[979.86 → 980.74] the Git log output
[980.74 → 982.00] and colourizing diffs
[982.00 → 982.48] off the bat,
[982.56 → 983.28] I think that's what makes
[983.28 → 984.18] a nice user interface.
[984.44 → 985.44] It thinks about the person
[985.44 → 986.18] using the tool
[986.18 → 987.58] and that always impressed me.
[987.66 → 988.46] Typing SVN log
[988.46 → 990.08] and getting every revision
[990.08 → 991.52] and just seeing like R1
[991.52 → 992.14] in my terminal,
[992.28 → 992.68] that doesn't seem
[992.68 → 993.48] like a good user interface
[993.48 → 993.84] to me.
[994.90 → 996.20] And the merging
[996.20 → 997.06] is light years ahead
[997.06 → 998.64] compared to anything
[998.64 → 999.42] else I've used.
[999.66 → 999.76] I mean,
[999.82 → 1000.12] it's just,
[1000.22 → 1000.72] it's amazing
[1000.72 → 1001.76] how well it handles
[1001.76 → 1004.06] merging two files.
[1004.78 → 1004.96] Yeah,
[1004.98 → 1005.72] it's just perfect
[1005.72 → 1006.74] at handling situations
[1006.74 → 1007.88] where you don't really know
[1007.88 → 1008.70] what you're up against
[1008.70 → 1009.36] and there might be
[1009.36 → 1010.10] multiple remotes,
[1010.24 → 1010.94] multiple contributors,
[1011.44 → 1012.20] you have different patches
[1012.20 → 1012.78] written against
[1012.78 → 1014.34] different masters
[1014.34 → 1015.66] and it's perfect
[1015.66 → 1016.98] at trying to resolve
[1016.98 → 1017.46] the changes
[1017.46 → 1018.06] or telling you
[1018.06 → 1018.92] exactly what went wrong
[1018.92 → 1019.92] and letting you fix them yourself.
[1020.12 → 1020.22] Yeah,
[1020.24 → 1020.86] that's a good segue
[1020.86 → 1021.68] into probably
[1021.68 → 1022.94] one of my favourite
[1022.94 → 1023.92] GitHub features
[1023.92 → 1024.94] and that's the 4Q.
[1025.42 → 1026.16] Can you talk about
[1026.16 → 1027.00] how that came about
[1027.00 → 1029.40] and just how that developed?
[1030.20 → 1030.80] The 4Q,
[1031.52 → 1033.30] there's a big list
[1033.30 → 1034.42] of things
[1034.42 → 1035.00] that we've wanted
[1035.00 → 1036.06] to have since day one.
[1036.98 → 1037.74] Me and Tom and PJ
[1037.74 → 1038.38] are pretty good friends
[1038.38 → 1040.52] so we'd hang out
[1040.52 → 1041.40] outside of work,
[1041.52 → 1042.60] outside of hobby time,
[1042.68 → 1042.88] you know,
[1042.96 → 1044.02] and we would eat dinner
[1044.02 → 1044.44] and drink it.
[1044.50 → 1045.06] We'd talk about
[1045.06 → 1045.70] what do we want
[1045.70 → 1046.72] for GitHub in the future.
[1046.72 → 1048.64] and two of the biggest things
[1048.64 → 1049.38] early on
[1049.38 → 1051.52] were GIST
[1051.52 → 1053.18] and the 4Q.
[1054.14 → 1055.48] The idea behind the 4Q
[1055.48 → 1058.08] for anyone that's not familiar
[1058.08 → 1059.64] is you can go to a page
[1059.64 → 1060.42] on a repository
[1060.42 → 1061.88] that you own
[1061.88 → 1062.98] or you have right access to
[1062.98 → 1064.24] and you can see a list
[1064.24 → 1065.12] of all the commits
[1065.12 → 1066.08] in your network
[1066.08 → 1067.40] that are unique.
[1067.74 → 1069.42] So if I forked your project
[1069.42 → 1070.30] and I made a commit
[1070.30 → 1071.78] but I didn't even tell you about it
[1071.78 → 1072.80] and I pushed it to GitHub,
[1073.10 → 1073.94] you would see that commit
[1073.94 → 1074.60] in your 4Q
[1074.60 → 1075.60] and you could then
[1075.60 → 1076.32] examine the commit,
[1076.32 → 1077.32] you can see what I did,
[1077.62 → 1078.62] you could leave a comment on it
[1078.62 → 1079.76] or you could check a box
[1079.76 → 1081.10] and you could have that commit
[1081.10 → 1082.22] if it applies cleanly
[1082.22 → 1083.98] applied directly to your master
[1083.98 → 1084.72] or some other branch
[1084.72 → 1085.50] on your repository.
[1085.68 → 1086.22] So in this way,
[1086.28 → 1086.98] you can kind of,
[1087.40 → 1087.60] you know,
[1087.64 → 1089.20] merge changes from your iPhone
[1089.20 → 1089.90] if you want
[1089.90 → 1091.56] or you can sort of review changes
[1091.56 → 1092.38] that people are just
[1092.38 → 1093.46] experimenting with
[1093.46 → 1095.58] or kind of help them out
[1095.58 → 1096.70] if you see them making things
[1096.70 → 1098.74] that you don't think is right
[1098.74 → 1099.42] or if they're not using
[1099.42 → 1100.08] the right methods
[1100.08 → 1100.86] even before they come
[1100.86 → 1101.56] ask you for help.
[1101.64 → 1103.10] So you can really be proactive
[1103.10 → 1104.12] about being a contributor
[1104.12 → 1105.36] if you want to take that control.
[1105.36 → 1106.48] And like I said,
[1106.52 → 1107.24] the best part of it though
[1107.24 → 1108.28] is being able to merge
[1108.28 → 1109.60] in changes that apply cleanly
[1109.60 → 1110.84] right from the web interface.
[1111.34 → 1112.74] It could be documentation fixes,
[1113.34 → 1114.04] little changes.
[1115.04 → 1115.26] You know,
[1115.30 → 1116.24] if you even have your project
[1116.24 → 1117.30] hooked up to a service
[1117.30 → 1118.14] like Runcorn,
[1118.48 → 1119.60] which will run your test suite
[1119.60 → 1120.18] on commit,
[1120.60 → 1121.42] you can apply changes
[1121.42 → 1122.02] from the site
[1122.02 → 1123.40] on the 4Q
[1123.40 → 1124.90] and then see if they pass
[1124.90 → 1125.26] or not
[1125.26 → 1126.78] on the continuous integration server,
[1126.88 → 1127.62] which is pretty cool too.
[1127.62 → 1128.90] That is very awesome.
[1129.08 → 1129.68] So the
[1130.54 → 1131.80] apply cleanly
[1131.80 → 1133.00] and will not apply cleanly.
[1133.16 → 1134.30] Is that built into Git
[1134.30 → 1135.10] or did you guys have to build
[1135.10 → 1136.10] some features around that?
[1136.66 → 1137.26] That's a
[1137.78 → 1138.74] we had to build a lot of features
[1138.74 → 1139.32] around the 4Q.
[1139.46 → 1140.90] The 4Q is entirely a production
[1140.90 → 1141.42] of Scott Charon.
[1141.74 → 1141.92] We,
[1142.92 → 1144.02] when we brought him on board,
[1144.16 → 1144.54] we actually,
[1145.00 → 1146.30] some of our first hiring talks
[1146.30 → 1146.80] with him
[1146.80 → 1148.34] were us discussing
[1148.34 → 1149.12] how would you implement
[1149.12 → 1149.78] this idea.
[1150.22 → 1150.76] We have
[1150.76 → 1151.94] these random,
[1152.18 → 1152.72] not random,
[1152.80 → 1153.86] but these connected repositories
[1153.86 → 1154.54] that are disparate
[1154.54 → 1156.36] on the site
[1156.36 → 1157.64] and they have unique commits
[1157.64 → 1158.34] and we want to apply them
[1158.34 → 1158.86] to each other.
[1158.98 → 1159.78] We want to see if they work,
[1159.84 → 1160.44] we want to see if they don't work.
[1160.48 → 1161.16] How would you do that?
[1161.26 → 1162.14] And that was kind of his interview,
[1162.24 → 1162.44] I guess,
[1162.46 → 1163.22] without him knowing it.
[1163.54 → 1164.82] And he explained it to us
[1164.82 → 1166.28] and we had no idea
[1166.28 → 1166.90] what he just said.
[1166.96 → 1167.76] So we decided to hire him
[1167.76 → 1168.44] and let him implement it.
[1168.88 → 1169.72] And yeah,
[1169.72 → 1170.44] a lot of the stuff
[1170.44 → 1171.38] is pretty interesting.
[1171.98 → 1172.76] The biggest problem
[1172.76 → 1173.30] with the 4Q
[1173.30 → 1175.62] is that it uses a cherry-pick,
[1176.08 → 1176.96] which basically takes
[1176.96 → 1177.76] the diff of a commit
[1177.76 → 1178.60] and applies it
[1178.60 → 1179.78] on top of your current head.
[1180.38 → 1181.14] So that way,
[1181.28 → 1182.10] the SHA changes,
[1182.46 → 1183.34] the heritage changes
[1183.34 → 1184.06] and all that sort of thing,
[1184.06 → 1185.02] including the commit time.
[1185.46 → 1186.10] But what that means
[1186.10 → 1187.88] is that the other really cool
[1187.88 → 1189.64] sort of community feature
[1189.64 → 1189.98] of GitHub,
[1190.22 → 1190.94] the network graph,
[1191.26 → 1192.14] doesn't work right now
[1192.14 → 1192.72] with the 4Q
[1192.72 → 1193.92] because the network graph
[1193.92 → 1195.26] works all based on merges
[1195.26 → 1196.50] if the 4Q works
[1196.50 → 1197.28] based on cherry-pick.
[1197.38 → 1198.42] So we're kind of still,
[1198.78 → 1198.94] yeah,
[1198.94 → 1199.48] there's lots of stuff
[1199.48 → 1200.12] we have to do
[1200.12 → 1201.24] right into our site,
[1201.40 → 1202.34] kind of piece,
[1203.18 → 1204.44] bits of get together
[1204.44 → 1205.18] to get the functionality
[1205.18 → 1205.68] we want.
[1205.80 → 1206.86] But it's actually
[1206.86 → 1208.00] not that hard
[1208.00 → 1208.76] when you have someone
[1208.76 → 1209.28] like Scott
[1209.28 → 1209.98] who understands
[1209.98 → 1211.04] how Git works.
[1211.10 → 1211.68] It's all just a matter
[1211.68 → 1212.34] of time
[1212.34 → 1213.58] and implementation.
[1214.90 → 1215.84] Talk a bit about
[1215.84 → 1217.44] the open source projects
[1217.44 → 1218.04] that you guys have had
[1218.04 → 1219.00] to release along the way
[1219.00 → 1220.08] just to power GitHub
[1220.08 → 1220.80] if you would for a moment.
[1221.70 → 1222.12] Oh, sure.
[1222.32 → 1224.54] We've been releasing
[1224.54 → 1225.46] open source projects
[1225.46 → 1226.94] on behalf of GitHub
[1226.94 → 1227.64] the whole time
[1227.64 → 1228.34] since the beginning,
[1228.46 → 1229.44] probably before the first day,
[1229.50 → 1229.72] really.
[1231.16 → 1232.34] Because we are all
[1232.34 → 1233.36] open source developers
[1233.36 → 1234.06] and it's just kind of
[1234.06 → 1234.58] what you do.
[1234.76 → 1235.62] The first one we released
[1235.62 → 1236.44] probably was Grit,
[1236.52 → 1237.72] which is our
[1237.72 → 1239.82] Ruby bindings to Git.
[1239.82 → 1240.90] and originally
[1240.90 → 1241.54] it would just
[1241.54 → 1242.86] do a fork and exec
[1242.86 → 1243.60] and just return
[1243.60 → 1244.84] a string from a command.
[1244.98 → 1245.70] So if you wanted to see
[1245.70 → 1247.74] a Git commit log message,
[1248.42 → 1249.34] you would just run
[1249.34 → 1250.18] Git commit
[1250.18 → 1251.82] and scrape out
[1251.82 → 1252.64] the message.
[1253.12 → 1254.16] And it worked
[1254.16 → 1255.56] and in the early days
[1255.56 → 1256.10] it was enough.
[1256.26 → 1257.54] But then once the site
[1257.54 → 1258.48] started getting more popular,
[1258.80 → 1259.36] that turned out to be
[1259.36 → 1260.52] a really slow approach.
[1261.30 → 1262.10] And so what Scott did
[1262.10 → 1262.70] was re-implement
[1262.70 → 1263.98] lots of gits itself
[1263.98 → 1265.04] in Ruby for us
[1265.04 → 1266.04] within the Grit library.
[1266.04 → 1267.54] And that's all open source
[1267.54 → 1268.70] and you can check that out.
[1268.78 → 1269.40] So that's kind of
[1269.40 → 1270.82] our first big library
[1270.82 → 1271.64] because it enabled us
[1271.64 → 1272.18] to build GitHub.
[1272.88 → 1273.58] It enabled us
[1273.58 → 1274.22] to kind of
[1274.22 → 1275.90] do these major changes
[1275.90 → 1276.46] to Grit.
[1276.70 → 1277.34] Like for instance,
[1277.42 → 1277.92] rewriting it
[1277.92 → 1278.72] from fork exec
[1278.72 → 1280.66] to actually using file read
[1280.66 → 1281.30] and that sort of thing
[1281.30 → 1282.38] without having to change
[1282.38 → 1283.02] the web app
[1283.02 → 1285.40] or our jobs
[1285.40 → 1286.20] or any of this sort of things.
[1286.28 → 1286.74] So that's been
[1286.74 → 1287.48] a real lifesaver.
[1287.88 → 1287.98] I mean,
[1288.00 → 1288.44] it would have been easy
[1288.44 → 1290.46] just to throw the Git calls
[1290.46 → 1291.16] in there originally,
[1291.46 → 1292.66] but that would have
[1292.66 → 1293.30] definitely been a pain
[1293.30 → 1293.78] in the long run.
[1293.88 → 1294.72] So Grit was a good decision
[1294.72 → 1295.22] early on.
[1295.22 → 1296.14] We've released
[1296.14 → 1296.68] tons of little
[1296.68 → 1298.14] jQuery plugins.
[1298.56 → 1299.12] Some of them
[1299.12 → 1299.48] are released
[1299.48 → 1300.08] at GitHub.com
[1300.08 → 1300.64] slash GitHub.
[1300.70 → 1301.04] The other ones
[1301.04 → 1301.64] we kind of just
[1301.64 → 1303.60] release on our own.
[1303.88 → 1305.04] The next big project
[1305.04 → 1305.40] that we released
[1305.40 → 1306.34] was GitHub services.
[1306.92 → 1307.36] This is actually
[1307.36 → 1308.38] a part of GitHub itself.
[1308.88 → 1310.30] When you make a push,
[1310.72 → 1311.98] there's a post-receive hook
[1311.98 → 1312.74] that Git runs.
[1313.08 → 1313.46] And so
[1313.46 → 1314.94] because we don't want
[1314.94 → 1315.42] people running
[1315.42 → 1317.60] code on our server
[1317.60 → 1318.32] that's untrusted,
[1318.74 → 1319.84] what we do is
[1319.84 → 1320.66] we will either make
[1320.66 → 1321.12] a web hook
[1321.12 → 1322.28] to a URL of your choice
[1322.28 → 1323.40] with a JSON payload
[1323.40 → 1324.66] representing the push
[1324.66 → 1326.96] or if you have
[1326.96 → 1327.62] your own service
[1327.62 → 1328.50] that is able
[1328.50 → 1329.64] to consume
[1329.64 → 1330.92] a GitHub web hook,
[1331.18 → 1331.56] you can write
[1331.56 → 1332.30] your own service.
[1332.84 → 1333.62] And what that is,
[1333.64 → 1334.08] it's a little
[1334.08 → 1334.92] Sinatra app
[1334.92 → 1335.94] plugin thingy.
[1336.28 → 1337.22] And then what we'll do
[1337.22 → 1337.98] is we'll list it on the site
[1337.98 → 1338.82] and people can enable it.
[1338.86 → 1339.52] So for instance,
[1340.26 → 1341.54] if you have Campfire
[1341.54 → 1342.62] and you want to get
[1342.62 → 1343.70] your push notifications
[1343.70 → 1345.00] in your Campfire chat room,
[1345.18 → 1346.08] you can turn on
[1346.08 → 1346.76] the Campfire service
[1346.76 → 1347.74] and type in your username
[1347.74 → 1348.44] and token
[1348.44 → 1349.06] and all that stuff
[1349.06 → 1349.56] and it'll work.
[1349.96 → 1350.60] And so the actual
[1350.60 → 1351.22] GitHub services
[1351.22 → 1351.86] like Campfire,
[1352.04 → 1352.50] IRC,
[1352.50 → 1353.14] all those things,
[1353.16 → 1353.96] those are all open sources.
[1354.58 → 1355.32] So in many cases,
[1355.32 → 1356.02] we've had people
[1356.02 → 1357.56] like Amy Hoy
[1357.56 → 1358.68] and Thomas Fuchs's Freckle
[1358.68 → 1360.02] where they contributed
[1360.02 → 1360.74] their own service hook
[1360.74 → 1361.44] for their service
[1361.44 → 1361.94] and we were able
[1361.94 → 1362.40] to roll it out
[1362.40 → 1362.98] into the site.
[1363.46 → 1364.30] And that's really awesome
[1364.30 → 1365.12] for us because a lot
[1365.12 → 1365.58] of times we'll have
[1365.58 → 1366.16] people saying
[1366.16 → 1366.84] you should really
[1366.84 → 1367.50] support Freckle,
[1367.60 → 1367.94] you should really
[1367.94 → 1369.06] support Pivotal Tracker
[1369.06 → 1370.24] and we don't use
[1370.24 → 1370.68] the tool.
[1371.34 → 1371.60] I mean,
[1371.62 → 1372.18] if you don't use
[1372.18 → 1372.52] the tool,
[1372.70 → 1373.14] it's not going
[1373.14 → 1373.72] to be as good
[1373.72 → 1374.82] as it would be
[1374.82 → 1375.54] if the maintainer
[1375.54 → 1375.78] was someone
[1375.78 → 1376.50] who actively used it.
[1376.62 → 1377.94] So we don't use
[1377.94 → 1378.60] Pivotal Tracker,
[1378.76 → 1379.16] for instance,
[1379.24 → 1379.64] even though it's
[1379.64 → 1380.34] a good project.
[1380.70 → 1381.38] So the Pivotal Tracker
[1381.38 → 1381.90] hook would never
[1381.90 → 1382.94] really be that great.
[1383.30 → 1383.76] We wouldn't really
[1383.76 → 1384.44] know when it broke.
[1384.98 → 1385.80] It just wouldn't be
[1385.80 → 1386.98] a good kind of
[1386.98 → 1387.82] display of GitHub
[1387.82 → 1388.52] and I think
[1388.52 → 1389.66] what's more GitHub-is
[1389.66 → 1390.40] and a better display
[1390.40 → 1391.54] is making it open source
[1391.54 → 1392.28] so people can either
[1392.28 → 1393.22] fix it themselves
[1393.22 → 1394.14] or if they don't
[1394.14 → 1394.74] even know Ruby,
[1394.86 → 1395.50] we can kind of say
[1395.50 → 1396.24] here's the code,
[1396.30 → 1396.90] here's what it's doing,
[1396.98 → 1397.88] did the API change
[1397.88 → 1398.52] and work with them
[1398.52 → 1399.38] and everyone kind of
[1399.38 → 1400.24] has the same thing
[1400.24 → 1400.70] in their site,
[1400.80 → 1401.36] which is the code.
[1402.38 → 1402.84] So that project
[1402.84 → 1404.08] is really an exciting one.
[1404.66 → 1405.66] And then some of the
[1405.66 → 1406.08] other big ones
[1406.08 → 1407.14] we have been Jekyll,
[1407.40 → 1408.96] which is Tom Preston Werner's
[1408.96 → 1409.84] static site generator
[1409.84 → 1410.76] and that's actually
[1410.76 → 1411.58] integrated into GitHub.
[1411.86 → 1412.96] So we have this,
[1413.36 → 1414.08] one of these other things
[1414.08 → 1414.86] we always wanted to do
[1414.86 → 1416.74] was static site hosting,
[1417.16 → 1417.94] which we call pages.
[1418.60 → 1419.90] And so you can put
[1419.90 → 1421.22] your index.html,
[1421.34 → 1421.90] whatever you want,
[1421.96 → 1423.28] into a Git repository,
[1423.82 → 1424.48] either standalone
[1424.48 → 1425.88] or on a special magic branch
[1425.88 → 1427.36] called faces.
[1427.88 → 1428.66] And what we'll do
[1428.66 → 1429.26] is we'll publish
[1429.26 → 1430.44] the HTML
[1430.44 → 1431.20] and all the assets
[1431.20 → 1431.74] and everything
[1431.74 → 1433.38] as a static site.
[1433.38 → 1435.44] So it'll be fast.
[1435.56 → 1436.88] It'll be whatever
[1436.88 → 1438.02] exactly what you want it to be.
[1438.28 → 1439.24] But if you want to use it
[1439.24 → 1440.14] for publishing a blog,
[1440.28 → 1441.06] we actually run it
[1441.06 → 1441.56] through Jekyll.
[1441.72 → 1442.74] So you can go to
[1442.74 → 1443.62] pages.git.com
[1443.62 → 1444.52] and get the scoop there.
[1444.78 → 1445.80] You follow a few conventions,
[1446.06 → 1447.08] give us a special layout,
[1447.20 → 1447.84] that sort of thing.
[1448.04 → 1449.76] We'll turn your.markdown
[1449.76 → 1452.10] or.textile posts
[1452.10 → 1453.40] into HTML
[1453.40 → 1454.24] just the way you would
[1454.24 → 1454.94] want to publish it,
[1455.00 → 1456.82] either as a static site publisher
[1456.82 → 1457.50] on your own
[1457.50 → 1458.24] or through WordPress
[1458.24 → 1458.86] or something like that.
[1459.06 → 1460.62] So we have a ton of blogs
[1460.62 → 1461.76] from hackers hosted at GitHub,
[1461.90 → 1462.54] which is pretty cool.
[1463.44 → 1464.60] And Jekyll is one of the
[1464.60 → 1465.38] the biggest projects on GitHub.
[1465.50 → 1466.06] People fork it.
[1466.12 → 1466.74] They add features.
[1467.00 → 1468.68] They fix bugs.
[1468.96 → 1469.58] And that's because
[1469.58 → 1472.04] they know it's being run
[1472.04 → 1472.88] when they push
[1472.88 → 1473.72] and it's running their blogs
[1473.72 → 1474.04] on GitHub
[1474.04 → 1475.60] and they can add stuff they want,
[1475.70 → 1476.58] which is pretty awesome
[1476.58 → 1477.36] if you think about it
[1477.36 → 1478.80] from a hacker perspective
[1478.80 → 1480.92] because a lot of the problems
[1480.92 → 1481.76] I have with sites
[1481.76 → 1482.94] like WordPress
[1482.94 → 1483.34] and whatever
[1483.34 → 1484.74] is I can't modify them
[1484.74 → 1485.94] or I can modify them
[1485.94 → 1486.84] after paying them money.
[1487.16 → 1488.00] So at that point,
[1488.04 → 1489.00] I'd much rather just go build
[1489.00 → 1491.02] this huge 10,000 line system
[1491.02 → 1491.60] on my own
[1491.60 → 1492.72] than pay them five bucks
[1492.72 → 1493.74] a month to modify the CSS.
[1494.44 → 1495.44] And so having Jekyll
[1495.44 → 1496.38] open source is pretty cool.
[1497.02 → 1498.32] I use Jekyll for my blogs too,
[1498.96 → 1499.66] reluctantly.
[1499.84 → 1500.82] I have my own static site thing
[1500.82 → 1501.24] for a while,
[1501.32 → 1502.24] but I finally switched to Jekyll
[1502.24 → 1503.00] because it's easier.
[1503.94 → 1504.66] So we have to do a lot
[1504.66 → 1506.50] for user evangelists though, right?
[1506.56 → 1508.14] Like if everybody is using
[1508.14 → 1509.32] something that's already
[1509.32 → 1510.56] on GitHub like Jekyll,
[1510.66 → 1511.40] it's already open source
[1511.40 → 1512.90] and they're always putting
[1512.90 → 1514.56] the fork me badge
[1514.56 → 1515.26] up in the top right
[1515.26 → 1516.00] and they're always putting
[1516.00 → 1518.06] attributes back to
[1518.06 → 1518.94] the Jekyll repo,
[1518.94 → 1519.84] it's always going to drive
[1519.84 → 1520.64] more and more traffic
[1520.64 → 1522.48] back to GitHub.
[1523.62 → 1524.52] Yeah, that's true.
[1524.72 → 1525.52] But, you know,
[1525.68 → 1526.76] we don't really think
[1526.76 → 1527.32] of it that way though
[1527.32 → 1528.78] because you can try
[1528.78 → 1530.12] and do user evangelism
[1530.12 → 1530.50] actively.
[1530.78 → 1531.90] You can have the fork you badges
[1531.90 → 1532.88] and you can have
[1532.88 → 1534.18] sort of like an open source Jekyll,
[1534.64 → 1535.54] but people aren't going to care
[1535.54 → 1536.28] if it's all crap.
[1536.66 → 1537.84] So I think the more important thing
[1537.84 → 1538.40] is making something
[1538.40 → 1539.22] really, perfect
[1539.22 → 1541.30] and then in the spare time
[1541.30 → 1542.36] trying to put together
[1542.36 → 1543.54] a little bit of user evangelism
[1543.54 → 1544.42] stuff to let them do
[1544.42 → 1545.06] what they want with it.
[1545.06 → 1546.50] So like the fork you badges
[1546.50 → 1547.36] didn't take more than
[1547.36 → 1548.30] an afternoon for Tom
[1548.30 → 1549.56] or fork me on GitHub badges.
[1549.72 → 1550.56] But, you know,
[1550.60 → 1551.64] the thing that took all the time
[1551.64 → 1552.30] was making pages
[1552.30 → 1553.14] really, perfect.
[1553.50 → 1554.02] One of the cool things
[1554.02 → 1554.50] about pages
[1554.50 → 1555.54] that people don't realize
[1555.54 → 1557.44] is we had a period
[1557.44 → 1558.10] of time last year
[1558.10 → 1558.92] we had lots of downtime
[1558.92 → 1560.30] and our site was always crashing
[1560.30 → 1560.98] and it was because of
[1560.98 → 1562.68] some of our data storage problems.
[1563.24 → 1564.06] But throughout that time
[1564.06 → 1565.16] pages was always still up
[1565.16 → 1566.22] because it was a different machine.
[1566.34 → 1567.04] It was NGINX.
[1567.20 → 1568.20] It was all cached.
[1568.40 → 1569.16] It was all static.
[1569.60 → 1570.18] So GitHub itself
[1570.18 → 1571.40] would be down and flailing
[1571.40 → 1572.56] but your blog
[1572.56 → 1573.52] would just be running fine
[1573.52 → 1574.28] and Noah would notice.
[1574.28 → 1575.70] And even on the current setup
[1575.70 → 1576.36] that's how it is now.
[1576.44 → 1577.06] We have things started
[1577.06 → 1577.58] in such a way
[1577.58 → 1578.92] that if, you know,
[1578.96 → 1580.12] the web app falls over
[1580.12 → 1581.20] your pages will be fine
[1581.20 → 1581.68] and they'll probably
[1581.68 → 1582.56] still generate too.
[1583.56 → 1585.06] That might be a nice segue
[1585.06 → 1586.56] into those trials
[1586.56 → 1587.16] and tribulations
[1587.16 → 1589.02] of switching hosts.
[1589.70 → 1590.80] Is there a possibility
[1590.80 → 1591.56] you could talk about
[1591.56 → 1592.72] the transition
[1592.72 → 1593.52] and the relationship
[1593.52 → 1594.62] ending with EGINHARD
[1594.62 → 1596.24] and what that took you
[1596.24 → 1596.94] into with Rackspace
[1596.94 → 1598.04] and why that came about?
[1598.78 → 1599.32] Yeah, sure.
[1599.90 → 1601.20] We posted about
[1601.20 → 1602.54] all of it on our blog.
[1602.54 → 1604.36] There are so many reasons
[1604.36 → 1604.96] going into it.
[1605.04 → 1606.22] We used EGINHARD
[1606.22 → 1608.00] since almost the very beginning.
[1608.44 → 1609.80] We've got lots of great relationships
[1609.80 → 1610.66] with those people over there,
[1610.78 → 1611.66] especially people like
[1611.66 → 1613.26] Yehuda and Ezra
[1613.26 → 1614.74] and Atmos.
[1615.32 → 1616.24] There's a lot of really smart,
[1616.32 → 1616.92] really awesome people
[1616.92 → 1617.66] over at EGINHARD.
[1617.66 → 1620.38] and they are able
[1620.38 → 1621.60] to recognize, I guess,
[1622.92 → 1623.16] you know,
[1623.24 → 1624.22] up-and-coming projects
[1624.22 → 1625.02] in the Ruby world
[1625.02 → 1625.60] really well.
[1625.76 → 1626.48] When GitHub was still
[1626.48 → 1628.88] just a baby, really,
[1629.22 → 1630.28] they saw it,
[1630.32 → 1631.12] they latched onto it,
[1631.16 → 1631.76] and they really wanted
[1631.76 → 1632.20] to help make it
[1632.20 → 1632.72] something great.
[1633.16 → 1633.84] They are really behind
[1633.84 → 1634.52] the idea of Git.
[1634.72 → 1635.36] They're really into
[1635.36 → 1636.92] the future of open source.
[1637.46 → 1638.10] And I think they're really
[1638.10 → 1639.68] invested in, you know,
[1640.10 → 1641.12] open source in Ruby,
[1641.32 → 1642.80] making sure that Ruby
[1642.80 → 1643.68] continues to be like
[1643.68 → 1644.84] an open source-driven community,
[1644.84 → 1645.52] even though they're
[1645.52 → 1646.30] a for-profit company.
[1646.30 → 1648.98] So we were a part of that
[1648.98 → 1649.58] for a long time.
[1649.66 → 1650.28] We had a good relationship
[1650.28 → 1650.80] with them.
[1651.58 → 1652.48] Randall Thomas over there
[1652.48 → 1653.64] took great care of us
[1653.64 → 1655.02] and is a pretty cool guy.
[1655.36 → 1656.32] And then eventually
[1656.32 → 1657.08] it came to a point
[1657.08 → 1658.56] where we decided
[1658.56 → 1659.12] on our own
[1659.12 → 1659.64] that we didn't want
[1659.64 → 1660.14] to run on
[1660.14 → 1661.98] virtualized hardware
[1661.98 → 1662.58] anymore, really.
[1663.14 → 1664.22] And, you know,
[1664.28 → 1665.78] EGINHARD can host us
[1665.78 → 1667.10] on our own machines,
[1667.42 → 1668.00] you know,
[1668.02 → 1668.92] without virtualization,
[1669.12 → 1670.06] but that's not really
[1670.06 → 1671.30] their business.
[1671.90 → 1672.34] It's like,
[1673.16 → 1673.76] yes, you can do
[1673.76 → 1674.48] a subversion import
[1674.48 → 1674.90] to GitHub,
[1674.90 → 1676.24] but we're not
[1676.24 → 1676.68] going to keep
[1676.68 → 1677.18] two-way,
[1677.32 → 1677.48] you know,
[1677.52 → 1678.84] just go to a subversion
[1678.84 → 1679.66] host, pretty much,
[1679.74 → 1680.54] is what it boils down to.
[1680.96 → 1681.68] So for us,
[1681.70 → 1682.34] we wanted to find
[1682.34 → 1683.06] a host that,
[1683.36 → 1683.78] you know,
[1683.84 → 1685.16] was designed
[1685.16 → 1687.48] to deal with
[1687.48 → 1688.12] the setup that we
[1688.12 → 1688.88] wanted to move to.
[1689.42 → 1689.98] And, you know,
[1690.02 → 1690.68] it's not EGINHARD.
[1690.84 → 1691.48] We wrote them
[1691.48 → 1691.98] an email,
[1692.06 → 1692.66] we talked to them,
[1692.84 → 1693.44] they said,
[1693.54 → 1694.26] yeah, we understand
[1694.26 → 1695.26] that works for both
[1695.26 → 1695.90] of us really well.
[1696.44 → 1698.42] We talked about
[1698.42 → 1699.18] a migration strategy,
[1699.18 → 1699.78] they helped us
[1699.78 → 1700.34] by dumping all
[1700.34 → 1700.82] of the repos
[1700.82 → 1701.92] onto databases,
[1701.92 → 1702.62] which we then
[1702.62 → 1703.52] flew to Virginia
[1703.52 → 1705.28] for our import,
[1705.58 → 1705.74] you know,
[1705.80 → 1706.42] kind of sneaker
[1706.42 → 1707.22] net operation.
[1708.68 → 1710.14] And, yeah,
[1710.22 → 1711.22] so then at Rackspace,
[1711.80 → 1712.72] things are really great.
[1712.94 → 1714.02] We have too many
[1714.02 → 1714.62] machines right now,
[1714.66 → 1715.08] which is good.
[1715.20 → 1715.86] We have way too
[1715.86 → 1716.36] much power,
[1717.12 → 1718.38] and we've got a
[1718.38 → 1718.94] pretty good relationship
[1718.94 → 1719.54] with those people.
[1720.12 → 1721.16] And we have Anchored,
[1721.30 → 1722.34] which is a company
[1722.34 → 1723.44] down in Australia,
[1723.64 → 1724.82] doing our support for us.
[1724.82 → 1726.28] So Rackspace handles
[1726.28 → 1726.74] the hardware,
[1726.94 → 1727.86] and Anchor handles
[1727.86 → 1728.34] the software.
[1728.34 → 1729.26] So it's really great
[1729.26 → 1730.10] to have someone
[1730.10 → 1731.20] who is really,
[1731.32 → 1732.52] really invested
[1732.52 → 1733.62] and interested in,
[1733.62 → 1734.52] you know,
[1734.56 → 1736.04] software systems
[1736.04 → 1736.50] administration.
[1736.72 → 1737.54] So now we're all
[1737.54 → 1738.58] set up with Puppet
[1738.58 → 1739.36] and all of that
[1739.36 → 1739.90] sort of thing.
[1740.32 → 1741.30] And the guys at Anchor
[1741.30 → 1742.18] are, you know,
[1742.20 → 1743.02] they have checklists
[1743.02 → 1744.32] and all these sort
[1744.32 → 1745.30] of procedures in place.
[1745.40 → 1746.12] It's very professional.
[1746.78 → 1747.52] People are on call
[1747.52 → 1748.18] 24-7,
[1748.60 → 1749.20] and they're always there
[1749.20 → 1749.88] to help us out
[1749.88 → 1750.88] in case we're in a problem.
[1751.02 → 1751.70] So it's really great
[1751.70 → 1752.26] because Engine Yard
[1752.26 → 1753.20] provided a lot of that too.
[1753.30 → 1753.94] We had sort of
[1753.94 → 1755.34] an Engine Yard chat room
[1755.34 → 1756.24] or a private GitHub
[1756.24 → 1757.08] Engine Yard chat room.
[1757.42 → 1758.22] And if there's a problem,
[1758.34 → 1759.20] at any hour of the day,
[1759.26 → 1759.84] you can go in there
[1759.84 → 1760.18] and you can say,
[1760.24 → 1761.08] hey, something's busted.
[1761.58 → 1762.04] And that's kind of
[1762.04 → 1763.04] the appeal of Engine Yard
[1763.04 → 1764.24] is they always have
[1764.24 → 1764.76] people around
[1764.76 → 1765.24] that are familiar
[1765.24 → 1765.74] with the setup
[1765.74 → 1766.46] because all the setups
[1766.46 → 1767.40] are kind of very similar.
[1767.62 → 1768.86] And that's what you pay for.
[1769.60 → 1770.80] And so we didn't really
[1770.80 → 1771.56] want to lose that
[1771.56 → 1772.52] because that's really
[1772.52 → 1773.14] one of the most
[1773.14 → 1773.56] awesome things
[1773.56 → 1774.12] about Engine Yard.
[1774.44 → 1775.44] And Anchor's really helped that
[1775.44 → 1776.32] and they've really stepped it up.
[1776.86 → 1777.26] And they have some
[1777.26 → 1777.98] really great people down there.
[1778.04 → 1778.48] Matt Palmer,
[1778.90 → 1779.22] Wobble,
[1779.46 → 1780.90] has totally led
[1780.90 → 1781.80] with Tom,
[1781.90 → 1782.50] the rear protecting
[1782.50 → 1782.94] of the site,
[1783.02 → 1783.52] and it's just been
[1783.52 → 1784.36] fabulous since then.
[1784.94 → 1786.42] So I think the Engine Yard
[1786.42 → 1787.62] and Rackspace move
[1787.62 → 1788.56] just boils down to
[1788.56 → 1789.54] finding the right tool
[1789.54 → 1790.08] for the job.
[1791.12 → 1793.16] Engine Yard knows that,
[1793.28 → 1793.36] I mean,
[1793.38 → 1793.80] they don't even try
[1793.80 → 1794.30] and advertise
[1794.30 → 1796.42] that they do what we want.
[1796.64 → 1797.50] And so it just didn't
[1797.50 → 1798.12] seem like a good fit.
[1798.26 → 1798.86] Whereas Rackspace,
[1799.04 → 1799.66] that's their whole business
[1799.66 → 1800.08] right there,
[1800.32 → 1801.18] or at least most of it.
[1801.28 → 1802.26] Now they're trying to do the
[1802.82 → 1803.16] or they're moving
[1803.16 → 1803.98] into the cloud space,
[1804.06 → 1804.82] which Engine Yard is too.
[1804.92 → 1805.60] So that's interesting
[1805.60 → 1806.18] because I guess now
[1806.18 → 1807.80] they're more competitors
[1807.80 → 1808.46] than they used to be.
[1808.70 → 1810.16] But for us,
[1810.18 → 1810.60] it's mainly about
[1810.60 → 1811.36] the dedicated hardware
[1811.36 → 1812.64] and the control over
[1812.64 → 1813.72] exactly what hardware we have
[1813.72 → 1814.22] and when we get it
[1814.22 → 1814.74] and that sort of thing.
[1815.16 → 1815.76] Let's talk about
[1815.76 → 1818.12] the very extremely short
[1818.12 → 1820.76] tagline that GitHub has,
[1820.84 → 1822.08] which is just social coding.
[1822.20 → 1822.96] Can you talk about that
[1822.96 → 1823.70] and where that came from?
[1824.40 → 1824.72] Sure.
[1824.90 → 1825.42] I think it,
[1825.58 → 1827.16] we had a couple of taglines.
[1827.28 → 1827.82] I think this one
[1827.82 → 1829.88] best reflects everything,
[1830.02 → 1830.60] the whole universe.
[1831.14 → 1832.62] The first couple of taglines
[1832.62 → 1833.50] were just something like
[1833.50 → 1834.88] Git code hosting
[1834.88 → 1835.98] and then,
[1836.06 → 1836.78] I think that was it,
[1836.86 → 1837.96] Git repository hosting,
[1838.06 → 1838.70] something like that.
[1838.92 → 1839.90] Because that's really
[1839.90 → 1840.76] what it was at the time
[1840.76 → 1841.70] and that's what we wanted it to be.
[1841.70 → 1842.70] That's what we were advertising.
[1842.70 → 1843.26] It says,
[1843.38 → 1843.54] hey,
[1843.96 → 1844.70] if you use Git,
[1844.94 → 1845.46] come to GitHub
[1845.46 → 1846.94] because we can host your stuff.
[1847.78 → 1848.34] And that was sort of
[1848.34 → 1849.84] the origin of the site.
[1850.58 → 1851.36] And then after that,
[1851.42 → 1852.46] when we started realizing
[1852.46 → 1854.20] what was going on
[1854.20 → 1855.08] and the sort of
[1855.08 → 1856.42] how this collaboration stuff
[1856.42 → 1857.04] was actually working
[1857.04 → 1858.12] much better than we had hoped
[1858.12 → 1858.80] or thought it would,
[1859.16 → 1859.98] we turned it into
[1859.98 → 1860.94] social code hosting,
[1861.02 → 1861.34] I think,
[1862.10 → 1862.44] because,
[1862.52 → 1863.00] you know,
[1863.02 → 1863.84] we were starting to get
[1863.84 → 1866.34] compared to Facebook
[1866.34 → 1866.94] and MySpace
[1866.94 → 1868.10] and all this sort of,
[1868.10 → 1868.32] you know,
[1868.42 → 1868.94] jibber jabber
[1868.94 → 1869.94] with the Web 2.0
[1869.94 → 1870.76] social sphere.
[1870.76 → 1872.26] So we added social code hosting.
[1872.66 → 1873.36] And finally,
[1873.50 → 1874.56] Tom and PJ decided
[1874.56 → 1876.18] that they didn't like
[1876.18 → 1876.90] that tagline
[1876.90 → 1878.44] because it gave the logo
[1878.44 → 1879.08] sort of tail
[1879.08 → 1879.76] and they needed to come up
[1879.76 → 1880.28] with something shorter.
[1881.16 → 1883.10] And in a moment of inspiration,
[1883.10 → 1884.36] they came up with social coding,
[1884.62 → 1886.24] which kind of perfectly explains
[1886.24 → 1887.00] what GitHub is about.
[1887.48 → 1888.16] Because it's not even really
[1888.16 → 1889.26] about the hosting anymore
[1889.26 → 1890.20] because that's kind of,
[1890.62 → 1890.76] you know,
[1890.78 → 1891.74] you can get hosting anywhere
[1891.74 → 1892.58] probably for free.
[1892.80 → 1893.70] It's more about
[1893.70 → 1894.72] the socialness
[1894.72 → 1896.62] and just actually coding,
[1896.96 → 1898.20] not any sort of
[1898.20 → 1900.06] really like politics
[1900.06 → 1902.80] or organizational stuff
[1902.80 → 1903.56] or hierarchies
[1903.56 → 1904.64] and all that sort of
[1904.64 → 1906.60] procedure that you find
[1906.60 → 1907.74] in other organizations
[1907.74 → 1908.80] that do open source stuff.
[1908.94 → 1909.24] We just,
[1909.38 → 1910.22] it's about coding really.
[1910.44 → 1911.82] Just throwing code up there
[1911.82 → 1912.98] and working on
[1912.98 → 1913.68] someone else's code
[1913.68 → 1914.32] and that sort of thing.
[1914.36 → 1914.90] We wanted it really
[1914.90 → 1916.44] to be about code
[1916.44 → 1917.04] and people
[1917.04 → 1918.56] more than projects
[1918.56 → 1919.52] and organizations.
[1920.62 → 1921.56] So two big aspects
[1921.56 → 1922.54] of that social coding
[1922.54 → 1924.06] philosophy
[1924.06 → 1925.96] is following users
[1925.96 → 1926.56] and,
[1926.62 → 1927.04] you know,
[1927.04 → 1928.00] watching repos.
[1928.00 → 1929.16] Were this just no-brainer
[1929.16 → 1930.06] features out of the box
[1930.06 → 1931.00] or how did those come about?
[1932.02 → 1932.14] Yeah,
[1932.20 → 1933.14] I think those were just,
[1933.64 → 1935.56] yeah,
[1935.74 → 1936.08] we never,
[1936.42 → 1936.90] it's funny.
[1937.00 → 1937.34] I don't know.
[1937.46 → 1938.40] I don't have an answer for that.
[1938.46 → 1939.18] We just added them
[1939.18 → 1940.66] because it seemed like
[1940.66 → 1941.72] what would be the point
[1941.72 → 1942.12] of the site
[1942.12 → 1942.68] if you didn't have
[1942.68 → 1943.24] those things.
[1944.24 → 1944.70] I mean,
[1944.72 → 1945.50] originally the dashboard
[1945.50 → 1947.06] wasn't really like a
[1947.10 → 1947.58] I don't know what you would
[1947.58 → 1947.82] call it,
[1947.84 → 1949.12] a Facebook style feed
[1949.12 → 1951.84] or really like a Twitter feed
[1951.84 → 1952.84] with different event types.
[1953.24 → 1954.16] It wasn't like that originally.
[1954.16 → 1954.82] It was just,
[1955.20 → 1955.30] you know,
[1955.34 → 1956.24] here are some repositories
[1956.24 → 1957.46] that you have,
[1957.86 → 1958.68] that you're watching
[1958.68 → 1959.84] that have had updates recently
[1959.84 → 1960.46] and,
[1960.66 → 1960.76] you know,
[1960.78 → 1961.30] here's information
[1961.30 → 1962.00] about the repository
[1962.00 → 1963.32] and it was very,
[1963.46 → 1964.80] you know,
[1964.86 → 1965.46] to the point
[1965.46 → 1966.24] and then we made it
[1966.24 → 1966.84] a little bit more
[1966.84 → 1967.62] kind of like
[1967.62 → 1968.72] stream of consciousness,
[1968.98 → 1969.48] fire hose
[1969.48 → 1971.08] and that's when we realized
[1971.08 → 1972.20] a lot of these social aspects
[1972.20 → 1972.98] really coming into play
[1972.98 → 1974.02] because now we had this place
[1974.02 → 1974.62] where we could show you
[1974.62 → 1975.50] stuff that's going on,
[1976.18 → 1976.96] a lot of stuff,
[1977.04 → 1977.56] really quickly,
[1977.66 → 1978.66] a lot of different types of stuff
[1978.66 → 1980.74] and I think watching
[1980.74 → 1981.26] and following
[1981.26 → 1983.16] kind of necessitated that
[1983.16 → 1983.46] because,
[1983.56 → 1983.64] you know,
[1983.72 → 1984.00] oh,
[1984.08 → 1984.20] well,
[1984.24 → 1984.34] you know,
[1984.36 → 1984.96] I want to see
[1984.96 → 1985.88] what Tom is following
[1985.88 → 1986.90] and I want to see
[1986.90 → 1987.50] what he's watching
[1987.50 → 1989.22] and the dashboard
[1989.22 → 1990.22] really lets you do that
[1990.22 → 1991.66] in some instances
[1991.66 → 1992.50] and,
[1992.58 → 1993.06] yeah,
[1993.14 → 1993.72] that's really where
[1993.72 → 1994.10] it came from
[1994.10 → 1994.62] but watching
[1994.62 → 1995.44] and following,
[1996.16 → 1996.54] those have just
[1996.54 → 1997.22] always been in there
[1997.22 → 1997.68] and we've always
[1997.68 → 1998.60] had the distinguished,
[1998.86 → 1999.36] we've always distinguished
[1999.36 → 1999.94] between the terms
[1999.94 → 2000.66] because otherwise
[2000.66 → 2001.20] we thought it would
[2001.20 → 2001.72] get confusing
[2001.72 → 2003.24] if you watch people
[2003.24 → 2004.02] and repositories.
[2005.44 → 2005.88] Sure.
[2007.28 → 2007.72] So,
[2007.78 → 2008.22] what do you think
[2008.22 → 2009.98] the fork term
[2009.98 → 2010.92] means on GitHub
[2010.92 → 2013.32] to be popularly forked
[2013.32 → 2014.38] as the Explore GitHub
[2014.38 → 2015.34] tab shows?
[2015.98 → 2016.98] Is there a certain point
[2016.98 → 2018.14] where being forked
[2018.14 → 2018.56] too much
[2018.56 → 2019.66] may be exposing
[2019.66 → 2020.22] some flaws
[2020.22 → 2021.40] in your particular project
[2021.40 → 2022.78] or how do you see that?
[2024.00 → 2024.24] Well,
[2024.28 → 2025.10] I think it depends.
[2025.88 → 2026.18] A lot of,
[2026.38 → 2026.66] right now,
[2026.72 → 2027.44] forks are all weighted
[2027.44 → 2028.24] across GitHub
[2028.24 → 2029.02] fairly equally
[2029.02 → 2030.56] so if I fork a project
[2030.56 → 2031.50] and I make no commits
[2031.50 → 2031.80] to it,
[2031.88 → 2033.06] I don't add anything unique,
[2033.58 → 2034.58] that's pretty much seen
[2034.58 → 2035.26] as the same
[2035.26 → 2036.26] as someone who has a fork
[2036.26 → 2037.08] where he rewrites
[2037.08 → 2038.84] functionality for the better
[2038.84 → 2039.64] and submits it back
[2039.64 → 2041.22] and gets it included
[2041.22 → 2041.86] in the main line
[2041.86 → 2042.94] and so I think
[2042.94 → 2043.24] one of the things
[2043.24 → 2043.82] we want to do
[2043.82 → 2044.80] in the coming year
[2044.80 → 2045.44] and the future
[2045.44 → 2045.82] with GitHub
[2045.82 → 2046.82] is sort of
[2046.82 → 2048.14] focus on forking
[2048.14 → 2048.74] in a way.
[2049.10 → 2049.60] Make forks
[2049.60 → 2050.64] that have unique content,
[2050.72 → 2051.06] make forks
[2051.06 → 2051.50] that are good
[2051.50 → 2052.16] more prominent
[2052.16 → 2053.22] and make forks
[2053.22 → 2056.06] that have no unique content
[2056.06 → 2056.86] less prominent,
[2057.02 → 2058.14] especially old ones.
[2058.38 → 2059.24] Just get them
[2059.24 → 2060.42] out of the user interface
[2060.42 → 2061.82] and get them
[2061.82 → 2062.60] out of the network graph,
[2062.68 → 2063.34] get them out of everywhere.
[2063.50 → 2063.60] I mean,
[2063.62 → 2064.22] the network graph
[2064.22 → 2064.78] and the fork queue
[2064.78 → 2065.66] already do a good job
[2065.66 → 2065.82] of that.
[2065.88 → 2066.92] You don't see forks
[2066.92 → 2067.46] that don't have
[2067.46 → 2068.32] anything unique in them
[2068.32 → 2069.76] but in other places
[2069.76 → 2070.88] like the popular forked
[2070.88 → 2071.50] and in the little
[2071.50 → 2072.56] network count
[2072.56 → 2074.08] in the repository information
[2074.08 → 2075.80] or the network tab itself
[2075.80 → 2076.48] with the count there,
[2077.14 → 2077.84] you still see
[2077.84 → 2078.68] how many forks there are.
[2079.32 → 2079.90] So I think that's
[2079.90 → 2080.24] one of the things
[2080.24 → 2081.82] I would like to change.
[2081.90 → 2082.36] I want forking
[2082.36 → 2083.02] to be about
[2083.02 → 2083.94] contributing
[2083.94 → 2084.60] more than just
[2084.60 → 2085.14] clicking the button,
[2085.24 → 2085.86] which it is now.
[2086.06 → 2086.54] But obviously,
[2086.74 → 2087.58] counting how many people
[2087.58 → 2087.98] click the button
[2087.98 → 2088.74] is an easier technical
[2088.74 → 2089.56] problem than
[2089.56 → 2090.84] counting who actually
[2090.84 → 2091.62] has a valuable fork.
[2092.12 → 2092.72] But now that we have
[2092.72 → 2093.48] resources and people,
[2093.56 → 2094.06] that's one of the things
[2094.06 → 2094.76] we want to focus on.
[2095.10 → 2096.96] How active is a project
[2096.96 → 2098.38] based on commits,
[2098.56 → 2100.04] not just people forking it,
[2100.24 → 2100.82] that sort of thing.
[2101.46 → 2101.86] And so I think
[2101.86 → 2102.58] for things like
[2102.58 → 2103.44] Homebrew,
[2103.86 → 2104.34] you're going to see
[2104.34 → 2104.98] that this is a project
[2104.98 → 2106.12] that has a ton
[2106.12 → 2107.18] of super active forks
[2107.18 → 2107.96] because people are
[2107.96 → 2109.10] contributing formula
[2109.10 → 2109.92] and that sort of thing.
[2110.44 → 2111.74] But for a project
[2111.74 → 2112.62] like Rails,
[2113.26 → 2114.04] maybe you won't see
[2114.04 → 2114.76] as many forks
[2114.76 → 2115.40] as there are now
[2115.40 → 2116.70] because it's so popular
[2116.70 → 2118.64] that there just have to be
[2118.64 → 2119.24] a bunch of forks
[2119.24 → 2119.74] people made
[2119.74 → 2120.22] intending to make
[2120.22 → 2120.84] a patch that never
[2120.84 → 2121.28] panned out.
[2121.64 → 2122.22] There's still going to be
[2122.22 → 2123.00] a ton of forks,
[2123.28 → 2124.02] but I think the more
[2124.02 → 2124.88] popular a project is
[2124.88 → 2125.38] like Rails,
[2125.58 → 2126.36] the less forks
[2126.36 → 2126.70] are going to have
[2126.70 → 2127.92] something substantial in it.
[2127.92 → 2128.10] I mean,
[2128.10 → 2129.10] I even fork projects
[2129.10 → 2130.34] intending sometimes
[2130.34 → 2131.80] to contribute to them
[2131.80 → 2132.88] and nothing ever happens
[2132.88 → 2134.06] and I end up deleting them later
[2134.06 → 2134.64] or I think,
[2134.74 → 2135.60] why did I ever fork that?
[2136.04 → 2136.80] And that happens
[2136.80 → 2137.88] and the system just has to be
[2137.88 → 2138.68] set up to deal with that.
[2139.08 → 2140.48] But I think we can do that.
[2140.48 → 2141.10] You know,
[2141.12 → 2141.66] that's one of the things
[2141.66 → 2142.16] we discussed
[2142.16 → 2143.58] on the last show
[2143.58 → 2145.18] is oftentimes now
[2145.18 → 2146.34] with moving to Get,
[2146.96 → 2149.08] the lead project
[2149.08 → 2150.00] for a particular fork
[2150.00 → 2150.72] is basically the one
[2150.72 → 2151.38] with the most momentum
[2151.38 → 2153.08] and that's kind of a challenge
[2153.08 → 2154.70] when you find a project
[2154.70 → 2155.16] on GitHub
[2155.16 → 2155.74] is sometimes
[2155.74 → 2157.64] you may stumble
[2157.64 → 2158.32] upon a project
[2158.32 → 2159.14] and it's a fork
[2159.14 → 2160.06] of a fork of a fork
[2160.06 → 2161.76] and so just following
[2161.76 → 2162.32] the fork tree
[2162.32 → 2163.04] back to the original
[2163.04 → 2164.26] and then trying to look
[2164.26 → 2165.02] at the 52-week
[2165.02 → 2165.58] participation
[2165.58 → 2166.32] just to see,
[2166.38 → 2166.50] you know,
[2166.54 → 2167.22] where's the momentum
[2167.22 → 2168.48] for this particular project
[2168.48 → 2169.76] is often a challenge.
[2170.96 → 2171.32] Yeah,
[2171.46 → 2172.04] I usually take
[2172.04 → 2172.62] the network graph
[2172.62 → 2173.08] for that stuff
[2173.08 → 2173.74] because even on
[2173.74 → 2174.60] the fork of the fork
[2174.60 → 2175.64] you'll be able to see
[2175.64 → 2177.28] if the upstream root
[2177.28 → 2178.62] has forwarded momentum
[2178.62 → 2180.46] but that's,
[2180.52 → 2180.62] yeah,
[2180.68 → 2180.96] that's something
[2180.96 → 2181.78] you shouldn't have to do.
[2181.90 → 2182.26] That's something
[2182.26 → 2183.08] that should just be obvious
[2183.08 → 2184.30] and I think we want
[2184.30 → 2184.98] to make the networks
[2184.98 → 2185.76] a little bit more cohesive
[2185.76 → 2187.14] in the future too
[2187.14 → 2188.62] and sort of say like
[2188.62 → 2189.68] when you hit that fork
[2189.68 → 2190.52] of a fork of a fork
[2190.52 → 2190.92] say,
[2191.32 → 2191.42] hey,
[2191.50 → 2192.82] you're in the defunct
[2192.82 → 2194.44] slash rescue network,
[2194.92 → 2195.24] you know,
[2196.12 → 2197.46] Adam stack slash rescue
[2197.46 → 2198.98] is the blessed fork
[2198.98 → 2199.38] right now.
[2199.38 → 2199.98] So even though
[2199.98 → 2200.52] it might have been
[2200.52 → 2201.56] my repo at one point
[2201.56 → 2203.64] and I publicized it
[2203.64 → 2204.50] and I was the contributor
[2204.50 → 2205.78] or the main maintainer,
[2206.04 → 2207.00] now it's passed on
[2207.00 → 2207.72] to Adam stack
[2207.72 → 2208.18] and that's where
[2208.18 → 2208.94] all the momentum is
[2208.94 → 2209.60] and GitHub's able
[2209.60 → 2210.30] to detect that
[2210.30 → 2211.42] because it's really
[2211.42 → 2212.12] not that complicated.
[2212.12 → 2212.84] We just need to
[2212.84 → 2214.40] detect it and show it
[2214.40 → 2215.16] and I think that would be
[2215.16 → 2216.00] really awesome for people
[2216.00 → 2217.06] is to say like,
[2217.36 → 2217.44] hey,
[2217.48 → 2217.92] you're here
[2217.92 → 2219.10] but this doesn't matter
[2219.10 → 2220.32] as much as this one
[2220.32 → 2221.26] which you might be looking for
[2221.26 → 2221.88] or,
[2222.04 → 2222.22] you know,
[2222.26 → 2223.10] if you land on
[2223.10 → 2224.72] the fork of a fork
[2224.72 → 2225.90] and it tells you that
[2225.90 → 2226.60] you can,
[2226.64 → 2226.78] you know,
[2226.82 → 2227.18] compare,
[2227.36 → 2227.52] you know,
[2227.58 → 2228.02] what's the difference
[2228.02 → 2228.82] between this fork
[2228.82 → 2230.16] and the upstream
[2230.16 → 2231.54] and kind of get an idea
[2231.54 → 2232.16] for what's going on
[2232.16 → 2232.70] that way too
[2232.70 → 2233.04] which I think
[2233.04 → 2233.76] would also be cool.
[2234.42 → 2234.88] We're talking about
[2234.88 → 2235.68] the social aspects
[2235.68 → 2236.60] of GitHub.com
[2236.60 → 2237.72] and what's going on there.
[2238.16 → 2238.80] How has
[2238.80 → 2240.12] the explosion
[2240.12 → 2240.96] of social media
[2240.96 → 2241.50] and this,
[2241.50 → 2242.14] you know,
[2242.22 → 2242.84] constant real-time
[2242.84 → 2244.10] connection between developers?
[2244.76 → 2245.46] For example,
[2245.96 → 2246.74] when we had
[2246.74 → 2248.36] Nathan Feigenbaum
[2248.36 → 2249.26] and Chris Epstein,
[2249.62 → 2250.86] the core contributors
[2250.86 → 2251.72] to Hamill,
[2251.84 → 2252.06] SAS,
[2252.10 → 2252.48] and Compass,
[2252.48 → 2253.36] when we had them
[2253.36 → 2253.84] on the podcast,
[2253.90 → 2254.22] it was actually
[2254.22 → 2255.18] the very first podcast
[2255.18 → 2255.94] from Changelog.
[2256.46 → 2257.28] When we had them on,
[2257.66 → 2258.30] they said one of the
[2258.30 → 2259.20] the biggest things
[2259.20 → 2260.20] that helped their project
[2260.20 → 2261.40] was the activity
[2261.40 → 2261.90] on Twitter.
[2262.64 → 2263.32] How has that
[2263.32 → 2263.90] impacted GitHub?
[2264.74 → 2265.14] Well,
[2265.28 → 2266.10] for GitHub itself,
[2266.36 → 2267.66] since the very first days
[2267.66 → 2268.24] we were using
[2268.24 → 2269.56] Surmiser at the time,
[2269.72 → 2270.20] Surmise,
[2270.84 → 2271.88] just to see what people
[2271.88 → 2272.56] were saying about GitHub,
[2272.74 → 2273.38] whether it was good
[2273.38 → 2273.94] or bad,
[2274.32 → 2274.82] because it's,
[2274.88 → 2275.14] you know,
[2275.20 → 2275.86] it's so much easier
[2275.86 → 2276.38] to tweet,
[2276.72 → 2276.94] oh,
[2277.44 → 2278.32] what the heck's up
[2278.32 → 2278.90] with GitHub's
[2278.90 → 2279.50] login screen,
[2279.54 → 2279.96] it's broken,
[2280.08 → 2280.72] than it is to
[2280.72 → 2281.74] find out where
[2281.74 → 2282.36] the support email
[2282.36 → 2282.76] addresses,
[2283.24 → 2283.44] you know,
[2283.52 → 2284.02] email it,
[2284.06 → 2284.56] or make an account
[2284.56 → 2285.38] on the support help desk
[2285.38 → 2286.00] and all that sort of thing.
[2286.06 → 2286.48] So we got lots
[2286.48 → 2287.06] of good feedback
[2287.06 → 2288.60] from Twitter
[2288.60 → 2289.18] in that way.
[2289.28 → 2289.62] We have,
[2290.34 → 2290.54] you know,
[2290.56 → 2291.28] we're able to see
[2291.28 → 2292.30] projects that are being
[2292.30 → 2293.42] publicized really easily
[2293.42 → 2293.98] because people,
[2294.14 → 2294.30] you know,
[2294.30 → 2294.90] they'll tweet about it,
[2294.94 → 2295.60] it'll have GitHub.com
[2295.60 → 2296.02] in the URL,
[2296.36 → 2296.98] and we can see that
[2296.98 → 2297.74] get passed around.
[2298.16 → 2298.96] We're able to see
[2298.96 → 2300.78] tutorials or blog posts
[2300.78 → 2301.34] that pop up
[2301.34 → 2301.96] talking about GitHub
[2301.96 → 2303.38] just because it's in the
[2303.38 → 2303.94] name of the title
[2303.94 → 2304.66] or something like that,
[2304.70 → 2305.72] and it pops up on Twitter
[2305.72 → 2306.52] under the search.
[2307.24 → 2307.76] And, you know,
[2307.78 → 2308.84] even when we do a deployment
[2308.84 → 2310.80] or we make a new blog post,
[2310.80 → 2311.98] a lot of times
[2311.98 → 2312.60] we'll have a blog post
[2312.60 → 2313.60] that'll get two comments,
[2314.02 → 2314.70] but it'll be tweeted
[2314.70 → 2315.28] about, you know,
[2315.28 → 2316.02] 30 times.
[2316.46 → 2317.66] And so it's a lot more
[2317.66 → 2318.46] useful for us now
[2318.46 → 2319.16] just to look at what
[2319.16 → 2319.66] people are saying
[2319.66 → 2320.36] on Twitter than it is
[2320.36 → 2321.36] to depend on them
[2321.36 → 2321.80] to make a comment
[2321.80 → 2322.74] on site because that's
[2322.74 → 2324.06] where it's happening anyway,
[2324.16 → 2324.70] whether we're looking
[2324.70 → 2325.08] or not.
[2325.46 → 2326.08] So, you know,
[2326.10 → 2326.86] it's really up to you,
[2326.90 → 2327.14] I think,
[2327.18 → 2327.76] if you're trying to do
[2327.76 → 2328.68] like a bootstrap business
[2328.68 → 2329.54] or you have an open source
[2329.54 → 2331.00] project to be proactive
[2331.00 → 2332.26] about finding that stuff
[2332.26 → 2333.24] because, you know,
[2333.30 → 2334.04] with the Hamill guys
[2334.04 → 2334.56] and SaaS,
[2334.88 → 2335.38] people are talking
[2335.38 → 2335.86] about that stuff
[2335.86 → 2336.44] whether they're watching
[2336.44 → 2336.78] or not.
[2336.78 → 2337.38] So they can either
[2337.38 → 2338.46] use it to their advantage
[2338.46 → 2339.58] and help shape the project
[2339.58 → 2340.62] or help improve things
[2340.62 → 2341.06] like, I don't know,
[2341.12 → 2341.82] someone says Hamill's
[2341.82 → 2342.66] documentation sucks
[2342.66 → 2343.28] because they couldn't
[2343.28 → 2343.88] find X.
[2344.44 → 2345.00] Now that's an opportunity
[2345.00 → 2346.24] for them to fix that there.
[2346.76 → 2347.50] Whereas before,
[2347.60 → 2348.32] they would just be thinking,
[2348.42 → 2348.62] you know,
[2348.82 → 2349.54] no one ever complains
[2349.54 → 2350.34] about Hamill's documentation
[2350.34 → 2351.48] so it must be good enough.
[2351.82 → 2352.18] And, you know,
[2352.20 → 2352.92] we do that same thing
[2352.92 → 2353.30] constantly.
[2353.42 → 2353.76] Every day,
[2354.12 → 2354.98] people are checking Twitter.
[2355.34 → 2355.48] You know,
[2355.50 → 2356.00] I'm sure people have
[2356.00 → 2357.12] different schedules.
[2357.28 → 2358.86] I check it normally
[2358.86 → 2359.46] towards the evening
[2359.46 → 2360.54] and just sort of read
[2360.54 → 2361.16] what's going on
[2361.16 → 2361.58] and get a feel
[2361.58 → 2362.22] for what was happening
[2362.22 → 2362.74] that day,
[2363.18 → 2364.76] either with the site itself
[2364.76 → 2365.60] and with the ecosystem
[2365.60 → 2366.30] around the site.
[2366.30 → 2366.82] Is that something
[2366.82 → 2367.74] that everybody does
[2367.74 → 2368.20] or is that just
[2368.20 → 2368.80] something you do?
[2369.42 → 2370.24] I'm sure everyone
[2370.24 → 2371.44] does it a lot.
[2373.24 → 2373.60] Yeah,
[2373.80 → 2374.32] I mean,
[2374.48 → 2375.66] we all use Twitter a lot
[2375.66 → 2377.28] so it's fascinating
[2377.28 → 2377.86] to see what other people
[2377.86 → 2378.48] are saying about it
[2378.48 → 2379.12] and that sort of thing.
[2379.68 → 2380.14] So, yeah,
[2380.18 → 2380.36] I mean,
[2380.38 → 2381.18] if anyone mentions GitHub
[2381.18 → 2381.86] on Twitter,
[2381.98 → 2382.44] there's a good chance
[2382.44 → 2383.02] someone at GitHub
[2383.02 → 2384.00] is going to read that.
[2385.04 → 2385.42] I mean,
[2385.44 → 2386.10] we don't all read
[2386.10 → 2386.46] all of them
[2386.46 → 2387.14] because it's gotten
[2387.14 → 2387.90] to the point where,
[2388.14 → 2388.36] I mean,
[2388.42 → 2389.14] Twitter is so big
[2389.14 → 2390.12] and GitHub is getting big
[2390.12 → 2390.62] and there's just
[2390.62 → 2392.16] a lot of tweets,
[2392.30 → 2393.78] especially in other languages.
[2393.78 → 2394.68] But, yeah,
[2394.80 → 2395.02] I mean,
[2395.46 → 2396.28] especially in the early days,
[2396.38 → 2398.42] we did lots of support
[2398.42 → 2398.98] and stuff that way.
[2399.02 → 2399.52] We still do.
[2399.68 → 2400.16] We'll help people
[2400.16 → 2401.08] complain on Twitter
[2401.08 → 2401.78] that something is broken
[2401.78 → 2402.96] and then we'll use
[2402.96 → 2403.60] a GitHub account
[2403.60 → 2404.10] on Twitter
[2404.10 → 2404.98] to at reply to them
[2404.98 → 2405.62] and try and figure out
[2405.62 → 2406.10] what's wrong
[2406.10 → 2407.50] or try and get more information
[2407.50 → 2408.54] and help people that way.
[2409.34 → 2410.20] We had a couple of times,
[2410.26 → 2412.70] a couple terrible incidents.
[2413.38 → 2414.10] Last year,
[2414.52 → 2415.92] our DNS provider went down
[2415.92 → 2417.24] and so GitHub.com
[2417.24 → 2418.24] was just erased
[2418.24 → 2419.20] from the face of the universe
[2419.20 → 2421.78] and one of the things we did
[2421.78 → 2422.46] was we posted
[2422.46 → 2423.84] like a workaround,
[2423.96 → 2424.78] a temporary workaround
[2424.78 → 2427.64] to edit your Etsy hosts
[2427.64 → 2430.08] and there was an OSX script
[2430.08 → 2431.40] and I think probably a Linux one
[2431.40 → 2433.02] and people were complaining
[2433.02 → 2433.46] on Twitter
[2433.46 → 2434.42] about GitHub being down
[2434.42 → 2434.92] and we were able
[2434.92 → 2435.70] to write a little script
[2435.70 → 2438.24] so if anyone had a complaint
[2438.24 → 2438.72] with DNS,
[2438.88 → 2439.00] GitHub,
[2439.12 → 2439.34] whatever,
[2439.34 → 2440.16] we could send them
[2440.16 → 2440.76] a link
[2440.76 → 2441.86] as an at reply
[2441.86 → 2442.32] on Twitter
[2442.32 → 2443.74] to the fix
[2443.74 → 2445.04] and so that was pretty awesome
[2445.04 → 2445.96] so we ended up sending out,
[2446.04 → 2446.34] I don't know,
[2446.62 → 2447.56] an annoying amount of tweets,
[2447.68 → 2448.64] 300, 400 tweets
[2448.64 → 2449.32] in an afternoon
[2449.32 → 2450.70] all with the same content.
[2450.80 → 2450.96] You're like,
[2451.02 → 2451.96] check this link to fix it
[2451.96 → 2452.82] but it actually worked
[2452.82 → 2453.42] and for a lot of people
[2453.42 → 2454.22] it helped them get around
[2454.22 → 2455.02] the DNS outage
[2455.02 → 2456.00] and get some stuff done.
[2456.48 → 2457.62] So for things like that,
[2458.16 → 2458.36] I mean,
[2458.42 → 2460.64] I guess you could say social media
[2460.64 → 2461.82] but for us, it's mainly just Twitter
[2461.82 → 2463.22] is pretty crazy.
[2463.44 → 2463.56] I mean,
[2463.62 → 2463.96] we check,
[2464.48 → 2465.58] I find Twitter more reliable
[2465.58 → 2466.46] for finding blog posts
[2466.46 → 2466.94] about GitHub
[2466.94 → 2467.80] and that sort of thing
[2467.80 → 2469.12] than I do like Google
[2469.12 → 2470.06] blog search
[2470.06 → 2470.98] or anything like that.
[2471.32 → 2471.64] Technocratic.
[2472.16 → 2472.84] Twitter is definitely
[2472.84 → 2473.50] where it's all out
[2473.50 → 2474.50] and same thing for projects.
[2475.14 → 2475.36] I mean,
[2475.46 → 2476.38] if you have a project,
[2476.50 → 2477.38] pick a unique enough name
[2477.38 → 2478.20] where you can either search
[2478.20 → 2479.82] for the name on its own
[2479.82 → 2481.10] or your username
[2481.10 → 2482.18] slash the project name
[2482.18 → 2483.10] and see what people
[2483.10 → 2483.78] are saying about it
[2483.78 → 2484.94] but that,
[2485.30 → 2486.14] I think a lot of times
[2486.14 → 2488.42] when you have a smaller project
[2488.42 → 2489.84] it is more just ego surfing
[2489.84 → 2490.72] than it is something,
[2491.14 → 2491.62] anything else.
[2491.72 → 2491.92] I mean,
[2492.26 → 2493.28] when you have a small project
[2493.28 → 2493.72] on GitHub
[2493.72 → 2494.88] and it's just you
[2494.88 → 2496.32] and maybe a couple watchers
[2496.32 → 2497.58] or even a couple of hundred watchers,
[2498.28 → 2498.88] a lot of those people
[2498.88 → 2499.90] are going to know what to do.
[2499.90 → 2500.40] They're going to know
[2500.40 → 2502.24] to go to your issue tracker,
[2502.58 → 2502.92] they're going to know
[2502.92 → 2503.48] to go to your README
[2503.48 → 2504.36] to look for the issue tracker,
[2504.46 → 2504.76] they're going to know
[2504.76 → 2505.52] to look for your mailing list
[2505.52 → 2506.34] and when they have a complaint
[2506.34 → 2506.86] with your project
[2506.86 → 2507.58] something won't work,
[2507.90 → 2508.56] they're going to go
[2508.56 → 2509.56] to the mailing list
[2509.56 → 2510.78] and try and make it work
[2510.78 → 2513.16] or Google a blog post
[2513.16 → 2513.88] and try and make it work.
[2514.30 → 2515.16] I don't think you see
[2515.16 → 2515.98] a lot of Twitter complaints
[2515.98 → 2516.62] for that kind of stuff
[2516.62 → 2517.98] but when you have a product
[2517.98 → 2519.08] or a website or a company,
[2519.22 → 2520.14] I think it's a lot easier
[2520.14 → 2520.96] just for someone to say,
[2521.56 → 2521.70] you know,
[2521.74 → 2522.36] because you're just saying
[2522.36 → 2522.98] if something's broken,
[2523.08 → 2523.78] you're saying screw GitHub
[2523.78 → 2525.16] whereas if you're using
[2525.16 → 2526.12] one of Adam's projects
[2526.12 → 2526.56] and it's broken,
[2526.56 → 2527.60] you're saying screw Adam.
[2527.82 → 2528.82] So I think it's a lot easier
[2528.82 → 2530.68] for people to kind of critique
[2530.68 → 2531.82] a website or product
[2531.82 → 2532.26] on Twitter
[2532.26 → 2533.18] than it is for them
[2533.18 → 2533.92] to do that same thing
[2533.92 → 2534.74] with an open source project
[2534.74 → 2535.88] that has like a single
[2535.88 → 2536.64] main container or owner.
[2537.32 → 2537.78] You know,
[2537.92 → 2538.82] GitHub's also giving you
[2538.82 → 2539.82] another response
[2539.82 → 2541.48] to that type of trolling.
[2541.60 → 2541.74] You know,
[2542.10 → 2543.26] the amount of complaints
[2543.26 → 2544.64] about free open source software
[2544.64 → 2546.42] just never ceases to amaze me
[2546.42 → 2547.98] but now you have the ability
[2547.98 → 2548.52] to say,
[2548.88 → 2550.00] fork it and send me
[2550.00 → 2550.70] a pull request.
[2551.04 → 2551.18] You know,
[2551.20 → 2552.12] it's just that easy.
[2553.12 → 2553.36] Right,
[2553.46 → 2554.44] and it really is.
[2554.98 → 2555.20] I mean,
[2555.22 → 2555.64] because we do that
[2555.64 → 2556.24] to each other too
[2556.24 → 2557.04] even in our company.
[2557.20 → 2557.88] Someone will complain
[2557.88 → 2558.60] and someone will say,
[2558.68 → 2558.78] well,
[2558.86 → 2559.12] you know,
[2559.16 → 2559.62] you can always send
[2559.62 → 2560.16] a pull request
[2560.16 → 2561.60] and that usually ends
[2561.60 → 2562.18] the conversation
[2562.18 → 2563.04] pretty quickly.
[2564.18 → 2564.36] But yeah,
[2564.44 → 2565.02] where do you take it
[2565.02 → 2565.40] from there,
[2565.46 → 2565.60] right?
[2565.60 → 2566.30] Like if you can fix
[2566.30 → 2566.70] the problem
[2566.70 → 2567.16] and you're complaining
[2567.16 → 2567.56] about it,
[2567.58 → 2568.30] just do your job.
[2568.92 → 2569.04] Yeah,
[2569.04 → 2570.54] exactly.
[2571.12 → 2573.22] And I've always contributed
[2573.22 → 2573.74] to open source
[2573.74 → 2574.00] but,
[2574.12 → 2574.84] you know,
[2574.88 → 2575.52] a lot of times
[2575.52 → 2577.30] sometimes I'll just add features
[2577.30 → 2578.70] or fix a bug
[2578.70 → 2579.46] that I wouldn't have added
[2579.46 → 2580.40] otherwise just because,
[2580.52 → 2580.60] you know,
[2580.66 → 2581.66] I have my GitHub workflow
[2581.66 → 2582.24] down pat
[2582.24 → 2583.04] and it's really easy
[2583.04 → 2584.36] for me to fork it
[2584.36 → 2585.60] and contribute a patch.
[2586.02 → 2586.70] And that's kind of the goal
[2586.70 → 2587.56] is to get that way
[2587.56 → 2589.30] with as many people
[2589.30 → 2590.12] as we can.
[2590.74 → 2591.14] Well,
[2591.16 → 2591.72] let's talk about that
[2591.72 → 2592.10] for a moment.
[2592.20 → 2592.98] So we talked about,
[2592.98 → 2593.30] you know,
[2593.48 → 2595.56] watchers and the projects
[2595.56 → 2596.22] that you followed
[2596.22 → 2597.58] on GitHub.
[2598.20 → 2598.34] You know,
[2598.34 → 2599.28] Adam and I often talk
[2599.28 → 2600.50] about the best way
[2600.50 → 2601.76] to find the folks
[2601.76 → 2602.76] and their projects
[2602.76 → 2604.42] to follow in open source
[2604.42 → 2605.68] and usually that means GitHub.
[2606.22 → 2606.36] You know,
[2606.40 → 2607.06] what's the best way
[2607.06 → 2608.32] to gauge someone's participation
[2608.32 → 2609.92] even if they may not be
[2609.92 → 2613.08] an active organizer
[2613.08 → 2614.06] of a particular project?
[2614.44 → 2615.24] How can you gauge
[2615.24 → 2616.12] someone's participation
[2616.12 → 2617.10] with patches
[2617.10 → 2618.46] and commits
[2618.46 → 2619.20] across GitHub?
[2620.00 → 2621.06] I think one of the things
[2621.06 → 2621.96] that I like about GitHub
[2621.96 → 2623.44] is that it doesn't try
[2623.44 → 2624.48] to be everything.
[2624.60 → 2625.14] It's not trying to be
[2625.14 → 2625.92] the entire world
[2625.92 → 2626.60] of open source.
[2627.44 → 2627.84] I think,
[2628.00 → 2628.40] like I was saying
[2628.40 → 2628.72] with Twitter,
[2628.82 → 2629.68] a lot of GitHub users,
[2629.80 → 2630.76] probably most of them,
[2631.04 → 2632.02] have Twitter accounts.
[2632.58 → 2633.44] And so we don't want
[2633.44 → 2635.88] to have you leave Twitter
[2635.88 → 2638.38] to tweet about open source
[2638.38 → 2639.64] in 140 characters or fewer
[2639.64 → 2640.84] on GitHub exclusively
[2640.84 → 2641.78] for GitHub users.
[2641.98 → 2642.06] You know,
[2642.08 → 2643.28] we don't want to add
[2643.28 → 2644.08] a Twitter component
[2644.08 → 2645.16] to GitHub
[2645.16 → 2646.52] that's just for you
[2646.52 → 2647.78] talking about whatever.
[2647.94 → 2648.04] I mean,
[2648.06 → 2648.90] maybe we'll do updates
[2648.90 → 2649.80] for repositories
[2649.80 → 2650.28] so you can say
[2650.28 → 2651.00] there's a new release,
[2651.52 → 2652.72] but not in the way
[2652.72 → 2653.50] that Twitter just lets you
[2653.50 → 2654.70] just communicate openly
[2654.70 → 2657.08] because Twitter already exists.
[2657.26 → 2658.20] And I think what GitHub
[2658.20 → 2658.66] should do
[2658.66 → 2659.90] is work really well
[2659.90 → 2660.44] with Twitter.
[2660.44 → 2661.64] And I think what it
[2661.64 → 2662.62] should also do
[2662.62 → 2663.72] in sort of way
[2663.72 → 2664.08] of finding,
[2664.20 → 2664.38] you know,
[2664.46 → 2666.42] what's the canonical
[2666.42 → 2667.48] Cristiano repository
[2667.48 → 2668.06] right now
[2668.06 → 2669.22] is it should work
[2669.22 → 2669.60] with Google.
[2669.70 → 2670.44] We should have ways
[2670.44 → 2671.42] to promote
[2671.42 → 2673.32] the most active fork
[2673.32 → 2674.32] in Google
[2674.32 → 2675.46] to be the first search result
[2675.46 → 2676.72] from within GitHub.
[2677.42 → 2678.24] And so what I really want
[2678.24 → 2678.64] GitHub to do
[2678.64 → 2679.28] is sort of play
[2679.28 → 2679.94] into the ecosystem
[2679.94 → 2680.94] of what people
[2680.94 → 2681.60] are already doing.
[2681.70 → 2682.22] People are already
[2682.22 → 2682.80] contributing.
[2683.48 → 2683.82] People are already
[2683.82 → 2684.32] making patches.
[2684.46 → 2684.82] People are already
[2684.82 → 2685.50] doing this stuff.
[2685.92 → 2686.04] You know,
[2686.06 → 2686.82] how can we either
[2686.82 → 2687.82] have them do it
[2687.82 → 2688.64] on GitHub to make it easier
[2688.64 → 2689.30] or how can we
[2689.30 → 2690.14] kind of hook into it
[2690.14 → 2690.70] like with the service
[2690.70 → 2691.20] hooks and that sort
[2691.20 → 2691.46] of thing.
[2691.62 → 2692.90] So for finding out
[2692.90 → 2693.46] someone's,
[2693.46 → 2694.06] you know,
[2694.38 → 2694.78] worth,
[2694.90 → 2695.12] I guess,
[2695.16 → 2695.64] in open source
[2695.64 → 2696.46] or not the worth
[2696.46 → 2697.64] but just how their weight,
[2697.72 → 2698.56] how active they are,
[2698.98 → 2699.82] I think GitHub's
[2699.82 → 2700.42] one part of it
[2700.42 → 2701.32] and we want to do,
[2702.00 → 2702.78] we want to put more
[2702.78 → 2703.46] stuff on the profile
[2703.46 → 2703.84] to say,
[2703.90 → 2704.10] you know,
[2704.44 → 2705.32] you go to Defunct
[2705.32 → 2706.12] and you see he does
[2706.12 → 2706.54] Ruby,
[2706.90 → 2707.20] Python,
[2707.42 → 2707.96] and JavaScript
[2707.96 → 2708.72] primarily
[2708.72 → 2709.40] because we detected
[2709.40 → 2710.30] that from my projects
[2710.30 → 2711.52] and he's contributed
[2711.52 → 2712.34] to these projects
[2712.34 → 2713.08] and so I could have,
[2713.14 → 2713.40] you know,
[2714.10 → 2714.62] jQuery
[2714.62 → 2715.32] slash jQuery
[2715.32 → 2716.04] on my profile
[2716.04 → 2716.92] even though I don't own it
[2716.92 → 2718.28] because I submitted a patch
[2718.28 → 2719.28] and they accepted it.
[2719.56 → 2719.94] And I think that'd be
[2719.94 → 2720.44] really awesome
[2720.44 → 2721.34] because if you want to be,
[2721.66 → 2721.82] you know,
[2721.84 → 2722.72] like a Rails contributor
[2722.72 → 2723.54] or something like that,
[2723.74 → 2724.28] we could show,
[2724.48 → 2724.64] you know,
[2724.68 → 2725.14] this guy,
[2725.48 → 2726.44] he doesn't have commit access,
[2726.56 → 2727.30] he doesn't own the project
[2727.30 → 2727.96] but he's contributed
[2727.96 → 2728.78] 14 patches
[2728.78 → 2729.48] that have been accepted
[2729.48 → 2730.46] to Rails
[2730.46 → 2731.22] or something like that
[2731.22 → 2731.96] which I think,
[2732.06 → 2732.22] I mean,
[2732.22 → 2732.98] that's what it's all about
[2732.98 → 2736.44] is just doing code.
[2736.72 → 2737.22] It's not about,
[2737.26 → 2737.44] you know,
[2737.54 → 2739.20] collecting badges
[2739.20 → 2740.22] or karma
[2740.22 → 2741.04] or getting upvotes
[2741.04 → 2741.68] or downvotes,
[2741.68 → 2742.36] it's about getting
[2742.36 → 2743.14] your patch accepted
[2743.14 → 2743.82] or rejected
[2743.82 → 2744.90] and we really want to base
[2744.90 → 2745.86] your sort of,
[2746.24 → 2747.30] your merit in GitHub
[2747.30 → 2748.22] on that sort of thing.
[2748.38 → 2749.68] So I think the ways
[2749.68 → 2750.36] to do it right now
[2750.36 → 2751.52] is just to kind of,
[2751.54 → 2751.78] you know,
[2751.90 → 2753.62] check what they've been doing
[2753.62 → 2754.02] on Google,
[2754.18 → 2754.78] check what they've been doing
[2754.78 → 2755.20] on Twitter
[2755.20 → 2756.52] and then check what they've been
[2756.52 → 2757.36] doing on GitHub.
[2757.48 → 2758.24] What have they been forking?
[2758.40 → 2759.18] Who are they following?
[2759.48 → 2760.36] What are those people into?
[2760.84 → 2762.38] And sort of dig around that way
[2762.38 → 2763.36] and ideally,
[2763.48 → 2764.74] I think we'd like the profile
[2764.74 → 2765.60] to show you a lot more
[2765.60 → 2766.72] of that information right there.
[2766.82 → 2767.30] Just this person
[2767.30 → 2768.20] has done these things
[2768.20 → 2769.30] and they're awesome
[2769.30 → 2769.80] or they're not.
[2770.36 → 2771.32] Any plans to link
[2771.32 → 2772.06] a Twitter account
[2772.06 → 2772.82] in your public profile
[2772.82 → 2773.18] on GitHub?
[2774.30 → 2774.94] I don't know.
[2775.28 → 2776.10] It's never come up.
[2776.84 → 2777.16] Maybe.
[2777.68 → 2778.00] Sure.
[2778.10 → 2778.24] I mean,
[2778.24 → 2778.70] we've talked a lot
[2778.70 → 2779.36] about the updates
[2779.36 → 2781.58] for repositories
[2781.58 → 2782.30] because it'd be useful
[2782.30 → 2782.80] to say,
[2783.20 → 2783.38] you know,
[2783.42 → 2784.42] check out this version
[2784.42 → 2784.86] of this.
[2785.02 → 2785.18] I mean,
[2785.20 → 2786.12] you might see a tag,
[2786.32 → 2787.56] but is that perfect enough?
[2787.92 → 2788.48] Maybe it is,
[2788.54 → 2789.12] maybe it isn't,
[2789.28 → 2790.86] but that's kind of
[2790.86 → 2791.54] on the drawing board
[2791.54 → 2791.88] for now.
[2792.00 → 2793.96] But for users,
[2794.12 → 2794.34] I don't know,
[2794.34 → 2795.50] that's a good question.
[2795.68 → 2795.82] You know,
[2795.84 → 2796.56] it's funny because
[2796.56 → 2797.76] when the site started
[2797.76 → 2798.38] on your profile,
[2798.50 → 2799.02] we had a little,
[2800.34 → 2800.68] in the very,
[2800.76 → 2801.22] very early days,
[2801.30 → 2801.80] there was a spot
[2801.80 → 2802.16] for you to put
[2802.16 → 2802.80] like your name,
[2802.92 → 2803.40] your company,
[2804.40 → 2805.56] and instead of your URL
[2805.56 → 2806.98] or our homepage,
[2807.26 → 2808.08] it just said blog.
[2808.30 → 2808.70] And now I think
[2808.70 → 2809.84] it says blog slash homepage.
[2810.16 → 2810.52] And we thought
[2810.52 → 2810.92] it was like,
[2810.98 → 2811.06] well,
[2811.08 → 2811.96] everyone on GitHub
[2811.96 → 2812.80] is going to have a blog,
[2812.94 → 2814.96] but even as late
[2814.96 → 2815.46] as 2007,
[2815.60 → 2816.10] I think we were,
[2816.66 → 2817.54] or even as early as 2007,
[2817.66 → 2818.46] I think we were wrong.
[2818.54 → 2819.00] It should have just said
[2819.00 → 2819.58] Twitter account,
[2819.70 → 2819.88] right?
[2820.22 → 2820.70] It should have been
[2820.70 → 2821.46] when you signed to GitHub,
[2821.96 → 2822.50] when you go to edit
[2822.50 → 2822.94] your profile,
[2823.10 → 2824.06] give us your Twitter account
[2824.06 → 2824.60] and then,
[2824.84 → 2825.32] you know,
[2825.36 → 2826.16] we'll do some cool stuff
[2826.16 → 2826.86] with that in the future.
[2827.04 → 2827.20] Just,
[2827.28 → 2827.40] you know,
[2827.46 → 2828.70] just your username.
[2828.70 → 2829.70] But yeah,
[2829.70 → 2830.22] I think that would be
[2830.22 → 2830.78] pretty interesting
[2830.78 → 2832.28] because a lot of times
[2832.28 → 2834.38] I see someone will have
[2834.38 → 2835.38] as their blog homepage
[2835.38 → 2836.66] just their Twitter URL
[2836.66 → 2837.84] and then you'll go to that
[2837.84 → 2838.34] and then they'll have
[2838.34 → 2839.38] as their Twitter URL
[2839.38 → 2840.64] as their homepage,
[2840.88 → 2841.72] they'll have their GitHub account.
[2841.84 → 2842.78] So they go in this little circle.
[2843.26 → 2843.66] And so I think,
[2843.70 → 2843.84] yeah,
[2843.88 → 2844.66] I think it's pretty cool
[2844.66 → 2845.64] if we could tie in Twitter
[2845.64 → 2846.42] a lot more,
[2846.52 → 2847.22] that would be useful.
[2847.34 → 2847.50] I mean,
[2847.50 → 2848.96] because I use those sites
[2848.96 → 2850.36] a lot for open source stuff
[2850.36 → 2851.26] and that would be pretty cool.
[2851.26 → 2852.14] Gotcha.
[2852.46 → 2853.58] So we just turned a new leaf.
[2853.72 → 2855.20] We have this brand-new year
[2855.20 → 2855.60] come up.
[2855.70 → 2856.30] It's 2010
[2856.30 → 2858.34] and it seems like
[2858.34 → 2859.62] everybody's made this list
[2859.62 → 2860.58] of reservations
[2860.58 → 2861.50] they're going to do this year
[2861.50 → 2862.64] and where they're taking
[2862.64 → 2863.12] their company
[2863.12 → 2863.72] or they've just had
[2863.72 → 2865.04] this 2010 planning meeting
[2865.04 → 2866.20] and they've realigned
[2866.20 → 2866.66] their goals.
[2866.86 → 2869.10] What are GitHub's priorities
[2869.10 → 2870.44] right now for 2010
[2870.44 → 2872.64] and what's in your extreme focus?
[2874.06 → 2874.52] You know,
[2874.56 → 2874.80] we don't,
[2874.92 → 2876.12] it's always the same thing
[2876.12 → 2876.42] it's been.
[2876.50 → 2877.46] We don't make a lot of plans.
[2877.54 → 2877.96] We don't make a lot
[2877.96 → 2878.78] of long-term plans
[2878.78 → 2879.32] because,
[2879.64 → 2880.42] you know,
[2880.42 → 2881.58] if I had tried to plan
[2881.58 → 2882.24] five years ago
[2882.24 → 2882.98] what I'd be doing now
[2882.98 → 2883.84] it would have just been
[2883.84 → 2884.66] a miserable failure
[2884.66 → 2886.28] and if I had stuck to that plan
[2886.28 → 2887.10] I would not be talking
[2887.10 → 2887.62] to you guys today
[2887.62 → 2888.04] probably.
[2888.74 → 2890.44] So what we try and focus on
[2890.44 → 2891.30] is really just making
[2891.30 → 2891.94] the site polish,
[2892.04 → 2892.86] making the site good,
[2893.30 → 2893.94] fixing bugs,
[2894.06 → 2895.10] adding awesome new features.
[2895.68 → 2896.06] One of the things
[2896.06 → 2896.60] I'm really proud about
[2896.60 → 2897.00] in our company
[2897.00 → 2897.54] is we can have
[2897.54 → 2898.14] a whole feature
[2898.14 → 2899.06] almost ready to go
[2899.06 → 2900.64] and if we decide
[2900.64 → 2901.52] that it's not worth it
[2901.52 → 2902.00] or it's going to take
[2902.00 → 2903.00] the company in a bad direction
[2903.00 → 2904.02] we'll just scrap it
[2904.02 → 2904.58] and we've done that
[2904.58 → 2905.06] a couple of times
[2905.06 → 2906.08] with some pretty major things
[2906.08 → 2907.58] and I think
[2907.58 → 2908.76] when you're planning
[2908.76 → 2909.18] and you have
[2909.18 → 2910.10] a lot of like
[2910.10 → 2911.98] really solid deadlines
[2911.98 → 2912.68] for no reason
[2912.68 → 2913.86] it's really easy
[2913.86 → 2914.44] to get trapped in
[2914.44 → 2914.72] and we're like
[2914.72 → 2915.76] oh well we need this
[2915.76 → 2916.40] done next week
[2916.40 → 2916.82] so why don't we
[2916.82 → 2917.66] just push it out anyway
[2917.66 → 2918.30] because otherwise
[2918.30 → 2919.86] we'll miss our next week deadline
[2919.86 → 2920.24] but,
[2920.72 → 2920.96] you know,
[2921.28 → 2922.32] we don't do that
[2922.32 → 2923.24] and it's great.
[2923.56 → 2924.12] Things are done
[2924.12 → 2924.60] when they're ready,
[2924.72 → 2925.04] things are done
[2925.04 → 2925.60] when they're good,
[2926.06 → 2927.24] we're constantly
[2927.24 → 2928.56] trying to improve things,
[2929.10 → 2930.58] we kind of allocate time,
[2930.92 → 2931.04] you know,
[2931.08 → 2931.62] we want to revisit
[2931.62 → 2932.88] the API later this year
[2932.88 → 2933.46] and then,
[2933.56 → 2933.72] you know,
[2933.72 → 2934.44] make it even better
[2934.44 → 2936.32] and add more features
[2936.32 → 2936.70] like trending
[2936.70 → 2937.48] and that sort of thing
[2937.48 → 2938.16] but,
[2938.36 → 2938.62] you know,
[2938.66 → 2939.28] in the short term
[2939.28 → 2939.92] it's all about
[2939.92 → 2941.72] making the features
[2941.72 → 2942.36] that exist better
[2942.36 → 2943.68] and adding new features
[2943.68 → 2944.46] that are really useful
[2944.46 → 2944.82] to people
[2944.82 → 2946.80] so that's what we're
[2946.80 → 2947.52] trying to do this year
[2947.52 → 2948.20] as far as
[2948.20 → 2949.26] growing the business
[2949.26 → 2949.74] I mean,
[2949.82 → 2951.06] we probably want to hire
[2951.06 → 2951.98] a couple more people
[2951.98 → 2952.42] maybe,
[2952.78 → 2954.22] we hired four people
[2954.22 → 2954.64] last year
[2954.64 → 2955.54] and they're all amazing
[2955.54 → 2956.36] and so things are going
[2956.36 → 2957.36] really well right there
[2957.36 → 2959.16] and I think we just want
[2959.16 → 2959.92] to just keep growing
[2959.92 → 2960.26] the site
[2960.26 → 2960.74] in the direction
[2960.74 → 2961.14] it's growing,
[2961.28 → 2961.38] you know,
[2961.42 → 2962.02] the stuff about
[2962.02 → 2963.12] having a fork
[2963.12 → 2965.32] that has unique commits
[2965.32 → 2966.46] be weighted higher
[2966.46 → 2967.34] than a fork without them
[2967.34 → 2968.22] and things like that
[2968.22 → 2968.70] that we've been talking
[2968.70 → 2969.58] about since day one
[2969.58 → 2970.36] we want to do that
[2970.36 → 2971.82] and just make it
[2971.82 → 2972.44] seem really obvious
[2972.44 → 2973.78] and so that's
[2973.78 → 2974.38] really the plan
[2974.38 → 2974.82] is make the site
[2974.82 → 2975.24] perfect
[2975.24 → 2975.94] make sure we still
[2975.94 → 2976.74] love using the site
[2976.74 → 2977.38] you know,
[2977.44 → 2978.42] fix any pain points
[2978.42 → 2979.16] and that sort of thing
[2979.16 → 2980.40] and just concentrate
[2980.40 → 2980.98] on,
[2981.36 → 2981.46] you know,
[2981.48 → 2982.22] the rise of Git
[2982.22 → 2983.06] I don't think that
[2983.06 → 2984.02] this year
[2984.02 → 2985.56] or even probably next year
[2985.56 → 2986.40] will be the year
[2986.40 → 2987.06] that Git peaks
[2987.06 → 2987.68] just because,
[2988.22 → 2988.32] you know,
[2988.38 → 2989.44] subversion and everything else
[2989.44 → 2990.96] is just so unbelievably massive
[2990.96 → 2992.42] and Git still has
[2992.42 → 2993.38] a really young ecosystem
[2993.38 → 2994.18] the whole idea
[2994.18 → 2995.12] of distributed version control
[2995.12 → 2996.52] is right now,
[2996.60 → 2996.84] you know,
[2997.08 → 2998.36] different and scary to people
[2998.36 → 3000.08] and so we just want to be ready
[3000.08 → 3000.38] when,
[3000.50 → 3001.10] like,
[3001.20 → 3001.96] all these people
[3001.96 → 3002.70] start coming over
[3002.70 → 3004.38] and start seeing the value of it
[3004.38 → 3005.02] we want to be there
[3005.02 → 3006.10] we want to make it really easy
[3006.10 → 3007.20] we want to make it newbie friendly
[3007.20 → 3008.66] and we want to make it perfect
[3008.66 → 3009.56] and so that's what we're
[3009.56 → 3010.34] trying to focus on.
[3011.28 → 3011.62] So your homepage
[3011.62 → 3014.42] has 180,000 coders on GitHub
[3014.42 → 3015.38] how many repos
[3015.38 → 3015.98] approximately?
[3016.82 → 3017.02] Oh,
[3017.38 → 3017.72] repos?
[3017.80 → 3018.16] I don't know.
[3019.32 → 3019.56] I mean,
[3019.58 → 3020.44] it depends on how you slice it
[3020.44 → 3020.88] I think overall
[3020.88 → 3022.64] there's about 350,000 maybe
[3022.64 → 3023.36] maybe 400
[3023.36 → 3024.54] and then
[3024.54 → 3025.60] you know,
[3025.60 → 3026.40] not that many forks
[3026.40 → 3028.32] maybe 120,000 forks
[3028.32 → 3028.90] out of that
[3028.90 → 3031.48] of public stuff
[3031.48 → 3032.08] so
[3032.08 → 3032.88] yeah,
[3033.02 → 3033.32] I mean,
[3033.44 → 3034.50] we've got a pretty good ratio
[3034.50 → 3035.90] of repos to users
[3035.90 → 3036.54] right now
[3036.54 → 3037.48] which is pretty awesome.
[3038.76 → 3039.42] So we
[3039.42 → 3040.56] we've obviously
[3040.56 → 3041.86] all been enjoying
[3041.86 → 3042.52] the new UI
[3042.52 → 3043.72] that's been coming out of Kyle
[3043.72 → 3045.40] what
[3045.40 → 3046.90] like,
[3046.96 → 3047.78] I remember actually
[3047.78 → 3048.66] looking at this article
[3048.66 → 3049.00] recently
[3049.00 → 3050.00] that was on 37 Signals
[3050.00 → 3051.40] that there was a guest blog
[3051.40 → 3052.40] of you talking about
[3052.40 → 3053.34] the early days of GitHub
[3053.34 → 3054.44] and I remember
[3054.44 → 3055.80] I just looked at the screenshot
[3055.80 → 3057.12] of the old view
[3057.12 → 3057.72] of a repo
[3057.72 → 3058.08] and I was like
[3058.08 → 3058.78] oh my lord
[3058.78 → 3059.48] what is that?
[3060.38 → 3060.42] And
[3060.42 → 3061.14] I mean,
[3061.18 → 3061.92] it's only been about
[3061.92 → 3063.00] maybe a month and a half now
[3063.00 → 3063.74] since the new
[3063.74 → 3065.12] the new UI has been in place
[3065.12 → 3065.84] for the repos
[3065.84 → 3067.22] but how has that
[3067.22 → 3068.38] impacted the
[3068.38 → 3070.18] I guess
[3070.18 → 3072.10] just overall user experience
[3072.10 → 3073.40] of GitHub users?
[3074.44 → 3074.60] I mean,
[3074.64 → 3075.10] you tell me
[3075.10 → 3075.72] I think
[3075.72 → 3076.88] from our perspective
[3076.88 → 3078.38] we went from people
[3078.38 → 3078.96] talking about
[3078.96 → 3080.24] how good GitHub is
[3080.24 → 3081.64] and how much they like it
[3081.64 → 3082.72] or how much they hate it
[3082.72 → 3083.04] and,
[3083.16 → 3083.58] you know,
[3083.76 → 3084.86] this sort of things
[3084.86 → 3085.58] to now we've added
[3085.58 → 3086.28] a new class
[3086.28 → 3088.00] of Jabber
[3088.00 → 3088.74] which is just like
[3088.74 → 3089.42] it's so beautiful
[3089.42 → 3090.88] like I love the new UI
[3090.88 → 3092.24] I just love the way it looks
[3092.24 → 3093.20] I just want to lick it
[3093.20 → 3093.96] and that sort of thing
[3093.96 → 3094.38] so
[3094.38 → 3095.42] lick it
[3095.42 → 3096.12] yeah
[3096.12 → 3098.26] that's really awesome for us
[3098.26 → 3098.98] is to not just have
[3098.98 → 3099.74] like a really great site
[3099.74 → 3100.52] that people are really into
[3100.52 → 3101.62] but have a site
[3101.62 → 3102.12] that a lot of people
[3102.12 → 3102.56] really like
[3102.56 → 3103.10] we've also had people
[3103.10 → 3104.26] tell us they hate the UI
[3104.26 → 3106.08] but that's kind of
[3106.08 → 3107.04] Kyle was kind of waiting
[3107.04 → 3108.34] for the first haters
[3108.34 → 3109.06] because that's how you know
[3109.06 → 3110.08] you did a perfect job
[3110.08 → 3110.54] with anything
[3110.54 → 3111.02] really
[3111.02 → 3112.04] I saw his reply
[3112.04 → 3112.76] on the blog post
[3112.76 → 3113.08] like yeah
[3113.08 → 3113.52] that's how I know
[3113.52 → 3114.14] I did my job
[3114.14 → 3115.40] because you don't like it
[3115.40 → 3116.86] and it's true
[3116.86 → 3117.28] we were
[3117.28 → 3118.16] I mean for a long time
[3118.16 → 3118.40] GitHub
[3118.40 → 3119.48] there was a lack
[3119.48 → 3120.28] of criticism
[3120.28 → 3120.94] and it was really
[3120.94 → 3121.70] starting to worry us
[3121.70 → 3122.14] because we thought
[3122.14 → 3122.80] it was going to be mediocre
[3122.80 → 3123.78] but then it all
[3123.78 → 3124.34] came flooding in
[3124.34 → 3125.10] and we felt much more
[3125.10 → 3125.62] confident
[3125.62 → 3126.94] did Tom get bummed out
[3126.94 → 3127.30] by that
[3127.30 → 3127.84] because I know
[3127.84 → 3128.78] that Tom was
[3128.78 → 3130.12] he's the UI guy
[3130.12 → 3130.72] of the team
[3130.72 → 3130.98] right?
[3131.68 → 3132.38] He was
[3132.38 → 3134.22] Tom Preston Werner
[3134.22 → 3135.36] was the original designer
[3135.36 → 3136.54] and he did the logo
[3136.54 → 3137.78] and all the
[3137.78 → 3138.54] all the GitHub
[3138.54 → 3139.32] all the designs
[3139.32 → 3140.32] until we brought in Kyle
[3140.32 → 3141.94] and Tom
[3141.94 → 3143.06] is the CTO
[3143.06 → 3144.26] so he's really been moving
[3144.26 → 3145.50] in more of a technical direction
[3145.50 → 3146.44] and that's what he wants
[3146.44 → 3147.88] so when we moved
[3147.88 → 3148.72] from Engine Yard
[3148.72 → 3149.16] to Rackspace
[3149.16 → 3149.74] we also
[3149.74 → 3150.94] did a lot of
[3150.94 → 3152.14] re-architecting
[3152.14 → 3152.56] of our site
[3152.56 → 3153.92] we changed a lot of the ways
[3153.92 → 3155.16] in which we store data
[3155.16 → 3156.32] and Tom
[3156.32 → 3157.06] kind of led that
[3157.06 → 3158.14] he was in charge of
[3158.14 → 3158.58] you know
[3158.58 → 3159.42] writing libraries
[3159.42 → 3160.64] hooking it into the site
[3160.64 → 3161.50] making sure the web app
[3161.50 → 3162.42] needed as few changes
[3162.42 → 3162.98] as possible
[3162.98 → 3164.68] making sure it still runs well
[3164.68 → 3166.30] in our GitHub firewall install
[3166.30 → 3167.60] which is the downloadable version
[3167.60 → 3168.56] that you can run
[3168.56 → 3169.66] and so
[3169.66 → 3170.62] Tom has been moving
[3170.62 → 3171.60] in a more technical direction
[3171.60 → 3172.02] the whole time
[3172.02 → 3173.40] he's always been great at both
[3173.40 → 3174.70] he worked as a developer
[3174.70 → 3175.52] for many years
[3175.52 → 3176.82] and he's worked as a designer
[3176.82 → 3177.26] print designer
[3177.26 → 3178.26] for many years as well
[3178.26 → 3179.60] but I think right now
[3179.60 → 3180.50] on a site as
[3180.50 → 3181.40] technically challenging
[3181.40 → 3181.82] as GitHub
[3181.82 → 3183.14] he's going to really
[3183.14 → 3184.42] take over in the CTO role
[3184.42 → 3185.36] and help lead us
[3185.36 → 3185.76] in the direction
[3185.76 → 3186.32] we need to go to
[3186.32 → 3186.82] which is
[3186.82 → 3187.72] dealing with
[3187.72 → 3188.92] terabytes of data
[3188.92 → 3190.20] and hundreds of thousands
[3190.20 → 3190.94] of millions of users
[3190.94 → 3191.62] and that sort of thing
[3191.62 → 3192.78] so if anything
[3192.78 → 3193.34] he's ecstatic
[3193.34 → 3194.06] him and Kyle
[3194.06 → 3194.86] work really well together
[3194.86 → 3196.26] Kyle is doing a great job
[3196.26 → 3197.16] and Tom's able to focus
[3197.16 → 3197.80] on what he's really
[3197.80 → 3198.48] really interested in
[3198.48 → 3198.96] and good at
[3198.96 → 3200.46] we've been talking about
[3200.46 → 3201.30] GitHub for a long time
[3201.30 → 3202.20] maybe we can talk about
[3202.20 → 3203.62] just you for just a second
[3203.62 → 3205.00] you know
[3205.00 → 3206.46] I guess wrapped up
[3206.46 → 3207.00] in all this
[3207.00 → 3208.04] is you
[3208.04 → 3208.58] Tom
[3208.58 → 3209.96] and PJ
[3209.96 → 3211.48] and some of the new hires
[3211.48 → 3211.92] that you brought on
[3211.92 → 3212.72] like Scott and what not
[3212.72 → 3213.90] but you guys
[3213.90 → 3214.84] have all been leading this
[3214.84 → 3216.02] and you said in a previous chat
[3216.02 → 3216.62] you guys are all
[3216.62 → 3217.58] you have to be Superman
[3217.58 → 3219.42] how can you be Superman
[3219.42 → 3220.82] in a small lean company
[3220.82 → 3221.50] like you are
[3221.50 → 3223.30] going in a profitable state
[3223.30 → 3224.46] and still keep up
[3224.46 → 3224.90] with your hobby
[3224.90 → 3225.78] and run the business
[3225.78 → 3226.54] how do you do that?
[3229.82 → 3230.90] I mean when you say it like that
[3230.90 → 3232.06] it sounds a lot more incredible
[3232.06 → 3232.92] than it really is
[3232.92 → 3233.22] this is
[3233.22 → 3234.68] really this is just a job
[3234.68 → 3235.78] if you think about it
[3235.78 → 3236.58] and that's kind of
[3236.58 → 3237.20] how you have to treat it
[3237.20 → 3238.04] when you get up in the morning
[3238.04 → 3238.90] you have to have
[3238.90 → 3241.14] time when you're not at work
[3241.14 → 3242.04] you have to you know
[3242.04 → 3242.76] take a shower
[3242.76 → 3243.52] do whatever you do
[3243.52 → 3244.06] in your daily routine
[3244.06 → 3244.68] make your coffee
[3244.68 → 3245.78] and you're not at work
[3245.78 → 3246.46] and you can be thinking
[3246.46 → 3247.28] about a cool feature
[3247.28 → 3248.36] or a cool idea
[3248.36 → 3249.72] but that's what you should be doing
[3249.72 → 3250.28] at your job anyway
[3250.28 → 3251.02] you can't let it kind of
[3251.02 → 3252.22] take over in that regard
[3252.22 → 3253.36] and then you get to work
[3253.36 → 3254.80] and then you just focus
[3254.80 → 3255.30] I mean
[3255.30 → 3258.74] you don't focus for 8 hours a day
[3258.74 → 3259.76] just like you didn't do that
[3259.76 → 3260.32] you don't do that
[3260.32 → 3261.32] in your normal job
[3261.32 → 3262.82] and you don't have
[3262.82 → 3263.48] the best day
[3263.48 → 3264.40] of your life every day
[3264.40 → 3266.16] but one of the advantages
[3266.16 → 3267.38] and one of the things
[3267.38 → 3268.48] that I think you have to be good at
[3268.48 → 3269.04] is
[3269.04 → 3271.04] if you get on a roll
[3271.04 → 3273.04] let's say you had a horrible day
[3273.04 → 3274.06] and you didn't even get anything done
[3274.06 → 3274.76] until 4pm
[3274.76 → 3275.66] and you don't even know
[3275.66 → 3276.30] where your morning went
[3276.30 → 3278.00] but you start getting into a groove
[3278.00 → 3279.80] around 4 and then 5
[3279.80 → 3280.88] and you're making test paths
[3280.88 → 3281.54] and that sort of thing
[3281.54 → 3283.10] I mean I think with our team
[3283.10 → 3284.66] and with small teams
[3284.66 → 3285.20] it's really important
[3285.20 → 3287.94] the ability to stay on task
[3287.94 → 3288.96] until you know
[3288.96 → 3290.06] 2am
[3290.06 → 3291.30] until you finish
[3291.30 → 3292.00] what you're working on
[3292.00 → 3292.66] and until you're really
[3292.66 → 3293.44] really happy with it
[3293.44 → 3295.16] is probably the most important trait
[3295.16 → 3296.00] is just to have
[3296.00 → 3297.32] just to know
[3297.32 → 3298.22] when you need to focus
[3298.22 → 3299.52] it's not focusing all the time
[3299.52 → 3300.82] or anything like that
[3300.82 → 3301.98] but knowing when you need to focus
[3301.98 → 3302.96] and when you need to get something done
[3302.96 → 3304.26] knowing when something is done
[3304.26 → 3305.78] and just doing everything
[3305.78 → 3306.44] so that it's good
[3306.44 → 3307.66] not harassing stuff like that
[3307.66 → 3308.70] I think that's what's really important
[3308.70 → 3309.86] for our small team
[3309.86 → 3310.66] and
[3310.66 → 3311.64] you know that
[3311.64 → 3312.32] that is really hard
[3312.32 → 3313.44] because you can't work till
[3313.44 → 3314.88] 2am every day
[3314.88 → 3315.96] and otherwise
[3315.96 → 3316.78] you just get burnt out
[3316.78 → 3317.24] and then you know
[3317.24 → 3317.60] the next day
[3317.60 → 3319.08] your sleeping schedule is all messed up
[3319.08 → 3320.74] but I think being able to identify
[3320.74 → 3321.74] and
[3321.74 → 3323.26] kind of build your day around
[3323.26 → 3323.64] you know
[3323.64 → 3324.00] in the morning
[3324.00 → 3324.44] I'm going to do
[3324.44 → 3325.18] these like
[3325.18 → 3326.14] support work
[3326.14 → 3327.00] and that's going to
[3327.00 → 3327.78] not require
[3327.78 → 3329.46] long periods of time
[3329.46 → 3329.88] of attention
[3329.88 → 3330.94] and then in the afternoon
[3330.94 → 3331.62] I'm going to have a meeting
[3331.62 → 3332.56] and then I'm going to work on this
[3332.56 → 3333.76] feature I've had in the back burner
[3333.76 → 3334.74] and then tomorrow
[3334.74 → 3335.80] when I have most of the day open
[3335.80 → 3336.54] that's when I'm going to spend
[3336.54 → 3337.16] the whole day
[3337.16 → 3338.74] crushing this really huge feature
[3338.74 → 3339.38] that we've been working
[3339.38 → 3341.04] and I'd really like to work on it today
[3341.04 → 3342.10] because we're behind on it
[3342.10 → 3342.68] but
[3342.68 → 3343.54] you know
[3343.54 → 3345.14] I can schedule my time
[3345.14 → 3346.30] so that I can just work on it tomorrow
[3346.30 → 3347.28] and it'll be worth it
[3347.28 → 3348.12] so I think for us
[3348.12 → 3349.08] that's kind of important right?
[3349.68 → 3349.80] yeah
[3349.80 → 3350.36] absolutely
[3350.36 → 3351.24] yeah I'm pushing back
[3351.24 → 3352.36] so much stuff right now
[3352.36 → 3353.16] awesome
[3353.16 → 3354.28] but yeah
[3354.28 → 3354.54] I think
[3354.54 → 3355.76] the Superman part
[3355.76 → 3357.34] isn't from being able to do everything
[3357.34 → 3360.06] it's just being able to know
[3360.06 → 3361.14] like what needs to get done
[3361.14 → 3361.86] in a small company
[3361.86 → 3362.82] and I mean
[3362.82 → 3364.00] I think the most important thing there
[3364.00 → 3365.52] is you're not working until 2am
[3365.52 → 3367.14] because your boss is telling you
[3367.14 → 3368.04] this needs to get done tomorrow
[3368.04 → 3369.28] so you have to recognize
[3369.28 → 3370.52] what is important
[3370.52 → 3371.96] because when you're a small team
[3371.96 → 3372.54] you can't have
[3372.54 → 3374.38] babysitting be one of your jobs
[3374.38 → 3374.96] you can't be
[3374.96 → 3375.92] managing
[3375.92 → 3376.60] you know
[3376.60 → 3377.06] a team
[3377.06 → 3378.50] when there's only eight people on there
[3378.50 → 3379.06] they all need to be
[3379.06 → 3380.00] pulling their full weight
[3380.00 → 3380.74] and they need to be able
[3380.74 → 3381.56] to be self-starters
[3381.56 → 3383.16] and be self-motivated
[3383.16 → 3383.58] in a way
[3383.58 → 3383.92] and
[3383.92 → 3384.74] you know
[3384.74 → 3385.80] one of the great things about
[3385.80 → 3387.04] not having an office for so long
[3387.04 → 3387.46] is that
[3387.46 → 3388.66] we've found people
[3388.66 → 3389.62] that can work at home
[3389.62 → 3390.08] alone
[3390.08 → 3390.68] you know
[3390.68 → 3391.34] just like
[3391.34 → 3391.82] Kyle
[3391.82 → 3392.90] go make the site look pretty
[3392.90 → 3393.54] and then like
[3393.54 → 3393.94] two months later
[3393.94 → 3394.48] he comes back
[3394.48 → 3394.98] and it's amazing
[3394.98 → 3396.00] we need people like that
[3396.00 → 3397.48] and that's really what you need to have
[3397.48 → 3398.44] and it's really hard to find
[3398.44 → 3398.96] this kind of people
[3398.96 → 3399.34] but
[3399.34 → 3400.52] I think once you do
[3400.52 → 3401.76] it shows
[3401.76 → 3402.62] in the product
[3402.62 → 3403.50] and we've been
[3403.50 → 3404.26] working very hard
[3404.26 → 3404.76] to find those people
[3404.76 → 3405.16] and I think we're doing
[3405.16 → 3405.82] a good job of it
[3405.82 → 3406.64] absolutely
[3406.64 → 3407.80] so passion
[3407.80 → 3408.74] is where it all comes from
[3408.74 → 3410.88] I think so
[3410.88 → 3411.64] I think it might be that
[3411.64 → 3412.04] but I think
[3412.04 → 3413.66] what it is for a lot of us
[3413.66 → 3414.76] is that we use the site
[3414.76 → 3416.58] and it's not even passion
[3416.58 → 3418.06] about loving working on the site
[3418.06 → 3418.52] it's that
[3418.52 → 3419.36] I don't want to
[3419.36 → 3420.58] settle
[3420.58 → 3421.56] you know
[3421.56 → 3422.32] I don't want to
[3422.32 → 3423.26] build something
[3423.26 → 3424.18] that I'm going to use
[3424.18 → 3425.00] that I'm not going to like
[3425.00 → 3426.40] so if it's going to be crappy
[3426.40 → 3427.62] just don't even bother with it
[3427.62 → 3428.78] only spend the time on it
[3428.78 → 3429.60] to make it perfect
[3429.60 → 3430.90] and in a lot of cases
[3430.90 → 3432.30] let's say you work on something
[3432.30 → 3433.42] for two weeks
[3433.42 → 3434.20] you know
[3434.20 → 3436.08] it might only be an extra two days
[3436.08 → 3437.66] to make it really, really pop
[3437.66 → 3438.78] and that is
[3438.78 → 3439.98] always worth it
[3439.98 → 3440.72] it's always worth it
[3440.72 → 3441.04] and
[3441.04 → 3442.32] I think that's what it's about
[3442.32 → 3443.66] it's making something for yourself
[3443.66 → 3445.18] that you want to use
[3445.18 → 3445.80] and I don't even know
[3445.80 → 3446.32] if that's passion
[3446.32 → 3447.60] that's just being practical
[3447.60 → 3448.46] in a lot of ways
[3448.46 → 3449.66] it's like I don't want to have
[3449.66 → 3450.48] broken stuff
[3450.48 → 3451.94] and if it's up to me
[3451.94 → 3452.82] if I'm the reason
[3452.82 → 3453.84] that it's broken or not broken
[3453.84 → 3454.86] then you know
[3454.86 → 3455.84] there's only one real option there
[3455.84 → 3456.06] it's
[3456.06 → 3457.56] I need to make it not broken
[3457.56 → 3459.16] and I think a lot of people
[3459.16 → 3460.22] on our team feel the same way
[3460.22 → 3461.74] that kind of leads us
[3461.74 → 3461.98] into
[3461.98 → 3463.92] this other larger question
[3463.92 → 3464.48] I wanted to ask
[3464.48 → 3465.00] before we
[3465.00 → 3466.54] start tailing this off
[3466.54 → 3468.04] with no pun intended
[3468.04 → 3469.08] for a later conversation
[3469.08 → 3469.38] but
[3469.38 → 3470.68] I wanted to
[3470.68 → 3471.54] ask you
[3471.54 → 3472.32] about
[3472.32 → 3473.60] this
[3473.60 → 3473.84] I mean
[3473.84 → 3474.56] many have set
[3474.56 → 3475.00] you know
[3475.00 → 3475.38] kind of
[3475.38 → 3476.02] just sat back
[3476.02 → 3476.36] in awe
[3476.36 → 3476.96] about your ability
[3476.96 → 3477.42] to
[3477.42 → 3479.12] fund this business
[3479.12 → 3479.86] without VC
[3479.86 → 3481.20] and I'm sure
[3481.20 → 3481.88] that so many people
[3481.88 → 3482.72] ask you this question
[3482.72 → 3483.88] whenever you're
[3483.88 → 3484.44] keynoting
[3484.44 → 3485.30] or speaking at a conference
[3485.30 → 3486.22] like how did you guys
[3486.22 → 3487.36] truly go
[3487.36 → 3488.70] and build GitHub.com
[3488.70 → 3489.68] without any VC funding
[3489.68 → 3490.58] like what does it take
[3490.58 → 3491.08] to do that
[3491.08 → 3492.42] and how did you do it
[3492.42 → 3494.32] well
[3494.32 → 3496.30] we had a lot of help
[3496.30 → 3496.82] from people
[3496.82 → 3498.36] for instance
[3498.36 → 3498.76] Engine Yard
[3498.76 → 3499.76] like I said early on
[3499.76 → 3500.72] helped us out
[3500.72 → 3501.30] in a lot of ways
[3501.30 → 3502.30] they covered our hosting
[3502.30 → 3503.00] and that sort of thing
[3503.00 → 3503.98] so when we were growing
[3503.98 → 3504.90] you know
[3504.90 → 3505.56] they were really there
[3505.56 → 3506.28] supporting us
[3506.28 → 3507.56] and
[3507.56 → 3509.76] it helps to have a partner
[3509.76 → 3510.34] because
[3510.34 → 3511.64] or someone else
[3511.64 → 3512.30] co-founders
[3512.30 → 3513.92] because then like I said
[3513.92 → 3514.72] it would have been easy
[3514.72 → 3515.48] to say
[3515.48 → 3516.50] I'm going to take
[3516.50 → 3517.26] a month off
[3517.26 → 3517.74] and just focus
[3517.74 → 3518.72] on consulting full-time
[3518.72 → 3520.94] it's a lot easier
[3520.94 → 3521.66] to let yourself down
[3521.66 → 3522.26] than someone else
[3522.26 → 3522.64] so
[3522.64 → 3523.76] you can't really say that
[3523.76 → 3524.48] if you have someone else
[3524.48 → 3525.08] who's working on it
[3525.08 → 3525.62] every weekend
[3525.62 → 3526.90] you kind of need to
[3526.90 → 3527.92] I mean if you have any
[3527.92 → 3528.72] sort of shame
[3528.72 → 3529.14] or guilt
[3529.14 → 3530.14] you're going to feel like
[3530.14 → 3530.70] well you know
[3530.70 → 3532.48] Tom is working on this
[3532.48 → 3533.64] he's been working on this
[3533.64 → 3534.32] for the past four weeks
[3534.32 → 3534.96] and I haven't done anything
[3534.96 → 3535.96] I really need to catch up
[3535.96 → 3536.86] I really need to work on this
[3536.86 → 3537.72] or maybe I shouldn't
[3537.72 → 3538.74] take off for four weeks
[3538.74 → 3539.36] and that sort of thing
[3539.36 → 3540.40] so
[3540.40 → 3541.44] you know I think
[3541.44 → 3542.26] a lot of it was being
[3542.26 → 3542.74] in the right place
[3542.74 → 3543.34] at the right time
[3543.34 → 3544.02] we were just building
[3544.02 → 3544.94] a site for ourselves
[3544.94 → 3546.08] that we wanted to use
[3546.08 → 3546.98] and we have done that
[3546.98 → 3548.28] a hundred times before
[3548.28 → 3548.86] we've built
[3548.86 → 3550.04] between me
[3550.04 → 3550.34] Tom
[3550.34 → 3550.64] PJ
[3550.64 → 3551.72] and even if you want to
[3551.72 → 3552.16] count the other people
[3552.16 → 3552.72] in the company now
[3552.72 → 3553.14] Ryan
[3553.14 → 3553.80] Kyle
[3553.80 → 3554.78] Tea
[3554.78 → 3555.48] Melissa
[3555.48 → 3556.20] Scott
[3556.20 → 3557.44] you know we've all built stuff
[3557.44 → 3558.60] countless number of times
[3558.60 → 3559.26] for ourselves
[3559.26 → 3560.88] and with the same philosophy
[3560.88 → 3561.86] that I'm sure you guys have
[3561.86 → 3562.08] you know
[3562.08 → 3563.34] I'm going to build it for myself
[3563.34 → 3564.12] I don't want it to be broken
[3564.12 → 3564.90] I want it to be awesome
[3564.90 → 3567.34] and GitHub was just the one time
[3567.34 → 3568.40] where it happened to work
[3568.40 → 3569.94] everything just lined up
[3569.94 → 3571.32] we were in the right place
[3571.32 → 3572.00] at the right time
[3572.00 → 3573.56] we had the right kind of jobs
[3573.56 → 3574.24] the right kind of money
[3574.24 → 3574.90] in our bank account
[3574.90 → 3576.88] and it just worked
[3576.88 → 3578.10] and so I think a lot of it
[3578.10 → 3578.98] is just you know
[3578.98 → 3579.54] persistence
[3579.54 → 3581.46] it's sticking with something
[3581.46 → 3582.24] until it does work
[3582.24 → 3583.58] and also knowing
[3583.58 → 3585.62] exactly when to
[3585.62 → 3586.66] to kill something
[3586.66 → 3587.94] exactly when to not launch
[3587.94 → 3588.34] that feature
[3588.34 → 3589.02] because it sucks
[3589.02 → 3590.04] you know PJ and I
[3590.04 → 3590.66] had another startup
[3590.66 → 3591.18] before GitHub
[3591.18 → 3592.20] called Tampa
[3592.20 → 3593.30] and it launched
[3593.30 → 3595.52] in December 2007
[3595.52 → 3596.94] and then the GitHub
[3596.94 → 3597.78] beta launched
[3597.78 → 3598.70] in January 2008
[3598.70 → 3599.64] we were going to get up
[3599.64 → 3600.10] on the side
[3600.10 → 3602.06] and I think by February 2008
[3602.06 → 3602.98] or March 2008
[3602.98 → 3603.86] we just knew
[3603.86 → 3605.00] that we had to kill
[3605.00 → 3606.14] stop working on Tampa
[3606.14 → 3606.78] and work full-time
[3606.78 → 3607.06] on GitHub
[3607.06 → 3608.08] because it was obvious
[3608.08 → 3608.70] that this was the thing
[3608.70 → 3609.52] that was going to
[3609.52 → 3609.80] you know
[3609.80 → 3611.20] lead us to financial independence
[3611.20 → 3612.22] and we were right
[3612.22 → 3613.06] and I think
[3613.06 → 3614.40] because we had invested
[3614.40 → 3615.38] so much more money
[3615.38 → 3616.10] in time in Tampa
[3616.10 → 3616.56] at the time
[3616.56 → 3617.54] and it would have been
[3617.54 → 3618.14] easy for us to say
[3618.14 → 3618.90] oh well we already have
[3618.90 → 3619.68] this thousand of bucks
[3619.68 → 3620.50] wrapped up in this other thing
[3620.50 → 3621.36] let's just see it through
[3621.36 → 3622.52] and you know
[3622.52 → 3623.16] maybe it would have been
[3623.16 → 3624.08] a colossal success
[3624.08 → 3626.16] but it wasn't
[3626.16 → 3626.84] at the time
[3626.84 → 3627.76] and I don't think
[3627.76 → 3628.10] we would have been
[3628.10 → 3628.70] happier doing that
[3628.70 → 3629.48] than we are right now
[3629.48 → 3630.60] you know you've
[3630.60 → 3631.74] you've said persistence
[3631.74 → 3633.20] I think early
[3633.20 → 3633.82] in the podcast
[3633.82 → 3635.30] in regard to something
[3635.30 → 3636.46] I can't recall exactly what
[3636.46 → 3638.30] but I think it was
[3638.30 → 3638.98] like what keeps you up
[3638.98 → 3639.74] and what keeps you going
[3639.74 → 3641.74] but a good friend of mine
[3641.74 → 3642.62] Kevin Milton
[3642.62 → 3643.26] from New Leaders
[3643.26 → 3644.26] I'm not sure if you're
[3644.26 → 3644.76] familiar with him
[3644.76 → 3646.62] but he's not far
[3646.62 → 3647.42] from releasing this
[3647.42 → 3648.20] this book called
[3648.20 → 3648.84] Lesson for Leaders
[3648.84 → 3650.94] and there's one quote
[3650.94 → 3651.84] in the very opening
[3651.84 → 3652.48] of this book
[3652.48 → 3653.88] that says
[3653.88 → 3654.40] persistence
[3654.40 → 3656.20] always triumphs
[3656.20 → 3657.02] never give up
[3657.02 → 3658.12] how do you feel about that?
[3658.98 → 3660.62] I have mixed feelings
[3660.62 → 3660.90] on that
[3660.90 → 3661.52] because if we had
[3661.52 → 3662.74] persisted with Tampa
[3662.74 → 3663.76] where would we be right now?
[3665.08 → 3666.12] I think it's about
[3666.12 → 3666.90] not
[3666.90 → 3668.02] persistence I guess
[3668.02 → 3668.62] maybe with
[3668.62 → 3670.66] with an understanding
[3670.66 → 3671.28] of where you're going
[3671.28 → 3672.02] yeah
[3672.02 → 3673.00] I think
[3673.00 → 3674.50] not giving up
[3674.50 → 3674.80] on something
[3674.80 → 3675.26] that you have
[3675.26 → 3676.12] a good feeling about
[3676.12 → 3677.10] is very important
[3677.10 → 3677.68] and that sounds
[3677.68 → 3678.28] sort of like
[3678.28 → 3679.20] stupid and obvious
[3679.20 → 3680.02] but you know
[3680.02 → 3680.46] how many times
[3680.46 → 3680.74] have you had
[3680.74 → 3681.40] a New Year's resolution
[3681.40 → 3681.98] where you wanted
[3681.98 → 3682.56] to do something
[3682.56 → 3683.60] and then you like
[3683.60 → 3684.52] stopped after a month
[3684.52 → 3685.16] or how many times
[3685.16 → 3685.56] have you decided
[3685.56 → 3687.00] to go try some new hobby
[3687.00 → 3688.24] and stopped after two weeks
[3688.24 → 3688.76] and even though
[3688.76 → 3689.16] you want to
[3689.16 → 3689.72] you want to learn
[3689.72 → 3690.30] guitar better
[3690.30 → 3690.82] or you want to
[3690.82 → 3691.30] just learn better
[3691.30 → 3692.20] you just didn't
[3692.20 → 3692.68] you just didn't
[3692.68 → 3693.16] stick with it
[3693.16 → 3693.38] you know
[3693.38 → 3693.96] and for whatever
[3693.96 → 3695.18] and I think
[3695.18 → 3695.88] that's
[3695.88 → 3696.70] that's the thing
[3696.70 → 3697.44] you have to fight against
[3697.44 → 3697.86] is
[3697.86 → 3698.84] even though you're
[3698.84 → 3699.40] in week four
[3699.40 → 3700.12] of you know
[3700.12 → 3701.18] playing guitar every day
[3701.18 → 3702.10] and you don't
[3702.10 → 3702.68] really want to do it
[3702.68 → 3703.10] you'd rather be
[3703.10 → 3704.06] watching TV or something
[3704.06 → 3704.64] or you'd rather be
[3704.64 → 3705.36] even working on
[3705.36 → 3706.04] your website
[3706.04 → 3706.56] you know
[3706.56 → 3707.16] just stick with it
[3707.16 → 3708.18] because in the end
[3708.18 → 3708.76] you got it
[3708.76 → 3709.50] you want to hit your goal
[3709.50 → 3710.54] or it will be worth it
[3710.54 → 3711.00] in some way
[3711.00 → 3711.98] and I think for us
[3711.98 → 3712.42] that was it
[3712.42 → 3712.98] I mean a lot of times
[3712.98 → 3713.46] it would have been easier
[3713.46 → 3714.58] just to not work on the site
[3714.58 → 3715.50] or just go back to
[3715.50 → 3716.92] making consulting money
[3716.92 → 3717.98] but we stuck with it
[3717.98 → 3718.50] because we had
[3718.50 → 3719.68] the goal in mind
[3719.68 → 3720.18] and so yeah
[3720.18 → 3720.80] I agree with that
[3720.80 → 3722.80] well I know you're west coast
[3722.80 → 3723.30] but so
[3723.30 → 3725.04] we're not here after dark
[3725.04 → 3725.56] let's go ahead
[3725.56 → 3726.18] and ask you
[3726.18 → 3726.76] what's on your
[3726.76 → 3727.52] open source radio
[3727.52 → 3728.30] I'm looking at your
[3728.30 → 3729.78] watched repos on GitHub
[3729.78 → 3732.52] and it's almost
[3732.52 → 3733.46] half the
[3733.46 → 3735.94] the GitHub list there
[3735.94 → 3737.16] so what excites you
[3737.16 → 3738.04] in the world of open source
[3738.04 → 3740.06] right now I think
[3740.06 → 3740.72] I mean I've been doing
[3740.72 → 3741.66] it sounds kind of cheesy
[3741.66 → 3742.66] I've been doing a lot of stuff
[3742.66 → 3744.10] with like old school
[3744.10 → 3744.80] Unix
[3744.80 → 3745.44] I guess
[3745.44 → 3747.38] knowledge mining
[3747.38 → 3747.98] I just read the
[3747.98 → 3748.72] art of Unix programming
[3748.72 → 3749.68] by Eric Raymond
[3749.68 → 3751.62] and I'm trying to get a feel for
[3751.62 → 3752.86] you know how the people
[3752.86 → 3755.36] in the generations before us
[3755.36 → 3756.50] kind of thought about
[3756.50 → 3757.18] software development
[3757.18 → 3758.36] and you know
[3758.36 → 3759.38] what tools they used
[3759.38 → 3760.74] how those tools
[3760.74 → 3761.38] were put together
[3761.38 → 3762.80] and that sort of thing
[3762.80 → 3763.44] and learning about
[3763.44 → 3764.20] you know the origins
[3764.20 → 3764.78] of everything from
[3764.78 → 3765.92] standard out to standard error
[3765.92 → 3766.96] and what they're for
[3766.96 → 3768.74] you know
[3768.74 → 3770.04] Ryan Tom eco just released
[3770.04 → 3770.68] this thing Ron
[3770.68 → 3771.70] for generating man pages
[3771.70 → 3772.40] which I've been using
[3772.40 → 3773.28] in all my new projects
[3773.28 → 3774.32] and sort of writing
[3774.32 → 3775.66] like perfect
[3775.66 → 3776.86] Unix tools
[3776.86 → 3777.88] that help development
[3777.88 → 3778.98] and can help
[3778.98 → 3779.84] for all sorts of things
[3779.84 → 3780.34] like deployment
[3780.34 → 3782.04] and any sort of
[3782.04 → 3782.88] programming task
[3782.88 → 3784.10] so I've been really
[3784.10 → 3784.98] interested in learning
[3784.98 → 3785.44] about you know
[3785.44 → 3786.78] the ideas and philosophies
[3786.78 → 3787.58] behind some of the people
[3787.58 → 3788.86] that came before us
[3788.86 → 3789.86] in a sense of speaking
[3789.86 → 3790.58] internet years
[3790.58 → 3791.08] let's say
[3791.08 → 3792.12] and just the origins
[3792.12 → 3792.58] of the internet
[3792.58 → 3793.28] and that sort of thing
[3793.28 → 3794.34] so for me
[3794.34 → 3795.28] that's been pretty exciting
[3795.28 → 3796.08] it's just kind of like
[3796.08 → 3797.98] reading about problems
[3797.98 → 3798.98] that have already been solved
[3798.98 → 3800.04] in a way that
[3800.04 → 3802.32] I'm intimately familiar with
[3802.32 → 3803.10] that I didn't even know
[3803.10 → 3803.70] was a problem
[3803.70 → 3804.92] just things like
[3804.92 → 3807.20] you know
[3807.20 → 3808.04] just like Unix pipes
[3808.04 → 3808.80] which you take for granted
[3808.80 → 3809.34] every day
[3809.34 → 3809.60] you know
[3809.60 → 3810.66] they were invented by someone
[3810.66 → 3811.68] to solve some problem
[3811.68 → 3812.90] and what was the thinking there
[3812.90 → 3814.12] and it's pretty awesome
[3814.12 → 3814.96] just reading about that stuff
[3814.96 → 3815.98] and the motivation behind it
[3815.98 → 3816.94] it's like when the guy
[3816.94 → 3817.86] who invented ramen
[3817.86 → 3818.80] died a couple of years ago
[3818.80 → 3819.22] you're like what
[3819.22 → 3820.12] someone invented ramen
[3820.12 → 3820.96] it's like well yeah
[3820.96 → 3821.38] of course
[3821.38 → 3821.70] everything
[3821.70 → 3823.24] someone has to start something
[3823.24 → 3823.92] you know
[3823.92 → 3824.66] and before ramen
[3824.66 → 3825.64] you know
[3825.64 → 3826.14] what do they do
[3826.14 → 3826.64] I don't even know
[3826.64 → 3827.14] but after ramen
[3827.14 → 3827.90] it just seems so obvious
[3827.90 → 3828.86] so a lot of that stuff
[3828.86 → 3829.46] has been pretty interesting
[3829.46 → 3831.54] a lot of college kids starved
[3831.54 → 3832.64] exactly
[3832.64 → 3833.82] exactly
[3833.82 → 3834.52] but
[3834.52 → 3835.56] and then other than that
[3835.56 → 3836.14] as far as like
[3836.14 → 3837.46] so Ron is
[3837.46 → 3838.40] art to make a slash Ron
[3838.40 → 3839.00] is a cool project
[3839.00 → 3840.52] for generating man pages
[3840.52 → 3841.46] it's in Ruby
[3841.46 → 3843.22] so if you have Ruby scripts
[3843.22 → 3844.04] I've been using them
[3844.04 → 3845.68] another thing I've been interested in
[3845.68 → 3847.10] is writing Ruby scripts
[3847.10 → 3847.48] that
[3847.48 → 3849.10] the fact that they're written
[3849.10 → 3849.48] in Ruby
[3849.48 → 3850.68] is incidental
[3850.68 → 3851.90] so I have this script hub
[3851.90 → 3852.92] which works with GitHub
[3852.92 → 3854.00] and can wrap git
[3854.00 → 3854.90] and the idea there
[3854.90 → 3855.20] is that
[3855.20 → 3855.84] it doesn't matter
[3855.84 → 3856.08] if you
[3856.08 → 3857.88] if you have Ruby
[3857.88 → 3859.04] if you have Ruby gems
[3859.04 → 3859.74] and that sort of thing
[3859.74 → 3860.60] it doesn't matter
[3860.60 → 3861.16] you don't need to know
[3861.16 → 3861.66] anything about Ruby
[3861.66 → 3862.76] it should be really easy
[3862.76 → 3863.26] to install
[3863.26 → 3863.90] and it should work
[3863.90 → 3864.50] just like any
[3864.50 → 3865.86] Unix command line script
[3865.86 → 3866.36] that you have
[3866.36 → 3867.66] and the inspiration for this
[3867.66 → 3868.00] is kind of
[3868.00 → 3868.40] ACK
[3868.40 → 3869.78] which is
[3869.78 → 3870.52] sort of like
[3870.52 → 3871.58] a grew replacement
[3871.58 → 3872.96] it's better than grep.com
[3872.96 → 3874.48] and it's written in Perl
[3874.48 → 3875.24] but
[3875.24 → 3876.88] you don't need to install it
[3876.88 → 3877.50] through CAN
[3877.50 → 3878.54] or even know what that means
[3878.54 → 3879.58] if you have Perl installed
[3879.58 → 3880.00] in your system
[3880.00 → 3880.96] you can just run
[3880.96 → 3881.70] his little one-liner
[3881.70 → 3882.40] and then now you have
[3882.40 → 3883.04] ACK installed
[3883.04 → 3884.22] and everything's just in one script
[3884.22 → 3884.86] there are no dependencies
[3884.86 → 3885.84] you don't fudge with it
[3885.84 → 3886.58] it just works
[3886.58 → 3888.12] and so I think there's a lot of
[3888.12 → 3888.74] appeal to writing
[3888.74 → 3890.10] scripts that way
[3890.10 → 3891.10] in your language of choice
[3891.10 → 3891.50] and you know
[3891.50 → 3892.80] whether it's in Python or Ruby
[3892.80 → 3893.78] sort of like
[3893.78 → 3894.52] hide that
[3894.52 → 3896.52] and it's tempting to be like
[3896.52 → 3897.80] oh I'm writing a Ruby project
[3897.80 → 3898.34] and I want to like
[3898.34 → 3899.10] make it Rock
[3899.10 → 3900.04] or use Yard Doc
[3900.04 → 3901.74] and make all these Spec tests
[3901.74 → 3902.94] and then you know
[3902.94 → 3904.78] have the README be an Rock
[3904.78 → 3906.08] and make it a gem install
[3906.08 → 3906.58] and all that stuff
[3906.58 → 3907.14] is really awesome
[3907.14 → 3907.84] for Ruby developers
[3907.84 → 3908.80] but there's a lot of
[3908.80 → 3909.48] assumptions there
[3909.48 → 3911.52] and to see what I'm talking about
[3911.52 → 3912.78] try diving into another language
[3912.78 → 3913.60] that you don't know
[3913.60 → 3914.56] for a while
[3914.56 → 3916.52] and just sort of like
[3916.52 → 3917.42] play with some of the projects
[3917.42 → 3918.08] and you'll have
[3918.08 → 3919.38] situations where you're like
[3919.38 → 3920.08] alright well I don't even know
[3920.08 → 3921.10] how to run these tests
[3921.10 → 3922.20] it doesn't stay anywhere
[3922.20 → 3923.28] because I'm not a
[3923.28 → 3923.90] you know
[3923.90 → 3924.74] X programmer
[3924.74 → 3926.08] and this is written for
[3926.08 → 3926.66] X programmers
[3926.66 → 3927.90] so writing projects for people
[3927.90 → 3929.04] that aren't necessarily
[3929.04 → 3929.74] Ruby programmers
[3929.74 → 3930.70] or Python programmers
[3930.70 → 3931.68] just people that are using
[3931.68 → 3932.08] Unix
[3932.08 → 3932.98] is pretty interesting
[3932.98 → 3933.52] to me right now
[3933.52 → 3934.56] because you know
[3934.56 → 3935.60] almost everything
[3935.60 → 3936.34] on the command line
[3936.34 → 3937.04] is written that way
[3937.04 → 3937.82] every project you use
[3937.82 → 3938.68] you don't care if it's in C
[3938.68 → 3939.16] or Perl
[3939.16 → 3940.48] or even both
[3940.48 → 3940.98] like Git
[3940.98 → 3941.92] all you care about
[3941.92 → 3942.50] is what it's doing
[3942.50 → 3943.16] and so I think there's
[3943.16 → 3943.86] a lot of appeal there
[3943.86 → 3944.50] and it's kind of
[3944.50 → 3946.10] unfortunately a lost art
[3946.10 → 3946.78] to us like
[3946.78 → 3948.14] mainly web developers
[3948.14 → 3949.84] and I think that there's
[3949.84 → 3950.90] a lot that can be done there
[3950.90 → 3952.18] so other than that
[3952.18 → 3952.82] I've been playing
[3952.82 → 3953.58] with just Node.js
[3953.58 → 3954.78] which I guess
[3954.78 → 3955.76] is like
[3955.76 → 3957.34] everyone else's favourite
[3957.34 → 3958.44] side project right now
[3958.44 → 3960.06] and it's interesting
[3960.06 → 3960.66] because I've always loved
[3960.66 → 3961.00] JavaScript
[3961.00 → 3961.84] we use a ton of JavaScript
[3961.84 → 3962.28] on GitHub
[3962.28 → 3964.08] and being able to use that
[3964.08 → 3965.16] in a server environment
[3965.16 → 3966.28] that's superfast
[3966.28 → 3967.48] and has tons of like
[3967.48 → 3968.30] new libraries
[3968.30 → 3969.14] for interesting new tech
[3969.14 → 3969.58] coming out
[3969.58 → 3970.54] is pretty interesting
[3970.54 → 3972.22] it's also fun
[3972.22 → 3972.76] to be able to use
[3972.76 → 3973.96] it seems to be getting
[3973.96 → 3974.54] a lot of momentum
[3974.54 → 3975.66] have you built anything
[3975.66 → 3976.34] of consequence
[3976.34 → 3977.82] personally with Node.js yet?
[3978.58 → 3979.22] Nothing public
[3979.22 → 3980.10] I've worked on some
[3980.10 → 3981.04] IRC stuff
[3981.04 → 3981.48] and some
[3981.48 → 3982.08] you know
[3982.08 → 3983.08] just buzzword
[3983.08 → 3983.64] real time
[3983.64 → 3984.68] browser stuff with it
[3984.68 → 3985.84] but nothing public
[3985.84 → 3987.04] I'm trying to move on
[3987.04 → 3987.38] What is the sweet spot
[3987.38 → 3988.38] for this particular
[3988.38 → 3989.46] framework?
[3990.70 → 3990.96] I think
[3990.96 → 3991.68] the sweet
[3991.68 → 3992.62] well from my experience
[3992.62 → 3993.36] I think the sweet spot
[3993.36 → 3993.98] is when you have
[3993.98 → 3994.56] a lot of JavaScript
[3994.56 → 3996.26] and you can share libraries
[3996.26 → 3997.10] between the front end
[3997.10 → 3997.64] and the back end
[3997.64 → 3998.88] so your template engine
[3998.88 → 4000.12] and things like that
[4000.12 → 4000.76] you can just load it
[4000.76 → 4001.36] in the back end
[4001.36 → 4002.32] load it in the front end
[4002.32 → 4003.08] and then now you're
[4003.08 → 4004.00] just passing templates
[4004.00 → 4005.20] and JSON back and forth
[4005.20 → 4006.02] and you can render it
[4006.02 → 4006.32] wherever
[4006.32 → 4007.44] if it's the first page load
[4007.44 → 4008.30] you can render it in Node
[4008.30 → 4009.96] if it's a little snippet
[4009.96 → 4010.52] or a partial
[4010.52 → 4011.60] you can render it
[4011.60 → 4012.26] in the front end
[4012.26 → 4012.90] and I mean
[4012.90 → 4014.06] in situations like that
[4014.06 → 4014.66] you can just sort of
[4014.66 → 4015.92] update your app
[4015.92 → 4017.38] and not have to worry
[4017.38 → 4017.96] about the user
[4017.96 → 4018.92] reloading the page
[4018.92 → 4019.88] in many instances
[4019.88 → 4020.70] you can just ship them
[4020.70 → 4021.86] updates to the HTML
[4021.86 → 4022.30] or whatever
[4022.30 → 4023.18] and not interrupt
[4023.18 → 4024.02] their user experience
[4024.02 → 4025.76] and I think Node
[4025.76 → 4026.84] would work really, really well
[4026.84 → 4028.12] with the NGINX
[4028.12 → 4029.08] HTTP push module
[4029.08 → 4030.06] which is my favourite way
[4030.06 → 4030.88] to do comment right now
[4030.88 → 4032.02] and so I've been playing
[4032.02 → 4033.22] with those two in tandem
[4033.22 → 4035.42] the push module
[4035.42 → 4036.64] holds open
[4036.64 → 4037.86] long polling connections
[4037.86 → 4038.34] from the browser
[4038.34 → 4039.40] for you in NGINX
[4039.40 → 4040.36] so it's perfect
[4040.36 → 4041.24] at holding a lot of them
[4041.24 → 4042.48] open at the same time
[4042.48 → 4043.62] and then it lets you
[4043.62 → 4045.48] send a post request
[4045.48 → 4047.52] to a published URL
[4047.52 → 4048.60] that is secret
[4048.60 → 4049.26] and internal
[4049.26 → 4049.90] to your network
[4049.90 → 4051.20] and you give it
[4051.20 → 4051.76] a channel ID
[4051.76 → 4052.92] and the browser
[4052.92 → 4053.42] is listening with
[4053.42 → 4053.90] the channel ID
[4053.90 → 4055.58] and when the push module
[4055.58 → 4056.36] gets that post
[4056.36 → 4057.38] it'll give the data
[4057.38 → 4058.32] you post it to the browser
[4058.32 → 4058.92] so in this way
[4058.92 → 4059.44] you can do
[4059.44 → 4060.22] long polling
[4060.22 → 4061.20] persistent connections
[4061.20 → 4062.40] fake a socket connection
[4062.40 → 4062.94] in the browser
[4062.94 → 4064.86] and do it really easily
[4064.86 → 4065.86] without having to worry about
[4065.86 → 4066.84] alright I'm starting up
[4066.84 → 4067.72] an orbited daemon
[4067.72 → 4068.36] I'm keeping over
[4068.36 → 4069.18] X number of connections
[4069.18 → 4070.90] I need X number of RAM
[4070.90 → 4071.64] and that sort of thing
[4071.64 → 4072.38] you just let NGINX
[4072.38 → 4073.10] handle what it's good at
[4073.10 → 4073.66] which is scaling
[4073.66 → 4074.62] and then you handle
[4074.62 → 4075.14] what you're good at
[4075.14 → 4075.94] which is building your app
[4075.94 → 4076.86] and then when you want
[4076.86 → 4077.42] to talk to the browser
[4077.42 → 4078.30] you just post stuff
[4078.30 → 4079.60] so it's a pretty elegant way
[4079.60 → 4080.38] to do it and very simple
[4080.38 → 4081.88] and I think those two technologies
[4081.88 → 4082.80] go together pretty well
[4082.80 → 4083.94] before we move away
[4083.94 → 4084.48] from Node.js
[4084.48 → 4085.02] I have to mention
[4085.02 → 4085.56] is that I think
[4085.56 → 4086.26] it's been like
[4086.26 → 4088.04] five or six consecutive
[4088.04 → 4089.00] podcasts we've done
[4089.00 → 4090.96] where Node.js was mentioned
[4090.96 → 4091.78] is that a
[4091.78 → 4093.10] are we trying to
[4093.10 → 4094.14] make a record or something
[4094.14 → 4096.08] well how much
[4096.08 → 4097.08] is it just that cool
[4097.08 → 4099.16] they're not paying us
[4099.16 → 4099.44] anything
[4099.44 → 4100.20] but it's just funny
[4100.20 → 4101.38] that everybody we talk to
[4101.38 → 4101.70] they're like
[4101.70 → 4102.24] Node.js
[4102.24 → 4102.72] Node.js
[4102.72 → 4103.16] I love it
[4103.16 → 4104.72] this is the first episode
[4104.72 → 4105.64] that we haven't spelled it
[4105.64 → 4106.20] so if you want to go ahead
[4106.20 → 4107.04] and spell it
[4107.04 → 4108.28] N-O-D-J-S
[4108.28 → 4109.28] N-O-D-E
[4109.28 → 4110.20] the first three episodes
[4110.20 → 4111.24] Adam thought we were saying
[4111.24 → 4111.84] Node.js
[4111.84 → 4113.58] no I thought you were saying
[4113.58 → 4114.40] Node.js
[4114.40 → 4116.14] that's just my accent
[4116.14 → 4116.86] I apologize
[4116.86 → 4117.98] is it like no sequel
[4117.98 → 4119.56] exactly no sequel
[4119.56 → 4120.82] I think that's what Adam thought
[4120.82 → 4122.38] so one last item
[4122.38 → 4122.74] you know
[4122.74 → 4123.68] we've been working on
[4123.68 → 4124.56] a skunk works project
[4124.56 → 4125.46] here at the changelog
[4125.46 → 4126.04] for a while
[4126.04 → 4128.16] tail to changelog.com
[4128.16 → 4129.48] so when this audio comes out
[4129.48 → 4130.72] we'll take the wraps
[4130.72 → 4131.22] off of it
[4131.22 → 4131.96] we just wanted to get
[4131.96 → 4133.04] your reaction
[4133.04 → 4133.40] because you know
[4133.40 → 4133.96] you've seen it
[4133.96 → 4134.64] and you know
[4134.64 → 4135.68] if it's not favourable
[4135.68 → 4136.72] we'll just cut this segment
[4136.72 → 4138.36] oh no
[4138.36 → 4139.26] I think it's awesome
[4139.26 → 4140.06] it's not favourable
[4140.06 → 4141.78] it must just be favourable
[4141.78 → 4144.10] I think it's a great
[4144.10 → 4145.02] I think it's a great site
[4145.02 → 4146.48] everyone at GitHub loves it
[4146.48 → 4147.94] it's cool too
[4147.94 → 4149.06] because it looks very simple
[4149.06 → 4149.46] at first
[4149.46 → 4151.06] and then you hit the little gear icon
[4151.06 → 4152.06] or you hit the more button
[4152.06 → 4153.42] and you can kind of dig deeper
[4153.42 → 4155.44] so it has that fun
[4155.44 → 4155.96] sort of like
[4155.96 → 4157.80] exploring feeling to it
[4157.80 → 4158.66] where you can sort of like
[4158.66 → 4159.42] mess around
[4159.42 → 4160.44] and uncover new features
[4160.44 → 4161.30] which is always awesome
[4161.30 → 4161.94] in good software
[4161.94 → 4163.24] and I think it's cool
[4163.24 → 4163.72] it's a great way
[4163.72 → 4165.00] to look at everything
[4165.00 → 4166.02] I wish we had
[4166.02 → 4166.92] built that ourselves
[4166.92 → 4167.64] earlier on
[4167.64 → 4169.44] and I hope we can work
[4169.44 → 4169.82] with you guys
[4169.82 → 4170.60] to make it better
[4170.60 → 4171.08] in the future
[4171.08 → 4172.30] but you know
[4172.30 → 4172.70] I think
[4172.70 → 4173.72] I could see myself
[4173.72 → 4174.36] leaving it open
[4174.36 → 4175.40] and glancing at it
[4175.40 → 4176.20] whenever I'm a little bit bored
[4176.20 → 4177.36] just to see what's on the screen
[4177.36 → 4178.42] at the time
[4178.42 → 4179.88] I want to ask you about that
[4179.88 → 4181.36] I find a lot of
[4181.36 → 4182.88] nice projects to follow
[4182.88 → 4183.84] just by following
[4183.84 → 4184.58] what you're following
[4184.58 → 4185.50] it shows up in my
[4185.50 → 4186.54] public timeline
[4186.54 → 4188.32] since I follow you on GitHub
[4188.32 → 4189.16] and wanted to know
[4189.16 → 4190.32] how often
[4190.32 → 4192.10] do you discover new projects
[4192.10 → 4192.68] cool projects
[4192.68 → 4193.32] just by watching
[4193.32 → 4194.00] the public timeline
[4194.00 → 4195.46] and how much of it is
[4195.46 → 4196.12] just through
[4196.12 → 4197.46] word of mouth
[4197.46 → 4199.02] I don't check the timeline
[4199.02 → 4199.50] that often
[4199.50 → 4200.12] it used to have
[4200.12 → 4201.30] like a two-hour cache on it
[4201.30 → 4202.28] so it was usually pretty stale
[4202.28 → 4203.10] I think now it updates
[4203.10 → 4204.06] about every five minutes
[4204.06 → 4204.94] and then if you hit
[4204.94 → 4205.92] the RSS feed
[4205.92 → 4206.78] I think doesn't have
[4206.78 → 4208.12] a timed cache
[4208.12 → 4208.76] in that way
[4208.76 → 4211.00] so I mostly
[4211.00 → 4211.88] I mean I find stuff
[4211.88 → 4213.26] on just mostly
[4213.26 → 4214.52] people tweeting about stuff
[4214.52 → 4215.42] or I follow
[4215.42 → 4216.22] a bunch of other people
[4216.22 → 4216.98] I try and follow
[4216.98 → 4218.36] as many people as I can
[4218.36 → 4218.68] on GitHub
[4218.68 → 4219.68] anyone new I see
[4219.68 → 4220.30] I try and follow
[4220.30 → 4222.30] and you know
[4222.30 → 4222.90] I'm on the site
[4222.90 → 4223.38] all day
[4223.38 → 4223.90] every day
[4223.90 → 4225.92] for every reason
[4225.92 → 4226.48] either I'm doing
[4226.48 → 4226.96] open source
[4226.96 → 4227.62] or I'm working
[4227.62 → 4228.24] or I'm trying
[4228.24 → 4228.96] to debug something
[4228.96 → 4230.06] or I'm doing
[4230.06 → 4230.88] a support request
[4230.88 → 4232.16] so I mean
[4232.16 → 4232.74] a lot of that time
[4232.74 → 4233.32] if I happen to see
[4233.32 → 4233.74] something cool
[4233.74 → 4234.28] I'll just you know
[4234.28 → 4235.16] follow it for later
[4235.16 → 4237.34] or watch the project
[4237.34 → 4237.70] for later
[4237.70 → 4238.50] or follow the individual
[4238.50 → 4239.92] you know
[4239.92 → 4240.22] I went through
[4240.22 → 4240.90] a long period of time
[4240.90 → 4241.48] where I was just
[4241.48 → 4242.70] watching projects
[4242.70 → 4243.58] and not following people
[4243.58 → 4244.08] so I was following
[4244.08 → 4245.36] like nine people
[4245.36 → 4246.80] as of a couple of months ago
[4246.80 → 4247.48] or something like that
[4247.48 → 4248.14] and I realized
[4248.14 → 4249.16] that a lot of the value
[4249.16 → 4249.62] comes from
[4249.62 → 4250.46] letting other people
[4250.46 → 4251.10] do the work for you
[4251.10 → 4251.66] like you just said
[4251.66 → 4252.18] you let me do
[4252.18 → 4253.20] so I've definitely
[4253.20 → 4253.84] been trying to follow
[4253.84 → 4254.72] as many people as possible
[4254.72 → 4255.52] because that's where you see
[4255.52 → 4256.26] like a lot of the new
[4256.26 → 4257.74] weird interesting stuff
[4257.74 → 4261.62] well I know I speak for a win
[4261.62 → 4262.30] when I say thank you
[4262.30 → 4263.14] for coming on the podcast
[4263.14 → 4263.70] with us
[4263.70 → 4264.80] and certainly appreciate
[4264.80 → 4267.10] your awesome remarks
[4267.10 → 4267.58] about Tail
[4267.58 → 4268.68] we were super jazzed
[4268.68 → 4269.12] about it
[4269.12 → 4269.74] you know
[4269.74 → 4270.44] a big credit
[4270.44 → 4271.08] Izzy to win
[4271.08 → 4271.42] because
[4271.42 → 4272.66] you know
[4272.66 → 4273.68] he did a heck
[4273.68 → 4274.22] of a lot of work
[4274.22 → 4274.60] on that
[4274.60 → 4275.30] I did some
[4275.30 → 4276.40] lightweight UI work
[4276.40 → 4276.74] on it
[4276.74 → 4277.96] and it was
[4277.96 → 4279.22] definitely a labour
[4279.22 → 4279.96] of love for us
[4279.96 → 4280.48] and we're excited
[4280.48 → 4281.30] about what we
[4281.30 → 4282.48] are doing now
[4282.48 → 4282.84] with it
[4282.84 → 4283.54] and what we
[4283.54 → 4284.28] definitely have
[4284.28 → 4285.22] planned for the future
[4285.22 → 4285.46] with it
[4285.46 → 4285.80] so we
[4285.80 → 4286.62] would certainly
[4286.62 → 4287.46] encourage your
[4287.46 → 4288.88] participation in that
[4288.88 → 4289.62] and however that
[4289.62 → 4290.22] works out
[4290.22 → 4291.62] one last question
[4291.62 → 4292.28] I know this is
[4292.28 → 4293.20] totally off-topic
[4293.20 → 4293.92] but I've got to
[4293.92 → 4294.72] ask this question
[4294.72 → 4295.74] before we let you go
[4295.74 → 4297.38] the origin behind
[4297.38 → 4298.18] the October
[4298.18 → 4299.12] is
[4299.12 → 4299.46] well
[4299.46 → 4300.64] Tom was looking
[4300.64 → 4301.10] for like
[4301.10 → 4301.80] a mascot
[4301.80 → 4302.56] and you know
[4302.56 → 4302.82] in Git
[4302.82 → 4303.32] there's such a thing
[4303.32 → 4304.30] as an octopus merge
[4304.30 → 4306.94] so there's different
[4306.94 → 4307.50] merge strategies
[4307.50 → 4307.78] in Git
[4307.78 → 4308.16] if you do
[4308.16 → 4308.62] if you man
[4308.62 → 4309.08] Git merge
[4309.08 → 4309.50] you can see
[4309.50 → 4310.26] there's a dash S
[4310.26 → 4310.80] for a strategy
[4310.80 → 4311.34] and you can do
[4311.34 → 4312.78] a couple different ones
[4312.78 → 4313.12] and one of them
[4313.12 → 4313.92] is the octopus merge
[4313.92 → 4314.56] so it just seems
[4314.56 → 4315.10] sort of obvious
[4315.10 → 4315.52] to us
[4315.52 → 4316.42] that you know
[4316.42 → 4316.90] one of Git's
[4316.90 → 4317.94] cool esoteric features
[4317.94 → 4318.98] become the cute
[4318.98 → 4319.86] cuddly mascot
[4319.86 → 4320.60] that we used
[4320.60 → 4321.88] on our error pages
[4321.88 → 4322.90] so that is the
[4322.90 → 4323.64] Did you actually engage
[4323.64 → 4324.48] the artist
[4324.48 → 4324.96] that did that
[4324.96 → 4325.88] wasn't that from
[4325.88 → 4327.28] I thought it was from
[4327.28 → 4328.08] an artist
[4328.08 → 4328.88] that was found
[4328.88 → 4329.84] on iStock Photo
[4329.84 → 4331.16] and I can't recall
[4331.16 → 4332.08] the guy's name right now
[4332.08 → 4332.76] but I definitely
[4332.76 → 4333.38] bookmarked him
[4333.38 → 4333.90] in my Delicious
[4333.90 → 4334.48] at some point
[4334.48 → 4335.08] so if you follow me
[4335.08 → 4335.46] on Delicious
[4335.46 → 4336.84] dig through there
[4336.84 → 4337.54] you'll find it
[4337.54 → 4338.62] but wasn't
[4338.62 → 4339.48] wasn't that from
[4339.48 → 4340.12] iStock
[4340.12 → 4341.10] and there was
[4341.10 → 4342.42] an artist
[4342.42 → 4343.22] that lives in Japan
[4343.22 → 4344.02] who does some
[4344.02 → 4344.98] very cool
[4344.98 → 4345.72] unique art
[4345.72 → 4347.22] that October
[4347.22 → 4347.96] was one of the
[4347.96 → 4348.52] earlier versions
[4348.52 → 4349.56] of his art
[4349.56 → 4350.74] yeah his name
[4350.74 → 4351.42] is Simon Oxley
[4351.42 → 4352.12] and he actually
[4352.12 → 4353.22] did the Twitter bird
[4353.22 → 4353.68] and a lot of the
[4353.68 → 4354.16] Twitter stuff
[4354.16 → 4355.02] right yeah
[4355.02 → 4355.46] that's true
[4355.46 → 4357.20] and yeah
[4357.20 → 4357.58] we got it
[4357.58 → 4358.24] from iStock Photo
[4358.24 → 4358.66] originally
[4358.66 → 4359.26] Tom was looking
[4359.26 → 4359.72] for the mascot
[4359.72 → 4360.02] there
[4360.02 → 4360.44] and then we
[4360.44 → 4360.80] ended up
[4360.80 → 4361.30] buying it
[4361.30 → 4361.68] so we
[4361.68 → 4362.52] own it now
[4362.52 → 4363.06] exclusively
[4363.06 → 4364.06] but yeah
[4364.06 → 4364.52] that's where
[4364.52 → 4364.96] it came from
[4364.96 → 4365.56] we bought it
[4365.56 → 4366.00] just like they
[4366.00 → 4366.36] did with
[4366.36 → 4367.28] the Twitter bird
[4367.28 → 4368.76] as a license
[4368.76 → 4369.34] so for actually
[4369.34 → 4369.80] for a while
[4369.80 → 4370.26] people would say
[4370.26 → 4370.84] can we make
[4370.84 → 4372.90] an October t-shirt
[4372.90 → 4373.42] or can I put
[4373.42 → 4374.16] October on my
[4374.16 → 4374.56] whatever
[4374.56 → 4375.94] and we would have
[4375.94 → 4376.30] to say well
[4376.30 → 4376.80] yeah if you buy
[4376.80 → 4377.40] an iStock Photo
[4377.40 → 4378.04] license for it
[4378.04 → 4378.78] we can't
[4378.78 → 4379.42] re-license it
[4379.42 → 4380.26] and a lot of
[4380.26 → 4380.78] people did that
[4380.78 → 4381.52] but now
[4381.52 → 4382.28] we own the rights
[4382.28 → 4383.30] so we can control it
[4383.30 → 4384.44] okay you've opened
[4384.44 → 4385.26] another can worms
[4385.26 → 4385.56] for you
[4385.56 → 4386.26] let you go
[4386.26 → 4387.72] the 4Q t-shirts
[4387.72 → 4388.36] that were popular
[4388.36 → 4389.02] a couple of years ago
[4389.02 → 4389.50] at Rails Con
[4389.50 → 4389.70] oh yeah
[4389.70 → 4390.82] how'd that come about
[4390.82 → 4392.18] because Adam wears it
[4392.18 → 4393.24] like two days a week
[4393.24 → 4394.30] I do not
[4394.30 → 4396.20] you're always wearing
[4396.20 → 4396.60] that shirt
[4396.60 → 4397.00] every time we
[4397.00 → 4397.80] video conference
[4397.80 → 4399.02] no
[4399.02 → 4399.84] no
[4399.84 → 4401.86] I'm wearing it
[4401.86 → 4402.38] right now
[4402.38 → 4402.82] crap
[4402.82 → 4404.32] you're wearing it
[4404.32 → 4404.70] in your avatar
[4404.70 → 4405.14] aren't you
[4405.14 → 4405.88] yeah I am
[4405.88 → 4406.72] yeah that's my avatar
[4406.72 → 4408.12] I actually took that
[4408.12 → 4410.76] picture in an Apple Store
[4410.76 → 4411.76] and I just happened
[4411.76 → 4412.38] to be wearing my
[4412.38 → 4413.54] my 4Q shirt
[4413.54 → 4414.52] and it's
[4414.52 → 4415.08] it's one of the
[4415.08 → 4415.68] badass shirts
[4415.68 → 4416.74] I have in my closet
[4416.74 → 4417.36] and I got a limp
[4417.36 → 4417.66] you know
[4417.66 → 4419.06] it's simple as that
[4419.06 → 4419.96] absolutely
[4419.96 → 4421.18] it was
[4421.18 → 4422.22] it was early on
[4422.22 → 4422.54] when we were
[4422.54 → 4423.14] we were doing
[4423.14 → 4423.80] the uh
[4423.80 → 4424.68] the site
[4424.68 → 4425.64] it was one of those
[4425.64 → 4426.34] decisions where
[4426.34 → 4427.78] we had the fork button
[4427.78 → 4429.18] and it's different now
[4429.18 → 4429.80] Kyle made it
[4429.80 → 4430.82] amazingly beautiful
[4430.82 → 4431.82] but I mean
[4431.82 → 4432.28] I like the way
[4432.28 → 4433.10] I like the old buttons
[4433.10 → 4433.78] to the old pill buttons
[4433.78 → 4434.12] we had
[4434.12 → 4435.16] and what it had
[4435.16 → 4435.88] was a little
[4435.88 → 4436.34] uh
[4436.34 → 4437.72] silk icon on it
[4437.72 → 4438.36] of a fork
[4438.36 → 4439.40] and it was in red
[4439.40 → 4440.50] and the link
[4440.50 → 4441.20] itself was red
[4441.20 → 4442.66] and we talked about it
[4442.66 → 4443.30] we decided the link
[4443.30 → 4444.22] should just be a normal colour
[4444.22 → 4445.40] and the icon should be green
[4445.40 → 4446.90] because forking is a good thing
[4446.90 → 4447.24] on GitHub
[4447.24 → 4448.56] we're going to use the same word
[4448.56 → 4450.12] but it shouldn't be bad
[4450.12 → 4451.34] it shouldn't be like the uh
[4451.34 → 4453.18] the big Emacs fork
[4453.18 → 4454.14] between XEmacs
[4454.14 → 4455.34] and Emacs GNU
[4455.34 → 4456.18] and all that sort of thing
[4456.18 → 4456.96] um
[4456.96 → 4458.28] and so on of the ways
[4458.28 → 4459.28] we wanted to try and enforce
[4459.28 → 4459.92] this idea
[4459.92 → 4460.74] is
[4460.74 → 4462.24] with the 4Q shirt
[4462.24 → 4462.68] so
[4462.68 → 4463.80] I mean when you see that
[4463.80 → 4464.80] it looks like a phrase
[4464.80 → 4466.26] which is
[4466.26 → 4467.06] you know
[4467.06 → 4468.50] not very friendly
[4468.50 → 4469.94] um
[4469.94 → 4470.38] and so
[4470.38 → 4471.60] like saying 4Q to someone
[4471.60 → 4472.64] is sort of a censored version
[4472.64 → 4473.34] of saying something
[4473.34 → 4474.24] not very friendly to them
[4474.24 → 4475.52] but we wanted to take that phrase
[4475.52 → 4476.18] and say now
[4476.18 → 4476.56] you know
[4476.56 → 4477.40] now it is friendly
[4477.40 → 4478.90] now forking is a good thing
[4478.90 → 4479.88] so saying 4Q to someone
[4479.88 → 4480.64] is actually like
[4480.64 → 4482.02] in some ways a good thing
[4482.02 → 4482.66] it's saying like
[4482.66 → 4483.42] we are going to
[4483.42 → 4484.10] you know
[4484.10 → 4485.06] send a pull request
[4485.06 → 4485.50] basically
[4485.50 → 4486.50] like we were talking about earlier
[4486.50 → 4487.72] that's what we think 4Q means
[4487.72 → 4488.82] just like send me a pull request
[4488.82 → 4489.80] fork my project
[4489.80 → 4490.88] and then we'll work on it together
[4490.88 → 4491.90] and we'll figure it out
[4491.90 → 4492.84] instead of the old way
[4492.84 → 4493.86] where 4Q means like
[4493.86 → 4494.20] you know
[4494.20 → 4494.96] get the hell out of here
[4494.96 → 4495.58] don't talk to me
[4495.58 → 4496.84] so that was sort of the idea
[4496.84 → 4497.76] is we're going to take this phrase
[4497.76 → 4498.60] we're going to put it everywhere
[4498.60 → 4499.58] we're going to put on these t-shirts
[4499.58 → 4500.74] and we're going to make it a good thing
[4500.74 → 4502.40] and I don't know how well that works
[4502.40 → 4503.72] I get more comments on that shirt
[4503.72 → 4505.18] from any other piece of clothing I wear
[4505.18 → 4505.80] I know
[4505.80 → 4506.78] everywhere I go
[4506.78 → 4507.70] if I go somewhere
[4507.70 → 4508.42] if I'm like
[4508.42 → 4509.80] if I'm in line
[4509.80 → 4511.08] putting my name in
[4511.08 → 4511.90] to sit down for dinner
[4511.90 → 4512.14] or something
[4512.14 → 4512.50] they're like
[4512.50 → 4513.20] oh I like your shirt
[4513.20 → 4514.60] and I totally forget what I'm wearing
[4514.60 → 4515.66] and I look down
[4515.66 → 4516.04] and they're like
[4516.04 → 4516.50] and I'm like
[4516.50 → 4517.66] oh yeah it is a nice shirt
[4517.66 → 4518.28] and they look back at me
[4518.28 → 4519.56] and it's usually a chick
[4519.56 → 4521.20] it's usually a chick
[4521.20 → 4521.48] they're like
[4521.48 → 4522.26] yeah I like that shirt
[4522.26 → 4524.56] it's good
[4524.56 → 4524.78] yeah
[4524.78 → 4526.00] we want to make more 4Q shirts
[4526.00 → 4528.04] and finally October shirts this year
[4528.04 → 4529.74] because now we can sell October stuff
[4529.74 → 4531.32] so that should be pretty exciting
[4531.32 → 4532.52] I do have one thing to mention though
[4532.52 → 4533.78] before you guys go
[4533.78 → 4535.36] anyone listening to this right now
[4535.36 → 4536.66] as you guys should know
[4536.66 → 4537.56] you can go to
[4537.56 → 4538.26] GitHub.com
[4538.26 → 4539.04] slash explore
[4539.04 → 4541.30] and it will be syndicated
[4541.30 → 4542.30] it'll have changelog stuff
[4542.30 → 4543.50] you don't even need to go to changelog anymore
[4543.50 → 4545.00] awesome
[4545.84 → 4546.82] so yeah
[4546.82 → 4547.28] it'll have
[4547.28 → 4548.56] it'll have a bunch of
[4548.56 → 4549.42] featured articles
[4549.42 → 4550.90] that changelog is written about
[4550.90 → 4551.92] it'll have podcasts
[4551.92 → 4552.88] that the changelog has made
[4552.88 → 4554.36] and it'll also have other
[4554.36 → 4556.30] not changelog related stuff
[4556.30 → 4556.76] such as
[4556.76 → 4558.00] trending repositories
[4558.00 → 4558.58] and
[4558.58 → 4559.04] you know
[4559.04 → 4559.84] stuff to look out for
[4559.84 → 4560.92] stuff that's being forked
[4560.92 → 4561.94] and actually contributed to
[4561.94 → 4563.14] so GitHub.com
[4563.14 → 4563.68] slash explore
[4563.68 → 4564.28] is going to be
[4564.28 → 4565.96] you can add that to your bookmark
[4565.96 → 4566.70] right next to tail
[4566.70 → 4567.58] dot the changelog.com
[4567.58 → 4568.88] is two big new time wasters
[4568.88 → 4569.44] in your life
[4569.44 → 4570.16] absolutely
[4570.16 → 4571.42] be sure to make episode 9
[4571.42 → 4572.24] sticky at the top
[4572.24 → 4573.38] so that people know what's up
[4573.38 → 4574.12] awesome
[4574.12 → 4574.64] will do
[4574.64 → 4575.12] sure
[4575.12 → 4576.06] well Chris
[4576.06 → 4577.62] definitely thank you for
[4577.62 → 4579.26] sharing your good thoughts
[4579.26 → 4579.66] on tail
[4579.66 → 4580.32] we're excited about
[4580.32 → 4581.08] what's going on with that
[4581.08 → 4582.52] and definitely excited about
[4582.52 → 4583.62] having our content syndicated
[4583.62 → 4584.00] onto
[4584.00 → 4585.50] GitHub.com
[4585.50 → 4586.58] forward slash explore
[4586.58 → 4587.82] so excited about
[4587.82 → 4589.36] the kind of relationship
[4589.36 → 4590.06] we can forge together
[4590.06 → 4590.48] and where this
[4590.48 → 4591.44] can go for us
[4591.44 → 4591.72] but
[4591.72 → 4592.88] it's been awesome
[4592.88 → 4593.84] picking your brain
[4593.84 → 4594.70] about all the cool stuff
[4594.70 → 4595.22] you've been working on
[4595.22 → 4595.80] over the past
[4595.80 → 4596.48] three years
[4596.48 → 4597.02] two years
[4597.02 → 4597.78] whatever it was
[4597.78 → 4599.54] 30 I thought
[4599.54 → 4599.92] you said
[4599.92 → 4600.94] 30 yeah 30
[4600.94 → 4602.68] in internet years
[4602.68 → 4603.44] it's 30 years
[4603.44 → 4603.94] right
[4603.94 → 4605.26] but definitely
[4605.26 → 4606.20] thank you for coming on the show
[4606.20 → 4607.20] appreciate it
[4607.20 → 4607.72] alright thanks Chris
[4607.72 → 4608.16] thanks a lot guys
[4611.08 → 4615.26] thank you for listening
[4615.26 → 4616.00] to this edition
[4616.00 → 4617.04] of the changelog
[4617.04 → 4619.18] point your browser
[4619.18 → 4619.88] to tail
[4619.88 → 4621.10] dot the changelog
[4621.10 → 4621.70] dot com
[4621.70 → 4622.20] to find out
[4622.20 → 4622.82] what's going on
[4622.82 → 4623.54] right now
[4623.54 → 4624.82] in open source
[4624.82 → 4626.80] also be sure
[4626.80 → 4627.22] to head to
[4627.22 → 4628.18] GitHub.com
[4628.18 → 4628.80] forward slash
[4628.80 → 4629.28] explore
[4629.28 → 4630.02] to catch up on
[4630.02 → 4630.94] trending and feature
[4630.94 → 4631.50] repos
[4631.50 → 4632.08] as well as
[4632.08 → 4633.18] the latest episodes
[4633.18 → 4634.58] of the changelog
[4634.58 → 4639.34] safe in your arms
[4639.34 → 4641.48] as if the passion
[4641.48 → 4643.02] show
[4643.02 → 4644.58] was
[4644.58 → 4645.84] mine
[4645.84 → 4647.46] alone
[4647.46 → 4649.96] open
[4649.96 → 4653.12] open
[4653.12 → 4657.42] for us to try
[4657.42 → 4659.06] bring it back
[4659.06 → 4660.42] bring it back
[4660.42 → 4660.96] to
[4660.96 → 4662.92] open
[4662.92 → 4665.88] up
[4665.88 → 4667.44] octopi
[4667.44 → 4667.98] in
[4667.98 → 4669.90] there
[4669.90 → 4670.02] to
[4670.02 → 4670.48] bull
[4670.48 → 4676.42] back
[4676.42 → 4676.60] back
[4676.60 → 4677.84] in
[4677.84 → 4678.70] rumours
[4679.94 → 4688.18] in
[4688.18 → 4689.48] air
[4689.48 → 4690.24] monsieur
[4690.24 → 4691.26] terror
