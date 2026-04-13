[0.00 --> 1.08]  Who's that girl?
[1.46 --> 2.30]  Who's that girl?
[2.70 --> 3.86]  Who's that girl?
[4.22 --> 5.08]  Who's that girl?
[5.16 --> 5.88]  It's Jess.
[12.68 --> 20.06]  This is JS Party, New Girl Edition, your weekly celebration of JavaScript and the web.
[20.44 --> 22.10]  Join the JS Party community.
[22.42 --> 23.42]  It's totally free.
[23.76 --> 27.28]  Head to jsparty.fm slash community and sign up today.
[27.28 --> 32.26]  Big thanks to our partners at Fly.io, the home of changelog.com.
[32.60 --> 35.94]  Easily launch your app close to your users all around the world.
[36.28 --> 38.64]  Find out how at fly.io.
[39.60 --> 40.80]  It's party time, y'all.
[49.84 --> 50.88]  What's up, friends?
[50.98 --> 55.92]  This episode of JS Party is brought to you by our friends over at Vercel.
[55.92 --> 58.74]  And I'm here with Lee Robinson, VP of product.
[59.50 --> 63.70]  Lee, I know you know the tagline for Vercel, develop preview ship, which has been perfect.
[63.70 --> 66.20]  But now there's more after the ship process.
[66.20 --> 72.62]  You have to worry about security, observability, and other parts of just running an application
[72.62 --> 73.16]  and production.
[73.44 --> 74.20]  What's the story there?
[74.32 --> 76.48]  What's beyond shipping for Vercel?
[77.00 --> 77.18]  Yeah.
[77.26 --> 80.86]  You know, when I'm building my side projects or when I'm building my personal site, it
[80.86 --> 82.50]  often looks like develop preview ship.
[82.58 --> 84.14]  You know, I try out some new features.
[84.14 --> 85.28]  I try out a new framework.
[85.28 --> 87.82]  I'm just hacking around with something on the weekends.
[88.16 --> 89.00]  Everything looks good.
[89.10 --> 89.32]  Great.
[89.46 --> 89.98]  I ship it.
[90.08 --> 90.48]  I'm done.
[90.80 --> 94.58]  But as we talk to more customers, as we've grown as a company, as we've added new products,
[95.00 --> 99.86]  there's a lot more to the product portfolio of Vercel nowadays to help pass that experience.
[99.86 --> 104.06]  So when you're building larger, more complex products, and when you're working with larger
[104.06 --> 106.72]  teams, you want to have more features, more functionality.
[106.96 --> 111.42]  So tangibly, what that means is features like our Vercel Firewall product to help you
[111.42 --> 113.88]  be safe and to have that layer of security.
[113.88 --> 118.40]  Features like our logging and observability tools so that you can understand and observe
[118.40 --> 122.32]  your application and production, understand if there's errors, understand if things are
[122.32 --> 124.62]  running smoothly, and get alerted on those.
[124.62 --> 130.16]  And also then really an expansion of our integration suite as well, too, because you might already
[130.16 --> 135.46]  be using a tool like a data dog, or you might already be using a tool at the end of this
[135.46 --> 139.66]  software development lifecycle that you want to integrate with to continue to scale and
[139.66 --> 141.16]  secure and observe your application.
[141.32 --> 143.66]  And we try to fit into those as well, too.
[143.78 --> 149.22]  So we've kind of continued to bolster and improve the last mile of delivery.
[149.76 --> 150.76]  That sounds amazing.
[150.76 --> 153.30]  So who's using the Vercel platform like that?
[153.52 --> 154.48]  Can you share some names?
[155.00 --> 160.06]  Yeah, I'm thrilled that we have some amazing customers like Under Armour, Nintendo, Washington
[160.06 --> 166.30]  Post, Zapier, who use Vercel's running cloud to not only help scale their infrastructure,
[166.54 --> 170.92]  scale their business and their product, but then also enable their team of many developers
[170.92 --> 176.48]  to be able to iterate on their products really quickly and take their ideas and build the next
[176.48 --> 176.98]  great thing.
[177.34 --> 177.82]  Very cool.
[177.82 --> 183.66]  With zero configuration for over 35 frameworks, Vercel's running cloud makes it easy for any
[183.66 --> 184.76]  team to deploy their apps.
[185.12 --> 191.00]  Today, you can get started with a 14-day free trial of Vercel Pro or get a customized enterprise
[191.00 --> 192.20]  demo from their team.
[192.66 --> 196.20]  Visit Vercel.com slash changelogpod to get started.
[196.74 --> 201.16]  That's V-E-R-C-E-L dot com slash changelogpod.
[201.16 --> 226.86]  Hello, friends.
[226.86 --> 231.98]  We are here for another excellent JSRT podcast.
[232.42 --> 233.86]  We are glad to have you with us.
[234.22 --> 236.68]  And I'm glad to have with me my friend Amel.
[236.96 --> 237.68]  What's up, Amel?
[237.86 --> 238.66]  Hey, hey, Jared.
[239.12 --> 239.86]  How you doing?
[240.12 --> 240.82]  Doing great.
[240.90 --> 241.70]  It's Fri-yay.
[241.94 --> 242.84]  That's what the kids say.
[242.94 --> 243.62]  They say Fri-yay.
[244.00 --> 244.58]  No, they're not.
[244.58 --> 246.30]  I was going to make a joke.
[246.40 --> 248.84]  Then I was like, you know, have some mercy.
[249.04 --> 250.02]  It's Friday, right?
[250.24 --> 250.46]  Yeah.
[250.46 --> 250.64]  I'm sorry.
[250.72 --> 251.58]  You thought better of it.
[252.04 --> 252.76]  Yeah, there you go.
[253.46 --> 254.48]  That's what the kids call it.
[254.70 --> 255.24]  No, they're not.
[255.24 --> 256.90]  Also, Chris Hiller is here.
[256.98 --> 258.40]  The kids call him Bone Skull.
[258.66 --> 259.24]  What's up, Chris?
[259.68 --> 260.08]  Hi.
[260.64 --> 261.84]  I'm here on the podcast.
[262.06 --> 263.26]  We're happy to have you here as well.
[263.76 --> 264.16]  Thanks.
[264.60 --> 265.02]  You're welcome.
[265.34 --> 268.42]  We have a brand new voice here with us today.
[268.58 --> 274.82]  It's our new panelist, a one-time guest, and now a recurring panelist, our friend Jessica
[274.82 --> 275.34]  Sachs.
[275.50 --> 276.74]  Jess, welcome to the show.
[277.36 --> 277.76]  Hi.
[278.32 --> 280.14]  It's really exciting to be here.
[280.66 --> 281.12]  I'm nervous.
[281.38 --> 281.94]  Exciting to have you.
[281.94 --> 284.98]  I think we met probably two years ago or so.
[284.98 --> 286.08]  I'm not sure when you came on the pod.
[286.14 --> 286.82]  It was me and Cable.
[286.90 --> 288.22]  We talked FakerJS.
[288.38 --> 289.18]  We talked-
[289.80 --> 291.08]  Yeah, we talked open source.
[291.52 --> 291.76]  Yeah.
[292.00 --> 294.00]  That was a while ago.
[294.24 --> 297.22]  2023 felt like it didn't happen for me.
[297.38 --> 297.72]  Yeah.
[297.84 --> 298.10]  Yeah.
[298.28 --> 301.82]  You know, time is a vortex and things.
[302.36 --> 303.96]  But we're glad to have you here now with us.
[304.00 --> 309.00]  And then we connected again at that conference and got to hang out and chat.
[309.06 --> 309.80]  And so that was cool.
[310.34 --> 311.24]  And now you're here.
[311.24 --> 312.90]  So we'd like to get to know you.
[313.16 --> 314.84]  Let our audience get to know you a little bit.
[314.90 --> 316.40]  We're going to get into the news today.
[316.50 --> 318.76]  We're going to discuss some goings-on.
[318.86 --> 320.58]  It will be a segment show.
[320.88 --> 325.22]  But we thought we'd start off with getting to know Jess by playing a little game of 20
[325.22 --> 325.76]  questions.
[326.80 --> 328.28]  However, I only wrote 15.
[328.40 --> 330.26]  So we're going to call this 15 questions.
[331.26 --> 334.90]  And we're going to pass them around so it's not just me talking to Jess.
[334.90 --> 337.38]  I have 15 questions written here.
[337.48 --> 340.28]  I'm going to hand them to Amel and to Chris.
[340.82 --> 346.74]  And we'll just throw them at you, round robin style, and see what's going on.
[346.82 --> 350.74]  Now, Amel and Chris, you have to promise to read these verbatim as you receive them.
[350.82 --> 351.32]  No edits.
[351.66 --> 351.86]  Okay?
[352.50 --> 353.08]  No pressure.
[353.84 --> 355.26]  I'll ask the first question.
[355.46 --> 359.58]  And then I will DM the other ones in the background as Jess responds.
[359.58 --> 359.96]  All right.
[360.32 --> 365.18]  Number one, tell us about a time when you shipped a bug to production.
[366.02 --> 368.76]  I think it probably is a boring one.
[369.36 --> 374.80]  Well, there was one time where I broke Expedia, and I didn't work at Expedia.
[378.88 --> 379.86]  That's a twist.
[380.34 --> 380.70]  Yeah.
[381.36 --> 386.08]  So I noticed it because I did build Canary Deploys.
[386.08 --> 390.28]  I was working at an ad tech company, and we were a third-party script.
[390.66 --> 394.16]  And they put us in top, window.top.
[394.80 --> 401.40]  And so we had access to the entirety of Expedia and all user data on the search page.
[402.04 --> 405.98]  And so when you would type in, like, San Francisco to JFK, our ads would run.
[406.40 --> 409.90]  And so my code ran on millions and millions of page loads.
[409.90 --> 411.84]  And it gave us a lot of volume.
[412.12 --> 419.72]  And on IE whatever, I broke Expedia by, like, messing up some CSS.
[420.42 --> 421.96]  And I think also the back button.
[422.16 --> 423.86]  I think, like, they had just switched routers.
[424.20 --> 426.56]  And the back button, like, we messed it up.
[426.92 --> 427.64]  So that was bad.
[428.02 --> 429.92]  We reverted within five minutes.
[430.18 --> 430.62]  Well, not bad.
[431.52 --> 435.82]  I think breaking the back button is kind of a time-honored tradition amongst web devs, right?
[435.86 --> 436.68]  Like, we've all done it.
[437.18 --> 439.60]  Someone else's back button, though.
[440.14 --> 440.54]  True.
[441.06 --> 443.46]  That does make it a little like that ups the ante a little bit, doesn't it?
[443.56 --> 448.12]  I mean, I say shame on them for giving you so much privilege, you know?
[448.50 --> 449.50]  Millions of dollars.
[450.00 --> 451.62]  The tech team did not like us.
[451.76 --> 457.64]  It was constant, like, constant questions about, like, every kilobyte of gzipped file we would send.
[457.74 --> 460.14]  They'd be like, there was this one guy, Chad, or something.
[460.32 --> 461.10]  It's always a Chad.
[461.46 --> 462.88]  I don't think it's his real name.
[462.88 --> 472.06]  But he built, like, a monitoring script on our JavaScript bundle sizes, 2014, 15.
[472.64 --> 475.06]  And if it went up, like, we heard about it.
[475.06 --> 477.64]  I'd say good hygiene there, Expedia.
[477.88 --> 482.80]  So you get points for, like, being conscientious about your third-party scripts, but you definitely
[482.80 --> 487.16]  get way more points deducted for, like, giving them way too much privilege.
[487.44 --> 487.72]  Money.
[487.86 --> 488.26]  But yeah.
[488.60 --> 490.48]  Money will make people do crazy things.
[490.50 --> 491.06]  That's true.
[491.68 --> 492.60]  All right, ML, your turn.
[492.72 --> 493.50]  Got a question for Jess?
[493.68 --> 493.78]  Oh, yeah.
[493.94 --> 499.12]  So what's a web development myth you'd like to debunk once and for all?
[499.62 --> 501.10]  I-frames make your page really slow.
[501.64 --> 504.62]  They don't necessarily make your page really slow.
[505.16 --> 506.42]  It's what you put in the I-frames.
[506.68 --> 507.32]  Yeah, yeah.
[507.62 --> 508.24]  That's true.
[508.54 --> 511.64]  It's what you put in the I-frames that makes your page really slow.
[511.92 --> 513.18]  That's an interesting distinction.
[513.30 --> 513.78]  I like that.
[513.78 --> 516.52]  A universal one almost, right?
[516.98 --> 518.62]  It's like, it's a universal.
[518.98 --> 519.20]  Yeah.
[519.98 --> 522.64]  It just happens that the stuff you put in your I-frames is all ads.
[523.20 --> 524.84]  All right, Chris, here comes your question.
[525.04 --> 525.48]  There you go.
[525.48 --> 529.22]  Tell Nick Neesey why TypeScript sucks.
[530.26 --> 533.62]  TypeScript sucks for app developers because you have to work around the type system.
[534.28 --> 536.56]  And it's really great for library authors.
[537.12 --> 537.76]  Spit and truth.
[537.82 --> 538.36]  You hear that, Nick?
[538.98 --> 539.84]  All right, next question.
[539.94 --> 540.66]  Number four.
[540.76 --> 542.50]  You have to pick a front-end framework.
[542.84 --> 544.10]  You cannot pick Vue.
[544.80 --> 545.16]  Solid.
[545.82 --> 547.20]  Oh, you didn't even let me finish.
[547.30 --> 547.76]  That was fast.
[547.76 --> 548.54]  Okay, why?
[548.88 --> 552.48]  Because it's reactivity-first framework.
[553.98 --> 554.58]  That's it.
[554.84 --> 555.08]  Period.
[555.48 --> 556.04]  Finish.
[556.38 --> 556.64]  Okay.
[556.96 --> 557.70]  And I don't care.
[557.86 --> 560.60]  Okay, and I'm not married to meta frameworks.
[560.76 --> 566.58]  If I had to pick a meta framework, I don't know what I'd do that wasn't Nuxt because Nuxt
[566.58 --> 568.24]  is de facto the best right now.
[568.60 --> 570.04]  I want to double-click into that.
[570.30 --> 573.48]  Like, why is Nuxt de facto the best meta framework?
[573.76 --> 579.70]  Bro, if I showed you the DX right now, you would be floored.
[579.70 --> 585.30]  I just showed my manager for like 45 minutes all of the dev tools.
[586.02 --> 587.58]  It is, you can see API routes.
[587.68 --> 591.08]  They built freaking Postman into the dev tools.
[591.30 --> 592.92]  It has end-to-end type safety.
[593.18 --> 596.84]  All of the SSR edge stuff on Vercel, same stuff.
[596.84 --> 598.76]  It's insane.
[599.36 --> 602.86]  Is that like on the nightly builds or is that like shit?
[603.22 --> 603.68]  Like production?
[604.16 --> 604.48]  Prod.
[604.68 --> 605.42]  NPM install.
[605.74 --> 606.06]  Okay.
[606.26 --> 607.76]  PNPM install or bun install.
[608.00 --> 608.26]  Okay.
[608.98 --> 609.82]  All right, Emel, your turn.
[610.62 --> 611.98]  Oh, really, Jared?
[611.98 --> 612.06]  Jared.
[612.94 --> 613.98]  Just read the question.
[614.08 --> 617.46]  Who is your favorite JS Party panelist and why is it Jared?
[621.18 --> 623.90]  Because of how red his face cuts.
[625.08 --> 625.88]  When I'm happy.
[625.92 --> 626.36]  Oh my God.
[626.44 --> 626.60]  Yeah.
[626.80 --> 627.40]  Good answer.
[627.66 --> 628.42]  We share that.
[628.66 --> 630.48]  I get progressively redder.
[631.20 --> 632.68]  Do you have a sunburn right now?
[633.06 --> 633.30]  Me?
[633.84 --> 634.10]  Yeah.
[634.56 --> 636.36]  No, I'm just naturally flush.
[636.50 --> 638.70]  It's my youthful exuberance.
[639.10 --> 639.24]  Yeah.
[639.24 --> 643.28]  Like later on in the episode, you'll start to see my like, my like collarbone.
[643.44 --> 645.68]  I'll start to get like red here and here.
[645.98 --> 646.18]  Yeah.
[646.54 --> 647.94]  That's a sign of good health, I think.
[648.40 --> 649.50]  All right, Chris, your question.
[650.30 --> 655.16]  You've been debugging for hours and you cannot figure out the problem.
[655.48 --> 656.70]  What's your next move?
[657.06 --> 657.68]  Phone a friend.
[658.58 --> 659.66]  That's not even hours.
[659.88 --> 660.96]  I just, I just ask.
[661.28 --> 661.86]  Who do you ask?
[662.46 --> 663.98]  Whoever's problem it is.
[664.22 --> 665.04]  What if it's your problem?
[666.54 --> 667.38]  Ask a friend.
[667.72 --> 669.08]  Like someone else on my team.
[669.60 --> 675.46]  Like, yeah, if it's, if it's my problem by myself, I'll just go to the docs eventually.
[675.66 --> 680.74]  But generally I'm going to ask a person because I'm doing something really stupid or easy, incorrectly.
[681.40 --> 681.84]  Yeah.
[681.96 --> 682.62]  That's a good answer.
[682.82 --> 683.66]  How long would you wait?
[683.80 --> 684.94]  You wouldn't wait an hour, obviously.
[685.46 --> 685.86]  Depends.
[686.28 --> 688.18]  30, 30 minutes, maybe.
[688.60 --> 689.42]  I just have lots of friends.
[689.44 --> 690.34]  30 to 45 minutes.
[691.28 --> 691.72]  Yeah.
[692.48 --> 692.92]  Yeah.
[692.92 --> 692.98]  Yeah.
[693.12 --> 697.84]  The good thing, the good thing about the Vue community is that they're very global.
[697.84 --> 700.44]  And then I also have friends on the West Coast.
[700.98 --> 704.84]  So open source has given me a lot of time zones to make friends in.
[705.42 --> 705.52]  Yeah.
[705.52 --> 705.84]  That's nice.
[705.90 --> 711.46]  I also just want to say, I mean, I think this is like an age old thing, but like, you know,
[712.30 --> 714.38]  women are much better at asking for help than men.
[715.54 --> 715.90]  Period.
[716.44 --> 717.24]  How rude.
[717.24 --> 717.44]  I'm sorry.
[717.44 --> 718.82]  How true, but how rude.
[719.32 --> 724.82]  You guys will just sit and wallow in your indirection for hours, you know, whether it's
[724.82 --> 727.34]  getting lost or, you know, whatever it is.
[727.40 --> 729.10]  Like this applies to so many things, you know.
[729.10 --> 733.00]  The reason I do it is because I actually learn when I talk to somebody.
[733.26 --> 735.78]  I can't learn unless it's conversational.
[736.20 --> 741.16]  Usually chat GPT has been really helpful in this because I just tell it to be really profane
[741.16 --> 743.10]  and like short and concise.
[743.10 --> 750.04]  And then it treats me like, I don't know, like Ken Wheeler might treat me just like straight
[750.04 --> 751.00]  up bro talk.
[751.14 --> 752.26]  And I'm like, yeah.
[752.52 --> 753.90]  I was like, why do I even care?
[754.00 --> 755.66]  And it'll be like, here's why.
[755.66 --> 760.98]  So it may replace by emulation, you know, a few of your friends over time.
[761.32 --> 762.26]  I think that's true.
[762.94 --> 767.16]  All of the things you like with none of the problems, you know, that's the problem with
[767.16 --> 772.16]  people is we have baggage that we bring to relationships, but the GPTs, they're just
[772.16 --> 772.76]  there for you.
[772.98 --> 773.38]  Yeah, exactly.
[773.80 --> 775.04]  I don't have to care about chat GPT.
[775.10 --> 776.72]  They'll give, give, give, and they'll never take.
[777.62 --> 777.92]  All right.
[778.02 --> 778.92]  Question number seven.
[779.00 --> 779.52]  Is it my turn?
[780.00 --> 780.74]  I think it is.
[781.22 --> 784.42]  If you weren't working in tech, what would you be doing?
[784.42 --> 789.52]  I wanted to be an anesthesiologist when I grew up, like specifically an anesthesiologist.
[790.16 --> 790.48]  Okay.
[790.72 --> 794.02]  It was a weird thing for an eight year old to say, but yeah, I was like, yes.
[794.38 --> 796.94]  I don't think I even knew what anesthesia was when I was eight.
[797.14 --> 798.12]  So it's impressive.
[798.46 --> 799.74]  I don't think I did either.
[799.96 --> 804.32]  It was just the number one paying job in the little software program that they had to load.
[804.78 --> 804.86]  Yeah.
[805.64 --> 806.00]  Yeah.
[806.00 --> 809.10]  I definitely remember doing that when we were in school and they like had all these different
[809.10 --> 811.86]  career paths and you just basically sorted by most money.
[811.96 --> 813.50]  And you're like, I guess I'll just do that one.
[813.50 --> 816.26]  My mom was really upset when I told her I was going into software.
[816.94 --> 818.60]  She was like, that, that doesn't make money.
[819.40 --> 819.74]  Wow.
[820.08 --> 820.76]  She's no profit.
[821.66 --> 823.42]  No, she, she understands now.
[823.48 --> 825.48]  She's like, oh, it made money.
[825.72 --> 826.20]  All right.
[826.22 --> 826.64]  Amelie, your turn.
[827.14 --> 827.56]  All right.
[827.72 --> 829.74]  Where is your favorite place to code?
[829.80 --> 831.92]  That's not your room or office.
[832.64 --> 835.28]  I code from the couch or yeah.
[835.48 --> 838.62]  I code from the couch or, um, is there anywhere else?
[839.02 --> 839.24]  Yeah.
[839.34 --> 839.72]  Room.
[840.24 --> 840.64]  We work.
[840.64 --> 842.64]  I would consider we work, not my office.
[842.64 --> 844.60]  Cause I don't go there at office hours.
[845.02 --> 848.20]  Like I go there at like 12 AM after I go to a bar.
[848.70 --> 849.28]  Oh yeah.
[849.34 --> 849.88]  12 AM.
[849.98 --> 850.96]  We work, you know, it's so funny.
[851.02 --> 855.10]  I think I used to do something very similar, uh, in the sense that like some of the best
[855.10 --> 860.42]  views in the city were at some of the coworking spaces that I had access to like a very,
[860.42 --> 861.36]  very long time ago.
[861.36 --> 865.10]  Um, and yeah, we just like get food.
[865.24 --> 869.48]  We'd get takeout and like eat and like watch TV and like a conference room or whatever.
[869.76 --> 872.12]  And like, it's just like, really, it's like a city apartment.
[872.12 --> 873.74]  That's not a city apartment, you know?
[874.30 --> 875.22]  So yeah.
[875.26 --> 875.44]  Yeah.
[875.50 --> 876.40]  I feel you on that.
[876.80 --> 877.30]  Like, yeah.
[877.42 --> 877.90]  Respect.
[878.52 --> 881.04]  It's also good utilization of the space.
[881.92 --> 883.02]  They're not using it.
[883.02 --> 886.06]  I mean, I read a really decent article actually about that.
[886.32 --> 887.76]  At some point we could talk about it.
[887.84 --> 891.62]  It should just convert like, uh, we works into senior centers in the evening or like,
[891.68 --> 892.36]  what do you mean?
[892.96 --> 894.80]  Cause the meetup acquisition didn't work.
[896.66 --> 897.46]  Communal housing.
[898.20 --> 903.22]  I mean, really like, honestly, like multi-purpose spaces, you know, that's a, that's a whole,
[903.32 --> 904.18]  that's a whole episode.
[904.18 --> 907.16]  That's a whole episode of a different podcast.
[907.34 --> 907.46]  Yeah.
[908.18 --> 908.58]  Different.
[908.68 --> 908.80]  Yeah.
[908.92 --> 910.34]  What are we going to do with all those malls?
[910.34 --> 911.24]  Like, that's what I want to know.
[911.30 --> 912.52]  All those like shopping malls.
[912.52 --> 914.56]  I think the answer to that is just rollerblading.
[914.82 --> 917.54]  You know, I feel like we could just, we could just all go rollerblading.
[917.78 --> 918.10]  How about housing?
[918.86 --> 921.30]  You know, but, uh, whatever.
[921.88 --> 922.56]  I guess.
[922.90 --> 923.30]  Okay.
[924.42 --> 925.96]  All right, Chris, you're up.
[926.60 --> 929.82]  What is the coolest place you've ever visited?
[930.40 --> 933.24]  I would say Park City, Utah.
[933.94 --> 935.58]  Park City, Utah was really cool.
[935.58 --> 936.18]  I've been to Park City.
[936.52 --> 936.74]  Yeah.
[936.88 --> 937.08]  Hmm?
[937.58 --> 938.08]  I've been there.
[938.08 --> 938.50]  It's beautiful.
[939.06 --> 939.34]  Yeah.
[939.52 --> 940.08]  It's gorgeous.
[940.34 --> 941.46]  What were you there for and what'd you do?
[941.46 --> 945.66]  I was there at a conference that was unrelated to front end whatsoever.
[945.66 --> 951.00]  I was at my, my friend's conference and I just got to hang out and see the city.
[951.16 --> 952.64]  It was like a work only thing.
[952.64 --> 954.78]  So it wasn't even that I could like watch them talk.
[954.78 --> 960.44]  And so I took a bike out by myself and just went around Park City in 2017.
[961.10 --> 964.52]  It was summer too, which is like makes it weird because it's a ski town.
[964.52 --> 965.64]  So it was dead empty.
[965.90 --> 967.38]  I was there also in summer.
[967.38 --> 973.28]  I went mountain biking and they convert the ski lifts into mountain bike lifts in the summer.
[973.72 --> 975.88]  And it was just a blast.
[976.02 --> 979.08]  I saw a moose from like 15 feet away, but I was in a ski lift.
[979.20 --> 980.12]  And so I wasn't even afraid.
[980.38 --> 980.58]  Oh, wow.
[980.72 --> 980.90]  Oh.
[981.08 --> 981.56]  It was beautiful.
[981.90 --> 982.02]  Yeah.
[982.02 --> 984.54]  He just walked underneath us and I was like, that's a moose.
[984.54 --> 986.22]  What an amazing way to see a moose.
[986.38 --> 986.74]  That's like.
[986.74 --> 986.94]  Yeah.
[987.00 --> 989.42]  It was the best because you're not afraid, but you're super close.
[989.66 --> 989.92]  Yeah.
[989.92 --> 990.12]  Yeah.
[990.34 --> 993.40]  Of getting like run over or whatever, you know.
[993.68 --> 996.88]  That's the day I learned that a moose is way bigger than you think a moose is.
[997.16 --> 997.28]  Yeah.
[997.30 --> 1001.34]  They say that like, if you're like in a sedan, you know, like, you know, you're seeing a
[1001.34 --> 1003.58]  moose when it looks like there's trees on the road.
[1003.98 --> 1005.20]  I was like, what?
[1005.36 --> 1008.42]  I mean, they are absolutely massive beasts.
[1008.66 --> 1009.58]  They are so big.
[1009.98 --> 1012.26]  You know what else is really big that I didn't know?
[1012.40 --> 1012.78]  What's that?
[1013.32 --> 1013.72]  Camels.
[1014.08 --> 1014.44]  Camels?
[1014.60 --> 1014.72]  They're huge.
[1014.82 --> 1015.54]  They're so tall.
[1015.54 --> 1017.08]  They're way bigger than horses.
[1017.78 --> 1018.12]  Wow.
[1018.38 --> 1020.34]  I didn't know that until I saw a camel.
[1020.44 --> 1022.42]  I'm not sure if I've seen a camel in real life before.
[1022.84 --> 1024.90]  I've seen a camel next to a person.
[1025.42 --> 1031.10]  Like, and I also like, I really like the word dromedary, which is like the formal word
[1031.10 --> 1033.42]  for camel and camel type animals.
[1033.60 --> 1033.78]  Yeah.
[1034.26 --> 1034.50]  Yeah.
[1034.50 --> 1037.92]  My parents are from, well, I mean, they left when they were teenagers, but they're from
[1037.92 --> 1042.30]  the country that like, I think is the number one exporter of camel meat and camel milk
[1042.30 --> 1043.42]  and camel everything.
[1043.90 --> 1044.30]  Yeah.
[1044.30 --> 1047.18]  So I wish I could say I've never seen a camel.
[1047.18 --> 1047.92]  They kill the dromedaries?
[1049.68 --> 1051.28]  They kill the dromedaries.
[1051.70 --> 1052.00]  Oh my God.
[1052.00 --> 1053.40]  So you've seen, you've seen part of a camel.
[1053.48 --> 1053.64]  Yeah.
[1053.72 --> 1053.86]  Yeah.
[1053.86 --> 1054.06]  Yeah.
[1054.10 --> 1054.44]  Definitely.
[1054.68 --> 1055.14]  I've seen a camel.
[1055.88 --> 1059.94]  One more thing that's big before we're just listing things that are big.
[1060.28 --> 1061.24]  Let's keep going.
[1062.34 --> 1062.74]  Wolves.
[1063.20 --> 1066.60]  Wolves are not just like a dog, but a little bit bigger.
[1067.00 --> 1068.78]  Wolves are like twice the size of a dog.
[1068.78 --> 1071.74]  I would not want to see a wolf up close.
[1071.74 --> 1075.60]  Game of Thrones, I think helped me understand how big wolves can get.
[1075.80 --> 1076.64]  The size of wolves.
[1077.06 --> 1077.86]  Dire wolf.
[1078.40 --> 1079.22]  And turkeys.
[1079.76 --> 1080.50]  Huge turkeys.
[1080.66 --> 1081.34]  Turkeys are big.
[1081.36 --> 1085.72]  When I was in Cambridge, I got a lot of experience with turkeys.
[1086.20 --> 1086.44]  All right.
[1086.44 --> 1088.44]  Would you rather fight one wolf or 50 turkeys?
[1088.70 --> 1089.08]  I'm sorry.
[1089.14 --> 1089.76]  That's not a question.
[1089.92 --> 1090.70]  I just added that one.
[1091.16 --> 1091.68]  50 turkeys.
[1091.68 --> 1093.56]  And the answer is 50 turkeys, of course.
[1093.70 --> 1094.96]  Well, maybe one wolf.
[1095.52 --> 1096.00]  All right.
[1096.08 --> 1097.10]  Let's go to Amel.
[1097.24 --> 1098.04]  I think you have a question.
[1098.14 --> 1098.28]  Ready?
[1098.44 --> 1099.26]  You wrote this one?
[1099.58 --> 1099.88]  Oh, yeah.
[1099.96 --> 1101.84]  I wrote it with my bare hands.
[1102.92 --> 1104.90]  How many programming languages do you know?
[1105.04 --> 1106.78]  HTML and CSS don't count.
[1106.96 --> 1107.68]  What the hell?
[1107.86 --> 1108.18]  No, I.
[1108.42 --> 1108.84]  Amel.
[1109.06 --> 1109.28]  Jared.
[1109.62 --> 1110.02]  That's fine.
[1110.22 --> 1111.04]  I didn't say that.
[1111.30 --> 1111.90]  Come on.
[1112.28 --> 1113.20]  Stop gatekeeping.
[1113.66 --> 1114.14]  Wow.
[1114.26 --> 1116.64]  I answered this yesterday for friends.
[1117.06 --> 1117.28]  Okay.
[1117.32 --> 1118.96]  So what do you count?
[1118.96 --> 1125.64]  Do you count languages that you would, without needing to read any documentation, do a network
[1125.64 --> 1126.38]  request in?
[1127.02 --> 1127.66]  What do you count?
[1128.06 --> 1129.00]  Similar to languages.
[1129.80 --> 1132.04]  Or have I ever programmed in professionally?
[1132.36 --> 1133.12]  That's different.
[1133.38 --> 1134.76]  I don't think it has to be professionally.
[1135.42 --> 1135.60]  Oh.
[1136.04 --> 1144.82]  If I went to Mexico, I know enough Spanish to find my way to the supermarket and acquire
[1144.82 --> 1145.52]  an orange.
[1145.52 --> 1146.12]  You know?
[1146.34 --> 1150.68]  I thought you were going to say, like, you know, be overcharged for goods and services,
[1150.92 --> 1151.12]  you know?
[1151.14 --> 1151.38]  Right.
[1153.24 --> 1156.14]  To be overcharged for goods and services?
[1156.14 --> 1158.34]  To pay more than the local taxi rate?
[1158.34 --> 1159.74]  When they're whispering about me.
[1160.14 --> 1160.40]  Yes.
[1160.70 --> 1161.00]  Yes.
[1161.16 --> 1162.82]  People will be like, tourist.
[1163.76 --> 1164.40]  You know?
[1164.84 --> 1165.14]  Yeah.
[1165.22 --> 1165.70]  Got it.
[1165.92 --> 1166.12]  Yeah.
[1166.24 --> 1167.20]  Like, I can ask you.
[1167.32 --> 1168.54]  I can know where the bathroom is.
[1168.58 --> 1169.48]  I can get to the library.
[1169.76 --> 1170.04]  Okay?
[1170.08 --> 1171.06]  But I don't know Spanish.
[1171.36 --> 1171.50]  So.
[1171.60 --> 1171.82]  Yeah.
[1172.48 --> 1173.32]  That doesn't help.
[1173.40 --> 1174.10]  Does that help at all?
[1174.10 --> 1174.66]  Yeah.
[1174.82 --> 1177.22]  Donde esta la biblioteca?
[1177.98 --> 1178.18]  Yeah.
[1178.30 --> 1179.66]  It's probably la biblioteca.
[1179.68 --> 1181.28]  La biblioteca, because it's feminine.
[1181.30 --> 1181.56]  Yeah, because it's feminine.
[1181.84 --> 1181.98]  Yeah.
[1182.42 --> 1183.78]  Why are books feminine?
[1183.92 --> 1184.38]  I don't know.
[1184.66 --> 1186.90]  Because women read better as well?
[1188.52 --> 1189.04]  Yeah.
[1189.16 --> 1189.52]  Languages.
[1189.74 --> 1190.32]  In order.
[1190.64 --> 1192.44]  It would be Objective-C was my first language.
[1192.68 --> 1192.90]  Okay.
[1192.90 --> 1195.68]  And then I went Ruby, Python.
[1196.40 --> 1200.44]  And then we went from Python to Java.
[1201.32 --> 1201.72]  JavaScript.
[1202.80 --> 1204.22]  I count TypeScript as separate.
[1204.40 --> 1204.90]  But oh, no, no, no.
[1204.90 --> 1205.82]  That was much later.
[1206.40 --> 1206.84]  Kotlin.
[1207.66 --> 1209.50]  And let's see.
[1210.00 --> 1210.80]  Then TypeScript.
[1211.70 --> 1212.56]  HTML, CSS.
[1212.82 --> 1213.14]  I don't know.
[1213.70 --> 1214.78]  So I think we're at seven.
[1214.80 --> 1215.78]  Well, ML doesn't count those.
[1215.98 --> 1216.46]  It's fine.
[1216.56 --> 1216.88]  It's fine.
[1216.88 --> 1219.96]  So seven, not counting, HTML, CSS.
[1220.84 --> 1223.72]  No, also Lisp, Bash, nine.
[1224.16 --> 1225.02]  That's pretty good.
[1225.08 --> 1225.78]  That's a pretty solid list.
[1226.06 --> 1233.46]  I'm amazed you stuck with it after Objective-C, because that's probably the most painful programming
[1233.46 --> 1238.84]  language I've ever even attempted to read or learn or use.
[1239.04 --> 1239.94]  I learned Objective-C.
[1240.00 --> 1241.08]  I kind of liked it over time.
[1241.08 --> 1241.28]  Really?
[1241.60 --> 1242.70]  Oh, my God.
[1242.76 --> 1243.52]  I like it a lot.
[1244.00 --> 1244.24]  Oh, wait.
[1244.28 --> 1245.30]  Did I mention Swift?
[1246.02 --> 1246.38]  No.
[1246.38 --> 1246.86]  10.
[1247.02 --> 1247.46]  10.
[1247.62 --> 1248.80]  And I was starting on Rust.
[1249.06 --> 1250.22]  Somebody mentioned in chat.
[1250.38 --> 1255.52]  I was starting on Rust about two weeks ago for the first time, but I didn't get far into
[1255.52 --> 1255.64]  it.
[1255.82 --> 1262.54]  The reason that I know so many languages is because I resented being called a front-end
[1262.54 --> 1269.98]  engineer for a very long time, and I refused to put on my resume JavaScript at the top.
[1269.98 --> 1276.96]  So I just listed, I got proficient and listed all of the languages, not all of them, because
[1276.96 --> 1282.46]  it's weird, but I listed the languages I was most proficient in, with Python being the number
[1282.46 --> 1282.70]  one.
[1282.92 --> 1284.50]  Python was the first language I got good in.
[1285.10 --> 1285.58]  Like, good, good.
[1285.58 --> 1287.34]  The Zen of Python is real.
[1287.42 --> 1287.64]  Cool.
[1287.84 --> 1288.48]  That's a lot of fun.
[1288.60 --> 1291.62]  It's definitely my favorite programming language after JavaScript.
[1291.62 --> 1295.24]  I wrote some Python a couple weeks ago, and I thoroughly enjoyed myself.
[1295.60 --> 1300.92]  I had written it probably like 10 years prior for about six months full-time and really got
[1300.92 --> 1303.16]  to know it, and then I hadn't used it for a very long time.
[1303.70 --> 1308.80]  And I was writing some just because it had to do some AI thing, and I got pulled in,
[1308.80 --> 1311.30]  you know, and I was like, you know what?
[1311.98 --> 1313.06]  I like this language.
[1313.60 --> 1314.42]  List comprehensions.
[1314.66 --> 1319.08]  List comprehensions are still my favorite programming language feature of all time.
[1319.24 --> 1319.78]  That's a good one.
[1319.84 --> 1322.48]  Explain that feature to the plebs out there.
[1323.16 --> 1323.76]  Oh my gosh.
[1324.12 --> 1330.88]  List comprehensions allow you to, how would you say, allow you to do a map in a single line.
[1331.42 --> 1332.16]  Is that about right?
[1332.38 --> 1332.62]  Yeah.
[1332.92 --> 1333.72]  Pretty much, yeah.
[1333.72 --> 1334.20]  Yeah.
[1334.20 --> 1340.50]  It's very, like an elegant iteration over like iterable objects, you know?
[1341.36 --> 1341.56]  Right.
[1341.88 --> 1342.06]  Yeah.
[1342.26 --> 1343.86]  And get the result out of it.
[1344.50 --> 1344.72]  Yeah.
[1344.84 --> 1350.30]  So it's like if map was built into the language in syntax instead of as a function.
[1351.06 --> 1352.46]  That's how I would explain it.
[1352.96 --> 1357.76]  I haven't written Python in seven years, eight years, but it was the first.
[1358.40 --> 1359.12]  That's good.
[1359.66 --> 1360.40]  Well, let's move on.
[1360.52 --> 1361.54]  Number 11.
[1361.54 --> 1363.40]  This is more of a request than a question.
[1363.40 --> 1365.84]  Please read us your favorite line of code.
[1366.14 --> 1367.96]  You probably have it on your wall over there, don't you?
[1369.42 --> 1370.06]  Frame it.
[1370.34 --> 1371.58]  You don't frame your code?
[1372.04 --> 1373.82]  Chris has given us the side eye over there.
[1374.14 --> 1376.10]  I don't have a favorite line of code.
[1376.54 --> 1377.66]  Am I supposed to have that?
[1377.76 --> 1378.38]  Do you have that?
[1378.40 --> 1379.20]  Do you have a favorite movie?
[1379.38 --> 1380.16]  Do you have a favorite song?
[1380.54 --> 1381.40]  Do you have a favorite line of code?
[1381.56 --> 1381.68]  No.
[1382.26 --> 1382.48]  No.
[1383.12 --> 1383.38]  All right.
[1383.42 --> 1385.58]  Well, good thing those are Jessica's questions and not yours.
[1388.48 --> 1389.42]  Console.table.
[1390.50 --> 1391.82]  You forgot the parentheses.
[1391.82 --> 1394.58]  I mean, it's assumed that they're parentheses.
[1395.08 --> 1396.60]  Oh, I thought you were going to read it for us.
[1397.20 --> 1397.78]  Oh, okay.
[1397.88 --> 1398.42]  So you want me to?
[1398.42 --> 1404.36]  So what I wrote two days ago was type UT.
[1404.60 --> 1410.24]  So this is a library did not export a public type from their API response.
[1410.82 --> 1413.46]  I'm not going to name names, but it was upload thing.
[1414.02 --> 1414.72]  Sorry, Theo.
[1415.04 --> 1415.78]  He knows I wrote this.
[1415.88 --> 1419.52]  And they promptly fixed this within a day.
[1419.52 --> 1424.36]  They texted me back about it like two hours in, but I had written the code already.
[1424.36 --> 1438.38]  So type UT file is equal to parentheses, return type, angle bracket, type of UTAPI.prototype.list files, end angle bracket, extends promise like.
[1438.38 --> 1442.20]  This is because they didn't return the type from the API request.
[1442.70 --> 1454.78]  Promise like, open, angle bracket, infer you, close angle bracket, ternary, U, colon, never, end parentheses, square bracket, number, square bracket, semicolon.
[1455.62 --> 1456.20]  Does that help?
[1456.60 --> 1457.30]  Excellent job.
[1457.76 --> 1458.00]  All right.
[1458.44 --> 1459.88]  Did you like console table better?
[1460.36 --> 1465.06]  I love console table, but I also appreciate the literality of your response.
[1465.06 --> 1467.40]  Bone Skull, you would like her to read something as well, wouldn't you?
[1467.84 --> 1468.38]  What's your question?
[1469.22 --> 1471.82]  What's your current banking password?
[1472.58 --> 1474.78]  Hunter, Hunter 2.
[1475.18 --> 1475.60]  Oh, wow.
[1475.64 --> 1477.60]  That's really low quality password.
[1478.10 --> 1481.82]  It's for all the people who grew up playing RuneScape.
[1482.48 --> 1482.78]  Oh.
[1483.12 --> 1483.28]  Yeah.
[1484.08 --> 1484.78]  It's a meme.
[1485.94 --> 1487.32]  It's actually in docs now.
[1487.98 --> 1489.22]  It's in documentation now.
[1489.28 --> 1490.46]  They put it in the pickle docs.
[1490.68 --> 1491.12]  Really?
[1491.52 --> 1491.70]  Yeah.
[1492.08 --> 1492.70]  Yeah, they did.
[1492.70 --> 1493.82]  And I was so proud.
[1493.92 --> 1494.82]  I was like, I'm represented.
[1495.06 --> 1499.00]  My age group has started to ship and be in charge of stuff.
[1499.20 --> 1500.28]  My age group has started to ship stuff.
[1501.08 --> 1501.34]  Yeah.
[1501.52 --> 1504.90]  Yeah, now your age group is going to sign into your bank account and drain it.
[1505.50 --> 1505.70]  Yeah.
[1508.08 --> 1508.48]  Okay.
[1509.20 --> 1510.36]  We're getting to the end here.
[1511.10 --> 1512.36]  I don't want Amal to read this one.
[1512.42 --> 1512.88]  Hold on, Amal.
[1513.06 --> 1513.86]  I'm going to give this one to you.
[1513.88 --> 1513.90]  Oh, my God.
[1513.90 --> 1518.10]  Why do you keep giving me like the, you know, these are like, no, these are not good.
[1518.32 --> 1519.84]  They're by whose standards?
[1519.90 --> 1520.48]  Oh, these are great.
[1521.02 --> 1522.18]  Oh, my gosh.
[1523.14 --> 1523.50]  Okay.
[1523.50 --> 1523.58]  Okay.
[1524.22 --> 1525.42]  Just read that out loud, please.
[1525.66 --> 1525.94]  Okay.
[1526.02 --> 1526.56]  Fine, Jared.
[1527.56 --> 1535.82]  Thrown any objects into the air and caught them in a continuous cyclical pattern, ensuring
[1535.82 --> 1540.54]  that at least one object is airborne at all times lately.
[1540.88 --> 1541.18]  Juggling.
[1541.36 --> 1541.66]  Okay.
[1542.38 --> 1542.72]  Juggling.
[1543.14 --> 1543.46]  Sorry.
[1543.58 --> 1543.94]  That's okay.
[1544.02 --> 1544.22]  No.
[1544.36 --> 1546.96]  I'm just like trying to like read this oddly constructed.
[1546.96 --> 1548.26]  Amal, what are you talking about over there?
[1548.26 --> 1548.54]  Yeah.
[1548.54 --> 1550.72]  So, so essentially, have you been juggling lately?
[1551.32 --> 1552.90]  Yes, I've been juggling lately.
[1553.34 --> 1554.10]  Tell us about this.
[1554.24 --> 1555.66]  Are you like a circus nerd too?
[1555.78 --> 1559.60]  Because, you know, it's like definitely like there's this fun intersection of like tech
[1559.60 --> 1561.18]  nerds that are also circus nerds.
[1561.18 --> 1564.98]  And I find them to be utterly like the most delightful people.
[1565.34 --> 1565.52]  So.
[1565.52 --> 1566.04]  Yeah.
[1566.04 --> 1567.14]  The Venn diagram is good.
[1567.64 --> 1567.90]  Yeah.
[1568.30 --> 1569.54]  Circusy stuff.
[1569.76 --> 1571.98]  I did contortion.
[1572.54 --> 1577.34]  So I did rhythmic gymnastics growing up, which is really good if you're hypermobile.
[1577.48 --> 1580.14]  So I can still do over splits, even though I don't train them anymore.
[1580.14 --> 1583.04]  So my legs go like over 180 degrees.
[1583.50 --> 1584.26]  They just do.
[1584.82 --> 1587.62]  And then my back still, you know, feet touch head.
[1587.88 --> 1591.98]  But then I had a back injury, totally unrelated to contortion.
[1592.40 --> 1596.44]  And I couldn't do the exciting like dynamic circus arts anymore.
[1596.54 --> 1597.60]  I couldn't do trapeze.
[1597.68 --> 1599.94]  I have a trapeze and I couldn't do lira.
[1600.18 --> 1601.62]  So I was like, what can I do?
[1601.70 --> 1602.86]  That's weird and circusy.
[1603.24 --> 1607.62]  I was like, I can stand straight and throw balls and make small movements with my core.
[1608.12 --> 1609.24]  So that's why juggling.
[1610.14 --> 1610.74]  What's lira?
[1611.40 --> 1613.30]  Lira is the metal hoop thingy.
[1613.36 --> 1613.72]  Ah.
[1614.26 --> 1614.52]  Yeah.
[1614.64 --> 1619.24]  I hear like people that are really flexible can like over injure themselves sometimes like
[1619.24 --> 1621.18]  because they're like, oh, I can do this.
[1621.22 --> 1626.26]  And then like they're like tendons are like, oh, no, maybe you shouldn't do this too much
[1626.26 --> 1626.92]  or too long.
[1627.32 --> 1628.24]  You know, so.
[1628.46 --> 1629.92]  It was a kettlebell lift.
[1629.98 --> 1631.98]  It was a kettlebell lift in front of a personal trainer.
[1632.78 --> 1633.26]  Yeah.
[1633.76 --> 1635.10]  It was like super tragic.
[1635.60 --> 1636.96]  I was 24.
[1636.96 --> 1639.24]  It was December 2019.
[1639.86 --> 1642.60]  Well, I'm sorry to hear that, but I'm glad you've discovered juggling.
[1642.98 --> 1644.04]  That sounds really fun.
[1644.92 --> 1648.38]  And there's just so much math involved in juggling for me.
[1648.46 --> 1650.16]  That's just the part that I find fun.
[1650.72 --> 1652.90]  Like the math and physics of it all.
[1652.90 --> 1653.34]  Yeah.
[1653.36 --> 1659.12]  I want to build a syntax parser for there's a language called site script.
[1659.36 --> 1660.56]  Am I getting that right?
[1660.86 --> 1661.58]  Site script?
[1661.96 --> 1662.50]  Site swap.
[1662.92 --> 1663.38]  Site swap.
[1663.58 --> 1663.66]  I do not know.
[1663.86 --> 1664.42]  I do not know.
[1664.42 --> 1664.66]  Yeah.
[1664.98 --> 1666.70]  I always mess up the word for it.
[1666.80 --> 1672.92]  There's a language that like lets you describe how many balls are in the air at a given moment
[1672.92 --> 1675.76]  and at what times and what hands they're going to.
[1675.76 --> 1680.30]  So you can throw the same ball to the same hand or you could throw one ball to the other hand
[1680.30 --> 1681.72]  or you could throw a ball high.
[1682.54 --> 1688.76]  And there's actually a mathematical language with parentheses and brackets and stuff and
[1688.76 --> 1695.34]  repeats that allows you to describe the math of juggling and throwing things and catching
[1695.34 --> 1696.18]  them in different times.
[1696.70 --> 1699.00]  And I want to write a little syntax parser for it.
[1699.80 --> 1699.88]  Yeah.
[1699.92 --> 1700.40]  That'd be cool.
[1700.40 --> 1703.44]  I feel like that's like the nerdiest thing I've learned all year.
[1703.58 --> 1705.62]  So thank you for enlightening.
[1705.80 --> 1706.00]  Yeah.
[1706.10 --> 1706.60]  Thank you.
[1707.28 --> 1707.42]  Yeah.
[1707.42 --> 1709.50]  I just figure you just throw stuff up and catch it.
[1709.62 --> 1711.98]  You know, I didn't really think there'd be much more to it than that.
[1712.04 --> 1715.64]  Although it does get increasingly, I can juggle three just fine.
[1716.46 --> 1718.62]  Generally same size balls, tennis balls.
[1718.76 --> 1719.04]  Balls.
[1719.16 --> 1719.26]  Yeah.
[1719.26 --> 1722.04]  But yeah, I've never really gone beyond that.
[1722.10 --> 1722.84]  I've tried four.
[1723.36 --> 1725.08]  It gets way more hard with four.
[1725.26 --> 1725.42]  Yeah.
[1725.42 --> 1726.08]  I've never done.
[1726.32 --> 1727.22]  But no one ever taught me how.
[1727.28 --> 1728.42]  So I just was guessing, you know?
[1728.66 --> 1728.90]  Yeah.
[1729.10 --> 1729.32]  Yeah.
[1729.32 --> 1729.52]  Yeah.
[1729.52 --> 1729.64]  Yeah.
[1729.64 --> 1732.14]  I learned from the MIT juggling club.
[1732.48 --> 1732.88]  Yeah.
[1733.14 --> 1733.98]  That probably would help.
[1734.44 --> 1738.38]  And you're doing, are you doing, I saw, was it on online?
[1738.48 --> 1739.12]  I think you get a picture.
[1739.40 --> 1741.68]  You're doing bowling pins as well?
[1742.22 --> 1743.84]  That's the first thing that they hate.
[1744.18 --> 1746.32]  The jugglers, they're like, they're not pins.
[1746.64 --> 1747.40]  They're clubs.
[1747.94 --> 1748.24]  Yeah.
[1748.24 --> 1748.46]  Yeah.
[1748.46 --> 1750.84]  That's the first thing that you'll get corrected on.
[1750.90 --> 1752.52]  If you ever go to a juggling meetup.
[1752.84 --> 1753.86]  Not too worried about it.
[1755.76 --> 1758.70]  Probably won't go to a juggling meetup, especially now that I know.
[1758.70 --> 1759.76]  Oh, they're going to ridicule me.
[1759.94 --> 1761.12]  No, they're the best.
[1761.20 --> 1762.28]  You find your people there.
[1762.40 --> 1767.86]  Like, if you're looking for nerds, nerds of all ages, juggling club, any city.
[1768.16 --> 1771.80]  So they're not called bowling pins because I've bowled a lot in my life.
[1771.80 --> 1773.64]  And I feel like they're always referred to as pins.
[1774.04 --> 1774.26]  Yeah.
[1774.34 --> 1776.66]  In juggling, they're referred to as clubs.
[1776.66 --> 1778.30]  Oh, just because you're juggling them.
[1778.64 --> 1778.92]  Okay.
[1779.38 --> 1779.76]  Yeah.
[1779.84 --> 1785.30]  I lived in the community that I think Jess also lived in for a while in the Cambridge
[1785.30 --> 1785.74]  area.
[1786.34 --> 1787.76]  Camberville, you know, area.
[1788.84 --> 1794.80]  And yeah, it's actually, you know, my husband and I, when we were first, we never really dated.
[1794.90 --> 1795.70]  We're just in a relationship.
[1795.70 --> 1799.52]  But like, that's like where we had our like little, you know, our like all of our, our
[1799.52 --> 1801.08]  first everythings were in that area.
[1801.62 --> 1806.72]  But yeah, like there's just so many circus nerds that are like concentrated there.
[1806.92 --> 1807.84]  Have you noticed that?
[1808.40 --> 1808.64]  Yeah.
[1809.32 --> 1809.72]  Yeah.
[1809.72 --> 1810.66]  It's quite serious.
[1810.66 --> 1813.12]  It's like, well, they have a, they have a circus school.
[1813.24 --> 1813.72]  Oh, yeah.
[1814.16 --> 1819.30]  So they, and they have a certain, a circus school in the middle of Cambridge and Somerville called
[1819.30 --> 1820.30]  Ash Circus Arts.
[1820.56 --> 1821.82]  And it's huge.
[1821.86 --> 1825.12]  It's right next to a rock climbing gym and a maker space.
[1825.12 --> 1826.56]  Like it's, it's nerd heaven.
[1826.58 --> 1826.78]  Yeah.
[1826.82 --> 1827.70]  Artisan asylum.
[1827.84 --> 1829.76]  And like, yeah, it's, it, there's just a lot.
[1829.84 --> 1834.04]  There's just, it just, it's just a, it's a nexus for nerds, you know, Cambridge.
[1834.16 --> 1834.88]  And yeah.
[1834.88 --> 1838.76]  I mean, also like the red line, which is like the train that serves that community, the subway.
[1838.76 --> 1843.68]  It's like the, it's the train that's ridden by the most Nobel laureates in the world.
[1843.76 --> 1849.32]  Like the most like intelligent people by far, like in terms of degrees, but also just like
[1849.32 --> 1852.34]  international awards, like the Nobel laureate prize.
[1852.94 --> 1854.30]  You would think that it ran on time.
[1854.50 --> 1854.62]  Yeah.
[1854.64 --> 1855.48]  You would think, right.
[1855.60 --> 1858.70]  No, no, that's, uh, nope.
[1858.92 --> 1863.56]  Everyone, everyone gets to have a crappy commute into wherever they're going.
[1863.62 --> 1865.16]  Cause we're still in America.
[1865.16 --> 1870.94]  So, but anyways, different show, different podcast, different show altogether.
[1871.62 --> 1872.22]  All right.
[1872.22 --> 1876.44]  Here's our 15th and final question of this game of 20 questions.
[1876.86 --> 1878.16]  Finish this sentence.
[1878.32 --> 1880.62]  Jazz party would be even more amazing.
[1880.86 --> 1881.38]  If.
[1883.68 --> 1884.52]  I don't know.
[1884.88 --> 1885.96]  If that was a question.
[1886.56 --> 1887.54]  That wasn't a question.
[1887.54 --> 1888.10]  If.
[1889.78 --> 1890.14]  There.
[1890.30 --> 1890.90]  Now's the question.
[1891.00 --> 1891.36]  If.
[1894.54 --> 1894.94]  Okay.
[1895.14 --> 1897.48]  Let me reword that into a form of a question, Alex Trebek.
[1898.02 --> 1900.54]  How would Jazz party be even more amazing?
[1901.02 --> 1901.56]  Question mark.
[1902.62 --> 1906.08]  What is more games for $3,000?
[1906.68 --> 1907.08]  Correct.
[1907.68 --> 1908.42]  Excellent answer.
[1908.74 --> 1909.20]  Excellent job.
[1909.38 --> 1912.04]  You are officially part of the gang now.
[1912.04 --> 1916.06]  We've added a juggler to our list of nerds.
[1916.30 --> 1916.80]  Nerds.
[1916.86 --> 1917.56]  Nerds.
[1918.16 --> 1918.92]  Nerds.
[1918.92 --> 1944.48]  What's up friends?
[1944.48 --> 1946.58]  I'm here with Conrad Hoffmeyer from PowerSync.
[1946.58 --> 1953.84]  PowerSync is the sync layer that enables an offline first architecture to make your application real time and reactive.
[1954.52 --> 1959.30]  Conrad, why is offline first, local first a big deal right now for developers?
[1959.96 --> 1968.04]  We're really excited about local first as a movement and we think it's going to become the default architecture for a very large number of apps that are going to be built going forward.
[1968.14 --> 1971.86]  Just because it has really big benefits for both developers and end users.
[1971.86 --> 1983.16]  So taking a step back, just looking at what local first is, so it's an architecture where your app code works directly with the client side embedded database, which then automatically syncs with a backend database in the background.
[1983.16 --> 1987.98]  That's compared to cloud first apps where they mostly use a cloud data store via APIs.
[1988.32 --> 1995.64]  That has some really big benefits for developers and end users having a local database and syncing with the cloud in the background.
[1995.94 --> 2004.50]  The biggest benefit for end users is that everything in the app feels instant because the app is working with a local database and you don't have to do round trips to the cloud.
[2004.80 --> 2005.88]  There's no loading spinners.
[2006.14 --> 2007.42]  Everything can just load instantly.
[2007.42 --> 2012.28]  It also means that the apps can be always available for the most part, regardless of connection.
[2012.68 --> 2015.00]  So even if the user goes offline, the app is always available.
[2015.10 --> 2025.44]  So like you said, if you have a momentary lapse in connectivity, if you're driving through a tunnel or if you're on the subway or if you're out in a rural area, you don't have latency and the app can just keep on working and loading data out of the local database.
[2025.98 --> 2028.86]  So this moved to an offline first architecture.
[2029.36 --> 2030.82]  What are the biggest benefits for developers?
[2031.24 --> 2034.92]  The biggest benefit for developers is that it really simplifies state management.
[2034.92 --> 2037.38]  So state management is a headache for most apps.
[2037.86 --> 2041.18]  Developers typically work with some kind of state management library or framework.
[2041.70 --> 2043.92]  There's a lot of kind of finicky aspects to it.
[2044.30 --> 2050.46]  But with local first, the global state is simply stored in the local database, like a SQLite database.
[2050.80 --> 2052.98]  And that really simplifies the app code.
[2053.30 --> 2058.58]  It keeps your logic really simple and functional because your UI basically just reflects the content of the database.
[2058.82 --> 2060.34]  So it just makes everything a lot simpler.
[2060.74 --> 2062.64]  And then there's other benefits for developers too.
[2062.64 --> 2067.12]  Since you're working with data and logic locally, your backend becomes simpler.
[2067.50 --> 2069.28]  You have to do less API development on the backend.
[2069.44 --> 2070.92]  You can shift a lot of stuff to the frontend.
[2071.14 --> 2073.90]  A lot of working with the data, manipulating the data and logic.
[2074.28 --> 2080.98]  And they also reduce your backend compute load and compute cost and your dependency on the backend in general.
[2081.34 --> 2086.14]  So it kind of takes the backend API off the critical path for the user using the application.
[2086.70 --> 2087.08]  I like it.
[2087.10 --> 2087.52]  Very cool.
[2087.64 --> 2089.32]  What's your goal with PowerSync?
[2089.32 --> 2094.16]  Our goal with PowerSync is to be framework agnostic and eventually even backend database agnostic.
[2094.38 --> 2098.06]  But we already support Flutter, React Native, JavaScript for web apps.
[2098.40 --> 2100.54]  Kotlin SDK is right around the corner.
[2100.96 --> 2104.94]  Our web SDK plays well with any JavaScript framework, including Next.js.
[2105.42 --> 2107.36]  Yeah, the goal is to be framework agnostic.
[2107.36 --> 2110.90]  And we will also be becoming increasingly backend database agnostic.
[2111.08 --> 2115.50]  So supporting additional backend databases, not just Postgres, but also Microsoft SQL Server, MySQL, etc.
[2116.00 --> 2122.88]  But there's a ton of applications that can communicate with the cloud asynchronously, where you can primarily work with a local database.
[2123.22 --> 2128.30]  And therefore, we think for the majority of apps, local first will become sort of the default architecture.
[2128.30 --> 2134.14]  Okay, the next step is to head to powersync.com slash changelog to learn more.
[2134.52 --> 2138.42]  Take your application offline first for free with PowerSync using their free tier.
[2138.76 --> 2139.96]  No credit card required.
[2140.38 --> 2143.96]  Again, powersync.com slash changelog.
[2143.96 --> 2154.66]  All right, nerds, let's turn now to the news because Amel is, I was going to say hot and bothered, but that implies something else.
[2154.70 --> 2155.80]  You're just bothered by this.
[2155.86 --> 2156.68]  This is big.
[2156.88 --> 2160.46]  This is Apple versus the world here.
[2160.46 --> 2169.42]  The OWA, a group of people that you've been working hard, Amel, to get a show together with, the Open Web Advocates, I believe, or Advocacy,
[2169.42 --> 2173.34]  has been fighting hard to have the web be more and more open.
[2173.76 --> 2180.16]  These are often legal battles or lobbying or those kinds of things, political arenas, in order to have that.
[2180.78 --> 2184.46]  And they've had some wins of late, or maybe what they thought was a win,
[2184.46 --> 2191.92]  and now Apple maliciously complying in Europe with regards to the DMA, which I don't know what that stands for.
[2192.18 --> 2197.50]  But there's a deal going on with PWAs specifically in Europe,
[2197.50 --> 2205.16]  and there's a post on the openwebadvocacy.org called It's Official Apple Kills Web Apps in the EU.
[2205.92 --> 2209.44]  Amel, do you want to give us the rundown of exactly what's going on here, and then we can discuss?
[2209.88 --> 2210.48]  Yeah, sure.
[2210.56 --> 2215.78]  But I think before we do that, I just want to go back to Jess for a second and just say we're really excited to have you on the show.
[2216.32 --> 2217.02]  And yay.
[2217.42 --> 2220.26]  And yeah, I just want to say that.
[2220.26 --> 2224.92]  So I think with this Apple thing, we kind of have to set the stage a bit.
[2225.16 --> 2227.42]  And I hope we're going to have hopefully a whole show on this.
[2227.72 --> 2236.78]  We just keep pushing the date back because the people that the guests that would be on the show are literally talking to like nation states right now.
[2237.08 --> 2240.34]  So they're like, we are in a battle against Apple.
[2240.48 --> 2243.14]  And like, you know, there's just every day there's something different.
[2243.14 --> 2246.46]  And so we just, you know, they're just really busy preparing for that.
[2246.60 --> 2250.78]  So we hope to get their time as soon as they have it to give.
[2251.22 --> 2256.98]  But essentially, just really kind of we have to go back like way, way back, like to, you know, the birth of the iPhone.
[2256.98 --> 2275.40]  And think of like 2007, where iPhones actually like helped birth web apps, mobile web apps, like, you know, after the iPhone came out, like there was another announcement, I think later that year, where they were where Steve Jobs was like really excited about bringing full Safari to iPhones.
[2276.00 --> 2280.04]  And like, hey, app developers, you don't have to worry about like going through us for distribution.
[2280.04 --> 2286.94]  You know, you get this browser and you can get all the things and like, you know, he's like there is a historical speech.
[2287.04 --> 2292.20]  You can go look it up where Steve Jobs, like, you know, is just kind of all pro the open web.
[2292.36 --> 2293.92]  He called it a real sweet deal or something like that.
[2293.96 --> 2295.10]  We got a real sweet deal for you.
[2295.18 --> 2296.40]  And it was all web apps.
[2296.58 --> 2297.08]  That was a deal.
[2297.28 --> 2297.44]  Yeah.
[2297.58 --> 2305.84]  You know, and so, so, you know, fast forward to kind of, you know, just even to 2011, the app store becomes a thing.
[2305.84 --> 2322.80]  And, you know, Apple's getting their 30% cut and, you know, throughout all these investigations that have been happening lately, there's, you know, with the Epic Games debacle, there's emails that date back to 2011 where the chief marketing officer is like, do we think that our 70-30 split is going to last forever?
[2322.94 --> 2324.90]  We're making a billion dollars a year right now.
[2325.00 --> 2332.60]  Like, do you think we should maybe, you know, think about going down to 75-20 or 80-20, you know, and still be able to get that same billion over time?
[2332.60 --> 2337.54]  You know, like, they're just like, they're just, they're fully aware that it's a racket, right?
[2337.56 --> 2339.30]  It's like this little mafia fee, right?
[2339.38 --> 2347.28]  Where like in-app purchases and all this stuff, like they just, they get 15 to 30% of pretty much all financial transactions done on iOS.
[2347.68 --> 2350.76]  So what they've done is, you know, there's no browser choice, right?
[2350.82 --> 2358.00]  So there's no, like you can, sure, you can get Chrome and Firefox on iOS, but like, it's really just a thin wrapper for WebKit, right?
[2358.00 --> 2368.82]  So any limitations that the WebKit engine has, any bugs are kind of gone across all of these, like pretty much like mobile on iOS is just, is WebKit.
[2369.30 --> 2371.58]  And so there's no browser choice.
[2371.84 --> 2377.34]  They've kind of pushed off and kind of systemically underfunded WebKit for years.
[2377.34 --> 2388.38]  And, you know, all the kind of rich APIs that have come to the Web that have been added to multiple browsers, you know, have just, they've just either they're missing or lagging or they're bugging in Safari, you know?
[2388.40 --> 2392.66]  So there's all this kind of like intentionality to kind of hold the Web back on mobile.
[2392.66 --> 2396.92]  And then there's like the whole battle with the App Store, which is like its own separate thing.
[2397.40 --> 2407.48]  So anyway, so the Open Web Advocacy group has been doing a lot of advocacy to kind of fight for browser choice on mobile devices so that there's just fair competition across the board.
[2407.90 --> 2410.58]  My God, I'm like, I'm getting worked up just like explaining this.
[2411.06 --> 2415.64]  Anyway, so to kind of, long story short, like they made some really good strides in the EU.
[2415.64 --> 2426.26]  However, like Apple trying to comply with the EU means that like they basically just came up with a bunch of like really not so friendly, I don't even, not responses.
[2426.26 --> 2428.30]  Like there's like a bunch of new really bad laws.
[2428.82 --> 2429.70]  Changes, yes.
[2430.28 --> 2432.98]  You know, both with the App Store, they're like, oh, fine.
[2433.24 --> 2438.16]  Sure, people can create their own third party digital like marketplaces.
[2438.50 --> 2440.92]  But you have to basically still go through us.
[2440.98 --> 2442.04]  You still have to give us money.
[2442.04 --> 2446.78]  If your app gets downloaded over a million times, like we're going to come after you for more money.
[2447.40 --> 2450.00]  Like, you know, you basically everything has to still get notarized by them.
[2450.08 --> 2452.06]  Like it's basically just it's lip service.
[2452.12 --> 2453.48]  They're like, OK, sure, we'll comply.
[2453.60 --> 2457.36]  But like here's how we'll comply in the most like douchey way.
[2457.98 --> 2465.92]  And then on the flip side of that with browsers, you know, so they basically they've now been forced in the EU to allow for browser choice.
[2465.92 --> 2473.74]  So, you know, hopefully now we can we'll have other browser engines starting with iOS 17.4, which I think is set to release in March.
[2474.38 --> 2481.24]  However, the big kind of hoopla this week is that two weeks ago they released a beta of 17.4.
[2481.24 --> 2487.82]  And basically that broke existing PWA support where like you had an app on the home screen.
[2488.42 --> 2490.80]  You know, it would launch in like a full screen mode.
[2491.46 --> 2494.38]  Now that same app is basically just like a bookmark.
[2494.72 --> 2496.24]  It's like just a regular browser app.
[2497.04 --> 2500.60]  It's not like a doesn't take advantage of all the other rich APIs.
[2500.60 --> 2507.50]  And and they came out with an excuse today where they said that, oh, yeah, we that wasn't a bug.
[2507.58 --> 2514.60]  We intentionally broke that because of some they were hand wavy about security and a bunch of other things that really just don't make sense.
[2514.72 --> 2519.38]  You know, they were like, oh, you know, yeah, we we have to kind of protect users.
[2519.48 --> 2525.08]  And like if we lift that home screen thing in, users would be able to see each other's data and this and that.
[2525.14 --> 2527.78]  I'm like, oh, really, Apple, like you multibillion dollar company.
[2527.78 --> 2533.00]  You really couldn't find a way to design this in a secure like in a secure way like that.
[2533.16 --> 2545.38]  You're just you're basically just intentionally breaking the PWA experience because you now are forced to sort of not only support it, but now there's going to be other browsers that like are also going to enable this experience for users.
[2545.38 --> 2552.32]  And so, you know, so long story short, like they're just being really problematic and, you know, they've been silent.
[2552.56 --> 2557.72]  They haven't really like there's been journalists and all these people trying to get them to comment, to explain.
[2557.78 --> 2572.42]  And like all they came up with today is this like one little, you know, a few paragraphs on the developer.apple.com under a section titled, why don't users in the EU have access to home screen web apps?
[2573.04 --> 2579.68]  So, yeah, so basically Apple is really I mean, this is just like a fight for this is a fight where like it's about money, clearly.
[2579.86 --> 2580.14]  Right.
[2580.14 --> 2584.18]  Like they're not going to just give up their 30 percent without a fight.
[2584.40 --> 2586.76]  But I just didn't think it would be this dirty of a fight.
[2587.32 --> 2591.54]  Like and I just didn't think that they would consider like do they think people are stupid?
[2591.66 --> 2595.24]  Like I just I just really don't like that's I don't I don't get that.
[2595.36 --> 2595.78]  So, yeah.
[2595.86 --> 2597.74]  So anyways, I'm done talking now.
[2597.84 --> 2598.98]  But, you know, so.
[2598.98 --> 2603.94]  I mean, a lot of those points hit, especially with developers, I think.
[2604.38 --> 2604.52]  Right.
[2604.64 --> 2608.88]  So developers were very aware of what could be and what could exist.
[2609.00 --> 2611.00]  Like what what's that future meme?
[2611.10 --> 2614.92]  It's like the world if, you know, so and so happened.
[2615.04 --> 2617.82]  I think there was actually literally one about Apple and PWAs.
[2618.16 --> 2619.34]  Somebody posted that on Twitter.
[2619.46 --> 2621.64]  It's like the world of Apple actually allowed PWAs.
[2622.04 --> 2623.24]  We think about that.
[2623.62 --> 2624.88]  I don't think my mom does.
[2624.88 --> 2631.48]  And my mom doesn't know that, you know, Apple's taking a 30 percent cut of all the downloads when she plays Solitaire.
[2631.96 --> 2635.48]  And so the capitalism just kind of like flies under the radar.
[2636.42 --> 2642.88]  And they're going to do what's in their best interest, like money first over a lot of stuff.
[2643.38 --> 2645.04]  And that's kind of I don't know.
[2645.38 --> 2651.32]  I think that's the way of the world, which is toxic to people who are paying attention like us.
[2651.32 --> 2656.78]  We could create something better if we were in a position of an Apple.
[2657.42 --> 2657.58]  Right.
[2657.78 --> 2659.48]  We could have chosen differently.
[2659.72 --> 2661.28]  And so that bothers us a lot.
[2661.48 --> 2664.98]  That's that's what gets us like bothered is we know.
[2665.72 --> 2666.28]  100 percent.
[2666.80 --> 2670.22]  And there's engineers inside of Apple and there's swirling rumors.
[2670.34 --> 2676.82]  These are just rumors that there's a divide in the company because there's people on both sides of this particular decision making.
[2676.82 --> 2684.30]  And you have those who get it and would love to see the open web available on their platform.
[2684.56 --> 2688.58]  They're the WebKit engineers and a lot of the people who are down there doing the things.
[2688.68 --> 2696.06]  And then there's, you know, the pointy herd bosses, so to speak, who are on the other side, you know, adding up the money.
[2696.22 --> 2697.54]  Trying to protect shareholder values.
[2697.60 --> 2701.86]  And I'm sure it's not that cut and dry, but there is dissent I've heard inside the company.
[2702.06 --> 2704.14]  And that's a good thing, I guess.
[2704.50 --> 2705.80]  Chris, what do you think about all this?
[2705.80 --> 2708.36]  Yeah, I mean, I'm with Jess.
[2708.46 --> 2712.46]  I mean, nobody except developers knows or cares about this stuff, honestly.
[2712.72 --> 2716.12]  And it's it's just one of those things.
[2716.24 --> 2716.94]  It's too bad.
[2717.06 --> 2718.52]  But Apple's counting on that.
[2718.70 --> 2728.84]  And so, you know, they OWA has a steep hill to climb, I think, to get the attention of, you know, lawmakers and whatnot.
[2729.12 --> 2730.90]  The regulators are paying attention, though.
[2730.96 --> 2733.98]  I mean, like what they've been able to bring to the table so far.
[2733.98 --> 2735.20]  So this what is it?
[2735.60 --> 2735.96]  DMA?
[2736.18 --> 2736.76]  The DMA.
[2737.16 --> 2737.52]  DMA.
[2737.64 --> 2737.74]  Yeah.
[2737.78 --> 2739.18]  So Digital Markets Act.
[2739.28 --> 2739.46]  Right.
[2739.52 --> 2741.98]  So that's that's kind of what's been put forth.
[2742.12 --> 2744.16]  That's made Apple have to kind of comply.
[2744.64 --> 2745.08]  Right.
[2745.14 --> 2746.20]  Like they are listening.
[2746.30 --> 2747.22]  People are paying attention.
[2747.36 --> 2749.04]  Like I agree with both of you.
[2749.04 --> 2753.28]  It's it's really a shame that like this isn't something everyone knows about.
[2753.44 --> 2754.94]  In theory, they shouldn't have to.
[2755.50 --> 2755.74]  Right.
[2756.16 --> 2759.10]  Like this is so I mean, it's so esoteric.
[2759.34 --> 2760.02]  But sure.
[2760.10 --> 2760.66]  The EU.
[2761.04 --> 2764.76]  Can you imagine that like sort of thing happening in the states?
[2764.80 --> 2765.66]  It's hard to imagine.
[2765.66 --> 2771.78]  It's hard to imagine something like that would get in front of get through the House and get
[2771.78 --> 2772.34]  through the Senate.
[2772.62 --> 2773.14]  You know what I mean?
[2773.34 --> 2774.44]  So that's an incredible.
[2774.62 --> 2774.80]  Yeah.
[2774.88 --> 2780.78]  And so the entire discussion and this is not I don't think something I don't know if you
[2780.78 --> 2785.20]  guys talk about this kind of stuff, but the entire discussion on, you know, the EU being
[2785.20 --> 2789.20]  able to regulate tech decisions of large companies.
[2789.20 --> 2789.50]  Right.
[2789.54 --> 2792.44]  So think USB-C charger and dongles.
[2793.10 --> 2793.54]  Right.
[2793.96 --> 2795.86]  For your iPhone and your headphones.
[2796.12 --> 2796.30]  Right.
[2796.38 --> 2802.00]  So now when I want to plug these in, I got to get an adapter instead of the existing
[2802.00 --> 2803.56]  lightning cable adapter I had.
[2803.56 --> 2803.82]  Right.
[2804.24 --> 2810.42]  And that's not quote unquote great for U.S. consumers that have already
[2810.42 --> 2814.64]  gone down that road or U.S. companies that have already gone down that road.
[2815.06 --> 2817.04]  And we don't have representation in the EU.
[2817.34 --> 2821.88]  And the largest companies that will be affected by it are the ones that we use the most.
[2822.44 --> 2828.36]  There was another thing with didn't Apple bend on China and the Great Firewall?
[2828.78 --> 2829.76]  That I don't know.
[2830.14 --> 2831.06]  That was about three years ago.
[2831.06 --> 2831.36]  Yeah.
[2831.46 --> 2835.98]  I mean, yeah, I think Apple's done whatever they can to appease the Chinese market.
[2836.86 --> 2837.02]  Yeah.
[2837.16 --> 2838.36]  So, yeah, absolutely.
[2838.84 --> 2838.88]  Like.
[2839.06 --> 2839.74]  But they weren't able.
[2839.74 --> 2840.18]  Yeah.
[2840.18 --> 2843.20]  They weren't able to sell, I don't think, in China for a long time.
[2843.82 --> 2848.54]  And they had to do something to appease the government.
[2849.16 --> 2851.42]  And they did because it's a freaking huge market.
[2851.52 --> 2852.28]  Oh, yeah.
[2852.44 --> 2853.48]  It'd be crazy not to.
[2853.60 --> 2855.90]  The interesting there, Jess, the divide there.
[2856.18 --> 2858.08]  The hardware-software divide is interesting, right?
[2858.08 --> 2865.78]  So, when it came to you have to have USB-C in your phones or whatever the actual rules became in the EU.
[2865.88 --> 2868.28]  It's like, okay, we're just going to do that now.
[2868.28 --> 2870.84]  And then it affects everybody around the world.
[2870.84 --> 2874.24]  When it comes to software, though, they've taken the completely different stance.
[2874.24 --> 2876.54]  They're like, okay, we're only going to do that in the EU.
[2876.66 --> 2878.86]  Like, we're going to actually bifurcate the code base.
[2879.04 --> 2883.94]  We're going to have, you know, think about the complexity inside of the code for the App Store and for all the things.
[2883.94 --> 2890.40]  In order to only enforce this stuff in the EU and then everybody else around the world, it's different.
[2891.16 --> 2894.18]  A, that's got to be tons of tech debt inside of Apple.
[2894.86 --> 2901.88]  B, it actually creates so many problems for people who are outside of Apple but are shipping apps to these stores.
[2902.32 --> 2909.88]  Because now they have to have certain forks in their code in order to apply, you know, these rules depending on where the thing gets downloaded.
[2909.88 --> 2914.76]  I mean, it's so messy that, gosh, it seems untenable in the long run.
[2915.50 --> 2920.38]  I mean, it speaks to the bets that they're making on their own ecosystem being such a lock-in.
[2920.68 --> 2920.76]  Yeah.
[2920.88 --> 2927.08]  And it speaks to probably what the truth is about how much money they take in.
[2927.70 --> 2931.40]  Like, bifurcating the code base versus B billions?
[2932.08 --> 2933.10]  I don't know.
[2933.38 --> 2934.44]  That seems easy to me.
[2934.60 --> 2936.90]  I'll bifurcate the code base all day for that.
[2936.90 --> 2947.24]  Yeah, they make a ton of money off of their kind of, you know, whatever their mafia fees or whatever, belly goat fees, you know, whatever you want to call them.
[2947.44 --> 2948.34]  They, you know, they make a ton of money.
[2948.34 --> 2950.56]  And I don't, and again, it's not just Apple here, right?
[2950.60 --> 2954.30]  I'm sure Google's not like, you know.
[2954.44 --> 2956.26]  Well, they have the exact same cut in Android.
[2956.30 --> 2958.32]  They're all doing something very similar.
[2958.48 --> 2958.66]  I think.
[2958.74 --> 2959.30]  It's 30%.
[2959.30 --> 2967.74]  I think, you know, the kind of difference with Google is that, like, you know, part of their business still relies, you know, not still heavily relies on the open web, you know?
[2967.88 --> 2973.04]  And so they have these kind of, they are two-headed dragon as opposed to, like, this one-headed dragon, right?
[2973.04 --> 2983.40]  And even just internally within Google, you know, for years, there's been tension between, like, the, you know, Chrome platform folks and the Android platform folks because, you know, one is trying to eat the other.
[2983.52 --> 2986.02]  Really, one is trying to cannibalize the other, right?
[2986.04 --> 2989.70]  Like, Android is trying to take over everything, you know, everything be native.
[2990.04 --> 2992.78]  You know, the Chrome folks are like, no, you know, we're trying to go the other way.
[2992.78 --> 3006.26]  We're trying to kind of save the web and trying to give the web legs and, like, you know, give the web these richer APIs, you know, things like file system access and, you know, push notifications and, like, you know, home screen kind of access.
[3006.36 --> 3007.16]  All this stuff, right?
[3007.20 --> 3011.66]  That kind of will give us the ability to kind of compete with native apps, you know?
[3011.68 --> 3017.44]  And there's no question that, like, obviously the browser sandbox is much more secure, much more private for users, right?
[3017.44 --> 3020.10]  There's tons of benefits for this, like, on the user side.
[3020.10 --> 3026.94]  You know, but Apple, like, ultimately, like, they've been systemically kind of, and I should say allegedly, right?
[3027.00 --> 3028.68]  Because this is, like, these are all allegations.
[3028.68 --> 3037.96]  But, like, systemically, they've been kind of allegedly underfunding WebKit, even though, even though, like, they actually get billions and billions of dollars.
[3038.36 --> 3040.30]  They make billions of dollars on the web.
[3040.36 --> 3041.30]  And how do they do that?
[3042.30 --> 3045.00]  Google gives Apple billions of dollars every year.
[3045.30 --> 3047.62]  Like, I think it started at, like, $10 billion in 2020.
[3047.62 --> 3050.38]  It went up to $15 billion in 2021.
[3050.96 --> 3053.86]  I think it was, like, $17 or $18 billion in 2022.
[3054.32 --> 3062.68]  You know, it's, like, well over $15 billion now annually so that Google is the default search on Safari.
[3063.06 --> 3064.30]  So they have the money.
[3064.44 --> 3066.10]  They have the money to fund the engineers.
[3066.30 --> 3068.58]  They have the money to beef up and staff up Safari.
[3068.82 --> 3073.40]  Like, there's no excuse here other than just, like, it hurts their other business.
[3073.40 --> 3076.76]  You know, like, they have no, there's no incentive for them to.
[3076.82 --> 3077.68]  Anti-competitive.
[3077.70 --> 3078.76]  To support the open web.
[3078.86 --> 3079.00]  Yeah.
[3079.18 --> 3079.56]  It's, like.
[3079.92 --> 3080.80]  Here's a side question.
[3081.38 --> 3087.32]  How many users do you have to get on your web browser to get a billion out of Google for your search bar?
[3087.54 --> 3090.22]  I mean, what percentage do you, I mean, it can't be that much.
[3090.26 --> 3091.46]  Because how much is Firefox getting?
[3091.82 --> 3094.14]  I mean, they're down in, like, the 1%, 3%.
[3094.14 --> 3096.36]  I can't remember where they are in browser share right now.
[3096.42 --> 3097.30]  It's not high anymore.
[3097.30 --> 3100.06]  And they're still getting paid for that search bar.
[3100.54 --> 3105.70]  So you have to understand the difference with iPhone users is that they represent the wealthiest people in the world.
[3106.18 --> 3106.26]  Yeah.
[3106.28 --> 3109.26]  And so that's, like, if, you know, it's very different.
[3109.34 --> 3112.84]  Like, the, however, I don't know, is it 16% of the global market share?
[3112.98 --> 3115.08]  18% of the global market share is iPhones.
[3115.20 --> 3117.00]  Like, it's under 20%.
[3117.00 --> 3122.88]  Like, but that 20% represents, like, the majority of the world's kind of purchasing power.
[3123.32 --> 3124.28]  Does that make sense?
[3124.38 --> 3124.84]  And so.
[3125.28 --> 3125.64]  Totally.
[3125.64 --> 3134.26]  So even, so that, like, any numbers or ratios have to kind of be taken into account with, like, with that other metric, you know, which is why this fight is so important.
[3134.54 --> 3136.00]  I'm just thinking we should start a browser.
[3136.16 --> 3136.80]  That's all I'm thinking.
[3137.10 --> 3137.46]  Well.
[3137.62 --> 3138.76]  Seems like there's good money in it.
[3139.80 --> 3140.54]  You know what?
[3140.66 --> 3142.40]  It's, people are doing that.
[3142.48 --> 3142.94]  There's this.
[3143.36 --> 3143.70]  They are.
[3143.88 --> 3149.04]  I have someone, well, they're a group of folks that I would like to invite on the show in the future.
[3149.32 --> 3149.80]  What is it called?
[3149.88 --> 3150.16]  Arc.
[3150.60 --> 3151.74]  Like, the browser company.
[3152.14 --> 3152.42]  You know?
[3152.72 --> 3153.18]  Yeah, yeah, yeah.
[3153.18 --> 3157.02]  I'd love to hear from them on, like, their ambitious goals.
[3157.22 --> 3158.24]  I can talk to it.
[3158.28 --> 3158.84]  Please, yeah.
[3158.90 --> 3159.28]  Yeah.
[3159.46 --> 3159.74]  I'm curious.
[3160.30 --> 3160.52]  Yeah.
[3160.62 --> 3166.52]  So they recently released, I think, over the last two months, they released a video about their vision for Arc.
[3166.52 --> 3178.52]  And the line that stuck with me is that they feel that we are in an era where we're hunting and pecking the gatherer, hunter, the gatherer.
[3178.52 --> 3178.90]  There we go.
[3178.90 --> 3182.74]  The gatherer stage of finding information.
[3182.74 --> 3191.16]  Where we have to manually type into a browser and kind of go through the links and be like, is this the right one?
[3191.22 --> 3192.22]  Is this the right one?
[3192.54 --> 3196.18]  And eventually we find the right source of information.
[3196.70 --> 3199.16]  So I think they're going to go search bar.
[3199.80 --> 3204.32]  I think they're going to, like, try to infer user intent and redirect you to the right page.
[3204.32 --> 3213.18]  I think they're, my bet, if I was the front door of the internet, I get in before the user types in google.com, right, if I'm building a browser.
[3213.60 --> 3218.30]  So I think they're going to go and try to make money off of building a browser.
[3218.88 --> 3224.32]  They said that we'll look back at this time period and be like, wow, how primitive.
[3224.32 --> 3233.08]  The way we look at books and the indices inside of the back of a book and we're like, oh, how do I find this material?
[3233.78 --> 3235.88]  Scan for the chapter page, open the book.
[3236.24 --> 3237.84]  Which was really cool tech back in the day.
[3238.02 --> 3238.20]  Yeah.
[3238.58 --> 3240.44]  So how does AI fit into ARX Model Jets?
[3240.54 --> 3248.86]  Like specifically, you know, with ChatGPT and Bing kind of having a little love festival, right?
[3248.86 --> 3253.74]  So are they planning on using AI to kind of supercharge that experience as well?
[3254.54 --> 3255.08]  I can't remember.
[3255.50 --> 3258.82]  I mean, everybody is, but I can't remember if they explicitly mentioned it.
[3259.42 --> 3267.68]  The one thing ARX does really well is UX and frequent releases and the publicity of those releases and the features that they've added.
[3267.82 --> 3273.16]  So they have release notes every single week on Thursdays is their release week.
[3273.82 --> 3275.40]  And it'll show up in my sidebar.
[3275.50 --> 3276.64]  It'll be like, release.
[3277.18 --> 3278.32]  It's a really cool browser.
[3278.32 --> 3279.24]  Try it out.
[3279.88 --> 3281.70]  It's a different way of organizing stuff.
[3281.92 --> 3285.08]  I no longer have tabs at the top of my screen or a URL bar.
[3285.42 --> 3286.86]  URL bar is my favorite part.
[3287.22 --> 3287.84]  It's useless.
[3288.18 --> 3289.10]  It's useless.
[3289.78 --> 3292.72]  I've never felt more obsolete than right now.
[3292.92 --> 3293.86]  My favorite part's useless.
[3294.36 --> 3307.14]  I have an entire rant on why URLs are actually a construct that we've made because we have to use text specifically to send information like over the wire.
[3307.14 --> 3307.78]  Okay.
[3307.78 --> 3309.12]  Versus something like airdrop.
[3309.34 --> 3310.46]  Airdrop has no URLs.
[3310.78 --> 3311.04]  True.
[3311.26 --> 3312.30]  I definitely want to hear that rant.
[3312.42 --> 3314.80]  Save that for an upcoming rant episode.
[3315.20 --> 3319.08]  Maybe we do some unpopular opinions or some hot takes or something.
[3319.58 --> 3320.18]  Rant hour.
[3320.44 --> 3323.30]  Nobody agreed with me, by the way, when I gave that hot take on a Twitter space.
[3323.30 --> 3325.36]  I see your point.
[3325.36 --> 3328.34]  I think we need a better protocol.
[3328.84 --> 3330.82]  I agree that protocol is outdated.
[3331.38 --> 3335.12]  But for me, it's like, show me what's the replacement.
[3335.12 --> 3335.48]  Right?
[3335.58 --> 3336.24]  Like, yeah.
[3336.32 --> 3336.60]  Oh, yeah.
[3336.62 --> 3338.34]  This is this is 15, 20 years.
[3339.00 --> 3340.04]  Hopefully not that long.
[3340.16 --> 3343.02]  But but yeah, I agree.
[3343.14 --> 3344.34]  It might it might be that long.
[3344.46 --> 3346.30]  I mean, for it to become a standard.
[3346.30 --> 3347.82]  Let's say 40.
[3348.18 --> 3348.32]  Yeah.
[3348.70 --> 3349.10]  Right.
[3350.14 --> 3350.62]  All we need.
[3350.70 --> 3352.44]  That's what we need is one more standard.
[3352.64 --> 3354.58]  Well, the blog post right now.
[3354.66 --> 3355.90]  This is a moving target.
[3356.36 --> 3361.80]  So as we record February 16th, as you listen seven days later, it'll be like 10 days left.
[3361.80 --> 3364.72]  They have a survey that they want you to fill in.
[3364.80 --> 3368.94]  If you are somebody who ships a web app in the EU, they think that that will help.
[3369.56 --> 3374.34]  I don't know what the OWA's next move is here, if they even have one.
[3374.84 --> 3379.18]  But iOS 17.4 ships 19 days from now, according to this.
[3379.90 --> 3383.46]  And they have a digital markets at countdown on the website.
[3383.66 --> 3387.30]  So we will link to that in the show notes.
[3387.30 --> 3397.00]  And then stay tuned for a full episode with the people who are the movers and shakers on the OWA side as a male.
[3397.08 --> 3398.02]  Trying to put that one together.
[3398.46 --> 3399.60]  I'm definitely excited about that.
[3399.68 --> 3399.78]  Yeah.
[3399.82 --> 3401.76]  I was literally just chatting with Bruce this morning.
[3401.90 --> 3403.36]  Bruce Lawson, who's one of the folks.
[3403.50 --> 3405.60]  And he I asked him, OK, what can I do to help?
[3405.84 --> 3408.36]  He's like, I'm going to read read his response to you.
[3409.10 --> 3412.92]  You could encourage anyone who operates a PWA in the EU.
[3412.92 --> 3416.84]  They could be a U.S. company with EU customers or an EU company.
[3417.30 --> 3419.20]  To fill the survey at the top of our blog post.
[3419.38 --> 3420.32]  So thank you.
[3420.74 --> 3421.50]  Thank you, Jared.
[3421.78 --> 3421.96]  Yes.
[3422.08 --> 3425.36]  And he said, this will give us evidence to take to the European Commission.
[3425.80 --> 3427.66]  And doing it this weekend would be great.
[3428.16 --> 3430.22]  You know, doing it as soon as possible, basically, would be great.
[3430.52 --> 3431.48]  And you don't need to.
[3431.68 --> 3433.34]  He said that they don't need to give their names.
[3433.60 --> 3434.72]  It would be nice if they do.
[3434.82 --> 3435.88]  But it can be anonymous.
[3436.60 --> 3438.68]  I will collate it and submit it to the right people.
[3438.68 --> 3441.08]  So yeah, they're collecting that.
[3441.98 --> 3442.68]  Collecting data.
[3443.36 --> 3443.46]  Yeah.
[3443.76 --> 3444.14]  All right.
[3444.14 --> 3448.80]  We have two other links that I gathered for this, but we've spent plenty of time talking
[3448.80 --> 3449.22]  about that.
[3449.28 --> 3452.06]  We have, is anybody excited to talk about either of the following two topics?
[3452.54 --> 3458.20]  Topic one, LLRT, Amazon's new low latency JavaScript runtime.
[3458.78 --> 3459.54]  That's one.
[3459.66 --> 3467.48]  And then two is a new library called Tempo, a new date library for JavaScript and TypeScript.
[3468.18 --> 3469.74]  Anybody excited to talk about either of those?
[3469.84 --> 3470.58]  Happy to talk about either.
[3470.76 --> 3472.02]  Happy to just call it a show.
[3472.02 --> 3472.96]  What are y'all thinking?
[3473.04 --> 3473.46]  What are y'all feeling?
[3473.68 --> 3477.24]  I'm excited about the LLRT thing, but I don't know if anyone else is.
[3477.74 --> 3481.40]  I didn't dig deep into it, so I don't have much to say except for we have another runtime.
[3481.74 --> 3481.90]  Yeah.
[3482.32 --> 3483.76]  That's all I have to say about that.
[3483.86 --> 3490.80]  All I have to say about that is like Amazon needs to contribute and fund Node.js and support
[3490.80 --> 3491.32]  the ecosystem.
[3491.32 --> 3492.22]  Instead of doing this work.
[3492.36 --> 3494.04]  Support the ecosystem that everyone else uses.
[3494.04 --> 3496.96]  Instead of just rolling their own.
[3496.96 --> 3502.50]  Specifically when Lambda basically is so heavily dependent on Node.js and essentially this is
[3502.50 --> 3504.42]  kind of a clone of Node.js.
[3505.42 --> 3510.88]  So fix the performance and runtime issues in Node core as opposed to reinventing your own
[3510.88 --> 3511.12]  wheel.
[3511.58 --> 3513.40]  But whatever, capitalism.
[3513.40 --> 3517.18]  So as I understand, they pulled in something called Quick.js.
[3517.54 --> 3519.12]  I don't know what Quick.js is though.
[3519.24 --> 3525.20]  It sounds like it's if LLRT is to Node as V8 is to Quick.js or something like that.
[3525.24 --> 3526.56]  I don't know what Quick.js is.
[3526.86 --> 3528.00]  I'm interested in that.
[3528.34 --> 3528.46]  Yeah.
[3528.54 --> 3530.88]  Quick.js, they say, is the JavaScript engine.
[3531.20 --> 3537.14]  The point of this particular low latency runtime, if it's not obvious by the name, is they're
[3537.14 --> 3542.84]  trying to specifically optimize for fast and efficient serverless applications.
[3543.04 --> 3547.64]  So boot time is really what they're optimizing for, which makes sense because of Lambda and
[3547.64 --> 3549.94]  all of the serverless things that they offer.
[3550.54 --> 3552.02]  I haven't heard of Quick.js either.
[3552.12 --> 3553.18]  I'd be interested in that.
[3553.30 --> 3557.48]  Maybe we can do a deep dive with some folks if that's like an open source thing that they're
[3557.48 --> 3560.80]  working on or that they've just pulled in from a different group.
[3561.04 --> 3562.68]  But yes, we have one more of these.
[3562.78 --> 3566.82]  It seems like it's been the, not the year of, but maybe like the couple years of
[3566.82 --> 3569.00]  proliferating JS runtimes.
[3569.48 --> 3572.08]  And there's pros and cons to that.
[3572.26 --> 3575.50]  Mel, obviously you are thinking, let's all contribute to Node.js.
[3576.42 --> 3583.12]  Other people are thinking, you know, different techniques, different approaches worth perhaps
[3583.12 --> 3584.64]  reinvention, worth competition.
[3584.80 --> 3585.18]  I don't know.
[3585.74 --> 3588.14]  I kind of flip flop on that myself.
[3588.14 --> 3588.58]  Yeah.
[3588.74 --> 3592.88]  I mean, I think for me, just relying on a new engine as well, like someone who's worked
[3592.88 --> 3596.80]  on with JavaScript engines very closely in the past, specifically when it comes to
[3596.82 --> 3602.54]  bugs and interoperability, like, you know, there's a whole matrix of bugs that you're
[3602.54 --> 3603.56]  now potentially introducing.
[3603.80 --> 3606.26]  Like how spec compliant is this, you know?
[3606.38 --> 3609.84]  And like, are these being run against the same tests that all of the other engines are
[3609.84 --> 3610.66]  being run against?
[3610.70 --> 3614.68]  And like, it's a lot of work to have a spec compliant JavaScript engine.
[3614.68 --> 3621.06]  So I'm very curious to see how spec compliant, like, Quik is, because obviously, like, if
[3621.06 --> 3625.36]  and what that means to developers, if something is not spec compliant, is that like, you think
[3625.36 --> 3630.02]  Fetch is doing something or you think a map is doing something and it's doing something
[3630.02 --> 3630.68]  different, right?
[3631.10 --> 3634.00]  Can you talk a little bit about the development of Bun if you're interested?
[3634.16 --> 3634.40]  Sure.
[3634.46 --> 3634.66]  Yeah.
[3634.66 --> 3634.94]  Yeah.
[3634.94 --> 3640.36]  You had the pleasure of listening to Jared Semner talk a lot over the last year.
[3640.94 --> 3648.00]  I did his interview on his Twitter space on Bun1.0 and they took a lot of the tests actually,
[3648.16 --> 3649.64]  specifically from Node.
[3650.10 --> 3654.90]  So like, they just read the tests and tried to comply with them.
[3655.72 --> 3657.14]  And so that was really interesting to hear.
[3657.24 --> 3658.34]  I was like, that's really smart.
[3658.34 --> 3664.92]  The second thing is that if you're a runtime and a company, what's your end game?
[3665.56 --> 3667.84]  Why do you want to be a company that builds a runtime?
[3668.54 --> 3670.14]  Why would investors invest in you?
[3670.62 --> 3674.70]  What's the end game plan for Bun's parent company, Oven, right?
[3674.98 --> 3676.10]  Which is currently only Bun.
[3676.62 --> 3679.78]  But what end game, if you were a founder, what would you do?
[3680.48 --> 3680.58]  Yeah.
[3680.68 --> 3686.72]  I mean, my guess is there's, you know, some compute, like cloud hosting thing that they're
[3686.72 --> 3690.32]  going to, you know, try to hopefully leverage to fund the open source?
[3690.46 --> 3690.98]  I hope so.
[3691.22 --> 3694.88]  Ultimately, like, you know, the best thing for the community is for there to be some
[3694.88 --> 3696.80]  path towards sustainability for Bun.
[3696.92 --> 3700.92]  So, you know, I really hope that like they find that because otherwise that would really
[3700.92 --> 3701.34]  suck.
[3701.44 --> 3701.74]  Right.
[3702.08 --> 3703.26]  But yeah, I agree.
[3703.38 --> 3707.80]  I think for me, like, I mean, I'm personally a little perturbed with like the whole like
[3707.80 --> 3709.84]  VC dev tooling space.
[3709.84 --> 3711.72]  Like it's in some cases it makes sense.
[3711.82 --> 3715.20]  In some cases I'm like, I don't, I don't understand how this is going to make money.
[3715.20 --> 3717.92]  But I think the verdict is still out for Bun.
[3718.08 --> 3719.12]  So I'm very eager to see.
[3719.46 --> 3719.60]  Yeah.
[3719.90 --> 3722.96]  So I think that they're going to try to be both.
[3723.40 --> 3729.20]  I think they're going to try to, you know, sell really fast serverless compute, right?
[3729.42 --> 3731.24]  Really fast spin up times.
[3732.20 --> 3736.62]  And I think that Amazon is trying to do the same.
[3737.08 --> 3742.18]  But what I think is good about Bun, it's different about Amazon is they're doing the whole
[3742.18 --> 3748.88]  thing and they're doing it open source and they're being friendly with every layer, right?
[3748.94 --> 3755.90]  You don't need to use, if you're using, let's say, node or, you know, TS node or whatever
[3755.90 --> 3760.30]  as your executable, you can still use Bun as a package manager.
[3761.10 --> 3762.48]  And that's an interesting thing.
[3762.56 --> 3765.46]  You can use Bun test to test your code.
[3765.68 --> 3770.00]  That's interesting to me because they're playing nice and being really interoperable.
[3770.00 --> 3775.32]  And eventually you might be like, I like Bun as a runtime because it has extra features.
[3775.68 --> 3779.28]  Like, you know, they added the ability to use Bash.
[3779.82 --> 3784.54]  And this is really critical because also this means Windows support, right?
[3784.86 --> 3786.92]  Bash scripts that have Windows support.
[3787.02 --> 3791.92]  I don't know how many times you guys have done NPM install RimRaf as a node package so
[3791.92 --> 3796.44]  that you can support Windows RMRF in your development environments.
[3796.44 --> 3802.52]  But like, there's interesting things happening in the Bun time.
[3802.80 --> 3803.88]  It needs to be called the Bun time.
[3804.30 --> 3806.80]  I'm over it being the Bun runtime.
[3807.32 --> 3810.26]  So many people are on board with me that it's the Bun time.
[3810.50 --> 3811.18]  Jared won't do it.
[3811.66 --> 3812.18]  I don't care.
[3812.58 --> 3814.66]  Every platform I'm on, I'm going to call it the Bun time.
[3815.08 --> 3821.48]  So the Bun time is doing some really interesting things that are extra, you know, like built-in
[3821.48 --> 3824.56]  server, built-in ability to serve web apps.
[3824.56 --> 3826.74]  Yeah, I mean, it's super cool.
[3827.04 --> 3830.04]  It's what I think the community also just generally needs.
[3830.28 --> 3834.86]  Like, there needs to be, like, without competition, it breeds stagnation, right?
[3834.92 --> 3839.54]  So, like, I'll think everything is going to get better because somebody threw the goalpost
[3839.54 --> 3840.86]  a little further this time.
[3841.26 --> 3842.06]  So that's great.
[3842.40 --> 3847.78]  And I think for me, the difference with the Bun and this new runtime LRT is that, like,
[3848.42 --> 3853.68]  Bun was strategic enough to use a very battle-tested JavaScript engine, which is JavaScript core.
[3853.68 --> 3855.04]  Ironically, the same.
[3855.60 --> 3857.06]  It's the WebKit engine.
[3857.62 --> 3859.30]  And so what is Quick?
[3859.64 --> 3861.00]  Like, I've never even heard of Quick.
[3861.60 --> 3865.92]  Like, you know, like, I'm so, like, I just, I don't know how battle-tested that is.
[3866.00 --> 3872.08]  So I'd be curious to see, like, how well-supported the JavaScript, like, JavaScript is.
[3872.18 --> 3873.46]  Or is it, like, limited JavaScript?
[3873.64 --> 3874.64]  Like, I don't even know, right?
[3875.16 --> 3877.96]  Quick.js is a small and embeddable JavaScript engine.
[3877.96 --> 3883.60]  It supports the ES2023 spec, including modules, asynchronous generators, proxies, and big int.
[3884.10 --> 3889.42]  It has had two releases, one in December and one in January of this year.
[3889.74 --> 3890.64]  So it's brand new.
[3891.20 --> 3894.26]  I haven't been able to figure out who's developing it.
[3894.38 --> 3896.98]  Does it sound like it's targeted to microcontrollers?
[3897.50 --> 3900.38]  The main features are small and easily embeddable.
[3900.90 --> 3903.10]  Just a few C files, no external dependency.
[3903.10 --> 3905.96]  The x86 code for a simple hello world program.
[3906.46 --> 3912.42]  Hard to say, but it seems like that because, yes, because easily embeddable is a point.
[3913.32 --> 3914.34]  Bellard.org.
[3914.50 --> 3915.28]  Is this the guy?
[3915.40 --> 3916.20]  Fabrice Bellard.
[3916.88 --> 3918.32]  Oh, this is Fabrice Bellard.
[3918.62 --> 3920.22]  He's built tons of awesome stuff.
[3920.38 --> 3920.58]  Yeah.
[3921.26 --> 3922.30]  He's supposed to be good.
[3922.30 --> 3926.30]  Yeah, he's the author of lots of stuff that I can't think of right now.
[3927.04 --> 3927.44]  Kimu.
[3928.46 --> 3928.94]  FFmpeg.
[3929.00 --> 3929.62]  That's the big one.
[3929.72 --> 3930.16]  FFmpeg.
[3930.30 --> 3932.20]  So the open question is how is spec compliant?
[3932.20 --> 3940.48]  Like, can you take your existing legacy JavaScript and just plop it and it'll work 100% as expected?
[3940.66 --> 3941.82]  Or are there gotchas, right?
[3941.90 --> 3947.36]  Like, are there certain parts of the spec that are not supported because they're starting in 2023?
[3947.90 --> 3948.70]  So I don't know.
[3948.78 --> 3952.46]  These are all questions I would love to have answers to.
[3952.70 --> 3954.38]  For Bunn, the answer is no, it's not.
[3954.56 --> 3957.48]  You said building on the existing JavaScript engine, right?
[3957.48 --> 3957.70]  Yeah.
[3957.82 --> 3964.70]  So Bunn uses JavaScript core, like JSC, which that's like the Bunn equivalent of V8.
[3965.94 --> 3971.04]  So Node doesn't like, Node uses a JavaScript engine to like parse JavaScript.
[3971.04 --> 3979.28]  And like, like it doesn't, it doesn't build its own engine and sit in the same, same way Bunn didn't build its own like JavaScript engine that uses JavaScript core.
[3979.28 --> 3984.04]  So JavaScript core is maintained primarily at Apple.
[3984.76 --> 3986.70]  V8 is maintained by Google.
[3987.08 --> 3987.50]  Wait, wait, wait.
[3987.82 --> 3989.22]  I don't think that's correct.
[3989.34 --> 3992.68]  But I want to be, I want to be like fact checked on this.
[3993.04 --> 3995.76]  What I do know is correct is it doesn't even use LibUV.
[3996.60 --> 4000.64]  Like they wrote their own, they wrote their own OS specific bindings.
[4000.64 --> 4003.58]  Yeah, that's so LibUV is like a node dependency.
[4003.96 --> 4005.78]  And so that's the difference.
[4005.90 --> 4009.84]  So that's where like, there's like, it's like kind of like a series of shells, right?
[4009.86 --> 4010.48]  Like in layers.
[4010.66 --> 4013.84]  So like the JavaScript engine is like the first layer.
[4014.16 --> 4018.70]  And then there's other layers built on top of that, that are node dependencies or node specific.
[4019.06 --> 4021.08]  And so that's the kind of Delta, right?
[4021.16 --> 4025.12]  So like Bunn has a JavaScript engine because it would, it's way too much work to create a new one.
[4025.12 --> 4033.30]  And then on top of that, they have their own like zig layers and, you know, their zig layers are going to be different than nodes.
[4033.92 --> 4034.88]  C++ layer.
[4035.22 --> 4035.48]  Yeah.
[4035.92 --> 4045.82]  There's a bunch of things in node that are like either third party dependencies or node specific code, you know, that kind of create that, create the API surface.
[4046.20 --> 4048.46]  So I don't know if I'm making sense, Jess, but like.
[4049.42 --> 4050.48]  You're doing fine.
[4050.78 --> 4051.04]  You're doing fine.
[4051.04 --> 4051.48]  That's correct.
[4051.48 --> 4056.36]  I did, I fact checked Amel and JavaScript core is the engine inside of Bunn.
[4056.90 --> 4057.30]  Thank you.
[4057.58 --> 4061.86]  And QuickJS is the engine inside of Amazon's new thing.
[4062.22 --> 4066.52]  QuickJS is brand new and written by one guy, even though he's very talented.
[4066.66 --> 4069.38]  My guess is it says it supports ES 2023.
[4069.94 --> 4076.34]  So there's probably no backwards compatibility with like old stuff, but definitely an interesting project.
[4076.34 --> 4076.90]  Yeah.
[4076.90 --> 4076.98]  Yeah.
[4077.34 --> 4082.74]  You'd have to run the test 262 conformance suite with it with QuickJS.
[4083.06 --> 4085.98]  And then we'd have an answer for like, how good is this thing?
[4086.04 --> 4087.96]  Like it could be perfect, you know, like who knows?
[4088.60 --> 4088.90]  It's just.
[4089.28 --> 4089.46]  Yeah.
[4090.12 --> 4090.56]  Yeah.
[4091.06 --> 4097.22]  Says right here, it passes nearly 100% of the ECMAScript test suite tests when selecting the ES 2023 features.
[4097.38 --> 4097.52]  Yeah.
[4097.52 --> 4098.78]  So that's what it is.
[4098.78 --> 4099.00]  So.
[4099.44 --> 4100.48]  Select subset of features.
[4101.12 --> 4101.38]  Yeah.
[4101.86 --> 4110.18]  Which makes sense when you have a very specific thing you're trying to do, which exactly Amazon's trying to create this engine that is really, really good at booting fast.
[4110.52 --> 4117.04]  Because that's a problem with serverless runtimes is the, what do you call it, cold start times.
[4117.66 --> 4118.86]  And everyone's trying to work that out.
[4118.86 --> 4119.56]  But that's a tradeoff.
[4119.64 --> 4124.96]  Even inside of their own readme, they state that there are limitations.
[4126.00 --> 4139.46]  There are many cases, they say, where LLRT shows notable performance drawbacks compared with JIT powered runtimes, such as large data processing, Monte Carlo simulations, or performing tasks with hundreds of thousands or millions of iterations.
[4139.70 --> 4142.40]  So it's a tradeoff as all engineering is.
[4142.40 --> 4151.94]  And so, you know, I like the fact that there are now going to be different runtimes with different tradeoffs, depending on your particular use case, like Chris alluded to.
[4152.08 --> 4163.84]  Like if you're really trying to get it onto microcontrollers or really small places, that's a tradeoff you're willing to take in order to not have 100% coverage of the entire language, that kind of stuff.
[4164.08 --> 4168.00]  So I think diversity in that case, I think, is cool.
[4168.00 --> 4174.42]  And I don't know how this plays into the whole Cloudflare, Deno.
[4174.94 --> 4179.28]  Well, my guess is there's probably no observability layer probably either, right?
[4179.30 --> 4181.26]  Because maybe in this use case, you wouldn't need to.
[4181.34 --> 4185.46]  And that's part of also like one of the things that makes Node very different than Bun, right?
[4185.56 --> 4190.92]  Like is, you know, having that like enterprise level observability, right?
[4190.96 --> 4192.90]  Like being able to trace and all that stuff.
[4192.90 --> 4196.96]  Like if there's no need here, then yeah, like strip the chassis, right?
[4197.16 --> 4198.36]  Like strip it.
[4199.24 --> 4201.26]  So that's, yeah.
[4201.38 --> 4203.32]  I mean, look, I'm all for.
[4203.66 --> 4204.18]  Stripping the chassis.
[4204.30 --> 4204.40]  Yeah.
[4204.42 --> 4206.80]  Not only stripping the chassis, like creating these different use cases.
[4206.80 --> 4207.80]  Like I think this is great.
[4207.90 --> 4211.80]  It's just more like really it's important to advertise the tradeoffs to people.
[4211.92 --> 4215.06]  It's important to like explain to people like what the difference is.
[4215.10 --> 4218.20]  Like this is not your every use case runtime, you know?
[4218.38 --> 4219.52]  So as long as people know that.
[4219.70 --> 4219.94]  Right.
[4219.94 --> 4220.90]  It's 2024.
[4221.22 --> 4224.92]  There's still no silver bullets and somebody who's trying to sell you a silver bullet, either
[4224.92 --> 4227.76]  deceive themselves or trying to take advantage.
[4228.30 --> 4231.20]  All right, Chris, last word, not on just on this, but on the entire episode.
[4231.48 --> 4232.46]  This is the end, man.
[4232.54 --> 4233.92]  You get the final word, Chris.
[4233.96 --> 4234.40]  What are you thinking?
[4234.84 --> 4243.72]  Well, I'm just, I'm glad Jessica's here and we have some fresh, no, I mean new blood on
[4243.72 --> 4246.96]  the podcast.
[4246.96 --> 4252.36]  And yeah, looking forward to doing the podcast.
[4253.00 --> 4253.54]  Love it.
[4253.92 --> 4255.52]  With Jessica, the new person.
[4255.58 --> 4256.80]  With Jessica, the new person.
[4256.94 --> 4258.74]  Jessica, thanks so much for being our new person.
[4259.52 --> 4261.72]  Amel, thanks for being here as well.
[4261.86 --> 4263.02]  And Bone Skull, of course.
[4263.14 --> 4263.80]  Tons of fun.
[4264.12 --> 4268.28]  This conversation has, for me, sparked other episodes I would like to do.
[4268.60 --> 4270.38]  I think we should do a show about QuickJS.
[4270.82 --> 4276.50]  Obviously, OWA is coming on at some point and more bun, maybe some people from Amazon.
[4276.64 --> 4277.12]  Who knows?
[4277.38 --> 4281.10]  Lots of conversations to be had, but that's our time for today.
[4281.54 --> 4287.82]  So we will say goodbye and we will kick on that BMC outro song and we'll talk to y'all
[4287.82 --> 4288.98]  on the next episode.
[4288.98 --> 4308.66]  Well, we ran out of time, but we didn't run out of excitement about that tempo library
[4308.66 --> 4309.78]  I brought up earlier.
[4309.78 --> 4316.02]  So if you want to hear that discussion, become a Changelog++ member and directly support our
[4316.02 --> 4317.62]  work with your hard-earned cash.
[4318.06 --> 4321.66]  Or even better, your employer-sponsored education budget.
[4321.82 --> 4322.10]  Brilliant!
[4322.44 --> 4327.02]  As a thanks for your support, we make the ads disappear, send you some sweet, sweet
[4327.02 --> 4332.24]  JS Party stickers for your laptop, and hook you up with awesome bonuses like this extended
[4332.24 --> 4332.70]  episode.
[4332.70 --> 4339.46]  Join hundreds of your fellow JS Party listeners and subscribe today at changelog.com slash plus
[4339.46 --> 4339.86]  plus.
[4340.02 --> 4341.02]  Changelog++!
[4341.58 --> 4342.32]  It's better!
[4342.56 --> 4346.38]  Thanks again to our friends at fly.io and Sentry.
[4346.76 --> 4350.84]  Use code changelog when you sign up to save $100 off their team plan.
[4351.36 --> 4357.08]  Thanks also to our mysterious friend, Breakmaster Cylinder, for beat freaking for us all these
[4357.08 --> 4357.44]  years.
[4357.44 --> 4363.12]  That's all for this week, but come back, we'll be partying together again next week.
[4363.12 --> 4363.14]  We'll be partying together again next week.
