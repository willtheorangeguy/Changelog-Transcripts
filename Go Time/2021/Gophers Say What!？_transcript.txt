[0.00 --> 2.88]  Okay, what were the changelog people drinking when they did that?
[4.46 --> 5.54]  You guys.
[7.78 --> 11.14]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[11.54 --> 12.16]  We love Linode.
[12.24 --> 14.00]  They keep it fast and simple.
[14.30 --> 17.16]  Get $100 in credit at linode.com slash changelog.
[17.48 --> 19.68]  Our bandwidth is provided by Fastly.
[19.82 --> 21.60]  Learn more at Fastly.com.
[21.60 --> 24.10]  And get your feature flags powered by LaunchDarkly.
[24.24 --> 26.36]  Get a demo at LaunchDarkly.com.
[26.36 --> 30.00]  This episode is brought to you by Teleport.
[30.20 --> 35.58]  Teleport lets engineers operate as if all cloud computing resources they have access to are in the same room with them.
[35.96 --> 43.26]  SSO allows discovery and instant access to all layers of your tech stack behind NAT, across clouds, data centers, or on the edge.
[43.56 --> 46.86]  I have Ev Consovoy here with me, co-founder and CEO of Teleport.
[46.86 --> 54.30]  Ev, help me understand industry best practices and how Teleport Access Plane gives engineers unified access in the most secure way possible.
[54.30 --> 62.94]  So the industry best practice for remote access means that the access needs to be identity-based, which means that you're logging in as yourself.
[63.06 --> 65.16]  You're not sharing credentials from anybody.
[65.42 --> 67.92]  And the best way to implement this is certificates.
[68.34 --> 72.42]  It also means that you need to have unified audit for all the different actions.
[72.74 --> 81.00]  With all these difficulties that you would experience configuring everything you have, every server, every cluster, with certificate-based authentication and authorization,
[81.36 --> 83.44]  that's the state of the world today that you have to do it.
[83.44 --> 87.84]  But if you are using Teleport, that creates a single endpoint.
[88.16 --> 93.28]  It's a multi-protocol proxy that natively speaks all of these different protocols that you're using.
[93.28 --> 97.50]  It makes you to go through SSO single sign-on.
[97.80 --> 102.66]  And then it transparently allows you to receive certificates for all of your cloud resources.
[103.08 --> 107.80]  And the beauty of certificates is that they have your identity encoded and they also expire.
[107.80 --> 112.98]  So when the day is over, you go home, your access is automatically revoked.
[113.20 --> 115.28]  And that's what Teleport allows you to do.
[115.54 --> 123.84]  So it allows engineers to enjoy the superpowers of accessing all of cloud computing resources as if they were in the same room with them.
[123.90 --> 125.06]  That's why it's called Teleport.
[125.28 --> 128.62]  And at the same time, when the day is over, the access is automatically revoked.
[128.94 --> 130.10]  That's the beauty of Teleport.
[130.10 --> 134.32]  All right, you can try Teleport today in the cloud, self-hosted or open source.
[134.50 --> 136.88]  Head to goteleport.com to learn more and get started.
[137.14 --> 139.32]  Again, goteleport.com.
[156.58 --> 157.52]  Let's do it.
[158.10 --> 159.14]  It's go time.
[159.14 --> 175.20]  Hello and welcome to Go Time.
[175.34 --> 179.14]  I'm Matt Ryer and today we're playing a very special game.
[179.82 --> 185.80]  This is Gophers Say, a game show all about the opinions of our lovely Go Time listeners.
[185.80 --> 190.26]  This is Go Time's 200th episode.
[193.40 --> 193.88]  200th.
[194.46 --> 195.70]  Try saying that.
[196.02 --> 198.10]  It's a difficult word to say, 200th.
[198.54 --> 199.80]  You know, because the d and the th.
[199.96 --> 200.82]  It's weird.
[200.82 --> 208.20]  Well, we, of course, for our 200th celebration had to welcome back the Go Time OG hosts.
[208.66 --> 209.82]  Brian Ketelson's here.
[209.90 --> 210.54]  Hello, Brian.
[210.82 --> 211.52]  Hello, Brian.
[211.52 --> 215.40]  Carlissia Thompson's also with us.
[215.48 --> 215.94]  Carlissia.
[215.98 --> 217.06]  Hi, everybody.
[217.06 --> 218.22]  Glad to be here.
[218.32 --> 219.10]  Glad you are here.
[219.68 --> 221.34]  Eric St. Martin is also here.
[221.42 --> 221.92]  Aren't you, Eric?
[222.46 --> 223.06]  Hey, everybody.
[223.78 --> 224.60]  Welcome, Eric.
[224.76 --> 225.74]  It's great to have you back.
[226.22 --> 230.92]  And we're also joined by some present-day hosts that you may have seen knocking about.
[231.62 --> 232.96]  Natalie Pistinovich is here.
[233.18 --> 233.62]  Hello, Natalie.
[234.04 --> 234.50]  And everyone.
[234.96 --> 235.26]  Welcome.
[236.10 --> 237.28]  Chris Brando's also here.
[237.36 --> 238.28]  Chris Brando.
[238.40 --> 239.28]  Hello, Chris.
[239.56 --> 239.84]  Hello.
[240.68 --> 241.92]  Welcome to the game show.
[242.46 --> 243.74]  We've also got Angelica Hill.
[244.14 --> 244.78]  Hello, Angelica.
[245.16 --> 245.50]  Hello.
[246.04 --> 246.52]  Angelica.
[246.98 --> 249.02]  Does everyone sing your name if they've seen Hamilton?
[249.34 --> 249.60]  They do.
[249.86 --> 250.26]  Yes.
[250.38 --> 252.98]  And I then respond and make them feel very uncomfortable.
[253.30 --> 253.42]  Yeah.
[253.46 --> 253.58]  What?
[253.62 --> 255.16]  You harmonize with them straight away.
[255.36 --> 255.98]  That's good.
[256.24 --> 256.48]  Yeah.
[256.62 --> 257.88]  I just go, Eliza.
[257.88 --> 259.04]  And they're like, oh, God.
[259.82 --> 261.20]  That was a bit off tune.
[261.58 --> 261.84]  No, no.
[261.88 --> 262.26]  It's brilliant.
[262.38 --> 263.10]  We'll fix it in post.
[263.10 --> 264.76]  We've got voice pitch fixed.
[264.86 --> 265.44]  Mark can do it.
[265.54 --> 266.58]  He's a music producer now.
[266.88 --> 268.08]  We're auto-tuning everybody.
[268.28 --> 268.62]  Exactly.
[269.52 --> 271.58]  We've also got Johnny Borsico here, though.
[271.70 --> 272.92]  Hello, Johnny Borsico.
[273.64 --> 274.00]  Hello.
[274.24 --> 274.84]  Yes, mate.
[274.88 --> 275.86]  I'm here knocking about.
[276.44 --> 277.64]  Oh, you certainly are.
[277.74 --> 280.08]  I appreciate the accent because I can understand you.
[281.20 --> 281.64]  Really?
[282.00 --> 284.04]  That just breaks my heart.
[284.70 --> 286.04]  That was pretty bad, Johnny.
[286.86 --> 287.58]  I know.
[287.70 --> 288.08]  I know.
[288.18 --> 288.50]  I know.
[288.60 --> 290.02]  I've heard you do better, Johnny.
[290.44 --> 291.44]  Oh, no.
[291.44 --> 292.56]  Don't troll Johnny.
[292.70 --> 293.20]  He's one of the nicest.
[293.20 --> 293.94]  I can have fun.
[294.28 --> 295.58]  Johnny's the nicest one on here.
[295.94 --> 297.00]  I can't have a go at him.
[298.06 --> 299.68]  And last but not least.
[299.92 --> 300.08]  What?
[300.36 --> 300.96]  It is least.
[301.42 --> 302.48]  It's Mark Bates.
[302.76 --> 303.78]  Hello, Mr. Bates.
[303.86 --> 304.58]  Welcome back.
[304.86 --> 305.54]  Hello, everyone.
[305.90 --> 306.26]  Yes.
[306.44 --> 309.82]  I would do my Scouse accent, which I can do really, really well.
[309.92 --> 311.42]  But every other word is a swear.
[311.62 --> 313.48]  So I don't think that would be appropriate.
[314.02 --> 315.74]  I think you should do it anyway, mate.
[315.74 --> 317.00]  I think it'll be crackly.
[317.24 --> 317.78]  All right, mate.
[317.90 --> 318.20]  Yeah.
[318.36 --> 319.02]  Yeah, he's done it.
[319.24 --> 320.68]  You've done the burgers and the murders.
[322.72 --> 324.78]  Let me tell you about Go For Say.
[325.74 --> 328.72]  Go For Say is like Family Feud.
[328.96 --> 333.62]  Or in the UK, it's called Family Fortunes, which is actually much nicer, I think.
[333.72 --> 339.00]  It's a bit like how we have the Great British Bake Off, which is like everyone's all nice and they help each other.
[339.00 --> 343.08]  And then you have the U.S. MasterChef where they're like, I will destroy you.
[343.18 --> 344.70]  I'm going to make a souffle.
[345.22 --> 348.18]  You will be wiped from the face of the earth.
[348.32 --> 349.62]  Talking about bad accents.
[349.82 --> 350.04]  Jeez.
[350.30 --> 350.42]  Wow.
[350.70 --> 353.14]  I've just sang that bit all week, too, which is really sad.
[353.38 --> 354.68]  You should have done Ramsey.
[355.16 --> 357.18]  You burnt the effing risotto.
[358.48 --> 359.20]  It's raw.
[359.50 --> 364.92]  Okay, I think we should all try not to do accents anymore because so far they've all been terrible.
[365.18 --> 367.02]  I admit I'm terrible at accents.
[367.02 --> 367.84]  Wait, wait, wait, wait.
[367.84 --> 370.86]  If you're not going to do accents, what am I going to do?
[374.14 --> 376.12]  Oh, we should really move on.
[377.24 --> 384.72]  We asked a hundred gophers a set of questions and it's your job to find the most common answers.
[385.14 --> 387.04]  It's not a game of right or wrong.
[387.48 --> 394.66]  This is about getting into the horrible little minds that we've surveyed of those gophers and figuring out what they would have said.
[394.66 --> 398.74]  If you're on my team, you better think that it's about getting it right.
[401.48 --> 402.00]  Competitive.
[402.24 --> 402.88]  That's what I'm saying.
[402.98 --> 403.84]  Always be winning.
[404.02 --> 404.50]  That's Kralisha.
[404.92 --> 405.84]  Nights are out.
[405.84 --> 409.64]  You're going to be split into two teams, which we'll do in a moment.
[410.06 --> 416.56]  And we're going to round Robin asking you to try and guess the most common answers without conferring.
[417.04 --> 420.82]  So, for example, if the question is, what's your favourite programming language?
[421.20 --> 422.58]  You might say go.
[422.80 --> 426.28]  And if people agree with you, you'll hear this sound.
[426.28 --> 433.52]  If 95 people agree with you, you get 95 points.
[433.80 --> 434.84]  So that's pretty good.
[435.24 --> 439.86]  If you said, I don't know, Java, you might hear this sound.
[441.00 --> 443.50]  And that means nobody agrees.
[443.60 --> 447.92]  And unfortunately, you receive nil pois, which is French for no points.
[447.92 --> 450.26]  And you lose a life.
[450.44 --> 454.28]  If your team loses three lives, then the other team has a chance to steal the round.
[454.78 --> 457.28]  And you will be allowed to confer when it comes to stealing.
[457.60 --> 460.28]  You actually only have to get anything on the board to steal.
[460.56 --> 463.00]  So be careful of those steals.
[463.72 --> 465.52]  I'll try and make that my catchphrase for this.
[466.00 --> 467.10]  So does everyone understand the rules?
[467.46 --> 468.44]  No, let's do it.
[468.80 --> 469.24]  Yeah, me neither.
[469.74 --> 471.88]  You ask questions, we try to get them right.
[472.12 --> 472.34]  Boom.
[472.92 --> 474.10]  Yeah, something like that.
[474.10 --> 477.26]  If you've ever sat in a dentist's waiting room, you've seen the show.
[479.06 --> 479.50]  Really?
[479.66 --> 481.00]  What kind of dentist do you go to?
[481.32 --> 488.54]  Apparently one that likes Steve Harvey and likes to show nothing but Steve Harvey's version of Family Feud all day long.
[488.88 --> 489.06]  Okay.
[489.32 --> 495.20]  Yeah, he only goes to comedy or light TV related dentists, which is why all his teeth are hilarious.
[496.42 --> 498.94]  Okay, so I've tried to, I'm going to just quickly go around.
[499.06 --> 501.04]  We're going to meet our contestants here.
[501.04 --> 503.96]  I'm going to ask for your Twitter name in case people want to follow you.
[504.62 --> 505.42]  And I've got a question.
[505.52 --> 507.50]  I've tried to come up with some questions to sort of probe deep.
[507.76 --> 509.88]  So, you know, we're going to see if we can learn a bit about it.
[509.94 --> 510.64]  Brian, let's start with you.
[510.92 --> 512.56]  What's your Twitter name, Brian?
[512.86 --> 513.74]  It's B. Ketelsen.
[514.02 --> 514.28]  I see.
[514.34 --> 515.66]  And how are you spelling Ketelsen, mate?
[515.92 --> 516.94]  The Norwegian way.
[517.06 --> 519.52]  K-E-T-E-L-S-E-N.
[519.98 --> 520.30]  Okay.
[520.48 --> 521.22]  Thank you so much.
[521.24 --> 524.64]  And your question, I thought, Brian, what's your favorite URL scheme?
[525.20 --> 527.18]  Sort of HTTPS, FTP?
[527.82 --> 528.50]  Which one do you reckon?
[528.80 --> 529.52]  I like Gopher.
[529.52 --> 532.24]  Oh, what an answer, Brian.
[532.24 --> 533.72]  That is an old school.
[533.96 --> 534.26]  Old school.
[534.82 --> 535.58]  That's clever.
[535.80 --> 536.20]  Thank you.
[536.54 --> 536.96]  Excellent.
[537.42 --> 538.52]  It's clever, isn't it, Carleesia?
[538.82 --> 542.74]  Anyone who understood what he said, just consider yourself very old.
[545.04 --> 545.84]  Already there.
[545.90 --> 548.10]  I didn't understand it, by the way, but I was just playing along.
[548.76 --> 549.28]  Right, right.
[549.46 --> 552.26]  Carleesia, what's your Twitter name in case people want to follow you?
[552.56 --> 553.38]  It's my first name.
[553.74 --> 554.00]  Okay.
[554.14 --> 554.84]  How are you spelling that?
[555.58 --> 558.04]  I-T-S-M-Y.
[558.94 --> 559.50]  That'd be good.
[560.00 --> 562.62]  C-A-R-L-I-S-I-A.
[562.92 --> 563.36]  Excellent.
[563.92 --> 566.44]  And what's your favorite capture?
[566.86 --> 570.70]  You reckon it's find all the bicycles, crosswalks, traffic lights?
[570.92 --> 571.62]  Which one's your favorite?
[575.14 --> 575.92]  Oh my God.
[575.92 --> 579.86]  It's like, this question, I never understand why people have to have one favor.
[580.00 --> 582.08]  It's like, I don't have one favor of anything.
[582.16 --> 582.76]  You like them all.
[582.86 --> 584.48]  In this case, I don't like any of them.
[584.58 --> 585.20]  Can I go with that?
[585.80 --> 586.74]  Yeah, fair enough.
[586.86 --> 587.48]  No, that's fine.
[587.78 --> 588.22]  Yeah, yeah, yeah.
[588.24 --> 590.02]  I like the sites that don't have a capture.
[590.36 --> 590.86]  All right.
[591.62 --> 591.80]  Yes.
[591.80 --> 591.92]  Yeah.
[591.92 --> 593.12]  Who wants security?
[593.56 --> 594.04]  I'm with you.
[594.80 --> 595.16]  Eric.
[595.40 --> 596.28]  Eric St. Martin.
[596.76 --> 597.08]  Twitter.
[597.36 --> 600.32]  In case people want to troll you on Twitter, what's your Twitter name, Eric?
[600.52 --> 603.74]  It's my full name with all spaces and punctuation removed.
[604.12 --> 606.20]  So Eric St. Martin, all jammed together.
[606.58 --> 607.96]  Eric with a K though, isn't it?
[608.08 --> 609.20]  The evil way, yes.
[609.66 --> 610.44]  Yeah, it's the baddie.
[610.76 --> 611.32]  The baddie way.
[611.66 --> 614.34]  And is it the abbreviated saint or the full saint?
[614.50 --> 615.80]  It's the abbreviated one.
[616.04 --> 617.70]  See, this is why we ask.
[617.82 --> 619.00]  Which is my legal name.
[619.20 --> 619.80]  Is it?
[619.80 --> 621.80]  Unless we're talking to an automated system.
[621.96 --> 624.80]  And then sometimes I'm Eric Street Martin because...
[624.80 --> 627.26]  That's what I thought it was, yeah.
[627.40 --> 629.92]  Or unless it's Microsoft in which he's just St. Eric.
[630.32 --> 631.38]  Yes, this is true.
[631.84 --> 633.00]  I know that's pretty cool.
[633.14 --> 634.20]  That's not a bad title.
[634.76 --> 635.12]  Yeah.
[636.00 --> 639.84]  Eric, are you a sort of light mode or dark mode person?
[640.24 --> 641.14]  What sort of mode?
[641.18 --> 641.68]  Dark mode.
[642.12 --> 642.32]  Yeah.
[642.46 --> 643.34]  Definitely dark mode.
[643.52 --> 643.80]  Yeah.
[643.88 --> 644.80]  With the K, isn't it?
[644.88 --> 646.02]  It's the baddie K, so...
[646.02 --> 646.20]  Yep.
[646.20 --> 647.90]  I wish that had been my question.
[650.46 --> 651.48]  Natalie Pustinovich.
[651.82 --> 653.72]  How do people reach you on Twitter, Natalie?
[654.22 --> 656.28]  For the non-Germans in the crowd, it's Natalie.
[656.54 --> 658.50]  For the Germans, it's Natalie without H.
[658.50 --> 663.34]  So it's N-A-T-A-L-I-E and then P-I-S, the first three letters of my last name.
[663.64 --> 663.86]  Brilliant.
[664.04 --> 664.86]  So people can find you.
[665.00 --> 670.40]  And we'll put these Twitter names in the show notes too, for those that can't follow this chaos.
[671.00 --> 675.78]  Natalie, what would you say is your favorite modifier key on the keyboard?
[676.00 --> 677.04]  Command, option.
[677.18 --> 678.04]  I know it's not shift.
[678.50 --> 679.36]  How do you know that?
[679.36 --> 684.34]  Because Matt always complains that I never use uppercase.
[684.44 --> 689.10]  I always just type lowercase everything and also no other commas and so on.
[689.68 --> 690.54]  Yeah, I have none.
[690.60 --> 692.04]  But can I answer Colicia's question?
[692.40 --> 692.92]  Yes, please.
[693.00 --> 693.16]  Yeah.
[693.22 --> 694.16]  About my favorite CAPTCHA?
[694.44 --> 695.08]  Yeah, what is it?
[695.28 --> 696.66]  The fire extinguishers.
[696.66 --> 699.74]  Because a person who does not live in the US will not recognize those.
[699.86 --> 704.16]  Or a person who has not seen any American ones will not necessarily recognize those.
[704.28 --> 704.64]  That's true.
[704.72 --> 705.86]  But you'd probably figure it out.
[705.96 --> 707.84]  What on earth is that little thing, if not that?
[707.84 --> 709.24]  What else could it be?
[709.44 --> 712.50]  That's like two different types of tests that you're going through.
[712.78 --> 713.26]  Yeah.
[713.42 --> 713.78]  That's fun.
[714.06 --> 714.46]  Yes.
[715.24 --> 715.78]  Very good.
[716.72 --> 717.60]  Chris Brando's here.
[717.88 --> 718.88]  Chris Brando.
[719.28 --> 719.56]  Hello.
[719.92 --> 721.62]  Sounds like a movie star name, doesn't it?
[721.98 --> 723.10]  Like Marlon Brando.
[723.52 --> 723.78]  No.
[724.46 --> 724.70]  No.
[725.46 --> 727.20]  It does sound like that.
[727.80 --> 728.56]  What's your Twitter handle?
[728.92 --> 734.86]  My Twitter name is Scriptable, and it is spelled S-K-R-I-P-T-B-L-E.
[735.20 --> 735.72]  Very cool.
[735.72 --> 738.10]  That sounds like it was a startup at some point.
[738.90 --> 743.78]  Chris, if you had to pick one, what would you say is your favorite GUID?
[744.24 --> 745.04]  Favorite what?
[745.88 --> 746.32]  GUID.
[746.48 --> 747.74]  Globally unique identifier.
[748.52 --> 750.10]  Microsoft loves GUIDs.
[750.16 --> 752.04]  Do you have a favorite, Chris?
[752.12 --> 753.02]  Any that caught your eye?
[753.44 --> 753.86]  No.
[753.98 --> 756.88]  So I'll just answer Eric's question instead, because I like that one.
[757.26 --> 761.98]  So I prefer dark mode for my editor and light mode for everything else.
[762.20 --> 762.92]  Oh, cool.
[763.06 --> 763.24]  Yeah.
[763.36 --> 764.20]  Strike the balance.
[764.20 --> 764.68]  Hmm.
[765.02 --> 765.34]  Great.
[765.46 --> 765.66]  Okay.
[765.78 --> 770.28]  I'm really not getting the respect I'd hoped for on this, with people just choosing their
[770.28 --> 771.08]  own questions.
[771.36 --> 772.32]  But let's press on.
[772.72 --> 773.50]  I will press on.
[773.52 --> 776.48]  That's the problem with having a show full of hosts.
[776.60 --> 777.20]  That's true.
[778.40 --> 779.26]  I'm sorry.
[779.44 --> 780.22]  Have we met?
[783.04 --> 785.02]  Angelica Hill's here, aren't you, Angelica?
[785.12 --> 786.26]  What's your Twitter name?
[786.26 --> 787.40]  It's my name.
[787.54 --> 789.12]  Angelica underscore Hill.
[789.80 --> 790.62]  Bog standard.
[790.92 --> 793.42]  You have to type it in a British accent or any...
[793.42 --> 794.58]  Yeah, it's mandatory.
[795.08 --> 795.36]  Yes.
[795.56 --> 798.82]  Think British tea scones, queen corgis.
[799.36 --> 800.24]  He'll get me.
[800.58 --> 802.70]  And the at side's on the other side.
[802.96 --> 803.86]  Obviously, yeah.
[804.40 --> 804.68]  Yeah.
[804.90 --> 805.94]  The correct side.
[806.60 --> 806.90]  Yeah.
[807.28 --> 807.44]  Yeah.
[807.44 --> 811.38]  Angelica, what would you say is the best HTML tag?
[812.18 --> 814.04]  You've got sort of divs, your spans, your Ps.
[814.66 --> 817.20]  Which one would you go with if you had to pick one, which you definitely do?
[817.90 --> 819.66]  Probably script.
[819.78 --> 820.48]  Just because I...
[820.48 --> 824.38]  When I was first learning software engineering, I was obsessed with just shoving JavaScript
[824.38 --> 825.38]  in.
[825.86 --> 826.66]  Just like...
[826.66 --> 827.00]  Yeah.
[827.42 --> 828.80]  I didn't want to have separate files.
[828.90 --> 829.68]  Just shove it in.
[830.12 --> 830.34]  Yeah.
[830.36 --> 831.40]  That's a good answer.
[831.52 --> 832.02]  I like that.
[832.10 --> 832.92]  Although it's wrong.
[833.16 --> 835.38]  The answer is A, because without that, it's not...
[835.38 --> 837.24]  There is no wrong answers, Matt.
[837.28 --> 838.08]  There are no right or wrong answers.
[838.08 --> 840.48]  How dare you discriminate against my answer?
[840.82 --> 841.34]  No, no, no.
[841.38 --> 842.06]  Absolutely right.
[842.16 --> 842.66]  There are no...
[842.66 --> 846.16]  You get all whiny about people not answering your questions, and I answer it.
[846.20 --> 846.86]  And then it's wrong.
[847.68 --> 848.70]  I know you did get it wrong.
[848.70 --> 850.80]  You're not really encouraging people, are you?
[850.90 --> 852.56]  I love when people call Matt out.
[852.66 --> 853.48]  This is great.
[853.68 --> 853.92]  Yeah.
[854.06 --> 855.66]  I've got different feelings in my tummy.
[855.72 --> 855.94]  Yeah, yeah.
[856.14 --> 856.50]  Angelica.
[856.62 --> 857.50]  I want to be on her too.
[857.54 --> 858.70]  Angelica, you're my best friend.
[859.06 --> 859.74]  Oh my gosh.
[859.78 --> 860.48]  I love this.
[861.38 --> 861.74]  Yeah.
[862.04 --> 864.12]  If I go red, it's just lighting.
[864.24 --> 866.44]  It's your coat.
[866.72 --> 867.16]  The jacket.
[867.38 --> 868.04]  The jacket.
[868.34 --> 868.66]  Yes.
[868.90 --> 869.48]  The reflection.
[869.80 --> 869.96]  Yeah.
[869.98 --> 871.08]  It's just a reflection of this.
[871.14 --> 871.90]  It's not anger.
[872.24 --> 872.36]  Yeah.
[872.58 --> 873.78]  You came well prepared, Matt.
[873.86 --> 875.10]  You know your crowds.
[875.28 --> 875.40]  Yeah.
[875.56 --> 876.14]  Yeah, exactly.
[876.26 --> 876.44]  Yeah.
[876.44 --> 877.00]  I do.
[877.16 --> 878.18]  I've made a terrible mistake.
[878.70 --> 879.60]  Okay, Johnny Bortico.
[880.08 --> 883.90]  What if people want to ping you on Twitter and get loads of free advice?
[884.04 --> 884.64]  How would they do it?
[884.68 --> 885.42]  What's your Twitter name?
[885.58 --> 886.66]  Actually, you can just search Google.
[886.84 --> 888.36]  Johnny Golang or Golang Johnny.
[888.52 --> 889.24]  That'll take you to me.
[889.46 --> 892.00]  Oh, that is a cool answer, isn't it?
[892.02 --> 892.76]  I'll do you one better.
[892.92 --> 894.78]  There's many ways of spelling Johnny.
[895.02 --> 895.54]  Yeah, exactly.
[895.70 --> 897.00]  If you do like, I'll do you one better.
[897.40 --> 898.50]  Golangjohnny.com.
[898.54 --> 899.48]  That'll take you to all the places.
[899.48 --> 903.26]  It's much easier than trying to spell out your last name.
[903.30 --> 903.62]  Yeah.
[903.62 --> 903.80]  Yeah.
[903.80 --> 904.08]  Yeah.
[904.08 --> 904.38]  Yeah.
[904.78 --> 905.16]  Yeah.
[905.16 --> 907.80]  It's a lot of unnecessary letters in that last name.
[907.86 --> 909.44]  And it could do with a bit of G-zip on it.
[909.84 --> 910.40]  I know, right?
[910.72 --> 910.90]  Yeah.
[911.02 --> 911.70]  But no, I like it.
[911.80 --> 912.56]  Compress that thing.
[912.96 --> 915.46]  Johnny, what's your favorite color in hex?
[915.82 --> 917.32]  I think I want to answer Angelica's question.
[917.50 --> 918.58]  Oh, for Pete's sake.
[918.76 --> 919.80]  Mine's the blink tag.
[920.14 --> 920.56]  The blink.
[920.56 --> 923.82]  I was hoping for an old school one, like blink or marquee.
[923.92 --> 924.44]  Marquee.
[924.72 --> 924.96]  Yeah.
[925.18 --> 926.20]  I love those tags.
[926.86 --> 927.36]  Oh, dear.
[927.54 --> 929.58]  So you're not going to tell us your favorite color in hex?
[930.16 --> 930.50]  No.
[930.80 --> 931.50]  Okay, fair enough.
[931.96 --> 935.54]  Well, I am partial to 000066.
[935.96 --> 936.32]  Ooh.
[937.24 --> 939.78]  Nice deep, deep blue.
[941.64 --> 942.32]  Very good.
[942.54 --> 943.20]  That's cool, isn't it?
[943.38 --> 947.36]  To non-tech people watching this, that probably looks really impressive, doesn't it?
[947.68 --> 949.44]  I mean, I did wear a shirt.
[949.44 --> 952.54]  Well, although not as deep, but that kind of gave you the hint, right?
[952.66 --> 953.06]  Yeah, it did.
[953.38 --> 955.28]  Let me just get the digital color meter up.
[955.44 --> 959.52]  I just want to check to see what color your shirt actually is in hex.
[959.96 --> 962.88]  Three, two, five, nine, F-E, Johnny, actually.
[963.36 --> 963.98]  Oh, okay.
[964.34 --> 964.54]  Thanks.
[964.64 --> 964.80]  Yeah.
[964.96 --> 965.40]  Thanks for it.
[965.44 --> 965.80]  No problems.
[966.58 --> 966.98]  Okay.
[967.54 --> 968.56]  We've got Mark Bates here too.
[968.68 --> 970.52]  Mark, are you on Twitter?
[971.04 --> 971.50]  I am.
[971.58 --> 975.04]  Can I just say, I am really scared of whatever my question is going to be.
[975.04 --> 980.84]  I am petrified knowing that you're about to ask me a question I've never heard before.
[981.22 --> 982.84]  Anyway, yes, I am on the Twitters.
[983.16 --> 988.74]  I am on the kind of everything's just as Mark Bates, just my full name that's spelt with
[988.74 --> 990.22]  two A's and an R.
[990.34 --> 991.60]  You can put them wherever you like.
[992.76 --> 995.26]  You signed up for all of those combinations of accounts.
[995.26 --> 999.34]  Just a random wild carding of Twitter handles.
[999.54 --> 999.72]  Yes.
[999.80 --> 1000.22]  Very cool.
[1000.28 --> 1005.82]  I did actually used to have a band that our website was catapulttheband.com.
[1005.92 --> 1011.52]  But I eventually had to get catapulttheband.com because of the two T's.
[1011.58 --> 1012.64]  Everybody just kept going.
[1013.06 --> 1013.48]  Yeah.
[1013.60 --> 1016.48]  You don't need two T's, which is why my name only has the one.
[1017.48 --> 1019.16]  No, your question's fine, Mark.
[1019.28 --> 1024.28]  It's simply, what's your favorite security question on signup forms when you have to sort
[1024.28 --> 1024.60]  of choose?
[1025.98 --> 1026.80]  Oh, geez.
[1026.84 --> 1027.48]  That's a great one.
[1027.56 --> 1028.60]  The blank one.
[1028.70 --> 1029.40]  The blank one.
[1029.46 --> 1030.94]  There isn't a blank one, is there?
[1031.42 --> 1031.68]  Yeah.
[1032.06 --> 1034.28]  The good sites let you write in your own question.
[1034.80 --> 1035.00]  Right.
[1035.02 --> 1035.88]  And what do you write in?
[1036.80 --> 1037.78]  And what is the answer?
[1038.00 --> 1040.80]  The question should be, what is your favorite security answer?
[1041.12 --> 1042.62]  What is your favorite security question?
[1042.92 --> 1043.24]  Okay.
[1043.38 --> 1044.30]  Thank you very much.
[1044.30 --> 1046.10]  I like answering them incorrectly.
[1046.42 --> 1048.00]  You have to remember that though, don't you?
[1048.24 --> 1049.06]  Otherwise you're screwed.
[1049.40 --> 1052.26]  You do have to remember that, but nobody's going to guess it, right?
[1052.26 --> 1055.96]  Like there's way more ways to lie than there is to tell the truth.
[1055.96 --> 1056.26]  Right.
[1056.56 --> 1058.70]  So like, what's your grandmother's name?
[1059.02 --> 1059.34]  Kevin.
[1059.68 --> 1062.82]  You know, that was my grandmother's name.
[1062.98 --> 1064.90]  And then you just write it on a piece of paper.
[1065.40 --> 1066.32]  Problem solved.
[1066.40 --> 1066.56]  Yeah.
[1066.64 --> 1068.42]  Mine are all right underneath my keyboard.
[1068.52 --> 1069.36]  Does everyone want to see?
[1069.44 --> 1070.18]  I keep it right here.
[1070.26 --> 1070.68]  Hang on.
[1070.88 --> 1071.70]  Sticking on the monitor.
[1072.00 --> 1072.34]  That works too.
[1072.38 --> 1076.02]  I wrote one password at the top and then I figured that was good enough.
[1076.10 --> 1076.26]  Right.
[1077.20 --> 1080.56]  That is quite secure there, Mark, because no one wants to come around to your house.
[1080.82 --> 1081.52]  That is true.
[1081.88 --> 1082.24]  Goodness.
[1082.90 --> 1083.22]  Goodness.
[1084.04 --> 1086.00]  Even my family doesn't want to spend time with me.
[1086.14 --> 1086.64]  You're right.
[1086.72 --> 1087.66]  That is a very good point.
[1087.98 --> 1088.92]  I'm obviously joking.
[1089.06 --> 1090.14]  Look at his studio he's got.
[1090.20 --> 1091.78]  I definitely want to go and spend time in there.
[1092.26 --> 1095.34]  Now, sometimes the banter will slip over into hate.
[1095.64 --> 1096.80]  And I'm sorry when that happens.
[1096.80 --> 1097.92]  It is an accident.
[1098.08 --> 1098.48]  I mean it.
[1098.68 --> 1102.10]  Honestly, all of it with the utmost love, mostly.
[1103.08 --> 1103.48]  Okay.
[1103.66 --> 1105.04]  Well, let's play.
[1105.14 --> 1105.74]  I think it's time.
[1105.82 --> 1106.72]  We've met the contestants.
[1107.08 --> 1109.04]  They're all a wonderful bunch of lovely people.
[1109.66 --> 1114.36]  Actually, the first thing we're going to do is choose our teams.
[1114.78 --> 1117.30]  Let me share my telly with you.
[1117.66 --> 1119.68]  And I'm using GitHub Codespaces here.
[1119.72 --> 1121.24]  And I've written a little program.
[1122.22 --> 1124.30]  And this essentially, I see the random there.
[1124.30 --> 1126.88]  Look, we've got all the players and little loop.
[1127.34 --> 1128.12]  One to four.
[1128.30 --> 1129.90]  I'm just going to pull out a random player.
[1130.32 --> 1133.00]  And this is like a pure function, Eric, for you.
[1133.32 --> 1135.46]  So, kind of rusty, isn't it?
[1135.90 --> 1136.94]  So, you pass in the players.
[1137.12 --> 1139.58]  We get back the list with the other one removed.
[1140.02 --> 1141.62]  And let's run it and see.
[1142.22 --> 1143.84]  See who's on what team.
[1144.20 --> 1144.44]  Wait.
[1144.52 --> 1149.52]  Why do you need the second loop if you're just getting the left out?
[1149.52 --> 1151.22]  I was waiting for somebody to start debugging this.
[1152.10 --> 1152.82]  Team two.
[1153.12 --> 1155.50]  You're just getting the left four, however.
[1156.30 --> 1156.46]  Yeah.
[1157.02 --> 1157.80]  Oh, man.
[1157.86 --> 1158.64]  I don't get it.
[1158.86 --> 1160.48]  Code review is harsh.
[1160.56 --> 1161.52]  I'm not getting a code review.
[1163.52 --> 1165.36]  She brings up a very good point.
[1165.42 --> 1167.74]  I mean, you really don't need that loop there at all.
[1167.84 --> 1168.52]  Oh, this is great.
[1169.16 --> 1170.40]  This is great for me.
[1170.40 --> 1174.78]  Because it's similar code, if you must know.
[1175.12 --> 1177.60]  And once you've learned the first one, you know what the second one's doing.
[1177.74 --> 1178.00]  All right.
[1178.06 --> 1179.88]  But you don't need the second one.
[1180.22 --> 1181.38]  I mean, I think you need the loop.
[1181.52 --> 1182.30]  You don't need to.
[1182.30 --> 1183.62]  It's highly inefficient and confusing.
[1183.70 --> 1184.96]  I don't think you need half this.
[1185.10 --> 1186.44]  I mean, realistically, you could have.
[1186.44 --> 1187.22]  You don't need to randomize it.
[1187.22 --> 1190.02]  Even if you wanted to call it twice, you could have abstracted it.
[1190.02 --> 1190.26]  Right.
[1190.58 --> 1190.84]  Right.
[1190.92 --> 1192.10]  Just print off the names.
[1192.42 --> 1192.90]  Yeah, Matt.
[1193.00 --> 1193.30]  Excellent.
[1193.56 --> 1195.38]  It could have been even done with a strings joined.
[1195.48 --> 1197.26]  You don't even need the loop for crying out loud.
[1198.10 --> 1198.42]  Goodness.
[1199.18 --> 1199.54]  Excellent.
[1201.18 --> 1203.76]  Well, at least we have our teams from this.
[1203.90 --> 1207.52]  Team one, Eric, Natalie, Mark, and Angelica.
[1208.36 --> 1212.36]  And team two is Brian, Carlicia, Johnny, and Chris.
[1212.88 --> 1213.52]  There we have it.
[1213.52 --> 1216.26]  And if you're not happy with the teams, you can blame Mathran.
[1217.34 --> 1218.58]  Or bad for loops.
[1218.60 --> 1219.54]  Blame Matt Ryer.
[1219.66 --> 1220.28]  Is that what you said?
[1222.16 --> 1224.52]  Sounded like Matt Ryer through my headphones.
[1224.84 --> 1225.72]  Yeah, a little bit.
[1225.78 --> 1225.94]  Yeah.
[1226.10 --> 1229.50]  I mean, I would be honored to have a package named after me in the standard library.
[1229.50 --> 1232.30]  So if that's what we're getting at, then I'm on board.
[1233.02 --> 1234.26]  Let's go for round one.
[1234.44 --> 1240.18]  To decide who's going to have the board, which we'll see in a moment, we're going to have
[1240.18 --> 1241.74]  to do a face-off.
[1241.86 --> 1244.20]  Or if you like puns, an interface-off.
[1244.20 --> 1248.34]  So we'll pick Eric and Brian.
[1248.58 --> 1250.52]  You are two team captains.
[1251.10 --> 1252.80]  You two are going to take part in the face-off.
[1253.02 --> 1254.54]  And we're going to ask the first question.
[1256.48 --> 1257.18]  Let's go.
[1257.18 --> 1262.34]  So this is to figure out who's going to own the board.
[1263.06 --> 1265.16]  What is the least useful Go keyword?
[1265.48 --> 1270.22]  What did our surveyed gophers say was the least useful Go keyword?
[1271.04 --> 1271.72]  Go to.
[1272.62 --> 1273.24]  Hang on.
[1273.36 --> 1274.70]  So let's do panic first.
[1275.22 --> 1278.52]  Brian, so panic is correct.
[1278.60 --> 1279.44]  It's on the board.
[1279.78 --> 1281.64]  Does the naked return have a keyword?
[1281.98 --> 1282.62]  No, right?
[1283.04 --> 1284.56]  Just return, I guess, is it?
[1284.56 --> 1286.36]  Oh, no, no, no.
[1286.42 --> 1287.30]  Return is very useful.
[1289.82 --> 1291.88]  Yeah, return is quite useful, isn't it?
[1292.20 --> 1292.98]  It is, isn't it?
[1293.52 --> 1294.58]  It has its moments.
[1295.00 --> 1295.70]  It does.
[1296.46 --> 1298.24]  Okay, Eric, what was your guess?
[1298.54 --> 1298.88]  Go to.
[1299.24 --> 1299.76]  Go to.
[1300.10 --> 1301.04]  Gophers say?
[1302.56 --> 1303.54]  Top answer.
[1304.44 --> 1307.32]  Okay, so Eric, you got the top answer there.
[1307.42 --> 1309.60]  So your team now controls the board.
[1309.68 --> 1313.08]  We're going to go around your team in order and take guesses.
[1313.08 --> 1314.52]  Remember, you have three lives.
[1314.66 --> 1320.16]  If you lose those three lives, it gives Brian's team the chance to steal.
[1320.86 --> 1323.48]  So, Natalie, let's have your guess, please.
[1323.58 --> 1326.32]  What's the least useful Go keyword, Natalie?
[1326.88 --> 1327.32]  Fall through.
[1327.66 --> 1328.42]  Fall through.
[1328.82 --> 1329.60]  Gophers say?
[1331.50 --> 1332.60]  You're like number four.
[1332.82 --> 1333.26]  Yes.
[1333.50 --> 1334.24]  Oh, number two.
[1334.40 --> 1334.60]  All right.
[1334.70 --> 1335.14]  Yes.
[1335.20 --> 1336.58]  Very, very good guess.
[1337.26 --> 1337.60]  Okay.
[1338.32 --> 1340.06]  We've got lots of points on the scoreboard.
[1340.14 --> 1341.12]  Let's see if we can get some more.
[1341.12 --> 1342.48]  It's Mr. Bates' turn.
[1342.88 --> 1343.24]  Careful.
[1343.54 --> 1345.40]  It's Mark Bates' turn.
[1346.18 --> 1347.28]  Mark, what's your guess?
[1347.40 --> 1348.44]  What's the least useful Go keyword?
[1349.14 --> 1350.72]  I was going to say fall through.
[1350.84 --> 1352.16]  That was my big guess.
[1352.30 --> 1353.62]  What are you going to say now?
[1354.42 --> 1355.98]  Oh, what am I going to say?
[1356.40 --> 1357.36]  Hang on a second.
[1359.14 --> 1360.78]  There's only 24 of them.
[1360.88 --> 1361.46]  There shouldn't be this high.
[1361.46 --> 1362.30]  There's like 25.
[1362.60 --> 1362.86]  25.
[1362.94 --> 1363.46]  I don't know.
[1363.60 --> 1363.82]  Yeah.
[1364.28 --> 1365.86]  But I don't know what they are.
[1367.40 --> 1368.14]  I should.
[1368.14 --> 1369.66]  I teach them all the time.
[1371.82 --> 1372.78]  That's what's so bad.
[1372.88 --> 1375.28]  I'm going to say, is Iota a keyword?
[1375.98 --> 1376.26]  Yeah.
[1376.54 --> 1376.88]  No.
[1377.08 --> 1377.56]  No, no.
[1377.58 --> 1378.26]  It's not a keyword.
[1378.42 --> 1379.72]  So I'm going to say.
[1381.38 --> 1381.82]  Oh, I know.
[1381.98 --> 1382.56]  I have one.
[1382.70 --> 1382.94]  I have one.
[1383.00 --> 1383.68]  Well, you can't tell.
[1383.84 --> 1384.72]  Don't say it.
[1385.00 --> 1385.28]  Sorry.
[1385.70 --> 1386.06]  No.
[1386.30 --> 1387.36]  When is my turn?
[1387.42 --> 1388.02]  I have one.
[1388.32 --> 1393.68]  It's not going to be if you, unless they lose all their lives because Eric won the team,
[1394.18 --> 1394.58]  the board.
[1394.64 --> 1394.88]  All right.
[1394.88 --> 1395.20]  Yeah.
[1395.28 --> 1396.08]  So you're good on this.
[1396.08 --> 1396.80]  I have one.
[1396.94 --> 1398.14]  I think it's a good one.
[1400.64 --> 1402.48]  Mark, can you say a keyword, please, mate?
[1402.58 --> 1402.98]  Yes.
[1403.24 --> 1403.80]  Just say one.
[1404.28 --> 1409.04]  I am going to say what people think is the least useful Go keyword.
[1409.60 --> 1410.52]  I don't agree.
[1410.98 --> 1414.00]  But I'm going to say select.
[1415.06 --> 1415.46]  Select.
[1415.68 --> 1416.74]  And I go for say.
[1417.66 --> 1417.84]  No.
[1417.84 --> 1418.04]  No.
[1418.64 --> 1419.56]  I'm sorry.
[1419.82 --> 1420.12]  No.
[1420.56 --> 1421.22]  Can I go?
[1421.30 --> 1421.68]  Can I go?
[1421.76 --> 1422.04]  No.
[1422.16 --> 1423.14]  They have two more lives.
[1423.52 --> 1423.66]  No.
[1423.74 --> 1427.10]  I'm afraid not, Carly, because we've got rules in this game.
[1427.92 --> 1429.06]  Next up is Angelica.
[1429.50 --> 1432.62]  Angelica, which is the least useful Go keyword?
[1433.28 --> 1433.68]  I don't know.
[1433.76 --> 1435.64]  I find them all pretty useful this stage.
[1435.64 --> 1439.80]  So we've got go to at number one.
[1440.02 --> 1441.50]  35 gophers said that.
[1441.68 --> 1442.90]  Four throughs in at number two.
[1443.08 --> 1444.42]  That's 26 gophers.
[1444.86 --> 1448.06]  And then in the fifth place on the board is panic with five.
[1448.16 --> 1450.80]  So we're looking for spaces three and four now.
[1451.02 --> 1452.54]  What could be in there?
[1452.86 --> 1455.10]  Maybe continue?
[1455.90 --> 1456.42]  Continue.
[1456.82 --> 1457.74]  Gophers say.
[1458.84 --> 1459.32]  No.
[1459.56 --> 1460.02]  No.
[1460.32 --> 1461.02]  I'm sorry.
[1461.24 --> 1462.22]  I gave it a go.
[1462.22 --> 1464.90]  So we've lost two lives.
[1465.14 --> 1466.30]  We're going to loop back round.
[1467.00 --> 1467.46]  You've got two lives.
[1467.46 --> 1467.84]  Can I go?
[1468.30 --> 1468.52]  No.
[1468.72 --> 1469.34]  I'm afraid not.
[1469.90 --> 1471.12]  Why can I go?
[1471.54 --> 1472.92]  I haven't gone yet.
[1472.94 --> 1473.58]  They're turned.
[1473.92 --> 1479.14]  Unless they lose their final life, and then you get a chance to steal.
[1479.32 --> 1481.16]  And then you might be able to steal and win all the points.
[1481.44 --> 1482.56]  So that'll be very exciting.
[1483.40 --> 1484.72]  Okay, Eric, back to you.
[1485.06 --> 1485.84]  Another guess.
[1486.40 --> 1487.62]  I'm going to go with const.
[1488.52 --> 1488.92]  Const?
[1489.56 --> 1489.84]  Yeah.
[1490.24 --> 1490.84]  Go for say.
[1490.84 --> 1492.82]  Oh, no.
[1492.98 --> 1493.36]  I'm sorry.
[1493.42 --> 1493.94]  It's not there.
[1494.24 --> 1495.82]  And you've lost three lives.
[1495.94 --> 1497.54]  I'm trying to think of the ones you used the least.
[1497.92 --> 1500.58]  So now that means team two has a chance to steal.
[1500.66 --> 1501.72]  You're welcome to confer.
[1501.90 --> 1503.86]  So you can just chat amongst each other.
[1504.02 --> 1505.48]  So, Calicia, it's your time to shine.
[1505.68 --> 1505.90]  Wait.
[1506.26 --> 1506.78]  Can I go?
[1506.92 --> 1507.28]  Can I go?
[1507.40 --> 1508.34]  We can confer.
[1508.48 --> 1509.22]  We can confer.
[1509.34 --> 1509.86]  Let's talk.
[1510.06 --> 1510.82]  You have to tell Brian.
[1511.34 --> 1512.02]  Let's confer.
[1512.34 --> 1513.48]  Where are we conferring?
[1513.82 --> 1514.34]  Right here.
[1514.74 --> 1517.06]  It's not like we can steal your answer at this point.
[1517.58 --> 1519.92]  I feel like break should probably be in there somewhere.
[1519.92 --> 1520.76]  No, no, no, no.
[1520.92 --> 1521.68]  Mine is better.
[1521.86 --> 1522.40]  What's yours?
[1522.92 --> 1523.12]  New.
[1523.44 --> 1523.76]  Yep.
[1523.96 --> 1524.86]  New is one of them.
[1525.04 --> 1525.98]  Else is another one.
[1526.08 --> 1528.28]  New isn't a keyword, is it?
[1528.46 --> 1528.72]  No.
[1528.92 --> 1529.60]  Yes, it is.
[1529.74 --> 1531.54]  I don't think panic's a keyword either.
[1531.76 --> 1532.66]  New is not a keyword.
[1532.92 --> 1533.70]  New is not a keyword.
[1533.90 --> 1534.08]  No.
[1534.46 --> 1535.18]  New isn't a keyword.
[1535.32 --> 1536.50]  But also panic's not a keyword.
[1536.62 --> 1537.34]  So I don't know.
[1537.52 --> 1538.62]  Oh, that's true.
[1538.82 --> 1539.52]  That is true.
[1539.78 --> 1540.62]  That is true.
[1540.74 --> 1542.08]  I have to go with import.
[1542.34 --> 1543.72]  New is sort of like a function.
[1544.40 --> 1545.24]  Yeah, it's not a keyword.
[1545.24 --> 1546.34]  This isn't right or wrong.
[1546.50 --> 1548.84]  This is just what the gophers answered.
[1549.38 --> 1549.78]  Import.
[1550.20 --> 1551.72]  We don't need other people's code.
[1551.72 --> 1552.00]  No.
[1552.00 --> 1555.86]  No, my vote is for break.
[1556.14 --> 1556.38]  Okay.
[1556.46 --> 1557.10]  So we got break.
[1557.22 --> 1557.88]  We got new.
[1558.28 --> 1559.38]  And I throw in else.
[1559.76 --> 1560.94]  Oh, else is a good one too.
[1561.04 --> 1561.66]  Those are useful.
[1562.00 --> 1563.32]  You shouldn't put else in your code.
[1563.60 --> 1566.70]  But I think break should probably be because I don't know.
[1567.10 --> 1567.40]  Okay.
[1568.06 --> 1569.24]  So what's your answer then, Brian?
[1569.30 --> 1569.94]  You have to choose.
[1570.32 --> 1573.90]  Hardcore gophers would say else shouldn't exist maybe.
[1574.20 --> 1575.82]  But use break all the time.
[1576.04 --> 1576.70]  It's very common.
[1577.24 --> 1577.38]  Yeah.
[1577.42 --> 1579.64]  Remember, this isn't about right or wrong.
[1579.74 --> 1582.60]  This is what the other gophers have answered to this question.
[1582.66 --> 1584.06]  I mean, clearly this isn't about right or wrong.
[1584.18 --> 1584.84]  Panic is on here.
[1585.22 --> 1585.44]  Right.
[1585.88 --> 1587.08]  Can we look at the list?
[1587.46 --> 1588.66]  Because we're not going to go anywhere.
[1589.78 --> 1590.54]  We don't know.
[1590.54 --> 1591.86]  We narrowed it down.
[1591.94 --> 1594.54]  We just have to pick the last two between new, else, and break.
[1594.70 --> 1596.64]  I think there's more to the list than those.
[1596.74 --> 1597.00]  Pick one.
[1597.40 --> 1597.84]  Final answer.
[1598.12 --> 1598.50]  I need it.
[1598.54 --> 1600.16]  Otherwise, we're just going to move to the next board.
[1600.42 --> 1600.64]  Break?
[1600.82 --> 1601.62]  Should we go with break?
[1601.84 --> 1602.10]  Sorry.
[1602.22 --> 1602.40]  Sorry.
[1602.60 --> 1603.48]  Break and what else?
[1603.56 --> 1604.54]  You just have to only guess.
[1604.64 --> 1604.86]  One.
[1605.02 --> 1606.38]  Your guess is break.
[1606.70 --> 1607.38]  Go for say.
[1607.66 --> 1608.24]  Is it break?
[1609.40 --> 1610.68]  Oh, I'm sorry.
[1610.82 --> 1611.04]  No.
[1611.16 --> 1611.62]  I'm telling you.
[1611.68 --> 1612.42]  New one else.
[1612.64 --> 1613.98]  Let's reveal the board.
[1614.38 --> 1616.22]  Number one, we had go to.
[1616.32 --> 1617.52]  Number two was fall through.
[1617.68 --> 1618.42]  Number three.
[1619.32 --> 1619.72]  No.
[1620.20 --> 1621.10]  It's not a keyword.
[1622.32 --> 1623.60]  I said that.
[1623.74 --> 1624.64]  Do we get the point?
[1624.94 --> 1625.76]  No, Carlycia.
[1625.76 --> 1627.22]  I'm afraid not.
[1627.42 --> 1628.48]  This is fake news.
[1628.62 --> 1629.16]  Number four.
[1629.56 --> 1629.84]  Else.
[1629.84 --> 1630.08]  Boom.
[1630.14 --> 1630.56]  Look at that.
[1630.86 --> 1631.76]  Oh, Johnny.
[1632.02 --> 1632.58]  I told you.
[1632.80 --> 1632.92]  Yeah.
[1633.38 --> 1634.92]  This is, it may be fake news.
[1635.06 --> 1636.44]  This is what the gophers said.
[1636.80 --> 1637.38]  That's the game.
[1637.42 --> 1638.34]  But I guessed it.
[1638.34 --> 1640.14]  I really did spell this out a lot.
[1640.16 --> 1641.14]  I don't understand this game.
[1641.30 --> 1642.58]  I guessed the word though.
[1642.60 --> 1643.24]  But it's wrong.
[1643.24 --> 1647.60]  I know, but I have to take a final answer from your team captain, Brian.
[1647.74 --> 1648.90]  I have to agree with Brian.
[1649.14 --> 1656.08]  Like, unless they were shown a list of keywords, letting them just randomly guess keywords at our functions is.
[1656.08 --> 1659.08]  Why did we choose to play this game with a bunch of pedants?
[1659.26 --> 1661.14]  Like, because they couldn't have said anything.
[1661.64 --> 1661.96]  Like, you know.
[1662.00 --> 1665.90]  Technically, the rules of the game is it's not really what's accurate, right?
[1666.00 --> 1668.08]  It's what do we think most people said.
[1668.24 --> 1668.58]  Exactly.
[1668.86 --> 1669.32]  Oh, goodness.
[1669.32 --> 1670.46]  This is what people said.
[1670.54 --> 1671.40]  We asked them.
[1671.90 --> 1672.74]  This is what they said.
[1672.82 --> 1673.38]  This is the data.
[1673.70 --> 1674.90]  Which people did you ask, Mark?
[1675.52 --> 1677.46]  It's like saying, what's your favorite movie?
[1677.50 --> 1679.18]  And someone says the TV guide.
[1679.22 --> 1680.66]  And you're like, okay, you win.
[1680.66 --> 1684.86]  You know, if we had documentation, we would not have this argument at all.
[1684.92 --> 1685.42]  Just saying.
[1691.06 --> 1694.90]  This episode is brought to you by our friends at Incident.io.
[1695.32 --> 1697.70]  Every software team on the planet has to manage incidents.
[1698.06 --> 1701.52]  And a very large percentage of those teams are using Slack to communicate.
[1701.70 --> 1702.68]  That includes us.
[1703.00 --> 1707.92]  With Incident.io, you can create, manage, and resolve incidents directly inside Slack.
[1708.20 --> 1709.14]  Here's how it works.
[1709.14 --> 1711.46]  Head to Incident.io and sign up for free.
[1711.86 --> 1713.10]  Then add it to your Slack.
[1713.38 --> 1717.14]  From there, you have a brand new Incidents channel where all incidents get announced.
[1717.52 --> 1720.08]  Use the slash incident command to create and manage incidents.
[1720.50 --> 1724.88]  This command lets you share updates, assign roles, set important links, and more.
[1725.20 --> 1727.08]  All without ever leaving the Incident channel.
[1727.50 --> 1730.98]  Each incident gets their own Slack channel plus a high-res dashboard.
[1731.46 --> 1734.94]  Add Incident.io with the entire timeline from report to resolution.
[1735.48 --> 1737.64]  Get everyone on the same page from the moment they join the incident.
[1737.64 --> 1739.54]  And help stakeholders stay in the loop.
[1739.90 --> 1741.44]  Add Incident, ILG, or Slack today.
[1741.60 --> 1745.64]  And prove to yourself and your team that they have everything you need to streamline your incident management.
[1746.10 --> 1748.56]  Learn more and sign up for free at Incident.io.
[1748.82 --> 1749.88]  No credit card required.
[1750.40 --> 1751.82]  Again, Incident.io.
[1751.82 --> 1770.14]  Okay, it's time to go to the next round.
[1770.54 --> 1774.18]  Team 1 bagged themselves 66 delicious points there.
[1774.78 --> 1775.10]  Let's see.
[1775.18 --> 1778.28]  Now we all understand the rules and we're not going to argue about it anymore.
[1778.46 --> 1780.20]  We can go on to round 2.
[1780.20 --> 1781.38]  Aren't I on Team 1?
[1781.70 --> 1783.94]  I have a list here of Team 1.
[1783.98 --> 1784.62]  I don't have the list.
[1784.70 --> 1785.40]  Where is the list?
[1785.52 --> 1786.32]  This is the list.
[1786.66 --> 1787.00]  Oh, great.
[1787.06 --> 1787.38]  I'm winning.
[1787.50 --> 1787.98]  Never mind.
[1788.48 --> 1790.22]  What was your first programming language?
[1790.42 --> 1791.90]  I take back anything I said.
[1791.92 --> 1792.44]  This one's a good one.
[1792.66 --> 1792.90]  Okay.
[1793.02 --> 1795.26]  So we're going to do interface again.
[1795.58 --> 1796.72]  An interface off.
[1797.24 --> 1801.14]  So this time we're going to ask for Natalie and Carlicia.
[1801.66 --> 1805.46]  So Natalie, first of all, what was your first programming language?
[1805.56 --> 1807.64]  What did the Gophers say to this, Natalie?
[1808.22 --> 1808.66]  Python.
[1808.66 --> 1808.86]  Python.
[1809.38 --> 1809.82]  Python.
[1810.44 --> 1811.18]  Gophers say?
[1812.92 --> 1813.36]  Correct.
[1813.92 --> 1815.48]  And let's see where it is on the board.
[1815.74 --> 1818.12]  It's right in the bang in the middle of number 4.
[1818.26 --> 1819.74]  We've got 7 items on the board here.
[1819.82 --> 1820.56]  Number 4 there.
[1820.90 --> 1821.30]  Python.
[1821.70 --> 1826.66]  Carlicia, if you can beat this, that means your team takes the...
[1827.66 --> 1829.18]  Ruby will beat that.
[1829.34 --> 1829.80]  Bring his bag.
[1829.88 --> 1830.10]  Bring his bag.
[1830.12 --> 1831.66]  It's like all the OG Gophers.
[1832.50 --> 1832.76]  Okay.
[1833.30 --> 1833.78]  Ruby.
[1834.04 --> 1834.50]  Let's see.
[1835.08 --> 1835.82]  Gophers say?
[1835.82 --> 1836.30]  No.
[1837.30 --> 1838.72]  Nobody said.
[1839.40 --> 1841.32]  Who answered this survey?
[1841.64 --> 1842.00]  Wow.
[1842.70 --> 1843.36]  Not Ruby.
[1843.52 --> 1844.66]  I guess that makes sense.
[1844.74 --> 1846.60]  This is first programming language.
[1846.82 --> 1847.02]  Yeah.
[1847.02 --> 1847.44]  Yeah.
[1847.44 --> 1847.50]  Yeah.
[1847.50 --> 1847.72]  Yeah.
[1848.16 --> 1848.40]  Okay.
[1848.40 --> 1850.96]  That means Natalie's team takes the board.
[1851.06 --> 1852.02]  That's team 1 again.
[1852.10 --> 1852.52]  But don't worry.
[1852.58 --> 1856.76]  There's always a chance to steal if they lose their three lives.
[1857.48 --> 1857.60]  So.
[1857.86 --> 1858.36]  Stab the steal.
[1858.36 --> 1859.92]  Mark Bates.
[1860.48 --> 1861.16]  What do you think?
[1861.44 --> 1864.92]  I'm going to say most people said JavaScript.
[1865.62 --> 1866.34]  Gophers say?
[1866.44 --> 1866.66]  Yeah.
[1868.38 --> 1868.66]  Oh.
[1868.90 --> 1869.18]  Whoa.
[1870.44 --> 1870.82]  Wow.
[1870.94 --> 1871.58]  This is amazing.
[1871.68 --> 1871.98]  I know.
[1872.10 --> 1873.40]  So you lose a life, unfortunately.
[1873.56 --> 1873.72]  Right?
[1873.78 --> 1874.84]  Like who answered this?
[1875.80 --> 1876.92]  The answers are anonymous.
[1877.30 --> 1879.06]  We have to protect the identities of our sources.
[1879.06 --> 1879.96]  I can hope so.
[1880.02 --> 1881.76]  Because we might have to find them after this show.
[1882.02 --> 1882.24]  Exactly.
[1882.96 --> 1884.56]  We would have to have a conversation.
[1884.56 --> 1885.12]  Okay.
[1885.28 --> 1885.72]  Angelica.
[1886.64 --> 1891.00]  Time for you to have a guess of which programming language was the people's first one.
[1891.26 --> 1892.18]  What would you think it is?
[1892.66 --> 1893.30]  Maybe Go.
[1893.70 --> 1894.10]  Go.
[1894.34 --> 1896.34]  Was my first software engineering language.
[1896.98 --> 1897.30]  Okay.
[1897.48 --> 1898.16]  Go for Say.
[1898.68 --> 1899.12]  Nice.
[1899.90 --> 1900.34]  Really?
[1900.60 --> 1901.00]  No.
[1901.28 --> 1902.12]  Nobody said Go.
[1902.12 --> 1903.84]  I still find this impressive, Angelica.
[1903.92 --> 1904.84]  That's an awesome answer.
[1904.96 --> 1905.92]  Even though it's not here.
[1906.08 --> 1907.48]  How old is this Go community?
[1907.68 --> 1908.00]  Come on.
[1909.08 --> 1910.46]  We don't have the demographic.
[1910.46 --> 1914.18]  There was some really old stuff in there, like Lisp or something.
[1914.18 --> 1914.66]  Yeah.
[1915.06 --> 1916.22]  We'll get it next time, guys.
[1916.48 --> 1917.28]  Eric, your turn.
[1917.68 --> 1918.02]  Come on.
[1918.14 --> 1918.86]  Let's get some points.
[1919.08 --> 1920.44]  This one has to be on there.
[1920.84 --> 1922.16]  C is going to be on there.
[1922.76 --> 1923.20]  Okay.
[1923.28 --> 1923.68]  Let's see.
[1923.72 --> 1923.92]  Yeah.
[1923.98 --> 1924.62]  That's got to be there.
[1924.90 --> 1925.46]  Go for Say.
[1927.48 --> 1927.88]  Yes.
[1928.54 --> 1929.98]  And it's at number three.
[1930.12 --> 1930.48]  Oh.
[1930.78 --> 1935.32]  So with 11 of our surveyed Gophers said C.
[1935.60 --> 1937.40]  You have a life remaining.
[1938.66 --> 1939.94]  So let's go.
[1940.04 --> 1941.32]  Natalie, it's your turn again.
[1941.60 --> 1942.12]  Pick a language.
[1942.24 --> 1942.60]  Be careful.
[1942.74 --> 1943.44]  One life left.
[1943.44 --> 1944.44]  Pascal.
[1944.92 --> 1945.36]  Pascal.
[1945.66 --> 1946.02]  Pascal.
[1946.28 --> 1946.90]  Go for Say.
[1947.26 --> 1947.66]  Pascal.
[1949.16 --> 1950.34]  Yes, it's on there.
[1950.52 --> 1950.82]  What?
[1951.16 --> 1951.40]  Wow.
[1951.40 --> 1951.68]  What?
[1952.06 --> 1953.42]  That was my first programming language.
[1953.42 --> 1954.04]  Number two.
[1954.44 --> 1954.84]  Wow.
[1955.12 --> 1955.84]  What on earth?
[1956.22 --> 1956.56]  Wow.
[1956.70 --> 1956.92]  Okay.
[1957.24 --> 1957.62]  Wow.
[1957.90 --> 1958.32]  All right.
[1958.50 --> 1959.98]  It's not going where I expected.
[1960.44 --> 1961.40]  Yeah, this is amazing.
[1961.68 --> 1963.68]  So now you get an idea who answered this question.
[1964.20 --> 1964.96]  Yeah, yeah.
[1965.02 --> 1965.72]  I didn't answer.
[1965.98 --> 1966.50]  Okay, Mark.
[1966.58 --> 1967.32]  Background to you.
[1967.32 --> 1968.14]  Okay.
[1968.32 --> 1973.18]  I'm going to go with one of my first languages, which is now a big enterprise language, but
[1973.18 --> 1975.20]  they teach it in schools all the time.
[1975.20 --> 1977.72]  I'm going to say, show me Java.
[1978.34 --> 1978.80]  Yes.
[1979.14 --> 1979.44]  Definitely.
[1979.58 --> 1980.22]  Go for Say.
[1981.68 --> 1982.96]  Yes, indeed.
[1982.96 --> 1984.16]  Probably number one or something.
[1984.30 --> 1984.46]  Yeah.
[1984.74 --> 1985.22]  Let's see.
[1985.76 --> 1987.12]  It's at number six.
[1987.30 --> 1988.22]  Oh, wow.
[1988.36 --> 1990.76]  Yeah, just seven people started with Java.
[1990.76 --> 1991.10]  Okay.
[1991.38 --> 1991.72]  Okay.
[1991.90 --> 1993.74]  So I know what number one is.
[1993.90 --> 1994.76]  I can tell.
[1995.00 --> 1995.86]  I think I know too.
[1996.10 --> 1996.52]  Hold on.
[1996.62 --> 1998.70]  Because before that, it's Angelica.
[1999.26 --> 1999.82]  It's your turn.
[2000.12 --> 2001.32]  They all know what it is.
[2001.36 --> 2002.04]  I don't.
[2003.08 --> 2004.18]  Well, it's your turn.
[2004.28 --> 2005.52]  There's no conferring, remember?
[2006.04 --> 2006.34]  Okay.
[2006.42 --> 2008.38]  Maybe just like Morse code me with winks.
[2008.72 --> 2009.80]  Beep, beep, beep, beep, beep, beep, beep.
[2009.88 --> 2011.22]  It means get a move on, please.
[2011.58 --> 2013.48]  Just let me take my time, Matt.
[2013.64 --> 2015.78]  No, we haven't really got time because of all the bants.
[2015.98 --> 2016.38]  Goodness.
[2016.60 --> 2017.80]  Well, that's your fault, isn't it?
[2020.84 --> 2022.38]  I'm glad she's on my team.
[2022.64 --> 2023.00]  I'm glad.
[2023.00 --> 2025.24]  The thing is, in that accent, it sounds really authentic.
[2026.10 --> 2030.58]  Let's go with, well, given the tone, maybe Scarla?
[2030.98 --> 2031.46]  Scarla.
[2031.64 --> 2032.32]  Go for Say.
[2033.86 --> 2034.26]  No.
[2034.26 --> 2034.58]  No.
[2034.96 --> 2037.36]  And that's, unfortunately, your live's over.
[2037.46 --> 2038.18]  But don't worry.
[2038.92 --> 2042.44]  Team two, it's your opportunity to steal now.
[2042.64 --> 2044.02]  We just need one correct answer.
[2044.14 --> 2046.14]  And you take all of the points.
[2046.22 --> 2047.00]  You gobble them all up.
[2047.08 --> 2047.94]  You eat all the points.
[2048.00 --> 2048.54]  You take them all.
[2048.76 --> 2050.06]  I think I know which one it is.
[2050.12 --> 2051.06]  My vote is for basic.
[2051.54 --> 2052.60]  No, don't say basic.
[2053.02 --> 2053.22]  No.
[2053.30 --> 2053.80]  Let's confer.
[2054.08 --> 2054.60]  That's my vote.
[2054.60 --> 2055.56]  We're conferring.
[2055.68 --> 2056.14]  We're conferring.
[2056.16 --> 2056.54]  Let's confer.
[2056.80 --> 2057.98]  Can I say what I think it is?
[2058.02 --> 2058.28]  You can.
[2058.38 --> 2059.00]  What do you think it is?
[2059.00 --> 2059.42]  Well, yeah.
[2059.50 --> 2060.20]  Well, we're conferring.
[2060.26 --> 2061.24]  This is not our official answer.
[2061.46 --> 2061.54]  Yeah.
[2061.68 --> 2063.06]  It's PHP, in my opinion.
[2063.24 --> 2064.04]  I was going to say that.
[2064.04 --> 2065.58]  I'm sure PHP is on there, too.
[2065.70 --> 2066.28]  I can see that.
[2066.44 --> 2067.74]  But I bet basic's on the top.
[2068.06 --> 2068.38]  Totally.
[2068.88 --> 2069.18]  All right.
[2069.30 --> 2070.02]  I think we agree.
[2070.12 --> 2070.36]  PHP.
[2070.60 --> 2070.82]  Yeah.
[2071.04 --> 2071.62]  We don't agree.
[2072.02 --> 2073.48]  Brian, I have to take it from the team captain.
[2073.60 --> 2073.78]  Brian.
[2074.18 --> 2075.20]  I'm not the team captain.
[2075.36 --> 2075.60]  You are.
[2075.60 --> 2077.20]  Who made Brian the team captain?
[2077.40 --> 2078.10]  Came out first.
[2078.96 --> 2080.00]  I think it's Carlisha.
[2080.26 --> 2081.20]  Carlisha's the team captain.
[2082.48 --> 2083.34]  It's two to one.
[2083.40 --> 2084.12]  They say PHP.
[2084.12 --> 2085.48]  So let's go with PHP.
[2085.96 --> 2086.30]  Okay.
[2086.60 --> 2087.00]  PHP.
[2087.42 --> 2088.12]  Go for say.
[2089.88 --> 2090.28]  Yes.
[2090.28 --> 2092.58]  You do it and you steal the points.
[2092.74 --> 2096.94]  It was at number five there with nine people starting with PHP.
[2097.24 --> 2097.46]  Okay.
[2097.52 --> 2100.84]  I think number one is going to be one of those things like this is not a language.
[2101.04 --> 2101.76]  It's going to be basic.
[2102.02 --> 2102.56]  It's basic.
[2103.02 --> 2104.68]  It's going to be YAML.
[2104.68 --> 2105.20]  Let's see.
[2105.24 --> 2105.50]  What was it?
[2105.58 --> 2107.40]  Number seven for TML.
[2107.90 --> 2108.76]  Better than basic.
[2109.28 --> 2110.90]  I'm out of here for TML.
[2111.04 --> 2111.40]  Boom.
[2111.74 --> 2111.88]  Wow.
[2112.08 --> 2114.16]  I knew it was going to be basic with this theme.
[2114.62 --> 2115.02]  Yeah.
[2115.40 --> 2115.62]  Yeah.
[2115.94 --> 2117.28]  Basic at number one.
[2117.38 --> 2118.34]  Pascal and stuff.
[2118.44 --> 2119.38]  I mean, who says Pascal?
[2119.54 --> 2120.44]  Unless you've done basic.
[2121.64 --> 2124.70]  Basic, Pascal, C, Python, PHP, Java.
[2124.70 --> 2127.66]  And at number seven was C++.
[2128.40 --> 2129.32]  That's not a language.
[2131.64 --> 2132.36]  Shots fired.
[2132.36 --> 2134.82]  I don't think etc is a language either.
[2134.98 --> 2135.24]  Yeah.
[2135.40 --> 2135.68]  What?
[2136.70 --> 2137.32]  Probably is.
[2137.62 --> 2138.26]  Et cetera.
[2138.80 --> 2141.46]  Well, we said a bunch of stuff that could fall into etc.
[2141.70 --> 2142.42]  Why didn't we get it?
[2142.42 --> 2142.70]  Right?
[2142.98 --> 2143.16]  Yeah.
[2143.16 --> 2143.56]  JavaScript.
[2143.80 --> 2144.68]  That falls under etc.
[2144.84 --> 2145.24]  Come on.
[2145.84 --> 2147.94]  JavaScript didn't get enough to make it to the board.
[2148.02 --> 2150.44]  Any with five answers or less don't make it on the board.
[2150.56 --> 2151.38]  JavaScript had two.
[2151.50 --> 2152.50]  C Sharp had three.
[2152.72 --> 2156.12]  And actually, believe it or not, ActionScript had three.
[2156.32 --> 2156.68]  Also.
[2156.96 --> 2157.38]  Very interesting.
[2157.38 --> 2157.78]  Nice.
[2157.78 --> 2158.14]  Wow.
[2158.50 --> 2160.84]  This crowd's doing old than this survey.
[2161.10 --> 2161.32]  Yeah.
[2161.32 --> 2162.14]  This is an older crowd.
[2162.14 --> 2162.66]  For sure.
[2162.76 --> 2164.82]  So that tells us a lot about future questions.
[2165.24 --> 2165.52]  Yeah.
[2165.82 --> 2166.08]  Yeah.
[2166.16 --> 2166.76]  I think so.
[2167.54 --> 2172.06]  Well, speaking of which, let's move on to round three.
[2173.98 --> 2174.46]  Jazz.
[2175.60 --> 2175.96]  Okay.
[2176.40 --> 2176.68]  Oh.
[2176.80 --> 2177.74]  The question is.
[2177.74 --> 2178.28]  Oh.
[2178.28 --> 2178.58]  Oh.
[2179.58 --> 2183.24]  Which IDE are you most productive in?
[2183.44 --> 2183.68]  All right.
[2183.74 --> 2184.88]  So let's be clear here.
[2184.92 --> 2186.20]  We're not talking about a text editor.
[2186.32 --> 2187.40]  We're talking about an IDE.
[2187.72 --> 2188.64]  Full-blown IDE.
[2189.00 --> 2189.20]  Yes.
[2189.38 --> 2190.16]  No, Johnny.
[2190.16 --> 2193.48]  You can't ask the people who answered the question this.
[2193.48 --> 2193.88]  Yeah.
[2194.04 --> 2197.28]  I don't think the community is going to distinguish the two of them.
[2197.28 --> 2197.58]  Yeah.
[2197.76 --> 2198.08]  Yeah.
[2198.08 --> 2198.44]  Maybe not.
[2198.46 --> 2200.66]  Once again, panic is not a keyword and neither is new.
[2201.18 --> 2201.20]  Like.
[2201.50 --> 2201.78]  Yeah.
[2202.20 --> 2202.64]  Johnny.
[2202.80 --> 2203.82]  These are people like me.
[2203.82 --> 2204.74]  It's also not an IDE.
[2204.90 --> 2206.86]  Who don't know what keywords are.
[2207.48 --> 2207.84]  Like me.
[2207.94 --> 2210.64]  Let's watch what we're saying about our listeners, please.
[2210.72 --> 2210.98]  No.
[2211.02 --> 2211.58]  Like me.
[2211.82 --> 2212.08]  I say.
[2212.08 --> 2213.44]  They're all really awesome people.
[2213.88 --> 2214.88]  They are like me.
[2215.04 --> 2217.68]  And they would think like things that are not keywords are keywords.
[2218.10 --> 2224.10]  Well, it's time anyway for the inter-face-off between Mark Bates and Johnny Borsico.
[2224.58 --> 2226.40]  Step to the podium, please, gentlemen.
[2226.72 --> 2227.32]  Metaphorically.
[2227.54 --> 2227.80]  Bring it.
[2228.14 --> 2228.46]  Okay.
[2228.62 --> 2229.74]  Mark, first of all.
[2229.94 --> 2234.10]  I'm going to go with the, well, it might not be my first choice.
[2234.10 --> 2236.82]  The incredibly popular VS Code.
[2237.26 --> 2238.36]  A gophers say?
[2240.02 --> 2240.42]  Yes.
[2240.66 --> 2242.18]  And it's in at number one.
[2242.38 --> 2247.58]  44 people out of our hundred gophers surveyed said VS Code.
[2248.34 --> 2249.62]  And it's the one I use, actually.
[2250.08 --> 2252.26]  Mark, because you're at number one, Johnny, I'm sorry.
[2252.36 --> 2253.06]  Go and sit down.
[2253.14 --> 2254.44]  You don't get to compete.
[2254.56 --> 2255.80]  No, he did it.
[2255.82 --> 2257.18]  He got the top answer there.
[2257.26 --> 2258.54]  44 with VS Code.
[2258.66 --> 2259.94]  Oh, it's too easy of an answer.
[2260.06 --> 2260.94]  Well, there we go.
[2261.16 --> 2261.68]  That was.
[2261.76 --> 2262.26]  That was.
[2262.28 --> 2263.22]  That was a really good one.
[2263.22 --> 2264.06]  I like this question.
[2264.18 --> 2265.16]  We should have more like this.
[2265.28 --> 2268.14]  Well, I know one number two is if anybody's wondering.
[2268.26 --> 2269.04]  Can we see the list, though?
[2269.10 --> 2269.72]  Can we see the full list?
[2269.84 --> 2270.86]  I think Vim's on there.
[2270.98 --> 2272.40]  Hold on, because we're still going to play the game.
[2272.50 --> 2274.28]  Johnny, why are you telling them?
[2274.38 --> 2275.36]  Don't give them ideas.
[2275.76 --> 2277.08]  You still have a chance to steal.
[2277.16 --> 2279.08]  We have to go through the rest of the list, Johnny.
[2279.30 --> 2281.28]  Well, it's not like y'all are going to guess that.
[2281.44 --> 2281.62]  I mean.
[2281.74 --> 2281.96]  It's fine.
[2283.12 --> 2284.76]  I've never heard of Vim before.
[2284.88 --> 2285.48]  What is that?
[2285.84 --> 2289.38]  And there's a couple people on here who are like old school Vim users.
[2289.38 --> 2293.10]  So I don't think nobody's surprised by it.
[2293.30 --> 2295.94]  Okay, Angelica, it's your turn to have a guess.
[2296.16 --> 2297.24]  This is really difficult.
[2297.64 --> 2299.00]  I think I'm going to go with Vim.
[2300.68 --> 2302.00]  That's going to be number two.
[2302.30 --> 2303.22]  Okay, Vim.
[2303.34 --> 2304.00]  Go for say.
[2304.00 --> 2304.32]  Correct.
[2305.52 --> 2305.88]  Correct.
[2306.42 --> 2308.50]  And it is, in fact, number three.
[2308.68 --> 2309.60]  Ooh, Neo Vim.
[2309.78 --> 2311.04]  Vim or Neo Vim.
[2311.18 --> 2312.58]  Got nine people saying that.
[2312.90 --> 2313.60]  Very interesting.
[2313.96 --> 2317.58]  So we still have option two to guess, four and five.
[2317.66 --> 2318.62]  Let's see if we can do it.
[2318.68 --> 2319.56]  You have three lives.
[2319.96 --> 2321.20]  Eric, what do you think?
[2321.48 --> 2324.00]  All right, I'm going to go with Emacs here, too.
[2324.18 --> 2324.92]  Emacs, baby.
[2325.16 --> 2325.82]  Go for say.
[2327.40 --> 2327.80]  Yes.
[2328.28 --> 2329.06]  On a roll.
[2329.24 --> 2330.74]  At number five.
[2331.12 --> 2331.50]  Can I go?
[2331.58 --> 2331.88]  Can I go?
[2331.88 --> 2331.94]  Can I go?
[2331.94 --> 2333.26]  Carlissian.
[2333.76 --> 2335.64]  Carlissian, how about I tell you when it's your turn?
[2335.92 --> 2336.88]  We'll do that system.
[2337.16 --> 2339.56]  If Carlissian wants to give our team points, I think it's fine.
[2339.90 --> 2340.14]  Sure.
[2340.24 --> 2341.12]  What was your idea?
[2341.28 --> 2342.26]  Just out of curiosity.
[2342.86 --> 2343.74]  Yeah, do last night.
[2343.92 --> 2344.60]  Can I say it?
[2344.66 --> 2345.12]  No, no, no.
[2345.14 --> 2345.46]  No.
[2345.84 --> 2347.06]  It's not her turn yet.
[2347.32 --> 2349.18]  It's Natalie's turn first.
[2349.50 --> 2350.84]  So, Natalie, what do you think?
[2351.04 --> 2354.30]  We may be thinking of the same thing, Carlissian, but IntelliJ.
[2354.66 --> 2356.66]  I was not thinking that, but that's a good one.
[2357.40 --> 2357.72]  IntelliJ.
[2358.38 --> 2359.00]  Go for say.
[2360.48 --> 2360.88]  Yeah.
[2360.88 --> 2363.60]  At number four there, IntelliJ.
[2364.04 --> 2364.40]  Yes.
[2364.58 --> 2365.38]  With six people.
[2365.72 --> 2366.08]  Can I go?
[2366.12 --> 2366.50]  Can I go now?
[2366.52 --> 2366.88]  No.
[2367.14 --> 2367.58]  I'm afraid not.
[2367.84 --> 2368.58]  Darn it.
[2368.86 --> 2369.50]  Yeah, I know.
[2369.58 --> 2370.54]  It's frustrating, isn't it?
[2370.56 --> 2372.26]  But it is always the same rules.
[2372.80 --> 2376.34]  So, in fact, that means it's back to Mark Bates.
[2376.64 --> 2377.80]  Who's going to now have his guess?
[2377.80 --> 2378.04]  Mark.
[2378.18 --> 2379.36]  I know the answer, Mark.
[2379.48 --> 2380.00]  I know the answer.
[2380.02 --> 2381.14]  You want to tell me what it is?
[2381.32 --> 2381.68]  No.
[2381.82 --> 2382.90]  You have three lines.
[2382.90 --> 2383.90]  You can text it to me.
[2383.96 --> 2384.78]  You have my number.
[2384.90 --> 2385.50]  Go for it.
[2386.16 --> 2386.74]  I'll wait.
[2386.94 --> 2387.44]  I got a minute.
[2387.44 --> 2388.36]  Bates, you don't have a minute.
[2388.36 --> 2388.86]  Can I do that?
[2389.10 --> 2389.74]  Can I do that?
[2389.74 --> 2392.92]  Well, apparently, Carlicia does not want to win the game.
[2392.94 --> 2395.46]  You know you're on different teams, right, Carlicia?
[2395.68 --> 2398.12]  I wasn't listening when the rules were being explained.
[2398.74 --> 2400.06]  And now we're all paying the price.
[2400.26 --> 2402.36]  You're not supposed to give the other team the answers.
[2402.48 --> 2403.48]  That's the first rule.
[2403.82 --> 2405.84]  There are two teams and you're not on Mark's.
[2406.04 --> 2407.22]  Oh, Mark is not on my team.
[2407.34 --> 2408.08]  No, I'm afraid not.
[2408.08 --> 2408.40]  No.
[2409.20 --> 2410.10]  Not this time.
[2410.10 --> 2410.44]  I'm sorry.
[2411.12 --> 2412.30]  I have to go look it up.
[2412.36 --> 2412.70]  Hold on.
[2412.84 --> 2413.36]  I'll be right back.
[2413.46 --> 2414.48]  That's not for Mark, though.
[2414.56 --> 2415.52]  I wrote it on paper.
[2415.68 --> 2416.28]  That helps.
[2416.68 --> 2419.18]  I'm sorry for my bad handwriting, but here's the list.
[2419.30 --> 2420.16]  Maybe it's off a mirror.
[2420.68 --> 2426.30]  I swear I asked somebody to put the list in Slack or Zoom earlier so we can avoid this confusion.
[2426.58 --> 2427.02]  But, you know.
[2427.24 --> 2428.24]  Anyway, it's my turn.
[2428.24 --> 2432.22]  So I am going to go with Goland.
[2432.36 --> 2432.68]  Goland.
[2433.02 --> 2433.48]  Let's see.
[2433.58 --> 2434.06]  Go for Say.
[2436.58 --> 2437.14]  Correct.
[2437.88 --> 2438.24]  Indeed.
[2438.40 --> 2441.16]  And you win the round and you win the points.
[2441.86 --> 2444.30]  Did we really separate Goland and IntelliJ?
[2444.80 --> 2447.14]  I thought IntelliJ was the same as Goland.
[2447.20 --> 2447.42]  Yeah.
[2447.42 --> 2448.70]  Why are those two separate?
[2448.82 --> 2449.18]  They are.
[2449.28 --> 2450.32]  I thought they were the same.
[2450.34 --> 2452.40]  Because they're two separate products by IntelliJ.
[2452.50 --> 2453.06]  I know, right?
[2453.12 --> 2454.78]  Why is new a keyword now?
[2454.88 --> 2455.36]  Who knows?
[2455.36 --> 2457.14]  Vim and NeoVim are together.
[2457.14 --> 2459.22]  And those are two separate things.
[2459.36 --> 2460.08]  So listen, listen.
[2460.48 --> 2461.60]  It's not what we think.
[2461.70 --> 2462.68]  It's what everybody else thinks.
[2462.76 --> 2463.42]  It's not what we think.
[2463.54 --> 2463.76]  Okay.
[2464.36 --> 2467.36]  Team 1 has 161 points.
[2467.74 --> 2471.86]  Team 2 is trailing with 47, but it's all still to play for.
[2471.98 --> 2473.42]  We set out for Family Feud.
[2473.50 --> 2474.44]  We got Jerry Springer.
[2475.26 --> 2477.44]  I was going to say Sublime, by the way.
[2477.46 --> 2479.24]  Oh, that's a good guess.
[2479.44 --> 2481.02]  Yeah, we did get a few other mentions.
[2481.02 --> 2485.48]  We had Sublime Text, TextEdit, the Unix Shell, and, quote,
[2485.48 --> 2487.96]  a wet piece of string.
[2489.46 --> 2489.82]  What?
[2490.66 --> 2493.76]  You had me a Unix Shell, but a wet piece of string.
[2493.92 --> 2494.68]  Oh, wait a minute.
[2494.78 --> 2495.94]  I was in that survey.
[2496.44 --> 2500.14]  I'll throw in, you know, a shout out to my Notepad++, you know,
[2500.20 --> 2500.98]  folks out there.
[2501.14 --> 2502.54]  And just, you know, just shout out to you.
[2502.72 --> 2502.90]  Yeah.
[2503.02 --> 2505.42]  I want to watch whoever it is that's using the Unix Shell.
[2505.42 --> 2509.40]  Is this just, like, echoing strings and concatting a file continuously?
[2509.72 --> 2512.32]  And then said to update it?
[2512.44 --> 2512.94]  Must be.
[2512.94 --> 2515.14]  I want to see what this workflow looks like.
[2515.24 --> 2516.20]  I like stream editors.
[2516.54 --> 2517.50]  Forget this IDE stuff.
[2517.80 --> 2518.82]  Those people are wizards.
[2519.22 --> 2519.70]  Or witches.
[2520.16 --> 2521.96]  I have a question about the rules.
[2522.08 --> 2525.44]  Is Team 1, do they always get to guess first in the face-off?
[2526.10 --> 2529.34]  Because we won the last round, but Team 1 guessed first.
[2529.40 --> 2530.10]  That's true.
[2530.34 --> 2531.24]  It's a fair point.
[2531.48 --> 2533.78]  Yeah, we don't have, I didn't randomize the seed, did I?
[2534.02 --> 2535.02]  Matt, bad host.
[2535.18 --> 2536.42]  We'll make sure we make up for it.
[2536.42 --> 2540.54]  In our next round, which is round four.
[2542.94 --> 2544.60]  Okay, round four.
[2544.96 --> 2551.40]  And we want to bring to the head-to-head now is going to be Chris and Angelica.
[2551.58 --> 2552.98]  Come to the podium, please.
[2553.34 --> 2554.10]  Wait, what?
[2554.80 --> 2556.16]  What is this question?
[2557.28 --> 2557.88]  Oh, I know.
[2558.10 --> 2563.96]  Okay, so this is like, in text speak, which text abbreviation do you use the most?
[2564.20 --> 2564.78]  And Chris...
[2564.78 --> 2565.70]  Wait a minute, wait a minute, wait a minute.
[2565.70 --> 2568.40]  That was not an answer to, that was not an explanation.
[2568.56 --> 2568.86]  All right.
[2569.04 --> 2572.02]  You gave us a GoDoc standard library answer.
[2572.18 --> 2574.92]  You used the same words five times at the end of the sentence.
[2575.02 --> 2576.88]  What's the context for this question?
[2577.48 --> 2580.40]  Okay, what were the changelog people drinking when they did this?
[2582.38 --> 2582.78]  LOL.
[2583.42 --> 2583.76]  You guys.
[2583.76 --> 2584.64]  Does that count?
[2585.24 --> 2589.66]  In text speak, when abbreviating, what's your favorite text abbreviation?
[2589.78 --> 2590.92]  What does that mean?
[2591.00 --> 2592.38]  What does that have to do with Go?
[2592.38 --> 2595.56]  Is it like when I'm texting?
[2595.92 --> 2596.54]  Let me explain.
[2596.56 --> 2597.36]  When I'm sexting?
[2598.00 --> 2598.22]  What?
[2599.12 --> 2601.04]  Wow, those are very different messages.
[2601.28 --> 2602.54]  You want to make sure you don't...
[2602.54 --> 2603.60]  I need to know more.
[2603.90 --> 2605.72]  I need more information.
[2606.10 --> 2606.92]  What does this mean?
[2607.30 --> 2608.00]  Peach emoji.
[2608.22 --> 2609.40]  This is not about Go.
[2610.40 --> 2612.98]  Look, let me explain this because this is...
[2612.98 --> 2616.90]  I think the crux of this, which I think is escaping a few of us a little bit.
[2617.44 --> 2619.00]  This is the question that was asked.
[2619.20 --> 2620.90]  We've collected the answers and counted them.
[2620.90 --> 2622.96]  What did people say when they were asked this question?
[2623.16 --> 2624.18]  It's as simple as that.
[2624.74 --> 2625.36]  It's as simple as that.
[2625.36 --> 2625.96]  Oh, Lord.
[2626.24 --> 2626.86]  I'm ready.
[2627.06 --> 2627.54]  I've got one.
[2627.54 --> 2629.22]  Chris, we're going to go first to Chris.
[2629.24 --> 2629.66]  I'm ready.
[2630.10 --> 2631.14]  Chris, what's your guess?
[2631.50 --> 2632.62]  I don't know the context.
[2632.94 --> 2636.94]  Is this like abbreviations in Go code or abbreviations in general?
[2637.26 --> 2638.68]  In text speak, when you're texting.
[2638.96 --> 2641.28]  I don't think we gave the people...
[2641.28 --> 2642.96]  In text speak, abbreviations.
[2643.08 --> 2645.42]  What are the text abbreviations in text abbreviation?
[2645.50 --> 2648.62]  Text speak, they'd abbreviate the most text abbreviation.
[2648.62 --> 2649.62]  Yeah, exactly.
[2649.92 --> 2651.38]  How is that not clear?
[2651.80 --> 2656.46]  I think we just have to guess how we think people interpreted this because...
[2656.46 --> 2657.20]  Oh, God.
[2659.02 --> 2660.08]  What do you think, Chris?
[2660.58 --> 2661.24]  I don't know.
[2661.26 --> 2663.30]  I'll just go with like the most generic one.
[2663.40 --> 2663.72]  LOL.
[2664.38 --> 2664.72]  LOL.
[2665.02 --> 2665.62]  Go for say.
[2666.94 --> 2667.42]  Yeah.
[2667.68 --> 2668.12]  There you go.
[2668.34 --> 2668.92]  There you go.
[2669.08 --> 2670.96]  And it's the top answer, which means...
[2670.96 --> 2671.04]  Really?
[2671.04 --> 2671.70]  There we go.
[2671.82 --> 2674.00]  Team two takes the board.
[2674.56 --> 2675.84]  You're in control of the board now.
[2675.84 --> 2677.48]  So we're going to go through the team.
[2677.54 --> 2678.22]  This is going to be good.
[2678.42 --> 2679.66]  So, Brian, you're up next.
[2680.22 --> 2680.88]  What's your guess?
[2681.10 --> 2683.16]  Which text abbreviation do you use the most?
[2683.82 --> 2684.78]  B-R-B.
[2684.92 --> 2685.24]  Boom.
[2685.88 --> 2686.94]  B-R-B.
[2687.24 --> 2687.90]  Go for say.
[2689.12 --> 2689.78]  Oh, what?
[2690.08 --> 2690.24]  What?
[2690.68 --> 2691.60]  Who are these people?
[2691.96 --> 2694.34]  They're people that don't leave for a little short while.
[2694.60 --> 2695.10]  That's who they are.
[2695.96 --> 2696.26]  Okay.
[2696.42 --> 2696.84]  Don't worry.
[2696.94 --> 2698.74]  You've just lost a life, but two lives left.
[2699.00 --> 2699.30]  Colicia!
[2700.22 --> 2700.94]  It's time!
[2701.50 --> 2702.18]  It's your guess.
[2702.18 --> 2702.78]  Okay.
[2702.94 --> 2708.62]  If R-L-O-L shows up on this board, I'm going to be mad because they should go together with L-O-L.
[2708.72 --> 2709.64]  So now I don't know.
[2711.42 --> 2713.22]  Usually you're desperate to guess an answer.
[2713.40 --> 2713.72]  Come on.
[2714.40 --> 2718.26]  I was thinking either L-G-T-M or K-A-T-S.
[2718.60 --> 2719.90]  We can confer if you'd like.
[2720.20 --> 2720.80]  You can't.
[2721.26 --> 2721.66]  We cannot?
[2721.88 --> 2723.44]  No, you can't confer until they're stealing.
[2723.56 --> 2723.76]  Wow.
[2724.46 --> 2725.54]  These rules, man.
[2726.80 --> 2727.26]  I know.
[2728.08 --> 2728.72]  I know.
[2729.20 --> 2730.42]  All right, Colicia, what do you think?
[2730.76 --> 2731.50]  What's your guess?
[2732.32 --> 2734.68]  Rolling on the floor laughing or L-O-L.
[2734.88 --> 2737.42]  So I'm just going to expect that that's in there.
[2737.64 --> 2738.36]  R-O-F-L.
[2738.50 --> 2739.04]  Go for say.
[2740.34 --> 2741.46]  No, I'm sorry.
[2741.64 --> 2742.50]  Nobody said that.
[2742.76 --> 2744.78]  I think the safest one is L-G-T-M.
[2744.90 --> 2746.00]  Nobody said that.
[2746.12 --> 2746.98]  Who are these people?
[2747.10 --> 2748.60]  The top answer only has 10.
[2748.84 --> 2750.20]  So nobody said that.
[2751.10 --> 2753.24]  I don't think I've ever typed that in my life.
[2753.72 --> 2754.12]  L-O-L?
[2754.24 --> 2754.56]  Raffle?
[2754.84 --> 2755.08]  Really?
[2755.08 --> 2756.90]  No, the rolling on the floor laughing.
[2757.06 --> 2757.98]  Yeah, nothing's ever made it.
[2757.98 --> 2759.72]  Does anybody remember the Rafflecopter?
[2760.22 --> 2760.46]  Mm-hmm.
[2760.46 --> 2761.38]  Rafflecopter.
[2761.70 --> 2762.04]  Yeah.
[2762.54 --> 2763.04]  What is it?
[2763.28 --> 2764.28]  No, I don't remember that.
[2764.50 --> 2764.76]  Okay.
[2764.92 --> 2765.78]  Johnny, your turn.
[2765.90 --> 2766.64]  Two lives left.
[2766.76 --> 2767.20]  What do you think?
[2767.54 --> 2767.98]  AFK.
[2768.58 --> 2768.98]  AFK.
[2769.38 --> 2770.06]  Go for say.
[2771.66 --> 2772.86]  No, I'm afraid not.
[2772.86 --> 2774.78]  What are these abbreviations?
[2775.08 --> 2775.48]  AFK.
[2775.60 --> 2776.28]  Away from keyboard.
[2776.38 --> 2777.14]  You never use that one?
[2777.22 --> 2778.62]  Don't consider it abbreviations.
[2778.62 --> 2781.78]  No, I'm like, what do people think of abbreviations?
[2781.98 --> 2784.42]  If AFK, BRB, all of these are not there.
[2784.54 --> 2785.16]  What is this?
[2785.46 --> 2787.34]  They don't leave the keyboard.
[2787.68 --> 2788.00]  Johnny.
[2788.22 --> 2789.82]  You lose another life, I'm afraid.
[2790.00 --> 2791.54]  But don't worry, you still have another life.
[2791.72 --> 2793.14]  Chris, what do you think?
[2793.82 --> 2794.44]  Oh, goodness.
[2795.28 --> 2796.88]  Text abbreviations.
[2796.88 --> 2799.16]  I'm trying to think of ones that I actually use.
[2799.26 --> 2801.26]  I don't like abbreviate things very often.
[2801.64 --> 2803.12]  Brian's trying to help you, Chris.
[2803.32 --> 2804.38]  That's not allowed.
[2804.64 --> 2805.68]  Well, he's not on that team.
[2806.40 --> 2806.80]  Uh.
[2809.08 --> 2810.24]  Oh, OMG.
[2811.72 --> 2812.12]  OMG.
[2812.12 --> 2813.38]  It's got to be on there, right?
[2813.64 --> 2814.38]  Is that on there?
[2814.68 --> 2814.92]  No.
[2814.92 --> 2815.92]  OMG.
[2819.30 --> 2819.82]  OMG.
[2820.44 --> 2821.48]  How about WTF?
[2822.06 --> 2823.26]  Yeah, WTF.
[2823.52 --> 2825.46]  I'm afraid that is all your lives.
[2825.66 --> 2828.72]  I am starting to have serious concerns for this community.
[2829.04 --> 2829.68]  Let's steal.
[2829.90 --> 2831.26]  Yeah, it's time to steal.
[2831.42 --> 2831.64]  Yeah.
[2831.64 --> 2831.92]  Maybe.
[2832.20 --> 2833.00]  You're allowed to confer.
[2834.04 --> 2835.10]  So what do we think?
[2835.32 --> 2837.40]  Yeah, I was going to say WTF team.
[2837.62 --> 2837.78]  We should.
[2838.58 --> 2839.98]  WTF, JK.
[2840.72 --> 2844.90]  And the other one I was thinking is if we think about programmers is what about?
[2844.92 --> 2846.32]  LGTM.
[2846.64 --> 2847.94]  Those are two different things.
[2848.06 --> 2849.06]  EG is an example.
[2849.42 --> 2850.22]  I feel that too.
[2850.28 --> 2852.28]  And IE is a different thing.
[2852.44 --> 2852.78]  Yeah.
[2854.12 --> 2855.54]  I think it's WTF.
[2856.98 --> 2858.14]  Or TLDR.
[2858.14 --> 2860.30]  Everybody uses WTF.
[2860.86 --> 2864.08]  Well, people use OMG like crazy too.
[2864.28 --> 2865.64]  And why is that not on there?
[2865.86 --> 2866.82]  I know, I know, I know.
[2866.86 --> 2867.82]  But these are programmers.
[2868.02 --> 2873.58]  They're either going to tell people to RTFM or WTF all the time.
[2873.58 --> 2877.64]  I think it's either going to be like LGTM or LMAO.
[2878.02 --> 2880.52]  You guys, you have like five choices.
[2880.70 --> 2881.62]  Pick one and go.
[2881.96 --> 2883.08]  I want to see those boards.
[2883.68 --> 2883.92]  Yeah.
[2884.12 --> 2885.20]  Eric, what do you think?
[2886.00 --> 2887.08]  I think LGTM.
[2887.56 --> 2890.60]  All the other like random text ones are not here.
[2890.94 --> 2891.20]  Okay.
[2891.68 --> 2893.46]  Go for say to steal.
[2893.46 --> 2895.46]  Yes.
[2896.00 --> 2896.72]  You got one.
[2896.84 --> 2898.08]  At number three.
[2899.48 --> 2900.00]  LGTM.
[2900.76 --> 2904.28]  So team one steals those delicious points.
[2904.40 --> 2905.04]  Gobbles them down.
[2905.18 --> 2906.20]  Eats them all up.
[2906.66 --> 2907.06]  Nom nom.
[2907.52 --> 2908.28]  Let's see what else.
[2908.38 --> 2908.92]  Number six.
[2909.00 --> 2910.42]  We're going to go over the bottom first.
[2910.66 --> 2915.46]  Number six was people that don't use any abbreviations.
[2915.46 --> 2927.46]  They always use proper grammatical, you know, like well-structured sentences for all the
[2927.46 --> 2928.08]  things all the time.
[2928.28 --> 2928.58]  Absolutely.
[2928.86 --> 2929.80]  There's always a tweet.
[2930.00 --> 2930.90]  Find these people.
[2931.12 --> 2932.34]  Go through their Twitter accounts.
[2932.46 --> 2933.26]  I think they use them.
[2933.84 --> 2934.06]  Okay.
[2934.06 --> 2937.16]  Number five with six people said this.
[2938.44 --> 2938.88]  IIRC.
[2939.40 --> 2940.56]  Who knows what that means?
[2940.94 --> 2942.20]  If I recall correctly.
[2942.66 --> 2943.00]  Okay.
[2943.16 --> 2943.36]  Yeah.
[2943.36 --> 2943.74]  Very good.
[2943.74 --> 2946.46]  And I'm HO is going to be one probably then.
[2946.74 --> 2946.90]  Yeah.
[2947.04 --> 2947.64]  Number seven.
[2948.16 --> 2948.72]  We had.
[2948.82 --> 2949.02]  Sorry.
[2949.08 --> 2950.52]  Number four with seven people.
[2950.74 --> 2954.62]  IMO or I am HO in my humble opinion.
[2955.42 --> 2955.76]  Seven people.
[2955.94 --> 2956.12]  WTF.
[2956.24 --> 2957.02]  You got to have that right.
[2957.54 --> 2958.54]  And number two.
[2959.32 --> 2960.50]  Surprisingly EG.
[2962.32 --> 2962.80]  Example.
[2962.96 --> 2964.92]  Who the hell are these people?
[2965.26 --> 2967.02]  What is this?
[2967.32 --> 2968.18]  What is EG?
[2968.38 --> 2969.44]  Can somebody explain that to me?
[2969.44 --> 2970.32]  It means example.
[2970.42 --> 2970.84]  For example.
[2971.00 --> 2971.10]  Yeah.
[2971.10 --> 2971.40]  Yeah.
[2971.40 --> 2974.44]  Do we think that they were trolling us when they answered this?
[2974.62 --> 2975.30]  Well, we don't know.
[2975.42 --> 2976.16]  We'll never know.
[2976.24 --> 2977.16]  Why not IE?
[2977.28 --> 2979.38]  You would think I see more of that than EG.
[2979.56 --> 2980.28]  In other words.
[2980.40 --> 2980.62]  Right.
[2980.82 --> 2981.62]  You shouldn't.
[2981.88 --> 2982.52]  Oh, I shouldn't.
[2982.58 --> 2983.36]  I'm just saying I do.
[2983.36 --> 2984.96]  EG is more grammatically correct.
[2985.50 --> 2986.22]  Most of the time.
[2986.44 --> 2987.06]  I'm arguing.
[2987.24 --> 2987.46]  Yeah.
[2988.00 --> 2989.14]  Is it like IE?
[2989.58 --> 2990.88]  But in a different country?
[2991.14 --> 2991.86]  What is this?
[2992.16 --> 2995.72]  Well, IE is like an exact replacement where EG is like an example.
[2995.84 --> 2996.76]  But anyway, this doesn't matter.
[2996.88 --> 2997.50]  Let's move on.
[2997.50 --> 3001.12]  Well, the people that said they don't use them, they left us some comments.
[3001.24 --> 3004.36]  They said, I work in a multi-country development team.
[3004.54 --> 3007.34]  And I found that avoiding them is better for the team.
[3008.10 --> 3011.42]  And some people say that they're less clear if you don't already know what they mean.
[3011.50 --> 3012.26]  So they avoid them.
[3012.32 --> 3012.88]  They don't use them.
[3012.92 --> 3013.64]  And that's fair enough.
[3013.70 --> 3014.96]  That's their right.
[3015.16 --> 3016.72]  So they don't need a podcast.
[3016.74 --> 3018.94]  This is less than half the people, though.
[3019.08 --> 3020.40]  Where is the rest of the answers?
[3020.50 --> 3021.78]  I want to know what the weird ones were.
[3021.80 --> 3024.30]  No other answers had five.
[3024.30 --> 3027.42]  I was thinking E4K was considered an abbreviation.
[3027.62 --> 3028.20]  I mean, it is.
[3028.30 --> 3029.16]  But at this point...
[3029.16 --> 3030.14]  I don't have that data.
[3030.78 --> 3031.78]  Actually, that's a good question.
[3031.88 --> 3032.68]  I don't know that it is.
[3033.06 --> 3033.82]  Let's move on.
[3033.90 --> 3035.30]  We're in round four of 20.
[3035.62 --> 3036.60]  So I think we should...
[3036.60 --> 3038.20]  Yeah, we're not going to finish that.
[3038.36 --> 3039.18]  We've got six rounds.
[3039.24 --> 3039.60]  Don't worry.
[3039.60 --> 3048.50]  What's going on, Gophers?
[3048.58 --> 3051.30]  This episode is brought to you by Equinix Metal.
[3051.70 --> 3059.04]  If you want the choice and control of hardware with the overhead and the developer experience of the cloud, you need to check out Equinix Metal.
[3059.34 --> 3063.64]  Deploy in minutes across 18 global locations from Silicon Valley to Sydney.
[3063.64 --> 3068.92]  Visit metal.equinix.com slash just add metal and receive $100 in credit to play with.
[3069.16 --> 3072.36]  Again, metal.equinix.com slash just add metal.
[3072.36 --> 3091.36]  Our next round, we've given it a little bit of a twist.
[3091.60 --> 3094.36]  It's time for Unpopular Opinions.
[3095.30 --> 3095.70]  Ooh.
[3095.70 --> 3101.24]  Oh, Unpopular Opinion.
[3102.36 --> 3108.64]  Unpopular Opinions.
[3111.38 --> 3112.28]  There we go.
[3112.46 --> 3116.38]  A cappella edition of Unpopular Opinions there.
[3116.48 --> 3117.58]  A little treat for everyone.
[3117.72 --> 3118.52]  And I do mean treat.
[3118.76 --> 3119.32]  That isn't you.
[3119.54 --> 3120.42]  Who recorded that?
[3120.80 --> 3121.38]  Who was singing?
[3121.72 --> 3126.06]  That's me when I did the Unpopular Opinion theme tune and then someone took out all the music.
[3126.06 --> 3127.26]  Oh, hell no.
[3127.56 --> 3128.24]  That is not you.
[3128.26 --> 3128.86]  I love it.
[3129.08 --> 3129.96]  I love it.
[3130.22 --> 3131.08]  Is it true?
[3131.48 --> 3131.90]  Yeah, yeah.
[3131.90 --> 3132.44]  I love it.
[3132.52 --> 3133.10]  I love it.
[3133.16 --> 3133.44]  Really?
[3133.86 --> 3134.22]  Yeah.
[3134.22 --> 3136.70]  Man, he must have auto-tuned you like real good.
[3138.14 --> 3139.44]  Oh, excuse me?
[3140.74 --> 3141.04]  Ooh.
[3141.40 --> 3141.62]  Okay.
[3141.68 --> 3144.18]  Well, in this round, we've given it a little bit of a twist.
[3144.30 --> 3146.62]  We're actually looking for the bottom answers.
[3146.76 --> 3150.46]  The things that made it onto the board, but they weren't high scoring.
[3150.46 --> 3153.92]  So we're looking for the Unpopular Opinions this time.
[3154.60 --> 3160.96]  And the question is, if I weren't using Go to write code, I'd be using what?
[3161.52 --> 3162.86]  Oh, there's no face-off.
[3162.92 --> 3165.32]  We're just going to bounce between the teams.
[3165.32 --> 3167.66]  And we'll start with the trailing team.
[3168.66 --> 3170.46]  Brian, what do you think?
[3170.70 --> 3171.98]  I think you meant losers.
[3172.68 --> 3175.54]  I did not like that term, trailing team.
[3175.66 --> 3176.48]  I did not like that.
[3176.52 --> 3176.76]  Really?
[3176.84 --> 3177.84]  I thought that was a politer.
[3177.84 --> 3179.54]  I think Eric's term, losers.
[3179.56 --> 3182.76]  If you want to call us losers, call us losers.
[3183.22 --> 3183.58]  Okay?
[3184.40 --> 3185.90]  We didn't win the second round.
[3186.14 --> 3189.72]  I mean, you only won the second round because Matt cheated for you.
[3189.90 --> 3192.48]  So that's why you have all those points.
[3192.96 --> 3194.90]  If you got it the right way, we'd be ahead.
[3195.72 --> 3199.82]  Brian, why did we do this with a bunch of pedantic programmers?
[3199.82 --> 3200.98]  This was a terrible rest.
[3203.36 --> 3205.26]  All you did was follow the rules, Matt.
[3205.86 --> 3206.10]  Yeah.
[3206.34 --> 3206.68]  Sure.
[3206.68 --> 3208.32]  I can't follow the rules.
[3208.82 --> 3210.44]  Brian, what do we think?
[3210.74 --> 3211.50]  Show me Rust.
[3212.16 --> 3212.60]  Okay.
[3212.94 --> 3213.30]  Rust.
[3213.94 --> 3214.52]  Go for Say.
[3215.68 --> 3216.56]  Yes, indeed.
[3216.86 --> 3218.30]  But that's going to be popular.
[3218.80 --> 3219.58]  Yeah, quite popular.
[3219.88 --> 3221.56]  You get 10 points for it, though.
[3222.12 --> 3223.44]  Even though 24 people said it.
[3223.46 --> 3225.44]  It's in at number two, so it was quite popular.
[3225.86 --> 3227.00]  So we're looking for...
[3227.00 --> 3227.58]  Okay, yeah.
[3227.70 --> 3228.28]  That's it now.
[3228.28 --> 3231.66]  We're going to bounce over to Eric for a guess.
[3232.18 --> 3233.12]  Eric, what do you think?
[3233.66 --> 3234.06]  Pascal.
[3234.98 --> 3235.34]  Pascal.
[3235.98 --> 3236.44]  Go for Say.
[3236.68 --> 3238.04]  Did you say Haskell or Pascal?
[3238.04 --> 3238.46]  Oh, sorry.
[3238.54 --> 3239.00]  What did you say?
[3239.30 --> 3239.66]  Haskell.
[3239.90 --> 3240.30]  Haskell.
[3240.66 --> 3242.34]  Yeah, the initial sound was this.
[3242.48 --> 3242.86]  Haskell.
[3243.86 --> 3244.16]  Ah.
[3244.48 --> 3246.76]  Ah, Haskell is not on the board, I'm afraid.
[3247.38 --> 3248.72]  Carlicia, what do you think?
[3249.06 --> 3253.76]  Eric didn't get the gist that people can't run away from Pascal to come to go.
[3254.04 --> 3254.32]  Yeah.
[3254.32 --> 3257.38]  And if they didn't do go, they run away from Pascal to do something else.
[3257.38 --> 3261.34]  What don't they run away from then, Carlicia?
[3261.92 --> 3263.14]  What do you think they'd be using?
[3263.52 --> 3267.22]  I wanted to say YAML to be cheeky, but hold on, hold on, hold on.
[3267.22 --> 3267.50]  No.
[3267.50 --> 3268.52]  Don't lose us the points.
[3268.68 --> 3269.18]  Don't lose us.
[3269.18 --> 3269.50]  I know.
[3269.74 --> 3270.62]  I don't want to throw it away.
[3270.64 --> 3270.98]  No conferring.
[3271.20 --> 3271.82]  We need the points.
[3272.52 --> 3273.16]  Wait, can we confer?
[3273.48 --> 3274.04]  No conferring.
[3274.12 --> 3275.02]  Carlicia, what do you think?
[3275.24 --> 3276.40]  Python, Python, Python.
[3276.56 --> 3276.92]  Python.
[3277.20 --> 3277.96]  Okay, let's see.
[3278.90 --> 3279.84]  Go for say.
[3281.24 --> 3281.68]  Indeed.
[3282.18 --> 3282.44]  Ooh.
[3282.64 --> 3283.50]  But very popular.
[3283.64 --> 3284.00]  Wow.
[3284.12 --> 3284.60]  Number one.
[3284.60 --> 3285.30]  Oh yeah, okay.
[3285.58 --> 3287.40]  So you just get five points, but that's good.
[3287.82 --> 3289.04]  It all adds up.
[3289.28 --> 3290.86]  As long as you get points, you know.
[3291.48 --> 3294.46]  Okay, next up, we've got Natalie.
[3295.16 --> 3298.82]  Wait, why is Python five points and the other one is ten points?
[3298.92 --> 3299.54]  I don't get it.
[3299.62 --> 3302.76]  We're looking for unpopular opinions, so it's the opposite now.
[3302.96 --> 3303.24]  Oh.
[3303.24 --> 3305.30]  So the higher up it is, the fewer points there are.
[3305.30 --> 3306.88]  We're looking for the ones lower down the board.
[3307.24 --> 3311.64]  Number one, we have Python that's 26 people said, which earns you five points.
[3311.90 --> 3312.98]  Rust's in at number two.
[3313.10 --> 3316.88]  24 people said that, which gives you ten points, but they're still three, four, and five.
[3316.98 --> 3318.44]  They're the high-scoring ones.
[3319.00 --> 3320.58]  So Natalie, can you find one?
[3321.12 --> 3321.48]  Scala.
[3322.12 --> 3322.52]  Scala.
[3323.00 --> 3323.86]  Go for say.
[3326.06 --> 3329.02]  So it's an infinite number of points because it's not there?
[3329.02 --> 3329.48]  Ooh.
[3331.62 --> 3332.60]  There we go.
[3333.30 --> 3334.92]  No, it's a divide by zero error.
[3334.92 --> 3335.98]  Yay, we won.
[3336.40 --> 3337.84]  No, you'll win, yeah.
[3338.24 --> 3338.72]  Okay, Johnny.
[3339.14 --> 3339.42]  Yeah.
[3339.70 --> 3340.58]  Johnny, be good.
[3340.76 --> 3341.86]  Be good, mate, and get a one.
[3342.66 --> 3343.00]  Java.
[3343.80 --> 3344.20]  Java.
[3344.72 --> 3345.38]  Go for say.
[3347.22 --> 3348.10]  Yes, indeed.
[3348.62 --> 3349.26]  Where is it?
[3349.32 --> 3350.58]  It's at number three.
[3350.88 --> 3354.48]  Eight people said it, which gets you 15 delicious points.
[3355.18 --> 3355.82]  Very good.
[3356.32 --> 3357.60]  Mr. Bates is up next.
[3357.70 --> 3358.98]  I mean, Mark Bates.
[3359.46 --> 3360.02]  Mark Bates.
[3360.38 --> 3361.14]  What about Mark Bates?
[3361.34 --> 3362.08]  What do you think, mate?
[3362.38 --> 3365.50]  I'm going to go with .net.
[3365.92 --> 3366.56]  .net.
[3367.04 --> 3367.48]  Okay.
[3368.28 --> 3368.72]  .net.
[3368.92 --> 3369.58]  Go for say.
[3371.70 --> 3372.98]  Yes, we're going to give you that.
[3373.56 --> 3374.68]  People said C-sharp.
[3374.76 --> 3375.52]  Seven people did.
[3375.78 --> 3377.48]  Which gives you 20 points.
[3378.10 --> 3379.32]  What are you going to spend your points on, Mark?
[3379.40 --> 3379.82]  Don't answer.
[3379.96 --> 3380.66]  We've really got time.
[3381.38 --> 3383.08]  Next up, it's Chris's turn.
[3383.50 --> 3385.88]  Chris, can you get this last one?
[3386.38 --> 3387.24]  I'm going to say JavaScript.
[3388.20 --> 3388.68]  Are you?
[3388.68 --> 3390.32]  Well, let's see what the Gophers say.
[3392.80 --> 3393.20]  Excellent.
[3393.72 --> 3394.42]  You've done it.
[3394.48 --> 3395.36]  The top scorer.
[3395.48 --> 3399.04]  25 points there because five people said JavaScript.
[3399.60 --> 3400.28]  Very good.
[3401.04 --> 3401.08]  Nice.
[3401.08 --> 3402.06]  And check out this point.
[3402.06 --> 3402.34]  Wow.
[3402.74 --> 3404.12]  You're catching up, team two.
[3404.24 --> 3406.32]  It's not the end of the road yet.
[3406.84 --> 3407.72]  We've got another round.
[3407.84 --> 3409.50]  Does anyone want to just do some quick banter?
[3409.66 --> 3410.42]  It's got to be quick.
[3410.62 --> 3412.44]  You can just insult me quickly and get it out of the way.
[3413.26 --> 3414.20]  Matt, where's the rest of your hair?
[3414.46 --> 3417.70]  Johnny, in the land of the bold, the receded man is king.
[3417.70 --> 3421.84]  On the nose, Johnny.
[3421.98 --> 3422.16]  Really?
[3422.54 --> 3422.80]  Okay.
[3423.46 --> 3424.64]  It was super direct.
[3425.02 --> 3426.78]  You're ugly, Matt.
[3426.88 --> 3427.84]  I like to beat around a bush.
[3428.22 --> 3428.36]  Yeah.
[3428.56 --> 3428.88]  Nothing.
[3428.98 --> 3430.26]  I'm saying how wonderful you are.
[3431.26 --> 3432.36]  No, that was good bants.
[3432.84 --> 3433.44]  It's really good bants.
[3433.92 --> 3436.22]  Round six, though, we're playing for double points.
[3436.30 --> 3437.84]  We're back to playing the normal now.
[3437.90 --> 3440.36]  We're looking for the top scoring, but they're double points,
[3440.36 --> 3444.84]  which does give a nice opportunity to catch up here and overtake,
[3445.02 --> 3446.18]  and team two could win this.
[3446.18 --> 3449.38]  So let's go on to next round.
[3449.58 --> 3450.54]  It's round six.
[3453.24 --> 3453.84]  Okay.
[3454.80 --> 3457.44]  The question we asked our gophers is,
[3457.84 --> 3462.96]  the most useful package in the standard library is what?
[3463.76 --> 3468.42]  Now you can nominate who you want to go head-to-head from each team.
[3469.24 --> 3471.16]  Who's going to go head-to-head?
[3472.48 --> 3473.66]  I picked Johnny.
[3474.36 --> 3475.70]  Team one, who do we think?
[3476.70 --> 3479.96]  Team one is Eric, Natalie, Mark, and Angelica.
[3480.10 --> 3481.28]  Who out of those four?
[3482.32 --> 3483.68]  Natalie, Angelica.
[3484.12 --> 3484.68]  Eliza.
[3485.56 --> 3487.24]  Natalie's like, leave me out of it.
[3487.48 --> 3488.98]  Yeah, I was like, Eliza.
[3489.18 --> 3490.68]  You're going to be a team player, Natalie.
[3491.34 --> 3492.34]  Because you're singing Hamilton.
[3492.40 --> 3493.68]  No, no, I said Eliza.
[3493.68 --> 3494.94]  Oh, Eliza.
[3494.94 --> 3495.04]  Eliza.
[3495.44 --> 3496.68]  I was singing to them.
[3496.68 --> 3500.12]  I mean, I have an idea for what I think probably the top one is.
[3500.34 --> 3504.04]  We can't confer in an answer just on who is going to say it, right?
[3504.06 --> 3504.46]  That's right.
[3504.54 --> 3504.68]  Yeah.
[3505.00 --> 3505.40]  Okay.
[3505.46 --> 3508.36]  Well, if Eric thinks he has a top answer, I say we go there.
[3508.44 --> 3508.72]  Okay.
[3508.80 --> 3512.58]  Eric and Brian, who, from your team, Brian, Carlicia, Johnny, and Chris,
[3512.78 --> 3515.46]  who's going to be going head-to-head with Eric?
[3515.94 --> 3516.20]  Me.
[3516.84 --> 3517.16]  Sure.
[3517.42 --> 3517.58]  Yeah?
[3518.02 --> 3518.90]  Go, Carlicia.
[3518.96 --> 3519.46]  No, no, no.
[3519.48 --> 3520.00]  You guys go.
[3520.00 --> 3523.94]  I can think of one, but I think it's the same that Eric is thinking.
[3524.26 --> 3527.10]  So if somebody has, like, multiple ideas.
[3527.42 --> 3528.40]  I've got a good one, too.
[3528.62 --> 3529.00]  Yeah, go.
[3529.14 --> 3530.48]  Team two is going to go first.
[3530.76 --> 3532.96]  So, Carlicia, if you want to do it, you get to go first.
[3533.26 --> 3534.06]  Go, Carlicia.
[3534.08 --> 3534.50]  Brian, go.
[3534.60 --> 3534.76]  Go.
[3534.98 --> 3535.14]  What?
[3535.22 --> 3535.60]  Or Brian.
[3535.70 --> 3536.10]  Brian, go.
[3536.34 --> 3537.20]  I'll pick IO.
[3537.74 --> 3538.00]  No.
[3538.12 --> 3538.48]  IO.
[3538.96 --> 3539.28]  Okay.
[3539.60 --> 3540.20]  Go for Say.
[3541.78 --> 3542.98]  Oh, indeed, Brian.
[3543.36 --> 3543.72]  Indeed.
[3543.90 --> 3544.98]  IO is up there.
[3544.98 --> 3545.46]  Indeed.
[3545.70 --> 3552.20]  At number three, 14 people said that the IO package is the most useful package in the
[3552.20 --> 3552.84]  standard library.
[3553.00 --> 3554.80]  That earns you 28 delicious points.
[3555.50 --> 3556.10]  That's good.
[3556.46 --> 3556.70]  Okay.
[3557.40 --> 3559.62]  Next person is...
[3559.62 --> 3560.52]  Is that still team two?
[3560.82 --> 3561.72]  Team two, yes.
[3561.84 --> 3563.00]  Oh, then let me go.
[3563.06 --> 3563.32]  Let me go.
[3563.44 --> 3564.18]  It's not a face-off?
[3564.52 --> 3565.82]  We're bouncing back and forth.
[3566.16 --> 3566.94]  No, sorry, we're not.
[3567.52 --> 3569.08]  Eric, you now have to guess.
[3569.14 --> 3570.66]  And if you beat him, you take the board.
[3570.74 --> 3571.10]  That's right.
[3571.16 --> 3571.36]  All right.
[3571.36 --> 3573.10]  So, Eric, can you find one?
[3573.10 --> 3575.04]  I thought Brian was going to steal mine.
[3575.24 --> 3575.86]  Net HTTP.
[3576.58 --> 3577.74]  Net HTTP.
[3578.26 --> 3579.10]  Gophers say...
[3579.90 --> 3580.50]  For the steal.
[3581.00 --> 3581.52]  Yes.
[3581.82 --> 3582.56]  It's on there.
[3582.64 --> 3583.40]  But where is it?
[3583.72 --> 3584.76]  It's at the top.
[3584.94 --> 3585.14]  Oh.
[3585.14 --> 3591.26]  The most useful go package according to our surveyed gophers is Net HTTP.
[3592.10 --> 3596.50]  29 people said it and that earns you a delicious 58 points and control of the board.
[3596.88 --> 3601.00]  Which means, Natalie, it's your turn to choose the next one.
[3601.22 --> 3601.54]  Guess.
[3601.78 --> 3603.30]  Do a, you know, guess one.
[3603.78 --> 3603.98]  And that.
[3604.44 --> 3604.92]  F-M-T.
[3605.30 --> 3606.60]  Would you like to pronounce it properly?
[3607.12 --> 3607.36]  Nah.
[3607.36 --> 3610.12]  I did.
[3610.30 --> 3611.42]  If you don't, you'll lose the game.
[3612.98 --> 3613.42]  Natalie.
[3614.02 --> 3614.58]  Formatting one.
[3614.58 --> 3614.74]  Yeah.
[3614.94 --> 3615.24]  F-M-T.
[3615.54 --> 3617.20]  Let's see if F-M-T is up there.
[3617.30 --> 3617.94]  Go for say.
[3619.10 --> 3619.88]  Yes, indeed.
[3620.14 --> 3621.58]  And it's at number two.
[3622.02 --> 3622.90]  21 people.
[3623.12 --> 3623.74]  Oh, boy.
[3623.84 --> 3625.10]  That was the one that I was thinking.
[3625.32 --> 3626.10]  Great minds, Curtis.
[3626.28 --> 3626.36]  Yeah.
[3626.42 --> 3627.42]  Great minds, indeed.
[3627.86 --> 3629.90]  So, we've got Net HTTP at number one there.
[3630.10 --> 3632.08]  F-M-T at number two or F-M-T.
[3632.56 --> 3634.46]  At number three, we have the IO package.
[3634.54 --> 3636.12]  That leaves four and five open.
[3636.84 --> 3641.20]  And we're going to find out if Mark can figure one of those out.
[3641.28 --> 3642.02]  What do you think, Mark?
[3642.66 --> 3644.16]  I have a couple good guesses.
[3644.64 --> 3653.80]  But I'm going to go with one of the most important packages in the Go standard library that we cannot live without day to day.
[3653.90 --> 3655.54]  And that's the testing package.
[3655.92 --> 3656.28]  Beautiful.
[3656.50 --> 3656.80]  Beautiful.
[3657.04 --> 3657.44]  Testify.
[3657.90 --> 3658.32]  Let's see.
[3658.42 --> 3658.80]  Testing.
[3659.20 --> 3659.78]  Go for say.
[3659.78 --> 3662.60]  Yes, it's up there.
[3662.80 --> 3663.96]  And it's number four.
[3664.08 --> 3666.38]  That gives you a lovely 14 points.
[3666.64 --> 3668.20]  I think I know what the last one is, too.
[3668.54 --> 3671.24]  I think it's the other one I didn't say, I hope.
[3671.40 --> 3672.78]  Well, remember, there's no conferring.
[3673.02 --> 3675.68]  I have in mind one that I hope is the last one.
[3675.74 --> 3678.16]  If it isn't, I will find it weird.
[3678.52 --> 3679.36]  Okay, interesting.
[3679.46 --> 3681.90]  We'll find out from after what that is then, Colicia.
[3681.90 --> 3684.08]  But first of all, Angelica, it's your guess.
[3684.28 --> 3685.00]  Can you get it?
[3685.46 --> 3689.30]  What's the most useful Go package in the standard library?
[3689.56 --> 3690.20]  It's a lot of pressure.
[3690.72 --> 3691.72]  Do you still have all three points?
[3692.38 --> 3696.42]  I mean, my first thought was math just because I stopped doing math when I was 16.
[3696.42 --> 3699.14]  So I found that very useful because I can't do any of that.
[3699.96 --> 3701.46]  Mark's giving me a weird look.
[3703.10 --> 3704.08]  Maybe math.
[3706.58 --> 3708.00]  I think I'll go with math.
[3708.66 --> 3710.92]  As my teammates cry inside.
[3711.34 --> 3711.64]  Math.
[3711.80 --> 3712.84]  Okay, go for say.
[3714.04 --> 3715.48]  Oh, no, it's not there.
[3715.60 --> 3716.76]  You lose a life.
[3716.88 --> 3718.16]  But don't worry, you've got two lives left.
[3718.52 --> 3720.86]  And Eric, it's your turn to guess this last one.
[3721.34 --> 3726.06]  If you lose all three lives, of course, remember, the other team get an opportunity to steal this board.
[3726.06 --> 3728.34]  Based on usage, I think it's going to be strings.
[3729.00 --> 3729.44]  Strings.
[3729.60 --> 3730.14]  Go for say.
[3731.84 --> 3733.08]  No, I'm afraid not.
[3733.16 --> 3733.78]  You lose a life.
[3733.86 --> 3735.18]  You have one life left.
[3735.62 --> 3740.34]  And that life is in the hands of Natalie Pistinovich.
[3740.70 --> 3743.24]  Natalie, what's the final one?
[3743.28 --> 3744.02]  I get to confirm.
[3744.22 --> 3744.80]  I'm afraid not.
[3744.90 --> 3745.20]  No.
[3745.32 --> 3747.78]  You have to just do it all on your own.
[3748.30 --> 3749.26]  What would this be?
[3749.58 --> 3750.44]  What do you think, Natalie?
[3750.84 --> 3752.92]  I'm actually going to go with Angelica's hunch.
[3753.12 --> 3753.70]  Go with archive.
[3754.20 --> 3754.58]  Log.
[3755.10 --> 3755.50]  Log.
[3755.50 --> 3755.82]  Log.
[3755.82 --> 3756.50]  Okay, this is it.
[3756.54 --> 3757.12]  Your last life.
[3757.24 --> 3760.42]  Let's see if you get the board or give the other team a chance to steal.
[3760.68 --> 3761.76]  Is Log on the board?
[3761.88 --> 3762.50]  Go for say.
[3764.18 --> 3766.26]  No, I'm afraid not.
[3766.46 --> 3767.38]  So we have now.
[3767.48 --> 3768.14]  You can confer.
[3768.64 --> 3770.70]  Team two has a chance to steal.
[3771.20 --> 3771.72]  It's errors.
[3772.04 --> 3772.22]  Yeah.
[3772.30 --> 3774.34]  I think it's either errors or database.
[3774.66 --> 3775.46]  No, it's errors.
[3775.52 --> 3777.92]  That's because everybody's been reading Mark Bates' code.
[3780.66 --> 3781.36]  It's errors.
[3781.76 --> 3782.64]  Yeah, I'd agree.
[3782.86 --> 3783.64]  I'd say errors.
[3783.64 --> 3785.66]  If we're going to fail, let's fail unanimously.
[3786.00 --> 3786.30]  Sure.
[3786.72 --> 3787.06]  Okay.
[3787.60 --> 3789.96]  Before we move on, does anyone else want to be mean to Mark?
[3790.10 --> 3791.44]  Because that felt good for me.
[3792.40 --> 3794.10]  I want to agree with the other team.
[3794.22 --> 3795.28]  I think it's a good answer.
[3796.16 --> 3797.22]  What was the answer then?
[3797.74 --> 3798.10]  Errors.
[3798.34 --> 3798.70]  Errors.
[3798.88 --> 3799.24]  Errors.
[3799.24 --> 3799.90]  Let's see.
[3800.04 --> 3800.74]  Go for say.
[3802.16 --> 3802.60]  No.
[3802.82 --> 3803.18]  Okay.
[3803.60 --> 3804.00]  Okay.
[3804.16 --> 3804.68]  I'm out of here.
[3804.70 --> 3805.82]  Is it database sequel?
[3806.08 --> 3807.08]  That's what I think it is.
[3807.38 --> 3808.28]  That's what I was thinking.
[3808.62 --> 3809.02]  No.
[3809.60 --> 3810.66]  Can I take a guess?
[3810.84 --> 3811.08]  Yeah.
[3811.24 --> 3813.74]  I think it would be the sync package.
[3814.26 --> 3815.04]  Oh, interesting.
[3815.62 --> 3817.22]  The points are going to be awarded already.
[3817.56 --> 3818.40]  And let's have a look.
[3818.46 --> 3820.70]  What was that final one at number five?
[3821.16 --> 3823.66]  Most useful go package was indeed sync.
[3823.66 --> 3823.94]  Sync.
[3823.94 --> 3824.32]  Sync.
[3824.58 --> 3825.10]  Oh, wow.
[3825.36 --> 3825.60]  Yes.
[3825.62 --> 3826.68]  Five people said that.
[3826.76 --> 3829.38]  You can't do concurrency and go without it.
[3829.64 --> 3829.86]  Wait.
[3829.98 --> 3831.12]  What's in the sync package?
[3831.28 --> 3832.62]  I don't think I've ever used it.
[3833.88 --> 3834.86]  What am I missing?
[3835.26 --> 3837.48]  That's where mutex and weight group and everything are.
[3837.62 --> 3838.30]  Oh, right.
[3838.70 --> 3840.06]  You're missing some synchronization.
[3840.22 --> 3840.48]  Okay.
[3840.78 --> 3840.96]  Yeah.
[3841.18 --> 3843.14]  Sync wants a favorite of mine there.
[3843.22 --> 3845.16]  I think that's a cracking little function.
[3845.34 --> 3848.08]  It's an incredibly useful package, the sync package, I would say.
[3848.10 --> 3848.30]  Yeah.
[3848.30 --> 3849.16]  It's very good, isn't it?
[3849.40 --> 3850.28]  We have time.
[3850.44 --> 3852.42]  If we want to, we have a bonus round.
[3852.52 --> 3853.42]  If you want to keep going.
[3853.42 --> 3854.46]  One more round.
[3854.60 --> 3855.14]  Shall we do it?
[3855.28 --> 3855.74]  Let's do a bonus round.
[3855.80 --> 3856.24]  Let's go.
[3856.44 --> 3856.68]  Yeah.
[3856.86 --> 3857.58]  Let's do it then.
[3857.64 --> 3857.90]  Okay.
[3859.64 --> 3860.04]  Okay.
[3860.14 --> 3861.06]  So please nominate.
[3861.18 --> 3864.70]  Who's going to go head to head to decide who controls the board?
[3864.98 --> 3865.90]  Oh, Lord.
[3866.14 --> 3867.34]  What is this?
[3867.94 --> 3869.32]  Oh, I don't want to touch this one.
[3870.60 --> 3872.04]  I'm setting this one out.
[3873.08 --> 3877.86]  The question is, which popular development practice would you like to outlaw?
[3878.44 --> 3879.86]  There's going to be some hot takes on this one.
[3880.08 --> 3880.86]  They're going to be.
[3880.86 --> 3883.64]  There's going to be a lot of hot takes.
[3883.94 --> 3884.62]  Oh, let me go.
[3884.72 --> 3885.04]  Let me go.
[3885.12 --> 3885.54]  I have one.
[3885.82 --> 3886.34]  Come on, Mark.
[3886.64 --> 3887.12]  Are you happy?
[3887.52 --> 3887.96]  Team one?
[3888.14 --> 3888.38]  Okay.
[3888.80 --> 3889.82]  Hang yourself, Mark.
[3890.00 --> 3890.20]  Okay.
[3890.52 --> 3892.66]  Who from team two is going to go head to head with Mark?
[3893.02 --> 3893.30]  Brian?
[3893.66 --> 3894.58]  Anybody have anything good?
[3894.84 --> 3895.48]  I've got one.
[3895.78 --> 3896.24]  I don't.
[3896.30 --> 3896.72]  I don't.
[3897.32 --> 3899.08]  Sounds like it's you then, Brian.
[3899.38 --> 3899.72]  All right.
[3899.80 --> 3900.44]  I think it's Brian.
[3900.62 --> 3900.92]  Okay.
[3901.08 --> 3901.46]  All right.
[3901.52 --> 3902.12]  I'll have one.
[3902.12 --> 3902.44]  I have one.
[3902.44 --> 3902.92]  Oh, you got one?
[3903.00 --> 3903.32]  Okay, go.
[3903.40 --> 3903.56]  Yeah.
[3904.06 --> 3904.30]  Okay.
[3904.40 --> 3904.54]  Well.
[3904.64 --> 3905.12]  Me first?
[3905.28 --> 3907.98]  Well, yes, it is you first.
[3908.10 --> 3909.12]  Carly, what do you think?
[3909.44 --> 3909.80]  Agile.
[3909.80 --> 3910.16]  Agile.
[3910.28 --> 3910.72]  Agile.
[3910.80 --> 3911.60]  What a good answer.
[3911.72 --> 3913.10]  Let's see if it's on the board.
[3913.20 --> 3914.66]  That's a terrible answer.
[3916.52 --> 3917.44]  Oh, what?
[3917.66 --> 3918.38]  It's on the board.
[3918.82 --> 3920.24]  At number one.
[3921.46 --> 3922.62]  Number one, baby.
[3922.62 --> 3923.40]  Number one, 14 people.
[3923.64 --> 3927.82]  At number one said, I'd like to outlaw Agile Scrum or Sprints.
[3927.94 --> 3929.36]  Shot straight to my heart.
[3930.14 --> 3932.12]  That hurts me to my core.
[3932.18 --> 3933.56]  It wasn't me who said it.
[3933.64 --> 3934.38]  It was them.
[3934.38 --> 3939.12]  I was speaking on her own thoughts, just guessing what other people are saying.
[3939.18 --> 3940.28]  She just channeled it.
[3940.34 --> 3941.64]  This is also double points.
[3941.82 --> 3942.24]  For real?
[3942.36 --> 3944.64]  You would never know, but that's what I'm going with.
[3945.96 --> 3946.36]  Okay.
[3946.40 --> 3949.42]  That means team two takes control of the board.
[3950.22 --> 3953.24]  And Johnny, it's your turn to take the next guess.
[3953.78 --> 3954.84]  This is a tough one.
[3955.10 --> 3956.44]  It sure is.
[3956.80 --> 3958.14]  Can I come far with my teammates?
[3958.94 --> 3959.34]  No.
[3960.34 --> 3961.00]  It won't help you.
[3961.08 --> 3962.46]  The product manager is an R&D.
[3966.24 --> 3969.02]  Popular development practice you want to outlaw.
[3969.04 --> 3970.66]  Yeah, we've got four items on the board.
[3970.84 --> 3972.50]  Agile at number one has already been taken.
[3972.64 --> 3973.92]  Two, three, and four still up for grabs.
[3974.02 --> 3974.90]  Double points available.
[3975.44 --> 3976.00]  What do you think, Johnny?
[3976.40 --> 3978.26]  And this is going to be an unpopular opinion.
[3978.84 --> 3979.58]  Rolled into it.
[3980.12 --> 3980.32]  TDD.
[3981.60 --> 3981.64]  TDD.
[3982.48 --> 3983.68]  That is an unpopular opinion.
[3983.84 --> 3984.52]  Is it on the board?
[3984.62 --> 3985.20]  Gophers say.
[3986.76 --> 3987.54]  Holy smokes.
[3987.54 --> 3988.48]  Good job.
[3989.56 --> 3990.56]  At number two.
[3990.78 --> 3991.32]  Listen up.
[3991.66 --> 3994.24]  There are like four development practices.
[3994.38 --> 3996.30]  We're just going to go through one by one and that's it.
[3997.76 --> 4000.60]  We don't want any of them as a community, as an industry?
[4000.78 --> 4003.28]  No, I'm just saying that four is all there is.
[4003.68 --> 4004.62]  So we just list them.
[4005.56 --> 4006.40]  Maybe so.
[4006.52 --> 4007.10]  Let's find out.
[4007.18 --> 4010.06]  It's Chris's turn next to have a guess.
[4010.22 --> 4010.54]  Oh.
[4010.76 --> 4011.62]  No conferring, please.
[4011.70 --> 4016.88]  Chris, which popular development practice would our gophers like to outlaw, do you think?
[4017.56 --> 4019.76]  I'm going to say continuous delivery.
[4020.28 --> 4021.78]  Oh, continuous delivery.
[4021.94 --> 4022.66]  C-I-C-D.
[4022.86 --> 4023.58]  C-I-C-D.
[4023.74 --> 4024.28]  Gophers say.
[4025.42 --> 4026.38]  No, no.
[4026.68 --> 4028.22]  No, they didn't say that.
[4028.90 --> 4030.00]  That would be really controversial.
[4030.22 --> 4031.36]  So you lose a life, but that's okay.
[4031.44 --> 4032.16]  Two lives left.
[4032.20 --> 4034.06]  I mean, people want to get rid of TDD, so.
[4034.20 --> 4034.50]  I know.
[4034.60 --> 4035.64]  I can't believe TDD is on here.
[4035.76 --> 4037.08]  This is ridiculous.
[4037.08 --> 4037.44]  Oh.
[4037.44 --> 4039.54]  Give me their names.
[4039.72 --> 4040.02]  Brian.
[4040.28 --> 4041.08]  Well, Carly's.
[4041.24 --> 4041.64]  Oh, Brian.
[4041.72 --> 4042.20]  Brian's up.
[4042.20 --> 4043.70]  Yeah, Brian's your turn next.
[4044.14 --> 4045.26]  I have an idea.
[4046.04 --> 4048.12]  Is it time to confer if it is?
[4048.32 --> 4048.64]  I have an idea.
[4048.64 --> 4049.10]  No, not yet.
[4049.22 --> 4049.70]  Soon, though.
[4049.90 --> 4050.76]  Brian, what do you think?
[4051.30 --> 4051.98]  Pair programming.
[4052.58 --> 4053.50]  Pair programming.
[4053.50 --> 4054.74]  Oh, that's a good one.
[4055.06 --> 4055.72]  Gophers say.
[4057.24 --> 4058.08]  Yes, indeed.
[4058.14 --> 4058.86]  It's on there.
[4058.98 --> 4059.86]  And it's at number four.
[4060.00 --> 4063.22]  Five people said they would like to outlaw Pair programming.
[4063.48 --> 4066.74]  They sound very social, those people.
[4067.58 --> 4069.46]  Well, I'll have a go at you.
[4069.70 --> 4070.94]  If you don't like it, it's fine.
[4071.44 --> 4072.42]  That's good, isn't it?
[4072.48 --> 4073.42]  Ah, it's going well.
[4073.74 --> 4077.42]  So we've got one, two, and four taken.
[4077.60 --> 4079.24]  Just leaves number three to guess.
[4079.36 --> 4080.72]  Carlesia, it's your turn.
[4081.22 --> 4083.42]  Can you guess what's the final one?
[4083.50 --> 4084.34]  Two lives left.
[4084.92 --> 4086.76]  I have an idea, but is it time to confer?
[4087.44 --> 4087.84]  Can people?
[4087.94 --> 4088.14]  No.
[4088.26 --> 4088.50]  No?
[4088.68 --> 4088.90]  Okay.
[4088.98 --> 4089.92]  Just on your own, mate.
[4089.98 --> 4091.02]  Don't repeat yourself.
[4091.42 --> 4093.08]  Oh, I love that answer.
[4093.52 --> 4094.50]  Dry programming.
[4094.84 --> 4095.70]  Is it up there?
[4095.78 --> 4096.42]  Gophers say.
[4098.08 --> 4098.48]  Okay.
[4098.94 --> 4099.38]  It's all right.
[4099.40 --> 4100.74]  I'm afraid not.
[4100.88 --> 4101.20]  Good answer.
[4101.20 --> 4101.90]  They don't know better.
[4103.74 --> 4106.40]  You still have one life left.
[4106.82 --> 4108.74]  And it's, of course, Johnny.
[4108.84 --> 4109.86]  Background to Johnny.
[4110.34 --> 4111.78]  Johnny, final life.
[4111.90 --> 4112.20]  Goodness.
[4112.56 --> 4112.90]  Wow.
[4112.90 --> 4114.16]  I'm getting all the hard ones.
[4115.26 --> 4118.10]  Which popular development practice would you like to outlaw?
[4118.20 --> 4121.28]  We asked a hundred gophers which they would like to outlaw.
[4121.60 --> 4122.56]  What did they say?
[4123.18 --> 4124.10]  Wait, I can't confer?
[4124.72 --> 4126.18]  No, I'm afraid not.
[4126.24 --> 4126.92]  Only during a steal.
[4126.92 --> 4134.60]  I will say, I will say, I'll throw my hands up there and say extreme programming.
[4135.02 --> 4137.78]  Ooh, extreme programming.
[4137.92 --> 4138.52]  Gophers say.
[4139.82 --> 4141.18]  No, I'm afraid not.
[4141.32 --> 4143.44]  And that's your three lives expired.
[4143.80 --> 4147.18]  Which means it's an opportunity to steal.
[4147.18 --> 4151.28]  Well, so you can confer now, everybody else, to steal these points.
[4151.58 --> 4155.82]  And team one, Eric, Natalie, Mark, Angelica, what do you think could be the final answer?
[4155.82 --> 4159.96]  What do people think about coding tests during interviews?
[4160.58 --> 4162.98]  I don't know if that is a development practice.
[4163.32 --> 4163.60]  Yeah.
[4163.68 --> 4165.52]  Have we seen the rest of the answer?
[4166.20 --> 4167.90]  How about, like, reviews?
[4168.48 --> 4169.34]  That's fine.
[4169.54 --> 4170.14]  Or requests.
[4170.14 --> 4174.40]  Yeah, I wonder if it's something, like, software development lifecycle related, whether we're
[4174.40 --> 4180.46]  talking, like, Waterfall or Kanban or something, or whether it's, like, a configuration management
[4180.46 --> 4181.82]  infrastructure as code.
[4182.58 --> 4184.44]  Test coverage being 100%.
[4184.44 --> 4187.58]  I don't know the answer, so hopefully you're not trying to read my...
[4187.58 --> 4189.84]  Didn't you know I love studying body language?
[4190.44 --> 4191.68]  We've already figured it out.
[4191.86 --> 4192.12]  Oh.
[4192.62 --> 4193.26]  What is it then?
[4193.98 --> 4194.42]  Kanban.
[4194.92 --> 4196.38]  Kanban's not a bad choice.
[4196.38 --> 4202.16]  I'm still sick into my coding tests, because that is, unfortunately, a popular practice
[4202.16 --> 4203.44]  in the development world.
[4203.70 --> 4209.42]  And these questions do get conflated with other things, as we've seen, I guess.
[4209.86 --> 4210.14]  Yeah.
[4210.68 --> 4211.58]  And I could...
[4211.58 --> 4212.48]  Interviews...
[4212.48 --> 4214.38]  I don't know whether people will confuse it.
[4214.68 --> 4215.50]  I'm also not sure.
[4215.52 --> 4217.38]  Maybe, like, code reviews or something.
[4217.92 --> 4218.20]  Yeah.
[4218.90 --> 4221.38]  Code reviews are as ingrained...
[4222.08 --> 4224.20]  Almost as ingrained as Agile stuff.
[4224.20 --> 4230.18]  But semantic input versioning and modules count is something we'd like to outlaw.
[4230.84 --> 4232.50]  Adding some spice to this.
[4232.74 --> 4234.62]  Is that a really unpopular opinion?
[4234.86 --> 4236.42]  Should I not have said that?
[4237.06 --> 4238.36]  I can say what you like, mate.
[4238.54 --> 4240.58]  GoTime is the Wild West.
[4241.30 --> 4242.82]  Actually, I'd love an answer.
[4243.30 --> 4243.52]  Eric?
[4244.02 --> 4244.32]  All right.
[4244.52 --> 4246.86]  Who feels really confident about their answer?
[4246.86 --> 4251.16]  Because with the answers to all of these questions, I'm not feeling so confident.
[4251.16 --> 4251.60]  Yeah.
[4252.34 --> 4253.00]  Code reviews.
[4253.18 --> 4254.44]  Is that such a vital one?
[4254.54 --> 4259.60]  But recently, I've been put off with that when you lot all destroyed my reputation reviewing
[4259.60 --> 4260.72]  my code just then.
[4261.38 --> 4262.14]  That's true.
[4262.28 --> 4263.66]  Could this even just be meetings?
[4264.74 --> 4265.94]  I mean, maybe.
[4266.48 --> 4271.18]  Would people say that, I guess, if you asked what popular development practice would you like
[4271.18 --> 4271.80]  to outlaw?
[4271.80 --> 4277.60]  I say, we say code reviews or, or like, pull requests, slash, slash, slash, et cetera.
[4277.68 --> 4277.86]  Yeah.
[4278.26 --> 4279.44]  All clumped together.
[4280.28 --> 4281.54]  E-G-I-E.
[4281.74 --> 4282.16]  I agree.
[4282.34 --> 4283.40]  I think that's what it's going to be.
[4284.12 --> 4284.66]  Okay, Eric.
[4284.74 --> 4285.88]  So what's your final answer, please?
[4286.66 --> 4287.78]  Let's go with code reviews.
[4288.34 --> 4289.48]  We got enough points anyway.
[4289.76 --> 4289.98]  Okay.
[4290.04 --> 4290.64]  Code reviews.
[4291.06 --> 4292.56]  To steal the board.
[4292.86 --> 4293.80]  Gophers say...
[4294.56 --> 4295.78]  No.
[4295.78 --> 4297.14]  I'm afraid not.
[4297.34 --> 4299.16]  You have said, it has been said, the answer.
[4299.26 --> 4299.74]  Oh, no.
[4299.74 --> 4304.20]  Why don't we just quickly go around each person and you can have one final guess each?
[4304.46 --> 4305.18]  Starting with Johnny.
[4305.68 --> 4307.10]  Big design up front.
[4307.14 --> 4308.06]  Big design up front.
[4308.12 --> 4309.26]  I don't think anybody said that.
[4309.62 --> 4312.42]  No, Johnny, it has been said and that has not been said before.
[4313.10 --> 4313.36]  Yeah.
[4314.00 --> 4317.58]  The answer was waterfall 64.
[4318.06 --> 4318.92]  I'm sorry.
[4319.08 --> 4320.20]  That was the first thing I thought.
[4320.46 --> 4320.94]  Popular?
[4321.54 --> 4323.06]  Is waterfall really popular?
[4323.74 --> 4326.22]  I didn't realize people are still doing waterfall.
[4326.22 --> 4330.70]  I was going to say, you can't outlaw something that has already been outlawed.
[4331.66 --> 4335.02]  Why are there 64 respondents and only 12 points for that?
[4335.54 --> 4339.02]  I think that is a very good question, Brian.
[4339.74 --> 4340.14]  Jared.
[4342.80 --> 4344.36]  Let me get some clarity on that.
[4344.62 --> 4345.32]  We'll find out.
[4345.68 --> 4349.30]  It does kind of feel like waterfall would be at the very top of that list.
[4349.38 --> 4349.62]  Yeah.
[4349.78 --> 4350.28]  It may be.
[4350.28 --> 4353.04]  What would the 65 responses at all?
[4353.20 --> 4353.74]  It's a typo.
[4353.90 --> 4354.38]  It was six.
[4354.38 --> 4355.42]  Oh, it's six.
[4355.54 --> 4356.52]  I typo the number.
[4356.64 --> 4358.00]  I think we should win by default.
[4358.26 --> 4358.42]  Yeah.
[4358.66 --> 4359.00]  Okay.
[4359.08 --> 4360.68]  So six people said waterfall.
[4360.98 --> 4362.78]  So we had at number one, agile.
[4362.98 --> 4365.66]  Number two was TDD, BDD, or DDD.
[4366.50 --> 4369.70]  Waterfall at number three and pair programming at number four.
[4369.88 --> 4372.56]  I wouldn't necessarily have answered those that same way.
[4372.86 --> 4373.32]  Would you?
[4373.46 --> 4374.18]  Very interesting.
[4374.80 --> 4375.12]  Okay.
[4375.16 --> 4377.60]  So let's have a look at the final scores.
[4377.94 --> 4381.70]  Team two, 164 points.
[4381.70 --> 4385.84]  But team one taking the lead and the prize, which is nothing.
[4386.32 --> 4389.24]  You get, you had 341 points.
[4389.38 --> 4390.60]  Congratulations to team one.
[4392.76 --> 4394.48]  So that's it.
[4394.58 --> 4396.00]  That comes to the end.
[4396.18 --> 4399.26]  Oh, some other interesting answers to this before we move on.
[4399.64 --> 4403.00]  Somebody said never going to V1 was something they would like to outlaw.
[4403.00 --> 4406.62]  Somebody wrote disagreeing with me specifically.
[4408.78 --> 4410.12]  Quite an interesting answer there.
[4410.26 --> 4412.38]  Again, I'm going to say I think I was in that survey.
[4413.36 --> 4413.64]  Disqualified.
[4414.50 --> 4415.76]  Meetings was mentioned.
[4415.82 --> 4418.48]  He sounded a lot like my responses in a lot of cases.
[4418.72 --> 4420.26]  Did you actually answer the survey, Mark?
[4420.58 --> 4420.82]  No.
[4421.28 --> 4421.82]  No, he didn't.
[4421.90 --> 4422.02]  Good.
[4422.08 --> 4422.42]  Thank you.
[4422.68 --> 4422.82]  Yeah.
[4422.84 --> 4426.22]  It's just because it's hard to separate out the joke from the lie sometimes, isn't it?
[4426.30 --> 4426.58]  With you.
[4426.78 --> 4428.74]  But they're all pretty much one and the same.
[4429.34 --> 4430.42]  Joke and lie.
[4430.42 --> 4431.10]  They're all.
[4431.44 --> 4432.42]  Yeah, exactly.
[4432.48 --> 4433.40]  What's the difference these days?
[4433.56 --> 4434.64]  Post-truth world.
[4435.10 --> 4437.90]  Being super clever was another answer that we got.
[4438.16 --> 4439.94]  So we want to outlaw being super clever.
[4440.56 --> 4443.54]  Being super clever is not a development practice.
[4444.20 --> 4447.28]  The famous development practice of being a 10x.
[4447.36 --> 4448.56]  That's probably what they meant.
[4448.74 --> 4451.96]  But I like where your head is at, whoever said that.
[4452.20 --> 4457.24]  I think that means like a metaprogramming kind of thing is what they'd like to outlaw more than being clever.
[4457.38 --> 4460.30]  I think a better term would say outlaw metaprogramming, right?
[4460.30 --> 4465.90]  Like, and that kind of, you know, the Ruby stuff that you couldn't ever grab for in your code base.
[4466.16 --> 4466.36]  Yeah.
[4466.70 --> 4468.68]  I feel like hackathon should be on here.
[4468.84 --> 4469.62]  Should get rid of those.
[4470.22 --> 4471.30]  So lots of lovely opinions.
[4472.36 --> 4473.30]  Duck typing for programming.
[4474.58 --> 4475.30]  Should be outlawed.
[4476.22 --> 4478.80]  80 character limits on the line length.
[4479.94 --> 4480.36]  Come on then.
[4480.42 --> 4480.80]  Keep going.
[4480.92 --> 4481.40]  What do you hate?
[4481.82 --> 4483.24]  It's a therapy session now.
[4483.38 --> 4484.26]  Just get it off your chest.
[4484.38 --> 4484.64]  Yes.
[4485.72 --> 4486.30]  I like spaces.
[4487.06 --> 4488.16]  I'm not going to lie.
[4488.42 --> 4489.34]  I love spaces.
[4489.34 --> 4492.08]  My dad just replying with one word answers.
[4492.44 --> 4495.54]  Not having a color coded terminal should be out loud.
[4495.96 --> 4496.28]  Ooh.
[4496.52 --> 4496.92]  Hmm.
[4497.52 --> 4497.82]  Well.
[4498.12 --> 4498.52]  Spicy.
[4498.72 --> 4501.24]  We're way over time, but wasn't it worth it?
[4501.32 --> 4506.74]  Thank you so much for joining us on our special 200th episode.
[4507.54 --> 4508.02]  200th.
[4508.28 --> 4509.28]  Can anyone say that?
[4509.40 --> 4509.96]  200th?
[4510.06 --> 4510.54]  200th.
[4510.64 --> 4511.32]  Yes, we can.
[4511.48 --> 4512.62]  I think you'll leave out the D.
[4512.82 --> 4514.04]  Nobody has a problem with that.
[4514.04 --> 4514.80]  It's just you.
[4514.80 --> 4515.96]  You're not saying the D.
[4516.18 --> 4516.96]  It's just you, man.
[4517.20 --> 4517.38]  200th.
[4517.70 --> 4518.06]  200th.
[4518.38 --> 4519.22]  You've got to say the D.
[4519.72 --> 4520.08]  200th.
[4520.28 --> 4520.56]  Nope.
[4520.68 --> 4521.16]  Still wrong, man.
[4521.20 --> 4521.88]  Even I can.
[4522.00 --> 4523.30]  There's no D there.
[4523.42 --> 4524.44]  What is wrong with you?
[4524.80 --> 4525.28]  Is it not?
[4526.22 --> 4526.90]  200th?
[4526.90 --> 4529.96]  You could say it's 10 score if you really wanted to.
[4531.14 --> 4533.52]  It's an alternate way of getting you the same way.
[4533.72 --> 4534.18]  Same math.
[4535.06 --> 4536.00]  I can say that.
[4536.16 --> 4537.08]  I wish I'd thought of that.
[4537.12 --> 4538.68]  He's been in graduate school for too long.
[4538.68 --> 4541.40]  I'm trying to bring score back, you know?
[4541.54 --> 4542.66]  I'm two score in five.
[4542.88 --> 4544.68]  I don't mind admitting that.
[4544.94 --> 4547.38]  Two score in four episodes ago.
[4548.10 --> 4548.70]  Fortnightly.
[4548.94 --> 4552.18]  Yeah, you'll listen to this episode in a fortnightly time period.
[4553.00 --> 4554.76]  Isn't it fun language?
[4555.26 --> 4556.02]  Oh, isn't it?
[4556.20 --> 4557.16]  Yeah, I've had lots of fun.
[4557.16 --> 4559.60]  Can't text abbreviate fortnight, that's for sure.
[4560.22 --> 4561.12]  No, true.
[4561.38 --> 4562.38]  Just put two W.
[4563.08 --> 4566.96]  Okay, well, I want to say thank you again so much for coming.
[4566.96 --> 4573.12]  Brian Ketlson, Eric St. Martin, Colicia Thompson, the OG Go Time.
[4573.26 --> 4575.22]  It's great to get back together and hang out.
[4575.28 --> 4576.08]  I really do mean that.
[4576.14 --> 4577.04]  So thank you so much.
[4577.36 --> 4586.08]  And also we had Natalie Pistinovich, Chris Brando, Angelica Hill, Johnny Borsico, and of course, Mark Bates.
[4586.18 --> 4586.92]  I was Matt Raya.
[4587.26 --> 4588.24]  Thank you so much.
[4588.36 --> 4590.16]  Tell all your friends about Go Time if you want.
[4590.36 --> 4590.84]  See you later.
[4591.28 --> 4591.62]  Bye.
[4592.08 --> 4592.68]  Bye, everyone.
[4592.68 --> 4593.16]  Bye.
[4593.16 --> 4593.54]  Bye.
[4593.74 --> 4594.10]  Bye.
[4594.52 --> 4594.76]  Woo!
[4596.96 --> 4598.18]  All right.
[4598.38 --> 4601.78]  This has been our 200th episode extravaganza.
[4601.96 --> 4603.24]  Thank you for playing along with us.
[4603.56 --> 4607.40]  And if you were one of the 100 gophers who took the survey, a special thanks to you.
[4607.58 --> 4610.76]  The winner of that free Go Time t-shirt was Johan Braunhorst.
[4611.20 --> 4613.96]  That means 99 of you didn't win a shirt, but don't fret.
[4614.26 --> 4617.76]  You can always hook yourself up at gotime.fm slash merch.
[4618.20 --> 4620.50]  We are restocking inventory as I speak.
[4621.04 --> 4624.40]  Go Time is produced by Jared Santo with music by Breakmaster Cylinder.
[4624.40 --> 4627.66]  We are brought to you by Fastly, Launched Darkly, and Linode.
[4628.04 --> 4632.40]  Next week, Matt and Johnny are joined by Grant Seltzer-Richmond and Derek Parker.
[4632.68 --> 4635.24]  The topic of conversation, EBPF.
[4635.72 --> 4637.50]  Subscribe now so you don't miss it.
[4637.96 --> 4640.58]  That's what's coming up next time on Go Time.
[4640.58 --> 4665.72]  That was so stressful for me because of you lot.
[4665.80 --> 4667.56]  My Apple Watch told me to calm down.
[4668.00 --> 4669.20]  You did amazing, Matt.
[4669.20 --> 4670.50]  Tough crowd.
[4670.64 --> 4670.96]  Tough crowd.
[4670.96 --> 4671.38]  That was good.
[4671.74 --> 4673.06]  That was so much fun, though.
[4673.46 --> 4674.30]  Thank you so much.
[4674.42 --> 4677.84]  I feel like we can all agree that the real loser here was Matt.
[4678.84 --> 4681.54]  Thank you.
[4681.62 --> 4681.94]  Yes.
[4682.10 --> 4682.90]  Plus one on there.
[4683.26 --> 4684.56]  That is how it feels.
[4685.74 --> 4688.86]  I can't believe you guys hated the text abbreviation one so much.
[4688.90 --> 4689.42]  It's so simple.
[4689.56 --> 4691.44]  What's your most used text abbreviation?
[4691.64 --> 4693.80]  I mean, how much context do you need?
[4693.80 --> 4694.80]  What?
[4696.30 --> 4696.62]  What?
[4696.98 --> 4699.34]  Significant more amount of context, I think.
[4699.46 --> 4699.78]  Oh, really?
[4700.50 --> 4702.28]  What's your most used text abbreviation?
[4702.72 --> 4704.94]  Well, we thought this was a developer game show.
[4705.16 --> 4705.86]  Developers text?
[4706.28 --> 4706.72]  I know.
[4706.84 --> 4707.24]  It's weird.
[4707.52 --> 4709.20]  Well, LGTM was on it, wasn't it?
[4709.34 --> 4710.20]  Yeah, LGTM.
[4710.20 --> 4711.76]  Yeah, IMHO as well.
[4711.90 --> 4712.92]  I do see that a lot on GitHub.
[4713.24 --> 4713.64]  IRC.
[4713.70 --> 4715.00]  How is IMG not in there?
[4715.34 --> 4716.44]  People didn't say it.
[4716.50 --> 4716.88]  I don't know.
[4717.00 --> 4717.40]  I know.
[4717.52 --> 4718.12]  No kidding.
[4718.20 --> 4718.58]  No kidding.
[4718.58 --> 4719.92]  Game on!
