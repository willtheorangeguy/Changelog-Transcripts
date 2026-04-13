[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.14] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to Linode.com slash Changelog.
[15.30 → 18.12] This episode is brought to you by Rollbar.
[18.42 → 24.36] Rollbar is real-time error monitoring, alerting, and analytics that helps you resolve production errors in minutes.
[24.68 → 28.60] And I talk with Paul Bigger, the founder of CircleCI, a trusted customer of Rollbar.
[28.60 → 32.96] And Paul says they don't deploy a service without installing Rollbar first.
[33.32 → 34.58] It's that crucial to them.
[34.78 → 36.60] We operate at serious scale.
[37.04 → 42.44] And literally the first thing we do when we create a new service is we install Rollbar in it.
[42.64 → 45.52] We need to have that visibility.
[45.94 → 50.44] And without that visibility, it would be impossible to run at the scale we do.
[50.58 → 52.54] And certainly with the number of people that we have.
[52.72 → 55.70] We're a relatively small team operating a major service.
[55.70 → 61.46] And without the visibility that Rollbar gives us into our exceptions, it just wouldn't be possible.
[61.84 → 62.00] All right.
[62.02 → 66.70] If you want to follow in Paul's footsteps and start deploying with confidence today, head to Rollbar.com slash Changelog.
[67.38 → 70.34] Once again, Rollbar.com slash Changelog.
[70.34 → 81.76] Welcome to JS Party, a weekly celebration of JavaScript and the web.
[81.90 → 88.38] Tune in live on Thursdays at 1 p.m. Eastern, 10 a.m. Pacific at changelog.com slash live.
[88.38 → 93.48] Join the community and Slack with us in real time during the show at changelog.com slash community.
[93.86 → 94.66] Follow us on Twitter.
[94.76 → 96.28] We're at JSPartyFM.
[96.44 → 97.76] And now on to the show.
[97.76 → 105.16] Hello and welcome to Mocha Party.
[105.42 → 106.08] Oh, wait.
[106.20 → 107.14] No, that doesn't sound right.
[107.48 → 109.88] Hello and welcome to EMMA Party.
[110.22 → 111.62] Nope, not that either.
[112.18 → 114.66] Hello and welcome to Webs Party.
[115.48 → 115.84] Hmm.
[115.96 → 117.68] I don't know why we're going with this.
[118.04 → 122.90] But today's episode, we are going to be debating whether JavaScript should be rebranded.
[122.90 → 129.48] As you may or may not know, there is a long, complicated history to the actual name of the
[129.48 → 131.38] language that we all love here on this party.
[131.38 → 138.20] And it has some interesting roots where it was originally internally called Mocha, but then
[138.20 → 142.52] they wanted to ride the coattails of the popularity of Java back at the time.
[142.60 → 144.40] And so it was renamed to JavaScript.
[144.74 → 150.82] But now it's technically ECMAScript, even though none of us really even write straight JavaScript
[150.82 → 151.38] anymore.
[151.38 → 157.18] Whether that's TypeScript or using Babel to do something else that is in between that
[157.18 → 157.90] with JSX.
[158.32 → 161.80] We're kind of writing this language that almost looks like JavaScript all the time.
[161.94 → 164.60] So should JavaScript be rebranded?
[165.02 → 166.80] Today we're going to be debating that.
[167.04 → 170.18] I'll be your host, Nick Needed, and your moderator as well.
[170.48 → 173.50] And then on the Yep team, we have Divya.
[174.06 → 174.70] Hey, hey.
[175.42 → 176.50] And Jared.
[177.08 → 177.62] Yep, yep.
[177.62 → 177.66] Yep.
[178.26 → 179.98] And on the Nope team, we've got K-Ball.
[180.62 → 181.42] Hello, hello.
[181.94 → 184.22] And Chris, aka Bone skull.
[184.58 → 185.34] Happy Halloween.
[186.32 → 186.74] Woo!
[186.84 → 190.02] We are recording on Halloween, so this will be a spooky episode, even though you won't
[190.02 → 191.58] hear it until the week after.
[191.74 → 193.96] So happy Halloween to everybody out there.
[194.48 → 196.18] And let's dive right into it.
[196.46 → 198.94] Well, hold on, hold on, because I just had a realization.
[199.40 → 203.60] Somehow this never hit me on our previous debates, but Yep Nope, our mascot should be the
[203.60 → 204.06] Yip Yips.
[204.06 → 204.70] The Yip Yips.
[205.72 → 207.48] I have no idea what you're talking about.
[207.84 → 208.06] Yeah.
[208.14 → 209.52] It's like The Muppets.
[210.26 → 212.20] Like, they go Yip Yip Yip Yips.
[212.52 → 212.78] Oh.
[213.40 → 213.56] Yep.
[214.04 → 214.40] Yep.
[214.70 → 216.02] Yip, yip, yip, yip, yip, yip, yip.
[216.08 → 218.20] And then they ask some questions where then there's nope.
[218.48 → 218.84] Nope.
[219.02 → 219.18] Nope.
[219.30 → 219.42] Nope.
[219.52 → 219.62] Nope.
[219.62 → 219.68] Nope.
[219.68 → 221.36] There's also a character that goes, meet, meet, meet, meet.
[221.38 → 221.56] Right?
[222.08 → 222.92] I'll have to Google that.
[223.56 → 224.10] Hi there.
[230.10 → 230.38] Book.
[230.74 → 230.96] Book.
[231.22 → 231.42] Book.
[231.58 → 231.68] Earth.
[231.84 → 232.02] Book.
[232.16 → 232.64] Earth.
[232.66 → 233.10] Book.
[233.10 → 233.32] Earth.
[233.38 → 233.60] Book.
[233.60 → 233.82] Yep.
[234.02 → 234.14] Yep.
[234.26 → 234.72] Yep.
[234.84 → 235.92] Yep.
[235.92 → 236.14] Yep.
[236.40 → 236.76] Yep.
[237.04 → 237.30] Yep.
[237.30 → 237.38] Yep.
[237.48 → 237.60] Yep.
[237.60 → 239.44] I will find a link to that.
[239.52 → 243.00] And then they like try to mimic different sounds like the telephone.
[244.80 → 247.00] Yes, it's kind of amazing.
[247.18 → 251.12] And I am shocked, absolutely shocked that you all are not familiar.
[251.44 → 254.38] It's been a while since I've watched The Muppets.
[254.98 → 255.48] Me too.
[256.36 → 259.26] I mean, I like The Muppets as much as the next guy.
[259.28 → 260.38] I like The Muppets.
[260.40 → 262.88] I haven't watched Muppets, but like that clip is hilarious.
[263.48 → 267.32] I just want to compliment K-Ball on his uncanny ability.
[267.32 → 270.04] To completely derail the show before it even starts.
[270.62 → 271.10] Totally.
[271.60 → 272.96] So what were we talking about?
[273.08 → 276.94] Whether we should have the Muppet party or.
[277.74 → 278.76] Yeah, no.
[279.24 → 279.64] Yep, yep.
[280.22 → 282.44] Yep, yep, yep, yep, yep, yep, yep, yep.
[283.00 → 284.44] You're on the nope team, K-Ball.
[285.60 → 286.44] Oh, my bad.
[286.94 → 289.98] So getting into this, I guess let's just dive right in.
[289.98 → 296.30] Now, actually, before we do, and I will turn it over to Divya to argue the yep, yep side.
[296.30 → 298.74] On whether JavaScript should be rebranded.
[298.88 → 302.36] But I totally am stealing an idea from you, Divya.
[302.50 → 303.00] And I'm sorry.
[303.46 → 306.96] I listened recently to the last yep, nope episode with you.
[307.04 → 310.48] And you had an awesome haiku about JavaScript tooling.
[310.82 → 315.64] And so I'm completely ripping that off with a limerick about today's topic.
[315.72 → 316.00] Yes.
[316.30 → 316.82] Nice.
[316.82 → 319.50] And that is, should JavaScript be rebranded?
[319.94 → 321.28] Does that seem too heavy-handed?
[321.78 → 325.52] We're going to debate, consider its fate, while not leaving users stranded.
[326.52 → 327.46] I love that.
[327.72 → 328.32] That's great.
[328.46 → 328.56] Thank you.
[328.72 → 329.40] That's beautiful.
[329.40 → 331.06] That's all I have to contribute as the moderator.
[332.60 → 333.00] Great.
[333.06 → 334.44] Then I don't have to make a limerick.
[334.54 → 334.96] I didn't.
[335.62 → 336.38] Yeah, not fair.
[336.44 → 337.28] You stole my argument.
[337.28 → 343.08] But for us, I mean, was it for us who broke it down?
[343.20 → 344.16] I forget who it was.
[344.24 → 345.88] It was like my entire limerick.
[346.00 → 346.62] Maybe it's Adam.
[347.56 → 349.62] Totally like tore it apart.
[350.02 → 350.94] But it was Michael.
[351.12 → 351.40] Michael.
[351.68 → 352.00] Yes.
[352.38 → 353.00] Tore it apart.
[353.46 → 354.14] It's fine.
[354.72 → 356.56] On that note, let's dive right in.
[356.66 → 361.02] Divya, do you want to start us off with your argument for why JavaScript should be rebranded?
[361.22 → 361.60] Sure.
[361.66 → 362.70] I can take it away.
[362.70 → 364.80] I will begin.
[365.14 → 366.22] So it's four minutes, right?
[366.66 → 367.52] I should time myself.
[367.92 → 368.14] Yes.
[368.26 → 368.80] Four minutes.
[370.58 → 371.22] Okay.
[371.80 → 376.46] So the premise being, should JavaScript be rebranded?
[376.72 → 378.20] And I represent the team.
[378.48 → 378.70] Yep.
[379.10 → 387.64] And so similar to how American football is actually fewer feet and more hand, JavaScript should be renamed because it's less Java and more web.
[387.64 → 400.52] Similar to what Nick mentioned earlier with the various namings of it, whether JavaScript should be called Web Script or something else is a valid point because JavaScript often gets conflated with Java.
[400.52 → 413.42] Many of us being web developers have gotten the very common email from recruiters asking us whether we're interested in a job in Java because of our extensive experience with Java, supposedly.
[413.98 → 422.40] But this is often a case where people tend to think that JavaScript includes Java or is a subset of Java, which is completely untrue.
[422.40 → 430.80] And so the naming itself causes a lot of confusion, especially for those who are not super technical and not in the technical community itself.
[431.48 → 438.58] And so the thing being, JavaScript also, as Nick mentioned, is an incredibly fractured community.
[439.40 → 444.74] Not only are we not writing JavaScript as is, many of us don't write vanilla JavaScript anymore.
[444.96 → 447.26] We write different flavours of JavaScript.
[447.66 → 451.14] There is React.js, which is now called React.
[451.14 → 452.72] I don't think anyone calls it React.js.
[453.46 → 456.80] There's Vue.js, which is a Vue flavour of JavaScript.
[457.38 → 458.02] There's Angular.
[458.28 → 458.78] There's Ember.
[458.88 → 460.10] There's all these different frameworks.
[460.26 → 465.84] And so all of us are no longer writing JavaScript in the same way that you would if you write vanilla JavaScript.
[466.14 → 468.16] No one is always documented. Query selector.
[468.36 → 473.72] Everyone is using their flavour of things and interacting with the DOM that way.
[473.72 → 482.90] And so the fracturing of the JavaScript community, and this is not even to say TypeScript comes in because TypeScript completely fractures the community.
[483.38 → 487.14] So the framework kind of gives pockets of people that we're still interacting with JavaScript.
[487.60 → 496.80] But the moment we think about TypeScript, that completely moves JavaScript in a completely different direction because JavaScript, by definition, is dynamically typed.
[496.80 → 502.42] And with TypeScript, it adds a type system to a language that doesn't have any types.
[502.94 → 505.50] And so in a sense, there is this split in the community.
[505.70 → 510.48] So there's the people who are very anti-TypeScript, and then there are people who are very pro-TypeScript.
[511.02 → 520.54] And so this fissure that's happening already comes to the fore and questions whether the term JavaScript actually fully encapsulates the community.
[520.54 → 522.44] Because TypeScript still uses JavaScript.
[522.62 → 524.12] It just adds types on top of it.
[524.12 → 527.36] And so should we now rename JavaScript to something else?
[527.48 → 529.14] There are many alternatives out there.
[529.50 → 533.88] There's, I think some people call it, there was Mocha, which is what it was called before.
[534.02 → 535.86] I think it was called Live Script at one point.
[536.24 → 546.46] But there's also various fun interpretations of it, such as Jota.js, or Jota.js, I think, or Yes, depending on the language that you speak.
[546.62 → 547.88] And then there's JavaScript.
[548.46 → 549.92] So it's not JavaScript.
[550.14 → 553.04] There's Conscript because of Brendan Eich.
[553.04 → 557.34] And then there's also this concept of ECMAScript, which is technically JavaScript.
[557.68 → 558.40] Very confusing.
[558.66 → 561.10] Similar to the confusion earlier with Java and JavaScript.
[561.68 → 568.74] There's a confusion around why is the community that federates or talks about the standards for JavaScript called ECMAScript.
[569.08 → 571.94] I mean, sure, there's naming and there's a lot of history around that.
[572.20 → 575.46] But there's often confusion because ECMAScript is technically JavaScript.
[575.46 → 580.46] But then there's TC39, which is the governing body for, like, pushing standards forward.
[580.94 → 586.12] And so all of this confusion leads to the community not being sure what exactly is happening at what point.
[586.62 → 599.32] And so it is indeed valid and is a point that we should consider renaming JavaScript to kind of bring that unity back so that all of us are aware of what we're doing whenever we say we write JavaScript.
[599.32 → 601.00] Very good.
[601.00 → 602.58] With five seconds to spare.
[602.94 → 604.88] All right, Chris, your rebuttal.
[605.56 → 607.50] So what's the end goal here?
[607.56 → 613.10] If the end goal of renaming, if you're a company, and you want to rebrand, well, why do you rebrand?
[613.22 → 614.88] There are many reasons for it.
[614.88 → 628.02] But in the case of JavaScript here, it seems to me that you would want to rebrand JavaScript, rename it something else to, I don't know, increase adoption of JavaScript.
[628.38 → 629.26] Is that a problem?
[629.44 → 631.58] Do we need to worry about JavaScript adoption?
[632.06 → 635.36] Do we need to worry about recruiters getting confused?
[635.48 → 636.76] I don't think that's an issue.
[636.76 → 647.10] But, you know, it seems to me that we have all these different frameworks and just like any other language, Java itself has, you know, spring.
[647.26 → 650.24] It has all sorts of different frameworks and flavours.
[650.88 → 653.22] You know, essentially, it's still all one language.
[653.26 → 656.18] Really, there's only one JavaScript.
[656.72 → 659.16] There's the ECMAScript standard.
[659.16 → 667.36] And you will use it insofar as what your transpired supports, what your target browsers support.
[667.70 → 670.20] But in the end, it's really all JavaScript.
[670.66 → 686.18] And I don't see any reason to make, you know, 50 different names for this stuff, depending on what particular feature you're using or where you're deploying it or, you know, what framework you're using.
[686.18 → 690.42] I think that would actually make the problem, you know, much worse.
[691.08 → 698.82] And so to Divya's point, you know, she said, we want to kind of bring everything back together and have that unity.
[698.98 → 699.78] Well, we do.
[700.14 → 702.20] We all write JavaScript, right?
[702.74 → 710.10] Insofar as the naming of it and the confusion around ECMAScript, because Oracle owns the trademark to JavaScript,
[710.10 → 716.36] I would imagine that if ECMAScript could call it JavaScript, they would.
[717.18 → 720.46] But they can't because Oracle owns the trademark.
[720.74 → 722.64] And so they had to come up with a different name.
[722.92 → 725.56] JavaScript is ECMAScript is JavaScript is ECMAScript.
[725.74 → 726.68] There's one language.
[726.92 → 730.60] So I don't see it as being necessary to rebrand.
[731.00 → 733.22] This is kind of a solution in search of a problem.
[733.58 → 736.66] There's really no good reason in my mind to do it.
[737.24 → 737.58] Good points.
[737.68 → 738.78] Good points for sure.
[738.78 → 743.74] Yeah, you make a good point about it not really having a marketing problem because it is the most popular language in the world.
[744.06 → 744.82] But what if that changes?
[744.96 → 747.08] What if something like I don't know?
[747.48 → 748.92] I know nobody everybody says it won't.
[748.98 → 752.42] But what if like a WebAssembly language overtakes JavaScript?
[753.00 → 754.60] Would we need to market it differently then?
[755.58 → 755.94] Nope.
[756.74 → 757.14] Yep.
[757.60 → 757.82] Yep.
[758.96 → 759.36] Definitely.
[760.22 → 763.96] Well, let me hop on that bandwagon, maybe steal a floor here for a moment.
[763.96 → 768.08] So Chris's argument is essentially if it ain't broke, don't fix it.
[768.78 → 771.40] And I'm here to tell you that it is definitely broken.
[771.90 → 774.70] The hallmark of a bad brand is confusion.
[775.34 → 780.20] In fact, most trademark law is centred around the idea of market confusion.
[780.20 → 793.16] If you go to Wikipedia on JavaScript's Wikipedia page, the very first sentence, the one right after from Wikipedia, the free encyclopedia, it says not to be confused with Java, the programming language.
[793.70 → 795.24] Later on, it talks about the naming.
[795.88 → 797.10] Nick, you went through some of that history.
[797.10 → 804.72] And it said the final choice of name caused confusion, giving the impression that the language was a spinoff of the Java programming language.
[805.06 → 815.26] And the choice has been characterized as a marketing ploy by Netscape to give JavaScript the cachet of what was then the hot new web programming language, Java.
[815.26 → 818.36] I like to tell a little story.
[818.48 → 827.58] So I had lunch with an acquaintance on Monday, wherein he was asking for advice about breaking into programming in this industry.
[827.70 → 830.84] This is something I do pretty often nowadays is advised people.
[830.84 → 839.52] And I spent at least 15 minutes of that one hour lunch explaining to him the difference between Java and JavaScript.
[840.28 → 840.96] Why?
[841.34 → 845.98] Because there is massive confusion around these two programming languages.
[846.56 → 852.74] Think about how many developers there are and think about how many developers are coming into our community.
[852.74 → 861.70] There's been estimates that the size of the developer ecosystem or the number of programmers in the world has been doubling every five years.
[862.26 → 863.88] Now, think about that conversation.
[864.58 → 877.96] In 2019, 25 years after the name JavaScript was chosen, and we're still explaining the difference between Java and JavaScript to people who are coming into our communities.
[879.22 → 880.84] It's time to end the confusion.
[880.84 → 884.78] It's time to cut ourselves loose from the rotting corpse that is Java.
[885.36 → 886.70] It's time to rebrand JavaScript.
[886.88 → 887.92] I rest my case, Your Honour.
[889.82 → 890.26] Yes!
[890.72 → 891.18] Yes!
[891.74 → 893.54] Okay, so I guess that makes it my turn.
[895.28 → 897.16] I love that you all are talking about confusion.
[897.60 → 908.00] This reminds me a lot of refactoring code that already works because it's confusing, and sometimes that's the right thing to do, and sometimes it just creates a lot more confusion.
[908.00 → 911.32] So, JavaScript, yes, the name is non-ideal.
[911.84 → 913.62] Yes, it confuses recruiters.
[914.18 → 917.86] So does every other distinction in the programming world.
[918.50 → 926.74] How many of you have gotten the, hey, long-time freelance web developer, would you be interested in this salaried embedded programming position using C++ in India?
[926.74 → 930.54] I mean, recruiters are always going to be confused.
[931.06 → 936.68] But if you want to confuse people, try renaming the most widely used language in the world.
[937.56 → 940.98] Have you ever tried changing the name of a widely used piece of code?
[941.70 → 943.36] Now try it again without find and replace.
[943.86 → 952.04] Try it again in over 1 million public packages downloaded over a billion times a day into who knows how many private applications and packages.
[952.04 → 956.56] Like, this is not going to reduce confusion, folks.
[956.64 → 959.02] This is going to ramp confusion up to 11.
[959.52 → 960.36] Not even thinking about the code.
[960.42 → 961.30] What about documentation?
[961.84 → 962.58] Past articles.
[963.08 → 966.56] How many millions of articles are already talking about JavaScript?
[966.80 → 974.62] Now, every new developer of Web Script or Ike Script or whatever the heck you want to call it is going to have to not only look for things in that,
[974.62 → 979.08] but also understand that these other things talking about JavaScript have relevance to them.
[979.22 → 980.48] They're not going to replace the knowledge.
[980.60 → 986.60] We're just adding onto the stack with something more and more confusing for new people coming into the industry.
[987.50 → 990.92] You know, every one of those recruiters is going to talk to you.
[991.22 → 993.70] Oh, you have JavaScript experience.
[993.82 → 995.06] Well, we're looking for Web Script.
[995.26 → 997.16] So you're clearly not applicable.
[997.48 → 999.28] This is not going to make anything better.
[999.28 → 1001.80] So I would close with a haiku.
[1002.62 → 1003.30] Yes.
[1003.90 → 1005.54] Because you all make it possible.
[1005.70 → 1007.02] Should we rebrand it?
[1007.54 → 1007.84] Duh.
[1008.10 → 1009.58] JavaScript is just fine.
[1009.96 → 1011.10] Stop navel-gazing.
[1011.42 → 1012.02] Very nice.
[1022.42 → 1024.90] This episode is brought to you by DigitalOcean.
[1024.90 → 1029.14] DigitalOcean is the simplest cloud platform for developers and teams.
[1029.48 → 1035.94] With products like droplets, spaces, Kubernetes, load balancers, block storage, and pre-built one-click apps,
[1036.20 → 1041.86] you can deploy, manage, and scale cloud applications faster and more efficiently on DigitalOcean.
[1042.22 → 1048.28] Whether you're running one virtual machine or 10,000, DigitalOcean makes managing your infrastructure way too easy.
[1048.62 → 1051.06] Head to do.co slash changelog.
[1051.06 → 1054.10] Again, do.co slash changelog.
[1059.28 → 1063.54] Now, what if we could find a middle ground between the two?
[1063.86 → 1070.32] So I think that the yip yips are arguing that it should be something potentially drastically different,
[1070.44 → 1074.74] like Mocha or Live Script or, you know, one of those or completely new name.
[1074.74 → 1078.70] And the nope-nopes are saying that JavaScript is just fine.
[1078.76 → 1085.32] But the article that this whole argument is based on actually offers a simple solution,
[1085.46 → 1091.00] which is why don't we just call it JS and drop JavaScript completely, and it just is JS,
[1091.00 → 1097.14] or maybe have server JS and web JS as kind of distinctions between the two,
[1097.22 → 1099.66] between like the obviously the server side and the client side.
[1099.76 → 1105.00] And the article argues that just like you don't really know what PHP stands for,
[1105.32 → 1107.74] eventually people will forget what JS stood for,
[1108.08 → 1112.66] but it will still be this name of a language that matches the file extension that we all use right now,
[1113.16 → 1116.00] potentially until MJS or something else comes along.
[1116.98 → 1117.30] Dot TS.
[1117.94 → 1118.64] Dot TS.
[1118.64 → 1119.20] Yes, yes.
[1119.24 → 1120.72] I wasn't going to go there, but thank you.
[1120.82 → 1122.62] Now, now we can go into this.
[1122.84 → 1123.04] All right.
[1123.44 → 1123.96] Dang it.
[1124.38 → 1124.74] No.
[1125.52 → 1129.72] Well, let me just say, I like the idea because we will not have to rename our podcast.
[1130.14 → 1130.90] That is true.
[1131.26 → 1131.82] That's true.
[1132.00 → 1132.72] So I'm pro.
[1132.84 → 1134.22] I'm pro JS for sure.
[1134.96 → 1137.22] Also happens to share my initials.
[1137.28 → 1137.64] Ooh.
[1137.90 → 1138.94] I like it less now.
[1141.14 → 1143.84] So yeah, now it would be the language named for Jared.
[1143.98 → 1148.62] The funny thing is my kids do think the JS Party t-shirt that I wear is because of my initials.
[1148.64 → 1150.86] And they're like, you have your own party and a t-shirt about it?
[1150.92 → 1151.74] I'm like, that's cool.
[1151.74 → 1152.08] That's right.
[1153.00 → 1159.32] So with the kids these days now, instead of having to distinguish between Java and JavaScript,
[1159.32 → 1162.90] looking up what does JS stand for in other places,
[1162.90 → 1166.54] we'd have to distinguish between the language JS and just saying.
[1166.54 → 1169.16] I've never heard that.
[1171.08 → 1171.52] What?
[1172.42 → 1173.96] No one says JS.
[1174.60 → 1176.44] They say JK, but JS.
[1177.64 → 1178.38] What's JS?
[1178.90 → 1179.48] I didn't hear it.
[1179.48 → 1180.06] Just saying?
[1180.56 → 1181.66] I've never seen that in my life.
[1181.70 → 1183.64] I don't know if that's a...
[1183.64 → 1184.06] JS.
[1184.06 → 1184.24] JS.
[1185.14 → 1191.02] Top five results on Google related to meanings of JS have to do with just saying...
[1191.02 → 1191.92] No, top four.
[1192.36 → 1193.82] Then we get down to JavaScript.
[1194.40 → 1194.66] Hmm.
[1195.40 → 1198.20] Oh, it could apparently also mean joint service.
[1198.90 → 1199.70] What is joint service?
[1200.46 → 1204.90] A military term referring to anything involving all services of the armed forces.
[1205.12 → 1205.34] Hmm.
[1206.10 → 1207.70] But Java could be coffee, right?
[1207.92 → 1208.06] So...
[1208.58 → 1209.14] That's true.
[1209.78 → 1212.14] Namespace conflicts are going to happen no matter what name.
[1212.14 → 1213.64] You're not going to pick a unique name.
[1213.70 → 1215.68] Now, here's a name that I thought was terrible was Go.
[1216.56 → 1219.12] Because there are so many things named Go.
[1219.76 → 1224.64] That being said, they've solved the search problem by suffixing Lang at the end.
[1224.72 → 1225.10] Golang.
[1225.18 → 1227.94] So you can search Golang to find Go related things.
[1228.18 → 1230.10] And that has never confused anyone.
[1230.18 → 1231.02] It works just fine.
[1231.68 → 1234.78] And they have an awesome mascot in the Gopher.
[1234.92 → 1238.12] This is another problem with the JS brand is we do not have an awesome mascot.
[1238.12 → 1243.46] Because we can't even get a name figured out, let alone an animal or some sort of creature.
[1243.80 → 1247.74] Also, on the logo thing, it's a pretty bland logo, like a very simple logo.
[1248.00 → 1252.84] It just has a square, and then it has JS in like the top, the bottom right corner.
[1253.48 → 1260.20] And I've actually seen that logo be used at a recruiting firm that had acronyms JS.
[1260.20 → 1262.94] And they used that as their logo.
[1263.54 → 1265.68] And they were a technical recruiting firm.
[1265.80 → 1268.18] And I was like, how do you, you can't do that.
[1269.58 → 1272.68] I mean, I don't think it's trademarked or anything, that logo.
[1272.86 → 1276.20] But it's annoying because now you can't have like cute interpretations of it.
[1276.26 → 1276.96] I mean, you can.
[1277.14 → 1284.62] I've seen like Singapore JS uses like the Singapore lion mascot instead of the J in the bottom and the yellow box.
[1284.70 → 1287.18] It's actually kind of like there are ways to do it.
[1287.60 → 1289.36] But yeah, it's pretty plain.
[1289.36 → 1293.88] I feel like the Gopher logo has cuter versions of it.
[1294.18 → 1299.04] Also, like frameworks, like Ember has a really cute little like, I don't even know what that thing is.
[1299.34 → 1301.78] What is, it's like the Ember squirrel or something?
[1302.96 → 1303.96] Like chipmunk?
[1304.44 → 1304.84] I don't know.
[1305.10 → 1305.94] I don't know what it is.
[1306.14 → 1311.28] Sounds like instead of rebranding the name of JavaScript, we should just come up with a better logo.
[1311.88 → 1313.06] What would you come up with as a logo?
[1313.68 → 1314.26] Or a mascot?
[1314.74 → 1316.22] A cup of coffee, like a job.
[1316.22 → 1319.82] And then a paper next to it, like a script.
[1320.10 → 1322.46] Yeah, but that was like coffee script, isn't it?
[1322.54 → 1328.04] Like, wasn't coffee script like a cup of coffee, and then it had like a in the phone, the logo, whatever.
[1329.12 → 1334.42] Looking around for things, animals starting with J and possibly asked what about a jumping spider?
[1334.42 → 1335.20] Oh, goodness.
[1335.20 → 1335.78] Oh, God.
[1336.86 → 1337.82] What about a rhino?
[1337.96 → 1339.66] Yes, actually the spider would be great.
[1339.66 → 1340.72] All right, I'm switching to Team Nope.
[1340.82 → 1341.70] We should not rebrand.
[1341.72 → 1343.88] Wait, but the spider would be great because it's like the web.
[1344.20 → 1344.64] The web.
[1345.26 → 1352.06] Ooh, JavaScript is like the web with, yeah, JavaScript is the spider crawling all over and making the web.
[1352.26 → 1352.74] I love that.
[1352.74 → 1354.54] All right, I'm getting on board with this.
[1354.64 → 1356.82] What about server-side JS though, or IoT?
[1357.56 → 1358.38] No, yeah.
[1358.66 → 1362.76] The server and the web stuff, like it's a false dichotomy.
[1362.90 → 1364.90] I mean, there's stuff that runs on the web.
[1365.02 → 1366.52] There's stuff that runs on Node.
[1366.66 → 1368.10] There's stuff that runs in boats.
[1368.26 → 1372.10] There's stuff that runs on microcontrollers and all sorts of things.
[1372.10 → 1378.02] It's a fool's errand to try to make these boxes for where your JavaScript belongs.
[1378.72 → 1382.20] Yeah, but at the same time, you would argue that JavaScript was built for the web.
[1382.20 → 1393.10] But us using it for server and IoT is just trying to fit it to these platforms, even though it was built specifically to run on the web.
[1393.92 → 1396.92] Essentially, JavaScript was built as the glue for HTML.
[1397.18 → 1398.64] I think that was how it was phrased.
[1398.98 → 1402.46] They just needed a way to interact with the DOM.
[1402.80 → 1404.84] And assembly was created for mainframes.
[1405.36 → 1406.54] The world has moved on.
[1406.98 → 1407.86] That's true for sure.
[1408.08 → 1410.36] And hence, we need a new name to encapsulate more.
[1410.36 → 1411.64] Yeah, we need to split.
[1411.82 → 1415.40] It needs to be like, this is web JavaScript, and then this is server.
[1415.72 → 1426.06] Because there are often cases when someone is like, this is JavaScript, but then they're showing node code, which I'm like, the node standards are different from the EMMA standards, for example.
[1427.26 → 1432.30] Yeah, and that is exactly what the article kind of comes to, is server.js and web.js.
[1432.78 → 1437.68] And so you'd have web.js 2020 referring to ES 2020.
[1438.22 → 1439.12] Good point, Nick.
[1439.18 → 1439.96] Yep, let's do it.
[1440.36 → 1446.90] Also, I wanted to say something to your confusion point about renaming being really hard.
[1447.48 → 1455.06] So JavaScript renames all the time, because they're like ES 2015, and then ES 2016, or like ES 5, and then ES 6.
[1455.18 → 1463.28] And then they were like, now we name by years, which is very confusing, because I'm pretty sure people still say ES 6, even though it's like ES 2015.
[1463.28 → 1465.82] And so there's this fissure that happens.
[1465.82 → 1470.76] And so I'm like, JavaScript already renames itself like every so often.
[1470.76 → 1475.68] And so what is the difference if we were to just rebrand it completely?
[1477.30 → 1478.72] People are already expecting it.
[1478.72 → 1482.88] And to your point about technical articles going out of date.
[1483.20 → 1487.30] Technical articles by nature expire within a couple of months.
[1487.30 → 1490.56] Like they're not valid because the standards move forward.
[1490.82 → 1492.32] And it's just the nature of it.
[1492.32 → 1493.88] Okay, what about the books then?
[1494.10 → 1495.06] Well, books are the same.
[1495.42 → 1496.68] Books are the exact same thing.
[1496.68 → 1507.16] If you write a technical book, that book is probably not going to be up-to-date the moment it's published.
[1508.54 → 1509.06] 100%.
[1509.06 → 1511.26] Like I have not written a book.
[1511.44 → 1515.34] I know a lot of people who have, and they put a lot of work into writing it.
[1515.40 → 1516.76] Not to discount that work.
[1517.24 → 1523.80] But the complaint generally is that from the time of writing it to going through the publication process,
[1523.80 → 1529.78] by the time it's published and out into the world, lots of things have changed, and they need to make updates.
[1529.78 → 1533.22] Which is why Manning created the early release version.
[1533.50 → 1535.76] So as you're writing the book, you can release it.
[1535.86 → 1538.22] So people get to see the content as you're writing it.
[1538.30 → 1540.32] So it's like always up to standard.
[1540.32 → 1542.56] And then you can always make updates as it goes.
[1542.68 → 1545.42] But that's generally the nature of writing technical content.
[1545.88 → 1552.26] You're never always going to be on point unless you write in a specific programming language that doesn't change.
[1552.68 → 1553.30] For example.
[1553.30 → 1556.40] So if you're writing in like Python, Python standards don't change.
[1556.50 → 1558.46] I mean, yeah, Python's moving from two to three.
[1558.86 → 1562.72] But like arguably Python 3 will not drastically change.
[1563.14 → 1569.12] And so if you were to write a book on Python 3, the likelihood of that being out of date in like a couple of months is very low.
[1569.20 → 1570.60] But in JavaScript, very high.
[1571.28 → 1573.56] I think you just made the argument for the resurgence of Perl.
[1573.80 → 1575.42] I don't think that's changed since I was born.
[1575.76 → 1578.98] And it has the perfect naming because it's a cute name.
[1578.98 → 1580.14] It's misspelled.
[1580.26 → 1582.38] So it's not to be confused with like Perls.
[1582.96 → 1585.52] And yeah, I'm pro Perl party.
[1586.04 → 1587.82] Also DuckDuckGo is written in Perl.
[1588.16 → 1588.96] Fun fact.
[1590.28 → 1592.24] Because I don't actually know why.
[1592.38 → 1596.18] I assume it was because of all the regex stuff that they have to do.
[1596.30 → 1596.82] I don't know.
[1597.68 → 1599.36] Speaking of bad names, DuckDuckGo.
[1599.54 → 1599.98] Terrible name.
[1600.30 → 1600.58] Yeah.
[1601.10 → 1603.12] You can't say it like, hey, did you DuckDuckGo that?
[1603.52 → 1604.54] Like it just doesn't roll off the tongue.
[1605.68 → 1607.24] DDG is a little better, but still.
[1607.56 → 1609.54] Perl is wonderful for write-only code.
[1610.30 → 1614.32] You have to work really hard to do readable code in Perl.
[1614.40 → 1615.14] It's not impossible.
[1615.32 → 1617.16] I know folks who've loved Perl and do a lot.
[1617.86 → 1619.80] Perl was one of the first languages I learned.
[1619.80 → 1620.44] Have you written much?
[1620.54 → 1621.94] Yes, 2019 yet?
[1621.94 → 1625.54] I don't keep track.
[1625.64 → 1626.22] It's all JavaScript.
[1626.50 → 1627.84] It's all ECMAScript, actually.
[1628.10 → 1628.86] It's all confusion.
[1629.34 → 1633.20] I just mean with all the new symbols and everything, there's a lot of Perl in there.
[1633.30 → 1639.62] Especially when you went from ES5 to ES2015, there was a bit of ramp up time to be able
[1639.62 → 1642.86] to read the JavaScript that you were accustomed to writing.
[1651.94 → 1665.50] This episode is brought to you by Brave.
[1665.98 → 1671.24] The Brave team is on a mission to fix the web by building an open source, privacy-focused,
[1671.56 → 1673.54] and performance-oriented browser.
[1674.16 → 1677.06] Browse the web up to eight times faster than Chrome and Safari.
[1677.62 → 1679.62] Block ads and trackers by default.
[1679.62 → 1683.72] And reward your favourite creators with the built-in basic attention token.
[1684.30 → 1685.56] Yes, you heard that right.
[1685.66 → 1687.72] A real-world use case for blockchain.
[1688.32 → 1693.74] Download Brave for free using the link in the show notes and give tipping a try on changelog.com.
[1703.50 → 1705.66] This is a question for Divya and Jared.
[1706.06 → 1709.32] When someone says JavaScript, are you confused about what they're talking about?
[1709.32 → 1714.54] I often sometimes think whenever someone says they wrote JavaScript, and I'm just going
[1714.54 → 1716.02] to bring up the TypeScript point again.
[1716.46 → 1718.28] People often are like, I wrote JavaScript.
[1718.50 → 1721.00] And then you look at their code, and you're like, why is there types in this?
[1721.02 → 1722.14] And you're like, oh, it's TypeScript.
[1722.28 → 1723.82] Like, sure, you can see it from the extension.
[1724.54 → 1727.34] But I think often those two are conflated.
[1727.54 → 1729.30] You're like JavaScript, TypeScript, whatever.
[1729.46 → 1731.30] Or it's like JavaScript with types, blah, blah, blah.
[1731.68 → 1732.84] And so it's not clear.
[1732.94 → 1734.24] Sometimes it's not clear.
[1734.24 → 1736.98] And based on my knowledge of the person.
[1737.16 → 1740.34] So like if Nick were like, hey, you want to look at some JavaScript code I wrote?
[1740.42 → 1742.74] And I was like, there's a high chance it's going to be TypeScript.
[1743.96 → 1745.26] Very high chance.
[1745.94 → 1746.42] Versus...
[1746.42 → 1747.14] You don't know me.
[1747.54 → 1748.60] I know you.
[1750.08 → 1755.30] I mean, the easiest way to like to get on Nick's nerves is to just talk about TypeScript.
[1755.30 → 1757.30] And then you automatically...
[1757.86 → 1757.98] Amen.
[1758.34 → 1758.98] That's my MO.
[1759.30 → 1759.56] Yeah.
[1759.86 → 1762.40] This does raise an interesting question.
[1762.94 → 1765.82] You know, is JavaScript just a language?
[1765.92 → 1768.60] I mean, we can get very technical and dry.
[1768.68 → 1770.60] But I'm curious about colloquial usage.
[1770.78 → 1772.04] Is JavaScript just a language?
[1772.04 → 1773.08] Or is it a runtime?
[1773.30 → 1776.66] Like, is JavaScript essentially a build target now?
[1776.74 → 1778.04] Is it the equivalent of assembly?
[1778.14 → 1780.20] Where there are many types of assembly out there.
[1780.28 → 1783.74] But everybody kind of knows if I'm writing something, I'm going to compile it to assembly.
[1783.74 → 1784.18] Yeah.
[1786.50 → 1787.22] What?
[1791.76 → 1793.82] Maybe the question doesn't make sense.
[1797.00 → 1798.30] Perfect work.
[1798.44 → 1799.92] Can be just...
[1799.92 → 1800.74] I just...
[1801.50 → 1804.58] If JavaScript can also mean TypeScript.
[1805.44 → 1807.02] And it can mean...
[1807.02 → 1807.66] JSX.
[1809.20 → 1809.88] JSX.
[1809.88 → 1816.04] And it can mean anything compilable by Babel into JavaScript.
[1816.38 → 1817.48] Maybe it can mean Elm.
[1817.58 → 1819.62] Maybe it can mean Clojure Script.
[1820.66 → 1826.20] Do people think when you say JavaScript, is it anything that can compile down to the language
[1826.20 → 1828.54] interpreted by the browser, which is currently JavaScript?
[1829.32 → 1832.22] Is there anything else that we talk about that way?
[1832.52 → 1834.14] Assembly is the one that I was thinking.
[1834.86 → 1839.44] So are you, like, thinking if you were to write something in C and then compile it to, like,
[1839.48 → 1841.52] assembly or Wasm, is that JavaScript?
[1841.98 → 1842.80] Is that the question?
[1843.64 → 1846.64] That wasn't quite where I was going, but that's a natural extension.
[1846.84 → 1847.40] I kind of like it.
[1847.46 → 1847.92] This is what...
[1847.92 → 1848.50] I'm confused.
[1848.84 → 1850.70] Is everything JavaScript?
[1851.06 → 1852.58] Has this world just become...
[1852.58 → 1853.66] JavaScript's eating the world.
[1853.74 → 1854.20] Is that what you're saying?
[1854.66 → 1854.96] Yeah.
[1855.12 → 1856.32] JavaScript is eating the world.
[1856.32 → 1856.84] But...
[1856.84 → 1857.78] If it runs with JavaScript.
[1857.78 → 1863.80] If I write C, if I write C, and it compiles down to assembly, I didn't say I wrote assembly.
[1864.40 → 1865.16] That's true.
[1866.06 → 1866.62] So...
[1866.62 → 1868.68] So why do we do that for JavaScript and TypeScript?
[1869.30 → 1869.82] Do we?
[1870.14 → 1870.60] Apparently.
[1871.02 → 1872.08] According to Divya.
[1872.26 → 1875.76] Well, but TypeScript is a superset of JavaScript.
[1876.00 → 1880.52] So, like, there's a distinction there versus something like Clojure Script or CoffeeScript,
[1880.64 → 1882.46] where it's not really the same syntax.
[1882.98 → 1884.42] With TypeScript, it is the same syntax.
[1884.52 → 1886.20] It's just with some additional stuff.
[1886.20 → 1887.86] And very hard to read, also.
[1888.70 → 1890.20] Oh, my God.
[1892.40 → 1892.84] Burn.
[1894.14 → 1894.72] Not going there.
[1894.86 → 1895.44] Not going there.
[1897.60 → 1898.52] But I agree.
[1898.68 → 1904.46] I think definitely certain things like Clojure Script, and it's very different.
[1904.58 → 1905.32] Like, it compiles down.
[1905.52 → 1906.48] And similar to Elm.
[1906.58 → 1908.94] Like, Elm is considered in the JavaScript ecosystem.
[1909.26 → 1912.30] I don't think Elm has been talked about as outside of it.
[1912.60 → 1915.34] So when we talk about frameworks, Elm kind of gets thrown in sometimes.
[1915.34 → 1919.10] But Elm, when you're writing Elm, it's not like writing JavaScript.
[1919.24 → 1921.80] It compiles down to JavaScript, even though they're part of the job.
[1921.88 → 1922.62] It doesn't make sense.
[1922.72 → 1923.34] I think it's crazy.
[1924.06 → 1926.76] Because I'm like, whenever you write Elm, it doesn't look like JavaScript.
[1926.76 → 1930.54] And you're using the compiler to compile to JavaScript.
[1930.54 → 1933.82] And so that is a really confusing thing.
[1933.92 → 1942.82] Because you're like, when you talk about frameworks in the front-end scope of things, which front-end generally includes all JavaScript-related things, that's a huge confusion.
[1942.82 → 1944.30] Because you're like, oh, you know JavaScript?
[1944.50 → 1945.60] You'll be able to pick up Elm.
[1945.72 → 1947.38] Which is totally not true.
[1947.38 → 1953.24] I know someone from the Elm community is probably going to have my neck on Twitter after this gets released.
[1954.10 → 1956.98] I don't think the Elm folks claim that Elm is JavaScript.
[1957.38 → 1960.24] Or I think they claim that it's a front-end framework.
[1960.66 → 1961.96] And I think that's a fair claim.
[1962.22 → 1962.50] Yes.
[1962.76 → 1963.06] Yeah, yeah.
[1963.10 → 1966.52] But I think the claim also is that if you know JavaScript, you can pick up Elm.
[1966.62 → 1970.10] Which I'm like, I'm not sure if that is a fair statement.
[1970.10 → 1980.14] Maybe we should take inspiration from another language, Java, and talk about the virtual machine we're compiling to, right?
[1980.26 → 1981.64] Java has the JVM.
[1981.74 → 1984.30] Maybe we just need to start calling things the JSVM.
[1984.70 → 1986.20] We have a V8, right?
[1986.52 → 1987.50] The engine.
[1988.16 → 1991.14] But also, some standards are pulling from Java.
[1991.34 → 1997.58] So there's the concept of interfaces, which I saw in the TC39 standards, where I'm just like, what?
[1997.58 → 2000.80] This is a Java thing, but we're pulling it into JavaScript.
[2001.08 → 2006.56] And there are certain things and elements that is being pulled into the JavaScript language that is inspired by Java.
[2007.22 → 2009.46] So there are a lot of those correlations that happen.
[2010.24 → 2012.10] And hence the confusion overall.
[2013.24 → 2018.12] So Rebecca in the chat points out that when you talk about architecture, there's usually follow-up questions.
[2018.18 → 2019.02] You say, I'm an architect.
[2019.20 → 2021.72] People will ask what kind of architecture do you do?
[2022.28 → 2025.42] And so what about when people say, I do JavaScript?
[2025.42 → 2027.70] Maybe it's just a matter of follow-up.
[2027.80 → 2028.96] Maybe it's a matter of education.
[2029.30 → 2046.82] We need to have a larger conversation because it encompasses so many different things now that it is really hard to just come up with one term, one word, one phrase that will encapsulate all the JavaScript does or is because it does and is so many things to so many people.
[2046.82 → 2049.44] So maybe it is just an education problem.
[2049.62 → 2053.96] So maybe our efforts would be better spent not renaming it, but improving education.
[2054.38 → 2058.76] That being said, going back to my conversation on Monday, it's strange.
[2058.90 → 2065.90] It's unfortunate with so many people coming into this industry that we're 25 years removed from this mistake, and we're still paying for the sins of our fathers.
[2065.90 → 2066.66] Right.
[2066.74 → 2071.00] We're still having to explain away the confusion all these years later.
[2071.30 → 2072.26] Also, how do you think?
[2072.54 → 2074.34] So this is my opinion on things as well.
[2074.68 → 2079.60] Just the correlation between JavaScript, like the community and how all of us relate to JavaScript.
[2079.92 → 2083.52] And then there's the standards committee, which is like TC39.
[2084.22 → 2087.22] And I often find there's a huge gap between the community.
[2087.22 → 2092.68] And I know TC39 hates when people bring this up, and they're trying to be better about it.
[2092.76 → 2093.82] But there's still this huge...
[2093.82 → 2095.72] You're trying to piss off everybody today, aren't you, Divya?
[2096.84 → 2097.64] It's just, you know...
[2097.64 → 2099.46] TypeScript, Elm, and TC39.
[2100.04 → 2100.48] Whatever.
[2101.08 → 2103.32] I'm just going to continue down this road.
[2104.02 → 2109.88] I wonder how much of that is people are just bored stiff of the concept of standards and committees, right?
[2109.92 → 2112.70] Like we've tried to shine a light there a little bit.
[2112.76 → 2113.56] We've tried to connect.
[2113.56 → 2117.74] We've had episodes on connecting with folks and talking about TC39.
[2118.40 → 2122.14] And when we ask community members, like, what was your least favourite episode?
[2122.24 → 2123.98] They're like, oh, that's standards one, man.
[2124.04 → 2124.98] That was terrible.
[2124.98 → 2127.46] That's not interesting to talk about standards.
[2127.76 → 2131.24] Well, because also if you're in a committee, there's a lot of process.
[2131.64 → 2137.72] So like the EMMA, like TC39 committee has specific ways in which they conduct their meetings.
[2137.72 → 2142.38] And there's language and processes because it's just a general, like, standard board.
[2142.90 → 2148.22] And so the language that they speak is very different from the average JavaScript developer.
[2148.98 → 2153.66] And so there's a huge disconnect because when TC39 has meetings, and they talk about things,
[2153.66 → 2166.66] they're so deep down in the weeds in terms of like how exactly the JavaScript language works and the repercussions of specific standards going through to like various stages,
[2166.66 → 2171.00] as opposed to the average JavaScript developer who's like, why don't we have this one thing?
[2171.10 → 2172.06] We should have this.
[2172.06 → 2175.78] And so the experiences are very different.
[2175.78 → 2186.42] And it's really hard to bring those two things together because also TC39 tends to be because it's very much a wider problem of like the problem of the web.
[2186.42 → 2193.18] And how do we make JavaScript better so that it encompasses all the problems you could potentially have when you work with JavaScript?
[2193.18 → 2198.88] But it often only includes members of specific companies.
[2199.22 → 2201.64] So it's very large scale tech companies.
[2201.64 → 2207.14] So like PayPal and Google and Microsoft, and all of them have representatives that go there.
[2207.30 → 2212.56] And so the question then becomes like, are they representative of the average developer?
[2212.56 → 2217.88] And oftentimes that answer is no, because they're thinking about things on a different scale.
[2217.88 → 2227.36] And so because of that, there's also this issue of how they talk to developers, because like, if you're at a level that's completely different from someone else,
[2227.62 → 2234.18] it takes a lot for you to kind of bring it down or not to bring it down, but to meet someone at their frequency.
[2234.68 → 2242.92] I think the issue that we're having now in the community, which is this like disconnect is because that gap hasn't been closed.
[2242.92 → 2253.88] There's a lot of like TZ39s trying to educate, but they're educating at a level that the average JavaScript developer is like, this is not a problem I care about, or it's not something I feel is tangible.
[2254.54 → 2260.58] And so that's a huge problem, because I'm like, they're supposed to represent us, but we don't feel represented.
[2260.96 → 2263.66] And so that causes a lot of disconnect.
[2264.28 → 2266.80] Therefore, we should rename JavaScript.
[2267.72 → 2270.46] Therefore, we should solve this problem.
[2270.46 → 2275.16] I think Chris is just scared we might call it Mocha, and then you have to have Mocha.
[2275.88 → 2276.76] Mocha.
[2277.12 → 2278.52] Chris has a dog in this hunt.
[2278.88 → 2283.36] Yeah, I think there is actually a trademark now, so you can't use it.
[2283.72 → 2285.06] Of Mocha or of JavaScript?
[2285.50 → 2286.72] Sorry, Mocha.
[2286.96 → 2288.82] Oh, really? Who owns a trademark for Mocha?
[2289.66 → 2291.76] It would be the Opens Foundation.
[2292.22 → 2292.82] Oh, really?
[2293.56 → 2294.00] What?
[2294.62 → 2295.96] Nice. So you're protected.
[2296.38 → 2297.36] Chris got out ahead of you.
[2297.36 → 2301.66] Yeah. That would be fun, because then the Opens Foundation would have to rename again, right?
[2302.32 → 2303.48] That would be fun.
[2304.62 → 2305.98] The Open Mocha Foundation.
[2306.18 → 2306.46] Oh, yeah.
[2306.72 → 2311.82] I talked about renaming in documentation, renaming in packages, renaming in applications,
[2311.82 → 2319.40] but can you imagine all of these companies that have legal documents that reference JavaScript or other things?
[2319.40 → 2329.54] Once again, if you want to increase confusion and chaos, try renaming one of the most popular things and widely used things in the world.
[2330.06 → 2331.28] You have to get with the times.
[2332.40 → 2335.54] There's a reason why Coca-Cola is still called Coca-Cola.
[2335.74 → 2337.46] Because it's a strong brand without confusion.
[2338.12 → 2338.70] Yeah, exactly.
[2339.44 → 2340.48] Oh, without confusion.
[2340.48 → 2346.36] How much of the Middle East or Midwest calls everything that's a soda a Coke?
[2346.36 → 2347.14] That's a strong brand.
[2347.18 → 2348.36] I don't know about that.
[2348.58 → 2349.32] Because they're actually extending it.
[2349.64 → 2352.10] They're extending it beyond what it even goes to.
[2352.46 → 2353.58] That's like Kleenex.
[2353.82 → 2354.98] Because it's so clear.
[2355.20 → 2357.32] It's so obvious that Coke is a soda.
[2358.18 → 2360.70] And so when you use it, people assume.
[2360.90 → 2366.10] And so JavaScript has not yet been used as a verb or a noun for various things.
[2366.60 → 2368.76] And so clearly there's a rebranding problem.
[2369.02 → 2369.60] Except TypeScript.
[2369.60 → 2371.70] Like, I'm Java Scripting right now.
[2372.40 → 2373.36] I'm on the JavaScript.
[2373.82 → 2376.36] I'm Java Scripting right now.
[2377.34 → 2380.50] We were just talking about one of the extensions of JavaScript to TypeScript.
[2381.08 → 2383.14] I think the brand is extremely strong.
[2383.24 → 2384.80] People are trying to ride the JavaScript brand.
[2385.00 → 2387.44] Increasingly, Java is trying to ride the JavaScript brand, right?
[2387.58 → 2389.54] Because we're the popular ones.
[2389.68 → 2389.90] We're cool kids.
[2391.10 → 2396.36] Well, in an effort not to rename everything, let's try to keep our podcast named JS Party.
[2396.36 → 2399.26] And maybe we can rename JavaScript to Party Script.
[2399.60 → 2400.30] What?
[2400.88 → 2402.90] And then we don't have to rename.
[2403.14 → 2404.46] And yet, no confusion.
[2404.64 → 2405.72] It's a Party Script.
[2406.22 → 2406.36] Huh?
[2406.64 → 2406.82] Huh?
[2407.04 → 2407.22] Huh?
[2407.34 → 2410.34] If we're talking names, I like Adscript.
[2410.90 → 2411.76] Oh, that's nice.
[2412.10 → 2412.24] Yeah.
[2412.62 → 2412.98] Rad.
[2413.16 → 2413.74] Okay, you win.
[2413.74 → 2415.98] Yeah, but then we'd have the RAM stack.
[2416.12 → 2417.00] And I don't know that that's a...
[2417.00 → 2417.28] Ram stack.
[2417.28 → 2418.58] Or A-D.
[2419.16 → 2423.76] I know, but I'm just saying everything that has a J in it is going to need to swap then
[2423.76 → 2428.00] to an R. And there's going to be some interesting acronym breaking.
[2428.22 → 2432.24] Also, I find that the J in multiple languages is pronounced very differently.
[2432.24 → 2437.06] And so you end up with like, if you're in a Spanish-speaking country, someone might say
[2437.06 → 2437.62] JavaScript.
[2437.82 → 2439.20] Even though that's not always the case.
[2439.26 → 2442.02] I think sometimes people just say the English version.
[2442.84 → 2447.58] But the J is a very confusing alphabet or letter.
[2447.58 → 2453.46] I mean, when we look at the majority of the population doesn't use the same letter system
[2453.46 → 2456.40] anyway, like, I don't think that should be a concern, right?
[2456.48 → 2462.12] Like, if the majority of people are using iconography because they're actually speaking
[2462.12 → 2466.82] in Mandarin, or they're using, I don't know what the script is called, but for Hindu or
[2466.82 → 2472.58] other things, like, really, should we be worried about the nuances of how a particular
[2472.58 → 2475.64] letter in our lettering system works?
[2476.52 → 2477.18] Probably not.
[2477.98 → 2479.58] Well, what else would we talk about then?
[2481.86 → 2484.42] It's a very Western-centric view, actually.
[2485.50 → 2488.70] We need a new technical committee to discuss this.
[2488.76 → 2489.28] That's what we need.
[2489.40 → 2490.86] One more name to add to the pile.
[2492.14 → 2493.04] One more protocol.
[2493.04 → 2497.46] Maybe we should just boil everything down to a logo or an icon.
[2497.90 → 2498.96] And then you can't even say it.
[2499.08 → 2501.26] It could be like, uh, Prince tried that.
[2501.44 → 2501.96] It did not work.
[2502.44 → 2502.88] Yeah.
[2503.08 → 2504.70] The language formerly known as JavaScript.
[2504.92 → 2505.04] Yeah.
[2505.14 → 2506.22] Prince did try that.
[2506.40 → 2507.42] And no one understood.
[2507.42 → 2508.44] I mean, yeah.
[2509.02 → 2509.34] Ooh.
[2509.70 → 2513.26] Can we draw lessons from the Prince renaming for JavaScript?
[2513.66 → 2517.44] Like, everyone would just start talking about the language formerly known as JavaScript.
[2518.24 → 2522.94] Well, that is a perfect way to end this podcast formerly known as JS Party.
[2522.94 → 2525.52] This is going to be our last episode.
[2527.40 → 2529.80] If we rename it, it will be the last episode of this.
[2529.80 → 2536.54] As a way to send us off then, let's have the Yip Yips, Divya and Jared, because you are pro
[2536.54 → 2537.12] renaming.
[2537.62 → 2539.30] Why don't you tell us what you would rename it to?
[2539.44 → 2540.96] And it doesn't have to be anything crazy or silly.
[2541.06 → 2542.74] It could just be JS or whatever.
[2543.30 → 2548.96] And then the Nope Nopes, let's have you tell us what mascot you would adapt to keep JavaScript.
[2548.96 → 2558.60] Well, I think that the article that we referenced by Kieran Potts, I think Kieran has the correct answer, which is it being just JS, folks.
[2558.74 → 2559.60] It's just JS.
[2560.02 → 2560.66] Keep it simple.
[2560.88 → 2561.88] Keep the extension.
[2562.38 → 2562.56] Boom.
[2562.56 → 2568.68] And you could just say, just, just, just, just saying.
[2569.32 → 2575.10] It would be like, yes, but just, just, just, just, just say.
[2575.24 → 2575.88] It's just.
[2576.66 → 2578.22] That's our official response, Nick.
[2581.16 → 2581.64] Perfect.
[2581.90 → 2582.58] Final answer.
[2582.94 → 2583.98] Oh, dear.
[2584.48 → 2588.10] K-Ball and Chris, what would you have as the JavaScript mascot?
[2588.68 → 2589.42] I like a goat.
[2590.12 → 2590.72] A goat?
[2590.72 → 2594.72] The greatest of all time.
[2594.72 → 2595.24] The greatest of all time.
[2596.36 → 2596.84] Oh, that's great.
[2596.84 → 2597.54] That's pretty good.
[2598.16 → 2599.22] I have a couple ideas.
[2599.46 → 2604.62] One is if there's one thing we learned from this episode, it's that JavaScript is the Coca-Cola of programming languages.
[2604.62 → 2607.76] So we could go with some sort of knock off of a soft drink.
[2608.56 → 2608.74] Gulp.
[2609.40 → 2613.52] Plus we, we know, yeah, fit well into Gulp.
[2613.56 → 2615.36] Also very unhealthy for you.
[2615.56 → 2618.72] Plus we know software developers love soft drinks.
[2618.72 → 2621.10] You can argue that JavaScript is unhealthy.
[2621.10 → 2621.74] No, you can.
[2621.84 → 2624.56] Cause you, you have too much of it and then your site is bloated.
[2624.92 → 2625.98] So clearly.
[2625.98 → 2631.58] You know, since I love coffee and it wouldn't cause any more confusion at all.
[2631.58 → 2634.64] I'd love it to be like a French press coffee maker, something like that.
[2634.96 → 2637.68] But really where I'm going to have to land is the jumping spider.
[2637.68 → 2644.34] Because I think, you know, the fun of spiders on the web and the fact there are land-based spiders that could be our node spiders.
[2644.34 → 2648.84] And there are web-based spiders that could be our web stuff.
[2649.02 → 2650.98] Like it's a flexible idea.
[2650.98 → 2653.96] And plus who doesn't love spiders all over their code.
[2653.96 → 2659.26] And it's, and it'll like, it'll take debugging to a true, you know, to its true form.
[2661.96 → 2663.28] That's wonderful.
[2663.50 → 2665.74] There are so many layers of this, right?
[2665.82 → 2669.18] Your spider is working on debugging the ecosystem.
[2669.18 → 2674.48] Yes, let's associate our brand with one of the most despised creatures on all earth.
[2675.86 → 2679.70] We've already noted how the JavaScript brand is so strong.
[2679.80 → 2682.60] It's like helping other brands come along now.
[2682.98 → 2684.28] So now you want to rebrand spiders.
[2686.10 → 2686.96] Recuperate spiders.
[2687.20 → 2687.76] Yeah, they're really.
[2688.54 → 2690.64] I mean, you could argue that people hate JavaScript.
[2690.72 → 2692.66] Like a lot of people are angry at JavaScript.
[2692.66 → 2698.14] If you talk to like other languages, a lot of people are like, oh, you JavaScript people, like blah, blah, blah.
[2698.14 → 2699.82] Such a fractured community.
[2700.48 → 2705.76] So yeah, like I feel like the spider would basically take, take that into account.
[2706.56 → 2707.24] Strong argument.
[2708.44 → 2709.72] I think it should be a goose.
[2710.02 → 2710.84] That's where I'll leave it.
[2712.14 → 2712.84] Thank you.
[2712.96 → 2713.84] That was wonderful.
[2714.24 → 2715.56] That's where I'll leave it.
[2718.20 → 2719.92] Like untitled goose game goose?
[2719.92 → 2721.80] Like untitled goose game because it's.
[2721.80 → 2722.98] I could get behind that.
[2723.10 → 2724.30] It's adorable yet annoying.
[2724.56 → 2724.70] Yeah.
[2724.78 → 2726.16] And so much fun to play with.
[2728.14 → 2729.84] Somehow Nick wins the day.
[2729.96 → 2730.76] Goose it is, folks.
[2731.38 → 2733.22] He's just trying to goose up listens.
[2733.72 → 2735.04] Oh, I love that.
[2735.56 → 2736.60] And cable killed.
[2736.82 → 2737.24] And yeah.
[2740.48 → 2741.06] All right.
[2741.10 → 2742.96] Thank you for tuning in to JS Party this week.
[2743.08 → 2746.04] Tune in live on Thursdays at 1 p.m.
[2746.06 → 2746.44] U.S.
[2746.56 → 2749.12] Eastern at changelog.com slash live.
[2749.54 → 2752.12] Join the community and slack with us in real time during the shows.
[2752.40 → 2753.94] Head to changelog.com slash community.
[2753.94 → 2755.18] And do us a favour.
[2755.34 → 2756.52] Share this show with a friend.
[2756.82 → 2758.02] We're just going to have a podcast.
[2758.24 → 2759.80] Go into Overcast and favourite it.
[2760.28 → 2762.54] And thank you to Vastly, our bandwidth partner.
[2762.90 → 2764.40] Head to fastly.com to learn more.
[2764.80 → 2767.40] And we move fast to fix things around here at changelog because of Rollbar.
[2767.60 → 2769.34] Check them out at rollbar.com.
[2769.60 → 2771.66] We're hosted on Leno cloud servers.
[2772.02 → 2773.62] Head to leno.com slash changelog.
[2773.70 → 2775.08] Check them out and support this show.
[2775.54 → 2777.52] Our music is produced by Break master Cylinder.
[2777.92 → 2780.96] And you can find more shows just like this at changelog.com.
[2781.10 → 2782.08] Thanks for tuning in.
[2782.08 → 2783.14] We'll see you next week.
[2797.98 → 2799.98] Break to win and break to lose.
[2800.18 → 2801.98] It's easier break to wrap your shoes.
[2802.20 → 2803.90] And these are the break.
[2804.18 → 2806.32] Break it up, break it up, break it up.
[2807.00 → 2808.10] Chris Mike dropped me.
[2808.10 → 2811.70] That what?
[2811.86 → 2812.28] Oh my gosh.
[2812.28 → 2814.22] I was going to say, I wish we had like the video for folks.
[2814.22 → 2814.66] Can we?
[2814.80 → 2816.12] Chris just leaning back.
[2817.24 → 2817.68] Vaping.
[2817.80 → 2821.24] And he's like, are either of you confused when I say JavaScript?
[2821.54 → 2822.66] I'm like, oh my gosh.
[2823.02 → 2824.60] He's just owning us over there.
[2824.90 → 2831.48] I just want to like save that sound bite of Chris saying what?
[2831.48 → 2837.68] And then in future episodes, just intersperse to the podcast.
[2839.34 → 2842.00] That is a soundboard moment for sure.
[2842.90 → 2843.34] What?
[2845.62 → 2846.02] 100%.
[2846.02 → 2847.38] 100%.
[2847.38 → 2849.50] And you could just do that as a cut.
[2849.62 → 2851.50] Like you could put something in before it.
[2851.66 → 2852.94] And just like somebody says something.
[2853.08 → 2853.16] You go.
[2854.16 → 2854.60] What?
[2854.60 → 2855.20] What?
[2855.98 → 2856.38] What?
[2859.64 → 2860.14] What?
[2860.14 → 2860.30] Oh my gosh.
[2860.76 → 2860.84] What?
[2860.84 → 2860.86] What?
[2860.86 → 2860.96] What?
[2861.00 → 2861.24] What?
[2861.24 → 2861.60] What?
[2861.60 → 2861.70] What?
[2863.92 → 2864.82] What?
[2864.82 → 2869.14] What?
[2870.08 → 2870.62] What?
[2870.66 → 2871.40] What?
[2871.40 → 2872.66] What?
[2873.34 → 2873.48] What?
[2873.48 → 2877.98] What?
[2877.98 → 2883.98] What?
[2884.04 → 2885.12] What?
