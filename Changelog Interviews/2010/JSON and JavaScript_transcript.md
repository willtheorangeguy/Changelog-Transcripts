[0.40 --> 2.60]  This is John Resig. You're listening to The Change Log.
[18.16 --> 22.44]  Welcome to The Change Log, episode 0.2.6. I'm Adam Stachowiak.
[22.54 --> 26.36]  And I'm Wynne Netherland. This is The Change Log. We cover what's fresh and new in the world of open source.
[26.48 --> 29.52]  If you found us on iTunes, we're also on the web at thechangelog.com.
[29.52 --> 30.74]  We're also up on GitHub.
[31.74 --> 36.40]  If you go there, you'll find some trending repos, some feature repos from our blog, as well as our audio podcast.
[36.78 --> 39.30]  If you're on Twitter, follow Change Log Show.
[39.86 --> 41.24]  And I am Adam Stach.
[41.32 --> 43.70]  And I am Penguin, P-E-N-G-W-Y-N-N.
[44.02 --> 46.96]  Such a fun time in Austin at Texas JavaScript this weekend.
[47.44 --> 49.82]  Got to interview one of our idols, Douglas Crockford.
[50.36 --> 53.36]  Yeah, he's probably more of your idol than my idol, but definitely high up on me.
[53.64 --> 55.98]  He's the man when it comes to JavaScript.
[55.98 --> 62.68]  The author of the Jason Speck, JavaScript The Good Parts, seems to be the rock star of the JavaScript community.
[63.52 --> 67.88]  Yeah, he seemed to have a very biased opinion against what's going on with HTML5, too.
[68.18 --> 68.58]  Yeah, I know.
[68.66 --> 78.42]  Called for HTML5 to be reset, as he saw it, and focused on less of the whiz-bang features and more on cross-site scripting, which he saw as the more pressing need.
[78.42 --> 81.54]  Yeah, he put a real big emphasis on that with his talk.
[81.90 --> 84.06]  He also had the slide, IE6 must die.
[84.58 --> 85.52]  I think, yeah.
[85.62 --> 88.46]  And then John Resig stood up and said, hey, what about IE7?
[90.36 --> 92.30]  I think we'll take what we can get right now.
[92.58 --> 96.00]  His tagline was, you know, and we must kill it.
[96.28 --> 97.36]  We must kill it, exactly.
[97.50 --> 98.24]  We must kill it.
[98.48 --> 99.06]  That's right.
[99.72 --> 104.86]  And speaking of Resig, he's going to be, we also chatted with him about some mobile web development with jQuery.
[105.16 --> 106.30]  He'll be in a future episode.
[106.92 --> 107.78]  Excited about that.
[107.78 --> 114.40]  Speaking of future episodes, we've got some Skunk Works news that we just can't share quite yet, but we're excited about it.
[114.48 --> 116.88]  And if we've slowed down on the blog, I guess that's why.
[117.46 --> 122.46]  Yeah, we're definitely doing some cool stuff, so just be patient, sit tight, and we'll impress, I'm sure.
[122.98 --> 123.88]  As will this interview.
[123.98 --> 124.56]  Should we get to it?
[124.88 --> 125.46]  Let's do it.
[134.34 --> 137.16]  Hi, we're joined today by Douglas Crockford from, I guess, Yahoo.
[138.06 --> 140.12]  Author of JavaScript, The Good Parts.
[140.38 --> 141.46]  Also, the Jason Spec.
[141.92 --> 143.54]  Douglas, why don't you introduce yourself?
[143.78 --> 146.26]  And for the three people out there that may not know who you are.
[146.54 --> 147.54]  I thought you did just fine.
[148.02 --> 148.70]  Let's go on.
[149.10 --> 149.62]  All righty.
[149.68 --> 152.88]  So, the story of Jason, the Jason saga.
[153.16 --> 155.26]  Just got your session here at Texas JavaScript.
[155.26 --> 161.74]  Give folks the Reader's Digest version of that talk about how the Jason spec came about and what problem you were trying to solve.
[161.74 --> 169.04]  I was in a startup in 2001 that was trying to do what we now call Ajax applications.
[169.80 --> 174.42]  And we needed an efficient way of exchanging data between the browser and our servers.
[174.42 --> 180.34]  And I had an epiphany that we could use JavaScript object literals to do that.
[180.54 --> 183.84]  And so, that was the creation of the Jason notation.
[183.84 --> 188.68]  We tried to convince our customers that it was a good idea.
[189.68 --> 194.06]  And they basically said, no, they couldn't use it because it wasn't a standard.
[194.82 --> 197.32]  So, I declared that it was a standard.
[197.82 --> 202.30]  And since then, it's taken off and become one of the most popular data interchange formats.
[202.80 --> 205.30]  Probably succeeding because of its simplicity.
[205.30 --> 209.62]  Yeah, simplicity, minimalism was an essential part of its design.
[210.74 --> 216.28]  The theory being that the less we need to agree on in order to interoperate, the more likely it will successfully interoperate.
[216.80 --> 220.08]  And so, the specification is really, really simple.
[220.86 --> 224.84]  And because of that, one of the promises of Jason is that it perhaps won't change.
[225.24 --> 226.62]  It'll just become obsoleted.
[227.04 --> 228.08]  Jason can't change.
[228.22 --> 230.26]  There's no version number on it.
[230.26 --> 235.00]  So, there's no way to declare Jason 2, for example, in a compatible way.
[235.70 --> 237.78]  So, Jason will always be Jason.
[238.62 --> 241.64]  And that limits it to an extent, but also makes it more stable.
[241.80 --> 247.32]  It means there's one part of the stack that you can guarantee is not going to ever break on you.
[247.60 --> 249.04]  And that's going to be Jason.
[249.26 --> 250.06]  Jason is stable.
[250.52 --> 255.34]  Jason spec itself is somewhat stable, but a lot of activity happening around the language.
[255.34 --> 261.00]  Talk a bit about Jason parse, Jason stringify, some of these new approaches that are finding themselves into the browser.
[261.32 --> 264.96]  So, support for Jason is now built directly into JavaScript.
[264.96 --> 266.50]  So, you don't need libraries anymore.
[266.88 --> 270.40]  So, json.parse and json.stringify are standard equipment.
[270.64 --> 271.42]  They're very fast.
[271.56 --> 272.20]  They're very secure.
[272.36 --> 272.98]  Very reliable.
[274.00 --> 277.28]  You mentioned in the talk a bit about YAML.
[277.50 --> 279.92]  Was YAML an influence of Jason at all?
[279.92 --> 280.32]  No.
[280.32 --> 280.80]  No.
[280.96 --> 283.58]  I was unaware of YAML when I was doing the Jason work.
[284.14 --> 286.10]  I ran into the YAML guys later.
[286.96 --> 292.18]  And we sort of discovered that we almost had a subset, superset relationship.
[292.18 --> 298.94]  And very often when you see standards like that that are kind of similar, they will try to grow apart.
[299.46 --> 301.18]  And we did the opposite thing.
[301.24 --> 302.34]  We tried to bring them together.
[303.54 --> 309.90]  You mentioned in the talk also about how JavaScript using JSON is excellent for state machines.
[310.62 --> 311.52]  Can you expand on that a little bit?
[311.58 --> 311.88]  No.
[311.96 --> 314.12]  Just JavaScript by itself is excellent for state machines.
[314.12 --> 320.32]  Because you can put functions into your state transition tables, you can come up with really, really efficient state machines.
[321.32 --> 324.74]  What sort of applications are you building with JavaScript and Jason these days?
[326.10 --> 329.14]  I'm actually not doing a lot of Jason stuff myself right now.
[329.20 --> 331.50]  I'm working on trying to fix the browser.
[332.38 --> 336.72]  We've got some really serious security problems that are not being addressed by the PC.
[338.24 --> 341.30]  And we just had a crash here at Texas JavaScript if you heard that.
[341.30 --> 348.08]  In your talk, you had some pretty strong opinions since we're talking about the browser, about HTML5 and that it needs to reset.
[348.18 --> 349.04]  Can you talk about that a little bit?
[349.92 --> 350.26]  Yeah.
[350.44 --> 357.94]  So the browser has one of the best security models of any application delivery system in the world.
[359.68 --> 363.02]  But it's not good enough to do the applications that we need to do.
[363.02 --> 368.24]  And one of the symptoms of that is known as the cross-site scripting problem.
[369.38 --> 374.84]  Where if third-party code gets onto a page, it can do terrible things.
[375.38 --> 378.88]  And there are a number of causes for that problem.
[379.18 --> 380.26]  Some are in HTML.
[380.54 --> 381.32]  Some are in JavaScript.
[381.56 --> 382.20]  Some are in the DOM.
[383.58 --> 384.76]  We need to fix it.
[385.26 --> 389.34]  It's the biggest problem facing web developers and sites that use the web.
[389.34 --> 393.02]  And it's been with us for 14 years.
[393.38 --> 396.72]  And the standards community has not fixed it yet.
[397.36 --> 408.12]  So I'm demanding that we change the priority on HTML5 to get security right first before we do anything else.
[408.26 --> 411.34]  Just for brevity's sake, what exactly is cross-site scripting?
[411.58 --> 412.04]  And what is it?
[412.76 --> 414.82]  It's a confusion of interests attack.
[414.82 --> 421.10]  So if third-party code can get onto a page, for example, through user-generated content,
[422.00 --> 427.02]  that script can do anything that the site's own script can do.
[427.34 --> 432.42]  The browser cannot distinguish between the interests of guest code and its own code.
[432.94 --> 439.96]  So that will give you the right to read the document, to change the document, to dialogue with the user,
[439.96 --> 447.42]  to ask things of the user as though you are representing the site, but you're not.
[447.90 --> 452.36]  It gives you the right to communicate with the site and its servers and its databases.
[453.04 --> 456.62]  So the security problems are huge.
[457.78 --> 460.22]  And fortunately, we know how to fix them.
[460.34 --> 463.74]  There is work done at Google on Caha and my own work on AdSafe,
[463.74 --> 469.24]  which show us how to do secure cooperative applications in a browser context.
[469.94 --> 477.06]  And we've put a lot of the knowledge that we've demonstrated in those systems into ECMAScript 5
[477.06 --> 478.52]  and more into the next edition.
[479.84 --> 482.70]  But that has not gotten into HTML.
[483.90 --> 488.98]  The HTML5 community is going, in my view, the wrong direction.
[488.98 --> 492.28]  And they're making the system significantly more complicated
[492.28 --> 496.32]  and making things significantly worse from a security perspective.
[497.38 --> 501.82]  And so while many of the things that they're talking about are nice and useful,
[502.10 --> 504.78]  we need to get the fundamentals right first.
[505.30 --> 507.80]  So what are you suggesting happen to HTML5?
[508.24 --> 513.08]  I'm proposing that we reset it, that we toss it out and start over with a new charter,
[513.08 --> 519.66]  which is to solve the security problems in as short a time as possible.
[520.14 --> 525.12]  Once we've done that, then we can go back to the pile of stuff that HTML5 was proposing,
[526.12 --> 531.32]  but review each of those features in the context of the new security model
[531.32 --> 536.12]  and the stuff that can be made to conform to the new model, then we'll add.
[536.12 --> 541.72]  If we didn't have the kind of the agreeing meaning of XSS, that acronym in our brains now,
[542.24 --> 546.56]  with the proper security model, cross-site scripting is actually a good thing.
[546.98 --> 548.10]  It's an essential thing.
[548.28 --> 549.38]  It's mashups.
[549.58 --> 554.52]  So we want to be able to have code representing multiple sites interacting on the same page.
[554.58 --> 556.54]  We're working really hard now to make that happen.
[557.04 --> 560.34]  The problem is that the browser did not anticipate that.
[561.16 --> 565.62]  And so it's not possible for each of those modules to defend themselves from the others.
[566.12 --> 569.92]  Or for the page to defend itself against the modules,
[570.02 --> 572.18]  or for the modules to defend themselves against the page.
[572.64 --> 577.86]  In order to do that, which is essential and valuable, we need to fix the browser.
[578.30 --> 581.74]  So one of the techniques that we use today is JSONP or JSON with padding.
[582.14 --> 582.94]  How did that come about?
[583.92 --> 585.18]  JSONP was not mine.
[585.82 --> 592.14]  It was the observation that the same origin policy prevents getting data from another server,
[592.30 --> 594.58]  but doesn't prevent getting script from another server,
[594.58 --> 596.42]  which, when you think about it...
[596.42 --> 596.52]  Crazy.
[596.82 --> 597.46]  Yeah, it's crazy.
[597.54 --> 598.28]  Absolutely crazy.
[598.78 --> 600.46]  But it's a workaround, okay?
[600.56 --> 605.12]  So if you load data as script, you can get around the same origin policy, which is really nice,
[605.62 --> 607.82]  except it comes in as script, not as data.
[607.98 --> 610.18]  So anything that it wants to do, it can do.
[610.48 --> 615.54]  And there's no way that the page can defend itself against JSONP delivery.
[615.54 --> 618.52]  So it's an extremely dangerous practice.
[619.18 --> 622.72]  But the browser doesn't present us many good opportunities.
[623.74 --> 628.02]  I noticed that in the last talk you mentioned the logo for JSON and how you designed that.
[628.20 --> 630.42]  And it's an incredibly creative logo.
[632.04 --> 635.08]  JSON is the kind of lingua franca for APIs now.
[635.40 --> 637.98]  And Adam and I are starting a new podcast to cover APIs.
[638.48 --> 640.54]  And the working title is JSONFM.
[641.14 --> 643.54]  I wanted to know if you would bless that or...
[643.54 --> 644.32]  Sure, that's fine.
[644.68 --> 649.50]  So I intentionally, in JSON, put no IP protection on it.
[650.04 --> 653.54]  So the JSON name is not trademarked.
[653.60 --> 655.28]  The JSON logo is not trademarked.
[655.28 --> 657.48]  So everybody is free to use it however they like.
[657.58 --> 660.22]  You did mention it's MIT, except you can't use it for evil.
[660.22 --> 667.70]  The reference implementation has an MIT license on it with the added provision that it must be used for good, not evil.
[668.20 --> 668.30]  Gotcha.
[668.44 --> 671.92]  I don't think we will fall into that snare with this particular project.
[671.92 --> 676.48]  But usually part of the show we ask you, ask our guests, what's on your open source radar?
[676.68 --> 678.88]  I know that JavaScript is a big part of your world.
[679.20 --> 682.54]  What else that's open source has you excited that you really want to play with?
[683.58 --> 689.42]  My concern about open source is that we're seeing more and more competition against the browser.
[689.42 --> 699.22]  The browser platform is basically 10 or 15 years old now, has not aged well.
[700.02 --> 704.28]  There are lots of much more modern systems that are attacking it.
[704.28 --> 714.04]  The browser will always be lagging behind because it's based on web standards, and standards have to be slow in their development.
[714.30 --> 716.16]  It's just an absolute requirement.
[717.26 --> 719.62]  But it's fallen way far behind.
[720.04 --> 725.44]  So part of the energy behind HTML5 is trying to catch up, which is commendable.
[725.44 --> 728.50]  But as currently practiced, it's misguided.
[728.50 --> 735.96]  So you see the cycle that we're in between native and browser-based applications seems to be like, you know, pant-style fashion.
[736.16 --> 736.94]  It comes and it goes.
[737.48 --> 740.86]  Are we just on another ebb, or do you see it?
[741.26 --> 749.72]  Well, the thing that the browser got right is that its security model, even though I've been saying bad things about it, is actually better than everything else.
[749.72 --> 757.14]  All of the other application delivery systems don't even distinguish between the interests of the user and the interests of the program.
[757.40 --> 759.46]  The browser at least doesn't make that mistake.
[760.74 --> 769.70]  So ultimately, I think the security, reliability, integrity of applications is going to be more important than their whizziness.
[770.60 --> 773.12]  And that's why I think the web is worth saving.
[773.66 --> 775.62]  One last question for you, and a comment first.
[775.74 --> 779.04]  I really enjoy your talks about how you give the history behind certain specs and things.
[779.04 --> 787.02]  For young guys like Adam and myself, how much lacking are we in our history, our roots as programmers?
[787.34 --> 788.38]  I'd say it's pretty tragic.
[789.48 --> 802.24]  There's so much history in our profession, and it shocks me sometimes how little intellectual curiosity some of the practitioners of this craft have about the stuff that they do.
[802.34 --> 803.32]  You know, where did it come from?
[804.14 --> 805.78]  Why do we do things the way they do?
[806.56 --> 808.18]  Sometimes we do things for good reasons.
[808.18 --> 809.36]  Sometimes we don't.
[810.02 --> 813.06]  And you can get a big leg up by understanding the difference.
[813.88 --> 819.78]  I like the way the first semester of physics is usually taught, as history, as biography.
[820.56 --> 822.38]  You know, this is what Galileo did.
[822.46 --> 823.28]  This is what Newton did.
[823.36 --> 824.48]  This is what Copernicus did.
[824.60 --> 825.40]  You know, that's great.
[825.72 --> 828.30]  We don't do that for computer science, and I think we should.
[829.30 --> 830.32]  Thanks for joining us today.
[830.32 --> 831.48]  Thank you.
[831.48 --> 831.52]  Thank you.
[831.52 --> 832.08]  Thank you.
[838.08 --> 841.14]  Thank you for listening to this edition of The Change Log.
[842.14 --> 848.94]  Point your browser to tail.thechangelog.com to find out what's going on right now in open source.
[848.94 --> 858.68]  Also, be sure to head to github.com forward slash explore to catch up on trending and feature repos, as well as the latest episodes of The Change Log.
[858.68 --> 881.50]  Thank you.
[881.50 --> 885.06]  Bring it back, bring it back to
[885.06 --> 887.50]  Auction
[887.50 --> 890.50]  Auction
[890.50 --> 893.90]  For a future
[893.90 --> 896.16]  Bring it back
