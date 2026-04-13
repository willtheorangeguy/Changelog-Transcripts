[0.00 → 6.18] The way that I approach that is exclusively with all the Tom Holland snap filters.
[6.78 → 16.38] And so when I share my screen, I just have these random I love Tom Holland and I don't know why, but there's a lot of them.
[16.56 → 18.02] So it gets you a lot of variety.
[18.16 → 18.78] But there you go.
[18.88 → 22.06] There are some pro tips to excite your next Zoom call.
[23.30 → 26.38] I will say this is the creepiest picture I've ever seen.
[26.38 → 30.00] And we'll have to include that in the show notes for people to enjoy the creepiness.
[30.12 → 30.94] You don't have to be more specific.
[31.22 → 31.62] Which one?
[33.00 → 33.40] Nope.
[33.72 → 34.16] Both of them.
[34.28 → 34.68] Wow.
[36.52 → 39.30] Bandwidth for Changelog is provided by Vastly.
[39.66 → 41.56] Learn more at Fastly.com.
[41.80 → 44.86] We move fast and fix things here at Changelog because of Rollbar.
[45.00 → 46.68] Check them out at Rollbar.com.
[46.68 → 49.12] And we're hosted on Linde cloud servers.
[49.46 → 51.46] Head to Linode.com slash Changelog.
[52.64 → 55.48] This episode is brought to you by Rollbar.
[55.48 → 57.52] Move fast and fix things.
[57.84 → 59.94] Resolve errors and minutes and deploy with confidence.
[60.50 → 62.78] Head to Rollbar.com slash Changelog.
[62.86 → 63.66] Request a demo.
[63.82 → 64.68] Get started today.
[65.10 → 67.32] It's loved by developers, trusted by enterprises.
[67.88 → 70.34] And most of all, we use it here at Changelog.
[70.72 → 73.38] Move fast and fix things with Rollbar.
[73.38 → 76.66] Once again, Rollbar.com slash Changelog.
[85.48 → 92.20] Welcome to JS Party, your weekly celebration of JavaScript and the web.
[92.62 → 95.92] Next week's episode is all about Node best practices.
[96.28 → 99.16] It's a deep dive that's filled with wisdom, so stay tuned for that.
[99.60 → 104.00] If this is your first listen, subscribe to the pod at ChangeLog.com slash JS Party
[104.00 → 105.62] or wherever you get your podcasts.
[106.16 → 108.16] Right now, let's welcome Abel to the show.
[108.16 → 110.32] Hey, it's party time, you all.
[124.52 → 125.82] Ah, yes.
[125.90 → 131.16] The sound of those BMC beats means it's time once again for JS Party.
[131.68 → 132.42] What's up, you all?
[132.76 → 133.24] Ow, ow.
[133.68 → 134.10] Hello.
[134.10 → 135.36] I'm Jared.
[135.50 → 138.14] I'm your friend, and I'm joined by three of my friends.
[138.38 → 139.40] Nick Needed is here.
[139.48 → 139.90] What's up, Nick?
[140.24 → 141.10] Ahoy, ahoy, ahoy, ahoy.
[141.22 → 143.26] And of course, you may know her as Short DIV.
[143.32 → 144.22] I know her as Divya.
[144.46 → 145.00] Divya's here.
[145.06 → 145.36] Hi, Divya.
[145.70 → 146.28] Hello, hello.
[147.00 → 151.30] And we have a brand-new face, a brand-new voice on the show, Abel Hussain.
[151.36 → 154.74] We're welcoming her for the first time as a JS Party panellist.
[154.82 → 155.68] Welcome, Abel.
[156.20 → 156.58] Hello.
[156.80 → 157.62] Happy to be here.
[157.76 → 158.12] Yay.
[158.66 → 159.02] Finally.
[160.52 → 161.92] Happy to have you.
[161.92 → 166.64] So the three of us know you well, but our listeners may not know you quite as well.
[166.80 → 170.14] Why don't you go ahead and introduce yourself by way of origin story?
[170.26 → 174.38] Every great superhero has an origin story, and surely you do as well.
[174.52 → 175.98] So tell us how you got here.
[176.28 → 178.82] Thank you so much for the warm welcome, Jared and company.
[179.32 → 180.92] My name is Abel Hussain.
[181.06 → 183.68] I'm a principal software engineer based in the Boston area.
[184.26 → 187.10] And my origin story is kind of a fascinating one.
[187.26 → 188.28] I was born in New York City.
[188.68 → 191.28] I ended up moving to Dubai when I was like two months old.
[191.28 → 192.58] My dad got a job there.
[192.68 → 196.18] So I grew up abroad as like an American, but who was an expat.
[196.34 → 201.36] And then I came back to the States when I was like 17, 18 and went to college, studied
[201.36 → 202.20] biomedical engineering.
[202.74 → 207.30] So I, yes, I transitioned into software from biomedical engineering after being exposed
[207.30 → 209.16] to kind of the rapid cycles.
[210.16 → 213.24] With software, like you're kind of your only bottleneck.
[213.24 → 218.86] And, you know, the kind of the long product arcs that existed in the biomedical engineering
[218.86 → 220.76] world are just like not really there.
[221.14 → 227.38] And I think also the knowledge sharing components with open source and how, you know, folks are
[227.38 → 229.92] sharing like million-dollar ideas freely and openly.
[230.30 → 235.58] It was very, very kind of different from like patent world, you know, of biomedical engineering
[235.58 → 238.78] where, you know, like everything is heavily guarded and regulated.
[238.78 → 245.98] And so for me, I was interested in solving problems at scale and really software felt
[245.98 → 247.34] like the right way to do that.
[247.60 → 250.34] And so that decision kind of happened about almost a decade ago.
[250.74 → 255.56] And since then, I've really just kind of been punching my way up the technical ladder,
[255.56 → 259.56] I would say, you know, from software engineer to senior software engineer, to tech lead, to
[259.56 → 263.50] project lead, to like engineering manager most recently at NPM.
[263.50 → 269.86] And I kind of have recently just made a big pendulum swing for management back into kind
[269.86 → 271.96] of an icy role that's technical leadership.
[272.32 → 278.26] But, you know, less, I would say, BS around all the pain points with middle management.
[278.94 → 280.92] So that's kind of a little bit of my origin story.
[281.22 → 287.04] I also am a community organizer, podcaster myself, been podcasting kind of part-time on
[287.04 → 289.14] the web platform podcast for a little while.
[289.14 → 294.52] And, you know, I speak at conferences and actually that's kind of how Jared and I connected.
[294.68 → 300.00] I think the first time we met in real life was last November at All Things Open.
[300.28 → 303.62] And for anyone who could see Jared, he's wearing the conference t-shirt.
[303.80 → 304.26] This was an accident.
[304.56 → 308.48] I wasn't sure if you wore that t-shirt intentionally or if you, you know, or not.
[308.82 → 309.68] It was a happy accident.
[310.12 → 310.32] Yeah.
[310.36 → 313.46] He's wearing the t-shirt, you know, from the conference where we met for the first time.
[313.70 → 316.26] I think I had actually been on the show at that point already.
[316.26 → 319.32] I had been on Changelog and I had been on JS Party as a guest before.
[320.46 → 324.76] And so Jared asked me to come on as a guest, but I was like really bogged down with NPM
[324.76 → 327.20] life and like new manager life.
[327.30 → 332.98] And I just like had no bandwidth to really like to schedule any recurring like meetings on
[332.98 → 338.46] my calendar between like 6 a.m. and 6 and like 10 p.m. to be quite frank.
[339.00 → 339.40] Yeah.
[339.44 → 342.28] And I'm just really happy to have the time to do this now and talk shop.
[342.48 → 342.62] So.
[343.10 → 343.50] Absolutely.
[343.68 → 344.38] Well, here we are.
[344.38 → 347.76] So we'll link up those old episodes in the show notes.
[348.12 → 350.40] As you said, you were on the Changelog talking Acts.
[350.74 → 352.16] You were on the Lightning Chats.
[352.24 → 354.92] If you all remember our may have been episode 100.
[355.04 → 356.98] We had like 11 Lightning Chats from all things open.
[357.10 → 358.96] So I'm always on that episode as well.
[359.18 → 361.94] We'll link those up if you're interested to go back and hear more.
[362.72 → 364.22] But we're all happy to have you here now.
[364.76 → 364.90] Yeah.
[364.94 → 367.98] And I was actually even on another episode of JS Party.
[368.12 → 370.12] I can't believe you don't remember this.
[370.34 → 371.46] Jared, shame on you.
[371.58 → 372.80] Well, I may not have been on it.
[372.80 → 374.18] So as a rotating panel.
[374.34 → 375.54] You were not, but Nick was on it.
[375.60 → 376.66] It was Nick and K-Ball.
[376.94 → 377.74] Oh, do you remember it, Nick?
[377.94 → 379.00] Yeah, I do.
[379.14 → 380.68] We did a live interview at a conference.
[381.48 → 382.18] So, you know.
[382.32 → 382.58] Awesome.
[382.66 → 383.32] That too.
[383.58 → 385.72] So now you're here for good.
[385.80 → 386.90] You're a regular panellist.
[387.10 → 391.70] And we're going to get to know you even better by asking you random questions.
[392.04 → 392.40] Okay.
[392.40 → 396.78] In rapid fire style that may or may not have to do with JS.
[397.62 → 399.76] And we'll start with this one.
[400.30 → 401.80] Abel, describe your perfect breakfast.
[402.32 → 407.90] Oh, my perfect breakfast lately has been, I discovered these buttermilk herb biscuits.
[408.26 → 410.02] So you get the like sweet and sour.
[410.46 → 416.70] So buttermilk herb biscuits with egg cheese, egg tomato, a slice of tomato and American cheese.
[416.86 → 418.92] That's like the perfect breakfast for me.
[419.42 → 419.56] So.
[420.30 → 421.08] That sounds perfect.
[421.08 → 421.86] So specific.
[422.46 → 422.92] Yeah, yeah.
[422.98 → 423.66] Super specific.
[423.86 → 425.82] Well, I'm like a foodie and so is my fiancé.
[426.06 → 430.12] So we've kind of gone into foodie overdrive since quarantine.
[430.66 → 434.94] It's like, you know, when engineers get into stuff, you know, they get really intense about their stuff.
[435.12 → 438.04] And so I feel like I'm very intense about food right now.
[439.64 → 440.68] I didn't have breakfast.
[440.82 → 442.68] So I'm very intense about food right now as well.
[442.78 → 444.82] I will survive.
[445.18 → 446.02] And we'll ask another question.
[446.10 → 448.22] Divi, do you have a question for Abel you'd like to ask her?
[448.52 → 448.86] Yeah.
[448.86 → 451.14] I feel like I know Abel like a lot.
[451.28 → 454.66] So it's really hard to ask like questions because I'm like, I know a lot of the answers.
[454.84 → 460.36] But I guess for the listeners who don't know her as well, here's a curveball of a question.
[460.98 → 462.78] Do you like to live dangerously?
[462.78 → 465.08] Oh, 100%.
[465.08 → 467.40] I mean, my parents are East African.
[467.76 → 468.46] Enough said.
[468.66 → 474.58] You know, I'm pretty sure like Somalis brought pirating, you know, into the mainstream conversation.
[474.58 → 476.28] You know, more recently.
[476.54 → 479.26] So I'm like descendants of some serious badass.
[479.52 → 480.28] So yes.
[480.56 → 480.96] Nice.
[481.18 → 482.28] Love to live dangerously.
[482.28 → 492.98] What's like the craziest, most spontaneous thing you've done that like sort of represents that personality or that side of you?
[493.10 → 506.16] The thing I'm willing to share in a semi-professional setting would probably just be the most dangerous thing I think I've done is like make friends with people on vacation and then like spend an excessive amount of time with them.
[506.32 → 507.30] That can be dangerous.
[507.30 → 508.46] Yeah, that can be dangerous.
[508.78 → 510.60] That feels kind of, yeah, right.
[510.72 → 513.34] And so like, I just met you, but like, let's go do stuff.
[513.48 → 517.56] And so, you know, I think, I think, yeah, I've done that like several times.
[517.92 → 518.40] So, yeah.
[518.54 → 519.18] That's super great.
[519.28 → 522.10] I've watched so many horror movies that I never do that.
[522.68 → 524.80] Just like you never trust anyone.
[525.42 → 525.52] Yeah.
[525.92 → 529.96] Nick would like to ask you what your favourite flavour of JavaScript is, and why is it TypeScript?
[530.76 → 531.52] I'm just kidding.
[531.80 → 533.40] That is something that wouldn't have crossed my mind.
[534.28 → 536.10] But it said non-JS questions.
[536.44 → 536.86] That's right.
[536.86 → 537.46] Go ahead, Nick.
[537.56 → 538.12] Throw one at her.
[538.14 → 540.56] Well, I mean, technically, if you want to get pedantic.
[542.26 → 543.62] Oh, we do want to get pedantic.
[543.86 → 544.36] Trust us.
[544.90 → 546.46] TypeScript isn't JavaScript, right?
[546.60 → 548.86] So it's a non-JavaScript question.
[549.18 → 550.98] You know what else isn't JavaScript?
[551.24 → 557.34] If you all want me to blow your minds a little bit, anything that is stage one through three, right?
[557.34 → 566.04] Like any feature that a lot of developers are using that hasn't passed stage three is technically also not JavaScript, right?
[566.14 → 566.74] It's true.
[567.14 → 567.82] Or JSX.
[568.02 → 568.58] It's like an idea.
[568.58 → 571.62] Oh, JSX is, yeah, it's definitely, it's...
[571.62 → 572.68] RCS isn't JS.
[573.08 → 573.30] Yeah.
[573.86 → 575.66] It's one of the more controversial things.
[575.98 → 580.68] But I have to say, JSX is like, you know, I appreciate the effort, right?
[580.68 → 586.60] What I really like about React is the fact that there's no magic, right?
[586.64 → 591.72] There's no magical incantation that you have to learn to kind of get started with it.
[591.86 → 593.94] It's just JavaScript for the most part, right?
[594.02 → 595.96] Minus some weird little rules here and there.
[596.32 → 601.14] But I mean, if you can kind of compare that with something like Angular 1x, for example, you know, pipes and filters.
[601.28 → 606.26] I mean, like I had to, yeah, I mean, how many times did I have to Google how do I pipe, how do I filter, how do I loop?
[606.26 → 614.82] Because there's just magical incantations that you're learning that are not HTML, not JavaScript, and like specific to Angular, right?
[614.90 → 621.48] So I think for me, you know, the success of a framework is also heavily dependent on, I think, the learning curve.
[621.54 → 625.60] And I think that's why you've seen that like mass adoption with tools like React.
[626.22 → 628.24] So sorry, I didn't mean to like pivot.
[628.48 → 630.14] It's not supposed to be about JavaScript.
[630.82 → 631.26] Yeah.
[631.50 → 631.98] Fair enough.
[632.36 → 633.72] No, but that is a great point.
[633.72 → 640.76] And that is one of the reasons I really like that over something like Angular, which is very, very dense to learn.
[641.28 → 645.38] But non-JavaScript aside, I hear you speak more than one language.
[645.64 → 646.74] How many languages do you speak?
[647.14 → 647.54] I do.
[647.68 → 652.72] So I told you my parents are Somali immigrants that came here like, you know, 40 something years ago.
[653.00 → 656.20] And I speak Somali because of that.
[656.44 → 662.74] And I can thank my dad for that because my dad like refused to speak to me in any other language when I was a small child.
[662.74 → 670.66] And so I really appreciate that because my brother and my sister don't speak Somali because he was like kind of done like heavy parenting.
[670.94 → 672.90] I think by the time they rolled around, I'm the oldest.
[673.14 → 675.18] So, you know, I got all the like energy from them.
[675.88 → 676.00] Yeah.
[676.04 → 678.76] So I speak Somali, Arabic, French, and English.
[679.10 → 681.46] So Arabic and French I learned to grow up in Dubai.
[682.02 → 682.30] Wow.
[682.48 → 682.84] That's cool.
[682.96 → 684.00] I feel so unaccomplished.
[684.52 → 685.80] No, no, not at all.
[686.14 → 686.48] It's okay.
[686.58 → 687.38] You're an American.
[687.56 → 688.86] You don't need to learn anything.
[689.20 → 689.76] You're in English.
[690.34 → 691.16] Thank you.
[691.16 → 692.34] That kind of compliment.
[692.90 → 693.52] Thank you.
[693.60 → 694.28] It's okay.
[695.18 → 698.30] But no, my partner is also like his parents are Korean.
[698.50 → 700.92] And so, and we're both learning Japanese together now.
[700.92 → 703.72] And like, we're both on that CJK track.
[703.72 → 705.58] So he already speaks Chinese and Korean.
[705.82 → 707.22] And so we're learning Japanese together.
[707.74 → 710.52] Eventually, I'd like to learn, you know, Mandarin and Korean as well.
[710.72 → 713.46] But I think Japanese is like my like entry point into that.
[714.00 → 715.72] And today I learned about the CJK track.
[715.72 → 716.10] Same.
[716.32 → 716.76] Oh, yeah.
[716.98 → 718.32] Oh, you guys don't know about CJK?
[718.42 → 718.74] No.
[719.34 → 719.94] CJK is a thing.
[720.02 → 720.14] Yeah.
[720.14 → 720.96] We should link that.
[721.06 → 724.34] Maybe there's a Wikipedia article we could add to the notes, Jared.
[724.48 → 726.52] But yeah, it's Chinese, Korean, Japanese.
[726.68 → 731.74] So if you speak those three languages, and you live in East Asia, you basically can do business
[731.74 → 732.48] for reals.
[732.66 → 733.00] Oh, wow.
[733.32 → 738.34] You know, and so it's kind of like a requirement, like to kind of get above certain like levels.
[738.34 → 745.08] Do you think that your practice and experience in learning multiple spoken languages has aided
[745.08 → 749.82] you in perhaps learning multiple programming languages or do you feel very in the JavaScript
[749.82 → 750.44] world?
[750.54 → 752.20] Or do you are you polyglot in that sense, too?
[752.70 → 754.08] Yeah, that's a really great question.
[754.08 → 755.98] I am definitely polyglot.
[755.98 → 761.98] And I identify like the longer I go in my career, the more I identify as a generalist,
[761.98 → 762.22] right?
[762.32 → 767.56] So the more and more I'm like, I don't really think about things in terms of frameworks and
[767.56 → 768.22] tools and languages.
[768.48 → 773.36] It's more like I look at the problem, and then I pick, okay, based on the problem and based
[773.36 → 776.22] on the constraints that I have, this is how I would approach it, right?
[776.22 → 778.98] And of course, a lot of that is pulling from my experience.
[779.12 → 783.06] But sometimes like I know that like something that I don't have expertise in would actually
[783.06 → 784.84] be like a better solution.
[784.84 → 787.42] And like that's an opportunity to come up to speed with that.
[787.64 → 792.06] And I would say the benefit of kind of having this open-minded approach to problem-solving
[792.06 → 799.96] is that basically what happens is you accelerate your learning a lot as you kind of progress
[799.96 → 800.80] through your career, right?
[800.84 → 805.24] So like I'm like, like I've gotten a lot better at learning new things because I'm like a lot
[805.24 → 809.26] more open to learning them in addition to like the fact that I constantly learn new
[809.26 → 809.80] things, right?
[809.90 → 813.42] So like my sphere of learning is like not small.
[813.80 → 820.58] And therefore, I feel like when I learn a new thing, I have more data points to kind of
[820.58 → 823.46] compare and contrast, right?
[823.54 → 827.36] Like, so for example, let's say JavaScript is your first language, and now you're learning
[827.36 → 827.74] Python.
[828.26 → 830.92] And, you know, so now you're not learning about what is a for loop, right?
[830.94 → 832.40] You know about the concepts of looping.
[832.58 → 834.96] Now it's just a matter of, okay, how do I loop with the syntax?
[835.24 → 835.42] You know?
[835.48 → 840.72] And so it's, it's that kind of applied, like that kind of mapping that I think helps me
[840.72 → 841.70] accelerate my learning.
[841.80 → 843.00] It's a very nerdy answer.
[843.10 → 843.50] I'm sorry.
[843.94 → 844.38] Love it.
[844.52 → 844.90] Love it.
[845.10 → 848.24] I guess I'm like the nerd curmudgeon that's going to be on this show.
[849.18 → 850.32] You found your people.
[850.80 → 851.76] Okay, cool.
[852.08 → 857.34] What's been your favourite language to work with since you've like sort of consider yourself
[857.34 → 858.90] a polyglot and learned a lot?
[859.06 → 859.88] And why is it TypeScript?
[860.64 → 861.44] And why is it TypeScript?
[861.58 → 861.98] It's so funny.
[861.98 → 863.98] I'm learning TypeScript now for the first time.
[864.04 → 865.66] I've managed to avoid it my whole career.
[865.66 → 869.02] And like the company I work for now uses TypeScript, and I'm learning it.
[869.12 → 871.90] And it's this fascinating curmudgeon-y experience.
[872.22 → 876.92] And I think I'm slowly understanding the benefits, but like we have to also be honest and
[876.92 → 883.04] acknowledge that like with good testing and good coding practices, you don't need TypeScript.
[883.04 → 887.34] And so, you know, I just think it's very important to like state that, right?
[887.44 → 893.92] Like TypeScript is there because we as developers are generally like lazy in a good way.
[894.14 → 899.60] And we're there, like it's there to kind of combat our laziness around not having proper
[899.60 → 903.46] conventions, you know, in a language that lets you shoot yourself in the foot all the time.
[903.52 → 903.66] Right?
[903.72 → 905.24] So like just putting that out there.
[905.50 → 906.90] I think I forgot the original question.
[907.30 → 908.04] Your favourite one.
[908.24 → 909.42] Your favourite one.
[909.42 → 910.88] Oh, favourite one.
[911.04 → 913.44] Oh, favourite one for sure is JavaScript.
[913.68 → 914.12] I'm sorry.
[914.32 → 917.14] I mean, I think like it's about accessibility.
[917.64 → 920.72] It's about like language of the web.
[920.92 → 922.62] It's, you know, there's like, it's so accessible.
[922.92 → 924.26] JavaScript lets you do so much.
[924.40 → 926.06] There's like no compiler needed, right?
[926.10 → 928.76] Like that should be like the tagline for JavaScript.
[929.02 → 932.12] Like JavaScript, it just works, you know?
[932.32 → 936.44] Like for me, that's like accessibility trumps all things.
[936.44 → 943.14] So accessibility and then like scale of usage, scale of examples, like ecosystem, right?
[943.20 → 948.80] Like there's so many kind of metrics, I think, to kind of score tools and languages and frameworks
[948.80 → 953.82] or whatever, like ecosystems on and like JavaScript, like really like massively wins on like all
[953.82 → 954.70] of those counts.
[954.70 → 963.48] So last question for you here before we skip to the next segment, which is what made you want to join us nerds here at JS Party?
[963.60 → 965.48] And what do you think you'll bring to the show?
[965.80 → 966.74] That's all a mail.
[967.46 → 967.72] Yeah.
[967.72 → 967.76] Yeah.
[968.00 → 974.70] I like, I'm really excited to be on this show because I really, you know, as I progressed
[974.70 → 980.22] through my career, I find myself kind of like lecturing a lot and having these like weird
[980.22 → 982.22] professorial moments with people.
[982.62 → 985.72] And I think it's like an outlet for that energy.
[985.88 → 990.88] And, you know, I really have like a strong passion when it comes to like teaching.
[990.88 → 1001.00] And also I think being a woman and a person of colour, that's like quite senior, you know, there's a representation factor,
[1001.32 → 1007.34] which I think I bring here that is really important and like inspirational to others.
[1007.50 → 1013.26] It's never something I went in, like I never spoke at a conference or did community work because I was like,
[1013.38 → 1015.90] I need to represent my, you know, brown people or whatever.
[1016.44 → 1016.56] Right.
[1016.76 → 1019.26] Like it's just the feedback that I've consistently gotten.
[1019.26 → 1019.62] Right.
[1019.62 → 1026.44] It's like the DMs that I get, or it's the people who apply for jobs referencing that they saw me speak, and they want to work with me.
[1026.58 → 1029.20] And like, you know, like it's, it's things like that.
[1029.26 → 1030.68] So your representation matters.
[1030.92 → 1038.12] And, you know, I think if I can show the world that not only do people who look like me belong.
[1038.18 → 1038.52] Right.
[1038.54 → 1043.90] So like, we're not, we're not just like in the classroom, but we're teaching, we're part of the conversation.
[1043.90 → 1047.34] You know, I think it's good for the web, right?
[1047.34 → 1050.54] Because we need more people that are not white dudes.
[1050.72 → 1051.04] Right.
[1051.28 → 1055.54] Like, like simply put, like representing and teaching and like leading the way.
[1056.46 → 1058.14] Well, we're super excited to have you.
[1058.28 → 1060.60] And on behalf of everybody, welcome to JS Party.
[1060.60 → 1061.42] Thank you.
[1061.42 → 1061.44] Thank you.
[1075.86 → 1077.64] Linde is our cloud server choice.
[1078.16 → 1080.66] Grab the NATO plan for just $5 a month.
[1080.76 → 1081.38] Just five bucks.
[1081.74 → 1086.64] That gets you a gig of RAM, a blazing fast 25 gig SSD, and one terabyte of transfer.
[1086.98 → 1087.60] Let's be honest.
[1087.60 → 1089.74] You can go a long ways on that five bucks.
[1090.22 → 1092.90] When you do need to scale up, their prices are predictable.
[1093.16 → 1094.28] So you can put your calculator down.
[1094.40 → 1094.94] You won't need it.
[1095.24 → 1099.44] We've been running changelog.com on Linde for years, and we've always impressed by their
[1099.44 → 1100.42] award-winning support team.
[1100.96 → 1103.66] Check them out at linode.com slash changelog.
[1103.86 → 1107.06] Once again, that's linode.com slash changelog.
[1114.86 → 1115.54] All right.
[1115.58 → 1117.34] We're back for pro tip time.
[1117.34 → 1118.00] Pro tip time.
[1118.24 → 1119.28] That's my intro theme song.
[1119.38 → 1119.92] Pro tip time.
[1120.54 → 1124.58] We need to really have somebody who's not me make a jingle for that.
[1124.94 → 1125.94] Maybe, Nick, you can do that.
[1126.00 → 1129.42] You could have your robots do a thing for us.
[1129.82 → 1130.38] Automate it.
[1132.30 → 1133.46] Pro tip time.
[1135.04 → 1137.00] This is where we share our pro tips.
[1137.32 → 1141.78] Sometimes we're actually pros at things, and sometimes we just play them on JS Party.
[1142.42 → 1145.68] These are life hacks, lessons learned from doing dumb things, et cetera.
[1146.02 → 1147.64] So let's share the wisdom.
[1147.90 → 1148.72] Nick, you're up first.
[1148.78 → 1149.92] Do you have any pro tips for the people?
[1149.92 → 1150.82] All right.
[1150.82 → 1159.98] I took this as an opportunity to give out some pro tips for your next Zoom call or meeting
[1159.98 → 1164.98] just to make it so you can shine and be the bright star that you are in that Zoom call.
[1164.98 → 1173.12] And I have three apps to kind of help you with that because we're all doing a lot of Zoom calls right now.
[1173.18 → 1174.06] And I spend a lot of time.
[1174.50 → 1176.54] Basically, I'm a professional Boomer.
[1176.54 → 1185.02] And so a couple of things that I found that have helped get a point across, like when I'm screen sharing,
[1185.46 → 1193.28] we're doing pair programming and not using Visual Studio Code's live share thing, foreshadowing a little bit there.
[1193.28 → 1198.88] But one cool thing is this app called, and I forgot the name of it.
[1199.28 → 1199.78] It's called.
[1201.12 → 1202.40] You're really a pro at this.
[1203.04 → 1203.26] Yeah.
[1203.38 → 1207.54] I put the name or the app store, the Mac App Store link in there.
[1208.02 → 1209.60] I think it's called Presenting.
[1209.92 → 1210.40] Presenting.
[1211.06 → 1211.28] Yeah.
[1211.60 → 1212.30] Thank you.
[1212.60 → 1213.08] You're welcome.
[1213.32 → 1214.56] You're really getting your point across here.
[1215.06 → 1215.32] Yeah.
[1215.32 → 1220.24] This basically brings the awesome drawing feature that you have in Slack.
[1220.34 → 1226.68] Like if you ever share your screen on Slack, it gives you that ability to draw on your screen with a simple key command.
[1226.72 → 1230.52] So you can just like toggle it and then your screen becomes a canvas.
[1230.52 → 1239.52] And so you can draw arrows, or you can draw squares or just freehand draw anything and delete it and really get your point across, which is really cool.
[1239.80 → 1244.80] And then for the vane screen share, this is where the next tool comes in.
[1244.80 → 1246.20] And this one is called Video.
[1246.80 → 1250.28] And I'll paste a link in the show notes.
[1250.82 → 1259.82] But it lets you, like when you screen share, you're not sharing your face as much or your face becomes smaller, and you're sharing your screen, which becomes bigger.
[1260.04 → 1261.96] And that's unacceptable if you're vane, right?
[1261.96 → 1269.30] So this lets you combine that by using opacity and the camera to share yourself with the screen as well.
[1269.54 → 1271.92] And so you can get really up close and creepy.
[1272.22 → 1274.48] And it's pretty fun.
[1274.80 → 1288.64] And then the third one I will say is, and I'm probably going to get a lot of hate for this, but there's a Snapchat filter for your webcam or a Snapchat at for your webcam that lets you use the Snapchat filters.
[1288.64 → 1296.60] And the way that I approach that is exclusively with all the Tom Holland snap filters.
[1297.60 → 1303.78] And so when I share my screen, I just have these random I love Tom Holland or pictures of Tom Holland.
[1304.50 → 1307.96] And I don't know why, but there's a lot of them.
[1308.16 → 1309.92] So it gets you a lot of variety.
[1310.08 → 1311.16] But there you go.
[1311.26 → 1314.44] There are some pro tips to excite your next Zoom call.
[1314.44 → 1318.76] I will say this is the creepiest picture I've ever seen.
[1318.90 → 1322.66] We'll have to include that in the show notes for people to enjoy the creepiness.
[1322.78 → 1323.58] You don't have to be more specific.
[1323.86 → 1324.26] Which one?
[1325.68 → 1326.04] Nope.
[1326.36 → 1326.80] Both of them.
[1326.94 → 1327.34] Wow.
[1328.28 → 1328.68] Very cool.
[1328.78 → 1337.04] So this Video, the idea is instead of being in the corner, like you are the whole screen, but you're just opacity is like cranked down.
[1337.04 → 1340.72] So you're just kind of like a ghost behind what's going on your screen.
[1341.30 → 1341.46] Yeah.
[1341.60 → 1344.54] And it works really well for your dark themed code editor.
[1345.06 → 1349.60] And so with me, I have a very bright background and then a dark theme for Vim.
[1350.08 → 1353.50] And so I just show up like I'm floating in the Vim window, which is really awesome.
[1353.50 → 1354.46] The ghost of Vim past.
[1355.08 → 1355.32] Yep.
[1355.94 → 1356.32] Awesome.
[1356.68 → 1357.46] He's stuck in Vim.
[1357.66 → 1358.18] He can't exit.
[1359.14 → 1359.96] Can't get out.
[1360.84 → 1361.92] That would actually make a good video.
[1361.92 → 1362.22] Literally.
[1364.22 → 1365.46] Just like floating around.
[1365.92 → 1366.18] Epic.
[1366.18 → 1366.30] Epic.
[1366.68 → 1367.16] Yeah, that's funny.
[1367.26 → 1371.76] One of my teammates actually just used that filter at work the other day and I just couldn't believe it.
[1371.82 → 1373.22] I was like, wow, that's incredible.
[1374.08 → 1376.58] And I'm never going to get any work done in meetings anymore.
[1377.06 → 1377.08] So.
[1378.36 → 1385.28] I want to say that I heard a story about somebody whose manager tried it out and turned themselves into a potato and then couldn't figure out how to turn it off.
[1385.32 → 1387.94] And so they give the entire meeting as a potato.
[1388.66 → 1390.24] They couldn't undo it.
[1390.60 → 1391.60] Yeah, I saw that too.
[1391.60 → 1392.56] That was hilarious.
[1393.04 → 1394.66] Because, I mean, there's just something.
[1394.66 → 1397.44] And I think it was like the manager of that team or the leader.
[1398.04 → 1400.48] So it's just like, you know, even more hilarious.
[1400.94 → 1401.48] But yeah.
[1401.96 → 1405.82] Yeah, I'm going to need a link to that because I missed it and I do not want to miss the potato man.
[1406.66 → 1407.54] Potato manager.
[1407.54 → 1408.40] All right.
[1408.56 → 1411.44] Good stuff for those boomers out there.
[1411.60 → 1415.38] Although, Nick, I think you're technically a millennial, but we'll give you a pass on this one.
[1415.76 → 1416.48] Boomer pass.
[1417.72 → 1418.98] Divya, your turn.
[1419.72 → 1419.94] Cool.
[1419.94 → 1423.12] So to go off of that, the foreshadowing.
[1423.32 → 1426.20] I use VS Code Live Share a lot.
[1426.46 → 1435.26] It's really cool because it fixes a lot of pain points you have when, especially you're remote, and you're like, oh, let's type on this thing together.
[1435.26 → 1436.86] And it's really nice.
[1436.96 → 1440.06] It's just sometimes really slow, especially if you have like a lot of things running.
[1440.62 → 1442.92] That's like the only downside to it.
[1443.08 → 1449.66] But in general, I think it's really nice to be able to like share a session and then have two people work on the same.
[1449.84 → 1454.02] So you can be like on a Zoom call sharing a VS Code Live session.
[1454.02 → 1462.24] And then it feels better because then you can also switch when you're pairing who drives rather than like having to be like, oh, let me share my screen.
[1462.38 → 1464.04] And then the other person be like, let me share my screen.
[1464.10 → 1467.04] And then they're in two different states of the project.
[1467.04 → 1470.68] But with this, it's really nice to just be able to work off of the same one.
[1471.42 → 1473.20] And you can make notes and whatever.
[1473.66 → 1478.60] So it feels like you're almost next to the person, even though you're not, which I think is super cool.
[1478.70 → 1481.10] It's made my pairings like really smooth.
[1481.86 → 1483.66] So 100% recommend that.
[1484.02 → 1485.58] And also related.
[1485.80 → 1495.22] So I talked a little bit about using or writing a playground at work, which is like essentially a little like online IDE type thing for validating whatever.
[1496.32 → 1499.52] And I'm building one currently, and I was using Monaco.
[1500.14 → 1502.28] And I complained a lot about Monaco.
[1502.66 → 1506.14] And I have switched away from Monaco completely.
[1507.02 → 1508.68] And I use Code Mirror now.
[1508.82 → 1511.22] And I honestly think it's so good.
[1511.22 → 1522.60] Like if you are thinking of writing like an IDE or a playground, Code Mirror is amazing because it's just like very bare bones and very simple to integrate.
[1523.02 → 1524.36] The resizing is really nice.
[1524.42 → 1527.24] I think I just got annoyed because Monaco didn't have proper types.
[1527.24 → 1530.82] And it also was annoying to resize.
[1531.02 → 1536.74] Like you had to keep telling it to resize when you resize the screen, which is really annoying and Jacky.
[1537.20 → 1539.02] And Code Mirror just automatically resizes.
[1539.66 → 1541.12] And it's just like super simple.
[1541.12 → 1546.96] In order to change the theme, you don't have to include like Monaco has like this giant library.
[1547.38 → 1549.22] And then you can change the themes, which is really nice.
[1549.34 → 1550.54] Code Mirror is super lightweight.
[1550.96 → 1555.16] And you just add in the CSS file if you want that specific theme.
[1555.70 → 1564.24] So if you imagine that your IDE will only have or your particular playground will only have one theme, you can just load that particular CSS file.
[1564.36 → 1566.74] And so you don't have the bloat of like extra other things.
[1567.10 → 1567.98] So I really like it.
[1567.98 → 1569.80] It's spotless, super smooth.
[1570.36 → 1572.52] There are so many different tools that use it.
[1572.62 → 1574.26] I think CodePen uses Code Mirror.
[1574.86 → 1576.56] Svelte's Playground uses Code Mirror.
[1576.96 → 1579.42] And I'm sure like a bunch of other tools as well.
[1579.54 → 1581.24] So it's like super neat and smooth.
[1581.58 → 1584.38] That's the story of the Playground that I'm building.
[1584.50 → 1585.30] It's moved away.
[1585.58 → 1586.18] Sorry, Microsoft.
[1586.48 → 1588.22] Also, Code Mirror is like open source.
[1588.52 → 1588.66] Yeah.
[1588.80 → 1593.76] I think it's funny that they don't have good type support, given that it is literally the editor that powers VS Code.
[1593.88 → 1597.70] So usually what happens is that you have it in like the indefinitely typed or whatever.
[1597.70 → 1599.14] So it's like at type slash.
[1599.52 → 1600.66] It doesn't exist.
[1600.94 → 1603.24] And it's just in the library itself.
[1603.24 → 1608.90] And I had to do some shenanigans with my view config to like grab that type and add it to my config.
[1609.56 → 1612.04] It was a horrible experience.
[1612.76 → 1613.90] I have played with it as well.
[1613.90 → 1619.12] And at least the last time I played with it, you couldn't run it without like it was all AMD.
[1619.34 → 1621.96] And so I had to load require JS into my project too.
[1622.24 → 1622.52] Yes.
[1622.64 → 1623.26] That also.
[1623.72 → 1623.92] Yeah.
[1624.02 → 1624.80] It's still the same.
[1624.88 → 1625.02] Yeah.
[1625.20 → 1625.96] They haven't changed that.
[1626.36 → 1626.56] Oh.
[1626.92 → 1627.22] Anyway.
[1627.22 → 1627.86] Yeah.
[1627.98 → 1641.52] Honestly, what I find kind of interesting in this like explosion of like smart IDEs in the JavaScript community is like as somebody who's been using tools like WebStorm for literally like more than seven years at this point.
[1641.52 → 1649.90] Like I'm just really confused at like all the like hype around VS Code because I'm like, wait, WebStorm, we've had this for years.
[1650.58 → 1652.18] I just think it's interesting.
[1652.30 → 1656.70] Like the barrier to entry, I think, has been licensing, right?
[1656.80 → 1660.16] So I think people have to pay for WebStorm.
[1660.42 → 1664.82] And WebStorm has been this awesome, fancy IDE that can do so many things for years and years and years.
[1664.82 → 1670.88] But I think like just like the accessibility factor of like free, like you can't beat that, you know?
[1671.00 → 1671.72] I'm like, wow.
[1671.80 → 1685.06] Like I feel like WebStorm is kind of getting their lunch handed to them, you know, with VS Code, even though performance wise and like many, many things like are quite good and or better in WebStorm.
[1685.24 → 1689.04] I think the ecosystem factor is where VS Code for me like wins.
[1689.26 → 1689.64] Right.
[1689.64 → 1694.28] And it's kind of like it's like the same idea behind why Slack kind of took off.
[1694.28 → 1694.68] Right.
[1694.72 → 1697.32] Like how many instant messaging and chat apps did we have?
[1697.78 → 1699.26] Like Slack works because of integration.
[1699.56 → 1699.68] Right.
[1699.78 → 1707.34] Like the value add for tools like Slack is like integrating your Jira and like, you know, your Google Drive and like everything else in this like one-stop shop.
[1707.46 → 1708.92] And so, so it's yeah.
[1709.00 → 1710.64] I mean, ecosystem matters.
[1710.86 → 1710.94] Yeah.
[1711.04 → 1711.68] Network effects.
[1711.78 → 1713.84] Everybody uses it because everybody uses it, you know?
[1714.04 → 1714.32] Yep.
[1714.60 → 1714.82] Yes.
[1715.00 → 1715.28] Pretty much.
[1715.60 → 1716.52] Tough to break it out of that.
[1716.82 → 1717.06] Yeah.
[1717.22 → 1718.00] That's fascinating.
[1718.14 → 1719.04] Thanks for sharing that, Divya.
[1719.38 → 1720.16] Yeah, for sure.
[1720.16 → 1725.68] And then my last thing is just I started doing a bunch of game development outside of work, which has been really fun.
[1726.96 → 1729.98] Because I've been so tired of just like doing coding projects.
[1730.18 → 1733.84] That's like strangely related to work and practical.
[1734.36 → 1734.46] Yeah.
[1734.48 → 1735.64] I don't want to do practical things.
[1735.66 → 1736.74] I want to do like dumb things.
[1736.82 → 1740.70] And so I took game development classes in college before at WEI.
[1740.94 → 1741.24] Yay.
[1741.56 → 1742.34] Oh, my God.
[1742.42 → 1742.64] Yeah.
[1742.76 → 1743.32] Holy crap.
[1743.82 → 1743.98] Yeah.
[1744.08 → 1745.36] We did talk about this.
[1745.44 → 1745.54] Yeah.
[1745.54 → 1746.38] That's so funny.
[1746.38 → 1748.18] I keep forgetting that you did WEI as well.
[1748.40 → 1748.74] Yeah, I did.
[1749.10 → 1750.88] And so I took game development classes.
[1751.28 → 1752.52] I did it in Unity.
[1752.86 → 1756.94] Hated Unity because I wrote it in JScript because I refused to write C Sharp.
[1757.54 → 1759.98] And like sort of chucked that aside.
[1760.10 → 1762.44] But then I found this new engine called Godot.
[1763.18 → 1765.56] And it's open source, which is awesome.
[1765.74 → 1766.58] I'm all for that.
[1766.88 → 1772.46] I think the biggest thing like from reading Reddit posts and stuff is they're sort of similar because you use C Sharp in both.
[1772.46 → 1777.24] But in Unity, if you want dark mode, you have to pay for it and Godot dark mode is free.
[1777.92 → 1778.86] It's the little things.
[1779.38 → 1780.66] It's the little things.
[1781.12 → 1781.24] Yeah.
[1781.30 → 1781.56] I know.
[1781.88 → 1783.60] Don't you care about our eyes, Unity?
[1783.76 → 1784.32] I know.
[1784.62 → 1785.12] I know.
[1785.32 → 1786.52] They care about your wallet.
[1788.04 → 1790.12] Just code with your sunglasses on, everyone.
[1790.16 → 1790.52] I know.
[1790.58 → 1791.16] Save your eyes.
[1792.32 → 1793.04] Open your wallet.
[1793.96 → 1794.44] Exactly.
[1794.62 → 1795.42] Open your wallet.
[1795.42 → 1796.58] Open your wallet.
[1796.74 → 1797.04] LOL.
[1797.62 → 1798.22] That's funny.
[1798.76 → 1798.92] Yeah.
[1799.06 → 1801.38] But yeah, it's a perfect game engine.
[1801.38 → 1807.02] And it's also like more geared towards indie developers, which I think is cool because I'm not like pro at all.
[1807.14 → 1807.90] I don't know what I'm doing.
[1808.04 → 1808.94] What kind of game are you building?
[1809.24 → 1813.38] So I'm building a platformer, like a 2D, like pixel style platformer.
[1814.06 → 1814.48] Sweet.
[1814.76 → 1816.10] Just because I think it's cool.
[1816.32 → 1819.70] The art style can be super lo-fi, which is really fun.
[1819.70 → 1823.24] And for pixel tools, this is another like fun tool thing.
[1823.32 → 1826.64] If anyone's interested, I'm using this tool called Aspirate.
[1827.58 → 1830.18] I'll link in the show notes for pixel art.
[1830.18 → 1831.80] You can use like whatever.
[1832.02 → 1833.24] You can use Illustrator or anything.
[1833.40 → 1837.12] But Aspirate is like very low definition tool for pixel art.
[1837.38 → 1839.56] There is, I think, a cost for it.
[1839.62 → 1841.60] So it's like $5 for the app.
[1841.92 → 1849.86] But it's free if you download the binary from GitHub and build it yourself, which I did because I'm cheap.
[1849.86 → 1854.64] Like any other developer, I'm like, I know how to do this.
[1854.82 → 1860.12] And so I pulled it down, and I essentially executed the binary and stuff and it runs.
[1860.30 → 1864.06] You should put it up on Docker Hub and make everyone's life easier in the future.
[1864.20 → 1865.42] No, but I feel bad.
[1865.42 → 1865.86] Oh, yeah.
[1865.92 → 1866.72] You actually take that back.
[1866.92 → 1867.84] Do not do that.
[1867.84 → 1868.26] I don't want...
[1868.26 → 1869.60] Nobody do that.
[1869.86 → 1870.12] Yeah.
[1870.22 → 1871.80] I want them to get the money.
[1872.80 → 1873.80] Cut this out of the show.
[1873.80 → 1877.64] I'm the worst.
[1877.90 → 1878.52] Like I want...
[1878.52 → 1879.20] Okay.
[1879.50 → 1879.70] Yeah.
[1879.80 → 1884.66] I decided since they offered this free alternative, I might as well take them up on it.
[1884.84 → 1885.72] But it's very cute.
[1885.86 → 1888.22] It's very like small, simple.
[1888.56 → 1890.30] There's not a lot of like craziness to it.
[1890.30 → 1893.60] Because usually with graphics development, it's like there's so many different tools.
[1893.70 → 1894.34] It's hard to learn.
[1894.70 → 1899.18] But for this, the tools are so bare bones that it's very quick for you to like get up and running.
[1899.18 → 1901.70] Also, I think the timelines are super nice.
[1901.82 → 1903.46] So you can create little pixel animations.
[1904.20 → 1905.20] So cute.
[1905.54 → 1907.80] And they have onion skinning, which is great.
[1907.96 → 1913.68] If you're familiar with animations, you could just like layer on frames and then just like draw as you go.
[1914.08 → 1915.48] Oh, so good.
[1915.94 → 1916.32] Awesome.
[1916.70 → 1917.26] Very cool.
[1917.60 → 1917.74] Yeah.
[1917.84 → 1920.70] We should link to Jen Schiffer's pixel art.
[1920.86 → 1921.20] Yes.
[1921.40 → 1922.16] Actually, yes.
[1922.24 → 1922.86] That's a good one.
[1922.96 → 1923.60] Jen is like...
[1923.60 → 1926.26] We both worked at Baku, but also we're friends now.
[1926.26 → 1929.58] And like I feel so cool saying like I'm friends with Jean Schopfer.
[1929.76 → 1931.64] It feels like I'm saying I'm friends with Beyoncé.
[1932.28 → 1935.60] Like basically it's like the equivalent of Beyoncé in the web community is Jean Schopfer.
[1936.06 → 1939.54] So she's like on an incredibly awesome, hilarious, satirical blog.
[1939.62 → 1941.38] But also she does pixel art, which is cool.
[1941.52 → 1943.64] So yeah, if you want some INSP, Divya.
[1943.98 → 1944.42] For sure.
[1944.70 → 1944.92] Yeah.
[1945.40 → 1945.58] Yeah.
[1945.68 → 1946.84] So I guess, yeah.
[1946.94 → 1948.54] Do you want to introduce me, Jared?
[1948.64 → 1950.64] Or should I just jump in?
[1950.74 → 1950.90] Go ahead.
[1951.18 → 1951.78] Do it.
[1951.84 → 1952.58] I already introduced you.
[1952.64 → 1953.32] That was the first segment.
[1953.46 → 1954.20] Now you're on the show.
[1954.20 → 1954.60] Just talk.
[1954.94 → 1955.84] Now just talk.
[1955.84 → 1956.48] Just talk.
[1956.60 → 1956.78] All right.
[1956.90 → 1961.70] So my pro tips are like I've been very like in the debugging headspace.
[1962.06 → 1964.46] So like a couple of things I have to share on debugging.
[1964.70 → 1968.88] The first thing is I'm surprised at the number of developers that don't know about console.trace.
[1969.06 → 1971.58] So console is an object with lots of methods.
[1971.70 → 1975.94] I would highly advise you to just like look at all the things that you can do with console.
[1976.16 → 1983.32] You can do many, many, many cool things, including like console table for like just easy viewing of data and like JSON object data.
[1983.66 → 1984.88] Just tons of cool stuff.
[1984.88 → 1986.62] But my favourite thing is trace.
[1986.82 → 1994.86] So when I'm debugging something, and I'm like want to cheat, and I don't want to like, you know, have to figure out like what's calling what.
[1995.04 → 1995.18] Right.
[1995.24 → 1999.52] So you instead of just doing a log, you can do a trace, which will do a log plus.
[1999.52 → 2001.96] And that plus is like the actual stack trace.
[2002.36 → 2004.52] And you can, that works in Node, that works in the browser.
[2005.04 → 2005.44] It's incredible.
[2005.86 → 2008.42] The second thing I want to share, actually there are two things.
[2008.68 → 2010.18] There are copy commands in DevTools.
[2010.18 → 2011.84] So there are two ways.
[2012.04 → 2016.78] I'm sure if you're debugging stuff, there's a lot of like copying and pasting back and forth, et cetera.
[2017.20 → 2021.32] You can kind of simplify this by using the copy object in the JavaScript console.
[2021.32 → 2028.06] So if you essentially just have like something that you're debugging, and it's a value that you want to be able to inspect in like another tool.
[2028.66 → 2034.08] So you basically, you can use the copy object and like, and then it's available on your clipboard.
[2034.26 → 2038.52] So you can wrap your code in the copy object and, or wrap a variable in the copy object.
[2038.52 → 2042.18] And then it'll just, it's on your clipboard, and you can paste it wherever you want.
[2042.66 → 2045.38] Same kind of thing for network responses.
[2045.80 → 2057.02] So sometimes when I'm doing API design or writing contract tests or something, you know, it's really nice to be able to just inspect my, or just like, or grab like my mock data or real data or whatever from the console.
[2057.16 → 2060.36] And it's always kind of a pain, but there's like some options.
[2060.46 → 2063.76] And we're linking that in the show notes so you all can see that.
[2063.76 → 2069.50] But there's an easy way for you to actually just copy network responses, and then they're available on your keyboard as well.
[2070.52 → 2071.20] Super cool.
[2071.78 → 2077.62] So the next couple of things I have to share are just some general tooling that I always install on all my new machines.
[2077.92 → 2080.06] It used to be called spectacle for like window management.
[2080.42 → 2084.22] So without this tool, I'm very disoriented, and I don't know how to use a computer.
[2084.38 → 2090.44] I just use my keyboard to move everything around, resize, centre, full screen, get it out of my way, you know?
[2090.44 → 2094.52] Um, but spectacle, unfortunately, as a few months ago, it's just no longer maintained.
[2094.52 → 2096.50] So rectangle is its predecessor.
[2096.96 → 2102.74] And so we'll link both, but obviously like start with rectangle if you're starting with it today.
[2102.74 → 2106.88] And then gift box is like one of my favourite tools too, for like making gifts and videos.
[2106.88 → 2111.16] And especially for doing front end work, it's a really nice thing to include in your PRs.
[2111.16 → 2113.60] It's a good thing to like to send to your product folks or your designers.
[2113.60 → 2117.40] Um, just like make a video, uh, you know, visual stuff.
[2117.40 → 2121.42] It's like communicates so much faster and better than like text.
[2121.42 → 2124.40] So just like use video when you can.
[2124.40 → 2127.76] And gift box is like a paid app that you can use on macOS.
[2127.88 → 2128.40] And it's incredible.
[2128.90 → 2129.34] Nice.
[2129.54 → 2129.88] Love it.
[2130.26 → 2131.42] I use something really similar.
[2131.60 → 2137.36] I use a tool called cap or captures with a K, and it does the same thing, but, but you're
[2137.36 → 2137.54] right.
[2137.56 → 2143.16] It does like wonders when you're like wanting to show differences like, Oh, this is what it was
[2143.16 → 2143.56] before.
[2143.64 → 2145.88] This is what it is now, or even to show interaction.
[2146.58 → 2146.78] Yeah.
[2146.90 → 2150.00] And the nice thing is the user experience of gift box is nice.
[2150.00 → 2154.72] So you can make things and just, you know, drag it into Slack or, you know, have it automatically
[2154.72 → 2156.50] go onto your clipboard after it's done.
[2156.62 → 2160.12] Like there's a nice usability there, which I think is good for, for dev workflows.
[2160.48 → 2161.60] But yeah, I couldn't agree more.
[2161.68 → 2166.36] Like making a video of a bug and saying like, is this expected is so much better than like,
[2166.72 → 2172.90] here are 40 lines of text, like, and like 17 questions that follow to clarify, you know,
[2172.90 → 2173.86] like, yeah.
[2174.22 → 2178.08] Combine that with presenting, and then you can notate it, annotate it before you take
[2178.08 → 2178.62] the screenshot.
[2179.02 → 2179.42] Wow.
[2179.62 → 2182.82] And then you put Tom Holland on it and then make it a ghost.
[2185.00 → 2185.92] Overachieving, Nick.
[2186.86 → 2187.10] Yeah.
[2187.10 → 2192.22] Well, I'll just very quickly share a pro tip, more conceptual than what you all have been
[2192.22 → 2195.92] sharing, but you all know that cliché, you're the average of the five people that you surround
[2195.92 → 2196.58] yourself with.
[2196.66 → 2198.32] You know, that's the cliché.
[2198.44 → 2200.12] Well, first, let me say something about clichés.
[2200.24 → 2204.24] Clichés are clichés because they are true and they, they are so true that you say them
[2204.24 → 2205.38] so much that they become a cliché.
[2205.60 → 2207.14] So don't discount a cliché.
[2207.14 → 2213.50] But my advice is, is given that, which I think it's true, I mean, it's not true.
[2213.58 → 2216.84] Like you don't, you don't average out people that are around you and five, who came with
[2216.84 → 2217.50] that number five.
[2217.92 → 2224.66] But if you want to learn a thing or learn a lot of things in life, find people who are
[2224.66 → 2228.36] smarter than you, surround yourself with them and then learn.
[2229.00 → 2230.34] Now that's a simple formula.
[2230.56 → 2234.52] It's somewhat hard to do, but it's gotten a lot easier lately.
[2234.52 → 2240.26] Especially with the advent of podcasts, because you can now have as a quote unquote friend,
[2240.92 → 2247.00] the smartest people on earth out there talking into microphones, and you don't have to maintain
[2247.00 → 2247.76] that relationship.
[2247.88 → 2248.92] There are a lot of things you can't do.
[2249.00 → 2252.94] Like you can't interactively ask them things, which sometimes is necessary to learn, but you
[2252.94 → 2256.92] can learn a lot just by gleaning from smart people all around.
[2257.08 → 2258.30] So I would advise others.
[2258.38 → 2259.04] I do it all the time.
[2259.46 → 2261.20] I've learned a ton, true podcasts.
[2261.20 → 2265.20] And I would advise, hey, if you're listening to this podcast, maybe you're trying to do
[2265.20 → 2265.42] that.
[2265.50 → 2266.20] Why are you listening to us?
[2266.24 → 2266.92] We're a bunch of schmucks.
[2267.00 → 2267.34] I'm just kidding.
[2268.32 → 2269.16] We got a Mel here.
[2269.24 → 2269.64] We got Nick.
[2269.70 → 2270.12] We got Divi.
[2270.16 → 2275.06] We got some smart folks, but go out there and learn via just hanging out and listening.
[2275.46 → 2276.16] That's a pro tip.
[2277.00 → 2277.44] All right.
[2277.54 → 2278.50] That's pro tip time.
[2278.92 → 2281.84] Insert Nick's robot theme song here.
[2283.80 → 2284.94] Pro tip time.
[2286.80 → 2287.64] And we'll be right back.
[2287.64 → 2303.12] What up, party animals?
[2303.40 → 2305.34] Here's some news that you may not have heard yet.
[2305.78 → 2307.84] Gatsby now has a partnership program.
[2308.04 → 2312.82] If you are building Gatsby sites for clients, or you're not yet, but you wish you were, you
[2312.82 → 2317.40] can now grow that with confidence by getting support and resources directly from the Gatsby
[2317.40 → 2317.76] team.
[2318.12 → 2322.60] Become a Gatsby certified partner today to accelerate your growth alongside their amazing
[2322.60 → 2323.08] ecosystem.
[2323.52 → 2329.16] Get exclusive access to Gatsby's product roadmap, beta test new features, access training materials,
[2329.16 → 2330.84] and connect with the Gatsby team.
[2331.16 → 2333.72] There's a whole bundle of partnership benefits.
[2333.94 → 2334.86] The sky's the limit.
[2334.86 → 2339.42] So check out Gatsby's partnership program using the link in the show notes or point your
[2339.42 → 2342.84] browser to gatsbyjs.com slash changelog.
[2342.98 → 2348.92] Once again, there's a link in your show notes or gatsbyjs.com slash changelog.
[2364.86 → 2372.08] All right, we are back.
[2372.18 → 2375.88] And speaking of learning things from people that are smarter than you, I'm trying to understand
[2375.88 → 2384.20] this CSS sweeper project that I came across last week, which is basically a minesweeper
[2384.20 → 2388.24] completely in HTML and CSS, no JavaScript.
[2388.24 → 2392.96] And it accomplishes the game, which we'll link it up, and you can go click through and
[2392.96 → 2393.94] play it yourself.
[2394.06 → 2397.56] It's the classic Windows minesweeper, which is a great time waster.
[2398.10 → 2400.66] I was more of a free cell guy myself, but still a good one.
[2401.00 → 2406.50] But it uses this trick in order to make CSS basically a full on programming language.
[2406.94 → 2409.32] They call it the space toggle trick.
[2410.14 → 2413.84] And it's taking advantage of CSS variables.
[2413.84 → 2418.66] This is explained in the README of the repo, which I'm sure you all are looking at.
[2419.56 → 2420.64] But I started reading that.
[2420.70 → 2421.86] I was like, I don't get it, you all.
[2422.12 → 2423.26] I don't understand what's going on here.
[2423.82 → 2425.74] So I thought maybe we could demystify it.
[2425.74 → 2429.30] Maybe one of you three can demystify it for me, or we could talk through it together.
[2430.28 → 2434.24] Who's given this a look, and who thinks they can explain what's going on and how you can
[2434.24 → 2435.60] play minesweeper with just CSS?
[2436.14 → 2438.68] Oh, I took a look and I feel like it makes sense.
[2438.68 → 2443.94] And then I opened up a quick code pen and tried to replicate a little bit of it.
[2444.78 → 2447.34] And so far in this call, I have not been able to get that working.
[2447.74 → 2450.92] But it's taking advantage of a couple of things with CSS variables.
[2451.06 → 2456.00] One of them is that you can set a default value for a variable.
[2456.00 → 2465.10] And the other is this what they call the space toggle trick where you set a variable to an
[2465.10 → 2469.02] empty space and then change it later to initial.
[2469.28 → 2474.56] And you take advantage of the idea that you can set a CSS variable, and then it will go
[2474.56 → 2478.10] to the most recent value of that.
[2478.10 → 2483.22] So if you think about the CSS cascade, you can set it somewhere else and set it to initial
[2483.22 → 2488.24] and then it will flip, basically like flipping a bit to be whatever the other value is.
[2488.90 → 2493.66] And you can take advantage of that to toggle things on and off and then take advantage of
[2493.66 → 2500.94] states in CSS, like a checkbox being checked to flip that bit and change it to something else.
[2501.34 → 2505.56] I was wondering what was triggering the actual interaction or triggering the logic,
[2505.56 → 2509.44] which is it just using like is checked or like some sort of selector.
[2510.16 → 2511.22] Like a radio button or something.
[2512.06 → 2512.20] Yeah.
[2512.62 → 2514.64] That's I mean, that's like mind-blowing cool.
[2514.78 → 2518.12] I did not know about this until like right before this show started.
[2518.26 → 2519.82] And I was like, oh, wow, what is this?
[2520.16 → 2520.40] Yeah.
[2520.44 → 2523.72] It's just been mind-blowing, like looking through the README and picking through the code.
[2523.96 → 2528.26] I think for me, what's a very interesting kind of takeaway here is this concept of variables
[2528.26 → 2533.16] kind of being introduced into the language, into CSS and how I think, you know,
[2533.16 → 2539.76] it's another story of like the developers kind of paving the way for the web platform, right?
[2540.00 → 2544.30] You know, web developers and library authors kind of like taking that, like doing that innovation
[2544.30 → 2547.32] in a low stake, low risk way, right?
[2547.34 → 2550.82] Because it's very, you can't really mess around on web platform.
[2551.02 → 2552.44] It's just too high stakes, right?
[2552.52 → 2553.82] People, it's banking software.
[2554.14 → 2555.86] It's how people do their jobs.
[2555.96 → 2556.64] It's how, right?
[2556.64 → 2562.08] Like, so it takes, you know, that's why the arc of like web development, standards development
[2562.08 → 2563.06] is so long.
[2563.20 → 2565.20] You know, it takes a while to get it right.
[2565.28 → 2568.88] It takes a while to perfect it and get it, you know, have consensus on implementation,
[2569.08 → 2569.32] et cetera.
[2569.52 → 2574.22] But, you know, this is a clear example for me of, you know, web developers leading the
[2574.22 → 2574.70] way here.
[2574.78 → 2577.08] And it's, I think it's a good moment for us, right?
[2577.08 → 2581.52] It's always a good thing when something that we've been doing for a while, and we have
[2581.52 → 2583.22] conventions that are not official, right?
[2583.22 → 2586.76] They're like best practices are now kind of abstracted into the platform, right?
[2586.78 → 2590.90] That just kind of, that like, it frees up our memory for something else, right?
[2590.92 → 2593.10] So that's kind of, that's exciting for me.
[2594.10 → 2594.50] Yeah.
[2594.92 → 2596.00] Divya, what's your take on this?
[2596.26 → 2597.16] On the space toggle?
[2597.28 → 2599.32] I think it's, it's super cool.
[2599.62 → 2603.32] I've used CSS variables before, but I've never used it to this level.
[2603.86 → 2605.82] And it is mind-blowing.
[2606.08 → 2610.92] I mean, I don't feel so bad because it is a trick that not a lot of people have heard of,
[2610.92 → 2617.72] I think in that particular GitHub README, they reference just like that it's been discovered
[2617.72 → 2620.62] like three times or something like that.
[2621.08 → 2622.26] So yeah, it's pretty cool.
[2622.84 → 2629.50] It's a fairly novel concept that's only been like in the README, they refer to it being
[2629.50 → 2630.98] discovered three times.
[2631.10 → 2636.32] And I think it's only been like, Anna Tudor found it supposedly three years ago and then
[2636.32 → 2638.88] no one talked about it until really recently.
[2639.20 → 2642.66] And so I think it's still blowing a lot of people's minds.
[2642.66 → 2647.42] And even when you look at the tweet in which, um, is it James?
[2647.80 → 2649.42] He wrote about finding that trick.
[2649.76 → 2651.88] He's like, not a lot of people engaged with it.
[2651.96 → 2654.80] It's not like thousands of likes and stuff.
[2655.02 → 2656.00] So yeah.
[2656.32 → 2661.04] The question is, is this a cool novelty by taking advantage of a feature that didn't really
[2661.04 → 2662.58] expect you to use it this way?
[2662.58 → 2667.90] Or is this so useful that you'll start to see it become more than just a trick, something
[2667.90 → 2670.08] that actually has real world value?
[2670.56 → 2673.48] Maybe it gets framework eyes and people start building things with it.
[2673.54 → 2676.64] Or is it just going to stay in like the, Hey, remember the CSS Minesweeper?
[2676.70 → 2677.20] That was cool.
[2677.64 → 2679.02] I think it might be a niche.
[2679.12 → 2683.78] Like, honestly, the thing that I find the most fascinating is like, it wasn't referred in
[2683.78 → 2684.04] here.
[2684.12 → 2689.70] It's someone used that trick with CSS, with like media queries, which I think is really neat
[2689.70 → 2694.44] because oftentimes with media queries, you end up having to write a lot of extra craft
[2694.44 → 2698.42] around like, Oh, for this media query and this class do this.
[2698.42 → 2705.26] But then if you could utilize this particular space toggle, that would make your code, like
[2705.26 → 2707.00] it won't make it more understandable.
[2707.28 → 2709.18] It will actually make it less understandable.
[2709.98 → 2712.08] I can't understand what I'm looking at right here.
[2712.56 → 2717.80] If anything, it would make it like less messy, but I don't know at what costs.
[2718.28 → 2718.84] So yeah.
[2718.84 → 2719.82] Time will tell.
[2719.92 → 2720.52] We'll check it out.
[2720.68 → 2722.86] CSS Sweeper on GitHub.
[2722.98 → 2724.46] Of course, the links in your show notes.
[2725.18 → 2727.06] This was a super fun episode.
[2727.22 → 2728.60] Super fun conversation.
[2728.74 → 2731.38] We hope everybody enjoyed it as much as we did.
[2731.86 → 2732.58] That's our show.
[2732.64 → 2733.56] We'll talk to you next time.
[2736.50 → 2737.32] Did you hear?
[2737.48 → 2739.22] We are launching a membership program.
[2739.48 → 2742.58] It's called Changelog++ and we think it'll be super cool.
[2743.18 → 2745.66] Join the club for 10 bucks a month or $100 a year.
[2745.66 → 2750.22] And if you move fast, you can get in for just six bucks a month or $60 a year.
[2750.22 → 2752.84] That discount ends on September 1st.
[2752.84 → 2757.70] So join today to support our work, get closer to the metal and make the ads disappear.
[2757.92 → 2760.84] Learn more at changelog.com slash plus.
[2761.06 → 2764.38] Once again, that's changelog.com slash plus.
[2764.38 → 2767.52] JS Party is brought to you by amazing sponsors.
[2767.76 → 2771.52] Thanks again to Vastly, Linde, and Rollbar for their continued support.
[2772.12 → 2775.58] And our beats are produced by the one and only Break master Cylinder.
[2776.30 → 2777.40] That's all for now.
[2777.96 → 2780.38] Node best practices next week.
[2780.38 → 2794.74] Change log plus.
[2795.42 → 2796.88] Clap your hands, everybody.
[2797.22 → 2798.98] If you've got what it takes.
[2799.22 → 2803.54] Because I'm Curtis Blow and I want you to know that these are the boys.
[2803.98 → 2807.12] Nick, has anyone ever told you that you look like, what's his name?
[2807.24 → 2807.92] Hugh Jackman.
[2807.92 → 2810.06] Like very Wolverine.
[2810.44 → 2811.08] Thank you.
[2811.36 → 2811.62] No.
[2811.96 → 2812.94] Definitely a compliment.
[2813.88 → 2815.18] No one's told you that?
[2815.42 → 2815.78] No.
[2816.32 → 2817.00] Oh my God.
[2817.28 → 2819.40] People suck because they're thinking it.
[2819.82 → 2821.70] They just haven't given you that compliment.
[2821.98 → 2822.20] Yeah.
[2823.66 → 2824.36] Thank you.
[2824.64 → 2825.30] You're welcome.
[2827.20 → 2828.50] Divya, do you see the resemblance?
[2828.64 → 2829.36] I can see it.
[2829.66 → 2831.12] I think it didn't occur to me.
[2831.80 → 2833.42] And then, yeah, I can see it.
[2834.06 → 2836.00] Kind of like a more handsome Hugh Jackman.
[2836.00 → 2837.12] Yeah, for sure.
[2837.12 → 2838.10] Like more handsome.
[2838.10 → 2839.08] Like if he was more handsome.
[2839.28 → 2839.48] Smart.
[2839.92 → 2841.50] Hugh Jackman who could program, right?
[2841.56 → 2841.86] Right.
[2841.94 → 2842.12] Yeah.
[2842.30 → 2843.96] Maybe that should be a future show.
[2844.34 → 2846.64] Like, you know, celebrities.
[2846.90 → 2849.20] Like, which celebrities do you wish could program?
[2852.02 → 2854.40] Which celebrities do you wish could program?
[2854.90 → 2855.68] That's a good segment right there.
[2855.68 → 2856.16] That's a good segment right there.
[2856.16 → 2856.44] That's a good segment, right?
[2856.48 → 2858.00] Megan, that's a good segment.
[2858.00 → 2859.32] DM Bestie?
[2859.32 → 2859.40] That's a good segment.
[2859.88 → 2860.30] announcement.
[2860.30 → 2860.48] That's a good segment.
[2860.58 → 2860.70] Ask.
[2860.70 → 2860.74] Coast Guard.
[2860.86 → 2861.42] Coast Guard.
[2861.42 → 2861.46] Do you want to watch Marvel as well?
[2861.62 → 2862.08] That's a good segment?
[2862.08 → 2862.34] Now, let's go that Fascias & Avengers Tampico сделable.
[2862.46 → 2862.76] No.
[2862.76 → 2862.78] You want to watch Marvel vermicular.
[2862.78 → 2863.18] They've been in 18 on September.
[2863.18 → 2863.32] The Spider-Italy just won Tokyo necessarily.
[2863.32 → 2863.88] See you tomorrow?
[2863.88 → 2865.90] German
[2865.90 → 2866.50] Hey, girl!
[2866.50 → 2867.60] See you in kas Story-
[2867.60 → 2867.96] It's a good title.
[2867.96 → 2868.60] People.
[2868.60 → 2868.92] Okay, April 22 is a gift.
[2868.92 → 2869.80] This is a great movie where I Roger applied you Crusade for the
[2869.80 → 2870.34] year in the удивX.
[2870.34 → 2872.10] We Myanmar
[2872.10 → 2874.68] popular.
[2874.68 → 2875.12] Meeter-
[2875.12 → 2876.22] thing about you call myself.
[2876.22 → 2877.54] You guys in slash
