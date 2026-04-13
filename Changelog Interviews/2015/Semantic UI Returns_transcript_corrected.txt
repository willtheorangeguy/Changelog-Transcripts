[0.00 → 15.82] welcome back everyone this is the change log and I'm your host Adam static this is episode 164
[15.82 → 22.70] and on today's show we're joined by jack Lutsk jack is back talking about semantic QI again
[22.70 → 29.10] we had him back on episode 106 almost a year and a half ago and that was before semantic QI
[29.10 → 37.32] was at 1.0 so that's pre 1.0 well now semantic QI is at 2.0 so a lot of new changes a lot of new
[37.32 → 43.88] additions, and we dive deep into a lot of the details about semantic QI, but we also talked quite a bit
[43.88 → 51.34] with jack about why and how because jack is doing semantic UI full-time it's crazy gotta listen to
[51.34 → 59.62] this show we have three awesome sponsors code ship code school and hip chat our first sponsor is
[59.62 → 65.00] code ship a hosted continuous delivery service focusing on speed security and customizability
[65.00 → 70.98] you can set up continuous integration in your app today in a matter of seconds and automatically
[70.98 → 77.26] deploy your code when your tests have passed code ship supports your GitHub and Bitbucket projects
[77.26 → 82.18] and you can get started today with code ship's free plan should you decide to go with a premium plan
[82.18 → 89.32] you can save 20 off any plan you choose for three months by using our special code that code is the
[89.32 → 96.64] changelog podcast again the changelog podcast save 20 off any plan you choose for three months head to
[96.64 → 101.16] codeship.com slash the changelog to get started and now on to the show
[101.16 → 114.06] all right we're back we got an uh returning guest jack music the maker of semantic UI back in episode
[114.06 → 119.04] 106 it was not me and jarred right jarred that's a bummer right it was me and Andrew
[119.04 → 125.54] it's a good show I listened to it uh today it was excellent show but uh yes bummer that I wasn't on
[125.54 → 129.94] there yeah but uh say la Vida Andrew we miss you buddy but that was a good show as well
[129.94 → 137.56] 106 that was October 5th 2013 almost a year and a half ago just give or take a few days or something
[137.56 → 145.54] like that seconds or whatever but uh jack you're back um that was when you were here at 106 that was
[145.54 → 152.04] pre 1.0, and you've gone through 1.0 you got in touch with us on our ping repo on GitHub um we didn't
[152.04 → 158.28] end up syncing, and now you're at 2.0 so I mean we missed 1.0 now we're at 2.0 uh semantic UI
[158.28 → 164.18] welcome back to the show thanks it's uh great to be here talk to you guys and just to summarize
[164.18 → 169.30] a bit from the last show jarred feel free to step in and help me as well but jack you're a language
[169.30 → 174.50] guy right you began more in the languages and that's why you're really into the semantics of
[174.50 → 181.04] the web and that's how you got into what you're doing with semantic UI am I right yep um so I studied
[181.04 → 187.28] cognitive science uh for my undergrad um I've always been sort of interested in the way that
[187.28 → 192.42] computer languages have been different from um natural languages and trying to sort of understand
[192.42 → 197.64] um you know what a program language would look like in the year 2100 or what program languages
[197.64 → 203.10] sort of what directions are they moving um so that's that's obviously a very large broad question
[203.10 → 207.76] um so I've tried to sort of scope it in the know the context of what we can do today to sort of
[207.76 → 213.28] you know uh change program languages to sort of you know look at these features of
[213.28 → 219.74] future programming very cool, and we've uh jarred we've been we lived through it right we talked
[219.74 → 225.30] about Zeeman at least once or twice on the show before right so uh web standards that was a big
[225.30 → 231.58] deal uh and obviously semantics matter um but as we start getting into the days today when people are
[231.58 → 237.48] sort of targeting the Dom, and it's a little less concern is not complete no concern but a little less
[237.48 → 242.28] concern about semantics I'm wondering uh if we can bring that up at some point during the show but
[242.28 → 248.42] maybe some more interesting things might be jack what your situation is making this project
[248.42 → 255.56] sure um so I think when you talked to me last I'm trying to your know replay in my head what I was
[255.56 → 261.84] doing in 2013 um I was working at a startup previously called quirky um if you don't know
[261.84 → 267.14] about quirky is a social invention company um people submit ideas for consumer products on their
[267.14 → 271.54] website, and then they convert them into real products and then share the proceeds with the inventor
[271.54 → 278.90] um so I left there a couple of years ago um semantic at the time was actually the code name of an
[278.90 → 286.56] internal redesign at quirky um which sort of involved uh like we're scaling the team from you know
[286.56 → 291.02] well the company was 50 people at the time and by the end of the year it was 150 people
[291.02 → 296.92] so it was like it was becoming a very different company overnight um and so for me, you know I was
[296.92 → 302.98] the lead front end developer at the time I was trying to sort of work out the idea of um how you
[302.98 → 307.44] get a bunch of developers to code on a platform together without having to deal with you know
[307.44 → 314.28] the idiosyncrasies of individual developer preference um naming conventions um and that kind of stuff
[314.28 → 319.58] um and so for me what was really exciting was you know going back to all this source material which
[319.58 → 326.88] fascinated me when I was younger um about just sort of how people construct meaning um and so
[326.88 → 334.76] uh semantic UI is sort of a byproduct of that it's a kind of new understanding not that new I guess
[334.76 → 339.84] but it's a unique understanding of of of how people should construct meaning through programming languages
[339.84 → 345.76] um and so it's an UI framework you know the nuts and bolts is a bunch of things you can plug in
[345.76 → 351.80] into your website that has drop-downs and modals and all that kind of stuff um but the language
[351.80 → 357.84] behind it is based off of natural language it uses uh relationships like plurality now modifier
[357.84 → 364.62] relationships uh tense things that are sort of constructs from natural languages um uh which sort
[364.62 → 372.04] of help people write um non-prescriptive uh front-end code so you know everyone has their own way of
[372.04 → 378.16] of calling something um and working with semantic UI sort of gives you a single language
[378.16 → 384.96] which um is maybe not objective but more objective than you know deciding at the spur of the moment
[384.96 → 393.44] what you want to call something um so yeah so I was working at quirky uh when I left um Ben the CEO
[393.44 → 403.08] there was really wonderful um also Nathan smith the um the head uh, uh CTO there um both you know
[403.08 → 407.98] were great and they let me open source the project um I continued to work on it afterwards
[407.98 → 412.94] um, and you know it was kind of one of those things where you know if you just finish
[412.94 → 419.34] a very gruelling startup and i kind of you know I took it easy I travelled for a while like
[419.34 → 424.90] I went through southeast Asian all that you know that kind of stuff and I came out of it um and i
[424.90 → 428.92] was just sort of like I still don't want to work on this like this is still really important to me
[428.92 → 437.72] um, and so i sort of went from there um yeah so it sounds like this is a solo project you may have
[437.72 → 442.44] some contributors which I haven't even gone to the tab on GitHub yet but I'm going to do that here right
[442.44 → 448.08] now so I don't put my foot in my mouth, but it sounds a bit like it's basically a solo project
[448.08 → 453.72] with 106 other people I just looked at the contributors tab yeah well 106 other people
[453.72 → 462.68] so it's technically 104 right so yeah we have 800 translators um we have 100 contributors um lots
[462.68 → 467.20] of issues open every day it's great it's one of those things where I realized the more you make
[467.20 → 472.52] something accessible the broader scope of people that will be helping you out so like every time
[472.52 → 476.28] that like it becomes less like a programming language and more like something that people can
[476.28 → 482.16] understand than like you get these like first-time GitHub contributors with like you know no avatar
[482.16 → 487.68] just like leaving their first issue which is actually like literally my favourite thing is because all the
[487.68 → 492.50] first-time contributors are like probably the best like they have the most insight they're like they
[492.50 → 496.80] come from a perspective where they're from you know some other industry they're from finance, or they're
[496.80 → 501.44] from something else and they know they want to make a website um so yeah so it's its been really
[501.44 → 510.14] great um I think um for me at least the way I think about the project it's I'm afraid of what it
[510.14 → 514.92] means to have too many cooks in the kitchen in terms of like naming and language and conventions
[514.92 → 521.40] um so obviously you know the hundreds of pull requests you know lots of contributors but generally
[521.40 → 526.98] I'm sure everyone has their own take on open source but generally for me, I feel like the people who
[526.98 → 533.62] contribute are solving very particular issues um whereas like road mapping and like planning the
[533.62 → 540.28] scope of a project it's very much like uh the work of a few individuals um and so, so yeah it's its
[540.28 → 545.16] been great too with integrations like the whole ecosystem has changed since we last talked it's like
[545.16 → 551.76] meteor react all these new you know technologies yeah um and people who know the those things
[551.76 → 558.06] back you know uh very well and sort of you know like having angular integrations and having
[558.06 → 563.20] meteor packages it's been wonderful having the community help with that so we'll, we'll definitely dive
[563.20 → 568.66] a bit deeper into those two nuances there that uh that you brought up but for those who haven't
[568.66 → 575.56] listened to episode 106 which is at changelaw.com slash 106 for those who haven't listened to that
[575.56 → 580.90] can you give the one-liner about what semantic UI is before we kind of dive deep into the what's the
[580.90 → 591.82] why isn't the how's yeah sure um so uh naming is arbitrary um semantic UI tries to give uh conventions
[591.82 → 598.48] based around natural language for um parts of the website um, so these aren't things that are part of
[598.48 → 604.26] the w3 spec these are things that are part of sure what the user community has you know begin to call
[604.26 → 609.92] things so the idea of a sidebar um which is like a know an off-campus navigation that appears
[609.92 → 617.42] um that that concept didn't exist 10 years ago um the w3c can't really adapt to create a standard
[617.42 → 625.44] around that um and so my goal is to sort of create um working standards for you know people who want to
[625.44 → 630.70] use this kind of components but um don't really want to you know create their own you know from
[630.70 → 636.40] from scratch yeah, so this is a lot, and maybe we'll get more into the details here as we go on but
[636.40 → 640.64] I'm kind of going back jarred you said you went back and listened to 106 and i kind of purposefully
[640.64 → 645.74] didn't either that or I'm lazy one of the two uh to go back and listen to it because I was there i
[645.74 → 653.72] you know, and you weren't so you know there you go but nonetheless um it seemed to me like semantic UI
[653.72 → 663.34] was a bit more focused on uh being a implemented standard versus a framework itself is that easy is
[663.34 → 672.38] that somewhat uh the idea so just I'll go back into the linguistic roots of it here is this is what's
[672.38 → 678.06] personally interesting to me and sort of why you know why I'm obsessed with this idea is I think
[678.06 → 681.96] there's a fundamental difference between programming languages and natural languages and I've been trying
[681.96 → 687.32] to sort of figure out um in what aspects are programming languages better at constructing meanings
[687.32 → 692.44] and what aspects are they worse at constructing meaning than the natural languages um, and so I think
[692.44 → 698.68] there 's's sort of a schism between um meaning as constructed for computers which um involves
[698.68 → 706.26] databases um you know memory uh different uh, uh constructs for computers and then there's meaning
[706.26 → 713.94] for people um and so uh the way I see it currently is that uh things that have to do with presentation
[713.94 → 722.20] uh markup languages are in a unique uh position because they benefit most from uh these uh features
[722.20 → 729.08] of natural language, so humans are cognitive misers you know we've spent uh between 50 and 100 000
[729.08 → 737.04] years evolving language to um use the least amount of sounds you know to construct the most meaning
[737.04 → 743.16] um, and so I'm fascinated by that like you imagine if we had 100 000 years of computer science history
[743.16 → 750.52] what that would mean um and so uh for me, it's its trying to sort of work through um what those features
[750.52 → 755.68] of natural language are that are useful and how they apply to programming languages so uh in terms
[755.68 → 763.28] of presentation websites are kind of like virtual scenes they're things on a page um they're uh HTML is
[763.28 → 769.34] unique in the sense that it is fits very well into this natural language system uh for describing things
[769.34 → 774.64] it's like um you might have three buttons on a page there might be three large buttons you have this
[774.64 → 782.16] concept of uh noun modified relationship the largeness is shared between three buttons um plurality like
[782.16 → 788.14] you don't need to say there's a button and a large button and a large button you understand um
[788.14 → 794.96] very clearly um and in programming we have this idea of classical inheritance classes of things but we
[794.96 → 801.32] don't necessarily break it down into the same nuance that natural language does where um words are classes
[801.32 → 807.42] of things like to me the idea of a word and a class is the same thing um but in English and in it
[807.42 → 812.88] basically every natural language there's an idea of a significant word order so for instance like
[812.88 → 823.84] if I say uh three large men versus um you know uh sorry excuse me this is a bad example if I say um
[823.84 → 830.70] in terms of a website um a right aligned left floated column you understand that right refers to the
[830.70 → 836.66] alignment and left refers to where the column sits on the page um whereas when we look at classes in
[836.66 → 843.64] HTML um everyone's used to just saying well left means this and right means this well, well in
[843.64 → 850.68] English it doesn't actually have a meaning it only has meaning in context of uh other classes um and
[850.68 → 856.40] so this is what I'm really fascinated with is sort of trying to reverse engineer this amazing system
[856.40 → 861.74] for constructing meaning which we have in natural language um so things that are interested in the
[861.74 → 867.68] library it's like that that exact example actually plays out um where uh certain class names have
[867.68 → 874.26] meaning only in relation to its position in uh in terms of word order so for instance you could have
[874.26 → 881.38] in the grid system um a right aligned left floated column, and it understands because you put right
[881.38 → 885.76] before the word aligned you didn't mean right floated, or you didn't mean you know write something else
[885.76 → 894.20] um you meant you know this particular concept um so yes it's its kind of obviously this is a
[894.20 → 899.58] very nascent field like this is something that people will be expanding on for you know decades to
[899.58 → 906.44] come um but I'm I'm really excited to sort of explore it more and try to really um you know reverse
[906.44 → 913.52] engineer um language so you've had um roughly a year and a half since the previous show I think you're
[913.52 → 921.38] like 0.3 at the time to watch it evolve a little bit and so could you take us uh from then to now
[921.38 → 926.90] the evolution of semantic UI and then kind of prognosticate a bit where do you see an end goal
[926.90 → 937.96] or a future end of the road looks like for a project like this sure um so yeah so when we talked last
[937.96 → 946.60] um the project was a pure CSS library um there was no pre-processing um when I launched 1.0 one of
[946.60 → 953.72] the things I realized is that all these concepts you know largeness redness um are uh represented by
[953.72 → 959.58] uh variables there are things that you know a user wants to find what largeness means to me or what
[959.58 → 965.76] redness means to me in the context of you know certain elements, and so I built this library out
[965.76 → 975.64] and you know internally it ended up being I don't know 3 000 plus uh CSS variables so very, very large
[975.64 → 985.70] amount of things are um uh arbitrary in sort of definitions um so right i sort of worked back
[985.70 → 991.72] from that um I created an inheritance system where I was really fascinated with sublime text at the time
[991.72 → 995.44] and it was one of those things that sort of came out of the ether like I don't know if you remember
[995.44 → 1001.42] when sublime text was coming out, but it was like what the f is this like this is insane who is this
[1001.42 → 1007.60] genius and why does he have no twitter followers and I was fascinated by this concept, and he still
[1007.60 → 1013.58] doesn't he just exists as this like mad genius that like doesn't want to be in the limelight and I was
[1013.58 → 1018.56] and it's obviously the best thing for um you know text I mean there's other choices Adam and so on but
[1018.56 → 1027.80] it was so, so good that it was insane at the time um and for me like I'm in terms of all
[1027.80 → 1035.98] types of of of uh art and literature I'm into these people who sort of create without a concept of ego
[1035.98 → 1042.40] they just do it because they have some idea, and he was like he was one of my idols um, and so I was
[1042.40 → 1047.82] looking at sublime text, and they have a very you know simple package system that just perfectly makes
[1047.82 → 1053.64] sense it's you know there are three levels of inheritance there's you know a user settings file
[1053.64 → 1060.62] there's the package defaults and then there's just the defaults for sublime text, and it seems
[1060.62 → 1065.62] ridiculous but I was just like this is so easy like why doesn't everything work off this um, and so I've
[1065.62 → 1071.56] looked at lots of different inheritance models for CSS, and you know sass and less everything is
[1071.56 → 1076.24] just like floating in this global namespace where it's like you if you define red later in the file
[1076.24 → 1083.68] it is actually like changes the know the red variable uh you know uh, uh anywhere else in
[1083.68 → 1089.34] that compilation so it's it was a very um basic sense of inheritance, and so I tried to sort of
[1089.34 → 1094.66] reverse engineer this sublime text inheritance model um and I came up with this system that works off of
[1094.66 → 1102.00] um a default theme a package theme and then a site theme um and so you know you have browser default or
[1102.00 → 1108.16] sorry library defaults which are very neutral just sort of how the um the UI components look um then
[1108.16 → 1113.66] you have this concept of a package theme which is like the hypothetical as you're saying you know the
[1113.66 → 1119.14] future of the library um if there's a package uh manager then you can download you know the GitHub
[1119.14 → 1124.08] button let's say it looks like a GitHub button um, but then you have this third level which is like
[1124.08 → 1127.70] well great I download that package but I still have some things I want to customize
[1127.70 → 1133.20] um and so there's a third level which is like a site theme so it's basically like a user override
[1133.20 → 1138.32] you know I've downloaded this theme I've overrode the default theme but I also want to add my own
[1138.32 → 1145.96] you know um my own colours, or you know other variables um so yeah so i I have launched 1.0
[1145.96 → 1153.74] it was built off of these you know massive amount of of of theming variables um and this three level
[1153.74 → 1159.54] inheritance system um, and it was I was happy with it, but it was also one of those things that
[1159.54 → 1164.12] feels like that pyrrhic victory where you like you finish it, and then you're like oh I did it and
[1164.12 → 1167.94] you're like you do like your little dance in your room um, and then you launch it out in the world and
[1167.94 → 1176.22] you just wait you know yeah, and it's hard because like you know these open source is one of those
[1176.22 → 1180.20] things where I feel like people don't discover it until they have a new project they have like
[1180.20 → 1184.50] you know they lift their heads up they have the thing they're used to, and then you have to convince
[1184.50 → 1190.52] them of something they've never heard of, and it's like it's a difficult proposition um and so uh so
[1190.52 → 1198.86] yeah so one point i was really happy with um around that time um I actually went back to
[1198.86 → 1206.66] um working on semantic UI full-time um so previous to that um I had a and this is going back into the
[1206.66 → 1213.26] personal life but um but i was working uh as an uh consultant for uh this magazine the new
[1213.26 → 1220.06] republic um so it was a great place to test out the ideas of what a framework would look like
[1220.06 → 1225.92] this would look like um and sort of you know helped evolve the standard for 1.0 um but then sort of when
[1225.92 → 1234.82] 1.0 launched i kind of went full tilt into the um doing it for doing it aspect and uh yeah i sort of
[1234.82 → 1241.52] gave up the day job and um I've since then I've sort of been working on it um full-time um you know
[1241.52 → 1249.08] without pay um and just sort of enjoying it for you know the ideas um and so yeah that's kind
[1249.08 → 1253.88] of leads me where I am now in our pre-call when jarred and i sort of prepare ourselves for the guests
[1253.88 → 1258.38] uh he was telling me he went back and listened to that episode and one thing that you did say was
[1258.38 → 1262.74] that you started working on it full-time in that episode and that Andrew and i just sort of like
[1262.74 → 1267.74] just glazed over the idea that you just said that you were working on this open source project full
[1267.74 → 1275.14] time, and we just didn't dig in so let's let's dig into that so you've I mean it astounds me
[1275.14 → 1281.78] let's preface this section I guess a bit with the fact that there's so much open source out there
[1281.78 → 1289.08] that you don't often understand as a user or someone who's just sort of determining what's out
[1289.08 → 1294.60] at their fingertips available to use what kind of sacrifice goes into making something happen
[1294.60 → 1300.24] or the passion like you've talked about jack that you've got for language and simplicity and
[1300.24 → 1303.90] all these different things and how it's played into making semantic UI what it is
[1303.90 → 1310.04] and I feel like you know there's a part of this show that can help uh foster and help explain some of
[1310.04 → 1314.82] the behind the scenes there on the motivations from you the way that you've done it in the
[1314.82 → 1320.18] past year and a half, and it's at your leisure to share whatever personal details you want but
[1320.18 → 1326.28] I think it's an interesting topic to figure out why you're doing it and how you're doing it without
[1326.28 → 1334.94] you know a job yeah no yeah it's just this is something for me, it's its very uh philosophical
[1334.94 → 1342.38] um I mean we live in a western country we have a unique concept of what you know being uh
[1342.38 → 1350.86] subsisting is um and for me, you know I'm a programmer um I've been doing this you know since college um
[1350.86 → 1355.46] and I just realized you know what I actually need is much less than what I think I need
[1355.46 → 1362.20] and the thing that really matters to me is ideas um, and so I've sort of given up on the idea of
[1362.20 → 1369.44] of pursuing the most profitable you know direction and I've gone just towards trying to
[1369.44 → 1375.44] uh cultivate the ideas that mean most to me and I know that sounds like I really hate even
[1375.44 → 1380.78] saying that out loud because it sounds terrible but for me, it's just you know I've my last paycheck
[1380.78 → 1387.20] was last July so I'm going on about a year now um it's one of those things where I like
[1387.20 → 1394.50] i I just imagine myself you know later in life and thinking there was this period of my life where
[1394.50 → 1401.38] um I had the most potential to do something and the idea of using that potential to
[1401.38 → 1408.70] you know and startups are wonderful, and you know they add much value to the world but for me to use
[1408.70 → 1413.82] that potential to you know help uh optimize the profit margins of a startup is not necessarily
[1413.82 → 1419.86] um the best way to use your best years and I mean this is obviously a very personal decision but
[1419.86 → 1424.74] for me, I was just really excited about um going down that rabbit hole and I think a lot of people
[1424.74 → 1430.36] this is actually for me fascinating my girlfriend's a librarian and I see there's
[1430.36 → 1434.94] a whole other type of world where people just make decisions all the time not based on money they
[1434.94 → 1442.42] just make decisions based on um morals or values or other things and I think programmers they're like
[1442.42 → 1447.62] they're so good at what they do that they're able actually to cover this up really well
[1447.62 → 1453.54] but I think that they're generally programmers are making decisions based on optimizing uh utility
[1453.54 → 1460.38] and optimizing for value and I'm you know I've tried not to do that, and it's its brought me in
[1460.38 → 1464.48] this sort of you know weird place where it's a year down the road and I'm like you know I had whatever
[1464.48 → 1470.64] savings there is, and it's been eaten through um but i I could not imagine wanting to do it any other
[1470.64 → 1476.44] way you know the I think also it's when you think about how many open source projects there are in the
[1476.44 → 1481.06] world, and you know people approaching it from different directions it's the thing that I'm
[1481.06 → 1490.50] really wary of is I mean there are startups that use open source as part of a marketing campaign
[1490.50 → 1499.36] and sort of part of hiring developers or like evangelizing a platform and i I think it has
[1499.36 → 1504.84] you value when the ideas are so good that they can't be disputed like react everyone's like this is too
[1504.84 → 1510.10] damn good like this could have come from like any company, and we would still be using this but um
[1510.10 → 1517.78] but it's i I find it kind of disparaging when open source is not necessarily used to you know promote
[1517.78 → 1525.70] uh independent ideas but more to you know promote uh agendas of uh of startups or software companies
[1525.70 → 1532.04] um and i obviously this is a very polemic issue I mean i have lots of opinions here but
[1532.04 → 1537.48] I'm sure there 's's lots of different opinions here but for me, it's i I really enjoy
[1537.48 → 1543.98] like i I have different maintainers that I'm like i I really like who I know have a certain following
[1543.98 → 1550.34] or you know, but they just do it um in perpetuity without like any sort of like pat on the back
[1550.34 → 1556.30] um and I've like I've always been fascinated by that and also like looking back at literature and
[1556.30 → 1560.18] looking back at the things that really you know I enjoyed in my life in terms of other people's
[1560.18 → 1567.88] creations I think it's those people who get to uh who create without like uh expectation that
[1567.88 → 1573.54] they will immediately be understood um and I don't necessarily think that obviously all these
[1573.54 → 1578.36] things are very loaded terms because you know I'm talking in the context of being interviewed on a
[1578.36 → 1583.94] program but like just in terms of inspiration like just talking about other people that those are the
[1583.94 → 1589.14] people who most inspired me um, and so I've been trying to sort of pursue that that idea of programming
[1589.14 → 1594.48] and you know whether I succeed or fail is kind of you know our code I guess
[1594.48 → 1601.82] yeah I mean I think uh I see I definitely see some of your points I think that you know innovation can
[1601.82 → 1609.72] come from many different areas and uh it's a spectrum and people do open source for different reasons
[1609.72 → 1618.22] um some purer than others and yet at the end of the day I think what we like about software especially
[1618.22 → 1627.52] open source software that we can all see and inspect and use and contribute to is that and maybe this is a
[1627.52 → 1634.66] romantic thought but at the end of the day it does speak for itself like the product right
[1634.66 → 1641.00] regardless of you if you're a Facebook you know, and you're with react, or you're you know jack music
[1641.00 → 1648.32] who's who's working on semantic for free you know without any income at all like your project is gonna
[1648.32 → 1654.86] succeed or fail to a large extent on you know its value proposition and so there's this great levelling
[1654.86 → 1662.42] uh that happens that being said as uh DHH said quite often in our show with him that you know
[1662.42 → 1666.86] marketing has a big aspect of it and there are plenty of other factors but yeah there is kind of that
[1666.86 → 1675.74] romantic utilitarian you know meritocracy aspect of open source and um you're taking definitely a
[1675.74 → 1682.40] different angle than many people take at it um so just to borrow a startup term what's what's your
[1682.40 → 1691.26] runway look like uh, uh yeah you got in trouble jarred no, no he wasn't expecting that one
[1691.26 → 1697.08] I actually was not expecting that one and the runway is you know there's when
[1697.08 → 1701.30] a startup would fold and then there's you know when a person would fold and for me, it's
[1701.30 → 1707.00] you know I don't I don't know if there is a runway it's I'll be doing this for the rest of my life
[1707.00 → 1712.08] because the idea is important to me whether it succeeds as a project will probably be decided
[1712.08 → 1721.88] soon um but you know it's its uh it's about ideas and like for even like the ideas that are
[1721.88 → 1728.48] kind of like unpolished and unrefined will eventually come around in terms of new projects and sort
[1728.48 → 1733.72] of different endeavours and that's obviously semantic wise and I mean I know I'm saying this at the same
[1733.72 → 1739.76] time I'm like top 20 job script project top 35 overall of any language in GitHub it's its it's succeeding
[1739.76 → 1744.66] all right and I'm very happy with the community and the community is amazing um but other than that
[1744.66 → 1752.56] um you know it's yeah if is for some reason it, it needs to you know be evolved in a new way then it
[1752.56 → 1758.90] will evolve like it's for me the thing that's important though is just you know the underlying
[1758.90 → 1764.74] ideas um and just sort of new way of thinking about programming and kind of relating programming back
[1764.74 → 1769.46] to natural language and I think also it's hard too because like once you have a name to something
[1769.46 → 1773.18] and you like to call it like this set of ideas that I've been talking about programs now called
[1773.18 → 1778.74] semantic UI like it'd be much easier for me to talk about it if it was just a set of ideas but as soon
[1778.74 → 1784.40] as it's like this is now a project that people can choose to like or not like star or not star
[1784.40 → 1791.84] follow or not follow it like adds this whole sense of like uh attachment and uh you know it puts you in
[1791.84 → 1797.80] the realm of uh of all these things which are harder to deal with this which is like you know
[1797.80 → 1803.38] self-concept and you know fitting into a marketplace and well since you mentioned the
[1803.38 → 1809.60] the stars and stuff could can we mention the stars that you got there you got 18 473 as of right now
[1809.60 → 1820.58] at least 18 473 stars and 2013 forks and 967 people watching this thing so it's like you said it's in the
[1820.58 → 1827.26] top 25 I didn't go and look at the indexes, but it sounded like CSS and JavaScript and the top 25
[1827.26 → 1833.54] on GitHub for those so it's its fairly popular yeah I mean it's nice to see like I don't remember
[1833.54 → 1836.88] the exact rankings but I remember there's like there are some libraries that I really respected
[1836.88 → 1841.94] when I was getting in the range of you know, and also it's interesting to think about there 's's
[1841.94 → 1846.28] lots of funded open source libraries now like you look at meteors last round they raised from
[1846.28 → 1851.04] injuries and Horowitz um, or you look at you know ionic or other frameworks which are wonderful
[1851.04 → 1856.90] projects which I love um but the caveat being that they have a bankroll now, and they can make
[1856.90 → 1862.78] decisions understanding they can, you know bankroll developers um and those people like that's almost
[1862.78 → 1867.20] what it takes to get into that ballpark like once you get into the top 20s it's like you look around
[1867.20 → 1873.66] it's people who are bankrolled at Facebook people are bankrupt uh bankrolled at Google um and vested
[1873.66 → 1880.08] startups um and so as this as you know doing the old source model the old model of like just doing
[1880.08 → 1884.12] open source development and GitHub issues and this kind of stuff it's really hard to make traction once
[1884.12 → 1890.60] you get to that point without like having you know some sort of juice so to speak juice so to speak
[1890.60 → 1895.30] exactly let's talk about that for a second because something that stood out to me that you just said
[1895.30 → 1900.38] was you said the fate of this project will be determined soon when jarred asked you about runway
[1900.38 → 1904.82] you sort of chuckled about your own personal runway, and it was mixed it was like there was a little
[1904.82 → 1908.68] bit of your own personal runway and that was indefinite because you said that this is really
[1908.68 → 1912.82] passionate to you and you're going to keep doing it, but then there was another side of it that
[1912.82 → 1918.06] you said the fate of this project will be determined soon can you talk a little bit about like
[1918.06 → 1922.78] what that what you meant by that what there was there some background meaning behind that
[1922.78 → 1931.54] yeah sure um so yeah it's its 2.0 you know I was really excited about 1.0 it was one of those
[1931.54 → 1938.16] things where I launched into the world, and you know had no concept of of of money at the time I was
[1938.16 → 1943.82] just sort of you know eating through savings and being okay with it um and yeah 2.0 is out, and it's
[1943.82 → 1948.32] six months of work I mean I know it's really hard to like to explain what that means but like literally
[1948.32 → 1954.82] just me going to an office for six months and working um full-time um, and it's getting to a
[1954.82 → 1962.58] point where um you know just to have the project uh continue on their needs to be some sort of uh
[1962.58 → 1969.18] uh way to make it sustainable um, and you know I tossed around the idea of a kickstarter and i just
[1969.18 → 1973.62] sort of felt really awkward about that concept of like because we already have a product it's not like
[1973.62 → 1978.76] I'd have to you know get people to bankroll a future product um and so yeah I'm just I'm trying
[1978.76 → 1982.54] to figure out a more sustainable way to do it I've asked people for donations in the past and
[1982.54 → 1988.34] by the way I want to call out how amazing the community is like I've at launch I had like a
[1988.34 → 1994.44] 250 donation like last few months I've had you know between 500 and 750 bucks in donations per month
[1994.44 → 2000.88] people have been really amazing about that um and I think also that's part of like when people
[2000.88 → 2004.50] understand when you have a community that understands kind of what you're doing like
[2004.50 → 2010.76] um in terms of you know not having any money coming in and working on a project like this they're
[2010.76 → 2016.14] really eager to help and I think that's the part that's like been really sobering about all this
[2016.14 → 2022.22] is that like even if you don't charge for anything like people understand that there's some
[2022.22 → 2027.76] sort of social responsibility to open source like that things don't just exist in ether um and I think
[2027.76 → 2033.20] when we talked last time like get tip was just coming out um and I think yeah it's its it's been
[2033.20 → 2040.32] really nice to see that um but yeah I guess in terms of what you specifically asked um I think I'm
[2040.32 → 2044.62] going to have to find some so a new financial model for the project if it's going to uh you know continue
[2044.62 → 2049.86] with the development that it has had previously um because you can't just not work for multiple
[2049.86 → 2057.48] years um living in a city like New York no, no absolutely I mean and i kind of i kind of wish we got a bit
[2057.48 → 2062.00] more of how you've done that and why you've done that out of there I don't want I'm not sure
[2062.00 → 2068.80] we've got some of the topics we want to hit up but um, and we got a sponsor break to do here in a
[2068.80 → 2073.90] second I'm almost tempted just to dive a little bit deeper into the the money situation
[2073.90 → 2080.02] because jarred you referenced 145 with David we talked about financing open source, and he's very against
[2080.02 → 2086.78] getting paid to open source and so jack is the exact anti dh8 so to speak in terms of getting paid to
[2086.78 → 2093.28] open source, and it's this full-time thing so you know there's Patreon getup was there what is it
[2093.28 → 2098.58] called now jarred there's a new version it's a new name for Gratian I mean have you been using that i
[2098.58 → 2104.72] saw flatter on the README yeah so is that the primary way that people have been helping you finance
[2104.72 → 2111.46] this so that you don't have a full-time job, and you can work on the full-time I wish i I feel like
[2111.46 → 2116.36] I am one of the more well-funded product or projects like in terms of the community giving
[2116.36 → 2123.40] back, but you know 500 a month is wonderful like it really helps but in terms of like being able to
[2123.40 → 2130.64] you know live long term yeah my rent is double that right you know my I have to eat food too so I'm like
[2130.64 → 2140.10] you have to eat what yeah I thought there was like a repo you can fork and eat that or something
[2140.10 → 2145.76] like that all right well lets this may sound uh tongue-in-cheek but seriously have you considered
[2145.76 → 2153.46] moving uh i the travelling aspect really helped with that like uh you know cost of living in
[2153.46 → 2158.90] Thailand or something it's so cheap but the girlfriend sort of makes it hard now
[2158.90 → 2166.26] yeah there's the road yeah all right well let's let's go ahead and use that as a chance to
[2166.26 → 2169.98] go ahead and pause and let's put a sponsor when we get back we're going to talk more about adoption
[2169.98 → 2177.68] uh we'll begin with uh you know how you adopt or how you begin to use semantic UI and then
[2177.68 → 2183.66] but we're curious to know who out there is using semantic UI you mentioned possibility of
[2183.66 → 2188.60] of users, so sometimes someone adopts it and starts to use it, and then they actually give
[2188.60 → 2192.48] back financially to it but let's go ahead and break, and we'll come back we'll talk about that
[2192.48 → 2198.30] all right put them away put them back put the books back on the shelf you don't need them
[2198.30 → 2206.62] and learn to code by doing with code school offers a variety of courses JavaScript
[2206.62 → 2216.14] HTML CSS ruby iOS git and many more to help you expand your skills and learn new technologies
[2216.14 → 2221.96] code school knows that learning to code can be a daunting task, and they've combined experienced
[2221.96 → 2227.62] instructors with proven learning techniques to make coding educational and memorable it gives
[2227.62 → 2232.50] you the confidence you need to continue past those rough tough hurdles that you will definitely face
[2232.50 → 2238.08] learning the code school also knows that languages are a moving target they're always updating
[2238.08 → 2242.92] their content to give you the latest and the greatest learning resources you can even try before
[2242.92 → 2249.60] you buy roughly one out of every five courses on code school is absolutely and totally free this
[2249.60 → 2256.42] includes instructor classes on git ruby jQuery and much more which allow free members to play full
[2256.42 → 2263.34] courses with coding challenges all included you can also pay as you go one monthly fee gives you access
[2263.34 → 2269.26] to every code school course and if you ever need a breather take a break you can suspend your account at any
[2269.26 → 2274.64] time don't worry your account history your points your badges they'll all be there when you're ready
[2274.64 → 2280.30] to pick things up again get started on sharpening your skills today at code school.com once again that is
[2280.30 → 2290.34] code school.com all right we're back, and now it is time with jack to dive a little bit deeper to figure out
[2290.34 → 2296.94] two things here one how do you use or the other word we can use is adopt how do you adopt
[2296.94 → 2302.80] semantic UI how can you begin to use it is it and the question jarred's got here is it all in or is
[2302.80 → 2309.50] it toes in the water how does it work right um so going back to the analogy of sublime text I'm sure
[2309.50 → 2314.12] like everyone has their first sublime text experience um so you download this new editor you're like what
[2314.12 → 2322.56] the hell is this um so for semantic you know it's NPM install semantic um the NPM is sort of I don't
[2322.56 → 2327.50] know how you feel about this but for me Bauer and other package managers are kind of on the way out
[2327.50 → 2334.20] in terms of uh managed dependencies NPM is uh is sort of the go-to point um one of the things that's
[2334.20 → 2339.56] wonderful about using NPM is that we have an interactive installer which kind of feels like
[2339.56 → 2344.66] installing one of those like adventure games when you're like 12 years old yeah basically yeah so it
[2344.66 → 2350.02] asks you questions it's like you know are you a right to left user you know do you need to choose
[2350.02 → 2355.14] which components you want to use um and so on um one of the things I'm actually really excited about
[2355.14 → 2361.92] adding in 2.1 is had you guys are you familiar with purify CSS just by name but not the details
[2361.92 → 2367.88] sure so the thing that like the first feedback I always get on having a monolithic UI framework
[2367.88 → 2375.18] is everyone's like that's great but like what if I just need one button what do I do and uh my answer
[2375.18 → 2379.92] previously was just like well just choose from the interactive installer button but my
[2379.92 → 2385.72] new answer is in 2.1 I'm going to be including purify which basically what it does is it goes
[2385.72 → 2391.86] through your HTML and your JavaScript and looks at what you actually use and then changes the CSS to
[2391.86 → 2397.98] only include CSS that is used in your HTML so you know if you want to use semantic you don't have to
[2397.98 → 2404.30] like worry about this you know 700 kilobyte download you can just you know specify your output you know
[2404.30 → 2409.90] your HTML folder, and then it'll go great well whenever you start using a new class name in HTML
[2409.90 → 2415.92] then we'll just add that class name to the CSS how does that work across dynamic pages just
[2415.92 → 2422.28] yeah I thought the same thing until I went to the repo and I was like wow it works yeah it just
[2422.28 → 2426.40] works its magic it's like it's some special magic that someone the open source community created
[2426.40 → 2432.40] this voodoo magic on their README so yeah that's better than auto magical which I was never a fan of
[2432.40 → 2439.00] that term but voodoo magic sounds pretty rad yeah um so back to the sort of the overview so you install
[2439.00 → 2446.26] it on NPM um it asks you questions what components to use um, and then it goes into a folder um with a
[2446.26 → 2453.12] you know it has basically two folders a CIRC folder like a source folder and a dist folder which is the uh
[2453.12 → 2459.34] the CSS you actually include in your page um and so the way it works is kind of like sublime text where
[2459.34 → 2464.40] you know you download a package, and you're like well my I like two spaces for indents instead of
[2464.40 → 2471.96] four and so you open up a file that's um a user file um in terms of semantic it's you know CIRC
[2471.96 → 2478.18] slash site slash uh global slash site variables and so you open that up, and you say well I want
[2478.18 → 2485.24] you know red to be this colour um and then the uh the build tools that are um built into the
[2485.24 → 2493.40] project um compile uh any change that happens, and then you know changes the uh the output uh CSS to
[2493.40 → 2499.22] sort of match your changes um so it's if you're familiar with bootstrap or foundation it's like
[2499.22 → 2504.82] that but instead of it being you know I just import this library and just start writing like override
[2504.82 → 2512.64] variables it's a more structured um uh system um which I think actually benefits projects because it
[2512.64 → 2517.42] means that you know if you want to start a new project, and you have you know all these defaults
[2517.42 → 2522.78] already set then you don't have to worry about like cutting and pasting parts of a CSS file that
[2522.78 → 2528.76] have to do with you know a menu or a button you actually have a dedicated file to that um and so i
[2528.76 → 2534.16] think this is for me this is a huge thing for uh HTML develop for front-end developers is to start
[2534.16 → 2540.62] thinking in terms of UI like when you're customizing a menu or a button like put that in a special file
[2540.62 → 2546.62] called button you now and then realize that when you're going to a new project um that you need to
[2546.62 → 2552.74] you know take those particular changes and if you want to reuse a button then you know it's there so
[2552.74 → 2557.66] yeah it's its a new it's kind of a more fragmented approach which I think people have a hard time
[2557.66 → 2561.42] getting used to at first because they want everything to be in their like monolithic you know
[2561.42 → 2568.10] uh index.css file or whatever but uh but once you get used to separating it I think it really helps
[2568.10 → 2573.06] you in the long run um and it sort of makes it very easy to you know create new projects
[2573.06 → 2579.98] so it does sound like it is an all-in thing, but it's going to strip out the stuff that you're not
[2579.98 → 2585.44] using so it's not like you get all the weight of yeah all the components that you don't necessarily
[2585.44 → 2591.46] use and there's individual repos for each uh component so if you're just like I just need a
[2591.46 → 2597.02] drop and I'd rather use your select drop-down than you know um another one then you can just
[2597.02 → 2604.20] you know NPM install semantic dash UI dash drop down, and you got that so, so yeah it's basically
[2604.20 → 2608.64] here's one of the things that I've had actually a really huge issue with which I would be interested
[2608.64 → 2614.14] in you know talking more about is that as open source developers it's like you have this idea of
[2614.14 → 2618.44] you have an opinion idea of how people should use a project which for me is this like inheritance
[2618.44 → 2624.26] system, but then you just have how people actually use a product um and so you have people who use
[2624.26 → 2628.30] angular people use ember people use meteor right um all of them have their own package managers
[2628.30 → 2633.30] um you have you know people who just want to use browser, and you're like whoa everything is
[2633.30 → 2639.14] compiled like you know from NPM dependencies and all of those are different packages with like different
[2639.14 → 2644.78] you know metadata like different you know things to manage um and what's really fascinating to me is
[2644.78 → 2649.58] like trying to be a developer who has like this is how I think you should use it but at the same time
[2649.58 → 2656.80] I'm just one dumb idiot in a room and if you want to use it like in you know another way then here's
[2656.80 → 2661.30] another way to use it so yeah it's been fascinating the community's been really you know
[2661.30 → 2666.40] wonderful with that where like I've I personally have never used ember but the guys who manage the
[2666.40 → 2672.06] ember integrations are amazing and like have a faster response time than me sometimes with issues
[2672.06 → 2677.74] which is kind of embarrassing but uh but at the same time I'm like wow that's thank you for caring
[2677.74 → 2684.32] about an ecosystem which I have yet to you know dig into so basically is your policy on integrations
[2684.32 → 2689.72] like those are all third-party open source deals or do you have any first-party like integrations
[2689.72 → 2696.76] with any of the popular frameworks or backends you guys are you guys gamers at all uh casual gamer
[2696.76 → 2703.78] my former life, so there was in the Nintendo 64 days there was a game called banjo kazoo oh now
[2703.78 → 2707.82] you're right in the wheelhouse yeah exactly all right so that was what I think it was
[2707.82 → 2713.56] like a second party game which is like um you're not necessarily a third party because like the
[2713.56 → 2718.14] organization that's in charge is like all right rare you're great like we're gonna release and like
[2718.14 → 2723.84] really promote you and that's how I feel with the integrations I'm like it's really hard it's for
[2723.84 → 2729.70] open source developers who like to have a repo hosted on their own like username on GitHub and like
[2729.70 → 2734.18] they're trying to like to promote it so I'm like anyone who I find who's doing a good work with
[2734.18 → 2739.50] you know an integration I try to you know get a semantic org repo and sort of you know promote
[2739.50 → 2744.50] it in the main repo with the README and like integrations docs and so on just so that like
[2744.50 → 2748.38] they understand they're part of a community, and they're like everything that you do has you know
[2748.38 → 2755.20] has purpose and value in terms of you know contributing to a larger good um, and so I think that's
[2755.20 → 2760.84] for me also like that's a hard part to deal with is trying to remember your context in terms of
[2760.84 → 2766.38] community I think like in the pre-show we talked about this like um everything you do in open
[2766.38 → 2770.94] source it's like it's just a commit going into the ether and so you have to understand like where that
[2770.94 → 2777.08] commit fits into like the people who are using that library like the know the other people who
[2777.08 → 2784.42] have dependencies on your project who you know add on to it um and so for me, I really want to like
[2784.42 → 2788.56] make sure that people understand that when they like to take the time to make you know a WordPress
[2788.56 → 2793.38] integration or something like that that may not get you know a massive amount of stars on GitHub that
[2793.38 → 2798.82] they're still doing perfect work and that like they need to you know feel some praise and like
[2798.82 → 2805.16] yeah some like pat on the backs from that so on that note the examples I think I've found
[2805.16 → 2812.90] paging back through the org here's like semantic UI CSS semantic UI less uh and then keeping that same
[2812.90 → 2818.96] prefix you got meteor data beta docs amber angular is that what you mean when you
[2818.96 → 2823.28] talk about the integration oh yeah yeah completely and I think it's this is one thing that I'm
[2823.28 → 2829.94] since we last talked I've started to understand more is that like once you just like to put that team jersey
[2829.94 → 2834.94] on someone you're like all right we're you're part of the team now and like here's this official repo
[2834.94 → 2841.54] like suddenly they understand that like you know their work is valued like there's this community that
[2841.54 → 2847.00] will appreciate everything they do and I think like that's that's such a wonderful transformation
[2847.00 → 2852.72] for me, it's like just watching people like to go from like this is my first time you know contributing
[2852.72 → 2857.92] an integration to like I'm in the maintainer of this official integration that's like other people
[2857.92 → 2864.04] are depending on and that's like that's really powerful what uh on that note what overhead is it for
[2864.04 → 2869.36] you because it seems like you're giving a lot of the onus on to whomever really cares about it
[2869.36 → 2874.60] what friction is it back onto you and the rest of the organ uh the contributors to the main
[2874.60 → 2878.30] repo and how does it kind of tie into the main repo and the build process and whatnot
[2878.30 → 2884.70] yeah I mean it's hard to like to channel the right issues back to the right place like meteor is a really
[2884.70 → 2891.00] popular integration now and meteor is taking off like crazy um, but you know there 's's a whole
[2891.00 → 2895.48] new pipeline for how people build with meteor like they have to have a special Jason file that like
[2895.48 → 2900.76] defines you know which components to use and the maintainer of that project sort of decided the
[2900.76 → 2905.68] the setup for that um, and you know when that's not working you know it's hard for people to
[2905.68 → 2912.32] differentiate between what's a semantic UI problem and what's like an integration problem um but I mean
[2912.32 → 2917.60] for me, it's gravy because like any of this is you know it's a whole new community of people who
[2917.60 → 2923.78] wouldn't have used have uh used the product who are now like getting excited about it um yeah it's
[2923.78 → 2930.40] same with like rails or ember um it's just one of those things where like as a developer you
[2930.40 → 2934.30] choose the communities you are involved in, and it's and there are other communities that you know
[2934.30 → 2938.34] are wonderful communities that you just don't have the know the depth of knowledge to be able to
[2938.34 → 2944.14] help out um and just having people have your back with that it's been wonderful I'm here on the
[2944.14 → 2952.36] semantic UI meteor repo and I'm seeing custom.semantic.Jason and this looks a lot like your affinity for
[2952.36 → 2959.66] sublime text and its inheritance that you talked about is that part of the layered uh I guess
[2959.66 → 2967.52] variables that you can settings you can use for semantic UI um yeah is that not part of it
[2967.52 → 2973.68] that's actually I would have to say hey does it not part of it, but it was the guy um uh I know
[2973.68 → 2979.10] him only by his GitHub username, so his actual name was given me flame uh who's the maintainer
[2979.10 → 2985.90] yeah, thank you uh he's been great he has some of the know very popular uh projects on atmosphere
[2985.90 → 2991.94] which is the manager for package manager for meteor um it's a system that he picked up from
[2991.94 → 2999.72] uh the bootstrap uh, uh project on atmosphere which i I think is specifically with the way that the
[2999.72 → 3005.10] files are set on meteor um it's much easier for them to just have a Jason file on the
[3005.10 → 3014.42] the top level that they can set that then triggers um uh the less pipeline to recompile the files
[3014.42 → 3021.14] correctly um you'd have to ask him that's why I asked it seems like it's keying off of what you
[3021.14 → 3023.94] were talking about earlier which is why I thought it was something that was
[3023.94 → 3029.36] part of the official way of doing things no, no you're right I'm being actually a bit of a pedant
[3029.36 → 3034.32] because the actual project has a semantic.Jason file which is basically the exact same thing
[3034.32 → 3040.52] um has a different structure um and that's sort of how people decide what components include
[3040.52 → 3047.24] what the input and output you know okay yeah so everything works off of a configuration file
[3047.24 → 3056.82] um yeah uh in terms of theming um there's a central config file that's like a theme.config file
[3056.82 → 3061.74] um so basically I was sort of describing this three-tiered system before um when you download
[3061.74 → 3067.78] the project all theme config has every component set to default theme um you can just and anytime
[3067.78 → 3072.18] after you download it you can open that file change the theme to you know you can change button to
[3072.18 → 3077.86] GitHub or something or uh site to material um and theming is done sort of per component
[3077.86 → 3084.46] in the library so you may choose to have a GitHub button but a material you know site theme so it
[3084.46 → 3089.06] have all of you know android fonts but then have buttons that look like GitHub and I think this is
[3089.06 → 3094.56] one of the things that for me is really differentiating is that I think theming is really nuanced like
[3094.56 → 3101.62] everything is in terms of UI and when people are like well I just need to make my site you know look like
[3101.62 → 3108.38] a material design well I'm like well a site is a lot of different things like a site is uh you know
[3108.38 → 3114.44] several dozen UI components each with their own you know custom look and feel um and I think that
[3114.44 → 3119.06] once people start to like to think about things that way and like distinguish, and you know in terms of
[3119.06 → 3125.88] their branding um between you know how maybe they want you know a card system that looks like Instagram
[3125.88 → 3131.80] um, but they want their buttons to look like material um and just sort of like being able to
[3131.80 → 3136.54] differentiate that way I think is really important um and I guess that's like the difference between
[3136.54 → 3143.20] bootstrap or uh foundation is like people are in those contexts are just used to loading like
[3143.20 → 3149.92] one master theme file it's like everything across my website is like this um and i I think also like
[3149.92 → 3154.62] for the open source you know component componentized web like you have to start thinking in terms of like
[3154.62 → 3161.22] little tiny things that fit together um and although the library is a big library of little tiny things
[3161.22 → 3165.26] fitting together really it's like it's a bunch of small components like when it comes down to it
[3165.26 → 3168.74] and every time I add to the library it's like it's another thing that you can just say that you
[3168.74 → 3175.16] don't want in your semantic.Jason file so it's like you know it's its it's hope I really hope that it
[3175.16 → 3179.96] doesn't turn into this thing that people are afraid of because they think it's too big um I want to make
[3179.96 → 3185.28] sure that yeah they make the decisions really early on to sort of make it small and limited yeah just
[3185.28 → 3191.56] looking at the uh the home page I mean your theming looks really, really nice um one thought I had
[3191.56 → 3197.02] coming into this is like who's using semantic UI because you know like I know bootstraps out there
[3197.02 → 3202.94] and you know uh in crazy mass, and we see foundation and these other those are the two big ones
[3202.94 → 3211.16] and I was thinking I don't really know any sites using it, but you know as a user of a front end
[3211.16 → 3217.52] yeah nice not knowing um you know yeah as developers we get to a point where I can spot a bootstrap
[3217.52 → 3223.74] uh site a mile away even if it's customized and that's fine most users don't have a clue about
[3223.74 → 3228.62] these things, but maybe it just speaks to the quality of the theming and the person you know the way you
[3228.62 → 3235.30] can personalize it that I don't actually know any sites that are you know semantic UI users um you
[3235.30 → 3241.80] think that's true a and b could you give us a couple examples to look at uh yeah um I mean in terms
[3241.80 → 3249.88] of public examples um it's a bit dicey, but it's being that's kind of new technology like i i I have
[3249.88 → 3254.48] to I've kind of explained like i I get personal emails from people and it's lots of like you know
[3254.48 → 3262.02] we're we have a startup that has gotten you know series a or c funding right, and we're using semantic UI
[3262.02 → 3266.02] um, and we don't have any public facing links yet, but we just want to know you know good job and
[3266.02 → 3271.30] we're hoping to you know the library grows like today for instance i I guess I can say this publicly
[3271.30 → 3277.12] I got an email from someone who is head of Darwin auto saying that they're using it and their internal
[3277.12 → 3282.30] tools and just sort of like uh we can't put this on the GitHub, but you know thanks I probably should
[3282.30 → 3286.42] say this in the podcast actually um, but it was one of those nice things where you're like
[3286.42 → 3295.26] okay, but you know it's its hard because I worry about these things too and I think part of
[3295.26 → 3299.72] of the way bootstrap works is that they're the first I hate to say market they're first to market
[3299.72 → 3306.54] with UI frameworks and they just sort of have a level of adoption that's kind of uh unrivalled like
[3306.54 → 3312.68] they're the most popular uh project on GitHub like in terms of stars like and I understand that and
[3312.68 → 3318.46] part of me understands that that's because UI is a huge problem that people like are really concerned
[3318.46 → 3325.76] with solving um and so that's kind of gives me ample you know uh fodder for wanting to grow up
[3325.76 → 3331.38] semantic UI into a really you know wonderful alternative for people who um oh
[3331.38 → 3336.10] and by the way I don't know how I didn't mention this the entire time semantic uh semantic UI 2.0 is
[3336.10 → 3342.58] all flex box so if you're like you're tired of bootstrap with its old you know floats for grids
[3342.58 → 3349.00] it's a flex box grid it's flex box components um it's based on em like very modern new things um
[3349.00 → 3353.70] which I think people who are making websites for you know IU 10 and up and you know sort of
[3353.70 → 3359.14] modern browsers are really excited about using on the note of bootstrap and I guess
[3359.14 → 3366.24] you know it's the same idea I guess where you think about an ecosystem where there's some need
[3366.24 → 3372.08] and there's so many fractures so bootstrap foundation, and you know all the other ones that sort of fall
[3372.08 → 3377.78] online there you know I'm kind of curious to your motivations of why um, and you said this in the
[3377.78 → 3383.94] pre-call you know working in a vacuum why you continue to be um why you've chosen the route
[3383.94 → 3390.86] you've gone versus folding your brain space your knowledge space into one of these other projects
[3390.86 → 3397.80] and just kind of going off the stars just simply for the numbers' sake you know 18 000 is hum
[3397.80 → 3401.76] 18 and a half thousand for semantic UI and then whenever you go to something like bootstrap you've got
[3401.76 → 3408.72] 82 000 83 000, and they've got like you know way more followers than the changelog I think will ever
[3408.72 → 3416.12] have 346 000 you know almost half a million followers on Twitter you know so yeah curiosity to why
[3416.12 → 3423.06] why uh why you go this route versus folding some of your knowledge space into that since you compared
[3423.06 → 3431.10] yourself to bootstrap when it came to flex box I just have an anecdote actually to explain um I was
[3431.10 → 3437.14] I read the news every once in a while and I'm not wonderful with it but I was I saw that uh north
[3437.14 → 3444.68] Korea announced um that they had a cure for uh most diseases they got a cure for cancer they had a cure
[3444.68 → 3450.76] for um you know balding uh all this kind of stuff I forget the name of the uh the medicine but i
[3450.76 → 3455.12] went to the website that was in the press release for North Korea, and it's like this is a BBC article
[3455.12 → 3460.46] and it's like this miracle product and I'm like I'm looking at the source code I'm like holy crap
[3460.46 → 3467.56] this is bootstrap North Korea uses bootstrap and I had this like moment where I'm like this is
[3467.56 → 3472.44] it in a nutshell it's like there's just entropy in the world like there's there are things that just
[3472.44 → 3477.84] exist because the world is chaotic and just you know selects for things, and you can't really change
[3477.84 → 3482.26] it and i I feel like there are better things and I want to like to take the things which I think
[3482.26 → 3487.98] in my life you know are the ideas that I think are better and just really try to you know uh
[3487.98 → 3492.68] be an advocate for them and sort of support them and push them and for me, it's I think there's a
[3492.68 → 3497.96] we didn't talk about it much in this episode but for me, I think there's a fundamental issue with
[3497.96 → 3504.38] program languages today I think that we're all creating program languages that look like um uh
[3504.38 → 3509.94] what program languages look like in the 1950s and 60s which think of things in terms of like
[3509.94 → 3515.28] baking a cake like here's a sequence of things I need to do for a computer to understand, and we're
[3515.28 → 3521.36] we're missing out on this entire uh different way of seeing language which is your know how we construct
[3521.36 → 3528.90] meaning on a day-to-day which is natural language uh systems of uh, uh grammatical relationships
[3528.90 → 3534.76] um and so for me that's that idea is just so fascinating and so like multifaceted even if I wasn't
[3534.76 → 3538.20] a programmer even if I was like for some reason I was an artist or a writer or something else
[3538.20 → 3542.90] I would just be very excited about exploring that idea of uh the different treating machine
[3542.90 → 3549.08] learning and human learning and understanding um and so I guess that's why I do it
[3549.08 → 3555.86] um but yeah I mean in terms of the practicals I think I'm such an idol I come back to the practicals
[3555.86 → 3559.94] very late in the game like I'm always the last one I'm like oh yeah I forgot I was too busy like
[3559.94 → 3566.16] getting really excited about this new you know thing I was coding, and then you know i think
[3566.16 → 3570.38] it'll get really serious when I like I can't pay my rent or like I have you know some other issue
[3570.38 → 3575.64] but for now it's like it's just trying to chase those things well I have two quick thoughts about
[3575.64 → 3580.56] the bootstrap thing, and then we'll uh go to sponsor break the first one is you know 18 000 stars ain't
[3580.56 → 3586.86] nothing to balk at so you're just fine there secondly you know that band that you found before anybody
[3586.86 → 3593.42] else, and you loved it, and it was your band and then everybody else you know they blew up and then
[3593.42 → 3598.06] everybody else knew about it and you're like oh now it's not my band anymore semantic you I could be
[3598.06 → 3604.46] that band for you, it's still in the phase where you know some people know about it, but you can still
[3604.46 → 3610.00] impress your boss they're not going to recognize it's in that perfect phase where it's time to go out and
[3610.00 → 3615.48] give it a shot is that is I stretching that analogy too far I think that's great
[3615.48 → 3624.00] I wish I was that man a few people have heard it all right 18 000 people yeah well
[3624.00 → 3629.58] at least that's those are the ones who are at least motivated enough to go and star it
[3629.58 → 3634.40] that's right well okay can I just that, but it's still, still pretty have a little plug
[3634.40 → 3641.34] just a really tiny plug sure um we're having a launch party in New York um on the 14th um there's
[3641.34 → 3646.46] an event right on the home page um if you're in New York, and you've heard this podcast, and you're
[3646.46 → 3651.22] excited about talking more I'm going to be there in person um you know it's going to be in blurry
[3651.22 → 3656.38] side I was just talking to the venue owner today it's still TBD but um I'm really excited about it and
[3656.38 → 3662.10] it's nice to like just celebrate open source um you know well that's true so that's the 14th and that
[3662.10 → 3667.76] would be the Monday this show comes out on a Friday which is July 10th so it'll be really close
[3667.76 → 3672.76] to the uh the 14th which is a Tuesday but nonetheless if you're listening to this go to
[3672.76 → 3677.56] cement hyphen ui.com and scroll down just a tiny little bit if you got a big monitor don't scroll at
[3677.56 → 3682.42] all uh, and it says right there rsvp to attend and click that button you go to an event bright page and
[3682.42 → 3690.12] you can use event bright as event bright works nice sounds like a blast let's pause here for a quick
[3690.12 → 3694.10] sponsor break, and we come back we'll ask our awesome closing questions we'll be right back
[3694.10 → 3702.24] hip chat is a game changer for team communication it helps you and your team get the information you
[3702.24 → 3708.08] need faster than email and reduces meaningless meetings teams that use hip chat are able to
[3708.08 → 3715.58] make faster decisions and get more work done with group chat video chat and file sharing hip chat is a
[3715.58 → 3720.22] great solution for distributed teams by letting you take the office with you no matter where you go
[3720.22 → 3728.62] iPhone android macOS it's all there hip chat is easy to use and gets everyone working in real time
[3728.62 → 3735.30] and right now hip chat is offering listeners of the changelog 90 days of hip chat plus totally free
[3735.30 → 3741.44] get premium features like unlimited file storage unlimited message history and guaranteed support
[3741.44 → 3749.82] totally for free for 90 days visit hip chat dot com slash changelog again that's hip chat dot com slash
[3749.82 → 3756.56] changelog get your team started using hip chat plus today go and check them out all right we are back
[3756.56 → 3761.18] with jack Lunik ready to wrap up here, but first we have to ask our awesome closing questions that we
[3761.18 → 3767.96] ask at the end of each show first one for you is what is a call to arms for semantic UI if you have the
[3767.96 → 3772.66] ear of the open source community what are you asking of them in regard to your project
[3772.66 → 3780.10] um are you passionate about UI and you uh you want to work on an open standard for people who
[3780.10 → 3787.58] uh work with UI frameworks come, come join us we're we're not a new framework we're not an old
[3787.58 → 3794.88] framework we're uh the upcoming framework so somewhere in between this is really terrible to use
[3794.88 → 3800.48] jarred's analogy the ban you're about to hear of that's right let's just uh jam that one into the
[3800.48 → 3808.60] ground yeah I liked it I think it was pretty good it seemed like jack was just like I like it though
[3808.60 → 3814.52] I like it, I like it it's its kind of a shame that you invite you know you did the party call out
[3814.52 → 3819.64] before the sponsor break because here would be a perfect call to arms in addition is gone to the party
[3819.64 → 3823.56] July 14th you'll have a blast throw that one in there for you absolutely
[3823.56 → 3830.34] Adam you want to take the next one yeah yeah yeah so what are we going to ask about the
[3830.34 → 3836.02] hero what is the next question have we determined what it's going to be I don't know you got me all
[3836.02 → 3844.36] you got me all mixed up here uh we asked several questions I would think that uh what's on the
[3844.36 → 3849.52] horizon this is a question from a different show that we don't ask too often on this show and we
[3849.52 → 3855.34] got one other question we'll ask you too but what's on the horizon for semantic UI you just went to 2.0
[3855.34 → 3860.72] you're about to have this party next Tuesday if you're listening to this in the real time uh in fact
[3860.72 → 3866.66] it's actually you know a couple Tuesdays from now because we're recording this on July 6th so it's a
[3866.66 → 3871.44] week a week and a day away so what's on the horizon what's something that no one knows about only you
[3871.44 → 3877.06] jack that you know where semantic is going semantic UI is going paint the picture for us
[3877.06 → 3884.66] sure um so theming right now requires some technical sophistication you have to be able to like
[3884.66 → 3891.34] get into the build tools and like open up files um aspiration has always been um and should be
[3891.34 → 3899.60] achieved in the next version which is uh going onto website um being able to customize and uh save
[3899.60 → 3907.54] your UI and then have it in the cloud uh sync it between projects um uh preview it um with you
[3907.54 → 3913.16] know all of the different variations and styles um and yeah and then every time you download semantic
[3913.16 → 3920.22] UI you have you know your uh UI guide that is uh built with it um I think a lot of companies are
[3920.22 → 3928.80] yeah it's like there's like dedicated projects just for that yeah my goal is that everyone can have
[3928.80 → 3935.06] their own Google.com material but with their own style that's fascinating so going back to
[3935.06 → 3940.10] the levels of inheritance with the classes and or not the classes but the different uh
[3940.10 → 3944.88] that would all tie into it, you would have you know the pattern level you would have the user level and
[3944.88 → 3949.98] you would have like semantic UI level oh yeah all play into this style guide that's that someone would
[3949.98 → 3955.64] actually get built on the fly for them with no extra effort yeah completely very interesting register for
[3955.64 → 3961.56] account change some variables maybe choose a preset or two um, and then it generates some sort of UI
[3961.56 → 3967.62] guide for your company which then can be used you know with microsites with in new employees like as
[3967.62 → 3972.56] a brand guide um that's the sort of goal that's so helpful for bringing on new people to front ends
[3972.56 → 3977.88] because I mean it's even it's helpful on both sides the front end bringing on new team members but
[3977.88 → 3984.34] also for developers who are building what the front Enders have defined as blessed you know oh yeah
[3984.34 → 3988.14] because once you get the buy, and you don't want it to change and not that developers have a habit of
[3988.14 → 3993.52] changing it, but they want to just be able to implement front end as best as they can, you know
[3993.52 → 3998.44] and not have to like trip over wires or whatever and if you could provide that guide rail for them then
[3998.44 → 4004.74] that's that's perfect yeah and none of that BTN dash primary it's literally be like red
[4004.74 → 4009.84] button and for I know for me talking to back-end developers like the thing that really works with
[4009.84 → 4014.32] semantic UI for people is like it just clicks like they just look, and they're like my god I can read this
[4014.32 → 4022.34] like a sentence and like it's not like there's no actual uh you know uh learning required like
[4022.34 → 4026.70] it's basically the language I use to you know describe a website to my friends um so that's
[4026.70 → 4030.42] what I'm hoping for people is that they start seeing websites not having to use a separate arbitrary
[4030.42 → 4037.04] language designed by developers uh and that it could just sort of use you know a more uh objective
[4037.04 → 4043.32] um reasonable language awesome that does sound awesome so next question for you and the last
[4043.32 → 4048.24] question is we know you've been a little bit heads down you said you were in a vacuum a little bit
[4048.24 → 4052.60] working on yeah I'm sure you've peaked up a little bit because you knew about react, and you know about
[4052.60 → 4058.32] some other things so uh what's on your open source radar if you had a free weekend and you
[4058.32 → 4062.66] weren't working on semantic UI you want to hack on something what's caught your eye what's what's
[4062.66 → 4068.92] interesting to you um I'm interested in all the React like frameworks that aren't reacted like the
[4068.92 → 4075.24] idea of virtual Dom diffing has this like magic ness to it that I think react solved in a very particular
[4075.24 → 4079.52] way and actually I don't have the name of any frameworks at hand right now but there 's's a
[4079.52 → 4084.78] lot of people working in this space and I'm more excited about not necessarily like what react feature
[4084.78 → 4090.38] is but what virtual Dom future is like what that means as a concept and how it fits into the browser
[4090.38 → 4096.44] um but I mean in terms of if I had a free weekend and what I'd be doing um I'd be embarrassingly
[4096.44 → 4103.72] getting back on my meteor chops because right now it's like my most uh popular uh, uh integration but
[4103.72 → 4109.98] i I am really uh a layman when it comes to understanding the pipeline um so, so yeah that's
[4109.98 → 4115.30] what I'll be doing on a weekend well you uh mentioned virtual Dom diffing I went ahead and
[4115.30 → 4120.98] plugged that into the Google and the Google said that uh there is a repo on GitHub called
[4120.98 → 4130.04] virtual Dom uh it's by Matt Esk, and it's got over 4 000 stars so it's definitely something that's
[4130.04 → 4133.76] up and coming if you haven't heard of that that may be a neat place to start it's a JavaScript
[4133.76 → 4140.26] Dom model supporting element creation diff computation and patch operations for efficient re-rendering and
[4140.26 → 4147.30] it's got quite the support level it's all green from what I can tell uh based on this this this
[4147.30 → 4153.18] image here android Firefox chrome i.e. iPad iPhone opera and safari so that's pretty, pretty exhausting
[4153.18 → 4160.68] in terms of support ie6 yeah gray oh yes of course sure is that is the gray one but hey that's a good
[4160.68 → 4166.70] place to start though so yeah when's it when's that free weekend coming oh man at the end of the runway
[4166.70 → 4172.62] you have to end it exactly just gotta land the plane, and then we'll
[4172.62 → 4179.20] so before we tail off the show then let's let's plug some ways that
[4179.20 → 4186.46] those who've listened to the show have some interest in UI maybe they can contribute maybe
[4186.46 → 4190.64] they can't contribute code maybe they can help with docs maybe they can do any they can't do anything
[4190.64 → 4194.94] whatsoever besides donate their finances if that's something that they wish to do
[4194.94 → 4202.24] uh what's the best way to support financially your endeavours and if there's someone out there that's
[4202.24 → 4210.26] that is a VC or is someone who would support this financially on a bigger scale what's the best way
[4210.26 → 4217.92] for those types of people to get in touch and get involved yeah um so I'll start off on the micro and
[4217.92 → 4222.30] we'll go to the macro, but basically you're not a developer, and you're just interested in some of
[4222.30 → 4229.84] these ideas um we have a big localization team like 800 people uh 30 languages um but even with
[4229.84 → 4235.50] that many people uh many languages are still less than 50 complete um so if you just go to the repo
[4235.50 → 4242.24] semantic org that uh slash semantic UI um there's a link to join our translation community um and that
[4242.24 → 4247.60] would sort of help you know make semantic UI available abroad um one of the things that I'm really
[4247.60 → 4254.94] actually frustrated with that I really need help with um so there's no uh SAS port yet um I noticed
[4254.94 → 4261.66] that repo was empty I was going to call it out yeah so in the README actually I have a link to
[4261.66 → 4267.06] the required pull request there's one pull request that's required for SAS to work with semantic
[4267.06 → 4274.04] UI it's allowing variables inside at import statements so the theming works off of uh dynamic
[4274.04 → 4282.50] uh import statements um if you like SAS uh it's pull request 739 it's in it's in the README
[4282.50 → 4290.70] please help us make SAS support dynamic imports um another wonderful way to contribute our angular
[4290.70 → 4296.04] bindings are still uh coming together if you're into angular there's a link in the repo um and then
[4296.04 → 4304.08] lastly as you said um you know if you're a VC or if you're a angel investor um there is uh if you
[4304.08 → 4312.88] reach out to me directly jack at semantic-ui.com um there's also a tiny microsite investor.semantic-ui.com
[4312.88 → 4318.38] um that just sort of gives an overview of the project and sort of its future can you repeat
[4318.38 → 4324.52] that last URL again uh yeah sure, so the email is uh jack at semantic UI and then the URL is investor
[4324.52 → 4331.88] dot semantic.u.com so it's a subdomain off of your main yeah it's its not mobile friendly so don't
[4331.88 → 4338.60] don't try that, but it was a weekend project a couple you know months ago so gotcha um what about
[4338.60 → 4343.22] flatter is that's we mentioned a little bit earlier in the show is that a common way is that the
[4343.22 → 4350.86] way um there's a PayPal donate link in the footer of semantic-ui.com um that's I feel it's a little bit
[4350.86 → 4357.78] easier to deal with than um flatter which is working off the euro I think gotcha and so when you go to
[4357.78 → 4362.32] that you do have the option to make it a monthly donation uh you're not putting a dollar amount in
[4362.32 → 4368.54] there so it could be a buck it could be 50 cents it could be five dollars it could be whatever uh the
[4368.54 → 4372.86] generous folks out there decide to put in that donation amount box is that correct
[4372.86 → 4379.82] yeah completely, and you know as uh somebody working this a long time I would just love to
[4379.82 → 4384.86] have other developers help so uh if you're more financially you know interested I would love
[4384.86 → 4390.70] you know to be able to have more as you say uh runway for this but also if you're a developer please
[4390.70 → 4396.10] help us with our integrations and uh else wise and uh something else I want to point out too here at
[4396.10 → 4402.74] the end is uh is you guys use Gitter so Gitter.I'm slash semantic hyphen org there's also a link in
[4402.74 → 4407.66] the main websites flitter which we'll also put in the show notes but that seems like a good way if
[4407.66 → 4411.80] you just want to hop in and say hi to jack and the rest of the community then you can easily hop in
[4411.80 → 4417.30] and just say hello and uh and just sort of step in and just kind of get to know people first before
[4417.30 → 4422.88] you commit to anything financially or even your actual work so you can sort of get a heartbeat of
[4422.88 → 4428.52] the community by stepping in and just saying hello yes it was wonderful plug, and also you know
[4428.52 → 4434.02] uh I love getter by the way I want to I want to plug them because they're amazing and what they've
[4434.02 → 4438.66] done um you know how do slack have like sort of closed chat rooms and then all of a sudden getter
[4438.66 → 4443.46] came along, and it's like my god people can organize around open source much easier thank you guys for
[4443.46 → 4446.72] doing it there are definitely some interesting things happening there because you can see like
[4446.72 → 4452.54] how you know for example your user has labelled something or someone some other user avalanche one
[4452.54 → 4459.82] not sure who that is opened issue 2530 at certain times so you can sort of not only catch up with
[4459.82 → 4464.74] people but also see the activity of the project which is pretty neat for that and I'm sure anybody
[4464.74 → 4469.84] else out there listening to this has played with getter but i I haven't much yet I've always only been
[4469.84 → 4476.32] a slack guy, so this is pretty interesting to see yeah I love getter um yeah if you want to keep track of an
[4476.32 → 4481.12] open source project like the first thing you should do is open its getter everything's in one view
[4481.12 → 4486.44] cool all right well jack hey thank you so much for coming back I know it's been a year and a half and
[4486.44 → 4493.50] we said 1.0, but we got you a 2.0 nonetheless uh great show today hopefully your runway is long to keep
[4493.50 → 4501.76] stretching out jarred's analogies I hope your band becomes the know American Idol or something like
[4501.76 → 4506.88] that maybe you get on the voice uh that's a that's a bad joke jerry why do you let me make that joke
[4506.88 → 4513.82] man oh man you wouldn't bail me out earlier so I'm not bailing you all right but the tail of this show
[4513.82 → 4517.74] I do want to plug some things uh we have some awesome sponsors making this show possible
[4517.74 → 4522.86] um, but we are going to be at gopher con as a matter of fact if you're listening to this
[4522.86 → 4527.96] we're at gopher con right now and if you're listening to this you're probably at gopher con
[4527.96 → 4531.08] well maybe you're not at gopher con but if you are listening to this, and you're at gopher con
[4531.08 → 4537.20] come and say hi if you haven't already yet uh we definitely love hanging out with all the gophers
[4537.20 → 4543.82] there in Denver the mile high the mile high city as they call it and jarred how excited are
[4543.82 → 4548.10] you about the temperature there man I guess you're not that excited because you don't live in Texas but
[4548.10 → 4556.30] what's it going to be it'll be nice 60s 70s it's like 90s okay right now outside it's
[4557.18 → 4564.96] 91 degrees that's not cool what's cool is 70 degrees that's cool have you considered moving
[4564.96 → 4572.54] I'm I'm pulling a jack here okay the in this case it's a wife not a girlfriend we can't quite move so
[4572.54 → 4578.56] but we have discussed that Denver is the city if we moved to any other state than Texas because
[4578.56 → 4584.88] it's Texas forever uh but if we did move it would probably be Colorado and in particular Denver
[4584.88 → 4593.10] Omaha did you say jarred oh I'm sorry I coughed oh okay gotcha jarred's from Omaha
[4593.10 → 4599.90] Nebraska I can't even cough that I've heard that's pretty cool anyway so thanks to our sponsors thanks
[4599.90 → 4605.50] to jack thanks to all the listeners for uh listening to this awesome show and jack we hope
[4605.50 → 4610.40] your one way is long my friend, and thank you so much for coming on this show let's say goodbye
[4610.40 → 4613.74] see ya thanks guys see ya
[4629.90 → 4630.40] you
