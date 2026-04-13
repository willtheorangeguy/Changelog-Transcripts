[0.00 → 18.28] This is the Change Log, and I'm your host Adam Stachowiak.
[18.48 → 23.64] We're a member supported blog and podcast that covers what's fresh and new in open source.
[23.64 → 30.54] Tune in live every Tuesday at 3pm Pacific, 6pm Eastern at thechangelog.com slash live.
[30.98 → 36.48] And this is episode 0.8.7 recorded April 30th, 2013.
[37.16 → 41.82] We're joined today by Chad Whitaker, the creator of Get Tip, also known as Gi dip.
[42.36 → 46.88] If you found this show on iTunes, we're also on the web at thechangelog.com.
[47.12 → 50.40] And if you're on Twitter, follow the Changelog because that is us.
[50.90 → 51.44] Enjoy the show.
[53.64 → 59.24] Three, three, four songs in California.
[63.98 → 64.82] Welcome back, everybody.
[64.92 → 66.90] This is the Changelog.
[67.00 → 67.56] It is Thursday.
[67.64 → 68.38] No, it's not Thursday.
[68.46 → 68.84] It's Tuesday.
[68.94 → 71.28] I'm so used to saying it's Thursday, but it's not because it's Tuesday.
[72.02 → 76.10] We take this show live every Tuesday at 3pm Pacific, 6pm Eastern.
[76.60 → 78.16] Got an awesome show lined up today.
[78.16 → 82.76] If you have not heard, the podcast is back.
[82.76 → 84.92] This is the third one going out.
[85.02 → 90.06] If you're waiting for 0.8.6, it's coming soon.
[90.30 → 91.30] I'm sorry about that.
[91.38 → 93.38] It's just taking a little bit longer than normal.
[93.38 → 96.74] But we do have some fun guests with us.
[96.78 → 101.22] We've got my ever popular, always fresh, always new, Andrew Thorpe.
[102.12 → 102.92] How's it going, Adam?
[103.22 → 104.02] How is it going?
[104.22 → 105.40] And we've got Kenneth.
[105.66 → 106.42] Kenneth Wright's here.
[106.62 → 107.46] What's going on, Kenneth?
[107.84 → 108.38] Not a lot.
[108.42 → 108.76] How are you doing?
[109.90 → 111.52] I'm fantastic, man.
[111.64 → 113.38] I'm just – it's such a good day.
[113.98 → 114.80] Today is a good day.
[114.90 → 115.54] Such a good day.
[115.66 → 117.32] It's a little overcast here, unfortunately.
[117.94 → 118.56] Where is here?
[118.88 → 120.36] Because, I mean, you never know where you're at.
[120.36 → 121.48] In the hills in Virginia.
[121.66 → 124.44] Next week, if I'm on the show, I'll be in Amsterdam, though.
[124.60 → 125.18] It would be pretty cool.
[125.36 → 126.30] I'm going to try to do it.
[126.42 → 126.76] We'll see.
[127.76 → 129.40] We'll have to get you on the satellite for that one.
[129.82 → 130.18] Yeah.
[131.08 → 132.38] I'm not sure if it's going to hold up.
[132.58 → 133.80] The new rig you just had commissioned, right?
[134.22 → 134.52] Yeah.
[134.70 → 135.58] With all the T-shirt money.
[136.24 → 140.06] Well, what the thing is we were promoting – what is it?
[140.12 → 141.42] Open.nasa.gov.
[141.72 → 143.44] And so they gave us a satellite.
[143.60 → 144.20] It's pretty sweet.
[144.48 → 144.90] It's awesome.
[145.60 → 145.88] Yeah.
[145.88 → 146.56] It's just like that.
[146.56 → 151.12] And speaking of satellites, we've got the Group extraordinaire with us, Chad Whitaker.
[151.22 → 151.64] What's up, bud?
[151.80 → 152.58] How's it going, man?
[152.94 → 153.94] Thanks for having me on the show.
[154.58 → 157.70] So we're here today to talk about sustaining open source.
[157.92 → 159.00] Can you help us talk about that, Chad?
[159.26 → 160.28] Oh, my heavens.
[160.92 → 161.60] Not quite yet.
[161.70 → 165.82] Before we actually officially get started, maybe a quick introduction of who you are.
[166.06 → 166.50] Absolutely.
[167.10 → 167.40] All right.
[167.40 → 169.32] So Chad Whitaker is my name.
[170.30 → 171.22] Group is my game.
[172.10 → 179.18] Gidup.com is a website which primarily right now is being used by open source developers
[179.18 → 180.86] and the companies that love them.
[180.86 → 197.78] And it's a crowdfunding site where you can go, and you can set up $1 a week or $3 a week or $0.25 a week as a gift to someone whose work you love and admire and are inspired by.
[198.22 → 200.54] So it's ongoing, sustainable crowdfunding.
[200.54 → 214.36] Every week, every Thursday, we pull money into the system, we shuffle it around in the system, and we push money out into people's bank accounts so they can buy beer and pay a bill or something or whatever they want.
[214.86 → 216.40] It's gift money.
[216.64 → 217.10] That's what it is.
[217.54 → 217.78] Gift money.
[217.92 → 224.94] So before we go too deeply into the show, just for the listeners' sake who are out there thinking it's Git Tip, how do you say it?
[226.54 → 227.80] Well, it depends.
[227.80 → 230.90] I say Group, and that's a change.
[231.16 → 238.88] I used to say Git Tip, and a lot of people still do say Git Tip, and if you want to be old school, you can keep saying Git Tip.
[239.40 → 254.22] I say Group because the vision for this thing is to take it beyond the tech community and the open source world and to get musicians on there, to get bloggers on there, to get artists on there, people that have no clue what GitHub is, for example.
[254.82 → 255.28] Or Git.
[255.88 → 257.46] Or Git, right?
[258.26 → 262.88] And in my experience so far, folks like that, when they see the word, they say Group.
[263.12 → 265.24] That's the first thing that comes out of their mouth.
[265.64 → 271.98] So I'm sort of trying to skate ahead of the puck on that one and get myself used to saying Group because I think in the long run that's how it's going to end up.
[272.62 → 276.80] And do you say puck because you're a Penguins fan or what?
[277.60 → 278.12] Uh-oh.
[280.18 → 280.54] Yes.
[280.62 → 281.78] Let's go with yes on that one.
[281.78 → 282.54] All right.
[282.54 → 284.00] Do you miss Remix or what?
[285.38 → 285.74] Wow.
[286.42 → 286.78] Remix.
[287.42 → 288.04] Don't we all?
[288.32 → 288.60] I don't know.
[288.66 → 288.70] Yeah.
[289.66 → 290.66] Are you a big hockey fan?
[291.46 → 292.22] Absolutely, man.
[292.22 → 292.82] I'm from Pittsburgh.
[292.98 → 294.56] I love the Penguins, man.
[294.80 → 294.92] Yeah.
[294.92 → 295.44] A hundred percent.
[296.22 → 296.46] Right on.
[296.46 → 297.54] I'm not a big hockey fan.
[297.68 → 299.22] Well, did that get mentioned on the air yet?
[299.22 → 300.08] So I'm here in Pittsburgh.
[300.40 → 300.68] Yeah.
[300.84 → 301.72] We were talking about that.
[301.86 → 302.02] Yeah.
[302.98 → 309.68] We definitely aren't worried about saying where Chad is from because he's very personal in his Twitter profile.
[309.78 → 310.54] You know, yeah.
[311.30 → 311.52] Yeah.
[312.24 → 313.72] I mean, right.
[313.78 → 314.36] That's a thing.
[314.48 → 315.24] Can you explain?
[315.96 → 318.86] Well, so I was on this Reddit thread like a year ago.
[318.98 → 322.28] I had this thing where I was like, I'm going to friend everybody on Facebook.
[323.04 → 323.32] Right?
[323.32 → 328.70] I was like, I'm going to try and friend like all, you know, 750 billion people or whatever it was at the time.
[328.78 → 329.36] They're on Facebook.
[329.36 → 333.84] So I started this thing and, you know, some folks on Reddit got interested in it.
[334.10 → 335.72] And so we started trying to friend each other.
[336.40 → 343.40] Long story short, this one guy on the thread was like, I look forward to being friended by you, you know, in five years or whatever when you get to me.
[343.64 → 345.60] And I essentially doxed him, right?
[345.64 → 351.84] Like I took his handle on Reddit and found out, you know, like where he was graduating from high school in two weeks kind of thing, you know.
[352.30 → 353.38] And it kind of freaked me out.
[353.38 → 358.16] And that was sort of a wake-up call for me about digital privacy, right, and how there is none.
[358.16 → 363.58] And that was the point, you know, I ended up like backing away from doxing this kid and like deleted my comment or whatever.
[364.26 → 367.68] But I was like, well, you know, what have I got to lose?
[367.92 → 370.14] You can find it all out anyway, you know.
[370.34 → 372.46] Might as well just live out in the open.
[372.76 → 374.86] So, I mean, it's part of the whole openness shtick.
[375.08 → 377.56] But that was like, that was the event that precipitated it.
[378.06 → 380.46] It's like, I'm going to try this, see what happens.
[380.46 → 383.48] So now in your bio, you have your address and your phone number, right?
[383.68 → 384.04] Exactly.
[384.18 → 386.96] So my Twitter bio, what does it say?
[387.06 → 387.92] I'm going to go click to it.
[387.98 → 390.62] But yeah, it says, you know, yes, that's my address, my phone number.
[391.72 → 392.30] Does it really?
[392.58 → 393.52] Yeah, email address.
[394.10 → 395.42] Founder of getup.com.
[395.60 → 397.26] Call me at, I'm not going to say it.
[397.80 → 399.34] Email me at, I'm also not going to say it.
[399.34 → 401.52] Call me at 412-925-4220.
[401.84 → 403.70] Email me at chat at zadeweb.com.
[404.14 → 407.42] And when I say visit me at 716 Park Road, 1503.
[407.42 → 409.18] And so what does your wife say about this?
[409.92 → 414.46] Um, you know, it almost came up the other night.
[415.20 → 416.30] Does she not know?
[416.66 → 418.84] No, she kind of knows, I think.
[419.48 → 422.80] She's not a super online kind of, she uses Facebook some.
[423.22 → 425.38] She's got a Chromebook like two weeks ago.
[425.62 → 427.06] And so now she can actually get on the internet.
[427.22 → 430.34] Before that, she had this like old laptop that barely worked.
[431.98 → 432.24] Yeah.
[432.46 → 436.54] Yeah, she's less open about, you know, she's less gunshot about it than I am.
[436.54 → 439.18] But, I mean, that's, you know, she knows who she married.
[440.64 → 445.86] I'm not going to say one way or the other about it, but, and not to sound awful.
[446.00 → 451.92] But when all that stuff was going on with the Pylon stuff, and that was one of the major reasons why.
[452.16 → 457.44] Like, I started to almost feel like whatever semblance of digital privacy I can achieve,
[457.56 → 461.88] like this is the reason why I would want it is to prevent this from happening.
[461.88 → 466.46] And that stuff, I mean, shoot, we don't need to talk about that because I don't want to shed light on it.
[466.56 → 469.14] But that's something that, like, I don't know.
[469.20 → 472.44] In a world today, it's something that people have different opinions on.
[472.70 → 474.52] And, I mean, you're rightfully saying what you're talking about.
[474.52 → 476.56] Yeah, it's a brave new world, right?
[476.64 → 482.52] I mean, I sort of have this idea, like, you know, at some point there will be a scandal, right?
[482.52 → 488.14] I'll be, like, dragged into scandal and somebody will be, like, you know, from one side or another,
[488.22 → 489.96] it'll be like, Chad did this or Chad did this.
[490.58 → 495.58] And, I don't know, I sort of, I'm hoping by getting into the habit now of being open
[495.58 → 499.14] that it will make it easier when it's tough, you know?
[499.22 → 503.08] I mean, that's not true just in the case of scandal, but just, you know, in general.
[503.62 → 506.92] It's like, you know, you've got to start early when it doesn't hurt quite so much
[506.92 → 511.56] if you want to, you know, have big things that are also open.
[511.56 → 512.30] I don't know.
[513.92 → 515.44] Yeah, that's where it's coming from.
[516.32 → 519.00] So transparency is a huge part of what you're trying to do.
[519.16 → 519.24] Huge, man.
[519.24 → 521.92] Do you want to talk about open companies at all?
[522.04 → 522.66] Oh, goodness.
[523.04 → 524.22] Yeah, so open companies.
[524.32 → 526.66] So I'm trying to run Gi dip as openly as possible.
[526.88 → 531.46] Well, before you do that, let's talk about what Gi dip is just so everyone kind of knows
[531.46 → 533.98] before we kind of get into the crux of it.
[534.04 → 539.18] So why don't you give, like, a, you know, just the short and dirty of what Gi dip actually is.
[539.60 → 540.56] Man, it would be great.
[540.56 → 543.08] Okay, so it's nice to do this with some screenshots, right?
[543.12 → 548.20] Like, so if you go to gidip.com, and you look at the homepage, you're going to see, right
[548.20 → 553.86] now you see a list of the top receivers and the top givers and the top, and new participants,
[554.08 → 554.24] right?
[554.64 → 555.88] People that have just joined the site.
[555.88 → 560.90] And you click through to one of those, and you see a profile.
[561.08 → 562.96] So everybody, you get a profile page and get it, right?
[563.02 → 563.60] You sign it for Gi dip.
[563.64 → 564.14] You get a profile.
[564.74 → 568.26] And you have this opportunity to sort of make a statement.
[568.52 → 570.50] You know, in the database, it's called your statement.
[570.66 → 571.14] That's the column.
[571.80 → 572.34] Your statement.
[572.52 → 576.06] I am making the world better by dot, dot, dot, fill in the blank.
[576.06 → 576.50] Okay.
[577.54 → 583.64] So the idea is that we've got these, you know, these industries, open source software,
[583.94 → 588.20] you know, the software industry being almost chief among them, where you've got all these
[588.20 → 590.22] people giving their workaway for free, right?
[590.26 → 593.16] I mean, that's, you know, that's like the heart and soul of open source, right?
[593.20 → 594.10] Is you're doing it for the love.
[594.10 → 597.70] And so Gi dip is a way to give back.
[598.88 → 604.16] So you go to somebody's profile page, and you see, you know, I'm Mike Bayer and I, you
[604.16 → 608.34] know, write the SQL Alchemy library, which is a really popular SQL library for Python.
[609.42 → 611.26] And, you know, I do this other stuff too, right?
[611.34 → 617.92] Then you have an opportunity there to click a button, $1, $3, $6 up to $24 or 25 cents is
[617.92 → 618.26] the minimum.
[618.72 → 619.84] So it's a small gift.
[619.92 → 621.44] You know, you can't give them $100 a week.
[621.48 → 622.94] You can't give them $500 a week.
[622.94 → 624.82] You can give them up to $24 a week.
[624.90 → 625.66] You set up that gift.
[626.08 → 628.54] The idea is you're going to set up these gifts to a bunch of different people.
[629.76 → 633.50] And, you know, that's going to, that's going to tick over every week.
[633.60 → 636.12] And then you're both a giver and a receiver on the site, right?
[636.16 → 640.06] So as soon as you've signed in to give to somebody else, you're also open to receiving
[640.06 → 640.86] gifts on the site.
[641.34 → 644.90] You know, so the idea is kind of to build a social network, right?
[644.92 → 648.50] Where there's this, you know, you're, you're linking people according to the relationships
[648.50 → 652.24] they've already got, you know, but there's money on the line, right?
[652.24 → 657.82] Try to take it to the next level here and, you know, see if we can stir some stuff up
[657.82 → 658.12] with it.
[658.72 → 662.12] So that's the basic mechanism is you, you go to somebody's profile, you read their profile,
[662.24 → 664.80] you set up a gift to them and that gift is recurring.
[665.08 → 669.70] So it's every week, you know, right now we don't actually support one-time gifts at all.
[670.98 → 673.84] You know, it's a big feature request, and we're talking about it.
[674.06 → 675.02] We'll get to it someday.
[675.98 → 679.32] One-time gifts, you know, so I'll give you 20 bucks and then walk away, right?
[680.16 → 682.12] That's not, that's not the essence of get it.
[682.20 → 684.52] The essence of get it is weekly recurring gifts.
[684.52 → 686.40] Yeah, because you're trying, I mean, this is the play.
[686.80 → 691.32] Well, Kenneth, I know you mentioned talking about the, the openness of it, which is so
[691.32 → 692.92] unique to the way you're trying to build it.
[693.00 → 698.10] But the, the sustaining part is, you know, I know that there's a lot of talk out there
[698.10 → 701.40] about just, you know, I know you said, I didn't know you were taking this beyond open
[701.40 → 703.44] source either, but that was news to me.
[703.44 → 708.72] But I know that sustaining is a, is a big topic at least over the last couple of years
[708.72 → 713.82] really, but because people get burned out and just, there's lots of this, you know,
[713.84 → 714.58] a lot of conversation around.
[714.60 → 720.04] I mean, how long have we had, you know, donate buttons on open source projects, you know,
[720.12 → 726.56] PayPal buttons on open source projects, pledge, you know, we've had these mechanisms, you
[726.56 → 730.36] know, but what I'm seeing is that one-time gifts aren't enough, you know?
[730.36 → 730.80] Right.
[731.16 → 738.40] Because on the one hand, you know, my bills are recurring, you know, my bills aren't one-time,
[738.50 → 739.66] rent isn't a one-time thing.
[740.36 → 743.10] And then on the other hand, awesomeness isn't a one-time thing.
[743.22 → 747.34] As my friend Bruce Adams said, you know, like you don't stop being awesome tomorrow, you
[747.34 → 751.46] know, like Gi dip is built on this idea that you're really buying into someone's story,
[751.60 → 755.48] you know, and what, you know, like you're inspired by the work that they do, and you want
[755.48 → 756.34] to, you want to support them.
[756.40 → 758.62] These, do you guys know about the MacArthur Genius Grants?
[758.62 → 759.64] Mm-hmm.
[759.86 → 760.50] Is that on your radar?
[760.68 → 761.78] I'm not familiar with it, no.
[761.84 → 762.06] Yeah.
[762.20 → 762.58] So, okay.
[762.66 → 767.72] So the MacArthur Foundation is, you know, big nonprofit, you know, philanthropic foundation
[767.72 → 769.14] and they give out these grants.
[769.18 → 771.64] And I think, you know, it's like 30 or 40 people a year get these.
[771.82 → 774.98] It's a half a million dollars, no strings attached.
[775.58 → 775.86] Wow.
[775.96 → 777.80] And it pays out over like five years, right?
[777.80 → 782.80] So it's basically like a solid salary for five years, no strings attached, no questions
[782.80 → 783.16] asked.
[783.16 → 785.12] And they call it the Genius Grant, right?
[785.16 → 789.42] Because the idea is like, you're such a genius that whatever we told you to do with this
[789.42 → 792.62] money would just be dumber than what you would come up with, right?
[792.66 → 794.28] Because like you're the genius, you know?
[794.48 → 797.96] So we're just going to give you this money just to see what you're going to do with it,
[798.46 → 798.72] right?
[799.08 → 801.64] Because like you've already proven yourself that you've done all this awesome stuff in
[801.64 → 803.64] your field, and it's across all different fields, right?
[804.04 → 805.54] So you've done all this awesome stuff.
[805.62 → 808.98] We're going to give you this money just because we know you're going to do something awesome with
[808.98 → 809.10] it.
[809.10 → 813.26] And so that's one way to think about Gimmick, right, is its sort of crowdsourced genius
[813.26 → 813.70] grants.
[814.24 → 815.44] So very much sustainable.
[815.78 → 821.50] You know, we want people to be set free to pursue their passion, right?
[821.58 → 824.72] And work on what they love.
[825.76 → 832.40] And so why did you decide to build it, as Kenneth mentioned earlier, in this open way that you're
[832.40 → 832.78] doing it?
[833.00 → 833.46] Why did you decide to build it?
[833.46 → 834.56] Well, it's the only way to do it.
[834.56 → 839.12] I mean, first, just because that's, I mean, that's a part of my personality, right?
[839.24 → 842.16] I mean, hanging it all out there on Twitter like we were talking about.
[843.72 → 845.58] You know, I mean, that's the way I want to live.
[845.68 → 846.86] You know, it's the future I want to live in.
[846.90 → 851.22] I want to live in a future where we've got transparent, open institutions.
[851.40 → 853.72] That's one of the things I love about open source, you know?
[853.72 → 858.48] You know, the best of open source, you can go, and you just find out how it's made.
[858.68 → 863.78] Like, if I want to find out, you know, so I'm coming from the Python world.
[863.90 → 866.08] I'm starting to make connections in a lot of the communities.
[866.20 → 867.24] But Python's sort of my scene.
[867.44 → 871.44] Like, so if I want to find out how Python's made, I can just go on the issue tracker.
[871.60 → 873.16] You know, I can get involved in the mailing list.
[873.22 → 877.58] And that level of transparency and openness, I think it's just a perfect thing for humanity.
[877.82 → 880.62] You know, I think it's just something I want to see more of.
[880.62 → 886.68] I look at, you know, I look at all this stuff over the past few years with the financial industry, right?
[886.84 → 892.22] And, you know, people are crying out for openness and transparency in government and in corporations.
[892.98 → 897.22] And so this is sort of a, you know, Gi dip is me planting a seed and saying,
[897.36 → 902.96] can we get to a stage where our big entities, like our big organizations,
[903.16 → 906.46] and the ways that we organize ourselves are done in this transparent way?
[906.46 → 911.66] You know, it's trying to apply the insights of open source software, of the open source world,
[912.30 → 917.46] to wider domains, to paraphrase Eric Raymond at a certain point.
[917.86 → 918.54] So I don't know, man.
[918.60 → 921.30] I mean, it was the only way I could think about doing it, you know?
[922.98 → 924.12] I mean, why would you not?
[924.24 → 926.12] Why would you, you know, push it back?
[926.20 → 928.44] Like, why do something closed anymore?
[929.40 → 930.02] It's no fun.
[930.02 → 935.12] I sometimes guess the reason why people choose, well, I guess not sometimes,
[935.24 → 942.48] most people choose to do closed things is at some level in their humanity a fear of failure, right?
[942.48 → 947.68] You'd rather fail silently than, you know, in a room full of people.
[948.92 → 950.82] And so I think I definitely applaud you for…
[950.82 → 951.14] Have you failed silently?
[952.16 → 952.48] No.
[952.64 → 953.44] I mean, yeah, sure.
[953.68 → 955.26] Yeah, I've had some silent failures before.
[955.82 → 956.52] I'm cunning.
[957.00 → 957.82] You're cunning.
[957.82 → 958.50] Yeah, you know.
[958.88 → 959.86] I'm sneaky.
[960.38 → 960.74] Yeah.
[961.50 → 962.00] You're right.
[962.00 → 962.54] I mean, you're right.
[962.62 → 963.74] Like, you put your name out there.
[963.86 → 965.26] You put, you know, you put something out there.
[965.34 → 966.02] It's a risk, right?
[966.10 → 967.40] I'm kind of with Andrew on it, though.
[967.44 → 973.12] Like, I don't want to be private, but there's a level of me that I want to keep personal.
[973.44 → 977.12] That there's, that, like, I think of it like this.
[977.18 → 983.30] Like, I have lots of friends on the internet, just like most of the people on this show and those that are listening.
[983.30 → 987.10] You know, you got lots of internet friends and internet pals that are perfect friends.
[987.10 → 990.78] But, you know, those who are really close to you know who you are in your heart.
[990.78 → 994.76] It's a little different from your internet personality potentially, you know?
[994.98 → 999.06] So I think I kind of, I hold that a little sacred to my heart.
[999.30 → 999.54] Yeah.
[999.54 → 1001.64] And that's, we're just different, though.
[1001.94 → 1003.08] No, I mean, yes.
[1003.22 → 1005.94] A, people are different and people have different comfort levels.
[1006.10 → 1012.54] And the last thing I want to do is force anybody, you know, into, you know, a situation they're not interested in.
[1012.54 → 1017.80] You know, so another key part of the way I'm running this, it's voluntary, right?
[1017.82 → 1019.62] That's another part of open source culture.
[1019.78 → 1023.00] Like, you're not, you know, you're not forced to work on something you don't want to work on, right?
[1023.02 → 1023.72] It's open source.
[1023.84 → 1024.18] It's free.
[1024.34 → 1027.70] It's, you know, the personal autonomy is, is, is prized.
[1029.14 → 1029.50] Yeah.
[1029.56 → 1032.04] You know, so obviously there's stuff that I don't share.
[1032.04 → 1037.08] You know, mostly at my wife's behest.
[1039.12 → 1040.14] You know, yeah.
[1040.22 → 1041.72] So there's, there's some, right.
[1041.94 → 1043.02] I mean, all right.
[1043.04 → 1051.16] So to get back to maybe, maybe to get back to the open company idea, the way I define an open company is it shares as much as possible.
[1051.30 → 1053.14] It charges as little as possible.
[1053.14 → 1053.70] Number two.
[1053.76 → 1056.78] And number three, it doesn't pay its employees.
[1058.36 → 1059.92] So I mentioned that.
[1060.04 → 1060.80] That's a tough one, that last one.
[1060.88 → 1061.02] Yeah.
[1061.02 → 1061.90] You said that one a little quiet.
[1062.04 → 1062.26] That's a tough one too.
[1062.68 → 1063.56] Were you scared?
[1063.58 → 1065.50] It doesn't pay its employees.
[1066.04 → 1067.98] It doesn't pay its employees, but we're hiring.
[1068.40 → 1069.24] But we're hiring.
[1069.40 → 1069.66] Exactly.
[1070.62 → 1075.78] Well, I mentioned it because, you know, we share as much as possible, but we don't share everything, right?
[1075.82 → 1079.86] Like you don't have, I hope, the password to our database, right?
[1080.30 → 1080.54] Right.
[1080.78 → 1083.02] You know, you don't have our secret API keys, right?
[1083.36 → 1085.52] You know, so we share as much as possible, but not everything, right?
[1085.80 → 1090.28] But if you want to sit on, on like the board meetings, those are, those happen in public, right?
[1090.72 → 1091.26] Pretty much.
[1091.26 → 1091.48] Yeah.
[1091.48 → 1092.72] I mean, it's interesting.
[1092.84 → 1100.18] I had a company come to me today in private email, and they were like, Chad, can we do this, you know, promotional deal together?
[1100.26 → 1102.08] Can we do this cross-marketing promotional thing?
[1103.12 → 1108.28] You know, and by the way, we respect the open company thing, but we need, you know, we want to do this privately, right?
[1108.28 → 1110.80] We want to plan this privately, and then we'll come out with a bang together.
[1110.80 → 1113.16] And I said, sorry, you know, I can't do it.
[1113.34 → 1118.60] You know, I can maybe try and work with you, but anything I, anything I'm going to do for this has to be done public.
[1118.72 → 1127.20] I just feel like I don't have the right to make any decisions privately because the GitHub community has entrusted so much to me, you know?
[1127.20 → 1130.02] And I take that very seriously, or I try to.
[1130.66 → 1130.74] Yeah.
[1130.74 → 1131.36] So it's interesting.
[1131.36 → 1139.44] I think the way that you have it on your frequently asked questions page is that you and only one other person have access to the sensitive data.
[1139.44 → 1147.80] So if, and I think that makes sense, obviously you don't want to make, you can't make other people's information public when they've, you know, when it's sensitive for them.
[1147.80 → 1150.62] Cause like you said, you can't make the decision what other people want to share.
[1150.80 → 1159.12] So, so if the company were to come to you and say, you know, we want to work with you, but we have sensitive data that like we want to give you access to, but you can't share it.
[1159.14 → 1161.84] I mean, you have to take that into consideration, right?
[1161.92 → 1169.42] So, um, so would you, would you tend to just like, I, I see you, you know, you tweeted about it a little bit and you kind of, kind of turn the offer down.
[1169.44 → 1181.82] But if it was something like that, where it was more just, Hey, like we, you can't share our internals, like the, the, the plan of what we do together can be public, but you know what, what we share with you privately, you can't share.
[1181.92 → 1182.90] And you're okay with that.
[1183.16 → 1183.32] Yeah.
[1183.42 → 1188.76] So that wasn't the case with the company I just mentioned, but we, you know, let me, let me bring out on the show right now, balanced payments.
[1189.22 → 1190.70] Are you guys familiar with balanced?
[1191.38 → 1192.76] Just from you tweeting about it all day.
[1192.76 → 1194.02] Because you've been pretty excited about it.
[1194.02 → 1195.14] Oh, especially today, man.
[1195.18 → 1196.62] I love the way this lined up.
[1196.62 → 1200.82] So balanced payments is, is the payment provider underlying get it.
[1201.58 → 1203.36] And they're a really close partner of mine.
[1203.58 → 1212.36] Uh, I went through two other payment providers in about a month, uh, at when get it first started and was kind of left high and dry.
[1212.36 → 1215.92] So I was with one that got acquired by Groupon, and they disappeared off the face of the earth.
[1216.02 → 1218.18] Then I went to Stripe, which is gorgeous, right?
[1218.18 → 1225.48] I mean, Stripe's top-notch product, but I was violating their terms of service, and they're not really designed for marketplaces.
[1225.48 → 1235.14] I mean, they've, they're sort of bolting on some marketplace features, but you know, the get it is weird enough that we didn't fit within the feature set that they had available.
[1235.36 → 1236.92] So they asked me to leave politely.
[1237.24 → 1238.38] I'm very professional about it.
[1238.70 → 1241.46] Uh, you know, so a month into get it, you know, it's going great guns.
[1241.58 → 1246.96] We're getting, you know, some hacker news traction and all this stuff and some growth, you know, first thing in a decade that I've tried, it's growing.
[1247.08 → 1250.52] All of a sudden, you know, the bottom falls out again, two payment providers are gone.
[1250.52 → 1265.64] And balance payments comes along and, you know, is it an interesting point in their own development where they were, you know, they were pretty hungry, and they came along, and they said, Chad, how about we submit a pull request to your repo to integrate with our service?
[1266.42 → 1266.86] Right.
[1267.28 → 1270.92] So this was a yeah, I said, thank you.
[1270.98 → 1271.62] Yes, please.
[1271.74 → 1271.94] Right.
[1271.94 → 1290.10] Uh, you know, so they showed up and they, uh, they did, man, they, they submitted this pull request to integrate with their service, you know, and, you know, the next week we were running on balance, and we did the, the, you know, the PCI-compliant transfer from Stripe over to balanced, and we're off and running, and I've never looked back, you know, so now I have a really close partnership with those, those folks.
[1290.10 → 1293.36] And, uh, it's been great.
[1293.44 → 1302.50] So I mentioned in this context because last November, I don't know if it was on your guys' radar, but we had this bout of fraud.
[1303.26 → 1310.82] Uh, these folks showed up on Kiddie, and they plugged in stolen credit cards and started dumping stolen money into Kiddie, which was interesting.
[1310.82 → 1322.94] Um, but that was, that was sort of, it was a bit of a test of our relationship, uh, balanced and I, you know, because fraud, anti-fraud, uh, is very, very closed, you know, as a rule.
[1323.16 → 1329.50] Traditionally, uh, you know, any, any information you leak is aiding, you know, the enemy, right?
[1329.54 → 1334.30] The fraudsters and giving them, uh, uh, you know, a potential upper hand in the constant battle.
[1334.96 → 1340.68] So that was something we had to work out together, you know, and I ended up on a phone call with, uh, you know, their risk officer and their lawyer.
[1340.82 → 1344.34] Uh, you know, who had, who had met before that, you know, we were on friendly terms.
[1344.38 → 1347.12] So we got into this call, and it was, you know, it was, it was a little bit tense.
[1347.12 → 1351.00] It was like, so I'm trying because I'm trying to do this openly.
[1351.00 → 1351.30] Right.
[1351.32 → 1357.52] So I was dealing with this fraud incident very openly, and I was blogging about it, and I was tweeting about it.
[1357.52 → 1367.72] And I put out a whole page on our website, on the Kiddie website, detailing who I was flagging as fraudulent, you know, and where the who the money was coming from and going to, right?
[1367.72 → 1369.00] Very detailed information.
[1369.32 → 1370.34] Wasn't hiding anything.
[1370.82 → 1373.88] So we had this call that was like, all right, so where's the boundary line?
[1374.02 → 1383.08] You know, like you guys have to let me know when I crossed that line of your comfort, you know, when, when you feel, you know, because we've, we've got to have that boundary established, right.
[1383.08 → 1391.30] Where you feel comfortable, uh, you know, and, and I'm able to, you know, to do what I need to do in terms of openness, and we work through it, you know, but, but you're right, man.
[1391.30 → 1397.68] When, when another company, uh, has needs like that, where they're like, you know, we've got a, you know, we've got our own policies in place, you know, obviously.
[1397.68 → 1397.94] Yeah.
[1397.98 → 1398.80] I have to respect that.
[1400.08 → 1400.36] Yeah.
[1400.36 → 1412.04] So I want to circle back real quick when stack was talking about, um, you know, the I think a lot of people go closed because a fear of failure, um, you know, that, that may be, or may not be, I'm not sure.
[1412.04 → 1414.58] But I think that we kind of hit on it a little bit.
[1414.64 → 1423.56] I want to kind of go into it a little deeper, but, uh, the, the beauty of open source, um, and not just, and not necessarily open company.
[1423.56 → 1424.80] Because I think there's a lot more.
[1425.14 → 1434.70] I think we can get into a lot more to that, but the beauty of open source and how we're trying to hit on this right now is if you fail or yeah, there, there always is a there always is failure.
[1434.70 → 1438.24] It's always an option, whether you're an open source project, a closed project, it doesn't matter.
[1438.30 → 1449.88] But the beauty is like, if you can get over your own personal fears, and you can make your code available to the public, the majority of this community wants to help and does not want you to fail.
[1449.88 → 1455.08] So if there's an idea and people can get behind it, then they want to help move that forward.
[1455.22 → 1458.94] And have you, I mean, so obviously get up is, you know, an open source project.
[1458.94 → 1466.78] So have you, have you experienced that firsthand with, with people more encouraged to help rather than to watch it fail publicly?
[1467.14 → 1467.62] Oh yeah.
[1467.82 → 1472.80] I mean, you know, as I indicated a little bit ago, I mean, you know, this is my first rodeo.
[1472.86 → 1478.66] I've been trying for over a decade, uh, to get something off the ground and doing different open source projects and different business ideas.
[1478.66 → 1484.60] You know, and this is the first one that's really gotten any traction, you know, which is super awesome.
[1485.00 → 1486.42] And it's, it's great.
[1486.50 → 1490.10] You know, it's, it, that's, that's what, that's what gets me up in the morning.
[1490.18 → 1495.10] You're like, I, I lie in bed in the morning, and then I'm like, oh crap, what are they saying on Twitter?
[1495.28 → 1497.12] You know, like, or, oh, that's right.
[1497.14 → 1502.42] There was that person I wanted to respond to, or there's that pull request I needed to get to, you know, that's, that's very motivating for me.
[1502.42 → 1504.80] The input of the whole community around it.
[1505.82 → 1506.38] You know, I don't know.
[1506.38 → 1511.32] Maybe I'm, maybe I'm, maybe after a decade I'm comfortable enough with failure or something.
[1511.56 → 1512.86] Can we pause there for a second then?
[1512.92 → 1516.74] So you, so this is becoming successful or successful.
[1516.86 → 1523.92] And then, and I'm trying to figure out what, uh, maybe exactly what is your commercial play?
[1524.32 → 1530.06] You know, not so much like you getting rich, but at least how do you, how do you make money?
[1530.06 → 1530.88] How much money do you make?
[1531.08 → 1532.18] You know, how much money do you make?
[1532.18 → 1535.42] What's the what are some of the metrics there since you're so open?
[1535.64 → 1536.92] How much money do I make?
[1537.04 → 1544.54] Well, on Gi dip, I think I'm making, I think I made $266 last week and I gave away 88.
[1545.90 → 1549.08] You know, so I, you know, so what's the next 180 there?
[1549.08 → 1554.82] Um, so I'm making, I'm making $150 to $200 a week on Gi dip right now.
[1555.46 → 1558.96] So call it, you know, six to 800 bucks a month on Gi dip.
[1560.96 → 1566.22] Um, and long, do you want, where do you want to go?
[1566.34 → 1566.64] Do you want to?
[1566.70 → 1568.04] Well, you're still company itself.
[1568.14 → 1572.80] Like how does, you said you, you don't have any, I mean, I got to imagine you have costs and stuff like that.
[1572.80 → 1574.20] I'm sure those are being met, but.
[1574.26 → 1574.52] Yes.
[1574.52 → 1575.70] Do you keep money in the bank?
[1575.80 → 1576.70] Are you a corporation?
[1576.84 → 1577.10] LLC?
[1577.66 → 1578.06] Absolutely.
[1578.22 → 1579.22] So there's Gi dip LLC.
[1580.24 → 1584.12] Gi dip LLC is a legal entity that's owning all this, right?
[1584.72 → 1590.72] And it has a bank account and we charge.
[1590.82 → 1597.92] So point two of the open company definition is charge as little as possible, but you still charge something, right?
[1598.60 → 1599.34] That's the idea.
[1599.34 → 1604.04] So when you move money into Gi dip or you pull money out of Gi dip, I do charge a fee.
[1604.94 → 1608.92] Gi dip charges a fee and that fee is designed to be as low as possible.
[1609.08 → 1617.50] It's designed to barely cover, you know, it's, you know, it's designed to cover your operating expenses and not wages and profit essentially.
[1617.88 → 1618.08] Okay.
[1618.26 → 1627.16] So that's designed to cover credit card fees and hosting costs and other services as well as some cash reserves, right?
[1627.16 → 1631.90] So there is a fee involved, but it's designed to be as little as possible.
[1632.72 → 1634.72] So if you put a dollar in, how much is the fee?
[1634.76 → 1635.82] Is it like five cents?
[1636.62 → 1637.30] Well, okay.
[1637.34 → 1647.16] So if you put a dollar in, then I'm going to charge you $10, and you're going to pay 68 cents in fee and $9 and 32 cents is going to be in your account.
[1647.16 → 1649.68] And that's going to tick down over nine weeks.
[1650.58 → 1655.62] You know, your dollar gift is going to go, you know, nine times till you're down to 32 cents.
[1655.76 → 1658.02] And then that, at that point, it's going to charge you another $10.
[1658.72 → 1659.92] So we charge you a minimum.
[1660.12 → 1662.74] The least we charge is $10 to minimize credit card fees.
[1663.78 → 1664.64] Does that make sense?
[1665.40 → 1665.52] Right.
[1665.62 → 1665.76] Yeah.
[1665.76 → 1668.42] So, I mean, it's, you know, I mean, it's, it's a business, right?
[1668.44 → 1681.88] It's a business, you know, with a plan and it, you know, it's got fees in there to cover the cost because, you know, I don't, I mean, the last thing that Gi dip is about is desperation, you know?
[1682.14 → 1689.10] And if I had to come to you all and be like, look, guys, I need to pay my hosting bill and I just need like a hundred bucks, please.
[1689.44 → 1691.44] Could I just have like a hundred bucks to pay my hosting bill?
[1691.82 → 1694.14] Like that's not, you know, how does that help anybody?
[1694.24 → 1695.16] That's not what it's about, right?
[1695.16 → 1699.66] Like, so we've got the fees in place to cover the things that we ourselves are charged for.
[1701.30 → 1704.52] And then beyond that, Gi dip is funded on Gi dip.
[1704.60 → 1710.54] So I personally am on the site and the understanding is that anybody who's going to be working on the site is also going to be on the site.
[1711.34 → 1713.94] I'm not, that's, you know, point three, don't pay your employees, you know?
[1713.98 → 1716.74] So I'm not, you know, I don't have any salaries to offer you, you know?
[1717.38 → 1719.04] I met with some people the other day.
[1719.98 → 1720.86] It was interesting.
[1721.02 → 1724.06] It was really, it was another, even more fraught meeting.
[1724.06 → 1733.60] These, a couple really top-notch marketing folks actually who, you know, I'd met in person here in Pittsburgh.
[1733.92 → 1736.48] They were interested in Gi dip and interested in getting involved.
[1736.62 → 1741.36] I'm trying to figure out how to get marketers in, into the picture, you know, because we've got it.
[1741.36 → 1745.34] We've got, we've got collaborative development figured out for developers, right?
[1746.34 → 1750.10] So how do we bring, you know, how do we, how do we take that beyond just developers?
[1751.60 → 1756.04] And, you know, we reach this point where they're like, well, so like, what are you offering me?
[1756.08 → 1757.84] You know, like you're saying you don't have equity.
[1757.96 → 1759.10] You're saying you don't have salaries.
[1759.10 → 1765.10] And it reached a point where it's like, look, bring your own carrot, BYOC, you know, I have no carrot for you.
[1765.48 → 1771.80] You know, like you're, if you're going to be working on Gi dip, it's going to be because you want to be here, you know, because that's why I'm here, you know?
[1772.28 → 1779.22] And that's, that's the open source way, you know, like, you know, at the best of it, it's, you know, you do the changelog because you want to do the changelog, you know?
[1779.22 → 1781.96] So let me, yeah, no, definitely.
[1782.12 → 1787.10] We, I think we, we struggled over, or I struggled over the term labour of love.
[1787.16 → 1791.26] I was trying to remember what it was in our first episode back, but that's the truth.
[1791.26 → 1794.44] Like, you know, we can kind of empathize with you on that.
[1794.50 → 1797.06] Like we do this because this is something we love to do.
[1797.12 → 1802.72] Not like what I said at the time, and it still rings true, not because, you know, we're going to become millionaires off the changelog.
[1802.72 → 1808.14] This is something that we, what we want to do is we want to shine a light on people like you that are doing neat things like this.
[1808.14 → 1814.00] And so you said that, you know, you're not going to pay salaries.
[1814.00 → 1820.42] And then you kind of said, talked about the fees, but so those fees, they obviously, they're not going to scale well.
[1820.42 → 1834.04] Like, like the more traffic that, you know, you get not traffic in terms of like visitors, but the more, you know, money that goes through the system, the more money that's going to get charged and essentially deposited in the LLC's bank account.
[1834.04 → 1837.20] So you, you might not be claiming a profit.
[1837.20 → 1841.42] So what do you do once you start to actually have more money than your expenses?
[1841.86 → 1842.02] Yeah.
[1842.20 → 1843.06] So we have a ticket.
[1843.34 → 1845.42] I mean, well, you know, we'll keep track of it.
[1845.52 → 1852.60] I actually need to do a better job of, of making that information actually public because it's not fully public right now.
[1852.60 → 1858.68] My, my, what's the word, you know, the people I look up to here are watsi.org.
[1858.74 → 1859.76] Are you guys familiar with Watusi?
[1860.84 → 1861.12] No.
[1861.46 → 1863.50] Watusi, W-A-T-S-I.org.
[1863.50 → 1866.78] Uh, they are crowdsourced.
[1867.28 → 1869.08] You guys will actually really like this.
[1869.14 → 1872.70] They, they crowdsource third world, uh, medical treatments.
[1874.16 → 1874.64] Right.
[1874.76 → 1880.06] So you can go, and you can see stories of, you know, kids all over the world, you know,
[1880.06 → 1885.20] and 500 bucks would make their, you know, turn their life from really sucky to awesome.
[1885.54 → 1885.56] Right.
[1885.58 → 1887.08] Oh, and it's for specific children.
[1887.60 → 1888.10] Exactly.
[1888.10 → 1888.46] Yeah.
[1889.66 → 1898.92] So watsi.org, uh, you know, is, is another crowdfunding platform where they do this stuff, and they are really awesome in regard to open finances.
[1899.36 → 1899.62] Okay.
[1900.58 → 1903.42] Um, they publish, I got to dig it up for you.
[1903.50 → 1904.72] I tweeted about it a while ago.
[1904.72 → 1909.82] If I can't, I'm going to get distracted if I go digging for it now, but I'll get it out of the show.
[1909.82 → 1916.90] So they, uh, they publish a Google doc, which has all their finances unaudited.
[1917.04 → 1922.74] So they're basically crowdsourcing the auditing of their finances, you know, and they get people coming back.
[1922.84 → 1926.78] They're a nonprofit, and they get people coming back to them being like, you know, is this line item right?
[1927.02 → 1928.34] You know, and they're like, no, it's not.
[1928.40 → 1929.90] You know, so talk about failing publicly.
[1929.90 → 1930.26] Right.
[1930.62 → 1933.18] And, uh, I mean, they're doing this right.
[1933.24 → 1936.80] So I sort of look up to them as, as an exemplar of open finances.
[1937.14 → 1938.48] Um, there are some others, right.
[1938.48 → 1941.34] Um, patio 11 does this too, right?
[1941.42 → 1943.04] He publishes a lot of financial data.
[1943.72 → 1944.36] Uh, yeah.
[1944.38 → 1947.82] So there's, there's definitely people that, that, that I have stuff to learn from there.
[1948.50 → 1952.22] Um, I'm expecting get up eventually to be a nonprofit.
[1952.42 → 1954.24] I haven't started filing that paperwork yet.
[1954.28 → 1955.96] If anybody wants to work on that, let me know.
[1956.52 → 1964.80] Uh, because somebody raised the point, you know, even though, you know, even though I'm not making a lot of money off of it, there is still obviously value in the company.
[1964.80 → 1969.42] And, uh, as long as it's a for-profit company, there's always a sort of shadow hanging over.
[1969.58 → 1971.52] Like, well, what if Chad turned around and sold the company?
[1971.66 → 1971.96] Right.
[1972.40 → 1975.64] And, uh, you know, sold out and it, and it went down the tubes.
[1975.96 → 1982.62] So we do need to, we do need to address some of those things just to shore it up and, uh, you know, make sure, make sure it's protected.
[1983.46 → 1984.98] You know, to reduce your bus factor.
[1985.70 → 1985.98] Yeah.
[1986.16 → 1986.38] Yeah.
[1986.38 → 1986.78] Yes.
[1986.98 → 1987.26] Yes.
[1987.30 → 1987.94] Reduce even further.
[1988.24 → 1989.80] Is that the kind of thing you were talking about, Andrew?
[1990.46 → 1991.40] Am I answering your question?
[1991.74 → 1991.88] Yeah.
[1991.92 → 1992.86] I was going to actually clarify that.
[1992.90 → 2001.26] I think, Andrew, were you talking about because it's an LLC and at the end of the year that money falls back on, because I'm assuming you're a single member LLC?
[2001.74 → 2002.12] Correct.
[2002.12 → 2011.14] Okay, so that money at the end of the year, when 2013 closes, that's going to fall into your personal, uh, you know, your personal tax.
[2011.86 → 2022.36] And then, so at some point, you're going to have to pull whatever profit, in air quotes, profit is out there in Group, whether it's, you know, realized or not, and you're going to pay tax on it.
[2022.72 → 2028.08] Well, and I'm not, I'm just saying there's, there are lots of different ways you can kind of, you know, shuffle it around and do different things.
[2028.08 → 2038.10] But, but I guess my point is, so there will come a point in time where it's not about like, okay, let's say, yes, let's say this year, the end of the year comes, and you realize, hey, like we made a profit.
[2038.10 → 2039.62] So now you have to figure out what to do with that money.
[2039.66 → 2040.10] That's fine.
[2040.22 → 2042.00] That's, that's scenario A.
[2042.10 → 2047.16] But then you can, you can look at it and say, okay, like now I have, I have actual data I can project.
[2047.22 → 2050.26] And next year, my operating costs, I can be more accurate with it.
[2050.30 → 2054.30] So how do you then prevent that from happening again?
[2054.30 → 2062.80] Like, are you going to look in the interest of, or look at, you know, maybe reducing your fees or cutting your, cutting your fees off at a certain point or, you know, things like that.
[2062.86 → 2064.62] Like, what's the big goal for that?
[2064.66 → 2064.78] Yeah.
[2064.80 → 2066.58] I mean, the goal is to charge as little as possible.
[2066.66 → 2067.46] That's point two, right?
[2067.54 → 2068.24] So yeah.
[2068.28 → 2071.24] So we'll review periodically, and we'll say, well, our fees are too high.
[2071.30 → 2072.80] I mean, cause honestly, they are a little high right now.
[2072.84 → 2074.98] It's 3.9% plus 30 cents.
[2074.98 → 2078.78] You know, I just picked that out of the air to get something going.
[2079.76 → 2080.14] Excuse me.
[2080.14 → 2086.64] The balance charges me 2.9% plus 25 cents for credit card transactions, which is pretty standard pricing.
[2086.78 → 2088.78] And it's what, I believe it's what Stripe does as well.
[2089.18 → 2097.80] Uh, you know, for sort of the first tier stuff, you know, and once we get enough volume, and we can do some volume discounts and whatever, uh, you know, we're going to pass that along.
[2097.84 → 2098.14] Absolutely.
[2098.94 → 2100.06] Uh, yeah.
[2100.10 → 2101.28] So we'll, we'll bring those down.
[2101.42 → 2110.06] It's not, you know, eventually, you know, the awesome thing would be to fully automate that, you know, so we can, uh, yeah, we can compute each week.
[2110.14 → 2112.76] What the fee is going to be that week based on projections.
[2113.16 → 2117.00] Now, I feel like the goal of an open company should be to have probably as few assets as possible.
[2117.24 → 2117.58] Right.
[2118.38 → 2118.72] Yeah.
[2118.80 → 2126.88] I mean, uh, it's, it's weird stuff, you know, like I just sponsored a conference here in Pittsburgh, the Steel City Ruby conference.
[2126.88 → 2132.16] I was at an event last night, you know, I was talking to some folks and, you know, it was like 300 bucks to sponsor this conference.
[2133.06 → 2138.40] And, you know, they're good friends of mine, and they've done a lot to, to help me, uh, you know, promote get appear on Pittsburgh.
[2138.72 → 2142.56] So I really wanted to be part of this and was talking to this friend of mine.
[2142.60 → 2143.66] I was like, yeah, I want to sponsor this.
[2143.74 → 2150.24] So I just paid for that out of personal, you know, uh, it's it because I don't, you know, I don't feel right putting that through get it.
[2150.24 → 2155.46] But, but I mean, this is, this is gray area stuff that that's going to need to get worked out.
[2156.14 → 2168.66] Uh, it's, I don't feel like it's my bottleneck right now, you know, and sort of, but at the same time, like I don't want to be, you know, I'm not looking to set get it up to, uh, you know, for a surprise.
[2168.66 → 2169.02] Right.
[2169.30 → 2170.42] I mean, that's the risk, right.
[2170.44 → 2172.34] Is it like, I mean, here's a big one for you.
[2172.34 → 2178.64] Even, you know, if you want to talk about risks and legality is like the idea of an open company, not paying its employees.
[2178.64 → 2180.48] Well, how about minimum wage tax, right?
[2180.54 → 2181.56] Or how about minimum wages?
[2181.66 → 2182.08] Excuse me.
[2182.12 → 2182.30] Right.
[2182.72 → 2192.98] Um, you know, how about, I mean, the tax issue is huge, you know, you're getting money for, you know, you're getting money through this, you know, when you've got hundreds of people, and you don't know who they are.
[2193.20 → 2193.60] Yeah.
[2193.76 → 2196.14] I mean, how do you decide what's a gift and what's not?
[2196.14 → 2204.76] You know, so I actually did talk to a lawyer about this, and she gave me this awesome two pages footnoted memorandum, you know, digging back into the case history on this.
[2205.22 → 2208.50] And it's really squirrel, you know, it's like the way, the way gift tax.
[2208.50 → 2212.92] Works in the U S you know, it's, it's just not clear-cut at all.
[2212.92 → 2213.18] Right.
[2213.22 → 2221.92] So, I mean, in some ways, Kickstarter is obviously the, you know, the gorilla that's sort of raising the trail here.
[2222.10 → 2224.80] Uh, you know, so they're going through a lot of this right now.
[2224.80 → 2225.04] Right.
[2225.04 → 2227.98] And there, I mean, it's just all, it's, it's a gray area of the law.
[2228.10 → 2229.22] I mean, crowdsourcing is new.
[2229.40 → 2230.20] Crowdfunding is new.
[2230.48 → 2233.34] It's new in the past few years, you know, it's new in the past few years.
[2233.34 → 2239.24] So, you know, GitHub's not, GitHub's a little fish in a big pond at this point.
[2239.52 → 2241.02] And, you know, we're keeping an eye on this stuff.
[2241.02 → 2247.82] Well, if you think about it in those terms of like gifts though, like maybe I'm a guy that likes to use metaphors to understand things.
[2247.90 → 2251.10] So maybe the audience can, can just bear with me for a moment.
[2251.18 → 2252.24] If not, I'll just be quiet.
[2252.24 → 2260.04] But I kind of think of it maybe in these terms as if I'm a really, really cool, popular open source person that is awesome to use your words from earlier.
[2260.38 → 2265.38] And I'm on the proverbial digital street corner saying, I write awesome code.
[2265.50 → 2266.68] Give me, give me a couple bucks.
[2266.88 → 2269.08] That's essentially what GitHub is, but it's not begging.
[2269.24 → 2271.46] It's just an opportunity to accept a gift from somebody else.
[2271.50 → 2273.38] Is that essentially the metaphor you use then?
[2273.72 → 2274.58] Yeah, more or less.
[2274.58 → 2277.22] It almost seems like that kind of flipped on its head.
[2277.52 → 2286.22] Like, you know, whereas traditional, you know, financial, you know, pay for things is pay for service.
[2286.30 → 2289.52] Like I'm going to do a service for you and this is what you're going to pay me.
[2289.82 → 2296.42] And so it's like the opposite of that where like you're doing, you're not doing these services for pay.
[2296.48 → 2302.12] You're doing these services because you want to do them, and you're not even necessarily expecting someone to pay you on GitHub.
[2302.12 → 2307.06] It just gives me, the consumer of the service, the opportunity to say you deserve something.
[2307.28 → 2315.66] Okay, so in the law though, it's much more about intentions than it is about how the parties frame it, it turns out.
[2315.78 → 2322.24] And this is all, okay, so I am not a lawyer and GitHub is not in the business of providing legal advice formally, right?
[2323.52 → 2323.74] Yet.
[2323.88 → 2324.40] You know, so.
[2324.56 → 2324.78] Yet.
[2324.78 → 2324.90] Yet.
[2325.34 → 2332.12] Well, yeah, I mean the lawyer I talked to advised me not to, you know, GitHub is not in the business of providing legal advice.
[2332.24 → 2333.60] But it gets really gray, you know?
[2333.66 → 2338.86] So like if Read the Docs has a Read the Docs account on there, right?
[2339.44 → 2341.64] And people are giving to the Read the Docs account.
[2341.88 → 2346.00] And for anybody who doesn't know, so Read the Docs.org is a documentation of his new website, right?
[2346.70 → 2348.38] And they're one of the top receivers on GitHub.
[2348.50 → 2350.22] They get $100, $120 a week.
[2350.22 → 2353.46] So, you know, they're getting $500 a month on Get It.
[2354.62 → 2360.72] And clearly, people are getting to Read the Docs so that Read the Docs keeps going.
[2361.14 → 2361.62] You know what I mean?
[2361.68 → 2363.22] Like it's for that project, right?
[2363.34 → 2366.14] So the people on the other end of that, they're getting the money for that?
[2366.66 → 2369.08] You know, what's the, you know, what's the status?
[2369.08 → 2371.82] Is that employment for a job that they've done?
[2371.92 → 2372.90] Keeping Read the Docs online?
[2372.90 → 2381.52] You know, isn't it, it's the line for it to be a pure gift in for income tax purposes is pretty, it's a pretty high bar.
[2381.82 → 2383.30] I'm going to switch the metaphors there.
[2384.00 → 2384.26] I don't know.
[2384.58 → 2386.68] It's all about expectation and context.
[2387.28 → 2387.64] Yeah.
[2387.76 → 2395.26] I mean, you know, when you go, and you look at the case law, it's like, you know, so these two business associates in Detroit in the 60s, you know, one, you know, they both had two companies.
[2395.26 → 2397.34] And they, you know, gave each other all these backroom deals.
[2397.34 → 2399.82] And the one gave a Cadillac to the other, right?
[2400.08 → 2403.82] And so the one that gave the Cadillac wrote it off on his taxes.
[2404.10 → 2409.28] And the other didn't, who received the Cadillac, didn't report it as income because he considered it a gift, right?
[2410.38 → 2416.68] And, you know, the auditor or whatever, the solicitor came around and said, you know, where's this Cadillac this guy wrote off?
[2416.94 → 2417.70] Well, it was a gift.
[2417.70 → 2428.66] And, you know, what they decided is you had to go in, and you had to look at the specifics of each case and decide, was this given out of a, quote, unquote, disinterested generosity?
[2430.18 → 2430.54] Okay.
[2430.74 → 2433.44] It has to be a disinterested generosity, right?
[2433.56 → 2434.80] So it's a really high bar.
[2434.92 → 2435.82] A, it's a really high bar.
[2435.92 → 2439.86] And B, it's a really messy line because it's not, you know, it's not clear-cut.
[2439.86 → 2447.46] Like for them to actually sort this out, you know, what the courts do is they set up a tribunal, right?
[2447.50 → 2453.12] They set up a trier of fact, and they go, and they look at the facts of the case, and they judge for themselves, right?
[2453.16 → 2460.94] Like was this, it was this pure disinterested charity gift or was the, you know, did this have some sort of motive?
[2461.14 → 2462.28] And it, and here's the thing.
[2462.76 → 2464.14] So, okay, here's the thing.
[2464.22 → 2469.56] I see Kiddie as interested generosity, but then I don't, you know, but who am I to say?
[2469.86 → 2473.28] You know, there are hundreds of people giving to read the docs.
[2473.36 → 2475.44] Like who am I to say what their motives are?
[2475.88 → 2478.52] And so that's where it gets messy is like how are you going to try the facts?
[2478.58 → 2489.14] How are you going to, how are you going to really dig into those hundreds or potentially thousands of people that are giving to you and decide, well, this percentage was disinterested, and this percentage was actually interested because of this library.
[2489.28 → 2490.46] And then how are you going to decide?
[2490.46 → 2493.42] Like, you know, so Mike Bayer's got five different open source projects.
[2493.58 → 2495.28] You know which one was I giving to him for?
[2495.50 → 2496.70] You know, I don't know.
[2496.88 → 2499.00] It's, it's, it's a huge thing, right?
[2499.00 → 2500.64] So, yeah, I don't know.
[2500.84 → 2502.22] Like it does get pretty messy.
[2502.38 → 2505.40] It does, you know, and I'm trying not to be chicken little about it.
[2505.44 → 2509.34] I mean, I'm trying, and I'm also trying not to be, you know, naive about it.
[2509.50 → 2509.72] Yeah.
[2509.84 → 2520.26] You know, just trying to forge ahead, and we'll, you know, like I said, I did talk to a lawyer this year and, you know, as we continue to grow, I'm going to, you know, keep, keep on top of that stuff.
[2520.26 → 2523.12] Well, I certainly appreciate the transparency on that.
[2523.18 → 2528.60] I think the I guess is a follow-up to that conversation there on the openness of it then.
[2528.70 → 2537.80] So when the year does close and let's say I made more than 600 bucks from getting up, whether it's considered a gift or not a gift as by law, however you find that out.
[2537.80 → 2543.90] Is it up to that, the receiver then to, to file that or do you provide paperwork?
[2544.16 → 2548.98] Is this something you have to eventually absorb as, you know, a liability and a cost?
[2549.24 → 2549.42] Yeah.
[2549.48 → 2550.30] So three things here.
[2550.38 → 2551.98] So first, it's your responsibility.
[2553.26 → 2563.78] I, you know, Chad Whitaker personally, I reported my income I received on Gi dip last year on my taxes under, I did it online.
[2563.78 → 2565.56] It wasn't even other income.
[2565.82 → 2566.44] I did report it.
[2566.50 → 2567.84] I found a line item to report it on.
[2567.90 → 2568.66] So I did report it.
[2569.10 → 2569.92] It is your responsibility.
[2570.08 → 2571.04] It's the person's responsibility.
[2571.26 → 2572.44] And that's in the terms of service.
[2572.86 → 2574.62] You know, and that's, that's what's on the site.
[2575.18 → 2578.66] Two, what was two, gang?
[2580.00 → 2581.08] We're talking about taxes.
[2581.36 → 2581.66] Okay.
[2581.78 → 2582.96] So yeah, two is balanced.
[2583.16 → 2583.28] Okay.
[2583.68 → 2584.14] Two is.
[2584.52 → 2585.04] Where's he going?
[2585.36 → 2585.56] Yeah.
[2585.96 → 2586.38] Come back.
[2586.38 → 2590.74] Two is, there are reporting requirements that balanced is responsible for.
[2590.74 → 2602.26] So if you receive over 200 different transactions or over $20,000 balanced is obligated to give you a 1099 K.
[2603.64 → 2607.44] So that's, you know, you have your bank account information stored with balance.
[2607.56 → 2608.22] They have your info.
[2608.38 → 2609.10] They have your identity.
[2609.32 → 2614.32] So they're going to provide you a tax document in the case that you're over that volume.
[2615.28 → 2617.78] So does one month count as one transaction?
[2617.78 → 2621.10] That would be each, each week.
[2621.34 → 2621.64] Each week.
[2621.70 → 2621.88] Sorry.
[2622.08 → 2622.30] Yeah.
[2622.36 → 2622.56] Yeah.
[2622.78 → 2623.04] Yeah.
[2623.04 → 2625.14] You know, the, the payout is also thresholded.
[2625.22 → 2627.24] So if you only have five bucks in your account, we don't pay out.
[2628.08 → 2630.72] So it could be every other week or whatever.
[2630.72 → 2631.02] Right.
[2631.12 → 2631.60] But yeah.
[2631.60 → 2637.84] So if you had, so you would only have 52 payouts at most in a year.
[2638.10 → 2643.60] So you wouldn't cross the 200 threshold, but you, you know, could conceivably in the future across the 200, you know, the 20,000 threshold.
[2643.60 → 2646.24] So balance will provide you a 1099 K in that case.
[2647.12 → 2655.46] Three, when we get to, all right, so there are some features we're working on to deal in different levels of abstraction.
[2655.72 → 2655.84] Okay.
[2655.90 → 2660.46] So right now, GDP is most clearly individual to individual.
[2660.46 → 2663.24] And this is something we get to.
[2663.58 → 2667.10] We're starting to get companies, ROK, involved.
[2668.74 → 2669.14] Sorry.
[2669.28 → 2669.46] Nice.
[2670.90 → 2671.66] And others.
[2671.76 → 2673.82] So there's, there are companies that are starting to get involved.
[2674.16 → 2676.50] There are projects like Read the Docs that are starting to get involved.
[2676.72 → 2679.22] GDP itself, of course, is an open company that's on there.
[2679.70 → 2683.78] You know, and then there's just open source communities in general that we want to deal in.
[2683.78 → 2688.12] So these different ways of grouping people, right, that we need to deal in to get it somehow.
[2689.02 → 2692.54] And some of those ways are going to involve tax implications, right?
[2692.58 → 2698.50] So I'm expecting that the people, for example, that receive money through the GDP account.
[2698.74 → 2700.44] So there's a GDP account on GDP.
[2700.82 → 2702.56] Right now it's getting like 950 a week.
[2702.56 → 2714.14] And what we're experimenting with just in the past couple weeks we started this is splitting that money up publicly in sort of, in a voting, through some sort of voting mechanism.
[2714.44 → 2714.58] Right?
[2714.76 → 2724.32] So basically the idea is like this is, you know, this, this 950 a week represents the wages and profit of GDP.
[2724.66 → 2724.94] Right?
[2725.08 → 2728.64] So the operating costs, the fees are taken care of in the fees that we charge.
[2728.64 → 2733.16] And then the 950 a week going to GDP is for the people.
[2733.86 → 2734.00] Right?
[2735.28 → 2739.76] And, you know, we split that 28 different ways, I think, the past couple weeks.
[2740.60 → 2749.22] And I expect as we grow that feature that that's going to include, you know, that's going to include a tax document component.
[2749.38 → 2749.52] Right?
[2749.58 → 2753.12] Where you're going to, you know, in order to receive money through, from this pool.
[2753.26 → 2753.50] Right?
[2753.64 → 2758.30] When there's $100,000 going through that or whatever, $10,000 a week or whatever it's going to be.
[2758.30 → 2758.58] Right?
[2760.58 → 2768.86] You know, that in order to receive money from that, you're going to have to sign an additional terms of service that says, you know, I am a contractor of GDP, and I'm going to get a 1099 at the end of the year.
[2768.96 → 2773.16] And so GDP would start to get into the business of providing tax documents for that kind of situation.
[2773.16 → 2778.42] So, I mean, yeah, again, I mean, this is all tricky stuff, right?
[2778.48 → 2788.50] And, I mean, we're starting to consult with lawyers and, you know, get feedback from people on this and try and be smart about it, you know, so we don't get flipped down the road.
[2789.08 → 2790.96] You know, so we're kind of, I don't know.
[2791.26 → 2792.36] Am I answering that question at all?
[2792.44 → 2793.36] I mean, it's pretty complicated.
[2793.36 → 2796.16] Well, no, I think it's a tough, I don't think it's really answering it.
[2796.16 → 2800.36] I think it's just talking about it because I don't think there's really an answer to your situation as it is now.
[2800.48 → 2802.18] I think one part.
[2802.18 → 2822.06] I think Andrew's got something funny to ask you in a second or two, but I think that's kind of part of coming on this show and talking about, you know, not just GDP but sustaining open source and how you're exposing yourself as the founder of this and then potentially the people that get involved in it.
[2822.10 → 2823.16] What's their exposure level?
[2823.24 → 2823.94] What's their risk level?
[2824.46 → 2825.92] You know, I think it's kind of neat.
[2826.00 → 2828.64] It's a cool discussion to have.
[2828.64 → 2832.48] And I think it's certainly cool that you're doing it, but I don't think there's really an answer.
[2832.80 → 2833.84] There's so much great area too.
[2833.84 → 2834.54] There's a lot of stuff though, man.
[2834.56 → 2836.76] I didn't come on here to talk about freaking taxes.
[2837.36 → 2838.42] How did this happen?
[2838.66 → 2848.58] Well, no, but I think that it's a good point and that is like you're doing something that maybe has never been done, but it's definitely not the norm.
[2848.58 → 2857.12] So, you know, if you look at like how companies operate, how, you know, like if you're going to start a company, you can kind of look at the model.
[2857.12 → 2859.06] Like this is the way that you start a company.
[2859.16 → 2861.12] This is the way you close in on your Series A funding.
[2861.24 → 2862.92] This is the way that you do X, Y, and Z.
[2862.98 → 2863.50] And for you –
[2863.50 → 2866.02] Well, this is how you franchise a McDonald's in the limit case.
[2866.16 → 2867.12] Like it's all in the book, right?
[2867.46 → 2867.60] Yeah.
[2867.66 → 2867.94] Right.
[2868.04 → 2870.32] And so for you, there's nothing like that.
[2870.48 → 2871.60] Like these are –
[2871.60 → 2872.30] There's no manual.
[2872.66 → 2874.04] Yeah, and these are huge questions.
[2874.04 → 2876.00] These are questions that they're not easily answered.
[2876.00 → 2880.78] These are questions that you could easily answer it incorrectly, and it could cost a lot.
[2881.02 → 2887.10] These are questions that – and so I think that it's interesting because this is where the open,
[2887.12 → 2889.92] open idea, and you can get so much community input.
[2890.20 → 2896.16] Like who's to say that a very respected corporate accountant doesn't get wind of this and say,
[2896.30 → 2900.58] I want to get involved in this or a very – some perfect lawyers don't get behind this and say,
[2900.70 → 2902.16] oh, this is cool.
[2902.32 → 2903.26] Like I want to get involved in this.
[2903.34 → 2904.58] And then you have – who knows?
[2904.62 → 2906.40] You have free – you have pro bono law.
[2906.56 → 2907.42] You have pro – you know what I mean?
[2907.60 → 2907.64] So –
[2907.64 → 2909.08] And it's so serendipitous.
[2909.08 → 2912.10] You know, like I never know what's going to happen and then somebody shows up.
[2912.18 → 2920.08] Like the fraud thing, I got a dozen emails, private emails from fraud specialists, anti-fraud professionals who are like,
[2920.16 → 2920.88] Chad, let's Skype.
[2921.00 → 2922.08] I want to help you out with this.
[2922.48 → 2923.06] It's awesome.
[2923.32 → 2924.20] It's fantastic.
[2924.86 → 2926.96] I mean or like – or I'm like, oh crap.
[2926.96 → 2930.78] The second payment provider just dropped out from under me and then Balance comes along.
[2931.08 → 2931.22] You know?
[2931.62 → 2935.78] Dude, I have to give a shout-out before we slip past this.
[2936.32 → 2937.98] Balance, I just learned today.
[2938.32 → 2949.16] So Lateen Tame, the CEO of Balance, they – I'm increasing – I'm watching them because they're on board with the open company idea
[2949.16 → 2951.24] and I'm watching how that develops for them, right?
[2951.24 → 2952.54] Because they're a payment provider, right?
[2952.54 → 2953.98] Which is traditionally very closed.
[2953.98 → 2959.58] And, you know, they keep saying, you know, we really believe in this openness thing, and we're trying to move our business in that direction.
[2960.54 → 2963.06] I just read the thing I was tweeting about today.
[2963.94 → 2970.90] Lateen had a blog post in Fast Company where he's talking specifically about what it means for his business when he says it's an open company.
[2971.16 → 2975.88] What I learned in there that was really awesome is that they've open sourced their dashboard, okay?
[2975.88 → 2984.78] So the new dashboard for Balance, the like, version 2 dashboards that they're working on right now, is being developed in the open on GitHub,
[2985.78 → 2992.14] which just blows my mind that, like, you know, any – like, imagine any service that you use, right?
[2992.18 → 2997.60] And, like, you're using this service, and you're like, all right, this dashboard is pretty good, but, you know, this is just annoying.
[2997.76 → 2998.24] You know what I mean?
[2998.30 → 2998.80] You know what I mean?
[2998.80 → 3005.04] Like, anybody who's a web developer, especially if you're a front-end dev, like, when you're – you have those experiences, right?
[3005.06 → 3008.92] Like, when you're using a product, and you're like, man, why doesn't somebody fix this?
[3009.20 → 3009.72] You know what I mean?
[3009.96 → 3010.88] Do you guys know what I'm talking about?
[3011.28 → 3011.60] Absolutely.
[3011.80 → 3014.26] I mean, like, a little bug with a browser or –
[3014.26 → 3014.76] Exactly.
[3014.92 → 3016.66] It could even be a way to get a job too, so.
[3017.00 → 3017.36] Yeah.
[3018.12 → 3018.82] Exactly, right?
[3018.82 → 3030.26] And so this is a case where now when you see that, like, there's no excuse for you not to just go and clone the thing, fix the bug, submit a pull request, and it's fixed, you know?
[3030.34 → 3031.56] And then, like you said, exactly.
[3032.04 → 3033.24] That's exposure for you.
[3033.32 → 3034.34] It's reputation for you.
[3034.42 → 3035.16] It's good for balance.
[3035.24 → 3036.46] It's good for all balanced customers.
[3037.00 → 3040.92] I just – that blew me away when I found that out today because that to me is just like – it's a watershed.
[3041.10 → 3043.70] It's going the extra mile with openness.
[3044.26 → 3048.18] I'm really – I'm humbled by how much they're doing openly.
[3048.18 → 3060.60] It's funny because you bring up something that – so, like, there's this thing called usability, and then there's the UX stuff, and they're kind of the same thing, but, like, there are some differences, right?
[3060.70 → 3078.00] So it's an interesting topic because if, like, 150,000 people get used to the way this feature works even though it's not working the way it should, and then a person comes and fixes that on – let's say they fix it, you know, submit a pull request, and it gets merged in and deployed to production.
[3078.18 → 3088.96] So now all the people that have become accustomed to the feature as it was – like, okay, Facebook releases a redesign, and everyone complains.
[3089.12 → 3099.06] Like, if they don't go back to the old version, I'm quitting, and then Facebook will release their white papers that show actually, like, our usage spikes tremendously when we receive these – when we update these even from you.
[3099.06 → 3103.82] And so, like, it's funny because now the companies are going to have to answer for that.
[3103.90 → 3106.66] So the bigger GitHub gets – somebody submits a pull request.
[3106.76 → 3107.80] Everyone got used to whatever.
[3108.30 → 3113.54] Somebody submits a pull request to fix a bug, and now that feature doesn't work the same way.
[3113.58 → 3114.92] So how do you respond to that as a company?
[3114.92 → 3117.08] Oh, but – okay, so the company has to answer for it, right?
[3117.30 → 3117.54] Yeah.
[3117.64 → 3123.00] And the answer is here's a link to the GitHub thread where we talked about it openly and publicly, right?
[3123.00 → 3127.42] Like, you could have participated, and you can next time, and now you're educated.
[3127.42 → 3134.18] Kind of like saying the reason your town is gone is that we posted it downtown that you're going to get your home excavated.
[3134.50 → 3134.70] Exactly.
[3134.70 → 3135.22] You should have moved.
[3135.22 → 3136.20] This is how it works.
[3136.32 → 3136.60] Yes.
[3136.86 → 3139.40] So, yeah, I can only see that as positive.
[3139.62 → 3142.20] You know, that's – I mean, it's transparency.
[3142.52 → 3147.08] You know, this gives a – like, yes, all of us, when Facebook changes something, what do we do?
[3147.12 → 3149.64] We grouse on Facebook because we feel powerless, right?
[3149.64 → 3152.42] It feels like there's us and there's, you know, them, right?
[3152.54 → 3158.16] And the is the people inside Facebook that get to make all the decisions, this cloudy conspiracy, right?
[3158.22 → 3160.94] Like, humans are so prone to conspiracy theories, right?
[3161.20 → 3163.14] And you just – we see it – or I don't know.
[3163.36 → 3165.44] I guess I – all right.
[3165.46 → 3166.76] So I have a tendency to see it.
[3166.88 → 3169.44] You know, it's like the stuff that happens behind closed doors.
[3170.04 → 3172.72] And here we're just throwing it wide open, you know?
[3173.10 → 3179.14] I think it's extremely important when you're doing this to have a BDFL in the projects as well
[3179.14 → 3184.10] because if you just did everything that all your users wanted to do, you know, it would collapse within minutes, right?
[3184.60 → 3185.28] Yeah, yeah, yeah.
[3185.34 → 3192.46] I mean, it's a whole new kind of leadership that's needed for this kind of project and this kind of product and this kind of thing.
[3192.46 → 3193.48] That's a good point right there.
[3193.56 → 3194.20] I like that.
[3194.36 → 3196.08] I'm glad you said that because you're right.
[3196.08 → 3213.60] I think it takes a different – not a skewed perspective but definitely a different perspective because like we said earlier, at least I said this earlier, people, you know, they operate closed companies out of fear, fear of failing or acting a fool or being a fool in front of a bunch of people.
[3213.82 → 3214.06] Or competitors, right?
[3214.44 → 3215.26] Yeah, or competitors.
[3215.68 → 3219.06] You know, there's – fear is the basic component of the concern.
[3219.88 → 3220.78] Yeah, exactly.
[3220.78 → 3221.54] Oh, my gosh.
[3222.26 → 3227.72] The number of people that have asked me to sign an NDA in a coffee shop, you know, that's like, come on, guys.
[3227.96 → 3228.32] Give me a break.
[3228.32 → 3228.50] Yeah.
[3228.66 → 3230.92] Have they asked you to do that as you were representing Petit?
[3232.50 → 3233.36] Yes, exactly.
[3233.64 → 3234.74] Like here I'm running – yeah.
[3235.22 → 3236.54] For me to tell you my idea.
[3237.24 → 3238.12] Yeah, but what you just started saying.
[3238.12 → 3249.62] So you call it an open company and I think that when I – and what we do and specifically because the code is open source, like obviously it's kind of – we can kind of mix those two things up.
[3249.62 → 3264.62] But, you know, just listening to you talk, like knowing a little bit about you, and it sounds almost like the idea of an open company or your vision for an open company almost embraces like the minimalism thing more so than even necessarily like the open source thing.
[3264.62 → 3270.88] Because it's like to – the lean minimal, like use as little as you need to keep going.
[3271.38 → 3280.16] And if you do that, you can prevent the big, you know, big bloated company that is very inefficient, that is very greedy or whatever you want to say.
[3280.42 → 3281.82] So, I mean, can you speak to that?
[3281.90 → 3286.06] Like is there any minimalist influence in this open company?
[3286.06 → 3288.32] Yeah, I mean, I love minimalism, you know.
[3289.24 → 3295.30] I guess I don't – I haven't made that connection consciously before, but, you know, it certainly could be there.
[3295.82 → 3301.10] You know, trying to learn the lessons of companies like GitHub, right, that do run a distributed team.
[3301.88 → 3307.94] You know, obviously open source projects have run distributed teams for decades and free software projects.
[3307.94 → 3311.38] You know, and companies are starting to pick up on this now too, right?
[3311.48 → 3315.76] Like we don't all have to be sitting in the same place to get stuff done.
[3316.22 → 3317.84] We can get by with less.
[3317.98 → 3319.38] But, I mean, you're right.
[3319.48 → 3320.78] With GitHub, it's even more.
[3320.94 → 3326.76] You know, what goes on the corporate credit card and what goes on Chad's credit card.
[3326.76 → 3330.66] You know, more goes on Chad's credit card than goes on the corporate credit card.
[3331.50 → 3332.10] Well, it's easy.
[3332.92 → 3336.04] Yeah, I mean, it's the open idea, and then it's the transparent idea.
[3336.04 → 3338.00] It's that everyone knows.
[3338.28 → 3340.58] So it almost helps to keep it accountable too.
[3340.78 → 3345.98] And you're definitely like – you know, we kind of keep going back to it, but you're definitely bucking the mould when it comes to this stuff.
[3346.72 → 3347.82] I'm having fun now.
[3348.02 → 3348.64] I'm having fun.
[3349.26 → 3350.84] Yeah, I'm excited to see where it goes.
[3350.98 → 3358.02] I mean just because where GitHub is right now, like there's no reason to think it's going to be the same place in two months.
[3358.18 → 3358.58] Absolutely.
[3358.82 → 3364.42] And it's so refreshing because you can look at – even companies that you do admire and respect, you know, like the GitHub's of the world.
[3364.42 → 3371.28] You know, like – OK, like Fab today, they had a huge pivot and that never happens.
[3371.48 → 3373.98] Like companies never pivot like that when they've established themselves.
[3374.18 → 3385.18] So it's cool to see like that GitHub is going to be this thing that I don't even know if you'll ever call it a pivot because you're going to be forever like this fluid company that's changing and shifting the way that you do things.
[3385.38 → 3387.00] And it's based on community feedback.
[3387.24 → 3391.88] So, you know, success or failure, like it's just going to be a really fun thing to watch no matter what.
[3391.88 → 3393.96] Chad Whitaker will be the new Eric Lies.
[3394.74 → 3395.02] Yeah.
[3395.46 → 3396.28] The open startup.
[3396.88 → 3400.24] So do you feel like the definition for an open company is super strict?
[3400.72 → 3405.26] Like do you think there could be a form of it where a company does pay its employees?
[3405.90 → 3406.10] Yeah.
[3406.30 → 3409.96] I mean so balanced is taking on board the terminology open company.
[3410.30 → 3410.50] OK.
[3410.50 → 3413.20] And of course they're doing it very differently than I am, you know.
[3413.60 → 3416.38] And that's – I'm fine with that, you know.
[3416.78 → 3420.02] They're allowed – you know, I don't have a trademark on the term open company.
[3420.22 → 3422.26] So you're not being a bit of a storming about it?
[3422.92 → 3423.18] No.
[3423.52 → 3423.88] Nope.
[3424.16 → 3424.86] Not doing that.
[3425.30 → 3425.56] No.
[3425.68 → 3426.36] I mean I love it.
[3426.36 → 3437.70] It's a huge win and a huge validation for balance to be taking this on board and to own the term and to, you know, to – yeah, to own it and to give it their own meaning.
[3437.96 → 3438.90] That's great.
[3438.98 → 3439.32] I love it.
[3439.32 → 3448.42] I think the really great takeaway with your relationship with them and what you're trying to do is just all about consistency really because, you know, you have your address up on your Twitter account.
[3448.90 → 3448.98] Yeah.
[3448.98 → 3452.64] And you're all about open companies and Gi tip is an open company, and they're doing the same thing.
[3452.84 → 3454.68] It seems like – I don't know.
[3454.82 → 3455.70] It's very, very consistent.
[3456.28 → 3456.90] Super fun.
[3457.18 → 3457.36] I don't know.
[3457.78 → 3457.98] OK.
[3458.10 → 3463.26] So now we get to – now I want to talk about Heroku two weeks ago starting to give on Gi tip.
[3463.84 → 3464.20] Yes.
[3465.28 → 3467.36] Because it was awesome and thank you, Kenneth.
[3468.00 → 3470.42] Are we public with this, Kenneth, that you were behind that?
[3470.54 → 3471.20] Can I say that now?
[3471.26 → 3471.60] Yeah, that's fine.
[3471.60 → 3471.70] OK.
[3472.14 → 3473.00] So thank you, man.
[3473.12 → 3473.72] It was awesome.
[3474.12 → 3474.48] Absolutely.
[3475.06 → 3475.86] I'm really excited.
[3475.86 → 3486.26] The thing I want to mention and you and I talked about this, I want this to be public as well, is that it worked because it inspired generosity, right?
[3486.64 → 3498.60] So the story is that Kenneth brought Heroku on board with Gi tip to start investing in open source through Gi tip and you put Heroku on the top of the giver's leaderboard, right?
[3498.86 → 3499.02] Correct.
[3499.02 → 3499.78] Two weeks ago, was it?
[3499.78 → 3502.28] And then it was a tremendous validation of what happened.
[3502.72 → 3510.52] The goal was to try to lead the way, so other companies would start doing the same because companies don't really contribute back to open source in that way often.
[3511.30 → 3514.90] So Max CDN now is the number two giver, which is perfect.
[3515.04 → 3518.62] And ideally, I want people to be fighting for that number one spot, right?
[3518.62 → 3518.96] Yeah.
[3519.60 → 3521.82] And having 10, 15 companies do it.
[3522.12 → 3523.68] I think it would change everything.
[3523.68 → 3533.78] I know I've spoken privately to two other companies that are in the works with this, and I think we're only going to see more.
[3534.28 → 3546.64] But I want to say it worked in that the week that Heroku started giving on Gi tip was the biggest – okay, so you did that on a Friday and it runs every Thursday.
[3546.64 → 3555.86] So the next Thursday – you did it Friday night after we'd already run that day, a Thursday night because I was about to go to bed, and then I sat down, and I went on Gitip.com, and I saw Heroku up there.
[3555.96 → 3556.42] I was like, what?
[3556.86 → 3558.14] You know, sometimes after a couple more hours.
[3558.14 → 3569.72] So that whole next week, we got the biggest bump in by percentage of givers that we'd gotten since month two.
[3569.86 → 3570.88] I mean since last summer.
[3571.54 → 3582.04] So it was like givers total went up 12% in the wake of Heroku joining and setting that example.
[3582.58 → 3583.02] That's amazing.
[3583.02 → 3589.40] And ideally as more companies get involved, that number will continue to grow, and it will be like a – I can't remember the term.
[3589.48 → 3592.78] It will be like the cruft of the hockey stick basically.
[3593.38 → 3594.02] The cruft?
[3594.82 → 3595.36] Is that what you call it?
[3595.38 → 3595.98] I don't know.
[3596.38 → 3596.78] I'm in.
[3597.20 → 3597.62] I'm in.
[3597.70 → 3598.92] The cruft of the hockey stick.
[3599.00 → 3599.26] Sure.
[3599.34 → 3599.66] Why not?
[3601.14 → 3601.46] Yeah.
[3602.18 → 3602.90] Up and to the right.
[3604.24 → 3604.76] We'll get there.
[3604.76 → 3614.20] Kenneth, since you pioneered Heroku supporting GitHub and not so much just GitHub but those that are on GitHub that need support.
[3614.68 → 3629.24] What do you – so if there's someone out there listening to the change law, whether it's live or the podcast, what do other companies like Heroku – not exactly like Heroku, like your technology, but that care about open source, that use open source?
[3629.32 → 3630.70] Pretty much lots of companies, right?
[3630.70 → 3635.52] But what should they know about GitHub that Heroku knows that can make them do the same?
[3636.16 → 3646.64] Well, I mean I feel like it should be any company really because I feel like every single company that's doing something meaningful in the world probably has a set of software developers, and they're probably using open source in some way.
[3647.22 → 3654.42] So they should all – they should sign up for an account and start just contributing like $5 a week to some developers.
[3654.62 → 3660.24] There's code they use or as there are more projects that will start to – there's Read the Docs right now and there's Git Tip.
[3660.24 → 3667.62] And ideally like there would be like a Django account, right, on Git Tip, and they could just contribute to that and that would be huge.
[3668.26 → 3675.46] And I think there are plans to have a page on Git Tip that will kind of explain – a pitch to a company on why they should do that.
[3675.84 → 3676.56] Right, Chad?
[3676.70 → 3676.96] Yeah.
[3677.20 → 3683.26] I wrote – I don't know if you saw it, Kenneth, but there's a ticket in GitHub that has some notes towards that.
[3683.50 → 3683.82] Awesome.
[3684.52 → 3684.76] Yeah.
[3684.76 → 3690.44] So it's cool because you see like – so there are obviously – one of the big problems.
[3690.60 → 3693.12] There are obviously well-known developers, right?
[3693.12 → 3701.28] There are well-known developers that do get paid a lot of money in their day job, or they do get paid a lot of money to speak at conferences or – well, you know what I'm saying.
[3701.28 → 3708.66] But there's this notion that only those developers could very easily get noticed.
[3708.86 → 3709.24] You know what I mean?
[3709.32 → 3712.16] Like those are the guys that are out in public that are doing things that you see.
[3712.30 → 3721.52] So it's easy to say – like, so someone like Kenneth, you obviously work at Heroku and you go to conferences.
[3721.74 → 3722.88] You do other things.
[3722.88 → 3730.16] So you're one of the top receivers on GitHub and I think it's cool, and I think this is an opportunity for you to say, OK, I'm just going to be a funnel.
[3730.48 → 3734.72] Like people can support me on GitHub, but then you're also one of the top givers.
[3734.86 → 3737.74] So then you can turn around and give that to other people that you've encountered.
[3737.74 → 3747.56] And hopefully – I mean I would love to see that happen where just because you're receiving money on GitHub, that doesn't mean we need the rich to get richer or – and I'm not trying to say you're rich or anything, Kenneth.
[3747.56 → 3752.54] But just to say you as a model, like it's cool to almost see you as, like I said, a funnel.
[3752.76 → 3760.60] Like money comes into you from GitHub, and then you can disperse it to things that you use, and it can keep going, and it has this effect where it can kind of chain like that.
[3760.70 → 3761.48] I think that's really cool.
[3761.48 → 3769.58] I think it's also really important that if you're receiving money on GitHub to consider keeping it all too because like it needs to leave the system for it to work, right?
[3769.76 → 3769.96] Right.
[3770.22 → 3775.98] And I feel like a huge part of it – like ideally, I think every like major open source contributor –
[3775.98 → 3785.48] I feel like in Git Tip's goals basically, their long-term goals are like they'd all be receiving like $2,000 a week and that would be like their salary, and they wouldn't have to work anymore.
[3785.60 → 3788.16] They could just work on open source all the time.
[3789.02 → 3796.12] So funnelling things all the time I don't think could work, but it depends on the sustainability of your situation and all these other things, right?
[3797.96 → 3798.56] I don't know.
[3798.94 → 3800.30] Chad, do you have any thoughts about that?
[3800.76 → 3801.16] Absolutely.
[3801.16 → 3805.12] I mean the goal is for people to make a living through Git It.
[3805.12 → 3810.54] The goal is for many people to make a living through Git It, not just the quote-unquote rock stars.
[3811.16 → 3821.28] That's been a huge subject of conversation in the issue tracker especially, and we've got some features in the works to work on that.
[3821.92 → 3828.62] One of them is this project thing that I think I started talking about with – how did I phrase it?
[3828.62 → 3832.08] When I was saying that we're trying to introduce these levels of abstraction, right?
[3832.14 → 3837.14] Layers of abstraction so that you've got groups as well as just individuals, right?
[3837.80 → 3844.62] So we're hoping to do – implement those in a way that helps the long tail, helps keep our genie index down.
[3845.42 → 3850.62] Genie is a measure of inequality that's used a lot and that is one index that we're starting to track.
[3850.62 → 3855.46] I lost the train.
[3857.46 → 3857.96] I lost the train.
[3857.96 → 3858.54] Genie index.
[3859.10 → 3859.76] The rock stars.
[3860.18 → 3861.42] Yeah, rock stars, right.
[3861.78 → 3863.90] We – man.
[3865.14 → 3868.24] We – I want it to work for everybody, right?
[3868.28 → 3872.28] I want it to work – I want it – okay, here's something I was thinking when we were talking about this.
[3872.28 → 3877.30] Open source projects is a big part of it.
[3877.82 → 3880.76] I'm interested – maybe this is a place to introduce this.
[3881.34 → 3890.52] Not just open source projects but open products which is an idea that has been floating around in my head, and I'm actually – I think you guys have seen.
[3890.74 → 3894.72] I'm hoping to get together a blog post for the changelog about this.
[3894.72 → 3904.80] But sites like GDP that are primarily a single hosted product but just happen to be open source, right?
[3904.92 → 3917.04] As opposed to something like WordPress, for example, which has a hosted version but is really like an open source project that also has people that will host it for you.
[3917.36 → 3918.26] Do you catch that distinction?
[3918.48 → 3919.12] You know what I'm talking about?
[3919.82 → 3921.78] Like for example, the balance dashboard, right?
[3921.82 → 3922.68] Like this is a great example.
[3922.68 → 3924.92] It would be what I would call an open product.
[3926.14 → 3934.60] You're not really – it's not primarily designed for you to go set up your own instance of it, although you could, and you're not going to be stopped from doing that.
[3935.10 → 3940.32] But it's really supposed to be like the balance dashboard, and it happens to be open, right?
[3941.44 → 3944.56] I feel like Read the Docs is probably the best example of that today.
[3945.04 → 3945.48] Say again?
[3945.80 → 3946.48] Read the Docs?
[3946.98 → 3947.30] Yeah.
[3947.46 → 3948.42] So Read the Docs.
[3949.26 → 3950.52] Get Sentry is another one.
[3950.62 → 3951.62] GetSentry.com, right?
[3951.62 → 3953.76] Travis CI.
[3954.62 → 3962.48] You know, we've got these instances of – and again, it's starting as open source itself does with the developer tools, right?
[3963.32 → 3968.26] It works for those products because they're developer focused.
[3968.26 → 3979.52] So I'm really curious how far we can push the limit with – how far we can push the envelope with consumer-facing products that also happen to be open.
[3980.36 → 3980.54] You know?
[3980.84 → 3986.24] I mean sort of the canonical thing in my mind is just like what if Twitter were open source?
[3986.40 → 3988.34] What if Google were open source, right?
[3988.34 → 3997.92] So I had that experience like we were talking about earlier where it's like there's a little niggling misfeature or bug on Twitter.com or on Google.com.
[3998.08 → 3999.52] You know, like Facebook.com.
[3999.64 → 4002.92] Big consumer applications.
[4003.10 → 4004.22] Big consumer products.
[4004.22 → 4005.22] Big consumer products.
[4005.22 → 4006.62] What if they just happen to be open?
[4006.98 → 4020.04] You know, that sort of – that what if is sort of, you know, out there in the future that I'm sort of aiming towards and why I'm so happy about this balanced thing today with their dashboard being open.
[4020.50 → 4022.20] So that's the kind of world I want to live in.
[4022.20 → 4024.92] You know, I want to live in a world where I feel empowered, you know?
[4025.04 → 4037.18] I want to live in a world, you know, where we have openness, you know, and transparency and where it's more fluid, you know, where I can go get involved in this project because look, man, we're already doing it.
[4037.24 → 4047.94] You know, I was talking to somebody who was I talking to yesterday, you know, that was saying like for, you know, for top programmers in the Valley, it's like four months is your employment.
[4048.06 → 4050.26] Your term of employment is not unusual.
[4050.56 → 4051.00] You know what I mean?
[4051.00 → 4054.04] I mean like two years ago it was two years, and now it's four months.
[4054.78 → 4055.36] I mean come on.
[4055.62 → 4060.48] Like clearly employment, you know, do we want to use the word broken or what?
[4060.64 → 4064.96] I mean, you know, clearly employment is shifting and changing, right?
[4065.08 → 4070.90] What does full-time employment mean when you work for four months, and then you move on to something else for six months?
[4071.48 → 4071.74] You know?
[4071.80 → 4079.36] So like why not – so part of what I'm trying to do here is loosen it up so you can work on something for four months, you know, without –
[4079.36 → 4081.48] and you can ease into it, you know?
[4081.54 → 4086.10] Like you don't have to go through this big hiring process and all this paperwork and everything.
[4086.34 → 4093.40] Like you can ease into one and then gradually fade into another project and somehow, you know, civilization goes on.
[4093.62 → 4094.00] I don't know.
[4094.00 → 4095.98] I don't know.
[4096.04 → 4097.54] We'll see how far the open products can go.
[4097.78 → 4098.60] In all directions.
[4099.34 → 4099.70] Yeah.
[4101.02 → 4101.38] Yeah.
[4101.76 → 4102.84] For better or for worse.
[4103.96 → 4104.26] I don't know.
[4104.26 → 4104.32] Yeah.
[4104.32 → 4108.24] In some ways, it's like you're going to be a pioneer in this area.
[4108.38 → 4114.52] I can – you know, you can see it because this is going to be something that it's just going to – like it's going to grow.
[4114.98 → 4122.68] And it's not necessarily, you know, just GitHub is going to grow, but you can just kind of see that the mindset that's behind this is going to be something that grows.
[4122.88 → 4123.86] And it's going to be really cool.
[4123.88 → 4124.74] Somebody's mentioning Reddit in the chat room too.
[4124.86 → 4126.56] That's another great one, right?
[4126.74 → 4127.56] It's open source.
[4127.64 → 4128.86] You can go run Reddit if you want.
[4129.00 → 4129.56] Oh, yeah.
[4129.60 → 4129.98] That's great.
[4130.28 → 4131.92] You know, that's absolutely a great one.
[4132.16 → 4133.26] Sorry, I didn't mean to jump in on the end.
[4133.26 → 4133.70] I always forget.
[4134.12 → 4135.40] Everyone always forgets about that.
[4135.96 → 4137.52] Changelog needs to be funded on GitHub.
[4137.72 → 4140.14] You know, we need – because it's not just for programmers.
[4140.28 → 4141.54] Because storytellers, right?
[4141.88 → 4145.28] Like you guys that are, you know, surfacing all this great stuff that's going on in the community.
[4145.40 → 4147.02] Like that's a really important role, you know?
[4147.32 → 4150.46] That's something we need to tie into GitHub more, right?
[4150.54 → 4151.78] Is like how to tell stories.
[4151.94 → 4154.76] Because developers aren't necessarily good at telling their own story.
[4154.86 → 4155.66] So that's another thing.
[4155.86 → 4161.18] It's another part about getting people who aren't rock stars taken care of is helping them tell their stories.
[4161.18 → 4165.70] Be like, look, you know, I spent the past six months, you know, deep down in the boiler room in the kernel.
[4166.34 → 4169.46] You know, and here's – I'm not going to toot my own horn.
[4169.56 → 4171.38] But you guys are the ones that can bring that out.
[4171.52 → 4171.86] You know what I mean?
[4172.12 → 4176.46] And originally you could sign up with a GitHub account to have a profile on GitHub.
[4176.46 → 4178.64] And now you can have a Twitter account, right?
[4178.72 → 4180.34] And that's to open the door for everybody.
[4180.48 → 4182.56] Is there any other services like that you're hoping to add?
[4182.56 → 4183.40] How about today?
[4183.74 → 4185.40] I never signed in to Facebook.
[4185.52 → 4186.98] I happened to sign in to Facebook today.
[4187.74 → 4193.76] And an acquaintance of mine had posted unbeknownst to me on Facebook all about GitHub, right?
[4193.84 → 4195.18] And she was super pumped about GitHub.
[4195.24 → 4196.88] And she was starting to tell all her friends about it.
[4197.06 → 4198.46] She's not a developer at all, you know?
[4198.76 → 4203.44] She's like – I actually met her at Occupy Pittsburgh, believe it or not, right?
[4203.44 → 4206.40] And, you know, she's super pumped about it, right?
[4206.48 → 4207.48] So Facebook.
[4207.70 → 4208.70] So now GitHub is on Facebook.
[4208.82 → 4210.14] We've already had a Facebook page.
[4210.48 → 4218.34] But, yeah, I think there are a lot more communities that can really find interesting uses for GitHub.
[4218.76 → 4220.46] And we want to support them.
[4221.48 → 4221.58] Yeah.
[4222.58 → 4226.04] I think there's so much more that we can go into.
[4226.04 → 4228.60] I think we're going to have you back for another show.
[4229.68 → 4230.94] So we're kind of running out of time.
[4231.14 → 4232.34] So let me ask you, Chad.
[4232.34 → 4235.74] But who is your – this is kind of the changelog question.
[4235.82 → 4238.28] Who is your programming hero, somebody that you have looked up to?
[4239.72 → 4240.78] Guido Van Possum.
[4241.22 → 4244.00] So I've been trying not to say that throughout this show.
[4244.24 → 4249.02] I've been trying not to, like, fanboy about Guido and use him as an example because I knew you were going to ask me this.
[4250.10 → 4251.10] So how about – all right.
[4251.14 → 4253.28] So here's a little funny – here's a little quirk about that.
[4253.28 → 4258.88] So at Pylon this year, we – I don't know if you guys have seen pictures online or whatever.
[4259.00 → 4261.22] But I have this penny puncher.
[4261.76 → 4264.44] I have a two-foot hole punch, right?
[4264.54 → 4266.20] And it puts holes in metal.
[4266.78 → 4272.06] And I made – I got some custom tooling made for it so I can put hearts in pennies.
[4273.14 → 4273.58] Okay.
[4273.94 → 4274.34] It's the –
[4274.34 → 4274.74] Is that legal?
[4274.74 → 4275.74] So –
[4275.74 → 4277.56] It's ambiguous.
[4277.70 → 4278.42] You're going to have to talk to my lawyer about that.
[4278.60 → 4278.72] Yeah.
[4280.10 → 4286.32] So I put hearts in pennies and I had a booth at Pylon, and we had this penny puncher there, right?
[4286.36 → 4287.14] So it was a huge hit.
[4287.28 → 4293.82] A bunch of people came by the booth, and we had them punching – we were punching holes in all kinds of different currency, right?
[4294.38 → 4295.20] It was a lot of fun.
[4295.88 → 4297.12] And I found a penny.
[4297.12 → 4298.22] I went, and I found a penny.
[4298.34 → 4302.62] It was a 1991 penny, which is the year that Python was first released, okay?
[4302.62 → 4310.94] And I put a heart in this 1991 penny and I went out, and I found Guido and I said, Guido, I want to give you this penny.
[4311.88 → 4314.24] And he said, oh, that's so sweet.
[4314.90 → 4318.12] But I'm not taking any swag this conference.
[4318.96 → 4326.34] I just hung my head in shame because he had like – he had tweeted about it like the week before the conference and I hadn't noticed or whatever.
[4326.56 → 4326.92] You know what I mean?
[4326.92 → 4336.14] So I just – every time I try and talk to that dude, I just like start drooling or whatever and just make a fool out of myself.
[4336.62 → 4341.26] But yeah, I mean like I started – when I started Get It, I was like I just want to give Guido money.
[4341.90 → 4342.94] Like I just love Python.
[4343.20 → 4346.16] I love the language and I love his leadership style.
[4346.32 → 4347.62] We mentioned it briefly earlier.
[4347.62 → 4349.78] I just love the way he runs the scene.
[4351.22 → 4352.82] And yeah, so I look up to him a lot.
[4353.62 → 4357.52] And maybe someday when we're not at the conference, he'll accept a hard coin from me.
[4359.18 → 4362.70] Until then, keep plugging away.
[4363.42 → 4364.68] We'll get there.
[4365.38 → 4365.54] Yeah.
[4365.80 → 4369.74] So like I said, there's so much more that we're going to get into.
[4369.80 → 4374.64] I think it will be fun to have you back maybe in a few months when we see kind of where this thing goes and the fluid of it.
[4374.64 → 4376.18] And we'll be talking about – who knows?
[4376.26 → 4379.38] I mean we'll be talking about some – like I live in Nashville now.
[4379.42 → 4383.66] We'll be talking about some small-time musician that's being funded on Get It.
[4383.80 → 4385.72] And it will be real cool to have that conversation.
[4386.32 → 4389.00] Let's – can we talk about one more thing before we close, Andrew?
[4389.92 → 4390.16] Yeah.
[4390.70 → 4396.86] So Chad, I know when we had that conversation, I kind of wish part of what we talked about could have been podcasted somehow.
[4397.18 → 4401.52] But one thing you mentioned, and we talked about it in the show is that it is open.
[4401.52 → 4408.24] You don't pay anybody, but you are hiring, and you have a huge stack of issues to go through.
[4408.42 → 4413.96] So if someone was out there listening right now, and they wanted to kind of like, yeah, I want to get into this open company thing.
[4414.10 → 4418.22] How could they – what is the easiest way besides just saying, hey, go check out the issues and just jump in?
[4418.26 → 4422.02] Do you have like a list of like your top ones, or what's the big need right now?
[4422.02 → 4428.66] So this is the biggest problem I'm trying to crack right now, right, is how to scale the community of developers.
[4429.08 → 4434.22] I mean if you're – like you were talking about, Andrew, the blueprint, right?
[4434.26 → 4438.30] I mean you go get some VC funding, and you hire your team, and you're off and running, right?
[4438.70 → 4442.06] So that's not available to me because I don't have any profit to share with venture capitalists.
[4442.18 → 4445.20] So I can't just go take salaries out and hire people.
[4445.20 → 4450.84] So we've gotten a lot of contributions from a lot of great people, which is awesome.
[4451.62 → 4462.74] What I see – really what I'm trying to do is get that Gi dip funding in place, that funding mechanism so that as you're working on Gi dip,
[4463.18 → 4469.04] there is that incentive where you are going to get a slice of the pie as you stick around and as you grow the whole system.
[4469.16 → 4470.80] So that's piece number one that I'm working on.
[4470.80 → 4475.64] Number two is in the meantime, I'm like trying to piece together a lot of things.
[4475.98 → 4478.46] So there is a page on Gi dip right now.
[4478.60 → 4483.38] On the About page, there is a Get Involved section, which does list a couple different mechanisms for getting involved.
[4483.60 → 4484.66] It links to the issue tracker.
[4484.82 → 4488.34] It links to IRC, free node, pound Gi dip.
[4489.10 → 4491.32] And it also links to a newsletter.
[4492.28 → 4496.10] I have been experimenting with a weekly newsletter that kind of – it's a summary.
[4496.10 → 4501.02] It's a digest of what's going on from my point of view in the community of people that are actually building Gi dip.
[4501.38 → 4509.20] So right now, that's the best way to get involved is to go to gidip.com slash about and under Get Involved, sign up for that newsletter.
[4511.28 → 4512.52] We'll see how that evolves.
[4512.70 → 4513.42] You know, that's an experiment.
[4513.56 → 4514.32] This is all an experiment.
[4514.32 → 4525.84] I'm hoping – Kenneth indicated earlier, he tipped our hand that we're hoping to get some pages out that explain – that go into more detail about getting involved.
[4526.02 → 4538.12] You know, that whether you're a company that wants to start investing in open source on Gi dip or you're a person that wants to start developing, or you want to give money, or you've got an open source project, and you want to receive money.
[4538.12 → 4545.86] You know, that's – I'm seeing that as a priority to just explain it for those different audiences in more detail.
[4546.28 → 4547.52] Here's what the community is like.
[4547.60 → 4548.40] Here's how to get involved.
[4548.76 → 4554.86] Jacob Kaplan Moss gave a great talk at Heroku's Gaza conference a couple of months ago.
[4555.48 → 4556.92] And it was about growing a community.
[4557.06 → 4559.00] It was about lessons learned from growing the Django community.
[4559.10 → 4560.58] And that's one of the ones that stuck with me.
[4560.58 → 4568.70] The idea of really documenting your contribution policies and ways to get involved, it sounds like that's something they really focused on.
[4568.94 → 4573.26] I mean they have great docs overall, but in particular how to get involved.
[4573.40 → 4577.84] So that's something I'm hoping to work on in the near term with Gi dip so it's easier to do.
[4578.48 → 4580.82] But for now, check out that newsletter I guess is what I'm trying to say.
[4581.78 → 4582.42] Check out the newsletter.
[4582.76 → 4585.04] So is it on the homepage, or where is it?
[4585.04 → 4587.76] Yeah, you've got to go to about – it's on tiny letters.
[4587.88 → 4589.78] So its tiny letter slash get it will get you there too.
[4589.78 → 4592.42] Oh, man, you've got to move the campaign monitor right away.
[4592.56 → 4593.48] You can't be there anymore.
[4593.66 → 4595.40] Look, where I want to move is Medium.
[4595.60 → 4596.42] Have you guys tried Medium?
[4597.38 → 4600.44] I just got my invite over the weekend, and I've got like two –
[4600.44 → 4604.88] They're the first people that have actually cracked WYSIWYG that I've seen.
[4604.96 → 4612.94] I mean tiny letter – like WYSIWYG is the Achilles heel of all content web apps and I love Medium's implementation of it.
[4613.22 → 4614.86] Maybe there will be an open product someday.
[4614.98 → 4615.24] I don't know.
[4615.72 → 4616.00] Maybe.
[4616.40 → 4616.62] Maybe.
[4616.82 → 4617.56] We'll get there.
[4618.98 → 4619.38] Yep.
[4619.38 → 4630.40] Well, so I think that we would – we will find a way via the changelog to try and take up the Heroku banner and start to give through GitHub.
[4630.52 → 4637.56] I think that will be fun to start to pick people and pick little projects to support because we use a lot of open source stuff at the changelog.
[4637.56 → 4641.88] Well, dude, the big one for you guys, man, you've just got to link to people's accounts.
[4642.06 → 4649.24] I mean Decoders Weekly, I believe it is, on all their – they have a weekly Python newsletter and each bullet point, they put a link.
[4649.24 → 4653.92] They just have a little GitHub icon, and it links out to that person's GitHub account.
[4654.30 → 4655.28] I mean this kind of things.
[4655.46 → 4661.44] The more we can build the network and weave the map denser, I see that as a great role for you guys.
[4661.44 → 4670.50] Yeah, we can definitely start doing that more on – when we cover different projects or some of the editorial stuff we're working on, we can definitely start doing that more often.
[4670.72 → 4675.92] It's something we certainly want to do because we like what you're up to, and we like supporting people, obviously.
[4676.30 → 4676.86] Thanks, man.
[4677.06 → 4678.38] Yeah, we'll talk about it offline.
[4679.64 → 4680.04] Cool.
[4680.26 → 4680.70] Privately?
[4681.56 → 4682.08] Yeah, privately.
[4682.96 → 4683.40] Sorry.
[4683.40 → 4686.04] Off the call on a GitHub issue.
[4686.16 → 4686.52] How about that?
[4687.38 → 4688.10] Oh, there you go.
[4688.28 → 4688.42] Yeah.
[4689.36 → 4689.66] All right.
[4689.68 → 4691.00] Well, I want to thank everyone for tuning in.
[4691.06 → 4696.56] Again, we do this every Tuesday live at 6 p.m. Eastern, 3 p.m. Pacific.
[4697.56 → 4699.12] Specifically, thanks for being on the show.
[4699.28 → 4702.24] I want to thank Kenneth and Adam and I want to thank you for hanging, Chad.
[4702.40 → 4703.04] It was a good time.
[4703.32 → 4703.66] Absolutely.
[4703.90 → 4704.32] For sure.
[4704.46 → 4705.18] It was a super fun time.
[4705.26 → 4705.70] Thanks for having me, guys.
[4705.70 → 4708.28] Before Chad goes, I want him to say my favourite quote from him.
[4708.98 → 4709.38] Uh-oh.
[4709.72 → 4710.12] Everybody.
[4710.64 → 4712.54] I'm not building GitHub.
[4712.54 → 4715.12] I'm building a community that's building GitHub.
[4716.00 → 4716.88] Is that the one, Kenneth?
[4717.42 → 4718.02] Yes, that's it.
[4718.02 → 4718.48] Thank you.
[4718.54 → 4719.16] That's a good one.
[4719.28 → 4719.70] I like that.
[4719.74 → 4721.38] It's a great one, and it's extremely important.
[4722.16 → 4722.38] Yeah.
[4722.94 → 4725.36] It definitely pulls back the curtain a bit more.
[4725.52 → 4727.14] And he was making waffles with me the other day.
[4727.24 → 4730.24] I was at his place and he said he was making waffles.
[4730.24 → 4731.50] He wasn't making waffles.
[4731.62 → 4733.36] He was making the community that was making waffles.
[4734.68 → 4735.62] We had a good time.
[4736.04 → 4736.22] Yeah.
[4736.34 → 4736.92] Anyway, sorry.
[4737.60 → 4740.90] Anybody wants waffles, 716 Park Road, 153 in the throat.
[4740.90 → 4743.22] Next time in Pittsburgh.
[4744.26 → 4744.62] Nice.
[4744.98 → 4745.62] All right, guys.
[4746.54 → 4748.64] Again, we are member supported here at The Changelog.
[4748.74 → 4751.56] You can visit us at thechangelog.com slash membership.
[4751.96 → 4755.34] You can visit us at thechangelog.com slash store to buy a shirt.
[4755.48 → 4757.64] And as Adam likes to say, to hack and style.
[4757.90 → 4760.18] Yeah, hack and style with The Changelog team, man, for sure.
[4761.48 → 4762.42] All day long.
[4763.02 → 4763.66] All right, guys.
[4763.72 → 4764.88] Thanks for being on the show with us.
[4764.94 → 4765.34] Very good.
[4765.76 → 4766.12] Keep real.
[4766.12 → 4766.40] Okay.
[4766.58 → 4767.30] Thank you, guys.
[4767.30 → 4785.90] See it in my eyes.
[4786.42 → 4789.30] So how could I forget when...
[4789.30 → 4811.90] So how could I be sitting here?
