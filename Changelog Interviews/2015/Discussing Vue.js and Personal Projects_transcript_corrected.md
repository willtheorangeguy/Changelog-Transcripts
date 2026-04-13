[0.00 → 2.56] I'm Evan You, and you're listening to The Changelog.
[10.56 → 14.32] Welcome back everyone. This is The Changelog, and I'm your host, Adam Stachowiak.
[14.44 → 20.66] This is episode 184 and on today's show, Jared and I are joined by Evan You talking about Vue.js.
[21.30 → 28.02] We had four awesome sponsors for this show, Code Ship, Upbeat, Braintree and also DigitalOcean.
[28.02 → 32.90] Our first sponsor is Code Ship. Got an awesome e-book out there totally for free.
[33.26 → 39.18] It's a 21-page deep dive into why containers and Docker are the future.
[39.30 → 46.32] This free e-book is about the rise of the container stack and why Docker and its ecosystem and community play such a big part in it.
[46.66 → 51.42] Now, when you download this e-book, you'll also get access to three other super secrete books.
[51.52 → 55.20] So go check this out. Resources.CodeShip.com slash e-books.
[55.20 → 58.10] I'll put the full URL in our show notes. So check that out.
[58.20 → 59.60] And now on to the show.
[67.70 → 70.32] Hey everyone, we're back. We got an awesome guest with us today.
[70.46 → 71.68] Evan You is joining us.
[72.24 → 79.12] Jared, it's kind of interesting because this show kind of kicked off with the very first issue submitted to Ping.
[79.16 → 80.14] And that was Evan.
[80.14 → 83.02] Evan You is a long time ago, though.
[83.62 → 85.30] That was like forever ago, basically.
[85.66 → 87.58] So he's our very first Ping. What'd he say?
[88.72 → 92.10] He said, can you cover Vue in Change Law Weekly? We did.
[93.56 → 95.50] And we were happy to do so.
[95.50 → 107.22] And recently he wrote us again and said, hey, let's talk about Vue on the podcast, which sometimes it's kind of hard to approach people and ask if we can talk about your thing.
[107.38 → 109.36] But he made a compelling argument.
[109.64 → 111.76] He listed multiple reasons why it's interesting.
[111.94 → 114.28] And I said, yeah, that actually does sound pretty interesting.
[114.44 → 114.94] Let's do it.
[115.70 → 116.32] Let's do it.
[116.32 → 120.34] And so, Evan You, you created Vue.js.
[121.22 → 121.44] Yep.
[121.80 → 125.60] Before we dive deep into that, obviously we're going to talk about that quite extensively.
[126.46 → 129.82] It's always interesting to kind of dive a little further into our guests.
[130.10 → 131.68] So tell us a bit about yourself.
[131.86 → 133.06] How do you introduce yourself?
[133.48 → 134.04] What do you do?
[134.86 → 135.14] Right.
[135.28 → 136.94] So I'm Evan You.
[136.94 → 142.56] I currently work at Meteor as a core dev and Vue.js is my personal project.
[143.34 → 146.56] And before joining Meteor, I was at Google.
[146.74 → 149.50] I worked at Google Creative Lab for a bit over two years.
[150.24 → 155.08] And before that, I went to Parsons, Parsons School for Design.
[155.66 → 163.56] I went to a master's program called MF ADT, which is Master of Fine Arts in Design Technology, which is a fun program.
[164.22 → 164.44] Wow.
[164.66 → 164.98] Okay.
[164.98 → 168.84] So that kind of makes sense why you say design, code, and things in between.
[169.30 → 169.44] Yep.
[170.08 → 172.46] So can you unpack that for us a bit more?
[173.28 → 173.80] Sure.
[174.00 → 179.66] So I started out doing some design on my own.
[179.96 → 185.84] When I was in college, I studied something completely unrelated to what I'm doing right now.
[186.46 → 192.12] But I have always been interested in designing and just trying to build the things that I designed.
[192.12 → 194.22] And it was really fun.
[194.22 → 204.90] And so a lot of my time was spent playing with Flash and trying to, you know, just crank out things that I think is creative and fun.
[205.14 → 210.54] And then that led to sort of the situation where I don't know what I was going to do when I graduated.
[210.54 → 219.94] And then I was like, okay, I need to find some place where I can combine two of my interests, you know, design and code.
[220.62 → 226.54] And that was, so I looked around and Parsons had this type of program, which looked pretty fun.
[226.54 → 234.04] And so I went there and ended up doing a lot of code experiments on the web.
[234.34 → 242.80] And then somehow that got me the opportunity to work at Google Creative Lab, which was also pretty fun.
[242.90 → 245.22] Had a lot of crazy experimental stuff in there.
[245.22 → 250.84] Yeah, that's, and I started working on Vue when I was at Google Creative Lab.
[251.04 → 255.14] And that's gradually evolving to what it is today.
[255.14 → 257.44] But it started like more than two years ago.
[257.52 → 259.12] It was a tiny experiment.
[259.90 → 260.30] Wow.
[260.38 → 260.56] Okay.
[260.62 → 267.32] So this is a two-year thing that you've been, I guess, that was two years ago when you started working at Google Labs?
[267.32 → 271.56] That's almost two, three years ago when I started.
[271.82 → 274.38] I started on Vue around two years ago.
[274.86 → 275.26] Okay.
[275.54 → 275.72] Yeah.
[276.02 → 280.04] Did any of your crazy experiments at Google Labs make it out into the wild?
[281.36 → 286.28] So I kind of want to clarify, like the place I worked at is called Google Creative Labs.
[286.38 → 289.08] It's like not the Google X, right?
[289.18 → 293.40] So Google Labs is yet another thing, which is no longer in existence.
[293.72 → 294.10] Right.
[294.10 → 297.88] Google X is this high-tech-like branch.
[298.16 → 304.24] And Google Creative Lab is more like half marketing, half UI prototyping.
[304.56 → 307.24] So we do a lot of internal prototypes.
[307.70 → 310.68] We did the UX prototyping for Google Glass.
[310.84 → 314.30] We did a bunch of stuff for the Google iOS search app.
[314.30 → 323.64] We were also, we were one of the responsible party behind the Google, the rebranding in 2015.
[324.10 → 326.42] That was a big deal, too, that rebranding this.
[326.80 → 328.76] So, I mean, I think it went over well.
[329.18 → 329.76] Everybody likes it.
[329.88 → 330.10] Yeah.
[330.42 → 334.92] It was pretty interesting because we actually had been pushing for quite a while.
[335.20 → 339.68] But it actually went out after I have already left Creative Labs.
[339.68 → 348.34] So it was pretty fun to see something you touched upon, you know, just going live after so long you almost forget about it.
[349.24 → 356.46] Why don't you take us further back, like before Vue, before Google, you know, how did you kind of get into what you're doing?
[357.36 → 358.34] Give us the backstory.
[358.34 → 359.02] Sure.
[359.98 → 365.28] So as I mentioned, I did a lot of Flash when I was still in high school, I believe.
[366.34 → 375.68] I have always been just fascinated by those, you know, really flashy websites, just fancy stuff.
[375.80 → 377.88] And I want to figure out how to make them.
[378.14 → 382.22] I believe my first web page was built with Frontage.
[382.22 → 391.30] I basically copied the markup from just a random website I saw and tried to mould it into what I wanted to look like.
[392.28 → 394.46] That was a fun experience.
[394.82 → 397.18] But at that time, I have no idea what's underneath.
[397.48 → 399.24] Like, I can't read the markup.
[399.34 → 400.74] I can't really read.
[401.38 → 404.02] I didn't even know what those script tags did.
[404.36 → 404.96] Right, right.
[404.96 → 413.46] So, and later on, I started playing with Flash because it just felt a bit more visual than Frontage, you know.
[413.82 → 418.24] And at that time, it was still using, I believe, ActionScript 2 or something.
[418.88 → 419.14] Okay.
[419.26 → 422.48] It was a really primitive scripting language.
[423.24 → 428.60] All the things I could do with it was just, like, play, pause, go to this frame, go to that frame.
[428.60 → 431.20] Doing small animations.
[431.70 → 437.24] And then Adobe released ActionScript 3, which was more like a real programming language.
[437.52 → 443.68] So I had to sort of step up the game and actually learn proper how to write code.
[444.40 → 449.86] But it was nothing like a real, like, computer science background thing.
[449.94 → 455.64] It's more like I want to build something, so I had to learn how to do it process.
[455.64 → 459.02] So I mostly picked up all the programming stuff by myself.
[460.06 → 464.78] I've got to ask you, because it's not often we have somebody who loves Flash or at least came from that.
[464.94 → 469.66] I guess we all kind of came from that era, but I can't say to myself I've done a lot with it.
[469.88 → 473.20] But if I say too advanced, what does that mean to you?
[473.74 → 475.66] Oh, yeah, I remember that studio.
[476.10 → 478.02] They have all these crazy websites.
[478.02 → 485.04] Yeah, I think I had one of their versions, like, version 2 or something.
[486.00 → 490.98] Like, I remember they built, like, multiple versions of their website.
[491.54 → 495.54] Every time it's, like, a completely different layout, different intro animations.
[495.96 → 496.00] Yeah.
[496.42 → 498.22] Yeah, those were crazy times.
[498.40 → 499.76] The art was so amazing, right?
[499.82 → 504.22] Like, that's what always fascinated me about, like, what was Flash in that era was, like,
[504.22 → 510.10] there's a very particular font, you know, all these, like, pixel fonts and, you know,
[510.18 → 512.14] and this artistic style to it.
[512.16 → 514.02] Like, it had a cool thing going for it.
[514.34 → 515.48] I kind of miss a little bit of that.
[515.54 → 515.96] What about you?
[516.04 → 516.46] I do.
[516.78 → 517.02] Yeah.
[517.48 → 518.22] I think it's...
[518.78 → 521.48] Especially to advanced, Doc, because they're the best.
[521.94 → 523.26] Like, there's nobody better than that.
[523.26 → 530.00] Yeah, they're probably, like, one of a kind in doing this type of, like, Flash-based animations.
[530.00 → 538.06] I believe I even have a copy of a source file of one of their sites.
[538.20 → 543.54] It's basically reverse-engineered or something so that I can look into it and, like, copy
[543.54 → 548.00] some of the teens and some key frames out of it to use it in my own projects.
[549.12 → 549.68] Yeah.
[550.00 → 550.56] Wow.
[550.68 → 551.48] That's crazy, man.
[552.56 → 555.02] So, roots go back to Flash and even to advanced.
[555.10 → 555.70] That's really cool.
[555.88 → 556.92] I'm impressed.
[556.92 → 559.76] I don't know many people who know of them.
[560.34 → 563.44] And when you do, you know they love them because they're really the best way they've
[563.44 → 563.64] done.
[564.20 → 566.50] Too advanced mean nothing to me, Adam.
[566.76 → 570.68] So, I was starting to look at 2LifeCrew stuff once you said that.
[570.76 → 572.68] So, I'm kind of off on a tangent over here.
[573.28 → 574.98] That means more to me than too advanced.
[575.12 → 579.56] Although, tooadvanced.com right now is just, like, a completely black page.
[579.64 → 582.06] So, maybe it's because I don't have Flash, and they're still rocking it all.
[583.22 → 588.56] I mean, it's, like, seriously just complete blackness in a modern...
[588.56 → 588.88] I don't doubt it.
[588.88 → 590.30] Yeah, I must have Flash installed.
[590.60 → 591.06] I don't know why.
[591.08 → 593.80] I'm in Chrome because that's just Safari, which...
[593.80 → 594.18] Oh, yeah.
[594.32 → 595.02] I'm in Chrome.
[595.52 → 596.48] So, in Chrome it works fine.
[596.58 → 597.64] I'm not sure if they still...
[597.64 → 599.28] Wait, it's 2Advanced, right?
[599.34 → 600.08] Yeah, the number 2.
[600.44 → 601.88] Yeah, 2Advanced.com.
[602.56 → 603.14] Like, the number 2.
[603.16 → 604.18] Oh, yeah, they guys are old school.
[604.28 → 607.46] It's still loading, like, up to 90, like, with a counter on how much it's loaded.
[608.46 → 610.10] It's a completely Flash website.
[610.96 → 612.20] Yeah, it's still pre-Flash.
[612.20 → 612.76] Wow.
[614.18 → 614.90] That's amazing.
[615.46 → 618.62] I don't want to go too deep into that, but, I mean, I never...
[618.62 → 623.08] We've never had anybody on the show that knew of 2Advanced, so I had to drop that question
[623.08 → 624.26] for you to see if you were familiar with them.
[624.26 → 625.32] I'm surprised I'm with the first one.
[625.32 → 629.18] Copyright 2011, so I'm wondering if they've moved on.
[630.60 → 631.68] They probably have moved on.
[631.76 → 634.16] Well, I think the web has moved on, so they had to.
[635.44 → 635.84] Right?
[635.96 → 636.72] They're in the dust.
[637.28 → 643.08] So, I guess we can move on as well to Vue, which is kind of the onus for the conversation
[643.08 → 643.38] here.
[644.78 → 651.66] Vue.js, now that's V-U-E for those listening, not V-I-E-W, which is probably what you'd assume
[651.66 → 653.66] is a...
[654.24 → 657.24] I'm not going to call it yet another client-side framework.
[657.34 → 661.20] I was going to make jokes about, you know, it's been a few weeks since we've had a JS
[661.20 → 663.60] framework on the show, Adam, but it actually has been longer.
[663.60 → 664.60] It's been...
[664.60 → 672.66] All the way back to 160 in June was ampersand, and then previous to that, if you count React,
[672.74 → 674.60] I guess, which isn't...
[675.12 → 678.58] We know that's actually a Vue layer, 149.
[678.58 → 686.88] So, you know, once every three or four months, usually, we bring up JavaScript front-end
[686.88 → 689.26] tooling, and it's about time.
[689.38 → 690.68] So, let's talk about Vue.
[690.76 → 696.22] It seems like it's kind of the silent assassin that I hadn't personally heard of, but is growing
[696.22 → 698.54] in popularity and seems to have quite a bit of merit.
[699.34 → 702.00] You said you started it when you were at Google Creative Labs.
[702.50 → 705.38] Why did you start it originally?
[705.38 → 705.86] Okay.
[706.34 → 713.28] So, primary reason was I was looking for something that's specifically good for what I was doing.
[714.12 → 720.80] We did a lot of UI prototyping, and those projects usually involve a lot of interactive content,
[720.98 → 726.32] interactive UI, but at the same time, we had to do it really fast because the design changed
[726.32 → 726.94] really often.
[727.42 → 729.94] We crank our ideas very, very fast.
[729.94 → 736.10] So, the pace kind of demands a solution that just makes some of the common UI tasks easy,
[736.30 → 741.62] but also don't overwhelmingly complex, right?
[741.78 → 744.94] We were using Angular for some of the projects, and we just felt...
[745.90 → 747.78] I really like the data-binding parts.
[748.48 → 755.08] It makes your UI more declarative, but at the same time, Angular is complex.
[755.08 → 761.88] It introduces a lot of concepts that I simply didn't need at all, and I felt there ought to
[761.88 → 766.40] be something simpler but provide the same benefits of a data-driven view.
[767.58 → 775.42] So, and also, it was partly also because I was curious on how Angular implemented it.
[775.42 → 782.64] It was somewhat a research project where I want to, you know, just dig into under the hood
[782.64 → 789.40] and see what is going on, how did they do it, and sort of figure out what I can do.
[789.50 → 791.12] Maybe I can build something like that, too.
[793.02 → 799.92] Yeah, and so it's half experiment, half out of the, you know, the need to use something
[799.92 → 802.38] for the projects I was working on.
[802.38 → 808.14] And if you had to describe it in a landscape of the current set of frameworks,
[808.26 → 816.32] so just throw out Angular, Ember, React with Redux, and such things, Aurelia, Ampersand,
[817.20 → 821.38] which kind of is, you know, you can lay those out sort of in a continuum of, like,
[821.74 → 826.78] lightweight to heavyweight, and, like, batteries included to more library-based.
[827.02 → 828.60] Where would Vue fit into that landscape?
[828.60 → 833.08] It's probably closest to React in that aspect.
[833.40 → 839.84] So it's more like Vue.js core is the V in the MV star system.
[841.22 → 843.28] It's strictly just a view layer.
[843.62 → 850.24] It concerns itself with you grab some state, you declare a view, and you render something
[850.24 → 850.92] onto the page.
[851.02 → 852.34] That's the job it does.
[852.34 → 861.10] But at the same time, so it started out as just a core library, and it intends to stay
[861.10 → 861.56] that way.
[862.40 → 865.60] It's really just a dropping type of thing.
[866.04 → 871.94] Like, in that aspect, it's even a bit simpler to get started with than React, because with
[871.94 → 876.84] React, you sort of need to do some JSX transpiration to get off the ground.
[876.84 → 881.76] But with Vue, it's literally just grab it off the CDN, and you can just get up and going.
[883.36 → 885.66] And then when you reach a...
[885.66 → 888.16] So Vue core packs a bunch of things.
[888.22 → 889.28] First is data binding.
[889.54 → 891.44] Then there is the component system.
[892.08 → 900.56] And it includes some transition effect helper to make it easier to build dynamic stuff.
[900.56 → 905.26] But out of that, it doesn't really include routing.
[905.48 → 908.14] It doesn't include any sort of opinionated data layer.
[908.42 → 912.22] It doesn't concern itself with how you bundle or structure your app.
[913.22 → 917.60] It stays out of your way if you simply want to use it as a view layer.
[917.96 → 922.92] But similar to the React ecosystem, there's React router, there's Redux.
[923.88 → 928.80] So VJS sort of provides you with an optional view router.
[928.80 → 932.04] It has a set of opinionated build setup.
[932.32 → 939.82] If you use Browser and Webpack, then you can use some transforms to write your view components
[939.82 → 947.24] in a very web component-like format, which in a single file, you sort of encapsulate the
[947.24 → 950.24] style, the template, and the script for your component.
[950.24 → 958.02] So it kind of grows out to a more opinionated framework-like experience if you are into that.
[958.22 → 959.94] But it's totally optional.
[960.68 → 962.80] So what's the sweet spot?
[962.94 → 967.78] I mean, for you, when you're building something on Vue, you're using all the components?
[967.92 → 970.66] Are you using Vue just for the view layer?
[971.82 → 973.72] How is it supposed to be used?
[973.72 → 974.12] Right.
[974.90 → 980.52] So I think the beauty of it is it doesn't really force you into one specific way of using it.
[981.32 → 987.86] The point being, a lot of people recently in the Laravel community are picking up Vue.
[988.30 → 994.76] And for a lot of them, their primary experience is building fully backend rendered apps.
[995.60 → 1000.18] Most of their stuff is rendered by the server side and just spit out to the front end.
[1000.18 → 1002.90] But they want to have interactivity.
[1003.06 → 1007.92] They want to have sort of like a mini SPA on each page.
[1008.86 → 1015.80] And full-blown frameworks like Angular or Ember doesn't really fit into that need well.
[1016.30 → 1022.10] It feels like such an overkill when you just want to add simple reactivity to a server side
[1022.10 → 1022.70] render page.
[1024.24 → 1028.76] So a lot of them just use Vue for that specific purpose, right?
[1028.76 → 1031.86] You just grab it from the CDN and you can just get going.
[1033.46 → 1039.86] But maybe when you build the next app, you want to grow the client-side presence.
[1040.68 → 1047.00] Or maybe it's just a different app that demands a different UX, which an SPA was suited better.
[1047.00 → 1052.84] Then they can grab the additional parts, and they can still use Vue, but they can build an app
[1052.84 → 1060.66] that's more single page oriented, more fully structured as a client-side app.
[1061.30 → 1069.00] So the same core principle applies in both situations, which I think is the power of this type of...
[1069.48 → 1071.92] How the framework presents itself.
[1071.92 → 1075.50] You can pick what you need to achieve what you want.
[1076.12 → 1076.92] Very cool.
[1077.06 → 1080.34] And it seems like you just reached 1.0 here recently.
[1080.86 → 1088.38] In preparation for this, you sent us a link to an excellent post called Vue.js, a reintroduction.
[1088.38 → 1095.64] Which highlights some of what Vue offers and compares and contrasts it with the frameworks
[1095.64 → 1096.50] that we've been talking about.
[1097.02 → 1100.36] You have one, two, three, four, five major points there.
[1100.44 → 1103.94] I think what we'd like to do is take a quick break here from a sponsor.
[1104.70 → 1107.86] And then on the other side of the break, what we'll do is kind of talk through those bullet
[1107.86 → 1111.84] points, use them as kind of waypoints that we can use to dive into other conversations
[1111.84 → 1113.74] about Vue in detail.
[1113.82 → 1114.16] Sound good?
[1114.98 → 1115.12] Yeah.
[1116.06 → 1116.56] All right.
[1116.62 → 1117.10] Let's do that.
[1117.16 → 1117.62] We'll be right back.
[1117.62 → 1125.16] Guess what, everyone?
[1125.44 → 1130.54] Upbeat is announcing their Node.js beta right here, right now, exclusively to our listeners.
[1131.44 → 1136.48] Upbeat combines performance metrics, release tracking, and error logging into a single simple
[1136.48 → 1137.04] service.
[1137.52 → 1142.14] And with all of your data in the same place, they're able to do smart things with it and
[1142.14 → 1143.58] help you make wiser choices.
[1144.20 → 1146.40] Upbeat integrates with your code base through Git.
[1146.40 → 1149.70] It makes monitoring and debugging your production apps much faster.
[1150.28 → 1155.48] It's free for an unlimited number of users and until now has only been available for Django
[1155.48 → 1156.32] and Flask.
[1156.60 → 1161.66] But now they're launching a private beta for Node.js and sharing it with our listeners
[1161.66 → 1162.16] first.
[1162.62 → 1164.54] So go check it out and sign up for the beta.
[1165.04 → 1167.48] Head to OpBeat.com slash changelog.
[1167.48 → 1172.82] That's O-P-B-E-A-T dot com slash changelog.
[1172.82 → 1176.72] All right.
[1176.78 → 1181.80] We are back speaking with Evan You about his awesome JS framework, Vue.js.
[1182.40 → 1187.44] Evan, you got five points here in this blog post, which we will definitely link up in
[1187.44 → 1187.96] the show notes.
[1188.66 → 1194.54] Point one is reactivity, in which you say that keeping the state and the view in sync is hard,
[1194.64 → 1195.20] or is it?
[1195.70 → 1198.20] You begin to describe the reactivity in Vue.js.
[1198.20 → 1199.08] Can you take us through that?
[1200.16 → 1200.58] Sure.
[1201.16 → 1209.90] So reactivity in Vue.js is one of the unique things that I haven't seen a similar
[1209.90 → 1212.10] implementation in any other framework, I believe.
[1212.64 → 1220.28] So the core of it is Vue.js converts plain JavaScript objects using some ES5 features called
[1220.28 → 1224.12] object-defined property and makes all these properties reactive.
[1224.12 → 1232.12] So when you retrieve a property or when you mutate a property, Vue.js knows under the hood,
[1232.54 → 1242.14] and so it's able to track the dependencies and be able to reactively perform DOM manipulations
[1242.14 → 1242.62] for you.
[1243.18 → 1251.10] So let's say when you have an object with a property A and you use Vue.js's emulating system
[1251.10 → 1255.94] to bind a moustache tag to the property.
[1256.98 → 1263.06] And so once you do that, the Vue and your data is essentially linked.
[1264.08 → 1268.92] And whenever you change the data, the Vue just updates, and it just becomes fully automatic.
[1268.92 → 1280.06] So instead of mutating some data and calling a re-render, you just change the data.
[1280.20 → 1282.54] So there's no need to call re-render any time.
[1283.64 → 1292.12] And in comparison, there are some other frameworks that use a similar model-based mechanism where
[1292.12 → 1298.12] you have reactive model objects, and you bind to your Vue and you can mutate them.
[1298.26 → 1305.74] But the thing is, none of them actually use this plain JavaScript object syntax.
[1306.64 → 1313.40] So for example, in Knockout, you have to create KO.observables.
[1313.94 → 1316.16] And in Ember, you have to create Ember objects.
[1316.16 → 1321.02] But in Vue, it's just plain JavaScript objects.
[1321.22 → 1326.86] Like you can do an AJAX call, you get some JSON, you parse it into plain objects, and you
[1326.86 → 1329.34] shove it into a Vue instance and the Vue updates.
[1329.90 → 1334.96] So like you said, a lot of these frameworks require you to use like Ember. Create object
[1334.96 → 1339.68] or something and to use their specific objects which have observability built into them.
[1340.02 → 1340.46] Right.
[1340.88 → 1343.76] And you have to use getters and setters in certain ways in some cases.
[1343.76 → 1348.50] I assumed you were using object. Observe or some sort of new feature, but you're using
[1348.50 → 1353.40] define property, which is available in like every major browser, right?
[1354.26 → 1357.20] Yeah, it's available down to IE 9.
[1357.52 → 1363.60] So Vue doesn't support IE 8 and below, but anything above IE 9 is fully supported.
[1364.14 → 1365.42] I don't think that's problematic.
[1365.62 → 1371.76] I saw just today that Microsoft, as of like January, is deprecating all the way back to
[1371.76 → 1372.36] IE 10.
[1372.48 → 1377.00] So 8, 9, and 10 will be officially unsupported, which is nice.
[1377.40 → 1378.14] It's good stuff.
[1378.28 → 1378.68] It is.
[1379.56 → 1380.62] Keep moving it forward.
[1382.08 → 1383.14] So, hmm.
[1383.80 → 1385.66] Are there any drawbacks to this method?
[1385.72 → 1390.26] It seems like if it was, you know, just use define property, it seems like the Ember team
[1390.26 → 1391.46] would have been using this feature.
[1391.58 → 1397.28] It seems like, you know, in Knockout they would have been just using define property because
[1397.28 → 1400.00] plain old objects is easier.
[1400.14 → 1401.66] It is more straightforward.
[1402.02 → 1403.40] How do you accomplish this?
[1404.56 → 1404.80] Right.
[1404.80 → 1412.14] I believe one of the reasons other frameworks don't pick it is either it has to support
[1412.14 → 1417.88] IE 8 because object define property is a feature that is unshamable in IE 8.
[1418.12 → 1421.72] Like there's no way to shim it if the engine doesn't support it.
[1421.72 → 1429.14] So if you are to support IE 8, then this mechanism is just out of the question.
[1430.40 → 1435.70] But if you are willing to drop support for IE 8, then this is totally feasible.
[1437.08 → 1439.42] So there is some...
[1439.42 → 1446.34] So it's a technical, very technical comparison with, say, an Angular's mechanism, which is
[1446.34 → 1454.60] dirty checking or React's mechanism, which is virtual DOM diffing, I would categorize the
[1454.60 → 1459.22] two into the pull-based mechanisms and the push-based mechanism.
[1460.10 → 1468.52] So all the like, Knockout or Ember or Vue are sort of in the push camp because when the
[1468.52 → 1475.80] change happens, the reactive model will push the changes to the Vue to automatically trigger
[1475.80 → 1477.24] updates in the Vue.
[1477.88 → 1483.60] And in comparison, Angular and React both are pull-based systems.
[1484.10 → 1488.68] Essentially, you need to give the system a signal saying, hey, something might have changed.
[1489.26 → 1491.12] And now you need to...
[1491.12 → 1495.14] So in Angular, you need to iterate over all the watchers to do the dirty checking.
[1495.32 → 1499.90] And in React, you render a new virtual DOM tree and diff it with the old one.
[1500.56 → 1502.84] But these things don't happen automatically.
[1502.84 → 1505.32] You sort of have to give the system a signal.
[1505.78 → 1510.48] And in Angular, it's somewhat baked into event handlers.
[1511.08 → 1512.42] So Angular does it for you.
[1513.08 → 1519.44] But when you are, say, Angular 1, when you are in a timeout, you have to manually call
[1519.44 → 1524.18] scope digest or scope apply in order to, like, tell Angular something has changed.
[1524.28 → 1524.52] Right.
[1524.52 → 1526.60] And in React, you have to call set State.
[1527.56 → 1532.44] If you directly mutate your state, there's no way for React and Angular to know it has
[1532.44 → 1532.82] changed.
[1533.26 → 1539.96] The comparison is that push-based mechanisms have better runtime performance, but it has
[1539.96 → 1546.72] a slightly higher initialization cost because you have to set up all the observation objects,
[1546.90 → 1548.80] the watchers, the dependency tracking.
[1548.80 → 1551.32] Like, you have to do all of that at boot up.
[1552.24 → 1557.36] You have to be, the system has to warm up and be ready for any future changes.
[1557.52 → 1562.82] But once that's set up, all the hot updates are really fast and efficient because if you
[1562.82 → 1567.66] change one single property, then only the views that's interested in that property would
[1567.66 → 1569.86] get notified and get updated.
[1569.86 → 1577.74] But in a pull-based system, because it's somewhat brute force, obviously, there's a lot of optimization
[1577.74 → 1582.08] in there, but the essence of it is we don't really know what has changed.
[1582.28 → 1583.74] We just know something has changed.
[1583.84 → 1588.78] So we have to, you know, either go through all the watchers or go through the whole virtual
[1588.78 → 1591.16] DOM tree to figure out what exactly has changed.
[1591.58 → 1598.34] So you do a lot of extra work when something has changed in order to update the view.
[1598.34 → 1604.20] So let's say you have a huge app, and you are changing only a small piece of state.
[1605.96 → 1612.34] The push-based implementations would probably take a bit longer to start up, but subsequent
[1613.02 → 1614.58] changes would be more efficient.
[1615.00 → 1623.66] But a pull-based system could start up relatively faster, but its hot updates would have performance
[1623.66 → 1624.32] implications.
[1624.32 → 1631.68] And it depends on how the implementation works and how optimizable it is.
[1632.74 → 1638.50] So dirty checking is hard to optimize, but virtual DOM is somewhat more optimizable because
[1638.50 → 1644.58] how in React you can implement a per-component method called shootComponentUpdate to sort of,
[1644.58 → 1647.72] you know, short-circuit some of the virtual DOM diffing.
[1647.72 → 1650.34] But it's still a manual process.
[1651.82 → 1656.02] So would you say that view is neither push nor pull then?
[1656.58 → 1658.00] It is in the push camp.
[1658.18 → 1658.42] Okay.
[1659.16 → 1660.00] Yeah, I might have.
[1660.56 → 1663.58] No, I just realized I might have gone into too many technical details.
[1663.84 → 1664.86] No, that's good.
[1665.34 → 1665.60] Okay.
[1665.80 → 1666.96] Go deep, please.
[1667.12 → 1667.64] Sure.
[1667.64 → 1667.68] Sure.
[1668.68 → 1672.98] So what about, so you're working with plain JavaScript objects.
[1673.68 → 1676.10] Obviously you have properties and properties can be functions.
[1676.24 → 1677.74] Can you then observe functions?
[1679.12 → 1681.36] So if you want to, yes, you can.
[1681.70 → 1683.94] You can put functions in your state.
[1683.94 → 1693.50] But the general advice is preferred to, because all the reactive parts in your app, especially
[1693.50 → 1699.08] in a Vue.js app, that represents the state of your application, right?
[1699.74 → 1707.10] And it's good if your state is playing objects that's serializable and permissible.
[1707.46 → 1710.14] Because functions are not really serializable.
[1710.14 → 1715.08] Like you wouldn't put functions in your, say, a JSON request.
[1715.76 → 1719.68] Like when you get some data from your server, the response wouldn't contain functions.
[1719.76 → 1719.92] Sure.
[1720.06 → 1720.22] Right?
[1720.94 → 1726.80] So most of the case, you kind of want to think of these reactive objects as things you would
[1726.80 → 1732.72] want to persist to the server or things that basically describe what your app state is
[1732.72 → 1737.26] like instead of putting arbitrary objects in it.
[1737.26 → 1744.72] So Vue is a little bit opinionated in that aspect because we want to use these reactive
[1744.72 → 1748.68] objects as the underlying source of truth to drive the Vue.
[1749.26 → 1753.94] So you want to keep it abstract, keep it clean and simple.
[1754.68 → 1759.86] So this offers two-way data binding in the sense of if you update it in the model, it updates
[1759.86 → 1760.24] the Vue.
[1760.32 → 1762.64] And if you update it in the Vue, it updates the model.
[1762.74 → 1762.92] Correct?
[1762.92 → 1763.32] Yeah.
[1763.86 → 1766.12] So Vue implements two-way data binding.
[1766.54 → 1772.06] But in my opinion, two-way data binding is kind of a word that's misunderstood by a lot
[1772.06 → 1776.48] because two-way data binding in its essence is just syntax sugar.
[1777.28 → 1784.70] What really happens under the hood is the user has triggered some input events.
[1784.70 → 1790.90] So the event triggers Vue to modify the state, which is the object.
[1791.60 → 1794.72] And because that object is modified, it triggers the Vue to re-render.
[1795.72 → 1802.92] So in fact, what's happening is still sort of like event triggering model update, model update
[1802.92 → 1804.12] triggering Vue to re-render.
[1804.30 → 1808.00] It's actually not that two-way if you think about it.
[1808.64 → 1811.14] It's just syntax sugar to make it easier to write.
[1811.14 → 1811.54] Sure.
[1814.28 → 1820.76] Aren't there times when your event triggers wouldn't necessarily want to re-render though?
[1821.12 → 1821.36] Right.
[1821.66 → 1825.74] So in that case, you just simply use event listeners instead of two-way bindings.
[1826.36 → 1828.46] So Vue gives you the options in that case.
[1829.20 → 1829.52] Yes.
[1830.82 → 1837.38] So two-way data binding, you know, I realize that you don't love the term, but people are
[1837.38 → 1838.10] used to that term.
[1838.10 → 1844.22] So with that particular aspect of Vue, you know, Ember famously had two-way data binding,
[1844.50 → 1850.04] this back and forth push and pull as a kind of flagship feature early on.
[1850.08 → 1853.60] And then they realized it's not actually always useful.
[1853.60 → 1856.44] And so let's allow people to turn it off and on.
[1857.42 → 1862.10] It's cool that Vue allows that kind of flexibility, but when it's on, and you're using it, when you
[1862.10 → 1867.32] have that feature on, are there performance implications that you found with Vue?
[1867.32 → 1867.92] Okay.
[1869.20 → 1875.90] So I think I want to take a step back and explain two-way data binding a bit more.
[1876.18 → 1882.70] So when we talk about two-way data binding, there are two types of things people would
[1882.70 → 1885.58] refer to, but they often confuse one with another.
[1885.58 → 1892.32] The first is strictly the form when you're handling form elements, form inputs.
[1893.22 → 1901.40] This type of two-way data binding is what, like say when you are typing into a field and
[1901.40 → 1907.54] the model updates and something else that's also bound to that property also updates.
[1907.54 → 1912.08] So this form-based two-way data binding, in my opinion, is just syntax sugar.
[1912.70 → 1918.84] There's another type of two-way data binding people talk about is binding a property on this
[1918.84 → 1924.90] component to another property on another component and keep the two in sync.
[1924.90 → 1930.10] And this is the problematic one that a lot of people don't like.
[1931.38 → 1936.68] That's why React sort of talks about how the data flow should be one-way.
[1936.78 → 1938.60] It should flow from a parent to a child.
[1939.00 → 1941.36] And that's actually what Vue is doing too.
[1942.06 → 1947.18] The default, the way you pass data from a parent component to a child component in Vue is
[1947.18 → 1950.94] also using something called props, and it's also one-way by default.
[1951.88 → 1959.94] And I think that's correct because a lot of these two-way binding between components
[1959.94 → 1967.70] becomes hard to understand and reason about in that these two properties are not the same
[1967.70 → 1967.96] thing.
[1968.04 → 1972.02] They don't have the same identity, yet we try to pretend they have.
[1972.96 → 1976.36] And that's the source of the confusion here, I believe.
[1976.36 → 1983.04] So I think the better way to do it is if the two properties should in fact be the same
[1983.04 → 1989.30] property, then they should in reality be the real same property on the same object.
[1989.80 → 1991.82] And that object should be the source of truth.
[1992.04 → 1998.52] And you have two components that observe the same object instead of two components each
[1998.52 → 2001.34] holding a copy of that property and try to keep them in sync.
[2002.98 → 2003.98] Does that make sense?
[2004.14 → 2004.48] It does.
[2004.56 → 2005.14] It does very well.
[2005.14 → 2011.94] I think it tees up very well our next bullet point on your list of things inside Vue, which
[2011.94 → 2012.62] is components.
[2012.82 → 2016.74] Maybe a little bit different from the component you just mentioned, or perhaps the same.
[2017.76 → 2024.06] Can you describe, I believe this would be akin to Angular's directives, or Ember, I guess
[2024.06 → 2025.12] they renamed theirs.
[2025.34 → 2026.86] I think they were Cues at one point.
[2026.94 → 2027.50] Now they're components.
[2028.32 → 2029.04] All these terms.
[2029.04 → 2031.04] Can you describe components in Vue.js?
[2032.08 → 2032.34] Sure.
[2033.34 → 2038.92] So I believe most of the major frameworks right now have converged on components.
[2039.56 → 2039.60] Right?
[2039.72 → 2042.26] Angular 2 is built around components.
[2043.00 → 2045.42] Ember is all about components.
[2045.60 → 2047.34] Now React has started with components.
[2047.48 → 2047.72] Right.
[2047.72 → 2050.52] So I think they more or less have...
[2051.20 → 2057.22] We have, like the whole ecosystem have sort of agreed that the component is a perfect
[2057.22 → 2058.96] abstraction for building user interfaces.
[2058.96 → 2064.84] And most of the UI can be represented as a tree of nested components.
[2065.64 → 2073.82] And each component would have its own state, have its own view, and should have some sort
[2073.82 → 2075.72] of logic encapsulated inside of it.
[2075.72 → 2081.32] And ideally, you want to build components that are self-contained and reusable.
[2081.72 → 2086.86] So when you build it, and you want to use it elsewhere, it should be easy and straightforward
[2086.86 → 2087.48] to do so.
[2088.96 → 2093.22] So I think that's what a general definition of components.
[2093.70 → 2096.78] And each framework sort of tackles it in a slightly different fashion.
[2096.78 → 2108.62] And a view, it's still pretty simple because when a lot of people first start with view, the only thing they know is they can create a view instance.
[2109.20 → 2109.30] Right?
[2109.42 → 2115.42] A view instance is essentially an object that binds a raw data object to a piece of DOM.
[2115.64 → 2115.92] Right.
[2116.28 → 2121.24] So these type of instances, if you think about it, that's a component.
[2121.92 → 2122.10] Right?
[2122.10 → 2126.72] If an instance can contain other instances, then we have the component tree we want.
[2126.90 → 2128.72] So that's exactly what view is doing.
[2129.62 → 2134.36] You define a bunch of options.
[2135.80 → 2139.34] You define a component by providing a bunch of options.
[2139.46 → 2141.34] For example, you can provide a template.
[2142.12 → 2148.92] You can provide a function that returns the initial state of that component, which is very similar to what React does.
[2148.92 → 2155.62] And you can provide other options, such as some methods that component might have.
[2156.76 → 2160.12] And you can provide computed properties.
[2162.44 → 2169.82] Essentially, it's like a class, but not exactly a class, but something like that.
[2169.96 → 2176.52] So when you create a component in view, you call view. Extend, then you're passing all the options, and you get a reusable constructor.
[2176.52 → 2178.52] Constructor function.
[2178.96 → 2182.56] And you can use that to create components, but it's imperative.
[2183.06 → 2189.98] So the recommended way is to register the component with a tag, an HTML tag, a custom element.
[2190.90 → 2200.74] So that becomes very similar to how web components work, how you define reusable web components, you register them as custom elements,
[2200.74 → 2204.66] and then you can nest them, compose them any way you want.
[2204.66 → 2209.22] So the view component development experience is very similar to that.
[2210.76 → 2217.68] But on top of that, view provides you the mechanism necessary to communicate between the components.
[2217.80 → 2222.68] For example, you can use the prop system to pass data from the parent to the child.
[2223.38 → 2227.96] And then components are event emitters, so they can dispatch events.
[2227.96 → 2236.96] So a parent component can listen to the events on the child so that the child can somewhat notify the parent that it needs to do something.
[2237.48 → 2250.38] So this sort of event, like triggering parent actions using events, decouples the child and parent because the child is only responsible for dispatching the event.
[2250.38 → 2254.72] And what exactly happens afterwards is up to the parent.
[2254.72 → 2261.08] And only the parent knows how to mutate its own state in reaction to that event.
[2262.84 → 2271.60] And then view also implements something that's very closely modelled after the web component spec.
[2271.60 → 2279.60] There is a mechanism called slots, which is previously content.
[2280.56 → 2290.78] So they recently, the spec drafters switched the content API to the slot API and view implemented that right before 1.0.
[2290.78 → 2297.22] So what the slot API does is allow you to compose these custom elements.
[2297.94 → 2303.98] So when you use a custom element, and you put other custom elements inside of it,
[2304.62 → 2308.76] so that custom element, because it has its own template, right?
[2309.18 → 2310.28] So what should we render?
[2311.00 → 2319.34] We need to somehow find a way to weave these runtime elements inside of it with its own template.
[2319.34 → 2320.80] So that's what slot does.
[2320.88 → 2325.14] It allows you to sort of better compose these components at runtime.
[2326.48 → 2335.62] It might be a bit hard to explain with words because the slot concept is somewhat hard to explain, I guess.
[2335.92 → 2340.92] But what it does is make components more composable.
[2341.18 → 2341.82] That's all it does.
[2342.68 → 2342.78] Right.
[2343.16 → 2345.20] So we solve several issues.
[2345.38 → 2348.00] First is how do we pass data from parent to the child?
[2348.00 → 2358.34] And the second issue is how do children notify their parents something has changed without being directly coupled to the parent?
[2359.02 → 2363.90] And the third question is how do we compose different components at runtime?
[2364.64 → 2375.34] So if we can solve these three questions, then we get a pretty good system where it allows us to build up more complex interfaces with these small building blocks.
[2375.34 → 2385.22] And this is very similar to what I believe what the web components people want us to be able to do eventually.
[2385.86 → 2389.62] And it's in fact, I believe, very similar to what Polymer is doing.
[2389.62 → 2396.26] The difference being that Vue is not specifically tied to the spec.
[2396.60 → 2398.54] It doesn't really rely on the polyfills.
[2400.86 → 2405.62] So you don't need to worry about, say, does this browser support this feature?
[2405.76 → 2407.48] Do I need to ship the polyfill or not?
[2407.48 → 2416.46] And you don't need to worry about it having inferior performance on an older browser simply because it doesn't support certain features.
[2417.40 → 2424.96] Well, once you have all those components set up, and they're decoupled but nested, and they're all ready to be used,
[2425.44 → 2429.82] what developers like to do is share them with themselves and with their friends.
[2430.12 → 2433.40] So it looks like you got some of that built in as well with modularity.
[2433.80 → 2434.74] That'll be our next topic.
[2434.74 → 2437.26] We do take another sponsor break at this point.
[2437.48 → 2437.76] Sure.
[2437.98 → 2441.74] On the other side, we'll talk about modularity, animations, and stability.
[2442.66 → 2443.26] Be right back.
[2449.74 → 2455.16] Braintree is all about making developer lives simpler with code for easy online payments.
[2455.56 → 2459.02] If you're searching for a simple payment solution, check out Braintree.
[2459.02 → 2466.96] For mobile app developers out there, the Braintree B.0 SDK makes it easy to offer multiple payment types.
[2467.40 → 2476.14] Start accepting PayPal, Apple Pay, Bitcoin, Venmo, traditional credit cards, and whatever's next, all with a single integration.
[2476.74 → 2479.56] Enjoy simple, secure payments that you can integrate in minutes.
[2480.00 → 2481.22] And developers, they've got you.
[2481.26 → 2483.46] Don't worry about taking days to integrate your payments.
[2483.96 → 2485.50] With Braintree, it's done in minutes.
[2485.50 → 2491.02] And if you don't have time, give them a call, and they'll handle the integration for you and walk you through it.
[2491.58 → 2495.36] Braintree supports Android, iOS, and JavaScript clients.
[2495.76 → 2502.94] They have SDKs in seven languages, .NET, Node.js, Java, Perl, PHP, Python, and Ruby.
[2503.38 → 2506.48] And their documentation is comprehensive, and it's easy to follow.
[2506.48 → 2515.70] To learn more and for your first $50,000 in transactions fee-free, go to braintreepayments.com slash changelog.
[2519.84 → 2520.98] All right, we are back.
[2521.06 → 2522.38] Let's talk about modularity.
[2522.66 → 2526.56] Once you have your components, Evan, how do you bundle them up and distribute them?
[2527.28 → 2527.48] Right.
[2527.48 → 2540.48] So currently, I think the mainstream way of organizing and building your web projects is using modules, right?
[2540.52 → 2541.96] Everyone uses modules today.
[2541.96 → 2547.40] So it's either common.js, AMD, or ES2015 modules.
[2548.02 → 2555.14] There are a lot of ways to do it, but the preferred way with Vue.js is you use either Webpack or Browser.
[2555.14 → 2560.60] So that indicates we want to write our components as common.js modules.
[2561.30 → 2571.90] But thanks to the transforms in these ecosystems, so you can use either Babel, Babel Loader or Bailiff,
[2572.32 → 2579.92] but both uses Babel to transpire your ES6 or ES2015 code into plain JavaScript.
[2580.26 → 2583.10] So you can use ES6 modules too.
[2583.10 → 2592.08] And Vue also, when you use Vue with Webpack or Browser, there are two Vue-specific tools.
[2592.56 → 2593.84] With Webpack, it's called Vue Loader.
[2594.38 → 2595.82] With Browser, it's called Verify.
[2596.46 → 2598.22] So these two do the same thing.
[2598.38 → 2603.18] They allow you to write your Vue components in a Vue-specific format.
[2603.84 → 2605.38] It's called a single-file component.
[2605.38 → 2609.38] As I would call it, it's very similar to Web Components 2.
[2609.78 → 2615.34] Essentially, in the same file, you have a style block, you have a template block, and you have a script block.
[2615.86 → 2619.66] So you have the three parts that's necessary that makes up your component.
[2619.66 → 2629.38] Because I think back when we built applications with Angular or some other client-side frameworks,
[2629.48 → 2634.20] it's very common for us to group, to structure our files based on the extension.
[2634.66 → 2637.10] You put all the HTML templates in the same folder.
[2637.58 → 2639.88] Then you put all the style files in the same folder.
[2640.04 → 2642.24] Then you put all the JavaScript in the same folder.
[2642.24 → 2650.40] But in the end, I came to the conclusion you shouldn't do that.
[2650.98 → 2652.08] The bad old days.
[2652.82 → 2658.76] They should be grouped based on what they are about.
[2659.64 → 2667.08] You have a template, you have a script file, you have a JavaScript.
[2667.08 → 2673.04] But they are all related to the same feature or functionality in your app.
[2673.14 → 2677.04] For example, this button that you're building.
[2677.90 → 2681.88] The button has its template, has its logic, has its styles.
[2682.16 → 2683.12] Why should they be separate?
[2683.24 → 2684.68] They should just be in the same file.
[2685.22 → 2690.22] So you have this single file that represents your button component, and you can just put it around.
[2690.22 → 2699.22] I think that's powerful, and I think it makes it easier for you to think in terms of components and develop components.
[2700.82 → 2705.62] And web components is a step in that direction and obviously a source of inspiration.
[2706.32 → 2711.36] And I think React sort of does that too, but in the way of shoving everything into JavaScript.
[2712.50 → 2716.86] You write JSX and styles in JavaScript so that it's a single file.
[2717.22 → 2719.04] But the idea is the same.
[2719.04 → 2728.06] So every component is in its own file, and it makes these things much easier to think about and to organize.
[2730.38 → 2731.04] And the good thing...
[2731.62 → 2735.52] So people may ask, why do you invent another component format?
[2735.76 → 2737.14] Why don't you just use web components?
[2737.38 → 2744.94] The answer is because few components are transpired using Webpack, you get to leverage the full power of Webpack.
[2744.94 → 2750.36] So you can use preprocessors inside your view components.
[2751.08 → 2757.80] So if you want to use SAS, less, or stylus for your style inside your component, yes, you can do that.
[2757.90 → 2761.84] Or if you want to write date templates for your view components, yes, you can do that.
[2762.38 → 2767.08] Or if you want to use CoffeeScript for all your scripts, yes, by all means.
[2767.08 → 2769.34] So that's the beauty of it, right?
[2769.38 → 2778.80] You have the same format for your components, but you also have the freedom to use all the preprocessors that you like inside of it.
[2778.80 → 2789.50] And in the end, because what View Loader does is essentially extracts out each part of your component, pipe them through the appropriate loaders that should be used.
[2790.18 → 2795.00] For example, if you write SAS in your component, it will pipe you through the SAS loader to process it.
[2795.44 → 2800.06] And eventually it assembles all the parts back together into a Commons module.
[2800.06 → 2806.16] So then these modules eventually get bundled together to become your app.
[2808.58 → 2811.06] And I think that makes it just...
[2811.68 → 2816.14] So when you use View Components, you don't have to throw away all the tooling that you're familiar with.
[2817.02 → 2823.14] You can leverage all the community contributions in the SAS community or in the LAS community.
[2823.36 → 2827.54] Or you can use the favourite language that you like.
[2827.54 → 2831.06] So you're still doing it the bad old ways, as Jared said.
[2831.36 → 2836.46] And when you run View Loader, it's dumping it into a single file.
[2836.56 → 2839.86] It's kind of processing, as you said, through the SAS file, through different compilers.
[2840.28 → 2841.76] Are you still writing it the old way?
[2842.94 → 2843.34] No.
[2843.68 → 2845.28] This all happens in memory.
[2846.24 → 2849.10] It's like Webpack is responsible for doing that.
[2849.16 → 2850.18] It's all hidden to you.
[2850.26 → 2851.86] You don't need to worry about that at all.
[2851.86 → 2855.02] All you need to do is just author your components.
[2855.42 → 2859.24] And Webpack is responsible for assembling it together into a final bundle.
[2859.94 → 2859.96] Gotcha.
[2860.08 → 2865.60] And these comments in the file, is that what allows the delimiter essentially to happen, to make that possible?
[2866.76 → 2868.60] Those comments are totally optional.
[2869.16 → 2873.24] The way you indicate your preprocessor, if you scroll down,
[2873.68 → 2878.88] you will see you provide the LAN attribute on your template or style blocks
[2878.88 → 2880.66] to indicate the language you're using.
[2880.66 → 2881.08] Gotcha. Okay.
[2882.00 → 2882.22] Yeah.
[2883.16 → 2883.68] Yes.
[2883.74 → 2887.94] And in addition to that, View doesn't really use Shadow DOM,
[2887.94 → 2890.34] because it's not a stable feature yet.
[2890.82 → 2894.92] But View provides a mechanism to simulate scoped styles.
[2895.66 → 2899.00] So if you add a scoped attribute to your style block,
[2899.22 → 2904.64] View will do some extra work on your styles and your templates.
[2904.64 → 2910.70] It rewrites them so that your style is encapsulated to the current component only.
[2910.80 → 2912.14] It doesn't affect other components.
[2912.58 → 2914.14] You also mentioned syntax highlighting.
[2914.26 → 2916.42] Can you break down how I guess that's possible?
[2916.46 → 2920.50] I'm not seeing how, I guess, you have one single file with many different languages in it,
[2920.54 → 2922.16] and it's still, you know.
[2922.36 → 2922.74] Right.
[2923.52 → 2927.78] That's really just providing a special View syntax highlighting file.
[2927.78 → 2937.48] I have a view.TM language, which is the syntax highlighting file that's format that's used by Sublime Text.
[2937.64 → 2944.78] But there are people who I have converted to use with Atom to other editors.
[2945.60 → 2949.44] So you're supporting the one for Sublime Text that essentially a .view file,
[2949.52 → 2955.12] you can mix CSS, SAS, whatever you want to choose, JavaScript, and HTML, Jade,
[2955.12 → 2956.68] whatever you choose for front-end languages.
[2957.04 → 2959.38] You can do that with View, and you maintain that yourself.
[2960.26 → 2960.66] Exactly.
[2961.00 → 2961.16] Okay.
[2961.90 → 2965.66] Well, it actually allows, so when you use a syntax highlighting file,
[2965.92 → 2968.98] like, you can actually just, like, declare, say, this block,
[2969.46 → 2972.04] we should include the syntax for another language.
[2972.24 → 2973.58] I was just going to ask you that.
[2973.66 → 2974.36] That's pretty awesome.
[2974.50 → 2978.50] Because otherwise, you're maintaining, like, six languages across a single syntax.
[2978.84 → 2980.56] That's how you do it in HTML, right?
[2980.62 → 2983.12] Like, you can embed JavaScript and CSS in HTML.
[2983.32 → 2983.84] Same thing.
[2983.84 → 2989.66] So, in fact, the ViewSyntaxHallitingFile is a modified version of the HTML syntax highlighting file.
[2990.08 → 2993.28] All it does is detecting the special language attributes
[2993.28 → 2996.86] in order to pull a different syntax rules for that block.
[2997.10 → 2997.86] That's interesting.
[2997.94 → 3000.40] As you get to keep the tried-and-true syntax out there,
[3000.42 → 3001.46] you're not creating something new.
[3001.54 → 3002.00] Yeah, exactly.
[3002.02 → 3005.24] And then you're leaving an attribute to sort of toggle back and forth between languages.
[3006.54 → 3006.72] Yeah.
[3007.20 → 3009.40] Jared, your favourite word is up next, hot reloadable.
[3009.82 → 3010.16] What do you think?
[3010.16 → 3010.60] Yeah.
[3013.60 → 3016.42] No comment on that.
[3016.54 → 3018.86] But go ahead and tell us about hot reloadable there, Evan.
[3019.50 → 3019.94] Sure.
[3019.94 → 3020.44] Yeah.
[3020.44 → 3020.94] Yeah.
[3020.94 → 3028.56] So, when you use Webpack to build your View Components, you will notice that if you build up your Webpack
[3028.56 → 3034.70] dev server in hot mode, which enables the hot module replacement API, and then when you edit
[3034.70 → 3040.20] your View Component, say you change the template, or you change the style, the page doesn't reload.
[3040.20 → 3043.56] It just swaps whatever has changed onto the page.
[3045.08 → 3047.70] So, it even keeps the current state of your application.
[3047.70 → 3059.00] So, obviously, this goes back to React hot reloading that's popularized by Dan Abrams.
[3059.54 → 3066.30] So, he's demoed at Reaction Europe, showing all the time travel, hot reloading.
[3066.30 → 3072.12] I think he's the original author of the React hot loader, and then he went on doing all
[3072.12 → 3075.32] those hot reloading-related work, which is super inspiring.
[3075.88 → 3079.64] And that's what kind of triggered me to investigate.
[3079.82 → 3082.10] Is it possible to make View Components hot reloadable?
[3082.10 → 3083.78] So, it turns out they are.
[3084.18 → 3091.18] It's not as perfect as the React hot reload, because when you reload a component, it will
[3091.18 → 3097.90] actually reset the state on its child components, but it doesn't affect the state outside of it.
[3098.36 → 3103.46] But it's still good enough, because a lot of time, it's frustrating for you to have to edit
[3103.46 → 3111.34] a single CSS attribute and have to wait for the app to completely reload, especially if it's
[3111.34 → 3115.24] affecting a component that's only visible after a few interactions.
[3115.48 → 3116.40] It's super frustrating.
[3116.60 → 3120.70] How do you deal with things like the compilers being slow?
[3120.84 → 3121.82] I'm thinking like SAS.
[3122.40 → 3126.18] Recently, a lot of hotness around that is Libras and it being faster to compile.
[3126.36 → 3132.06] So, if you've got a big CSS stack, for example, then you might be delayed on the actual compiling
[3132.06 → 3132.60] of SAS.
[3132.70 → 3133.48] How do you deal with that?
[3134.16 → 3137.26] The good part is Webpack basically handles it for you.
[3137.26 → 3143.94] Webpack uses a lot of advanced optimizations, incremental rebuilding, and it caches each
[3143.94 → 3144.98] module it compiles.
[3145.70 → 3151.76] So, say when you are editing a single view component, only that component will get recompiled.
[3152.24 → 3154.90] Like, all the other components are unaffected.
[3155.44 → 3161.30] And usually when we talk about SAS being slow to compile, it's because we are recompiling all
[3161.30 → 3164.50] the styles for our entire app on every watch.
[3164.50 → 3166.56] That is obviously going to be slow.
[3167.14 → 3172.82] But if you're only compiling a small SAS file, it's always going to be fast enough.
[3173.26 → 3178.20] And if you're writing that much SAS inside a single component, you probably should reconsider.
[3179.46 → 3180.32] Wise words.
[3180.52 → 3181.06] Wise words.
[3182.42 → 3183.38] Shameless plug.
[3184.24 → 3185.64] We're having Dan on in a couple of weeks.
[3185.84 → 3186.24] It's true.
[3186.56 → 3187.40] Dan Abrams.
[3188.64 → 3189.12] Yeah.
[3189.54 → 3190.54] So, stay tuned for that.
[3190.74 → 3191.16] Stay tuned for that.
[3191.78 → 3192.22] Flux.
[3192.22 → 3194.46] I don't know, Jared.
[3194.52 → 3195.84] Should we skip animations and routing?
[3195.92 → 3198.52] We're kind of getting short on time and jump rate to stability.
[3198.96 → 3204.98] Maybe you can give a one-minute version of what you're talking about in routing and animations.
[3205.78 → 3206.44] Evan, what do you think?
[3207.60 → 3211.16] I can probably skip animation and just talk about routing.
[3211.28 → 3211.44] Okay.
[3211.72 → 3213.46] What's the most important thing happening here?
[3214.62 → 3214.84] All right.
[3214.84 → 3217.06] So, Vue Router is optional.
[3217.46 → 3220.30] Like, VS Code doesn't concern itself with routing.
[3220.46 → 3226.98] But if you want routing to build a more single-page application-like thing, then you should use the router.
[3227.26 → 3231.34] And the router essentially does all what you expect a client-side router to do.
[3231.68 → 3235.04] You can either use hash mode or HTML5 history mode.
[3235.04 → 3240.58] It's a little bit opinionative that it maps the routes to components.
[3241.06 → 3245.08] That's basically what React Router and the new Angular Router is doing.
[3246.92 → 3256.06] And because these components, when you switch between components, you can leverage Vue's own transition system to easily apply transition effects.
[3256.06 → 3261.64] You have fine-grade transition control for route switches.
[3262.00 → 3265.08] Like, you can control whether this switch is allowed or should be rejected.
[3266.94 → 3268.68] And, yeah, it's pretty straightforward.
[3269.18 → 3272.78] If you want to build a single-page application, then you should definitely use the Vue Router.
[3274.48 → 3278.74] So, I think we should, before we dive deep into stability, we'll take a quick break.
[3278.82 → 3281.76] We'll also do our closing questions, but we'll come back and talk about stability.
[3281.98 → 3283.54] So, we'll be right back.
[3286.06 → 3294.56] I have yet to meet a single person who doesn't love DigitalOcean.
[3294.78 → 3297.86] If you've tried DigitalOcean, you know how awesome it is.
[3298.14 → 3304.64] And here at the Changelog, everything we have runs on blazing fast SSD cloud servers from DigitalOcean.
[3304.86 → 3316.04] And I want you to use the code Changelog when you sign up today to get a free month run a server with 1GB of RAM and 30GB of SSD drive space totally for free on DigitalOcean.
[3316.06 → 3318.74] DigitalOcean. Use the code Changelog.
[3319.00 → 3323.08] Again, that code is Changelog. Use that when you sign up for a new account.
[3323.46 → 3327.16] Head to DigitalOcean.com to sign up and tell them the Changelog sent you.
[3327.16 → 3336.02] All right. So, we're here with Evan You and we're talking about Vue.js.
[3336.68 → 3342.30] And, you know, this is the tailing of this article that's kind of diving into the reintroduction of Vue.js.
[3342.58 → 3346.46] And stability seems to be the, you know, the ending hook here.
[3346.46 → 3351.58] And the quote you put in here, Evan, was a personal project with a question mark.
[3351.96 → 3353.20] Seriously, question mark.
[3353.60 → 3358.24] So, like, I guess maybe people don't think it's stable.
[3358.56 → 3359.78] What's the situation here?
[3360.58 → 3367.64] Well, I've seen some discussions where, for example, in a comment thread where people say,
[3367.64 → 3369.92] Hey, I think Vue.js is nice.
[3370.36 → 3373.02] And then there will be that guy.
[3373.58 → 3374.68] He jumps out and says,
[3375.06 → 3378.00] Oh, it's just a personal project.
[3378.08 → 3379.30] You know, dying a year.
[3379.74 → 3380.52] That guy.
[3381.66 → 3382.22] Right?
[3382.22 → 3391.66] And, you know, some people just like knowing a project is backed by a huge enterprise of a full team of people working behind it.
[3392.64 → 3397.62] That gives them a sense of, I don't know, maybe just makes them feel safe.
[3397.76 → 3398.06] I don't know.
[3399.16 → 3399.60] I agree.
[3399.70 → 3405.64] It's important to think about how stable the software that you use to build your product upon.
[3405.64 → 3415.98] But sometimes, you know, whether it's a personal project or not may not be the deciding factor because we know there are a lot of great personal projects that stand out.
[3416.32 → 3421.44] Like Backbone or CoffeeScript are both personal projects by Jeremy Askesis.
[3421.66 → 3424.08] And he has, like, more than one of this type of projects.
[3424.60 → 3424.72] Right?
[3424.78 → 3425.32] It's amazing.
[3426.96 → 3429.04] And so many people use it.
[3430.86 → 3435.54] I don't get the situation with that because I think, Jared, help me out here if you agree.
[3435.84 → 3445.36] But I think it's over the last few years that's become a thing where people feel more comfortable with frameworks that are backed by, as you said, some sort of enterprise.
[3446.44 → 3450.30] But, you know, open source began as all personal hobbies to a degree.
[3451.20 → 3457.60] And a lot of the open source that we use daily, you know, Linux, for example, was a personal project.
[3457.90 → 3459.08] And look how many people use that.
[3459.70 → 3463.06] And I mean, that's the impetus of what open source is.
[3463.12 → 3464.10] I don't get that statement.
[3464.34 → 3464.48] Right.
[3464.48 → 3465.76] It's business risk.
[3465.88 → 3466.20] You know what I mean?
[3466.26 → 3474.78] More and more businesses are coming to open source and seeing the light in regard to licensing costs and maintainability and these things.
[3475.48 → 3478.46] And, you know, they're all about risk assessment.
[3478.74 → 3478.86] Right?
[3478.94 → 3480.52] Like, what's our risk here?
[3480.52 → 3487.18] And they find that open source actually reduces risk because you do have access to the source code, for instance.
[3487.30 → 3489.74] But they're coming from a place where they're used to proprietary software.
[3490.00 → 3490.04] Right.
[3490.04 → 3496.80] They, you know, they have money to spend on things like support and just, you know, wanting a company to be there.
[3498.06 → 3506.56] So I get it from both sides, you know, even as an individual software developer who's just been in the startup scene for long enough.
[3506.56 → 3510.28] Like, I don't love fly-by-night things.
[3511.28 → 3514.32] You know, you think of services you're going to start relying upon.
[3514.42 → 3517.88] Like, what if Slack just disappeared now that we're all, you know, loving it?
[3518.28 → 3519.36] That kind of would suck.
[3519.36 → 3523.20] You know, there'd be a disruption to us.
[3523.52 → 3527.08] And so it's risk amercement.
[3527.26 → 3527.92] I don't know the word.
[3529.54 → 3529.94] Advertisement.
[3530.68 → 3530.94] Yeah.
[3531.06 → 3541.14] It's just being averse to risk and thinking that a single developer project is riskier than something that's backed by a corporation, which it is.
[3541.14 → 3547.88] But I think, as you said in your post here, Evan, you're proving by your track record.
[3549.88 → 3562.58] And the fact is that you've been maintaining this for multiple years, and you've reached a stable 1.0, and you have 100% test coverage, and you go through reasons why you are somebody that's providing stability in their project.
[3562.98 → 3563.06] Yeah.
[3563.52 → 3564.64] And I think that's admirable.
[3564.76 → 3566.96] I think that would win over a lot of people that have that problem.
[3567.08 → 3567.20] Yeah.
[3567.24 → 3569.42] Is that why you've put this here at the close of your article?
[3569.82 → 3570.26] Yeah.
[3570.26 → 3570.70] Yeah.
[3571.40 → 3575.26] Mostly this is sort of out of my...
[3576.08 → 3580.10] Because I've been seeing people talk about Vue quite a lot of times.
[3580.26 → 3582.56] And this question comes up actually quite often.
[3582.70 → 3586.44] Like when people ask, is this still going to be around in a year or so?
[3586.70 → 3596.56] Maybe it's because of the bat name the JavaScript ecosystem has gotten because of so many new frameworks coming out and then just disappear in a few years.
[3596.56 → 3605.98] And if you take a look at 2DMVC, like the survival rate is not that great, I would say.
[3605.98 → 3610.72] Maybe some frameworks are just no longer maintained or things like that.
[3610.80 → 3624.62] So people in general, I kind of understand why when they are accessing a new JavaScript framework, and especially if it's a personal one, they would think, oh, like it has a high chance that this is just not going to be around in a year or so.
[3624.62 → 3625.06] Right.
[3625.06 → 3631.96] But again, I think it's a common first impression.
[3632.46 → 3632.58] Sure.
[3632.58 → 3640.50] But when you really want to seriously evaluate a project, it's better to look at the real numbers, right?
[3640.86 → 3642.00] Because everything is public.
[3642.50 → 3649.48] The issues, the commits, everything that this project's gone through is on GitHub.
[3649.48 → 3650.88] You can just go there.
[3650.96 → 3658.24] You can see how many issues are there, how many bugs are open, how fast are they closed or fixed.
[3658.64 → 3660.08] There are statistics for that.
[3660.78 → 3667.18] And you can look at the commit log to see how often this, how active this project is.
[3667.36 → 3676.52] You can look at the tests, see if it's robust, see the source code, and see if the author cares about the quality of their projects.
[3676.52 → 3683.20] These are real useful information for you to decide whether this project is reliable.
[3683.94 → 3695.86] And rather than resort to this is backed by an enterprise, people sort of bet on that, bet on Angular 1 because of that.
[3696.08 → 3697.38] But you see what happened.
[3697.62 → 3697.70] Right.
[3697.94 → 3698.84] That's a good point there.
[3699.86 → 3701.26] You made me think of something, Evan.
[3701.26 → 3710.50] Is there any sort of tool that you know of that you can point at a repo and say, you know, a bug issue is opened and closed this quickly with a resolution?
[3711.50 → 3711.72] Yes.
[3711.76 → 3716.22] There is a site called issuestats.com, I believe.
[3718.00 → 3720.24] It's a site where you're just typing the repo name.
[3720.24 → 3727.06] It'll analyze how fast issues and pull requests are merged or closed for that specific repo.
[3727.28 → 3730.56] And I even have a badge on the VJS README.
[3732.48 → 3735.34] So if you go to, yeah, it's called issuestats.com.
[3736.08 → 3736.68] This is interesting.
[3737.34 → 3737.94] There it is.
[3739.06 → 3739.84] Did you know about this, Jared?
[3740.04 → 3740.74] Is this new to you?
[3741.42 → 3743.22] This is news to me.
[3744.12 → 3744.96] Very cool.
[3745.00 → 3745.96] Brand new right here.
[3746.08 → 3746.36] Wow.
[3746.70 → 3747.16] Thanks, Evan.
[3747.32 → 3747.80] No problem.
[3747.80 → 3753.34] Yeah, I actually learned about this a while ago, I think because Babel.
[3753.52 → 3754.58] Babel also used this.
[3754.92 → 3759.74] And Sebastian, Babel's author, is very meticulous in closing issues.
[3760.36 → 3762.56] And I admire him for that.
[3763.42 → 3763.70] Wow.
[3764.36 → 3769.28] So, I mean, you mentioned Angular, obviously, Google, and look where that turned out.
[3769.34 → 3773.96] Not that it's in a terrible way, but, you know, it's had some hurdles, long story short.
[3773.96 → 3774.40] Right.
[3774.40 → 3787.84] Um, with Vue, obviously, you can point issues or issue stats at this and get some good results back at test coverage, issues closure time, issue closing time.
[3787.84 → 3792.44] And then also the fact there's no open issues that have reproducible bugs.
[3793.00 → 3796.62] And that's something to sort of tout, I guess, if you're, if you're into that.
[3796.62 → 3797.06] Mm-hmm.
[3797.58 → 3806.50] I think it's also worth mentioning, and I think probably, you know, I think we all know this, and I think many of our listeners know this, but when it comes to like, you know, is this a personal project?
[3806.64 → 3809.08] Will this be around, you know, years from now?
[3809.28 → 3814.48] Is that you're adopting somebody else's software when you're using open source, right?
[3814.48 → 3824.20] And that doesn't completely free you of the responsibility of like ever writing any code or maintaining things yourselves or, you know, that's the beauty.
[3824.42 → 3826.22] I'm not sure what you're licensing is.
[3826.64 → 3828.44] Probably pretty liberally open source.
[3828.58 → 3829.34] Evan, what's your license?
[3829.88 → 3830.50] It's MIT.
[3830.94 → 3831.40] It's MIT.
[3831.64 → 3833.46] So as liberal as you can get, right?
[3834.14 → 3836.52] Um, do whatever you want with it.
[3837.14 → 3838.14] You know, here's the copyright.
[3838.46 → 3840.06] And I can't remember what else.
[3840.16 → 3841.26] It's about all MIT says.
[3841.66 → 3843.14] You can't sue us for anything.
[3843.14 → 3847.96] You have all the source code of a stable thing, right?
[3848.36 → 3856.72] And you're a software developer, or you're a company that writes software or, you know, just you can also help out.
[3856.86 → 3856.96] Yeah.
[3857.08 → 3862.70] So, you know, if that's a great point, if Evan totally is like, I'm done with view, I'm sick of it.
[3862.74 → 3867.84] I'm going to start this other new thing as software developers do tend to, you know, want to chase the new shiny.
[3867.84 → 3873.18] Like somebody else can just step in and take it over and run it from there.
[3873.24 → 3876.44] Or if he's doing it in a way you don't like to, you know, that's what the fork button's for.
[3876.58 → 3883.96] So I think it is risk-averse, but it's also perhaps a little bit of laziness or something.
[3885.30 → 3886.70] Just going to put it out there.
[3886.70 → 3894.98] Somebody, I wish I had researched this before I opened my mouth, but hopefully I can type fast or click fast.
[3895.04 → 3895.48] One of the two.
[3895.56 → 3900.80] Somebody just tweeted recently either to us or something like that.
[3900.86 → 3909.92] They recently listened to this show, and they were like, after listening to this, I can't believe that something about how we build stuff, build businesses on top of open source.
[3909.92 → 3913.14] I'm going to find the tweet and put it in the show notes and that's a good paraphrase.
[3913.58 → 3914.36] Actually, right here it is.
[3914.40 → 3920.76] It's Nicholas Young listening to the changelogs, the latest episode on Metabase and realizing I couldn't build businesses without open source.
[3920.86 → 3931.54] And I think, Jared, to your point of laziness is that, or laziness is that, you know, businesses are actually out there, obviously, to create revenue and do good things for the world.
[3931.54 → 3936.54] But at the same time, you have a responsibility to give back and not just freeload.
[3936.74 → 3937.78] You know, and he's right.
[3937.78 → 3943.12] Like, today, you probably couldn't build a single business without leveraging some piece of open source.
[3943.86 → 3949.32] And that doesn't mean just, you know, stand on Evan's shoulders and, you know, enjoy it.
[3949.38 → 3951.32] You know, sometimes you got to get down and carry them a little bit.
[3952.28 → 3952.68] Right.
[3954.50 → 3955.24] Good points.
[3955.38 → 3955.60] Good points.
[3955.68 → 3956.22] Good points.
[3956.22 → 3959.88] That being said, you do have stability.
[3960.82 → 3961.84] You've proven that.
[3962.20 → 3967.48] And just for the record, are you going to give up on view here after the call's over?
[3967.48 → 3968.98] Or are you going to keep working on it?
[3970.20 → 3971.24] I guess the latter.
[3972.68 → 3973.38] All right.
[3973.46 → 3974.16] That sounds good.
[3975.04 → 3976.22] So we touch quickly.
[3976.44 → 3978.74] I know we're, we're like getting close on our time here.
[3978.74 → 3983.78] We got like nine minutes left, but it would be remiss if we didn't at least touch on the
[3983.78 → 3987.50] interesting things happening with view in the Laravel community.
[3988.40 → 3988.66] Uh-huh.
[3988.66 → 3989.66] Yeah.
[3989.74 → 3994.48] So just a couple of points that you made that, you know, we'd like to highlight is that, um,
[3994.76 → 3997.80] Laravel has been picking up view at a very fast pace.
[3998.00 → 4000.68] Uh, it's got, you know, I think over 9,000 stars on GitHub.
[4000.84 → 4002.56] So you're definitely getting some traction there.
[4002.66 → 4008.12] And you were recently on Hacker News and you got actually nice things said about view on Hacker News.
[4008.12 → 4009.60] Um, so what's your secret?
[4010.48 → 4015.62] Um, but for instance, wow, the docs look great for being 99% a one-man job.
[4015.72 → 4016.44] This is incredible.
[4016.60 → 4017.46] I'm very impressed.
[4017.70 → 4019.70] If I was an employer, I would hire you.
[4019.98 → 4020.50] There you go.
[4020.60 → 4022.94] So got some good things going for you.
[4024.06 → 4025.88] Uh, so what's the question?
[4026.02 → 4027.12] Like, what's the secret?
[4027.36 → 4027.48] Yeah.
[4027.48 → 4030.12] What's the secret to getting good comments on Hacker News?
[4030.24 → 4032.40] It's a on the side, no less.
[4032.40 → 4036.50] That's probably a much harder question than I expected.
[4038.04 → 4039.68] Um, I don't know.
[4039.82 → 4045.62] Uh, I guess it's, it's, uh, it's very specifically tied to view because, um, it's been my baby.
[4045.62 → 4058.32] So I, you know, I care about it and I kind of want to, you know, just make it, make it as, uh, as good as, as, as presentable as possible.
[4058.32 → 4068.70] Like the, the point being, um, I have a project that people use and people like, so, um, that's really great, right?
[4068.72 → 4074.70] Like I, I get a lot of thanks from people say, Hey, like, thank you for making this great project.
[4074.70 → 4077.88] So, uh, that's, that really makes me happy.
[4077.88 → 4090.46] And that kind of keeps, keeps me motivated and, you know, keep working on view, uh, making it better, uh, writing better docs, so people can, you know, have an easier time working with it.
[4090.46 → 4103.06] I think all of this sort of, um, sort of ends up showing like it's, it's a project built with, um, with care for its users, I guess.
[4103.06 → 4116.78] So, um, if you, I guess a lot of times some people build really cool projects, but, um, but they sort of just, you know, treat it as a, um, as a one-time thing.
[4116.78 → 4118.68] They think, okay, this is a cool project.
[4118.76 → 4119.34] I'll share it.
[4119.38 → 4133.00] But they, they don't really plan on, you know, uh, doing long-term investment into it or like they, they're, um, or they just simply don't think they,
[4133.00 → 4143.38] they want to, you know, go that far to, to make it something that, um, that would attract more people, or maybe they just don't care, but I do care.
[4143.54 → 4154.84] So I am willing to, you know, write the docs, make the docs look beautiful or, uh, provide examples, help people out just to make sure people can pick it up and get productive.
[4154.84 → 4163.14] I think enabling a lot of, uh, people who've hated front end work before to, to find it enjoyable.
[4163.40 → 4165.34] I think that's, that's just great.
[4165.88 → 4168.38] Let's take a very specific example of your documentation.
[4168.86 → 4172.44] You know, we all love to code, but we don't all love to write docs.
[4172.72 → 4173.48] It's boring.
[4173.62 → 4174.26] It's hard work.
[4174.30 → 4176.30] It's, it's difficult to do well.
[4176.88 → 4179.06] Um, it's easy to get wrong.
[4179.14 → 4182.96] It's hard to write as if you're, you don't have the intimate knowledge that you have, you know what I'm saying?
[4182.96 → 4188.44] So, you know, the first thing this person says, anonymous hacker news user is, wow, the documentation looks great.
[4189.04 → 4190.80] Um, so like you said, you put a lot of thought into it.
[4190.82 → 4192.20] You put a lot of care into your documentation.
[4192.20 → 4198.94] Can you give some, like, uh, some hard examples of like things that you did with your documentation that you think it really paid off?
[4198.98 → 4203.26] Like it was worth your effort so that other people could perhaps put that kind of care into their projects.
[4204.38 → 4212.94] So before that, um, before 1.0, the old docs are, um, kind of accumulated over all the projects.
[4212.96 → 4218.46] It's from like back, uh, back in the days of the initial release all the way up to 0.12.
[4219.20 → 4224.04] Um, so before the 1.0 release, I did a complete rewrite of the docs.
[4224.70 → 4239.98] Um, basically rewriting the whole guide, uh, just trying to take a step back and think about what would, assuming someone who's never worked with you before, someone maybe even just, uh, you know, uh, hardly familiar with JavaScript.
[4239.98 → 4241.70] And they're just picking up the framework.
[4242.42 → 4247.48] Um, what would they have to go through to be able to build something with it?
[4247.58 → 4249.32] I think that's the most important thing.
[4249.40 → 4268.28] I think a lot of, uh, technical documentation, uh, not essentially failing, but like they, they don't really recognize the fact that, um, a lot of users start reading the documentation without all the context and information you have as the author of the library.
[4268.28 → 4280.18] So you have to sort of kind of like when you're designing a product, you have to put yourself in the position of, of the user in order to, uh, to write a doc that makes sense for them.
[4280.86 → 4288.08] Um, so I also really value what people like to make when, when people make suggestions, Hey, like this part is confusing.
[4288.08 → 4290.56] Maybe you should add an example here or there.
[4290.56 → 4301.50] Uh, I really like that type of feedback because it helps me to, you know, the next new user who, who read the doc will, would don't have to deal with that confusion.
[4301.72 → 4306.74] Uh, so I always take those suggestions really seriously and just put them into the doc.
[4307.38 → 4311.42] Um, other than that.
[4311.80 → 4313.10] So care basically.
[4313.10 → 4314.10] Yeah.
[4314.10 → 4314.66] Yeah.
[4314.72 → 4316.80] Like put yourself in the yeah.
[4316.86 → 4337.38] Put yourself in the position of, uh, someone who's never used your library before and don't assume that they know this or that, like all these advanced concepts, like try to explain things and make sure, like, I guess it's easier to overlook sometimes when you assume they are, they're already familiar with one thing.
[4337.38 → 4344.72] So you just jump right ahead into something that builds upon that concept, then your doc quickly becomes harder to follow.
[4345.32 → 4345.72] Yeah.
[4346.48 → 4348.98] I think one thing you've done that's really awesome is your examples.
[4349.70 → 4355.36] Um, so just for that initial, like before I even get to the API documentation, I'm usually looking at examples.
[4355.54 → 4358.10] Like what can I do, and how hard is it to accomplish a few things?
[4358.10 → 4367.18] And you have a nice page where there's about 10 or so examples on the left-hand side, and they're, uh, varying difficulties and complexity.
[4367.18 → 4370.88] It starts off with like, you know, a little, uh, tree view here.
[4371.04 → 4375.42] You have a markdown editor, which is surprisingly brief, uh, to implement.
[4375.66 → 4380.58] And then you all the way down to like you should do NBC example, um, and a hacker news clone.
[4380.58 → 4386.66] And then on the right-hand side, you have basically an embedded JS fiddle, which is showing you hereare the HTML you got to use.
[4386.74 → 4387.14] Here's the JavaScript.
[4387.30 → 4387.86] Here's the CSS.
[4388.28 → 4397.30] And it's just a nice way to provide, um, an obvious and outright example of like, what do I get to do to accomplish this thing?
[4397.60 → 4404.54] And that helps me decide like, okay, do I, do I, or do I not want to spend the time to, to dig into the API documentation?
[4404.54 → 4410.72] And I think, uh, that was really impressive to me and I think probably is something that is worth emulating.
[4411.76 → 4412.20] Yeah.
[4412.32 → 4419.04] Uh, I had, um, when I first released VJS, uh, that was in February 2014.
[4419.46 → 4424.86] Um, I had a blog post talking about the first work, the first week of launching it.
[4425.18 → 4434.34] And, uh, from the Google Analytics, uh, I think over half of the traffic landing on the site directly went to the examples after landing on the homepage.
[4434.54 → 4437.90] So, yeah, I think that sort of echoes what you just said.
[4438.70 → 4448.36] How common is it, Jared, that, you know, I mean, I never really paid much, I mean, I guess I pay attention to it, but how often is an examples' navigation item at the top level?
[4448.36 → 4450.64] Is it always there for most projects like this?
[4450.94 → 4452.34] Were you surprised it was there?
[4452.50 → 4460.14] I mean, um, no, not that there was an example section, but I was surprised at when you get there, it's a single page.
[4460.68 → 4463.20] That's very easily, you know, exactly what you're looking at.
[4463.20 → 4464.98] Usually examples are kind of like long.
[4465.28 → 4465.38] Right.
[4465.76 → 4466.12] I don't know.
[4466.22 → 4469.76] Just, it's just put together in a way that's like outright and obvious, which I think stands out.
[4469.84 → 4474.98] And, you know, it's nice when you're working with JavaScript, for instance, where, you know, it's all web technology.
[4475.18 → 4481.70] So, yes, you can just embed everything that you need to right here into the same page and then show how it renders, which is awesome.
[4481.70 → 4484.32] So, you know, he's making good use of JS Fiddle.
[4484.40 → 4489.42] Some projects don't have that, um, advantage, but people have started to get more creative.
[4489.54 → 4494.60] I know animated GIFs are becoming more useful as people showing like, here's how my command line tool works.
[4494.80 → 4495.24] Right.
[4495.24 → 4502.86] Um, and those are great for a little, you know, getting people to see the payoff of why would I invest time into using this thing right away?
[4503.58 → 4504.02] Yeah.
[4504.70 → 4508.70] I think a good example is, uh, it's hard to explain hot reloading without a GIF.
[4509.98 → 4511.12] There you go.
[4511.98 → 4513.26] Some would say that's true.
[4514.08 → 4514.90] Some would say.
[4514.90 → 4518.32] Well, all right, Evan, well, it's, it's time to close out the show.
[4518.40 → 4521.74] I know we've been, uh, certainly enjoying this conversation with you.
[4522.04 → 4528.20] Um, but we, we can't close the show without asking you who your, your programming hero is.
[4529.08 → 4529.46] Okay.
[4529.54 → 4538.16] So, um, yeah, there are, there are many of them like at different stages of like when you program, I think you would have different heroes along the way.
[4538.22 → 4538.44] Right.
[4538.52 → 4540.52] Um, to advance might be an old school one.
[4541.38 → 4542.34] Yeah, definitely.
[4542.34 → 4544.94] To advance was definitely one of them.
[4545.56 → 4554.00] Um, and then when I was at Parsons, uh, Zach Lieberman was someone I looked to, looked, looked up to a lot.
[4554.06 → 4558.92] Um, in case people don't know, Zach is, uh, the author of Open Frameworks.
[4559.20 → 4563.64] Uh, it's a C++, C++ based creative coding framework.
[4564.12 → 4570.86] Uh, tons of crazy artwork produced with purely code, uh, made with that framework.
[4571.36 → 4572.20] Uh, and, uh, it's a great, uh, great.
[4572.34 → 4577.42] So if you're into creative arts with, uh, combined with computer science, something you should check out.
[4577.90 → 4596.50] Um, and then when I first stepped into JavaScript, all of that, um, uh, the people at data arts team, Google data arts team, Aaron Cobbling, uh, is probably, uh, another, uh, big hero of mine.
[4596.50 → 4600.36] Uh, he was, uh, he was, uh, he was the team lead of the data, the data arts team.
[4600.46 → 4602.50] Uh, they did a lot of Chrome experiments.
[4603.16 → 4610.52] When, when Flash was dying, it was, it was them showing people, hey, HTML5 can be capable of fancy stuff too.
[4610.52 → 4615.34] So, um, that was pretty, pretty important.
[4615.34 → 4629.36] Uh, and, uh, and then when I was just getting started with Node.js, uh, uh, TJ Holloway Chuck is, uh, really, uh, like, I was just amazed how could a single person be so productive?
[4629.36 → 4635.00] Like making so many, so many impactful projects in the ecosystem.
[4635.74 → 4637.26] Um, yeah.
[4637.26 → 4640.68] I see you're a fan of stylists too with your hacker news example.
[4641.16 → 4641.28] So.
[4641.78 → 4642.00] Yep.
[4642.22 → 4642.54] Yep.
[4644.06 → 4649.52] Next question is what is on your open source radar?
[4649.72 → 4658.62] So it doesn't necessarily have to be view related, although it could be, but if you had a free weekend, and you were just going to pick up some open source and check it out or hack on it,
[4658.62 → 4659.84] what's on your radar?
[4661.02 → 4677.68] Um, I would probably play with, so something I want to, but haven't had time to play with, um, Elixir, uh, and the Phoenix framework and, uh, the, the closure script stuff.
[4677.68 → 4680.00] Uh, I'm next would be one of them.
[4680.70 → 4688.50] Um, yeah, I think, uh, I think currently my interest would, uh, I would really be interested to just play.
[4688.62 → 4698.46] Outside the JavaScript ecosystem and just, you know, because oftentimes we, we take good ideas from other languages and ecosystems, and we learn from each other.
[4698.54 → 4700.18] So I think that's pretty important.
[4700.96 → 4702.60] You said, um, next, right?
[4703.58 → 4703.78] Yeah.
[4703.90 → 4709.00] Not I'm, um, um, um, we'll get that in the show notes for those of you listening.
[4709.38 → 4712.12] Uh, anything else do you want to mention before we close the show?
[4714.12 → 4714.60] Nada.
[4715.62 → 4716.06] Nope.
[4716.06 → 4716.28] Nada.
[4716.28 → 4716.92] Uh, all right.
[4717.40 → 4717.94] Aaron, how about you?
[4718.02 → 4719.68] Or Evan, not Aaron, Evan.
[4720.24 → 4720.90] My bad.
[4721.38 → 4723.30] Anything on your side you want to close out with?
[4723.36 → 4727.76] Uh, anything else you want to mention view, your interests, open source?
[4728.10 → 4732.34] If you had the ear of the community about open source, what would you share back with them?
[4733.10 → 4735.00] Um, I don't know.
[4735.74 → 4736.64] Any advice?
[4738.16 → 4738.56] Advice?
[4738.56 → 4740.78] Uh, I think, uh, I don't know.
[4740.78 → 4743.00] I'm probably not senior enough to give advice.
[4743.30 → 4743.48] Yeah.
[4743.78 → 4745.54] Don't, uh, take my words.
[4746.08 → 4746.66] Use your codes.
[4747.68 → 4748.16] Yeah.
[4748.26 → 4748.80] Use my code.
[4749.00 → 4749.16] There you go.
[4749.30 → 4749.68] There you go.
[4750.46 → 4750.90] Yeah.
[4750.94 → 4752.66] One more thing we'll link out to in the show notes.
[4752.82 → 4761.78] Um, there is a repo called awesome view following the awesome dash star meme of repos where all
[4761.78 → 4767.36] sorts of things related to view, including a nice list of, uh, people using it, Ajax libraries,
[4767.46 → 4768.08] those kinds of things.
[4768.08 → 4772.04] So if you're interested in view, obviously check out the website, check out the, the
[4772.04 → 4775.88] awesome docs he's put together, but, uh, check out this awesome dash view as well.
[4775.88 → 4778.82] And you'll have all sorts of inspirational related things.
[4778.82 → 4779.36] There you go.
[4780.62 → 4783.34] And with that, that is the, uh, the close of our show.
[4783.44 → 4785.88] We, uh, we try to keep it, uh, we're, I'm kidding.
[4785.94 → 4787.06] We're not keeping it commuter friendly.
[4787.20 → 4789.52] This is not commuter friendly show at all.
[4789.52 → 4791.44] We ditched that idea.
[4791.66 → 4792.84] We ditched that a long time ago.
[4793.12 → 4796.28] You know, we used to do shows that were like 30, 45 minutes long.
[4796.50 → 4797.06] Uh huh.
[4797.24 → 4800.62] And, and people were just like, it's, it needs to be longer.
[4800.88 → 4803.92] You know, like we would get into conversations and end them prematurely.
[4804.26 → 4805.78] And so here you go.
[4805.88 → 4807.26] A 75-minute show at least.
[4807.88 → 4810.44] And, uh, well, yeah, that's, that's long.
[4810.64 → 4813.08] You can call it commuter friendly in LA or something.
[4813.18 → 4813.36] There you go.
[4813.44 → 4814.88] You know, we get that two hour commute.
[4815.14 → 4816.10] So, you know what?
[4816.10 → 4821.76] I used to take a 75-minute commute when I was, uh, working a working at Google.
[4821.88 → 4826.70] Like I live in Jersey and I have to do the catch the bus to go into the city every day.
[4826.70 → 4826.90] Wow.
[4827.18 → 4828.90] That's like 75 minutes one way.
[4828.98 → 4829.08] Yeah.
[4829.08 → 4829.44] There you go.
[4829.44 → 4831.04] You must be a fan of the change law then.
[4832.06 → 4832.84] I am.
[4833.64 → 4835.14] Remember I was the first one to pay.
[4835.14 → 4835.38] You were.
[4835.56 → 4836.88] And thank you so much for doing that.
[4836.90 → 4837.64] That was so awesome.
[4837.74 → 4840.10] Like we threw it out there, and we're like, you know what?
[4840.10 → 4841.56] This is our open inbox.
[4841.70 → 4848.48] And so for those listening, you can go to GitHub.com slash the change log slash ping and go to the issues.
[4848.48 → 4849.36] You'll see a bunch there.
[4849.40 → 4853.32] And if you go to issue number one, you'll find Evan's original mention of view.
[4853.48 → 4856.06] And that actually hit, uh, change law weekly.
[4856.06 → 4861.58] And the issue number for that was issue number 24, which shipped on February 15th, 2014.
[4861.58 → 4867.30] So that was a cool issue and, and like view made it into there.
[4867.40 → 4872.40] So if you listen or, you know, if you, if you read channel weekly, then you, you, you got that back in the day.
[4872.48 → 4875.26] And we even linked to those examples we talked about earlier in the show.
[4875.40 → 4880.38] So, uh, but with that fellas, uh, we do have a couple of sponsors to mention.
[4880.38 → 4885.56] We got code ship, op beat brain tree, and also digital ocean.
[4886.06 → 4888.10] Uh, but that is it for the show.
[4888.10 → 4899.40] Thanks also to the listeners for listening to the show and Evan, you for sharing so much and being one person, making an awesome project, really shine and being a good example of how to do it.
[4899.54 → 4900.98] So thanks for coming on the show.
[4901.08 → 4902.60] And, uh, let's say goodbye, fellas.
[4903.00 → 4903.28] Goodbye.
[4903.40 → 4903.94] Thanks for coming.
[4904.60 → 4905.62] Thanks for having me.
[4918.10 → 4919.10] Bye.
